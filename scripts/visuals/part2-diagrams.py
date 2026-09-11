#!/usr/bin/env python3
"""Reproduce the final eight Part 2 teaching diagrams as editable SVGs.

Run from any directory. Use --output-dir to render into a staging directory.
PNG delivery copies are made by render-part2-diagrams.mjs.
"""
from pathlib import Path
import argparse
import math, html

REPO = Path(__file__).resolve().parents[2]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output-dir', type=Path, default=REPO / 'public' / 'diagrams')
args = parser.parse_args()
OUT = args.output_dir.resolve()
OUT.mkdir(parents=True, exist_ok=True)
W,H=1136,360
BG='#f6f8fa'; INK='#142233'; BLUE='#1f5fae'; TEAL='#008b9a'; SECOND='#586879'; RULE='#d4dde7'; ORANGE='#a95018'; PALE='#e7eff9'; WHITE='#ffffff'
class Svg:
 def __init__(self):
  self.a=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 1 L 9 5 L 0 9" fill="none" stroke="context-stroke" stroke-width="1.5"/></marker></defs><rect width="1136" height="360" fill="{BG}"/>']
 def add(self,x): self.a.append(x)
 def text(self,x,y,t,size=26,color=INK,anchor='start',weight=400): self.add(f'<text x="{x}" y="{y}" font-family="Pretendard, sans-serif" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{color}">{html.escape(t)}</text>')
 def line(self,x1,y1,x2,y2,c=RULE,w=2,dash=None,arrow=False): self.add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{w}" '+(f'stroke-dasharray="{dash}" ' if dash else '')+('marker-end="url(#arrow)" ' if arrow else '')+'/>')
 def path(self,d,c=BLUE,w=3,fill='none',dash=None,arrow=False): self.add(f'<path d="{d}" fill="{fill}" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" '+(f'stroke-dasharray="{dash}" ' if dash else '')+('marker-end="url(#arrow)" ' if arrow else '')+'/>')
 def rect(self,x,y,w,h,fill=WHITE,stroke=RULE,sw=2,r=0): self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
 def circle(self,x,y,r,c=BLUE,fill=BG,w=3): self.add(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{c}" stroke-width="{w}"/>')
 def head(self,x,y,s=1):
  self.add(f'<g transform="translate({x},{y}) scale({s})">');self.circle(0,0,25,INK,WHITE,3);self.path('M -7 -23 L 0 -34 L 7 -23',INK,3,WHITE);self.path('M -24 -9 C -37 -11 -37 13 -24 12 M 24 -9 C 37 -11 37 13 24 12',INK,3);self.add('</g>')
 def bell(self,x,y,s=1,c=BLUE):
  self.add(f'<g transform="translate({x},{y}) scale({s})">'); self.path('M -18 10 L -13 3 L -13 -10 Q -13 -24 0 -24 Q 13 -24 13 -10 L 13 3 L 18 10 Z',c,3,WHITE); self.path('M -5 15 Q 0 21 5 15 M 0 -24 L 0 -29 M -22 -19 L -28 -25 M 22 -19 L 28 -25',c,3); self.add('</g>')
 def voice(self,x,y,s=1,c=TEAL):
  self.add(f'<g transform="translate({x},{y}) scale({s})">');self.circle(-8,-11,9,c,WHITE,3);self.path('M -25 17 Q -25 0 -8 0 Q 7 0 7 16 M 11 -13 Q 18 -7 11 -1 M 20 -21 Q 34 -7 20 7',c,3);self.add('</g>')
 def wave(self,x,y,w,a,c=BLUE,phase=0):
  pts=[]
  for i in range(181):
   t=i/180;env=(math.sin(math.pi*t)**1.2)*(.7+.3*math.cos(6*math.pi*t));v=math.sin(18*math.pi*t+phase)*env+.2*math.sin(31*math.pi*t)
   pts.append((x+w*t,y-a*v))
  self.line(x,y,x+w,y,RULE,1.5)
  self.path('M '+' L '.join(f'{xx:.1f},{yy:.1f}' for xx,yy in pts),c,2.6)
 def save(self,name): self.add('</svg>');(OUT/name).write_text(''.join(self.a))
# S38 concrete source identity and position swap
s=Svg();s.text(568,34,'왼쪽에서 나는 소리는?',30,INK,'middle',600)
for i,(cx,swap) in enumerate([(275,False),(861,True)]):
 s.text(cx,78,'장면 B · 위치만 교환' if swap else '장면 A',24,TEAL,'middle',600)
 s.path(f'M {cx-195} 240 Q {cx} 115 {cx+195} 240',RULE,2,dash='6 7')
 s.head(cx,216,1.2);s.text(cx,281,'청취자',24,SECOND,'middle')
 for px,isbell in [(cx-174,not swap),(cx+174,swap)]:
  s.line(px,164,cx+(-32 if px<cx else 32),204,RULE,2)
  (s.bell if isbell else s.voice)(px,142,1.25)
  s.text(px,197,'알람' if isbell else '말소리',26,BLUE if isbell else TEAL,'middle',600)
 s.text(cx-178,259,'왼쪽',24,SECOND,'middle');s.text(cx+178,259,'오른쪽',24,SECOND,'middle')
 s.text(cx,337,'답: 말소리' if swap else '답: 알람',30,BLUE,'middle',700)
s.line(568,95,568,324,RULE,2);s.save('p2-s38-position-swap.svg')
# S40 feature weight selection preceding shared parameter branches
s=Svg();s.text(125,34,'바이노럴',26,TEAL,'middle',600);s.wave(25,128,185,38,BLUE);s.wave(25,227,185,32,TEAL);s.text(8, ninety:=89,'L',24,BLUE);s.text(8,188,'R',24,TEAL)
s.line(226,175,275,175,SECOND,3,arrow=True)
s.text(362,34,'입력 특징',26,TEAL,'middle',600)
# offset feature planes show actual changing image intensities but illustrative, no measured attention claim
for k in range(3):
 x=287+k*18;y=104+k*18
 s.rect(x,y,134,124,WHITE,RULE,1.5)
 for r in range(6):
  for c in range(7):
   op=.16+.65*((r*3+c*5+k*2)%9)/8
   s.add(f'<rect x="{x+c*18+4}" y="{y+r*18+5}" width="15" height="15" fill="{BLUE if k%2==0 else TEAL}" opacity="{op}"/>')
s.text(362,320,'mel · IPD · ILD · GCC',24,SECOND,'middle')
s.text(697,34,'과제별 특징 선택',26,TEAL,'middle',600)
s.line(460,178,496,178,SECOND,3)
for y,c,typ in [(98,BLUE,'사건'),(187,TEAL,'방향'),(276,BLUE,'거리')]:
 s.path(f'M 496 178 L 496 {y} L 520 {y}',c,2.5)
 for k,h in enumerate([20,38,28,48] if typ=='사건' else [42,24,48,28] if typ=='방향' else [30,46,24,40]):s.rect(526+k*18,y-h/2,11,h,c,c,0)
 s.line(610,y,644,y,c,2.5,arrow=True)
 s.rect(654,y-29,168,58,WHITE,RULE,2)
 for k in range(5):
  s.rect(672+k*26,y-16,16,32,PALE,BLUE,1.4)
 s.line(832,y,895,y,c,2.5,arrow=True)
 if typ=='사건':s.bell(939,y+6,.85,c)
 elif typ=='방향':
  s.circle(939,y,24,c,WHITE,2);s.line(939,y,957,y-17,c,3,arrow=True)
 else:
  s.line(915,y,966,y,c,3);s.line(915,y-10,915,y+10,c,2);s.line(966,y-10,966,y+10,c,2)
 s.text(993,y+9,typ,27,c,weight=600)
s.line(738,128,738,158,SECOND,2,'4 4');s.line(738,217,738,247,SECOND,2,'4 4');s.text(730,341,'공유: patch embedding · Transformer',24,SECOND,'middle');s.save('p2-s40-feature-selection.svg')
# S45 same wave, gain amplitude only three alternatives
s=Svg()
for i,(name,gl,gr) in enumerate([('Left',.9,.3),('Center',.65,.65),('Right',.3,.9)]):
 x=i*383;s.text(x+182,36,name,30,BLUE,'middle',700)
 if i:s.line(x-8,22,x-8,324,RULE,2)
 s.text(x+24,97,'L',26,BLUE,weight=600);s.wave(x+66,121,275,50*gl,BLUE)
 s.text(x+24,210,'R',26,TEAL,weight=600);s.wave(x+66,216,275,50*gr,TEAL)
 s.line(x+62,310,x+340,310,SECOND,2,arrow=True);s.text(x+180,343,'시간',24,SECOND,'middle')
 # ratio visually explicit without an arbitrary numerical panning law
 s.text(x+184,286,'오른쪽 gain 우세' if gl<gr else '동일 gain' if gl==gr else '왼쪽 gain 우세',26,INK,'middle',500)
s.save('p2-s45-gain-waveforms.svg')
# S49 model contracts across a clear training/inference boundary
s=Svg();s.text(374,29,'학습에서 제공',26,TEAL,'middle',600);s.text(876,29,'추론에서 제공',26,TEAL,'middle',600);s.line(590,48,590,348,BLUE,2,'7 7')
rows=[('BAT / DSpAST',78,'공간 사전학습 → QA','binaural'),('OWL',157,'depth·RIR → 고정 QA','owl'),('Dual-BEATs',236,'BEATs 고정 + 연결','gain'),('PhaseCoder',315,'공간 사전학습 → SFT','phase')]
for name,y,training,kind in rows:
 s.text(6,y+9,name,24,INK,weight=600)
 if kind!='owl':s.text(381,y+9,training,24,INK,'middle')
 if kind=='owl':
  # depth image train only and crossed boundary path
  for k in range(3):s.rect(220+k*7,y-22+k*7,34,29,WHITE,TEAL,2)
  s.text(414,y-9,'depth·RIR 지도',24,INK,'middle');s.text(414,y+22,'QA: encoder 고정',24,INK,'middle')
  s.line(535,y,565,y,ORANGE,2);s.line(565,y-11,565,y+11,ORANGE,3)
  s.head(654,y,.57);s.text(751,y+9,'바이노럴',24,INK,'middle');s.text(958,y+9,'+ 질문',24,INK,'middle')
 elif kind=='gain':
  s.wave(643,y-10,72,15,BLUE);s.wave(643,y+15,72,7,TEAL);s.text(818,y+9,'gain · dither',24,INK,'middle');s.text(1020,y+9,'방향',24,BLUE,'middle')
 elif kind=='phase':
  for px,py in [(646,y-15),(673,y+12),(704,y-8)]:s.circle(px,py,6,BLUE,BLUE,1)
  s.path(f'M 646 {y-15} L 673 {y+12} L 704 {y-8}',RULE,2)
  s.text(803,y+9,'다채널 + mono',24,INK,'middle');s.text(1010,y+9,'좌표 + 질문',24,BLUE,'middle',600)
 else:
  s.head(654,y,.57);s.text(799,y+9,'합성 바이노럴',24,INK,'middle');s.text(1010,y+9,'+ 질문',24,INK,'middle')
 if y!=315:s.line(0,y+40,1136,y+40,RULE,1.5)
s.save('p2-s49-learning-inference.svg')
# S50 room with source association, timelines and environment
s=Svg();s.text(291,30,'同一 음원에 속성을 연결'.replace('同一','같은'),26,TEAL,'middle',600)
s.path('M 58 75 L 504 75 L 558 304 L 21 304 Z',RULE,3,WHITE)
s.path('M 58 75 L 87 50 L 521 50 L 558 304 M 504 75 L 521 50',RULE,2)
s.head(279,256,.9)
s.bell(128,132,1.1,BLUE);s.voice(437,148,1.1,TEAL)
s.line(150,149,255,236,BLUE,2.5,arrow=True);s.line(416,164,302,237,TEAL,2.5,arrow=True)
s.text(110,190,'알람 A',26,BLUE,'middle',600);s.text(463,207,'말소리 B',26,TEAL,'middle',600)
s.text(283,189,'방향·거리',24,SECOND,'middle')
s.path('M 102 106 Q 112 90 129 88 Q 168 88 180 121',BLUE,2,dash='5 5');s.path('M 457 91 Q 491 112 495 145',TEAL,2,dash='5 5')
s.text(277,340,'방: 잔향 · 크기 / 배경: 종류 · 음압',24,SECOND,'middle')
s.line(596,44,596,336,RULE,2);s.text(869,30,'음원별 기록 · 최대 4개',26,TEAL,'middle',600)
for y,typ,c in [(103,'알람 A',BLUE),(220,'말소리 B',TEAL)]:
 s.text(639,y-20,typ,26,c,weight=600);s.wave(754,y,321,29,c)
 s.rect(799 if typ=='알람 A' else 849,y+39,149 if typ=='알람 A' else 199,9,c,c,0)
 s.text(636,y+52,'발생 구간',24,SECOND)
s.text(864,340,'소리 설명 · 방향·거리 · 음압·명료도',24,INK,'middle');s.save('p2-s50-scene-attributes.svg')
# S59 three time requirements shown as three distinct observables
s=Svg()
for i,t in enumerate(['사건 순서','연속 이동','질문 관련 구간']):s.text(i*383+182,31,t,28,TEAL,'middle',600)
s.line(374,53,374,346,RULE,2);s.line(757,53,757,346,RULE,2)
# event-order true timeline nonoverlapping bars
s.bell(40,112,.8);s.voice(40,228,.8);s.rect(86,91,97,36,BLUE,BLUE,0);s.rect(207,207,104,36,TEAL,TEAL,0);s.text(135,166,'먼저',25,BLUE,'middle');s.text(259,282,'나중',25,TEAL,'middle');s.line(82,319,330,319,SECOND,2,arrow=True);s.text(205,350,'시간',24,SECOND,'middle')
# one source continuous left to right position over time
s.line(470,307,470,81,SECOND,2);s.line(470,307,721,307,SECOND,2,arrow=True);s.text(444,108,'오른쪽',24,SECOND,'end');s.text(444,285,'왼쪽',24,SECOND,'end');s.path('M 487 267 C 545 267 580 221 606 190 S 662 116 707 103',BLUE,4,arrow=True);s.bell(500,259,.6,BLUE);s.bell(684,117,.6,BLUE);s.text(600,350,'시간',24,SECOND,'middle')
# temporalmask
s.rect(890,77,125,208,PALE,PALE,0);s.wave(795,161,321,52,BLUE);s.path('M 795 265 L 890 265 L 890 233 L 1015 233 L 1015 265 L 1116 265',TEAL,3);s.text(950,108,'알람 구간',24,BLUE,'middle',600);s.line(795,319,1116,319,SECOND,2,arrow=True);s.text(951,350,'시간',24,SECOND,'middle');s.save('p2-s59-time-requirements.svg')
# S62 a continuous same-source identity trajectory, two snapshots clearly time conditioned
s=Svg();s.text(152,30,'위치',26,TEAL,'middle',600);s.text(683,30,'같은 A·B를 시간 사이에 연결',26,TEAL,'middle',600)
s.line(184,289,184,72,SECOND,2);s.text(160,95,'오른쪽',26,SECOND,'end');s.text(160,285,'왼쪽',26,SECOND,'end')
s.line(184,319,1094,319,SECOND,2,arrow=True);s.text(266,351,'처음',24,SECOND,'middle');s.text(1021,351,'나중',24,SECOND,'middle');s.text(647,351,'시간',24,SECOND,'middle')
s.rect(951,53,140,249,PALE,PALE,0)
s.path('M 269 269 C 453 267 483 230 641 179 S 848 101 1024 89',BLUE,4)
s.path('M 269 89 C 453 90 483 130 641 181 S 848 256 1024 269',TEAL,4)
for x,y in [(269,269),(1024,89)]:s.bell(x,y,.72,BLUE)
for x,y in [(269,89),(641,181),(1024,269)]:
 if x!=641:s.voice(x,y,.72,TEAL)
s.text(323,249,'알람 A',26,BLUE,weight=600);s.text(323,122,'말소리 B',26,TEAL,weight=600)
s.text(983,160,'A는 오른쪽',24,BLUE,'middle',600);s.text(983,203,'B는 왼쪽',24,TEAL,'middle',600);s.save('p2-s62-source-trajectories.svg')
# S65 event-order grids: arrows denote time, never motion
s=Svg();s.text(568,30,'“왼쪽 알람이 울린 뒤, 오른쪽에서 말소리”',28,INK,'middle',600)
for i,(name,events) in enumerate([('기준',[(0,1,'bell'),(1,0,'voice')]),('순서만 반전',[(0,0,'voice'),(1,1,'bell')]),('위치만 교환',[(0,0,'bell'),(1,1,'voice')])]):
 x=i*383
 if i:s.line(x-9,52,x-9,350,RULE,2)
 s.text(x+188,83,name,26,TEAL if i==0 else ORANGE,'middle',600)
 s.text(x+84,147,'오른쪽',24,SECOND,'end');s.text(x+84,240,'왼쪽',24,SECOND,'end')
 for y in [139,233]:s.line(x+107,y,x+341,y,RULE,1.5,'4 6')
 for xx in [154,290]:s.line(x+xx,114,x+xx,274,RULE,1.5,'4 6')
 for tx,py,typ in events:
  px=x+[154,290][tx];y=[139,233][py]
  s.circle(px,y,31,BLUE if typ=='bell' else TEAL,WHITE,2)
  (s.bell if typ=='bell' else s.voice)(px,y,.75)
 s.line(x+111,303,x+343,303,SECOND,2,arrow=True);s.text(x+154,340,'먼저',24,SECOND,'middle');s.text(x+290,340,'나중',24,SECOND,'middle')
s.save('p2-s65-event-negatives.svg')
print('created',len(list(OUT.glob('p2-*.svg'))),'diagrams')
