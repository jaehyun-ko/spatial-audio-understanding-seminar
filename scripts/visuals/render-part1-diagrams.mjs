#!/usr/bin/env node
/** Rasterize the original Part 1 SVGs with bundled fonts, without a Slidev server. */
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium } from 'playwright-chromium';

const root = fileURLToPath(new URL('../../', import.meta.url));
const options = { inputDir: path.join(root, 'public/diagrams'), outputDir: path.join(root, 'public/diagrams') };
for (let index = 2; index < process.argv.length; index++) {
  const flag = process.argv[index];
  if (flag === '--help' || flag === '-h') {
    console.log('Usage: node scripts/visuals/render-part1-diagrams.mjs [--input-dir DIR] [--output-dir DIR]\nDefaults to the repository public/diagrams directory. Relative overrides use the current directory.');
    process.exit(0);
  }
  const key = { '--input-dir': 'inputDir', '--output-dir': 'outputDir' }[flag];
  if (!key || !process.argv[index + 1] || process.argv[index + 1].startsWith('--'))
    throw new Error(`Unknown or incomplete argument: ${flag}`);
  options[key] = path.resolve(process.argv[++index]);
}

const files = (await fs.readdir(options.inputDir)).filter(name => /^p1-.*\.svg$/.test(name)).sort();
if (!files.length) throw new Error(`No Part 1 SVG diagrams found in ${options.inputDir}`);
const fontFaces = await Promise.all([
  [400, 'Regular'], [600, 'SemiBold'], [700, 'Bold'],
].map(async ([weight, style]) => {
  const data = await fs.readFile(path.join(root, `public/fonts/Pretendard-${style}.woff2`));
  return `@font-face{font-family:Pretendard;src:url(data:font/woff2;base64,${data.toString('base64')}) format('woff2');font-weight:${weight};font-style:normal;}`;
}));

await fs.mkdir(options.outputDir, { recursive: true });
const browser = await chromium.launch({ headless: true });
try {
  const page = await browser.newPage({ viewport: { width: 1136, height: 400 }, deviceScaleFactor: 2 });
  for (const file of files) {
    const svg = await fs.readFile(path.join(options.inputDir, file), 'utf8');
    await page.setContent(`<html><head><style>html,body{margin:0;}${fontFaces.join('')}</style></head><body>${svg}</body></html>`);
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: path.join(options.outputDir, file.replace(/\.svg$/, '.png')) });
  }
} finally {
  await browser.close();
}
console.log(`Rendered ${files.length} Part 1 PNGs to ${options.outputDir}`);
