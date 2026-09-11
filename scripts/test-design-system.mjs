#!/usr/bin/env node
/**
 * Regression tests for the ten-slide seminar design specimen.
 * node scripts/test-design-system.mjs --url http://localhost:3036
 * Fixtures mutate only an isolated Chromium DOM, never the source deck.
 */
import { chromium } from 'playwright-chromium';
import { mkdir, writeFile } from 'node:fs/promises';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

export const EXPECTED = {
  colors: { '--color-paper': '#f6f8fa', '--color-surface': '#ffffff', '--color-ink': '#142233', '--color-secondary': '#586879', '--color-accent': '#1f5fae', '--color-signal': '#008b9a', '--color-rule': '#d4dde7', '--color-caution': '#a95018', '--color-inverse': '#ffffff', '--color-dark': '#0c1b2f' },
  rows: [104, 404, 52, 36],
  sizes: { '--type-cover': 82, '--type-title': 44, '--type-body': 27, '--type-label': 20, '--type-caption': 18, '--type-citation': 14, '--type-number': 38, '--type-number-dense': 32 },
};

// Self-contained browser-side assertion collector. DOM Range rectangles include
// font ascender/descender metrics, so allow a 3px glyph-boundary tolerance.
export function inspectDesign(root, expected) {
  const issues = [];
  const check = (condition, code, detail) => { if (!condition) issues.push({ code, ...detail }); };
  const round = n => Math.round(n * 100) / 100;
  const rect = r => ({ x: round(r.x), y: round(r.y), right: round(r.right), bottom: round(r.bottom), width: round(r.width), height: round(r.height) });
  const shown = el => {
    if (!el.getClientRects().length) return false;
    for (let p = el; p; p = p.parentElement) {
      const c = getComputedStyle(p);
      if (c.display === 'none' || c.visibility === 'hidden' || Number(c.opacity) === 0) return false;
    }
    return true;
  };
  const fragments = el => {
    const items = [];
    // KaTeX includes a visually hidden MathML copy and many positioned spans.
    // Measure each visible expression once instead of treating its numerator,
    // denominator and scripts as separate text lines.
    const mathRoots = [...el.querySelectorAll('.seminar-math,.katex')].filter(math => !math.parentElement.closest('.seminar-math,.katex'));
    if (el.matches('.seminar-math,.katex')) mathRoots.unshift(el);
    for (const math of mathRoots) {
      if (!shown(math)) continue;
      const visual = math.querySelector('.katex-html') || math;
      const r = visual.getBoundingClientRect();
      if (r.width && r.height) items.push({ rect: rect(r), text: (visual.textContent || '').trim().slice(0, 100), math: true });
    }
    const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
    while (walker.nextNode()) {
      const node = walker.currentNode;
      if (!node.textContent.trim() || !shown(node.parentElement) || node.parentElement.closest('svg,style,script,.seminar-math,.katex,.katex-mathml,math,annotation')) continue;
      const range = document.createRange();
      range.setStart(node, node.textContent.length - node.textContent.trimStart().length);
      range.setEnd(node, node.textContent.trimEnd().length);
      for (const r of range.getClientRects()) if (r.width && r.height) items.push({ rect: rect(r), text: node.textContent.trim().slice(0, 100) });
    }
    return items;
  };
  const lineCount = el => {
    const lines = [];
    const items = fragments(el);
    for (const { rect: r } of items.filter(item => !item.math)) {
      const line = lines.find(line => Math.abs(line.y - r.y) <= 3);
      if (line) line.bottom = Math.max(line.bottom, r.bottom);
      else lines.push({ y: r.y, bottom: r.bottom });
    }
    // An inline fraction can extend above the surrounding text while still
    // occupying the same line. Its box must overlap that line, not share its top.
    for (const { rect: r } of items.filter(item => item.math)) {
      if (!lines.some(line => Math.min(line.bottom, r.bottom) - Math.max(line.y, r.y) > 3)) lines.push({ y: r.y, bottom: r.bottom });
    }
    return lines.length;
  };
  const rootStyle = getComputedStyle(root);
  check(rootStyle.backgroundColor === 'rgb(246, 248, 250)', 'slide-background', { expected: 'rgb(246, 248, 250)', actual: rootStyle.backgroundColor });
  const tokens = {};
  const normalizedHex = color => /^#[0-9a-f]{3}$/.test(color) ? '#'+[...color.slice(1)].map(c=>c+c).join('') : color;
  for (const [name, value] of Object.entries(expected.colors)) {
    tokens[name] = rootStyle.getPropertyValue(name).trim().toLowerCase();
    check(normalizedHex(tokens[name]) === normalizedHex(value), 'color-token', { token: name, expected: value, actual: tokens[name] });
  }
  for (const [name, value] of Object.entries(expected.sizes)) {
    tokens[name] = rootStyle.getPropertyValue(name).trim();
    check(parseFloat(tokens[name]) === value, 'size-token', { token: name, expected: value, actual: tokens[name] });
  }
  const faces = [...document.fonts].map(font => ({ family: font.family.replace(/["']/g, ''), status: font.status }));
  check(faces.some(font => font.family === 'Seminar Pretendard' && font.status === 'loaded'), 'webfont-not-loaded', { faces });
  check(document.fonts.check('44px "Seminar Pretendard"', '공간 오디오 이해'), 'webfont-check', {});
  const fontResources = performance.getEntriesByType('resource').filter(entry => /\/fonts\/[^/]+\.woff2(?:\?|$)/.test(entry.name)).map(entry => entry.name);
  const declaredLocalFont = [...document.styleSheets].some(sheet => {
    try { return [...sheet.cssRules].some(rule => rule.type === CSSRule.FONT_FACE_RULE && /Seminar Pretendard/.test(rule.cssText) && /(?:url\([\"']?\/fonts\/|localhost[^)]*\/fonts\/)/.test(rule.cssText)); }
    catch { return false; }
  });
  check(fontResources.some(url => new URL(url).origin === location.origin) || (declaredLocalFont && faces.some(font => font.family === 'Seminar Pretendard' && font.status === 'loaded')), 'local-webfont-resource', { fontResources, declaredLocalFont });
  const observedSizes = [];
  const roleSizes = [
    ['h1,h2', root.classList.contains('seminar-cover') ? 82 : root.classList.contains('seminar-section') ? 60 : 44],
    ['.seminar-body,.seminar-takeaway', 27], ['.seminar-source', 14],
    ['.seminar-aside', 23], ['.seminar-label', 20], ['figcaption,.seminar-condition', 18], ['table caption', 20],
  ];
  for (const [selector, expectedSize] of roleSizes) for (const el of root.querySelectorAll(selector)) {
    if (!shown(el)) continue;
    const c = getComputedStyle(el);
    observedSizes.push({ selector, actual: parseFloat(c.fontSize), expected: expectedSize });
    check(parseFloat(c.fontSize) === expectedSize, 'computed-font-size', { selector, expected: expectedSize, actual: c.fontSize });
    check(c.fontFamily.split(',')[0].replace(/["']/g, '').trim() === 'Seminar Pretendard', 'computed-font-family', { selector, actual: c.fontFamily });
  }
  for (const el of root.querySelectorAll('.seminar-label,table caption')) {
    if (!shown(el)) continue;
    const expectedColor = el.matches('caption') ? 'rgb(88, 104, 121)' : el.classList.contains('semantic-negative') ? 'rgb(169, 80, 24)' : 'rgb(0, 139, 154)';
    const actual = getComputedStyle(el).color;
    check(actual === expectedColor, 'role-color', { role: el.matches('caption') ? 'table-caption' : 'seminar-label', text: el.textContent.trim().slice(0, 100), expected: expectedColor, actual });
  }
  for (const el of root.querySelectorAll('.seminar-results td.is-numeric')) {
    if (!shown(el)) continue;
    const c = getComputedStyle(el);
    const expectedSize = el.closest('table').classList.contains('seminar-results--dense') ? 32 : 38;
    observedSizes.push({ selector: '.seminar-results td.is-numeric', actual: parseFloat(c.fontSize), expected: expectedSize });
    check(parseFloat(c.fontSize) === expectedSize, 'computed-font-size', { selector: '.seminar-results td.is-numeric', expected: expectedSize, actual: c.fontSize });
  }
  const mathErrors = [...root.querySelectorAll('.katex-error')].map(el => ({ text: el.textContent.trim(), message: el.getAttribute('title') }));
  check(mathErrors.length === 0, 'math-render-error', { errors: mathErrors });
  const renderedMath = [...root.querySelectorAll('.seminar-math,.katex')].filter(el => !el.parentElement.closest('.seminar-math,.katex')).filter(shown).map(el => {
    const katex = el.matches('.katex') ? el : el.querySelector('.katex');
    const visual = katex?.querySelector('.katex-html');
    const bounds = visual?.getBoundingClientRect();
    const rendered = Boolean(katex && visual && shown(visual) && bounds.width > 0 && bounds.height > 0);
    const item = { text: (visual?.textContent || el.textContent).trim().slice(0, 100), rendered, rect: bounds ? rect(bounds) : null };
    check(rendered, 'math-not-rendered', item);
    return item;
  });
  const color = css => {
    const values = css.match(/[\d.]+/g)?.map(Number);
    if (!css.startsWith('rgb') || !values || values.length < 3) throw new Error(`Unsupported computed color: ${css}`);
    return { rgb: values.slice(0, 3), alpha: values[3] ?? 1 };
  };
  const blend = (fg, bg, alpha) => fg.map((value, i) => value * alpha + bg[i] * (1 - alpha));
  const luminance = rgb => rgb.map(value => value / 255).map(value => value <= 0.04045 ? value / 12.92 : ((value + 0.055) / 1.055) ** 2.4).reduce((sum, value, i) => sum + value * [0.2126, 0.7152, 0.0722][i], 0);
  const titleContrasts = [];
  for (const title of root.querySelectorAll('h1,h2')) {
    if (!shown(title)) continue;
    const layers = [];
    let opacity = 1;
    let unsupportedBackground = false;
    let nearestOpaque = null;
    for (let p = title; p; p = p.parentElement) {
      const c = getComputedStyle(p);
      opacity *= Number(c.opacity);
      if (c.backgroundImage !== 'none') unsupportedBackground = true;
      if (!nearestOpaque) {
        const background = color(c.backgroundColor);
        layers.push(background);
        if (background.alpha === 1) nearestOpaque = p.className || p.tagName;
      }
    }
    let background = [255, 255, 255];
    for (const layer of layers.reverse()) background = blend(layer.rgb, background, layer.alpha);
    const foreground = color(getComputedStyle(title).color);
    const effectiveForeground = blend(foreground.rgb, background, foreground.alpha * opacity);
    const light = luminance(effectiveForeground), dark = luminance(background);
    const ratio = (Math.max(light, dark) + 0.05) / (Math.min(light, dark) + 0.05);
    const result = { text: title.innerText.replace(/\s+/g, ' '), foreground: foreground.rgb, background, nearestOpaque, ratio: round(ratio), lines: lineCount(title) };
    titleContrasts.push(result);
    check(!unsupportedBackground, 'title-contrast-background-unresolved', { text: result.text });
    check(ratio >= 4.5, 'title-contrast', { ...result, minimum: 4.5 });
  }
  const images = [...root.querySelectorAll('img')].filter(shown).map(img => ({ src: img.currentSrc || img.src, loaded: img.complete && img.naturalWidth > 0, width: img.naturalWidth, height: img.naturalHeight, rect: rect(img.getBoundingClientRect()) }));
  for (const image of images) check(image.loaded, 'image-not-loaded', image);
  const videos = [...root.querySelectorAll('video')].filter(shown).map(video => ({ src: video.currentSrc, loaded: video.readyState >= 1 && video.videoWidth > 0 && video.videoHeight > 0, width: video.videoWidth, height: video.videoHeight, duration: video.duration, rect: rect(video.getBoundingClientRect()) }));
  for (const video of videos) check(video.loaded, 'video-not-loaded', video);
  const rows = rootStyle.gridTemplateRows.split(/\s+/).map(parseFloat);
  const regular = !root.classList.contains('seminar-cover') && !root.classList.contains('seminar-section');
  const frames = [];
  if (regular) {
    check(rows.length === 4 && rows.every((height, i) => Math.abs(height - expected.rows[i]) < 0.5), 'frame-rows', { actual: rows, expected: expected.rows });
    const r = root.getBoundingClientRect();
    const scaleX = r.width / root.offsetWidth, scaleY = r.height / root.offsetHeight;
    const x = r.x + parseFloat(rootStyle.paddingLeft) * scaleX;
    const width = r.width - (parseFloat(rootStyle.paddingLeft) + parseFloat(rootStyle.paddingRight)) * scaleX;
    let y = r.y + parseFloat(rootStyle.paddingTop) * scaleY;
    for (const [i, name] of ['header', 'body', 'takeaway', 'source'].entries()) {
      const element = root.querySelector(`.seminar-${name}`);
      check(Boolean(element), 'missing-frame', { frame: name });
      const height = (rows[i] || 0) * scaleY;
      frames.push({ name, element, x, y, width, height, right: x + width, bottom: y + height });
      y += height + parseFloat(rootStyle.rowGap) * scaleY;
    }
    for (const frame of frames) {
      if (!frame.element) continue;
      const text = fragments(frame.element);
      for (const item of text) {
        const r = item.rect;
        const edges = [r.x < frame.x - 3 && 'left', r.right > frame.right + 3 && 'right', r.y < frame.y - 3 && 'top', r.bottom > frame.bottom + 3 && 'bottom'].filter(Boolean);
        check(!edges.length, 'frame-text-overflow', { frame: frame.name, edges, ...item });
        for (const other of frames) {
          if (other === frame) continue;
          const overlapX = Math.min(r.right, other.right) - Math.max(r.x, other.x);
          const overlapY = Math.min(r.bottom, other.bottom) - Math.max(r.y, other.y);
          check(overlapX <= 3 || overlapY <= 3, 'frame-text-intrusion', { from: frame.name, into: other.name, ...item });
        }
      }
      for (const img of frame.element.querySelectorAll('img')) {
        const r = img.getBoundingClientRect();
        check(r.x >= frame.x - 3 && r.right <= frame.right + 3 && r.y >= frame.y - 3 && r.bottom <= frame.bottom + 3, 'frame-image-overflow', { frame: frame.name, src: img.src, rect: rect(r) });
      }
    }
    const header = root.querySelector('.seminar-header');
    const takeaway = root.querySelector('.seminar-takeaway');
    const source = root.querySelector('.seminar-source');
    check(!header || lineCount(header) <= 2, 'header-line-budget', { actual: header ? lineCount(header) : 0, maximum: 2 });
    check(!takeaway || lineCount(takeaway) <= 1, 'takeaway-line-budget', { actual: takeaway ? lineCount(takeaway) : 0, maximum: 1 });
    check(!source || lineCount(source) <= 2, 'source-line-budget', { actual: source ? lineCount(source) : 0, maximum: 2 });
    for (const caption of root.querySelectorAll('figcaption')) check(lineCount(caption) <= 2, 'caption-line-budget', { actual: lineCount(caption), maximum: 2 });
  }
  return { title: titleContrasts[0]?.text, issues, tokens, faces, fontResources, observedSizes, renderedMath, titleContrasts, images, videos, gridRows: rows, frames: frames.map(({ element, ...frame }) => frame), lineCounts: Object.fromEntries(['header', 'takeaway', 'source'].map(name => [name, root.querySelector(`.seminar-${name}`) ? lineCount(root.querySelector(`.seminar-${name}`)) : null])) };
}

function argumentsFor(argv) {
  const options = { url: 'http://localhost:3036', out: 'tmp' };
  for (let i = 0; i < argv.length; i++) {
    if (argv[i] === '--help') return { help: true };
    if (!['--url', '--out'].includes(argv[i]) || !argv[i + 1]) throw new Error(`Unknown or incomplete option: ${argv[i]}`);
    options[argv[i].slice(2)] = argv[++i];
  }
  const url = new URL(options.url);
  if (!['http:', 'https:'].includes(url.protocol)) throw new Error('--url must use http or https');
  url.hash = '';
  options.url = url.href;
  options.out = resolve(options.out);
  return options;
}

export async function runDesignTests(options) {
  await mkdir(options.out, { recursive: true });
  const report = { generatedAt: new Date().toISOString(), url: options.url, expected: EXPECTED, slides: [], fixtures: [], runtimeErrors: [], runtimeWarnings: [], limitations: ['Contrast checks use CSS foreground and ancestor background colors, not raster pixels or overlapping pseudo-elements.', 'Frame checks use DOM text/visual bounds with 3px font-metric tolerance.', 'Only initial click states and the ten specimen slides are covered.'] };
  let browser;
  try {
    browser = await chromium.launch({ headless: true });
    const page = await browser.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 1, reducedMotion: 'reduce' });
    // Vite loads enough modules to exhaust the default 250-entry resource
    // timing buffer before fonts arrive. Keep their original network evidence.
    await page.addInitScript(() => performance.setResourceTimingBufferSize(10000));
    page.setDefaultTimeout(15000);
    page.on('pageerror', error => (/wake lock.*permission.*denied/i.test(error.message) ? report.runtimeWarnings : report.runtimeErrors).push(error.message));
    const cdp = await page.context().newCDPSession(page);
    await cdp.send('DOM.enable');
    await cdp.send('CSS.enable');
    async function openSlide(number, reload = false) {
      await page.goto(`${options.url}#/${number}`, { waitUntil: 'domcontentloaded' });
      if (reload) await page.reload({ waitUntil: 'domcontentloaded' });
      const slide = page.locator(`.slidev-page[data-slidev-no="${number}"] .slidev-layout.seminar:visible`).first();
      await slide.waitFor();
      await page.waitForFunction(() => document.fonts.status === 'loaded');
      await slide.evaluate(async root => {
        await document.fonts.ready;
        await Promise.all([...root.querySelectorAll('img')].map(img => img.decode().catch(() => {})));
        await Promise.all([...root.querySelectorAll('video')].map(video => video.readyState >= 1 || video.error ? Promise.resolve() : Promise.race([
          new Promise(resolve => {
            video.addEventListener('loadedmetadata', resolve, { once: true });
            video.addEventListener('error', resolve, { once: true });
          }),
          new Promise(resolve => setTimeout(resolve, 5000)),
        ])));
        await new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)));
      });
      await page.mouse.move(1, 1);
      return slide;
    }
    async function actualFonts(number) {
      const { root } = await cdp.send('DOM.getDocument');
      const probes = [];
      for (const suffix of ['h1', '.seminar-body p', '.seminar-body td', '.seminar-source p', '.seminar-takeaway p']) {
        const selector = `.slidev-page[data-slidev-no="${number}"] ${suffix}`;
        const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector });
        if (nodeId) probes.push({ selector: suffix, ...(await cdp.send('CSS.getPlatformFontsForNode', { nodeId })) });
      }
      return probes;
    }
    for (let number = 1; number <= 10; number++) {
      try {
        const slide = await openSlide(number);
        const result = { number, ...(await slide.evaluate(inspectDesign, EXPECTED)), renderedFonts: await actualFonts(number) };
        for (const probe of result.renderedFonts) if (probe.fonts.length && !probe.fonts.some(font => font.isCustomFont && /pretendard/i.test(font.familyName) && font.glyphCount > 0)) result.issues.push({ code: 'rendered-webfont-missing', ...probe });
        if (!result.renderedFonts.some(probe => probe.selector === 'h1' && probe.fonts.some(font => font.isCustomFont && /pretendard/i.test(font.familyName)))) result.issues.push({ code: 'rendered-title-webfont-missing' });
        report.slides.push(result);
        console.log(`Slide ${number}: ${result.issues.length ? 'FAIL' : 'PASS'} — ${result.title}; title contrast ${result.titleContrasts.map(title => `${title.ratio}:1`).join(', ')}`);
      } catch (error) { report.slides.push({ number, issues: [{ code: 'capture-failure', message: error.message }] }); }
    }
    let slide = await openSlide(4, true);
    await slide.evaluate(root => {
      root.querySelector('.seminar-header').innerHTML = '<h1>첫 번째 충분히 긴 제목으로 공간 단서를 살펴보기<br>두 번째 충분히 긴 제목에서 입력과 출력을 구별하기</h1>';
      root.querySelector('.seminar-source').innerHTML = '<p>Baek et al., Physics-Informed Audio-Geometry-Grid Representation, ICLR 2026, Fig. 1(a–b).<br>두 번째 출처 줄: 원본 벡터 그림과 평가 조건을 함께 표시하는 긴 학술 인용문.</p>';
      root.querySelector('figcaption').innerHTML = '첫 번째 설명 줄: 두 마이크에 도착하는 시간차와 경로 차이를 확인한다.<br>두 번째 설명 줄: 같은 지연에서도 주파수에 따라 위상차가 반복된다.';
    });
    const stress = await slide.evaluate(inspectDesign, EXPECTED);
    const stressImage = resolve(options.out, 'design-system-stress.png');
    await page.screenshot({ path: stressImage, animations: 'disabled' });
    report.fixtures.push({ name: 'two-line-title-source-caption', expected: 'pass', passed: stress.issues.length === 0 && stress.lineCounts.header === 2 && stress.lineCounts.source === 2, screenshot: stressImage, ...stress });
    slide = await openSlide(4, true);
    await slide.evaluate(root => { root.querySelector('.seminar-header').innerHTML = '<h1>첫 번째 제목 줄<br>두 번째 제목 줄<br>세 번째 제목 줄이 본문 영역을 침범한다</h1>'; });
    const threeLines = await slide.evaluate(inspectDesign, EXPECTED);
    report.fixtures.push({ name: 'three-line-title-rejected', expected: 'detect header overflow', passed: threeLines.issues.some(issue => issue.code === 'frame-text-overflow' && issue.frame === 'header') && threeLines.issues.some(issue => issue.code === 'header-line-budget'), ...threeLines });
    slide = await openSlide(4, true);
    await slide.evaluate(root => { root.querySelector('.seminar-takeaway').innerHTML = '<p>첫 번째 긴 결론 문장은 고정된 한 줄 공간을 사용한다.<br>두 번째 긴 결론 문장은 출처 영역을 침범하므로 허용하지 않는다.</p>'; });
    const longTakeaway = await slide.evaluate(inspectDesign, EXPECTED);
    report.fixtures.push({ name: 'two-line-takeaway-rejected', expected: 'detect takeaway overflow', passed: longTakeaway.issues.some(issue => issue.code === 'frame-text-overflow' && issue.frame === 'takeaway') && longTakeaway.issues.some(issue => issue.code === 'takeaway-line-budget'), ...longTakeaway });
    // Reproduce the original black-on-dark-cover regression in memory.
    slide = await openSlide(1, true);
    await slide.evaluate(root => {
      const dark = getComputedStyle(root).getPropertyValue('--color-dark');
      root.style.backgroundColor = dark;
      root.querySelector('h1').style.color = dark;
    });
    const darkCover = await slide.evaluate(inspectDesign, EXPECTED);
    report.fixtures.push({ name: 'dark-on-dark-cover-rejected', expected: 'detect title contrast below 4.5', passed: darkCover.issues.some(issue => issue.code === 'title-contrast'), ...darkCover });
  } catch (error) { report.fatalError = error.message; }
  finally { if (browser) await browser.close(); }
  report.summary = { testedSlides: report.slides.length, slideFailures: report.slides.filter(slide => slide.issues.length).length, fixtures: report.fixtures.length, fixtureFailures: report.fixtures.filter(fixture => !fixture.passed).length, runtimeErrors: report.runtimeErrors.length, runtimeWarnings: report.runtimeWarnings.length };
  report.passed = !report.fatalError && report.summary.testedSlides === 10 && !report.summary.slideFailures && report.summary.fixtures === 4 && !report.summary.fixtureFailures && !report.summary.runtimeErrors;
  const output = resolve(options.out, 'design-system-test-report.json');
  await writeFile(output, `${JSON.stringify(report, null, 2)}\n`);
  for (const fixture of report.fixtures) console.log(`Fixture ${fixture.name}: ${fixture.passed ? 'PASS' : 'FAIL'}`);
  console.log(`${report.passed ? 'PASS' : 'FAIL'}: ${JSON.stringify(report.summary)}\nReport: ${output}`);
  if (report.fatalError) console.error(report.fatalError);
  return report;
}

if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) {
  try {
    const options = argumentsFor(process.argv.slice(2));
    if (options.help) console.log('node scripts/test-design-system.mjs [--url http://localhost:3036] [--out tmp]');
    else process.exitCode = (await runDesignTests(options)).passed ? 0 : 1;
  } catch (error) { console.error(error.message); process.exitCode = 1; }
}
