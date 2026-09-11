#!/usr/bin/env node
/** Rebuild a question-led main talk and evidence appendix from stable source IDs. */
import fs from 'node:fs/promises';
import {parseSync} from '@slidev/parser';

const plan=JSON.parse(await fs.readFile('plans/CAUSAL_DECK_ORDER.json','utf8'));
const before=parseSync(await fs.readFile(plan.archive,'utf8')).slides;
const noteCorrections=JSON.parse(await fs.readFile('plans/HISTORY_NOTE_CORRECTIONS.json','utf8'));
const missing=[];
for(const row of plan.slides)if(row.bridge)try{await fs.stat(`slides/bridges/${row.bridge}.md`)}catch{missing.push(row.bridge)}
if(missing.length)throw new Error('Bridge authoring is incomplete: '+missing.join(', '));

const takeaway={
  10:'**쌍별 공간 응답을 학습하고 합산하는 설계**가 위치 피크를 바꾼 정성 예시다.',
  14:'AGG-RL의 **DOA 재구현 안에서** 정합의 효과를 비교한다. 원형의 2D 위치 실험과는 구별한다.',
  19:'인코더를 고정한 판독에서 **사건과 방향 정보의 접근성**을 확인한다.',
  25:'이 결과는 **공간 특징 사전학습 후 전체 미세조정**의 근거다. 고정 표현 판독과는 다르다.',
  29:'**마스킹은 학습 목표**, 고정 인코더의 여러 과제 판독은 **재사용을 확인하는 시험**이다.',
  32:'ELSA의 검색용 문장 정렬은 **사건과 위치를 함께 맞추는 요구**를 보여 준다.',
  34:'SALM은 **의미·공간을 각각 감독하고 결합**한다. LLM의 답변 생성과는 다른 정렬 문제다.',
  35:'**의미 정렬 loss의 기여**를 본 결과다. LLM·LoRA의 효과를 측정한 표가 아니다.',
  51:'**기존 의미 경로는 고정**하고 공간 encoder·projector·LoRA를 적응한다.',
  54:'**projector 정렬 → LLM LoRA → 공간 경로 적응**으로 학습 문제를 나눈다.',
  55:'이 zero-spatial 비교는 **공간 입력 기여의 근거**이며 제거 시점·checkpoint 공유는 미명시다.',
  57:'**source slots로 감독**하지만, LLM에는 의미 경로와 결합한 **dense 특징**을 보낸다.',
  63:'고정 인코더의 **의미·궤적 토큰**을 학습하는 connector와 LoRA로 연결한다.',
  64:'같은 41-token 인터페이스에서도 **시간 구조를 배운 표현**의 평균 성과가 달랐다.',
  41:'LLM 인터페이스를 맞춘 비교에서 **인코더 설계·사전학습의 기여**를 읽는다.',
  43:'**기하 지도는 인코더 학습에**, projector·LoRA는 그 표현을 사용하는 QA 학습에 쓴다.',
  44:'이 표의 개입은 **인코더의 geometry loss**다. 어댑터·LoRA·CoT 효과를 뜻하지 않는다.',
  48:'**관계 QA와 공간 지정 목표 발화 전사**는 별도 과제로 확인해야 한다.',
  73:'고정 인코더의 **같은 판독 규칙**으로 의미·위치·방 정보의 접근성을 비교한다.',
  75:'이 표현 거리 반응만으로 **LLM이 같은 단서를 사용한다**고 말할 수는 없다.',
};

const output=[];
for(const row of plan.slides){
 const s=row.bridge?parseSync(await fs.readFile(`slides/bridges/${row.bridge}.md`,'utf8')).slides[0]:before[row.origin-1];
 if(!s)throw new Error('Missing source '+JSON.stringify(row));
 let content=s.content;
 if(row.title)content=content.replace(/^# .+$/m,'# '+row.title);
 if(row.origin===1){
  content=content.replace(/::subtitle::\n[\s\S]*?(?=\n::source::)/,'::subtitle::\n마이크의 관측을 LLM의 답변으로 연결하는 조건\n');
  content=content.replace(/::source::\n[\s\S]*$/,'::source::\n본문 '+plan.mainSlides+'장 · 근거 부록 '+plan.appendixSlides+'장 · 27편의 설계와 검증 범위');
 }
 if(takeaway[row.origin])content=content.replace(/::takeaway::\n[\s\S]*?(?=\n::source::)/,'::takeaway::\n'+takeaway[row.origin]+'\n');
 if(row.origin===73)content=content.replace('입력 범례','요인 범례');
 if(row.origin===71)content=content.replace('실제 WearVox 시험 · Side Talk Rejection', '기기에게 건넨 말인가? · WearVox · Side Talk Rejection');
 let note=(s.note||'').replace(/\[(?:다음 연결|전환)\]\n[^\n]+(?:\n(?!\[|\n)[^\n]+)*(?:\n|$)/g,'');
 // The archive retains every original note; only superseded navigation is removed here.
 if(row.origin===55){
  note=note.replaceAll('같은 SO-7B에서 공간 토큰을 없앤 조건','SO-7B-zs의 zero-spatial 조건');
  note+='\n\n[원문 확인 보완]\nSpatial-Omni v2 §5.3과 Appendix E.2는 zero/null spatial token을 사용한 변형을 명시하지만, 적용 시점이 학습부터인지 추론만인지와 checkpoint 공유 여부는 명시하지 않는다. 고정 checkpoint의 추론 시 제거 ablation으로 단정하지 않는다.\n';
 }
 if(row.origin===13||row.origin===14){
  note+='\n\n[원형과 재구현의 구별]\nNeural-SRP 2024 원형은 STFT 위상·쌍 좌표·방 크기로 25×25 2D 위치 응답을 예측한다. AGG-RL 2026 §4.1의 Neural-SRP는 time-domain GCC-PHAT 입력·Fibonacci DOA 격자·다중 spatial spectra로 수정된 재구현이다. 앞의 Recorded 4 위치 오차와 여기 Dynamic-U DOA 결과는 한 checkpoint의 단계적 향상이나 동일 과제의 연속 성능 비교가 아니다.\n';
 }
 if(row.origin===14)note+='\n[시험 축]\n후보 재질의 기능과 구별하여, 이번 정량 비교는 미노출 채널 수를 검사한다.\n';
 if(row.origin===48)note+='\n[과제 귀속 보완]\nTask 4는 공간으로 지정한 목표 화자를 골라 전사하는 targeted transcription이다. WER는 선택·결속·전사 오류를 함께 반영하며 일반 ASR 또는 기존 의미 능력 보존을 직접 측정한 지표가 아니다.\n';
 if(row.origin===54)note+='\n[기존 의미 능력]\n기존 audio tower를 고정한 구조만으로 의미 능력의 보존을 보장하지 않는다. Spatial-Omni v2 Table 18과 MIX 비교가 별도의 일반 오디오 평가 근거다. PhaseCoder의 targeted transcription WER와 구별한다.\n';
 if(row.origin){
  note=note.replaceAll('부록','원문의 추가 자료');
  note=note.replace(/[^.\n]*(?:다음 절|다음 회차|다음 고정 판독 결과)[^.\n]*[.]?/g,'');
  const bridgeNumber=k=>plan.slides.find(x=>x.bridge===k)?.number;
  const fallback={7:bridgeNumber('gcc-phat'),8:bridgeNumber('srp-candidate'),9:bridgeNumber('srp-candidate'),17:18,18:17,20:17,22:17,28:18,31:bridgeNumber('history-synthesis'),38:bridgeNumber('audio-llm-contract'),49:bridgeNumber('module-evidence'),53:plan.slides.find(x=>x.origin===55)?.number,67:bridgeNumber('causal-evaluation'),77:bridgeNumber('history-synthesis'),78:bridgeNumber('closing-tests')};
  note=note.replace(/\bS(\d{1,2})\b/g,(m,id)=>'S'+(plan.slides.find(x=>x.origin===Number(id))?.number||fallback[id]||id));
 }
 for(const [from,to] of Object.entries(noteCorrections))note=note.replaceAll(from,to);
 const next=plan.slides[row.number];
 const nextLine=row.number===plan.mainSlides?'본문은 여기서 마친다. 다음 장부터는 질문별 근거 부록이며 필요한 비교를 선택해 열어 본다.':row.appendix?'이 장은 본문의 '+row.chapter.replace('근거 부록 ','')+' 질문을 보완하는 선택 자료다.':next?'다음에 확인할 질문: '+(next.title||next.role):'';
 note=`[현재 S${String(row.number).padStart(2,'0')} · ${row.appendix?'근거 부록':'본문'}]\n${row.chapter}\n\n[설명의 중심]\n${row.role}\n\n[연결]\n${nextLine}\n\n[상세 근거와 해석 범위]\n${note}`;
 const fields={layout:s.frontmatter.layout||'seminar'};
 if(s.frontmatter.variant)fields.variant=s.frontmatter.variant;
 if(s.frontmatter.transition)fields.transition=s.frontmatter.transition;
 if(row.number!==1)fields.chapter=row.chapter;
 fields.causalStage=row.appendix?'appendix':'main';
 if(row.origin)fields.originSlide=row.origin;
 const front=Object.entries(fields).map(([k,v])=>`${k}: ${JSON.stringify(v)}`).join('\n');
 output.push(`---\n${front}\n---\n\n${content.trim()}\n\n<!--\n${note.trim()}\n-->\n`);
 row.renderedTitle=content.match(/^# (.*)$/m)?.[1];
}
if(output.length!==plan.mainSlides+plan.appendixSlides)throw new Error('Unexpected total');
let start=0;
for(const [index,count] of plan.partSizes.entries()){
 await fs.writeFile(`slides/part${index+1}.md`,output.slice(start,start+count).join('\n'));start+=count;
}
if(start!==output.length)throw new Error('Part sizes do not cover deck');
await fs.writeFile('plans/CAUSAL_DECK_ORDER.json',JSON.stringify(plan,null,2)+'\n');
console.log(`Rebuilt ${plan.mainSlides} main slides + ${plan.appendixSlides} evidence appendix slides, preserving 27 source-paper identities.`);
