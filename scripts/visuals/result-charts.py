"""Lecture-sized result plots from the deck's exact reported table cells."""
from pathlib import Path
import json,math,re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
for w in ('Regular','SemiBold','Bold'):fm.fontManager.addfont(str(Path.home()/'Library/Fonts'/('Pretendard-'+w+'.otf')))
plt.rcParams.update({'font.family':'Pretendard','svg.fonttype':'path','mathtext.fontset':'stix','axes.unicode_minus':False})
BG='#f6f8fa';INK='#142233';MUTED='#586879';GREY='#586879';BLUE='#1f5fae';TEAL='#008b9a';ORANGE='#a95018';RULE='#d4dde7'
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'public/diagrams'
DATA={r['slide']:r for r in json.loads((ROOT/'plans/RESULTS_VISUAL_DATA.json').read_text())['charts']}
# Metrics, full method names and scales are explicit; no normalized cross-paper score.
config={
11:dict(metrics=['평균 위치 오차 (m) ↓'],labels=['SRP','NeuralSRP+'],limits=[1.5]),
14:dict(metrics=['방향 MAE (°) ↓',r'$\\mathrm{ACC}_{10}$ (%) ↑'],labels=['기본 Neural-SRP','AGG 적용'],limits=[30,100]),
19:dict(metrics=['사건 정확도 (%) ↑','방위각 오차 (°) ↓'],labels=['사전학습 없음','MC-SimCLR · w/o DA'],limits=[100,90]),
21:dict(metrics=['TDoA MAE (samples) ↓'],labels=['처음부터 지도학습','사전학습 + 전체 미세조정'],limits=[.5]),
27:dict(metrics=['Test SELD ↓'],labels=['no-stitch · cs00','late-only · cs01'],limits=[1]),
33:dict(metrics=['4방향 정확도 (%) ↑'],labels=['S-Clotho · 합성','S-AC · 합성','S-RWD · 실녹음'],limits=[100],focus=2),
35:dict(metrics=['T2A R@1 (%) ↑','A2T R@1 (%) ↑','위치 오차 (°) ↓'],labels=[r'$L_{\\mathrm{sCL}}+L_{\\mathrm{DOA}}$',r'위 조건 + $L_{\\mathrm{CL}}$'],limits=[15,15,3]),
37:dict(metrics=['MAE (°) ↓','F1 ↑'],labels=['Full','IPD Enhancer 제거 · A1'],limits=[3,1],focus=0),
39:dict(metrics=['관계 질문 · 평균 BA (%) ↑'],labels=['P · 질문만','B + P · 바이노럴 + 질문'],limits=[100]),
41:dict(metrics=['방향 정확도 (%) ↑\nType D · 8범주','DER (%) ↓\n거리 오차 > 0.5 m','관계 평균 BA (%) ↑\nType E'],labels=['SpatialAST','DSpAST'],limits=[100,100,100]),
44:dict(metrics=['방향 MAE (°) ↓','거리 DER (%) ↓'],labels=[r'바이노럴 loss · $\\eta_2=0$',r'전체 loss · $\\eta_2=10^{-2}$'],limits=[30,25]),
46:dict(metrics=['PA = 0.00','PA = 0.50'],labels=['Dither Off','Dither On · DA = 0.05'],limits=[100,100],transpose=True,unit='방향 정확도 (%) ↑'),
48:dict(metrics=['Synthetic 정확도 (%) ↑','RSL2019 정확도 (%) ↑'],labels=['Baseline · mono','SFT · 공간 입력 + 학습'],limits=[100,100]),
55:dict(metrics=['EAzi (%) ↑\n방위각 오차 ≤ 20°','IS-Loc (%) ↑\n위치로 음원 식별','RLR (%) ↑\n상대 좌우'],labels=['SO-7B-zs · 공간 토큰 0','SO-7B · 실제 공간 토큰'],limits=[100,100,100]),
58:dict(metrics=['L1 · 지각','L2 · 관계 연결','L3 · 복합 질의'],labels=['TWNM-SFT','TWNM-SAPO'],limits=[100,100,100],unit='정확도 (%) ↑'),
60:dict(metrics=['DoA·trajectory','Overall'],labels=['DSAST + Qwen7B','DSAST w/ AGM + Qwen7B'],limits=[100,100],unit='QA 정확도 (%) ↑'),
61:dict(metrics=['NoMask','AGM mask','GT mask'],labels=['Thinking','Non-Thinking'],limits=[100]*3,mode='mask'),
64:dict(metrics=['시간 관계\nTemp. rel.','이동 조건\nMove-spat.','궤적 관계\nTraj. rel.','평균'],labels=['Spatial-AST-FOA + OLMo2','ST-AudioLM'],limits=[100]*4,unit='정확도 (0–100) ↑'),
66:dict(metrics=['Global T2A R@1 (%) ↑'],labels=[r'대조 학습만 · $L_{\\mathrm{cl}}$',r'전체 · $L_{\\mathrm{cl}}+L_{\\mathrm{st}}+L_{\\mathrm{local}}+L_{\\mathrm{consist}}$'],limits=[10]),
69:dict(metrics=['Localization','Relation','Trajectory'],labels=['무작위 선택','Gemini 2.5 Pro'],limits=[100]*3,unit='AA (%) ↑'),
71:dict(metrics=['Side Talk Rejection 정확도 (%) ↑'],labels=['SC · beamformed','MC · 채널 0 + beamformed'],limits=[100]),
75:dict(metrics=['표현 거리비 지표 (dB)'],labels=['Spatial-AST','DSpAST','GRAM-T','WavJEPA'],limits=[8],focus=None),
76:dict(metrics=['유의한 반응 비율 (%)'],labels=['원신호','고역통과 > 2 kHz','Mel 대역 ILD 제거','50 Hz 포락선 vocoding'],limits=[100],mode='stack'),
}
for c in config.values():
 c['metrics']=[x.replace('\\\\','\\')for x in c['metrics']];c['labels']=[x.replace('\\\\','\\')for x in c['labels']]
def canvas():
 fig=plt.figure(figsize=(11.36,3.20),dpi=100,facecolor=BG);ax=fig.add_axes([0,0,1,1],xlim=(0,1136),ylim=(320,0));ax.axis('off');return fig,ax
def txt(ax,x,y,t,size=18,c=INK,ha='left',weight='normal',**kw):return ax.text(x,y,t,fontsize=size,color=c,ha=ha,va='center',fontweight=weight,**kw)
def clean(v):return float(v.replace('*','').replace('−','-'))
all_data=[]
for n,c in config.items():
 values=DATA[n]['values']
 vals=[[clean(v)for v in row]for row in values]
 entry={'slide':n,'metrics':c['metrics'],'labels':c['labels'],'values':values,'limits':c['limits'],'mode':c.get('mode','comparison')};all_data.append(entry)
 fig,ax=canvas();focus=c.get('focus',1)
 if c.get('mode')=='stack':
  left,right=355,1090;w=right-left
  txt(ax,left,18,c['metrics'][0],size=19,c=MUTED)
  for i,(label,row)in enumerate(zip(c['labels'],vals)):
   y=72+i*53;txt(ax,0,y,label,size=18)
   ax.plot([left,right],[y+22,y+22],c=RULE,lw=.8)
   start=left
   for j,(v,col)in enumerate(zip(row,[BLUE,ORANGE])):
    if v:
     ax.barh(y,w*v/100,left=start,height=29,color=col)
     txt(ax,start+w*v/200,y,values[i][j],size=18,c='white',ha='center',weight='bold')
    start+=w*v/100
  for v in [0,50,100]:txt(ax,left+w*v/100,285,str(v),size=15,c=MUTED,ha='center')
  for xx,col,label in [(360,BLUE,'Unmasking'),(610,ORANGE,'Reversal')]:
   ax.plot([xx,xx+24],[303,303],c=col,lw=7);txt(ax,xx+34,303,label,size=16,c=MUTED)
 elif c.get('mode')=='mask':
  left,right=160,980;top,bottom=50,228
  for v in [50,55,60]:
   y=bottom-(v-50)/10*(bottom-top);ax.plot([left,right],[y,y],c=RULE,lw=1);txt(ax,left-22,y,str(v),size=16,c=MUTED,ha='right')
  txt(ax,0,18,'Overall 정확도 (%) ↑',size=18,c=MUTED)
  xs=np.linspace(left+70,right-70,3)
  for r,row in enumerate(vals):
   col=GREY if r==0 else BLUE;ys=[bottom-(v-50)/10*(bottom-top)for v in row]
   ax.plot(xs,ys,c=col,lw=2.4,marker='o',ms=8)
   for x,y,v in zip(xs,ys,values[r]):txt(ax,x,y+(-22 if r==0 else 24),v,size=20,c=col,ha='center',weight='bold')
  for x,m in zip(xs,c['metrics']):txt(ax,x,264,m,size=18,c=INK,ha='center')
  for x,col,label in [(335,GREY,c['labels'][0]),(620,BLUE,c['labels'][1])]:ax.plot([x,x+25],[307,307],c=col,lw=3);txt(ax,x+36,307,label,size=17,c=col)
 elif len(c['metrics'])==1:
  maxv=c['limits'][0];left=370 if n!=66 else 560;right=1050;w=right-left
  txt(ax,0,17,c['metrics'][0],size=20,c=MUTED)
  cnt=len(vals);ys=np.linspace(91,235,cnt)if cnt>2 else [108,217]
  for i,(y,label,row)in enumerate(zip(ys,c['labels'],vals)):
   col=BLUE if focus is None or i==focus else GREY
   txt(ax,0,y,label,size=18 if n!=66 else 17,c=INK)
   ax.barh(y,w*row[0]/maxv,left=left,height=29,color=col)
   txt(ax,left+w*row[0]/maxv+13,y,values[i][0],size=24,c=col,weight='bold')
  axisy=279;ax.plot([left,right],[axisy,axisy],c=RULE,lw=1)
  for v in [0,maxv/2,maxv]:
   x=left+w*v/maxv;ax.plot([x,x],[axisy-4,axisy+4],c=MUTED,lw=.9);txt(ax,x,303,f'{v:g}',size=15,c=MUTED,ha='center')
 else:
  k=len(c['metrics']);gap=42 if k<4 else 28;pw=(1136-gap*(k-1))/k
  for j,m in enumerate(c['metrics']):
   x0=j*(pw+gap);left=x0+44;right=x0+pw-46;w=right-left;maxv=c['limits'][j]
   txt(ax,x0,30,m,size=18 if k<4 else 17,c=INK)
   # The native protocol caption states the common unit once per slide.
   ay=160
   # Shared numeric scale per panel, all baselines explicit at zero.
   ax.plot([left,right],[ay,ay],c=RULE,lw=2)
   xx=[left+w*row[j]/maxv for row in vals]
   ax.plot(xx,[ay]*len(xx),c=MUTED,lw=2)
   for i,x in enumerate(xx):
    col=BLUE if i==focus else GREY
    ax.scatter(x,ay,s=120 if i==focus else 100,c=col,edgecolors=BG,linewidths=1.5,zorder=5)
    # Fixed separate rows avoid label collisions when scores are close.
    txt(ax,x,ay+(-37 if i==0 else 38),values[i][j],size=25 if k<4 else 23,c=col,ha='center',weight='bold')
   for v in [0,maxv/2,maxv]:
    x=left+w*v/maxv;ax.plot([x,x],[ay-5,ay+5],c=RULE,lw=1);txt(ax,x,233,f'{v:g}',size=14,c=MUTED,ha='center')
  # Legend appears once per slide and preserves the actual compared conditions.
  for i,label in enumerate(c['labels']):
   y=270+i*28;col=BLUE if i==focus else GREY
   ax.scatter(14,y,s=60,c=col);txt(ax,32,y,label,size=17,c=col)
 fig.savefig(OUT/f'result-{n:02}.svg',facecolor=BG)
 fig.savefig(OUT/f'result-{n:02}.png',facecolor=BG,dpi=180)
 plt.close(fig)
(OUT/'results-data.json').write_text(json.dumps(all_data,ensure_ascii=False,indent=2)+'\n')
print(f'Generated {len(all_data)} exact-data charts')
