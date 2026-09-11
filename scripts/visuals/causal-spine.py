"""Original teaching diagrams and a sourced TWNM connector result chart."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch
from matplotlib.font_manager import FontProperties

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'public/diagrams'
FONT=FontProperties(fname=str(Path.home()/'Library/Fonts/Pretendard-Regular.otf'))
BOLD=FontProperties(fname=str(Path.home()/'Library/Fonts/Pretendard-SemiBold.otf'))
BG='#f6f8fa'; INK='#142233'; MUTED='#586879'; BLUE='#1f5fae'; TEAL='#008b9a'; RULE='#d4dde7'; SOFT='#e7eff9'; ORANGE='#a95018'
plt.rcParams.update({'svg.fonttype':'path','mathtext.fontset':'stix'})

def canvas():
 f=plt.figure(figsize=(11.36,4.04),dpi=100,facecolor=BG)
 a=f.add_axes([0,0,1,1]);a.set(xlim=(0,1136),ylim=(404,0));a.axis('off');return f,a
def txt(a,x,y,t,size=25,c=INK,bold=False,ha='center'):
 return a.text(x,y,t,fontsize=size*.72,color=c,ha=ha,va='center',fontproperties=BOLD if bold else FONT,linespacing=1.3)
def line(a,x1,y1,x2,y2,c=RULE,w=2,ls='-'):
 a.plot([x1,x2],[y1,y2],color=c,lw=w*.72,ls=ls)
def arrow(a,p,q,c=MUTED,w=2):
 a.add_patch(FancyArrowPatch(p,q,arrowstyle='-|>',mutation_scale=13,color=c,lw=w*.72))
def box(a,x,y,w,h,label,c=BLUE,fill=BG):
 a.add_patch(Rectangle((x,y),w,h,ec=c,fc=fill,lw=1.5));txt(a,x+w/2,y+h/2,label,c=c,bold=True)
def matrix(a,x,y,rows=4,cols=6,c=BLUE,cell=10):
 for r in range(rows):
  for k in range(cols):
   a.add_patch(Rectangle((x+k*(cell+4),y+r*(cell+4)),cell,cell,fc=c,ec='none',alpha=.25+.7*((r*3+k*5)%11)/10))
def waves(a,x,y,w=120,c=BLUE,phase=0):
 t=np.linspace(0,1,180);v=np.sin(2*np.pi*(4*t)+phase)*np.exp(-((t-.48)/.24)**2)
 a.plot(x+w*t,y+17*v,c=c,lw=1.7)
def peak(a,x,y,w=165,h=52):
 t=np.linspace(0,1,130);v=np.exp(-((t-.55)/.1)**2)+.18*np.exp(-((t-.22)/.08)**2)
 a.plot(x+w*t,y-h*v,c=BLUE,lw=2);line(a,x,y,x+w,y);line(a,x+w*.55,y,x+w*.55,y-h,TEAL,1.5,':')
def save(f,name):
 f.canvas.draw();rend=f.canvas.get_renderer();records=[]
 for a in f.axes:
  for t in a.texts:
   b=t.get_window_extent(rend);records.append({'text':t.get_text(),'bounds':[round(v,1) for v in (b.x0,b.y0,b.x1,b.y1)]})
   assert b.x0>=-1 and b.y0>=-1 and b.x1<=1137 and b.y1<=405,(name,t.get_text(),b.bounds)
 (OUT/(name+'.labels.json')).write_text(json.dumps(records,ensure_ascii=False,indent=2))
 f.savefig(OUT/(name+'.svg'),facecolor=BG);f.savefig(OUT/(name+'.png'),facecolor=BG,dpi=200);plt.close(f)

# One observation feeds either a task-specific coordinate or a richer language interface.
f,a=canvas()
txt(a,110,34,'같은 두 채널 관측',26,c=TEAL,bold=True)
line(a,33,110,180,110,MUTED)
for x in [70,140]:
 a.add_patch(Circle((x,110),7,ec=INK,fc=BG,lw=1.5));line(a,x,119,x,133,INK);line(a,x-8,133,x+8,133,INK)
txt(a,192,110,'x',22,c=MUTED)
waves(a,38,205,135);waves(a,38,260,135,TEAL,.6)
txt(a,105,318,r'$X$',29)
arrow(a,(196,208),(241,208))
line(a,250,104,250,288,MUTED)
arrow(a,(250,104),(316,104));arrow(a,(250,288),(316,288))
txt(a,435,30,'먼저: 위치를 계산한다',28,bold=True)
peak(a,347,134,170,60)
txt(a,433,169,'SRP → 학습한 공간 응답',23,c=BLUE)
arrow(a,(555,105),(676,105))
txt(a,755,79,r'$(\hat{x},\hat{y})$',33,c=BLUE)
txt(a,755,123,'정해진 위치 출력',25)
txt(a,948,101,'잔향·배열 변화',24,c=MUTED)
txt(a,509,216,'다음: 질문에 필요한 정보를 남긴다',28,bold=True)
box(a,325,264,142,68,'인코더 E',BLUE,SOFT)
matrix(a,489,276,3,4,BLUE,10)
arrow(a,(555,297),(600,297))
box(a,610,264,135,68,'어댑터 P',TEAL)
arrow(a,(755,297),(800,297))
box(a,810,264,136,68,'LLM',BLUE)
arrow(a,(956,297),(1000,297))
txt(a,1060,282,'종류',24);txt(a,1060,314,'위치·시간',24)
txt(a,428,374,'공간·의미·시간 보존',23,c=MUTED)
txt(a,681,374,'토큰으로 전달',23,c=MUTED)
txt(a,883,374,'질문에 맞게 사용',23,c=MUTED)
save(f,'causal-roadmap')

# TWNM Appendix G Table 15: additional reported connector results, not a matched causal claim.
f,a=canvas()
txt(a,0,24,'Overall (%) ↑',25,c=MUTED,ha='left')
adapter_data=json.loads((ROOT/'plans/CAUSAL_ADAPTER_DATA.json').read_text())
rows=[(row['method'].replace(':', ' ·'),float(row['value'])) for row in adapter_data['values']]
left,right=440,1040
for i,(label,value) in enumerate(rows):
 y=88+i*100;col=BLUE if i==2 else MUTED
 txt(a,0,y,label,29,bold=i==2,ha='left')
 a.barh(y,(right-left)*value/60,left=left,height=32,color=col)
 txt(a,left+(right-left)*value/60+16,y,f'{value:.2f}',32,c=col,bold=True,ha='left')
line(a,left,350,right,350)
for v in [0,30,60]:
 x=left+(right-left)*v/60;line(a,x,345,x,355,MUTED,1.2);txt(a,x,382,str(v),23,c=MUTED)
save(f,'causal-module-evidence')

# A synthesis of the three different questions, with supporting families, not historical lineage.
f,a=canvas()
cols=[179,568,957]
for i,(x,label,question) in enumerate(zip(cols,['인코더 E','어댑터 P','LLM 적응'],['무엇이 남았는가?','무엇을 전달했는가?','무엇을 사용했는가?'])):
 txt(a,x,30,label,29,c=TEAL,bold=True);txt(a,x,75,question,29,bold=True)
 if i<2:line(a,x+195,15,x+195,392)
waves(a,82,152,90);matrix(a,227,132,4,5,BLUE,10);arrow(a,(180,152),(217,152))
txt(a,179,225,'위치·사건의 고정 표현 판독',24)
txt(a,179,279,'예: GRAM · SARL',22,c=MUTED)
txt(a,179,330,'단서 개입: BMLD',24,c=BLUE)
for k in range(3):
 matrix(a,449+k*81,131,4,3,BLUE if k%2==0 else TEAL,10)
txt(a,568,199,'의미  ·  공간  ·  시간',24,c=BLUE)
txt(a,568,246,'분기·압축·결속의 설계',24)
txt(a,568,293,'예: Spatial-Omni',22,c=MUTED)
txt(a,568,329,'시간 구조: ST-AudioLM',22,c=MUTED)
box(a,817,125,112,62,'질문',MUTED)
arrow(a,(939,156),(974,156))
box(a,984,125,110,62,'답변',BLUE,SOFT)
txt(a,957,226,'오디오 유무 · zero 기준선',24)
txt(a,957,275,'BAT · Spatial-Omni',22,c=MUTED)
txt(a,957,329,'학습 목표 변화: TWNM',23,c=BLUE)
txt(a,568,384,'한 단계의 점수로 다음 단계까지 입증하지 않는다.',23,c=MUTED)
save(f,'causal-synthesis')
print('Generated 3 causal-spine diagrams')
