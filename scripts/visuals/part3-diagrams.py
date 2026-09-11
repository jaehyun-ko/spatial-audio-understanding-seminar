"""Original teaching diagrams for Part 3, not experimental data. Run with .venv/bin/python."""
from pathlib import Path
import numpy as np
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon, FancyArrowPatch, Arc
from matplotlib.font_manager import FontProperties

OUT=Path(__file__).resolve().parents[2]/'public'/'diagrams'
PAPER='#f6f8fa'; INK='#142233'; SECONDARY='#586879'; BLUE='#1f5fae'; TEAL='#008b9a'; ORANGE='#a95018'; RULE='#d4dde7'; SOFT='#e7eff9'; WHITE='#ffffff'
FONT=FontProperties(fname=str(Path.home()/'Library/Fonts/Pretendard-Regular.otf'))
BOLD=FontProperties(fname=str(Path.home()/'Library/Fonts/Pretendard-SemiBold.otf'))
plt.rcParams.update({'svg.fonttype':'path','mathtext.fontset':'stix','axes.unicode_minus':False})

def canvas():
    fig=plt.figure(figsize=(11.36,4.04),dpi=100,facecolor=PAPER)
    ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,1136);ax.set_ylim(404,0);ax.axis('off');ax.set_facecolor(PAPER)
    return fig,ax

def save(fig,name):
    fig.canvas.draw()
    renderer=fig.canvas.get_renderer()
    records=[]
    for ax in fig.axes:
        for t in ax.texts:
            b=t.get_window_extent(renderer)
            records.append({'text':t.get_text(),'bounds':[round(v,2) for v in (b.x0,b.y0,b.x1,b.y1)],'outside':bool(b.x0<0 or b.y0<0 or b.x1>1136 or b.y1>404)})
    (OUT/f'{name}.labels.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
    assert not any(r['outside'] for r in records), [r for r in records if r['outside']]
    fig.savefig(OUT/f'{name}.svg',facecolor=PAPER)
    fig.savefig(OUT/f'{name}.png',dpi=200,facecolor=PAPER)
    plt.close(fig)

def txt(ax,x,y,s,size=26,color=INK,ha='center',bold=False,va='center'):
    return ax.text(x,y,s,fontsize=max(size,27)*.72,color=color,ha=ha,va=va,fontproperties=BOLD if bold else FONT,linespacing=1.3)

def line(ax,x1,y1,x2,y2,color=RULE,lw=2,ls='-'):
    ax.plot([x1,x2],[y1,y2],color=color,lw=lw*.72,ls=ls,solid_capstyle='round')

def arrow(ax,a,b,color=SECONDARY,lw=2,scale=15,style='-|>'):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle=style,mutation_scale=scale,lw=lw*.72,color=color))

def circ(ax,x,y,r,color=BLUE,fill=WHITE,lw=2):
    ax.add_patch(Circle((x,y),r,edgecolor=color,facecolor=fill,lw=lw*.72))

def wave(ax,x,y,w=160,h=22,phase=0,color=BLUE,cycles=3,noise=False,seed=14,lw=3):
    t=np.linspace(0,1,240)
    z=np.sin(2*np.pi*cycles*t+phase)
    if noise:
        rng=np.random.default_rng(seed);z=np.convolve(rng.normal(size=t.size),[.2,.6,.2],mode='same');z/=max(abs(z))
    ax.plot(x+t*w,y-h*z,color=color,lw=lw*.72,solid_capstyle='round')

def mic(ax,x,y,color=INK,s=1):
    ax.add_patch(Rectangle((x-6*s,y-13*s),12*s,22*s,facecolor=WHITE,edgecolor=color,lw=2*.72))
    ax.add_patch(Arc((x,y+2*s),23*s,26*s,theta1=0,theta2=180,edgecolor=color,lw=2*.72))
    line(ax,x,y+15*s,x,y+25*s,color,2);line(ax,x-9*s,y+25*s,x+9*s,y+25*s,color,2)

def speaker(ax,x,y,s=1,color=BLUE):
    ax.add_patch(Polygon([(x-18*s,y-12*s),(x-8*s,y-12*s),(x+7*s,y-24*s),(x+7*s,y+24*s),(x-8*s,y+12*s),(x-18*s,y+12*s)],closed=True,edgecolor=color,facecolor=SOFT,lw=2*.72))
    for r in [22,36]: ax.add_patch(Arc((x+6*s,y),r*s,r*1.5*s,theta1=-55,theta2=55,edgecolor=color,lw=2*.72))

def room(ax,x,y,w=210,h=145,speaker_on=True,coords=False):
    # Oblique room outline: a diagram, not a measured geometry.
    dx=42;dy=-34
    corners=[(x,y),(x+w,y),(x+w+dx,y+dy),(x+dx,y+dy),(x,y)]
    for a,b in zip(corners,corners[1:]):line(ax,*a,*b,RULE,2)
    for a in [(x,y),(x+w,y),(x+w+dx,y+dy),(x+dx,y+dy)]:line(ax,*a,a[0],a[1]-h,RULE,2)
    for a,b in zip(corners,corners[1:]):line(ax,a[0],a[1]-h,b[0],b[1]-h,RULE,2)
    mic(ax,x+w*.4,y-18,INK,.8);mic(ax,x+w*.68,y-18,INK,.8)
    if speaker_on:
        speaker(ax,x+w*.76,y-h*.7,.65)
        line(ax,x+w*.76,y-h*.7,x+w*.4,y-18,BLUE,1.5, '--')
        line(ax,x+w*.76,y-h*.7,x+w*.68,y-18,BLUE,1.5,'--')
    if coords:
        arrow(ax,(x+w*.54,y-16),(x+w*.95,y-16),INK,1.5,11)
        txt(ax,x+w*.99,y-15,'x',24)

def lock(ax,x,y,s=.85):
    ax.add_patch(Arc((x,y-7*s),24*s,25*s,theta1=180,theta2=360,edgecolor=SECONDARY,lw=2*.72))
    ax.add_patch(Rectangle((x-15*s,y-7*s),30*s,24*s,edgecolor=SECONDARY,facecolor=PAPER,lw=2*.72))
    circ(ax,x,y+2*s,2*s,SECONDARY,SECONDARY,1)

def vector(ax,x,y,h=82,w=23):
    vals=[.25,.75,.48,.95,.35,.62]
    for k,v in enumerate(vals):
        ax.add_patch(Rectangle((x,y+k*h/6),w,h/6-2,facecolor=matplotlib.colors.to_rgba(BLUE,.18+.7*v),edgecolor=PAPER,lw=1))

# S67: three independent evaluation objects (no staircase or progressive guarantee).
fig,ax=canvas()
for x in [379,757]:line(ax,x,30,x,376,RULE,1.5)
for x,title,sub in [(190,'시스템의 답','STAR-Bench · WearVox'),(568,'고정 표현','SARL'),(946,'단서 변경','BMLD')]:
    txt(ax,x,33,title,30,TEAL,bold=True);txt(ax,x,375,sub,24,SECONDARY)
# Multiple-choice audio question and selected option.
speaker(ax,72,126,.85)
arrow(ax,(119,126),(161,126),SECONDARY)
ax.add_patch(Polygon([(173,84),(332,84),(332,164),(219,164),(201,182),(201,164),(173,164)],closed=True,edgecolor=BLUE,facecolor=WHITE,lw=2*.72))
txt(ax,252,123,'어디에서?',26,BLUE,bold=True)
for i,(x,lbl) in enumerate([(101,'A'),(190,'B'),(279,'C')]):
    circ(ax,x,238,28,BLUE if i==1 else RULE,SOFT if i==1 else WHITE,3 if i==1 else 2)
    txt(ax,x,239,lbl,27,BLUE if i==1 else SECONDARY,bold=i==1)
txt(ax,190,317,'답변 정확도',27,bold=True)
# Frozen representation -> linear projection -> labels.
lock(ax,464,96,.85)
for i in range(3):vector(ax,439+i*29,137,86,21)
arrow(ax,(540,182),(593,182),TEAL)
line(ax,622,104,699,256,TEAL,3)
for xx,yy in [(604,129),(631,172),(643,208),(687,218),(660,241)]:
    circ(ax,xx,yy,5,BLUE,BLUE,1)
    # Perpendicular-ish projection paths illustrate reading a label axis.
    line(ax,xx+6,yy,xx+28,yy-12,RULE,1.5)
txt(ax,568,317,'요인별 선형 판독',27,bold=True)
# L and R target waves, only right target flips; unchanged noise indicated explicitly.
txt(ax,808,104,'L',24,SECONDARY);wave(ax,833,104,100,19,color=BLUE)
txt(ax,808,175,'R',24,SECONDARY);wave(ax,833,175,100,19,color=BLUE)
arrow(ax,(950,140),(983,140),ORANGE)
wave(ax,1001,104,103,19,color=BLUE);wave(ax,1001,175,103,19,color=ORANGE,phase=np.pi)
txt(ax,946,235,'같은 잡음 · 표적 위상 변경',24,SECONDARY)
txt(ax,946,317,'표현 거리의 반응',27,bold=True)
save(fig,'p3-evidence-targets')

# S72: controlled scene -> frozen encoder -> mean-pooled representation -> trained probes.
fig,ax=canvas()
txt(ax,133,30,'단일 음원 · 10초',27,TEAL,bold=True)
room(ax,25,239,165,113,True)
txt(ax,133,291,'모델별 전처리',24,SECONDARY)
arrow(ax,(245,182),(288,182),SECONDARY)
# Encoder drawn as neural layers, without prose-filled container.
for xx,count in [(323,4),(366,5),(409,4)]:
    ys=np.linspace(127,239,count)
    for yy in ys:circ(ax,xx,yy,8,BLUE,SOFT,1.5)
for xa,na,xb,nb in [(323,4,366,5),(366,5,409,4)]:
    for ya in np.linspace(127,239,na):
        for yb in np.linspace(127,239,nb):line(ax,xa+8,ya,xb-8,yb,RULE,1)
lock(ax,366,70,1)
txt(ax,366,290,'인코더 고정',26,bold=True)
arrow(ax,(431,182),(471,182),SECONDARY)
# Frame embedding matrix collapses in time, then one pooled vector.
for i in range(4):vector(ax,489+i*26,131,103,20)
line(ax,489,247,588,247,SECONDARY,1.5);txt(ax,538,272,'시간',24,SECONDARY)
arrow(ax,(602,182),(649,182),SECONDARY)
vector(ax,667,131,103,29)
txt(ax,680,290,'평균 pooling',25,bold=True)
# Every task gets its own learned linear classifier; two task families are explicit.
line(ax,716,182,760,182,TEAL,2)
line(ax,760,84,760,354,TEAL,2)
for yy in [96,139,182,225,268,311,354]:
    arrow(ax,(760,yy),(812,yy),TEAL,lw=1.6,scale=12)
    ax.add_patch(Rectangle((815,yy-13),44,26,facecolor=SOFT,edgecolor=TEAL,lw=1.5*.72))
    line(ax,826,yy+6,847,yy-6,TEAL,2)
for yy,lbl in zip([96,139,182,225,268,311,354],['사건','방위','고도','거리',r'$\mathrm{RT}_{60}$','부피','형상']):txt(ax,893,yy,lbl,25,INK,ha='left')
txt(ax,943,29,'선형 판독기만 학습',27,TEAL,bold=True)
line(ax,996,77,996,239,RULE,2);txt(ax,1054,158,'음원',24,SECONDARY)
line(ax,996,255,996,369,RULE,2);txt(ax,1054,311,'방',24,SECONDARY)
txt(ax,366,366,'학습하지 않음',24,SECONDARY)
txt(ax,680,366,'장면 표현',24,SECONDARY)
save(fig,'p3-sarl-linear-readout')

# S74: exact same noise seed across L/R and conditions; illustrative units, no reported data.
fig,ax=canvas()
txt(ax,326,26,'왼쪽 L',27,TEAL,bold=True);txt(ax,666,26,'오른쪽 R',27,TEAL,bold=True)
line(ax,870,47,870,357,RULE,1.5)
t=np.linspace(0,1,600);rng=np.random.default_rng(24)
n=np.convolve(rng.normal(size=600),np.ones(4)/4,mode='same');n=n/max(abs(n))*.52
s=.45*np.sin(2*np.pi*4*t)
for row,(label,l,r) in enumerate([(r'$N_0$',n,n),(r'$S_0N_0$',n+s,n+s),(r'$S_{\pi}N_0$',n+s,n-s)]):
    y=94+row*106
    txt(ax,68,y,label,30,bold=True)
    for col,(x,z) in enumerate([(172,l),(512,r)]):
        line(ax,x,y,x+285,y,RULE,1)
        ax.plot(x+285*t,y-30*n,color=SECONDARY,alpha=.45,lw=.9*.72)
        colr=SECONDARY if row==0 else ORANGE if row==2 and col==1 else BLUE
        ax.plot(x+285*t,y-30*z,color=colr,lw=2*.72)
    if row==0:txt(ax,838,y,r'$n$',25,SECONDARY)
    if row==1:txt(ax,838,y,r'$n+s$',25,BLUE)
    if row==2:txt(ax,838,y,r'$n-s$',25,ORANGE)
txt(ax,494,380,'공유 잡음 n · 표적 s',24,SECONDARY)
# Right: metric expressed without illustrative embedding locations or fake values.
txt(ax,1006,81,'잡음 표현까지',25,SECONDARY)
txt(ax,1006,117,'거리 비교',28,TEAL,bold=True)
txt(ax,924,191,r'$d_0$',28,BLUE);txt(ax,1030,191,'동위상 거리',24,INK)
txt(ax,924,244,r'$d_\pi$',28,ORANGE);txt(ax,1030,244,'역위상 거리',24,INK)
txt(ax,1006,313,r'$20\log_{10}\!\left(\frac{d_\pi}{d_0}\right)$',32,BLUE)
save(fig,'p3-bmld-stimulus-waveforms')

# S77: shared observation, distinct outputs, and distinct evaluation evidence.
fig,ax=canvas()
room(ax,10,249,180,145,True,True)
txt(ax,126,318,'같은 알람 장면',26,TEAL,bold=True)
line(ax,250,199,292,199,SECONDARY,2);line(ax,292,72,292,199,SECONDARY,2)
line(ax,292,72,991,72,SECONDARY,1.6)
for cx0 in [457,706,991]:arrow(ax,(cx0,72),(cx0,94),SECONDARY,lw=1.6,scale=12)
# Three output families each have a compact scientific object; names group research, not results.
# 1: direction response and selected target.
cx=457;cy=187
for rad in [40,70]:ax.add_patch(Arc((cx,cy),rad*2,rad*2,theta1=185,theta2=355,edgecolor=RULE,lw=1.5*.72))
line(ax,cx-81,cy,cx+81,cy,SECONDARY,1.5)
angles=np.linspace(np.pi,2*np.pi,200);rr=18+58*np.exp(-((angles-4.6)/.22)**2)
ax.plot(cx+rr*np.cos(angles),cy+rr*np.sin(angles),color=BLUE,lw=3*.72)
speaker(ax,cx+3,211,.48)
txt(ax,cx,45,'방향·목표',28,TEAL,bold=True)
txt(ax,cx,280,'AGG-RL',24,bold=True);txt(ax,cx,313,'SelectTSL',24,SECONDARY)
# 2: retrieved sentence and source-indexed scene attributes.
line(ax,570,30,570,345,RULE,1.5)
x=609
for i in range(3):
    yy=102+i*36
    circ(ax,x,yy,7,BLUE if i==1 else RULE,BLUE if i==1 else WHITE,2)
    line(ax,x+22,yy,x+177,yy,BLUE if i==1 else RULE,3 if i==1 else 2)
for xx,co in [(643,BLUE),(715,TEAL),(787,SECONDARY)]:
    circ(ax,xx,224,12,co,SOFT,2);line(ax,xx,239,xx,256,co,2)
txt(ax,706,45,'문장·장면',28,TEAL,bold=True)
txt(ax,706,280,'ELSA',24,bold=True);txt(ax,706,313,'Sci-Phi',24,SECONDARY)
# 3: source trajectory over time, no numeric score.
line(ax,834,30,834,345,RULE,1.5)
xs=np.array([885,925,965,1005,1045,1085]);ys=np.array([221,188,145,127,145,166])
ax.plot(xs,ys,color=BLUE,lw=2*.72)
for i,(xx,yy) in enumerate(zip(xs,ys)):circ(ax,xx,yy,6,BLUE,WHITE if i<5 else BLUE,2)
arrow(ax,(1045,145),(1085,166),BLUE,lw=2,scale=12)
arrow(ax,(877,245),(1101,245),SECONDARY,lw=1.5,scale=12)
txt(ax,991,45,'시간·움직임',28,TEAL,bold=True)
txt(ax,991,280,'ST-AudioLM',24,bold=True);txt(ax,991,313,'정적 / 동적 QA',24,SECONDARY)
line(ax,331,353,1106,353,RULE,1.5)
txt(ax,716,382,'검증: 답변 · 선형 판독 · 자극 반응',25,SECONDARY)
save(fig,'p3-alarm-evidence-recap')

# S78: scientific claim is conditioned on observed input, defined output, and discriminating comparisons.
fig,ax=canvas()
for x,s0 in [(161,'관측'),(568,'출력'),(976,'근거')]:txt(ax,x,32,s0,31,TEAL,bold=True)
room(ax,34,246,176,134,True,True)
wave(ax,48,288,82,17,color=BLUE);wave(ax,160,288,82,17,color=TEAL)
txt(ax,161,362,'음원 · 방 · 배열',27,bold=True)
arrow(ax,(286,188),(354,188),SECONDARY,lw=2.5,scale=18)
# Coordinate output with two sensors along x, distance ray, azimuth and elevation.
o=np.array([543,239]);ex=np.array([1.0,0]);ey=np.array([-.65,.42]);ez=np.array([0.,-1.])
for vec,lbl in [(102*ex,'x'),(100*ey,'y'),(140*ez,'z')]:
    e=o+vec;arrow(ax,o,e,SECONDARY,lw=1.6,scale=12);txt(ax,e[0]+(12 if lbl=='x' else -10),e[1]-12,lbl,24,SECONDARY)
azi=np.deg2rad(24);elev=np.deg2rad(40);rad=180
projected_dir=np.cos(azi)*ex+np.sin(azi)*ey
proj=o+rad*np.cos(elev)*projected_dir
src=proj+rad*np.sin(elev)*ez
line(ax,*o,*src,BLUE,2.7);line(ax,*src,*proj,BLUE,1.5,'--');line(ax,*o,*proj,BLUE,1.5,'--')
circ(ax,*src,10,BLUE,BLUE,2)
for xx in [515,571]:mic(ax,xx,239,INK,.6)
angles=np.linspace(0,azi,80)
arc=o+65*(np.cos(angles)[:,None]*ex+np.sin(angles)[:,None]*ey)
ax.plot(arc[:,0],arc[:,1],color=TEAL,lw=2*.72)
angles=np.linspace(0,elev,80)
arc=o+85*(np.cos(angles)[:,None]*projected_dir+np.sin(angles)[:,None]*ez)
ax.plot(arc[:,0],arc[:,1],color=BLUE,lw=2*.72)
txt(ax,692,115,'distance',24,BLUE)
txt(ax,691,187,'elevation',24,BLUE)
txt(ax,578,302,'azimuth',24,TEAL)
txt(ax,568,362,'목표 · 위치 · 시간',27,bold=True)
arrow(ax,(753,188),(815,188),SECONDARY,lw=2.5,scale=18)
# A paired room comparison changes only the pictured room shape; no scores are fabricated.
room(ax,839,235,85,85,True,False)
room(ax,1011,235,73,127,True,False)
arrow(ax,(952,181),(993,181),TEAL,lw=1.8,scale=14,style='<->')
txt(ax,976,290,'같은 질문 · 바꾼 조건',24,SECONDARY)
txt(ax,976,362,'통제 비교 · 실제 시험',27,bold=True)
save(fig,'p3-observation-output-evidence')
print('Rendered 5 light teaching diagrams (SVG + PNG), 1136 × 404 view; PNG 2272 × 808.')
