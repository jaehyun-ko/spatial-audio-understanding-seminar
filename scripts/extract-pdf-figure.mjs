#!/usr/bin/env node
import fs from 'node:fs'
import path from 'node:path'
import { createHash } from 'node:crypto'
import { execFileSync } from 'node:child_process'

const help = `Extract an unchanged PDF figure as SVG with Poppler.

Usage:
  node scripts/extract-pdf-figure.mjs \\
    --pdf tmp/agg-design-source.pdf --page 2 --box 106,465,398,125 \\
    --out public/research/agg-rl-fig1.svg --source https://example.org/paper.pdf

Required:
  --pdf PATH       Existing local PDF; it is never modified.
  --page N         One-based page number.
  --box X,Y,W,H    Integer PDF points (1/72 inch), from the page's top left.
                   X/Y must be nonnegative and W/H positive. No screen pixels.
  --out PATH.svg   SVG destination. Its parent directory must already exist.
  --source URL     Original HTTP(S) source URL, recorded without downloading.

Options:
  --force          Explicitly allow replacing the SVG and its source sidecar.
  --help           Show this help.

Requires pdfinfo, pdfimages, and pdftocairo on PATH. Rotated pages are rejected
because this CLI uses unrotated page coordinates. Inspect the PDF page first.
The output is the exact pdftocairo SVG byte stream, with no SVG rewriting.
Poppler may outline text. Vector output can still contain raster <image> nodes.
The sidecar replaces .svg with .source.json and records hashes, source, crop,
the actual command, PDF raster inventory, and SVG image/path/use/text counts.

When a figure is an embedded raster image, prefer its native PNG/JPEG asset
over rendering the PDF page. First inspect: pdfimages -f N -l N -list input.pdf
Then extract native images into a new empty directory:
  pdfimages -f N -l N -all input.pdf empty-directory/figure
Select the matching image and preserve its attribution. An SVG wrapper does
not increase raster detail. Review the final crop visually before slide use.
`

function fail(message) {
  throw new Error(message)
}

function parseArgs(argv) {
  const options = {}
  const values = new Set(['--pdf', '--page', '--box', '--out', '--source'])
  for (let i = 0; i < argv.length; i++) {
    const key = argv[i]
    if (Object.hasOwn(options, key)) fail(`Duplicate option: ${key}`)
    if (key === '--help' || key === '--force') options[key] = true
    else if (values.has(key)) {
      const value = argv[++i]
      if (!value || value.startsWith('--')) fail(`Missing value for ${key}`)
      options[key] = value
    } else fail(`Unknown option: ${key}`)
  }
  if (options['--help']) return options
  for (const key of values) if (!options[key]) fail(`Required option: ${key}`)
  return options
}

function run(command, args) {
  try {
    return execFileSync(command, args, {
      shell: false,
      stdio: ['ignore', 'pipe', 'pipe'],
      env: { ...process.env, LC_ALL: 'C' },
      maxBuffer: 256 * 1024 * 1024,
      timeout: 120_000,
    })
  } catch (error) {
    if (error.code === 'ENOENT') fail(`Missing Poppler executable: ${command}`)
    const detail = error.stderr?.toString().trim() || error.message
    fail(`${command} failed: ${detail}`)
  }
}

const sha256 = bytes => createHash('sha256').update(bytes).digest('hex')
const sameFile = (a, b) => a.dev === b.dev && a.ino === b.ino

function inspectTarget(target, inputStat, force) {
  let stat
  try { stat = fs.lstatSync(target) }
  catch (error) {
    if (error.code === 'ENOENT') return
    throw error
  }
  if (stat.isSymbolicLink() || !stat.isFile()) fail(`Output must be a regular file, not a symlink or directory: ${target}`)
  if (sameFile(stat, inputStat)) fail(`Refusing to overwrite the input PDF: ${target}`)
  if (!force) fail(`Output already exists (use --force to replace): ${target}`)
}

function pageDetails(pdf, page) {
  const info = run('pdfinfo', [pdf]).toString()
  const pages = Number(info.match(/^Pages:\s+(\d+)\s*$/m)?.[1])
  if (!Number.isSafeInteger(pages) || pages < 1) fail('Could not read the PDF page count.')
  if (page > pages) fail(`Page ${page} is outside this ${pages}-page PDF.`)
  const selected = run('pdfinfo', ['-f', String(page), '-l', String(page), '-box', pdf]).toString()
  const number = '(-?\\d+(?:\\.\\d+)?)'
  const prefix = '(?:Page\\s+\\d+\\s+)?'
  const media = selected.match(new RegExp(`^${prefix}MediaBox:\\s+${number}\\s+${number}\\s+${number}\\s+${number}`, 'm'))
  const crop = selected.match(new RegExp(`^${prefix}CropBox:\\s+${number}\\s+${number}\\s+${number}\\s+${number}`, 'm'))
  const rotation = Number(selected.match(/^(?:Page\s+\d+\s+rot|Page rot):\s+(-?\d+)/m)?.[1])
  if (!media || !crop || !Number.isFinite(rotation)) fail('Could not read the selected page boxes and rotation.')
  if (rotation !== 0) fail(`Page rotation is ${rotation} degrees; rotated-page crop coordinates are not supported.`)
  const mediaBox = media.slice(1, 5).map(Number)
  return {
    count: pages,
    rotation,
    mediaBox,
    pdfCropBox: crop.slice(1, 5).map(Number),
    width: mediaBox[2] - mediaBox[0],
    height: mediaBox[3] - mediaBox[1],
  }
}

function writeOutputs(out, sidecar, svg, metadata, inputStat, force) {
  // Stage both files before touching either destination. No shell is involved.
  const staging = fs.mkdtempSync(path.join(path.dirname(out), '.extract-pdf-figure-'))
  const stagedSvg = path.join(staging, 'figure.svg')
  const stagedSource = path.join(staging, 'figure.source.json')
  const committed = []
  try {
    fs.writeFileSync(stagedSvg, svg, { flag: 'wx' })
    fs.writeFileSync(stagedSource, `${JSON.stringify(metadata, null, 2)}\n`, { flag: 'wx' })
    // Recheck after extraction; COPYFILE_EXCL also protects against new files.
    inspectTarget(out, inputStat, force)
    inspectTarget(sidecar, inputStat, force)
    for (const [from, to] of [[stagedSvg, out], [stagedSource, sidecar]]) {
      if (force) fs.renameSync(from, to)
      else fs.copyFileSync(from, to, fs.constants.COPYFILE_EXCL)
      committed.push(to)
    }
  } catch (error) {
    // Without --force, only files created by this invocation can be rolled back.
    if (!force) for (const target of committed) fs.unlinkSync(target)
    else if (committed.length) console.error(`Partial replacement: ${committed.join(', ')}. Retry to finish the pair.`)
    throw error
  } finally {
    for (const target of [stagedSvg, stagedSource]) {
      try { fs.unlinkSync(target) } catch (error) { if (error.code !== 'ENOENT') throw error }
    }
    fs.rmdirSync(staging)
  }
}

function main() {
  const options = parseArgs(process.argv.slice(2))
  if (options['--help']) return console.log(help)
  if (!/^[1-9]\d*$/.test(options['--page'])) fail('--page must be a positive integer.')
  const page = Number(options['--page'])
  if (!Number.isSafeInteger(page)) fail('--page is too large.')
  const parts = options['--box'].split(',').map(value => value.trim())
  if (parts.length !== 4 || parts.some(value => !/^\d+$/.test(value))) fail('--box must contain four nonnegative integers: X,Y,W,H.')
  const [x, y, width, height] = parts.map(Number)
  if ([x, y, width, height].some(value => !Number.isSafeInteger(value) || value > 2_147_483_647) || width === 0 || height === 0) {
    fail('--box needs nonnegative X/Y and positive W/H in the Poppler integer range.')
  }
  let source
  try { source = new URL(options['--source']) } catch { fail('--source must be an HTTP(S) URL.') }
  if (!['http:', 'https:'].includes(source.protocol)) fail('--source must be an HTTP(S) URL.')

  const pdf = fs.realpathSync(path.resolve(options['--pdf']))
  const inputStat = fs.statSync(pdf)
  if (!inputStat.isFile()) fail('--pdf must name a regular file.')
  const requestedOut = path.resolve(options['--out'])
  if (path.extname(requestedOut).toLowerCase() !== '.svg') fail('--out must end in .svg.')
  const parent = fs.realpathSync(path.dirname(requestedOut))
  if (!fs.statSync(parent).isDirectory()) fail('The output parent must be an existing directory.')
  const out = path.join(parent, path.basename(requestedOut))
  const sidecar = out.slice(0, -4) + '.source.json'
  const force = Boolean(options['--force'])
  inspectTarget(out, inputStat, force)
  inspectTarget(sidecar, inputStat, force)

  const inputHash = sha256(fs.readFileSync(pdf))
  const details = pageDetails(pdf, page)
  if (x + width > details.width + 0.01 || y + height > details.height + 0.01) {
    fail(`Crop ${parts.join(',')} exceeds the page MediaBox (${details.width} x ${details.height} pt).`)
  }
  const imageList = run('pdfimages', ['-f', String(page), '-l', String(page), '-list', pdf]).toString()
  const rasterItems = imageList.split(/\r?\n/).filter(line => /^\s*\d+\s+\d+\s+\S+\s+\d+\s+\d+\s/.test(line))
  const args = ['-svg', '-f', String(page), '-l', String(page), '-x', String(x), '-y', String(y),
    '-W', String(width), '-H', String(height), '-paperw', String(width), '-paperh', String(height),
    '-nocenter', '-noshrink', pdf, '-']
  const svg = run('pdftocairo', args)
  const xml = svg.toString('utf8')
  if (!/<svg\b/.test(xml) || !/<\/svg>\s*$/.test(xml)) fail('pdftocairo did not produce a complete SVG.')
  if (sha256(fs.readFileSync(pdf)) !== inputHash) fail('The input PDF changed during extraction; no outputs were written.')
  const counts = Object.fromEntries(['image', 'path', 'use', 'text'].map(tag =>
    [tag, (xml.match(new RegExp(`<(?:[\\w.-]+:)?${tag}\\b`, 'g')) || []).length]))
  const metadata = {
    schemaVersion: 1,
    sourceURL: options['--source'],
    inputPDF: { path: pdf, sha256: inputHash },
    outputSVG: { path: out, sha256: sha256(svg) },
    page,
    cropBox: { x, y, width, height, unit: 'PDF pt (1/72 inch)', origin: 'top-left of the unrotated page MediaBox' },
    pageGeometry: details,
    command: { executable: 'pdftocairo', args, shell: false, stdout: 'Saved byte-for-byte as outputSVG.path' },
    rasterInventory: { command: { executable: 'pdfimages', args: ['-f', String(page), '-l', String(page), '-list', pdf] }, pageItemCount: rasterItems.length, rows: rasterItems },
    svgElementCounts: counts,
    notes: [
      'The source PDF was read only. The SVG byte stream was not rewritten or optimized.',
      'Text may be outlined as paths and referenced with use elements; SVG does not guarantee editable text.',
      'SVG image elements may contain raster data; a vector wrapper does not add raster detail.',
      'The PDF CropBox may clip content within the requested MediaBox-relative rectangle.',
      'Inspect the final crop visually, including labels, legends, units, captions, and attribution.',
    ],
  }
  writeOutputs(out, sidecar, svg, metadata, inputStat, force)
  console.log(`SVG: ${out}\nSource record: ${sidecar}\nSVG elements: ${JSON.stringify(counts)}`)
  if (rasterItems.length || counts.image) console.warn('Raster content detected. For raster figures, prefer a native PNG/JPEG extracted with pdfimages -all; see --help.')
}

try { main() }
catch (error) {
  console.error(`extract-pdf-figure: ${error.message}`)
  process.exitCode = 1
}
