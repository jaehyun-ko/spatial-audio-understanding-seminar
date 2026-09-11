// Replace slides 02–07 only, preserving every other slide byte for byte.
import { readFile, writeFile, mkdir } from 'node:fs/promises';
import { parseSync } from '@slidev/parser';
const meta=JSON.parse(await readFile('manim/intro-sequence/slides.json','utf8'));
const replacement=meta.map(s=>`---\nlayout: seminar\nvariant: figure\ntransition: none\n---\n\n# ${s.title}\n\n::body::\n<ManimScene src="/animations/intro-sequence/${s.id}.mp4" webm="/animations/intro-sequence/${s.id}.webm" poster="/animations/intro-sequence/${s.id}-start.png" print-poster="/animations/intro-sequence/${s.id}-end.png" description="${s.title}: 같은 3차원 장면을 유지하는 설명용 애니메이션" />\n\n::takeaway::\n${s.takeaway}\n\n::source::\n${s.source}\n\n<!--\n[S${String(s.number).padStart(2,'0')} 발표 노트]\n${s.note}\n\n[Sources]\n${s.urls.map(u=>'- '+u).join('\n')}\n-->\n\n`).join('');
await mkdir('tmp/intro-sequence/before',{recursive:true});
for(const name of ['slides/part1.md','slides.md']){
 const original=await readFile(name,'utf8'),parsed=parseSync(original),lines=original.split('\n');
 if(![37,78].includes(parsed.slides.length))throw Error('Unexpected slide count: '+name);
 const begin=parsed.slides[1].start,end=parsed.slides[7].start;
 const updated=[...lines.slice(0,begin),replacement.trimEnd(),'',...lines.slice(end)].join('\n');
 const next=parseSync(updated);
 if(next.slides.length!==parsed.slides.length)throw Error('Changed slide count');
 for(let i=0;i<parsed.slides.length;i++)if(i<1||i>6){if(parsed.slides[i].content!==next.slides[i].content||parsed.slides[i].note!==next.slides[i].note)throw Error('Unexpected change to '+(i+1))}
 await writeFile('tmp/intro-sequence/before/'+name.replaceAll('/','-'),original);
 await writeFile(name,updated);
 console.log(name+': replaced only slides 02–07');
}
const introHead=`---\ntheme: default\ntitle: '도입부 2–7 · 공간 관측'\naspectRatio: 16/9\ncanvasWidth: 1280\ncolorSchema: light\ntransition: none\nrouterMode: hash\nmdc: true\nfonts:\n  sans: Seminar Pretendard\n  provider: none\nlayout: seminar\nvariant: figure\n---`;
await writeFile('intro-review.md',introHead+replacement.replace(/^---\n[\s\S]*?\n---/,''));
