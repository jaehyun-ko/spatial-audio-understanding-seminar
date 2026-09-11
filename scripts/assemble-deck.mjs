#!/usr/bin/env node
import { readFile, writeFile } from 'node:fs/promises';
import { parseSync } from '@slidev/parser';
const plan=JSON.parse(await readFile('plans/CAUSAL_DECK_ORDER.json','utf8'));
const head = `---
theme: default
title: '공간 소리를 듣고 판단하는 모델'
description: 'GCC-PHAT 시간차 추정과 SRP 좌표 탐색, Neural-SRP 응답 학습을 설명한 뒤 LLM 통합으로 연결한다: 본문 ${plan.mainSlides}장과 근거 부록 ${plan.appendixSlides}장'
aspectRatio: 16/9
canvasWidth: 1280
colorSchema: light
transition: none
routerMode: hash
mdc: true
fonts:
  sans: Seminar Pretendard
  provider: none
layout: seminar-cover
drawings:
  persist: false
---`;
const parts = await Promise.all([1,2,3].map(n => readFile(`slides/part${n}.md`, 'utf8')));
const counts = parts.map(p => parseSync(p).slides.length);
if (counts.join(',') !== plan.partSizes.join(',')) throw new Error(`Unexpected part sizes: ${counts}`);
const full = head + parts[0].replace(/^---\n[\s\S]*?\n---/, '') + '\n\n' + parts[1] + '\n\n' + parts[2];
const parsed = parseSync(full);
if (parsed.slides.length !== plan.slides.length) throw new Error(`Expected ${plan.slides.length}, received ${parsed.slides.length}`);
await writeFile('slides.md', full.replace(/\n{4,}/g,'\n\n\n').trimEnd()+'\n');
console.log(`Assembled ${parsed.slides.length} slides from ${counts.join('+')}`);
