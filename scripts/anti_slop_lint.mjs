#!/usr/bin/env node
import fs from 'node:fs';
import {parseSync} from '@slidev/parser';
const text=fs.readFileSync('slides.md','utf8');
const slides=parseSync(text).slides;
const errors=[],warnings=[];
const banned=['계보상의 의미','새로운 전환점','아직 동시에 해결되지 않은','강한 방법 논문','Open gap','아직 아무도','완전한 범용'];
for(let i=0;i<slides.length;i++){
  const content=slides[i].content;
  for(const p of banned)if(content.includes(p))errors.push(`Slide ${i+1}: banned phrase ${p}`);
  const plain=content.replace(/<[^>]+>/g,' ').replace(/::\w+::/g,' ').replace(/[#*_`|]/g,' ');
  const words=plain.split(/\s+/).filter(Boolean);
  if(words.length>140)warnings.push(`Slide ${i+1}: ${words.length} onscreen tokens; inspect density`);
}
if(errors.length){console.error(errors.join('\n'));process.exit(1)}
console.log(`Anti-slop lint OK: ${slides.length} slides`);
if(warnings.length)console.log(warnings.join('\n'));
