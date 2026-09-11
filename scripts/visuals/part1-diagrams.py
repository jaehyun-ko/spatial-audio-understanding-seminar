"""Original, schematic teaching figures. No plotted data are experimental measurements."""
from pathlib import Path
import argparse, math, html

ROOT = Path(__file__).resolve().parents[2]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output-dir', type=Path, default=ROOT / 'public' / 'diagrams',
                    help='SVG destination; relative paths are resolved from the current directory')
OUT = parser.parse_args().output_dir.resolve()
OUT.mkdir(parents=True, exist_ok=True)
W,H=1136,400
P='#f6f8fa'; I='#142233'; S='#586879'; B='#1f5fae'; T='#007b80'; L='#008b9a'; R='#d4dde7'; O='#a95018'; BS='#e7eff9'; TS='#e4f1f1'
class SVG:
 def __init__(self):
  self.e=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="{P}"/><defs>']
  for name,c in [('b',B),('t',T),('i',S),('o',O)]: self.e.append(f'<marker id="{name}" markerWidth="8" markerHeight="8" refX="7" refY="3.5" orient="auto"><path d="M0 0 L7 3.5 L0 7 Z" fill="{c}"/></marker>')
  self.e.append('</defs><g font-family="Pretendard, Arial, sans-serif" fill="'+I+'" stroke-linecap="round" stroke-linejoin="round">')
 def raw(self,x): self.e.append(x)
 def text(self,x,y,s,size=24,c=I,weight=400,anchor='start'):
  self.raw(f'<text x="{x}" y="{y}" font-size="{size}" fill="{c}" font-weight="{weight}" text-anchor="{anchor}">{html.escape(s)}</text>')
 def line(self,x1,y1,x2,y2,c=R,w=2,dash=None,arrow=False):
  self.raw(f'<path d="M{x1} {y1} L{x2} {y2}" fill="none" stroke="{c}" stroke-width="{w}"'+(f' stroke-dasharray="{dash}"' if dash else '')+(f' marker-end="url(#{ {B:"b",T:"t",O:"o"}.get(c,"i")})"' if arrow else '')+'/>')
 def path(self,d,c=B,w=3,fill='none',dash=None,arrow=False):
  self.raw(f'<path d="{d}" stroke="{c}" stroke-width="{w}" fill="{fill}"'+(f' stroke-dasharray="{dash}"' if dash else '')+(f' marker-end="url(#{ {B:"b",T:"t",O:"o"}.get(c,"i")})"' if arrow else '')+'/>')
 def rect(self,x,y,w,h,fill='none',stroke=R,sw=2,rx=0): self.raw(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
 def circle(self,x,y,r,fill=P,stroke=I,w=2): self.raw(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{w}"/>')
 def label(self,x,y,s): self.text(x,y,s,24,L,600)
 def wave(self,x,y,w=200,amp=25,shift=0,c=B,pulse=False,periods=5):
  pts=[]
  for n in range(181):
   u=n/180; v=u-shift
   a=math.exp(-((v-.45)/.18)**2) if pulse else (.5+.5*abs(math.sin(math.pi*(v*3+.1))) if periods==9 else 1)
   z=a*math.sin(2*math.pi*periods*v)
   pts.append(f'{x+u*w:.2f},{y-amp*z:.2f}')
  self.raw('<polyline points="'+' '.join(pts)+f'" fill="none" stroke="{c}" stroke-width="3"/>')
 def mic(self,x,y,name=None,c=T):
  self.rect(x-9,y-21,18,34,P,c,3,9); self.path(f'M{x-15} {y-2} v9 a15 15 0 0 0 30 0 v-9',c,3); self.line(x,y+23,x,y+35,c,3); self.line(x-11,y+35,x+11,y+35,c,3)
  if name:self.text(x,y+65,name,22,c,600,'middle')
 def speaker(self,x,y,c=B,label=None,scale=1):
  self.raw(f'<g transform="translate({x} {y}) scale({scale})">'); self.path('M-24 -11 H-11 L8 -28 V28 L-11 11 H-24 Z',c,3,BS if c==B else TS)
  self.path('M19 -17 Q36 0 19 17',c,3); self.path('M29 -28 Q57 0 29 28',c,3); self.raw('</g>')
  if label:self.text(x,y+64,label,25,c,600,'middle')
 def head(self,x,y,size=45):
  self.raw(f'<ellipse cx="{x}" cy="{y}" rx="{size*.8}" ry="{size}" fill="{P}" stroke="{I}" stroke-width="3"/>')
  self.path(f'M{x-10} {y-size+2} L{x} {y-size-14} L{x+10} {y-size+2}',I,3,P)
  for d in [-1,1]:self.raw(f'<ellipse cx="{x+d*size*.84}" cy="{y}" rx="8" ry="17" fill="{TS}" stroke="{T}" stroke-width="3"/>')
 def encoder(self,x,y,w=110,h=78,label='인코더',frozen=False):
  for off in [14,7,0]:self.rect(x+off,y-off,w,h,P,T if frozen else B,2,2)
  self.text(x+w/2,y+h/2+8,label,24,T if frozen else B,600,'middle')
  if frozen:self.lock(x+w-4,y-18)
 def lock(self,x,y):
  self.rect(x-11,y,22,18,P,T,2,2);self.path(f'M{x-7} {y} v-6 a7 7 0 0 1 14 0 v6',T,2)
 def strip(self,x,y,mask=(),w=240,h=58,channels=1,c=B):
  cw=w/12
  for row in range(channels):
   for j in range(12):
    fill=P if j in mask else (BS if c==B else TS)
    self.rect(x+j*cw,y+row*(h+10),cw-3,h,fill,R,1)
    if j in mask:self.line(x+j*cw+4,y+row*(h+10)+h-5,x+(j+1)*cw-7,y+row*(h+10)+5,R,2)
    else:
     for k in range(3):self.rect(x+j*cw+3,y+row*(h+10)+7+k*15,max(2,cw-7),6+(j+k)%4,c,'none',0)
 def save(self,name):
  self.raw('</g></svg>');(OUT/(name+'.svg')).write_text(''.join(self.e))

# S03: directly compare two observations, not three paragraphs.
s=SVG()
for x in [365,753]:s.line(x,25,x,360)
for x,label in [(16,'도착 시간'),(405,'신호 크기'),(792,'주파수별 위상')]:s.label(x,35,label)
s.text(16,83,'M₁',22,B,600);s.text(16,224,'M₂',22,T,600)
for y,c,sh in [(132,B,0),(272,T,.18)]:
 s.line(40,y,335,y);s.wave(45,y,285,36,sh,c,True,4)
s.line(173,88,173,310,S,1,'5 5');s.line(224,215,224,310,S,1,'5 5');s.line(173,329,224,329,B,2,arrow=True);s.line(224,329,173,329,B,2,arrow=True);s.text(198,369,'시간차',24,B,600,'middle')
for y,c,amp in [(132,B,48),(272,T,24)]:s.line(420,y,723,y);s.wave(426,y,280,amp,0,c,True,4)
s.line(710,84,710,132,B,2,arrow=True);s.line(710,132,710,84,B,2,arrow=True);s.line(710,248,710,272,T,2,arrow=True);s.text(562,369,'레벨차',24,B,600,'middle')
for y,c,sh in [(132,B,0),(272,T,.065)]:s.line(808,y,1120,y);s.wave(810,y,304,36,sh,c,False,3)
s.line(835,81,835,316,S,1,'5 5');s.line(855,221,855,316,S,1,'5 5');s.text(955,369,'주파수마다 다른 위상차',24,B,600,'middle')
s.save('p1-channel-cues')

# S06: source strength, propagation and reverberation all act on the recorded signal.
s=SVG();s.rect(25,38,655,295,P,R,3);s.label(45,26,'방의 전달 경로');s.speaker(118,225,label='음원 레벨');s.mic(580,225,'관측 장치')
s.line(169,225,555,225,B,4,arrow=True);s.text(355,257,'직접음 · 거리',24,B,600,'middle')
s.path('M165 207 L360 39 L564 207',T,3,dash='8 6');s.text(380,96,'반사',24,T,600)
s.path('M163 239 L363 332 L560 247',T,3,dash='8 6')
s.line(710,220,770,220,S,3,arrow=True);s.label(800,80,'두 채널 신호');s.wave(800,166,300,38,0,B,True,6);s.wave(800,270,300,28,.06,T,True,6)
s.text(800,355,'여러 원인이 함께 반영됨',24,S)
s.save('p1-room-observation')

# S07: same plane-wave direction and origin, two baselines; dashed wavefronts parallel.
s=SVG()
for x,label,d in [(25,'배열 A',100),(595,'배열 B',210)]:
 s.label(x+10,34,label);ox=x+250; oy=257
 for k in [-1,0,1,2]:s.line(ox-148+k*63,oy-78,ox-40+k*63,oy-213,R,2)
 s.line(ox-98,oy-188,ox-16,oy-123,B,3,arrow=True);s.text(x+302,83,'같은 음원 방향',23,B,600)
 s.line(ox-230,oy,ox+230,oy,S,2,arrow=True);s.text(ox+231,oy-13,'x',24,S)
 s.circle(ox,oy,4,S,S);s.text(ox,oy+35,'O',22,S,400,'middle')
 s.mic(ox-d/2,oy-18,'M₁');s.mic(ox+d/2,oy-18,'M₂')
 s.line(ox-d/2,oy+89,ox+d/2,oy+89,T,2);s.line(ox-d/2,oy+80,ox-d/2,oy+96,T,2);s.line(ox+d/2,oy+80,ox+d/2,oy+96,T,2)
 s.text(ox,oy+127,'간격 d' if d==100 else '더 넓은 간격',24,T,600,'middle')
s.line(558,26,558,358);s.text(565,205,'→',31,S,600,'middle');s.save('p1-array-baseline')

# S08: an angular response has two unlabeled peaks, then a separate semantic question.
s=SVG();s.label(20,32,'혼합 관측');s.wave(25,160,230,43,0,B,True,5);s.wave(25,254,230,35,.06,T,True,5);s.text(130,334,'말소리 + 알람',26,I,600,'middle');s.line(295,207,365,207,S,3,arrow=True)
s.label(400,32,'활성 방향 후보');s.line(403,300,820,300,S,2,arrow=True);s.line(423,300,423,87,S,2,arrow=True)
pts=[]
for j in range(201):
 x=425+1.85*j;y=300-175*math.exp(-((j-53)/15)**2)-155*math.exp(-((j-151)/18)**2);pts.append(f'{x:.1f},{y:.1f}')
s.raw('<polyline points="'+' '.join(pts)+f'" stroke="{B}" stroke-width="4" fill="none"/>')
for x in [523,704]:s.circle(x,300,6,B,B);s.text(x,342,'이름 없음',24,S,400,'middle')
s.text(821,329,'방향',23,S,400,'end');s.line(855,207,915,207,S,3,arrow=True);s.text(936,172,'어느 후보가',26,I,600);s.text(936,212,'알람인가?',28,B,600);s.text(936,277,'사건과 연결',24,S);s.save('p1-direction-then-event')

# S09: geometry yields delays, which index observed correlation; aggregate array pairs.
s=SVG();s.label(20,31,'후보와 배열');s.circle(90,285,9,T,T);s.circle(215,285,9,T,T);s.circle(278,230,9,T,T);s.line(90,285,280,88,B,3,arrow=True);s.line(215,285,280,88,R,2);s.line(278,230,280,88,R,2);s.text(280,64,'후보 방향',24,B,600,'middle');s.text(175,345,'쌍별 기대 지연',24,T,600,'middle');s.line(320,205,367,205,S,3,arrow=True)
s.label(400,31,'관측 관계와 대조')
for y,peak in [(118,545),(206,584),(294,531)]:
 s.line(407,y+33,746,y+33,R,2);pts=[]
 for j in range(151):
  xx=410+j*2.2;yy=y+33-57*math.exp(-((xx-peak)/30)**2)-8*math.exp(-((xx-690)/25)**2);pts.append(f'{xx:.1f},{yy:.1f}')
 s.raw('<polyline points="'+' '.join(pts)+f'" stroke="{T}" stroke-width="3" fill="none"/>');s.line(peak,y-29,peak,y+41,B,2,'4 4');s.circle(peak,y-24,5,B,B)
s.text(574,365,'후보가 예측한 지연에서 읽기',23,S,400,'middle');s.line(775,205,826,205,S,3,arrow=True)
s.label(860,31,'쌍들의 일치 합산');s.line(858,294,1110,294,S,2,arrow=True);pts=[]
for j in range(151):
 xx=865+j*1.55;yy=292-165*math.exp(-((j-91)/16)**2)-32*math.exp(-((j-26)/20)**2);pts.append(f'{xx:.1f},{yy:.1f}')
s.raw('<polyline points="'+' '.join(pts)+f'" stroke="{B}" stroke-width="4" fill="none"/>');s.line(1006,126,1006,305,B,2,'5 5');s.text(987,347,'공간 응답',25,B,600,'middle');s.save('p1-candidate-delay-match')

# S12: microphones and actual waveform are identical; angular query rays become denser.
s=SVG();s.label(17,30,'같은 녹음 · 같은 배열');s.wave(25,104,265,30,0,B,True,5);s.wave(25,181,265,24,.06,T,True,5);s.mic(112,267,'M₁');s.mic(215,267,'M₂');s.line(323,208,378,208,S,3,arrow=True)
for ox,angles,title in [(545,range(0,181,45),'성긴 후보 격자'),(946,range(0,181,15),'촘촘한 후보 격자')]:
 oy=298;s.label(ox-130,31,title)
 for a in angles:
  rad=math.radians(a);ex=ox+155*math.cos(rad);ey=oy-155*math.sin(rad);s.line(ox,oy,ex,ey,T,2);s.circle(ex,ey,5,T,T)
 s.path(f'M{ox-155} {oy} A155 155 0 0 1 {ox+155} {oy}',R,2)
 s.circle(ox,oy,6,B,B);s.text(ox,350,'물어보는 방향 목록',24,S,400,'middle')
s.text(745,207,'→',35,S,600,'middle');s.save('p1-query-grid')

# S15: event activities in time are linked to separate direction arrows.
s=SVG();s.label(20,30,'사건 + 활성 시점');s.text(23,135,'말소리',28,T,600);s.text(23,255,'알람',28,B,600);s.line(185,330,775,330,S,2,arrow=True);s.text(775,367,'시간',24,S,400,'end')
for y,c,spans in [(99,T,[(210,175),(506,175)]),(219,B,[(310,150),(578,120)])]:
 s.line(185,y+29,750,y+29,R,2)
 for x,w in spans:s.rect(x,y,w,57,TS if c==T else BS,c,2,2);s.wave(x+12,y+29,w-24,17,0,c,False,4)
s.label(852,30,'방향과 결합');s.head(961,245,44);s.line(924,215,846,131,T,4,arrow=True);s.line(998,215,1075,131,B,4,arrow=True);s.text(841,101,'말소리',25,T,600,'middle');s.text(1078,101,'알람',25,B,600,'middle');s.text(961,353,'활성일 때의 방향',24,S,400,'middle');s.save('p1-seld-timeline')

# S16: microphone samples vs ear filtering vs spherical harmonic basis components.
s=SVG()
for x in [361,749]:s.line(x,26,x,373)
s.label(20,30,'마이크 배열');s.line(55,230,306,230,S,2,arrow=True)
for x,y in [(75,224),(165,154),(277,216)]:s.mic(x,y)
s.text(185,312,'서로 다른 위치의 관측',24,I,600,'middle');s.text(185,354,'좌표: 방법별 입력 조건',22,S,400,'middle')
s.label(401,30,'바이노럴');s.head(553,180,67);s.line(423,180,490,180,B,3,arrow=True);s.line(623,180,690,180,T,3,arrow=True);s.text(550,312,'두 귀의 관측',24,I,600,'middle');s.text(550,354,'머리·귓바퀴의 전달 특성',22,S,400,'middle')
s.label(792,30,'FOA');s.circle(844,134,29,BS,B,2);s.text(844,199,'W',23,B,600,'middle')
for cx,cy,label,angle in [(967,134,'X',0),(844,246,'Y',45),(967,246,'Z',90)]:
 s.raw(f'<g transform="translate({cx} {cy}) rotate({angle})"><ellipse cx="-21" cy="0" rx="21" ry="17" fill="{BS}" stroke="{B}" stroke-width="2"/><ellipse cx="21" cy="0" rx="21" ry="17" fill="{TS}" stroke="{T}" stroke-width="2"/></g>');s.text(cx,cy+55,label,23,B,600,'middle')
s.text(930,354,'1차 구면조화 성분',24,I,600,'middle');s.save('p1-input-representations')

# S17: trainable gradient span is the main visible variable.
s=SVG()
for y,label,frozen in [(91,'고정 표현 판독',True),(259,'전체 미세조정',False)]:
 s.label(15,y+16,label);s.wave(266,y+21,140,26,0,B,True,4);s.line(435,y+21,475,y+21,S,3,arrow=True);s.encoder(500,y-16,130,74,'인코더',frozen)
 s.line(655,y+21,710,y+21,S,3,arrow=True);s.rect(739,y-16,129,74,BS,B,2,2);s.text(803,y+29,'판독기',25,B,600,'middle');s.line(890,y+21,944,y+21,S,3,arrow=True);s.text(1010,y+30,'출력',27,I,600,'middle')
 s.path(f'M1000 {y+71} V{y+91} H{803 if frozen else 565} V{y+62}',B,2,arrow=True)
 s.text(843 if frozen else 704,y+125,'정답으로 업데이트',23,B,600,'middle')
s.save('p1-frozen-finetune')

# S18: aligned multichannel crops and their representations are the actual objects.
s=SVG();s.label(20,30,'한 다채널 녹음');
for y,c in [(113,B),(175,T)]:s.wave(20,y,465,24,0,c,False,9)
s.rect(68,72,132,143,'none',B,3);s.rect(303,72,132,143,'none',T,3);s.text(134,253,'구간 A',25,B,600,'middle');s.text(369,253,'구간 B',25,T,600,'middle');s.text(255,334,'시간 구간만 다름 · 채널 관계 유지',24,S,400,'middle')
s.path('M493 115 H550 L592 143',B,3,arrow=True);s.path('M493 176 H550 L592 177',T,3,arrow=True);s.encoder(613,123,129,83,'공유 인코더');s.line(770,163,831,163,S,3,arrow=True)
s.label(858,30,'표현 공간');s.circle(918,146,15,BS,B,3);s.circle(1052,250,15,TS,T,3);s.text(899,117,'A',24,B,600);s.text(1066,282,'B',24,T,600);s.line(939,161,978,191,B,3,arrow=True);s.line(1031,234,992,204,T,3,arrow=True);s.text(983,338,'가깝게 학습',26,B,600,'middle');s.save('p1-contrastive-crops')

# S20: branch-specific masking shown as aligned STFT time frames.
s=SVG();s.label(15,31,'공간 분기');s.label(403,31,'스펙트럼 분기');s.text(15,73,'같은 프레임을 함께 가림',22,S);s.text(403,73,'상보적으로 가림',22,S)
for x,spectral in [(45,False),(430,True)]:
 for row in [0,1]:
  mask=[3,4,8,9] if not spectral else ([1,3,5,7,9,11] if row==0 else [0,2,4,6,8,10]);s.strip(x,111+row*88,mask,w=270,h=57,c=B if row==0 else T)
  s.text(x-30,150+row*88,str(row+1),21,B if row==0 else T,600)
 s.text(x+130,307,'시간 프레임 →',23,S,400,'middle')
s.path('M332 150 H370 V346 H753 V228',B,2,arrow=True);s.line(718,223,796,223,T,3,arrow=True);s.encoder(820,174,122,83,'복원기');s.line(962,214,1005,214,S,3,arrow=True)
s.label(833,31,'복원 목표');s.strip(1025,160,[0,1,4,5,6,7,10,11],w=104,h=103,c=B);s.text(979,327,'가린 STFT',24,B,600,'middle');s.text(979,363,'한 채널의 관측',22,S,400,'middle');s.save('p1-ccsr-masking')

# S26: early vs late fusion as alternative connections into the same processing depth.
s=SVG();s.label(12,29,'결합 위치만 비교');
for y,title,target in [(115,'early',514),(276,'late',800)]:
 s.text(15,y+15,title,27,B,600);s.text(180,y-38,'FOA',24,T,600,'middle');s.strip(125,y-15,[],w=105,h=44,c=T);s.line(250,y+9,298,y+9,S,3,arrow=True)
 for x,label in [(323,'낮은 특징'),(624,'높은 특징')]:s.encoder(x,y-30,187,80,label)
 s.line(535,y+9,593,y+9,S,3,arrow=True);s.line(839,y+9,900,y+9,S,3,arrow=True);s.text(958,y+17,'SELD',28,I,600,'middle')
 s.text(376,y+101,'태깅 의미 특징',24,T,600);s.path(f'M543 {y+94} H{target} V{y+61}',T,3,arrow=True)
s.save('p1-fusion-depth')

# S29: pretrain once, then transfer fixed encoder to supervised probe.
s=SVG();s.label(20,32,'마스킹 사전학습');s.strip(30,96,[2,3,7,8],w=220,h=64);s.line(278,128,326,128,S,3,arrow=True);s.encoder(350,90,145,80,'인코더');s.line(522,128,570,128,S,3,arrow=True);s.rect(598,90,120,80,BS,B,2,2);s.text(658,137,'복원기',24,B,600,'middle');s.line(744,128,793,128,S,3,arrow=True);s.strip(820,96,[],w=250,h=64)
s.path('M430 184 V237',T,3,arrow=True);s.text(476,221,'가중치 전달 후 고정',24,T,600)
s.label(20,274,'후속 과제 판독');s.wave(30,334,220,24,0,B,True,5);s.line(278,332,326,332,S,3,arrow=True);s.encoder(350,295,145,80,'인코더',True);s.line(522,333,570,333,S,3,arrow=True);s.rect(598,295,120,80,BS,B,2,2);s.text(658,341,'판독기',24,B,600,'middle');s.line(744,333,793,333,S,3,arrow=True);s.text(841,342,'방향 등 출력',27,I,600);s.text(660,266,'새 과제 정답으로 학습',22,B,600,'middle');s.save('p1-pretrain-probe')

# S31: six compact protocol paths; freeze icon and output object communicate differences.
s=SVG();s.label(14,27,'학습 목표');s.label(510,27,'이번 평가에서 바꾼 모듈');s.label(946,27,'읽어낸 출력')
rows=[('MC-SimCLR','구간 대조','고정 인코더','판독기','사건·방위각',True),('GRAM','마스킹 복원','고정 인코더','판독기','방향 분포',True),('CCSR','STFT 복원','인코더','판독기','TDoA',False),('SFD','clean 특징','인코더','판독기','DOA',False),('LAM','공분산 복원','표현','지도 판독','DOA·재현율',None),('AT2SELD','태깅 전이','공간 경로','지도 적응','사건·위치',None)]
for j,(name,task,enc,head,out,freeze) in enumerate(rows):
 y=66+j*57;s.text(14,y+20,name,24,I,600);s.text(188,y+20,task,23,S)
 if j==0:
  s.circle(378,y+9,6,BS,B);s.circle(405,y+9,6,TS,T);s.line(386,y+9,397,y+9,B,2)
 elif j in [1,2,3]:
  for k in range(5):s.rect(368+k*11,y-2,8,23,P if k in[1,3] else BS,B,1)
 elif j==4:
  for a in range(3):
   for b in range(3):s.rect(374+a*12,y-4+b*10,9,7,BS if a!=b else B,'none',0)
 else:
  for k,h in enumerate([12,25,17]):s.rect(375+k*13,y+19-h,9,h,T,'none',0)
 s.line(441,y+10,477,y+10,S,2,arrow=True);s.rect(499,y-10,162,40,TS if freeze else P,T if freeze else R,2,2);s.text(580,y+18,enc,22,T if freeze else I,600,'middle')
 if freeze:s.lock(650,y-11)
 s.line(680,y+10,716,y+10,S,2,arrow=True);s.rect(737,y-10,137,40,BS,B,2,2);s.text(805,y+18,head,22,B,600,'middle');s.line(895,y+10,929,y+10,S,2,arrow=True);s.text(953,y+18,out,24,I,600)
 if freeze is False:s.line(506,y+36,870,y+36,B,3)
s.save('p1-protocol-map')

# S32: observed rear alarm with same semantics but competing spatial text.
s=SVG();s.label(15,30,'空間 오디오'.replace('空間','공간'));s.head(192,148,45);s.speaker(191,304,B);s.line(194,272,194,216,B,3,arrow=True);s.text(96,64,'앞',23,S);s.text(88,365,'뒤',23,S);s.text(220,357,'알람',26,B,600)
s.line(321,208,393,208,S,3,arrow=True);s.encoder(426,164,143,86,'오디오');s.text(634,216,'↔',40,S,600,'middle')
s.text(714,79,'후보 문장',24,L,600);s.line(705,199,1081,106,R,2);s.line(705,218,1081,305,R,2)
for y,d,c in [(136,'앞쪽',S),(302,'뒤쪽',B)]:
 s.text(747,y,d,33,c,600);s.text(839,y,'의 알람',33,I,600);s.line(748,y+13,823,y+13,c,3)
s.text(744,375,'소리 이름은 같고, 위치 표현은 다름',23,S);s.save('p1-spatial-language')

# S34: movement changes spatial caption, while omni semantics remain the same.
s=SVG();s.label(14,31,'같은 소리를 다른 위치에');s.head(160,203,40);s.speaker(70,96,B,scale=.65);s.speaker(280,299,B,scale=.65);s.path('M104 77 C274 31 350 168 306 267',B,2,dash='6 5',arrow=True);s.text(22,358,'알람의 종류 유지',25,B,600)
s.line(352,203,420,203,S,3,arrow=True);s.circle(448,203,6,T,T);s.path('M448 203 V106 H519',T,3,arrow=True);s.path('M448 203 V292 H519',T,3,arrow=True)
s.label(540,49,'의미 분기');s.encoder(541,71,143,73,'omni');s.line(709,107,768,107,S,3,arrow=True);s.text(808,115,'“알람 소리”',31,B,600);s.text(809,157,'원래 caption',23,S)
s.label(540,235,'공간 분기');s.encoder(541,257,143,73,'FOA 전체');s.line(709,293,768,293,S,3,arrow=True);s.text(808,292,'“왼쪽 / 오른쪽의 알람”',27,T,600);s.text(809,341,'공간 caption · 방향',23,S);s.save('p1-salm-factorization')

print('Generated',len(list(OUT.glob('p1-*.svg'))),'Part 1 diagrams')
