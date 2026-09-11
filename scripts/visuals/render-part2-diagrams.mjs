#!/usr/bin/env node
/** Reproduce the final Part 2 delivery PNGs using pinned Playwright Chromium.
 * node scripts/visuals/render-part2-diagrams.mjs
 * Optional --input-dir / --output-dir permit rendering into a staging directory.
 */
import { chromium } from 'playwright-chromium';
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const repo = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const options = { inputDir: path.join(repo, 'public/diagrams'), outputDir: path.join(repo, 'public/diagrams') };
for (let i = 2; i < process.argv.length; i++) {
  const key = { '--input-dir': 'inputDir', '--output-dir': 'outputDir' }[process.argv[i]];
  if (!key || !process.argv[i + 1]) throw new Error('Usage: render-part2-diagrams.mjs [--input-dir DIR] [--output-dir DIR]');
  options[key] = path.resolve(process.argv[++i]);
}
const names = [
  'p2-s38-position-swap', 'p2-s40-feature-selection', 'p2-s45-gain-waveforms',
  'p2-s49-learning-inference', 'p2-s50-scene-attributes', 'p2-s59-time-requirements',
  'p2-s62-source-trajectories', 'p2-s65-event-negatives',
];
const [font, semibold] = await Promise.all([
  fs.readFile(path.join(repo, 'public/fonts/Pretendard-Regular.woff2')),
  fs.readFile(path.join(repo, 'public/fonts/Pretendard-SemiBold.woff2')),
]);
await fs.mkdir(options.outputDir, { recursive: true });
const browser = await chromium.launch({ headless: true });
try {
  const page = await browser.newPage({ viewport: { width: 1136, height: 360 }, deviceScaleFactor: 2 });
  for (const name of names) {
    const svg = await fs.readFile(path.join(options.inputDir, `${name}.svg`), 'utf8');
    await page.setContent(`<style>@font-face{font-family:Pretendard;src:url(data:font/woff2;base64,${font.toString('base64')});font-weight:400}@font-face{font-family:Pretendard;src:url(data:font/woff2;base64,${semibold.toString('base64')});font-weight:500 800}html,body{margin:0;background:#f6f8fa}</style>${svg}`);
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: path.join(options.outputDir, `${name}.png`) });
  }
} finally {
  await browser.close();
}
console.log(`Rendered ${names.length} Part 2 diagrams at 2272×720`);
