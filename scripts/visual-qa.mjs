#!/usr/bin/env node
/**
 * Read-only Slidev visual diagnostics using an isolated Playwright Chromium.
 * node scripts/visual-qa.mjs --url http://localhost:3035 --slides 42 --out tmp/design-before
 * --slides 42 means 1..42; --slides 1,4-9 selects individual slides/ranges.
 * Geometry findings are review candidates, not a verdict on visual quality.
 */
import { chromium } from 'playwright-chromium';
import { inspectDesign, EXPECTED } from './test-design-system.mjs';
import { mkdir, writeFile } from 'node:fs/promises';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

const HELP = `Usage: node scripts/visual-qa.mjs --url URL --slides COUNT|LIST --out DIRECTORY

  --url URL             Slidev base URL (default: http://localhost:3030)
  --slides 42           Inspect slides 1 through 42
  --slides 1,4-9        Inspect selected slide numbers
  --out DIRECTORY      Output folder (default: tmp/visual-qa)
  --timeout-ms 15000    Per-navigation/readiness timeout
  --settle-ms 200       Additional layout settling time
  --fail-on-warnings    Exit 1 for diagnostic findings, not just capture failures
  --help               Show this help

Writes slide-NN.png, report.json, and contact-sheet.html. Screenshots use a
1280x720 viewport and include Slidev global layers. Only visible current-slide
content is diagnosed. Text clipping/overlap checks are geometric heuristics;
CSS background assets, text inside raster images, and animation click states
are not exhaustively checked. No user browser/profile is accessed.
`;

export function parseArgs(argv) {
  const options = { url: 'http://localhost:3030', out: 'tmp/visual-qa', timeoutMs: 15000, settleMs: 200, failOnWarnings: false };
  for (let i = 0; i < argv.length; i++) {
    const flag = argv[i];
    if (flag === '--help' || flag === '-h') return { help: true };
    if (flag === '--fail-on-warnings') { options.failOnWarnings = true; continue; }
    const keys = { '--url': 'url', '--out': 'out', '--slides': 'slides', '--timeout-ms': 'timeoutMs', '--settle-ms': 'settleMs' };
    if (!keys[flag]) throw new Error(`Unknown option: ${flag}`);
    if (!argv[i + 1] || argv[i + 1].startsWith('--')) throw new Error(`Missing value for ${flag}`);
    options[keys[flag]] = argv[++i];
  }
  const url = new URL(options.url);
  if (!['http:', 'https:'].includes(url.protocol)) throw new Error('--url must use http or https');
  url.hash = '';
  options.url = url.href;
  if (!options.slides) throw new Error('--slides is required');
  const input = options.slides;
  const numbers = new Set();
  const addRange = (start, end) => {
    if (!Number.isSafeInteger(start) || !Number.isSafeInteger(end) || start < 1 || end < start || end > 10000)
      throw new Error(`Invalid slide range: ${start}-${end} (supported: 1..10000)`);
    for (let n = start; n <= end; n++) numbers.add(n);
  };
  if (/^\d+$/.test(input)) addRange(1, Number(input));
  else for (const item of input.split(',')) {
    const match = item.trim().match(/^(\d+)(?:-(\d+))?$/);
    if (!match) throw new Error(`Invalid slide selection: ${item}`);
    addRange(Number(match[1]), Number(match[2] ?? match[1]));
  }
  options.slides = [...numbers].sort((a, b) => a - b);
  for (const key of ['timeoutMs', 'settleMs']) {
    options[key] = Number(options[key]);
    if (!Number.isFinite(options[key]) || options[key] < (key === 'timeoutMs' ? 100 : 0))
      throw new Error(`Invalid ${key}`);
  }
  options.out = resolve(options.out);
  return options;
}

// Runs inside the page. Keep this function self-contained for locator.evaluate.
export function inspectSlide(root, { tolerance = 2 } = {}) {
  const ignoredSelector = '.global-page-number,.slidev-page-number,[data-visual-qa-ignore]';
  const annotationSelector = '.source,.note,.footnote,.citation,[data-source],[data-note]';
  const round = n => Math.round(n * 100) / 100;
  const rect = r => ({ x: round(r.x), y: round(r.y), width: round(r.width), height: round(r.height), right: round(r.right), bottom: round(r.bottom) });
  const box = root.getBoundingClientRect();
  const viewport = { x: 0, y: 0, right: innerWidth, bottom: innerHeight };
  const intersection = (a, b) => ({ width: Math.min(a.right, b.right) - Math.max(a.x, b.x), height: Math.min(a.bottom, b.bottom) - Math.max(a.y, b.y) });
  const intersects = (a, b) => { const size = intersection(a, b); return size.width > 0 && size.height > 0; };
  const outside = (a, b, x = true, y = true) => [
    x && a.x < b.x - tolerance && 'left', x && a.right > b.right + tolerance && 'right',
    y && a.y < b.y - tolerance && 'top', y && a.bottom > b.bottom + tolerance && 'bottom',
  ].filter(Boolean);
  const isShown = el => {
    if (el.closest(ignoredSelector) || el.closest('.katex-mathml')) return false;
    for (let p = el; p; p = p.parentElement) {
      const style = getComputedStyle(p);
      if (style.display === 'none' || style.visibility === 'hidden' || style.visibility === 'collapse' || Number(style.opacity) === 0 || style.contentVisibility === 'hidden') return false;
    }
    const r = el.getBoundingClientRect();
    return r.width > 0 && r.height > 0;
  };
  const selector = el => {
    if (el === root) return '.slidev-layout';
    const path = [];
    for (let p = el; p && p !== root && path.length < 5; p = p.parentElement) {
      let part = p.tagName.toLowerCase();
      if (p.id) { path.unshift(`${part}#${CSS.escape(p.id)}`); break; }
      if (p.classList.length) part += [...p.classList].slice(0, 3).map(c => `.${CSS.escape(c)}`).join('');
      const peers = p.parentElement ? [...p.parentElement.children].filter(e => e.tagName === p.tagName) : [];
      if (peers.length > 1) part += `:nth-of-type(${peers.indexOf(p) + 1})`;
      path.unshift(part);
    }
    return path.join(' > ');
  };
  const sample = el => (el.innerText || el.textContent || el.getAttribute('alt') || '').replace(/\s+/g, ' ').trim().slice(0, 200);
  const describe = el => ({ selector: selector(el), text: sample(el), rect: rect(el.getBoundingClientRect()) });
  const annotation = el => {
    const candidate = el.closest(annotationSelector);
    return candidate && root.contains(candidate) ? candidate : null;
  };
  const elements = [...root.querySelectorAll('*')].filter(el => !el.closest('svg') && isShown(el));
  const outsideSlide = [];
  for (const el of elements) {
    const hasText = [...el.childNodes].some(node => node.nodeType === Node.TEXT_NODE && node.textContent.trim());
    if (!hasText && !el.matches('img,video,canvas,table,hr')) continue;
    const edges = outside(el.getBoundingClientRect(), box);
    if (edges.length) outsideSlide.push({ ...describe(el), edges, annotation: Boolean(annotation(el)) });
  }
  // An SVG is one visual asset; SVG path/text geometry needs a separate audit.
  for (const el of root.querySelectorAll('svg')) {
    if (!isShown(el) || el.parentElement?.closest('svg')) continue;
    const edges = outside(el.getBoundingClientRect(), box);
    if (edges.length) outsideSlide.push({ ...describe(el), edges });
  }
  const images = [...root.querySelectorAll('img')].filter(el => isShown(el) && intersects(el.getBoundingClientRect(), box) && intersects(el.getBoundingClientRect(), viewport));
  const missingImages = images.filter(el => !el.complete || el.naturalWidth === 0).map(el => ({
    ...describe(el), src: el.currentSrc || el.src, complete: el.complete, naturalWidth: el.naturalWidth,
  }));
  const videos = [...root.querySelectorAll('video')].filter(el => isShown(el) && intersects(el.getBoundingClientRect(), box) && intersects(el.getBoundingClientRect(), viewport));
  const missingVideos = videos.filter(el => el.readyState < 1 || !el.videoWidth || !el.videoHeight).map(el => ({
    ...describe(el), src: el.currentSrc || el.src, readyState: el.readyState, videoWidth: el.videoWidth, videoHeight: el.videoHeight,
  }));
  const textFragments = [];
  const clipped = new Map();
  const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
  while (walker.nextNode()) {
    const node = walker.currentNode;
    const el = node.parentElement;
    if (!node.textContent.trim() || !el || el.closest('svg,script,style') || !isShown(el)) continue;
    const range = document.createRange();
    const leading = node.textContent.length - node.textContent.trimStart().length;
    range.setStart(node, leading);
    range.setEnd(node, node.textContent.trimEnd().length);
    const fragments = [...range.getClientRects()].filter(r => r.width > 0 && r.height > 0);
    const clipBounds = [];
    for (let p = el; p && root.contains(p); p = p.parentElement) {
      const style = getComputedStyle(p);
      const clipsX = /^(hidden|clip|scroll|auto)$/.test(style.overflowX);
      const clipsY = /^(hidden|clip|scroll|auto)$/.test(style.overflowY);
      if (!clipsX && !clipsY && p !== root) continue;
      const bounds = p.getBoundingClientRect();
      const sx = p.offsetWidth ? bounds.width / p.offsetWidth : 1;
      const sy = p.offsetHeight ? bounds.height / p.offsetHeight : 1;
      clipBounds.push({ el: p, x: clipsX || p === root, y: clipsY || p === root, bounds: {
        x: bounds.x + p.clientLeft * sx, y: bounds.y + p.clientTop * sy,
        right: bounds.x + (p.clientLeft + p.clientWidth) * sx,
        bottom: bounds.y + (p.clientTop + p.clientHeight) * sy,
      } });
    }
    for (const fragment of fragments) {
      textFragments.push({ el, annotation: annotation(el), rect: fragment });
      for (const clip of clipBounds) {
        const edges = outside(fragment, clip.bounds, clip.x, clip.y);
        if (!edges.length) continue;
        const key = `${selector(el)}::${selector(clip.el)}`;
        if (!clipped.has(key)) clipped.set(key, { ...describe(el), clippedBy: selector(clip.el), edges: [], textRects: [] });
        const entry = clipped.get(key);
        entry.edges = [...new Set([...entry.edges, ...edges])];
        if (entry.textRects.length < 5) entry.textRects.push(rect(fragment));
      }
    }
  }
  const visuals = [...root.querySelectorAll('img,svg,canvas,video')].filter(el => isShown(el) && !el.parentElement?.closest('svg')).map(el => ({ el, annotation: annotation(el), rect: el.getBoundingClientRect() }));
  const overlaps = new Map();
  for (const a of textFragments.filter(item => item.annotation)) {
    for (const b of [...textFragments, ...visuals]) {
      if (a.el === b.el || a.annotation === b.annotation || a.annotation.contains(b.el) || b.el.contains(a.el)) continue;
      if (!intersects(a.rect, box) || !intersects(b.rect, box)) continue;
      const size = intersection(a.rect, b.rect);
      if (size.width <= tolerance || size.height <= tolerance) continue;
      const labels = [selector(a.annotation), selector(b.annotation || b.el)].sort();
      const key = labels.join('::');
      if (!overlaps.has(key)) overlaps.set(key, {
        annotation: describe(a.annotation), other: describe(b.annotation || b.el),
        intersection: { width: round(size.width), height: round(size.height) },
        kind: b.annotation ? 'annotation-annotation' : 'annotation-content',
      });
    }
  }
  const headings = [...root.querySelectorAll('h1,h2,h3')].filter(isShown).map(el => el.innerText.replace(/\s+/g, ' ').trim());
  const footer = [...document.querySelectorAll('.global-page-number')].filter(el => {
    const r = el.getBoundingClientRect();
    return r.width > 0 && r.height > 0 && getComputedStyle(el).visibility !== 'hidden';
  }).map(el => ({ text: sample(el), rect: rect(el.getBoundingClientRect()) }));
  return {
    title: headings[0] || sample(root).slice(0, 100), headings,
    actualSlide: Number(root.closest('[data-slidev-no]')?.getAttribute('data-slidev-no')) || null,
    slideRect: rect(box), slideOutsideViewport: outside(box, viewport),
    unrenderedMarkup: root.innerText.includes('**') ? ['literal bold delimiters in rendered text'] : [],
    visibleImageCount: images.length, visibleVideoCount: videos.length, missingImages, missingVideos, outsideSlide,
    textClipping: [...clipped.values()], annotationOverlaps: [...overlaps.values()],
    globalPageNumbers: footer,
  };
}

const escapeHtml = value => String(value ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]);

function contactSheet(report) {
  const cards = report.slides.map(slide => {
    const messages = [slide.error, ...(slide.unrenderedMarkup || []), slide.designIssues?.length && `${slide.designIssues.length} frame/type findings`, ...(slide.readinessWarnings || []),
      slide.missingImages?.length && `${slide.missingImages.length} missing images`,
      slide.missingVideos?.length && `${slide.missingVideos.length} missing videos`,
      slide.outsideSlide?.length && `${slide.outsideSlide.length} outside elements`,
      slide.textClipping?.length && `${slide.textClipping.length} text clips`,
      slide.annotationOverlaps?.length && `${slide.annotationOverlaps.length} source/note overlaps`,
      slide.slideOutsideViewport?.length && 'slide exceeds viewport',
    ].filter(Boolean);
    return `<article id="slide-${slide.number}" class="${messages.length ? 'flagged' : ''}"><h2>${slide.number}. ${escapeHtml(slide.title || 'Capture failed')}</h2>${slide.screenshot ? `<a href="${escapeHtml(slide.screenshot)}" target="_blank"><img src="${escapeHtml(slide.screenshot)}" alt="Slide ${slide.number}" loading="lazy"></a>` : '<div class="missing">No screenshot</div>'}<p>${messages.length ? messages.map(escapeHtml).join(' · ') : 'No automated findings'}</p><details><summary>Diagnostics</summary><pre>${escapeHtml(JSON.stringify(slide, null, 2))}</pre></details></article>`;
  }).join('\n');
  return `<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Slidev visual QA</title><style>
*{box-sizing:border-box}body{margin:0;padding:28px;background:#ecebea;color:#242424;font:16px/1.45 system-ui,sans-serif}header{margin-bottom:24px}h1{font-size:26px;margin:0 0 8px}header p{margin:4px 0;color:#555}.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px}article{background:white;border:1px solid #d1d1d1;padding:12px;min-width:0}article.flagged{border-color:#b05739}h2{font-size:17px;font-weight:600;margin:0 0 10px;min-height:25px}img{display:block;width:100%;height:auto;aspect-ratio:16/9;object-fit:contain;background:#222}article p{font-size:13px;margin:10px 0;color:#555}details{font-size:13px}pre{white-space:pre-wrap;overflow-wrap:anywhere;max-height:450px;overflow:auto}.missing{aspect-ratio:16/9;display:grid;place-items:center;background:#ddd}@media(min-width:2400px){.grid{grid-template-columns:repeat(3,minmax(0,1fr))}}@media(max-width:950px){.grid{grid-template-columns:1fr}}@media print{body{background:white;padding:0}.grid{gap:8px}article{break-inside:avoid}details{display:none}}
</style><header><h1>Slidev visual QA</h1><p>${escapeHtml(report.url)} · ${report.slides.length} slides · 1280 × 720</p><p>${escapeHtml(report.generatedAt)} · ${report.summary.captureErrors} capture errors · ${report.summary.slidesWithFindings} slides with review candidates · ${report.summary.runtimeErrors} runtime errors · ${report.summary.runtimeWarnings} environment warnings</p><p>Open an image for full resolution. Geometric checks do not establish readability or scientific accuracy.</p>${report.fatalError ? `<p>Capture failed: ${escapeHtml(report.fatalError)}</p>` : ''}<a href="report.json">JSON report</a></header><main class="grid">${cards}</main></html>`;
}

async function ready(page, layout, options) {
  const warnings = await layout.evaluate(async (root, timeoutMs) => {
    const warnings = [];
    async function bounded(promise, label) {
      let timer;
      try { await Promise.race([promise, new Promise((_, reject) => { timer = setTimeout(() => reject(new Error(label)), timeoutMs); })]); }
      catch { warnings.push(label); }
      finally { clearTimeout(timer); }
    }
    await bounded(document.fonts.ready, 'Fonts did not settle before timeout');
    const images = [...root.querySelectorAll('img')].filter(img => {
      const r = img.getBoundingClientRect();
      return r.width && r.height && r.right > 0 && r.bottom > 0 && r.x < innerWidth && r.y < innerHeight && getComputedStyle(img).visibility !== 'hidden';
    });
    await bounded(Promise.all(images.map(img => img.complete ? img.decode().catch(() => {}) : new Promise(resolve => {
      img.addEventListener('load', resolve, { once: true });
      img.addEventListener('error', resolve, { once: true });
    }))), 'Visible images did not settle before timeout');
    const videos = [...root.querySelectorAll('video')].filter(video => {
      const r = video.getBoundingClientRect();
      return r.width && r.height && r.right > 0 && r.bottom > 0 && r.x < innerWidth && r.y < innerHeight && getComputedStyle(video).visibility !== 'hidden';
    });
    await bounded(Promise.all(videos.map(video => video.readyState >= 1 ? Promise.resolve() : new Promise(resolve => {
      video.addEventListener('loadedmetadata', resolve, { once: true });
      video.addEventListener('error', resolve, { once: true });
    }))), 'Visible videos did not settle before timeout');
    await new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)));
    return warnings;
  }, options.timeoutMs);
  if (options.settleMs) await page.waitForTimeout(options.settleMs);
  return warnings;
}

export async function run(options) {
  await mkdir(options.out, { recursive: true });
  const report = {
    schemaVersion: 1, generatedAt: new Date().toISOString(), url: options.url,
    viewport: { width: 1280, height: 720 }, requestedSlides: options.slides,
    limitations: ['Geometry findings require visual review.', 'Global page numbers are recorded but excluded from content overlap checks.', 'Intentional source/note positioning is allowed; intersecting text/visual bounds are review candidates.', 'Only the initial click state is captured.', 'CSS background images, raster-internal text, SVG-internal clipping, and arbitrary body-body overlaps are not exhaustively checked.'],
    slides: [], runtimeErrors: [], runtimeWarnings: [],
  };
  let browser;
  let activeSlide = null;
  try {
    browser = await chromium.launch({ headless: true });
    const context = await browser.newContext({ viewport: report.viewport, deviceScaleFactor: 1, reducedMotion: 'reduce' });
    const page = await context.newPage();
    page.setDefaultTimeout(options.timeoutMs);
    page.on('pageerror', error => {
      // Headless Chromium cannot keep a physical display awake. Preserve this
      // environmental warning without classifying successful captures as failed.
      const collection = /wake lock.*permission.*denied/i.test(error.message) ? report.runtimeWarnings : report.runtimeErrors;
      collection.push({ slide: activeSlide, message: error.message });
    });
    for (const number of options.slides) {
      activeSlide = number;
      // Full navigation avoids stale text paints while Slidev changes hash routes.
      const captureUrl = new URL(options.url);
      captureUrl.searchParams.set('qa-slide', String(number));
      captureUrl.hash = `/${number}`;
      const result = { number, url: captureUrl.href };
      try {
        await page.goto(result.url, { waitUntil: 'domcontentloaded', timeout: options.timeoutMs });
        await page.mouse.move(1, 1);
        await page.waitForFunction(number => {
          const layouts = [...document.querySelectorAll('.slidev-page .slidev-layout, #slideshow .slidev-layout')];
          return layouts.some(el => {
            const r = el.getBoundingClientRect();
            const no = el.closest('[data-slidev-no]')?.getAttribute('data-slidev-no');
            return (!no || Number(no) === number) && r.width > 0 && r.height > 0 && r.right > 0 && r.bottom > 0 && r.x < innerWidth && r.y < innerHeight && getComputedStyle(el).visibility !== 'hidden';
          });
        }, number);
        let layout = page.locator(`.slidev-page[data-slidev-no="${number}"] .slidev-layout:visible`).first();
        if (!await layout.count()) layout = page.locator('#slideshow .slidev-layout:visible').first();
        if (!await layout.count()) throw new Error(`No visible layout for slide ${number}`);
        result.readinessWarnings = await ready(page, layout, options);
        Object.assign(result, await layout.evaluate(inspectSlide));
        if (await layout.evaluate(el => el.classList.contains('seminar'))) {
          const design = await layout.evaluate(inspectDesign, EXPECTED);
          result.designIssues = design.issues;
          result.lineCounts = design.lineCounts;
        }
        if (result.actualSlide !== null && result.actualSlide !== number) throw new Error(`Requested slide ${number}, rendered ${result.actualSlide}`);
        const screenshot = `slide-${String(number).padStart(2, '0')}.png`;
        await page.screenshot({ path: resolve(options.out, screenshot), animations: 'disabled', fullPage: false });
        result.screenshot = screenshot;
      } catch (error) {
        result.error = error.message;
      }
      result.findingCount = (result.unrenderedMarkup?.length || 0) + (result.designIssues?.length || 0) + (result.missingImages?.length || 0) + (result.outsideSlide?.length || 0) + (result.textClipping?.length || 0) + (result.annotationOverlaps?.length || 0) + (result.readinessWarnings?.length || 0) + (result.slideOutsideViewport?.length ? 1 : 0);
      report.slides.push(result);
      console.log(`Slide ${number}: ${result.error ? `ERROR ${result.error.split('\n')[0]}` : `${result.findingCount} review candidates — ${result.title}`}`);
    }
  } catch (error) {
    report.fatalError = error.message;
  } finally {
    if (browser) await browser.close().catch(error => { report.runtimeErrors.push({ message: `Browser close: ${error.message}` }); });
  }
  report.summary = {
    requested: options.slides.length, captured: report.slides.filter(s => s.screenshot).length,
    captureErrors: report.slides.filter(s => s.error).length + (report.fatalError ? 1 : 0),
    slidesWithFindings: report.slides.filter(s => s.findingCount > 0).length,
    findings: report.slides.reduce((sum, s) => sum + s.findingCount, 0),
    runtimeErrors: report.runtimeErrors.length, runtimeWarnings: report.runtimeWarnings.length,
  };
  await writeFile(resolve(options.out, 'report.json'), `${JSON.stringify(report, null, 2)}\n`);
  await writeFile(resolve(options.out, 'contact-sheet.html'), contactSheet(report));
  console.log(`Report: ${resolve(options.out, 'report.json')}`);
  console.log(`Contact sheet: ${resolve(options.out, 'contact-sheet.html')}`);
  if (report.fatalError) console.error(report.fatalError);
  return { report, exitCode: report.summary.captureErrors || report.summary.runtimeErrors || (options.failOnWarnings && report.summary.findings) ? 1 : 0 };
}

if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) {
  try {
    const options = parseArgs(process.argv.slice(2));
    if (options.help) console.log(HELP);
    else process.exitCode = (await run(options)).exitCode;
  } catch (error) {
    console.error(`visual-qa: ${error.message}\nRun with --help for usage.`);
    process.exitCode = 1;
  }
}
