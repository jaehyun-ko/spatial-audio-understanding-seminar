#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import {parseSync} from '@slidev/parser';
const text=fs.readFileSync('slides.md','utf8');
const deck=parseSync(text);
const errors=[];
const plan=JSON.parse(fs.readFileSync('plans/CAUSAL_DECK_ORDER.json','utf8'));
if(deck.slides.length!==plan.slides.length)errors.push(`Expected ${plan.slides.length} slides, found ${deck.slides.length}`);
const papers=['Neural-SRP','AGG-RL','MC-SimCLR','CCSR','SFD','GRAM','LAM','AT2SELD','ELSA','SALM','SelectTSL','BAT','DSpAST','OWL','PhaseCoder','Dual-BEATs','Sci-Phi','Spatial-Omni','The World is Not Mono','Spatial Audio Motion','Dynamic Source Movements','ST-AudioLM','CoSTALA','STAR-Bench','WearVox','SARL','BMLD'];
for(const p of papers)if(!text.toLowerCase().includes(p.toLowerCase()))errors.push(`Missing paper: ${p}`);
let assets=0;
for(let i=0;i<deck.slides.length;i++){
  const s=deck.slides[i],num=i+1;
  if(!s.content.match(/^#\s/m))errors.push(`Slide ${num}: missing title`);
  if(!s.note||s.note.trim().length<40)errors.push(`Slide ${num}: missing presenter notes`);
  if(!/https?:\/\//.test(s.note||'')&&!/설명용|발표.*재구성|발표.*정리|범위/.test((s.note||'')+' '+s.content))errors.push(`Slide ${num}: source or illustrative provenance missing`);
  if(!s.content.includes('::source::'))errors.push(`Slide ${num}: visible source missing`);
  const variant=s.frontmatter.layout;
  if(!['seminar','seminar-cover','seminar-section'].includes(variant))errors.push(`Slide ${num}: unexpected layout ${variant}`);
  for(const m of s.content.matchAll(/(?:src|poster|print-poster|webm)="\/(.*?)"/g)){
    assets++;if(!fs.existsSync(path.join('public',m[1])))errors.push(`Slide ${num}: missing asset ${m[1]}`);
  }
  if(/TODO|TBD|PLACEHOLDER|확인 전 수치/.test(s.content))errors.push(`Slide ${num}: unresolved production placeholder`);
}
if(errors.length){console.error(errors.join('\n'));process.exit(1)}
console.log(`Validated ${deck.slides.length} slides, ${papers.length} paper identities, ${assets} asset references and all presenter notes.`);
