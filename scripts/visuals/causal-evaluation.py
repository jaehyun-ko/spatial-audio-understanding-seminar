"""Teaching diagrams: observed evidence versus proposed spatial-representation tests.

No numerical outcomes are simulated. Fixed light-paper style, 1136x404 SVG and 2x PNG.
Run: .venv/bin/python scripts/visuals/causal-evaluation.py
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon, FancyArrowPatch, Arc
from matplotlib.font_manager import FontProperties

OUT = Path(__file__).resolve().parents[2] / 'public' / 'diagrams'
QA = Path(__file__).resolve().parents[2] / 'tmp' / 'causal-bridge-qa'
BG='#f6f8fa'; INK='#142233'; MUTED='#586879'; BLUE='#1f5fae'; TEAL='#008b9a'; ORANGE='#a95018'; RULE='#d4dde7'; SOFT='#e7eff9'; WHITE='#ffffff'
FONT=FontProperties(fname=str(Path.home()/'Library/Fonts/Pretendard-Regular.otf'))
BOLD=FontProperties(fname=str(Path.home()/'Library/Fonts/Pretendard-SemiBold.otf'))
plt.rcParams.update({'svg.fonttype':'path','mathtext.fontset':'stix','axes.unicode_minus':False})

def canvas():
    fig=plt.figure(figsize=(11.36,4.04),dpi=100,facecolor=BG)
    ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1136); ax.set_ylim(404,0); ax.axis('off')
    return fig,ax

def txt(ax,x,y,s,size=27,color=INK,ha='center',bold=False):
    return ax.text(x,y,s,fontsize=max(size,27)*.72,color=color,ha=ha,va='center',fontproperties=BOLD if bold else FONT,linespacing=1.25)

def line(ax,x1,y1,x2,y2,color=RULE,lw=2,ls='-'):
    ax.plot([x1,x2],[y1,y2],color=color,lw=lw*.72,ls=ls,solid_capstyle='round')

def arrow(ax,a,b,color=MUTED,lw=2,scale=14,style='-|>',ls='-'):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle=style,mutation_scale=scale,lw=lw*.72,color=color,linestyle=ls))

def rect(ax,x,y,w,h,color=BLUE,fill=WHITE,lw=2,ls='-'):
    ax.add_patch(Rectangle((x,y),w,h,edgecolor=color,facecolor=fill,lw=lw*.72,linestyle=ls))

def circ(ax,x,y,r,color=BLUE,fill=WHITE,lw=2):
    ax.add_patch(Circle((x,y),r,edgecolor=color,facecolor=fill,lw=lw*.72))

def wave(ax,x,y,w=110,h=16,color=BLUE,phase=0):
    t=np.linspace(0,1,150); z=np.sin(6*np.pi*t+phase)
    ax.plot(x+w*t,y-h*z,color=color,lw=2.1,solid_capstyle='round')

def mic(ax,x,y,s=.7):
    circ(ax,x,y,6*s,INK,BG,2)
    ax.add_patch(Arc((x,y),21*s,23*s,theta1=0,theta2=180,edgecolor=INK,lw=1.5))
    line(ax,x,y+11*s,x,y+20*s,INK,1.8); line(ax,x-8*s,y+20*s,x+8*s,y+20*s,INK,1.8)

def speaker(ax,x,y,color=BLUE,s=.8):
    ax.add_patch(Polygon([(x-16*s,y-10*s),(x-7*s,y-10*s),(x+6*s,y-22*s),(x+6*s,y+22*s),(x-7*s,y+10*s),(x-16*s,y+10*s)],closed=True,edgecolor=color,facecolor=SOFT if color==BLUE else WHITE,lw=1.6))
    for r in (23,36): ax.add_patch(Arc((x+5*s,y),r*s,r*1.4*s,theta1=-50,theta2=50,edgecolor=color,lw=1.5))

def voice(ax,x,y,s=.85,color=TEAL):
    circ(ax,x,y-11*s,9*s,color,BG,2)
    ax.add_patch(Arc((x,y+19*s),34*s,30*s,theta1=180,theta2=360,edgecolor=color,lw=1.6))
    for r in [25,36]:ax.add_patch(Arc((x+9*s,y-4*s),r*s,r*s,theta1=-45,theta2=45,edgecolor=color,lw=1.4))

def matrix(ax,x,y,w=60,h=62,color=BLUE,cols=3,rows=5,mode=0):
    # Symbolic latent cells only. Their intensities are illustrative, not observations.
    for j in range(cols):
        for k in range(rows):
            a=.16+.12*((j*3+k+mode)%6)
            rect(ax,x+j*w/cols,y+k*h/rows,w/cols-3,h/rows-3,RULE,matplotlib.colors.to_rgba(color,a),.7)

def readout(ax,x,y,label,color=TEAL):
    rect(ax,x-43,y-22,86,44,color,BG,2)
    txt(ax,x,y,label,27,color,bold=True)

def plane(ax,x,y,w=120):
    line(ax,x-w/2,y,x+w/2,y,MUTED,1.8)
    arrow(ax,(x,y),(x,y-74),RULE,1.5,11)
    mic(ax,x-20,y,.65); mic(ax,x+20,y,.65)

def output_pair(ax,x,y,left,right,color=TEAL):
    txt(ax,x-68,y,left,27,color);arrow(ax,(x-18,y),(x+18,y),color,1.6,12);txt(ax,x+72,y,right,27,color)

def save(fig,name):
    OUT.mkdir(parents=True,exist_ok=True); QA.mkdir(parents=True,exist_ok=True)
    fig.canvas.draw(); renderer=fig.canvas.get_renderer(); records=[]
    for ax in fig.axes:
        for t in ax.texts:
            b=t.get_window_extent(renderer)
            records.append({'text':t.get_text(),'bounds':[round(v,2) for v in (b.x0,b.y0,b.x1,b.y1)],'outside':bool(b.x0<0 or b.y0<0 or b.x1>1136 or b.y1>404)})
    (QA/f'{name}.labels.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
    assert not any(r['outside'] for r in records), [r for r in records if r['outside']]
    fig.savefig(OUT/f'{name}.svg',facecolor=BG)
    fig.savefig(OUT/f'{name}.png',dpi=200,facecolor=BG); plt.close(fig)

def encoder_criteria():
    fig,ax=canvas()
    for x in (379,757):line(ax,x,16,x,389,RULE,1.5)
    titles=[(190,'위치만 이동'),(568,'종류만 교체'),(947,'순서만 교환')]
    for x,title in titles:txt(ax,x,28,title,31,TEAL,bold=True)
    # One source, two positions: semantic label invariant, position readout changes.
    for x in (98,282):plane(ax,x,187,112)
    speaker(ax,65,107); speaker(ax,311,107)
    line(ax,65,126,98,183,BLUE,1.4,'--');line(ax,311,126,282,183,BLUE,1.4,'--')
    arrow(ax,(162,134),(215,134),ORANGE,2,15)
    txt(ax,190,222,'같은 알람',27,MUTED)
    # One position, two classes: location invariant, semantic label changes.
    for x in (477,660):plane(ax,x,187,112)
    speaker(ax,493,107);voice(ax,676,107)
    for x in (477,660):line(ax,x+16,128,x,184,TEAL,1.4,'--')
    arrow(ax,(540,134),(594,134),ORANGE,2,15)
    txt(ax,568,222,'같은 좌표',27,MUTED)
    # Same event segments, reversed order. No identity tracking success implied.
    for y in (107,177):arrow(ax,(812,y+20),(1094,y+20),MUTED,1.4,12)
    for x,y,color,s in [(834,90,BLUE,'A'),(969,90,TEAL,'B'),(834,160,TEAL,'B'),(969,160,BLUE,'A')]:
        rect(ax,x,y,95,33,color,matplotlib.colors.to_rgba(color,.12),1.4);txt(ax,x+47,y+17,s,27,color,bold=True)
    arrow(ax,(804,135),(804,160),ORANGE,2,12)
    txt(ax,947,222,'같은 두 사건',27,MUTED)
    for x in (190,568,947):
        arrow(ax,(x,244),(x,268),MUTED,1.8,12)
        matrix(ax,x-95,286,46,43,BLUE,3,3)
        txt(ax,x-72,266,'H',27,BLUE)
        arrow(ax,(x-43,307),(x-8,307),TEAL,1.7,12)
        readout(ax,x+50,307,'판독')
    txt(ax,190,368,'종류 =  ·  위치 ↔',27,bold=True)
    txt(ax,568,368,'종류 ↔  ·  위치 =',27,bold=True)
    txt(ax,947,368,'순서 AB ↔ BA',27,bold=True)
    save(fig,'causal-encoder-criteria')

def evaluation_map():
    fig,ax=canvas()
    txt(ax,21,26,'보고된 관측 위치',27,BLUE,ha='left',bold=True)
    txt(ax,1115,26,'점선 = 후속 제안',27,ORANGE,ha='right',bold=True)
    # Shared abstract pipeline, not a diagram of one paper's architecture.
    y=163
    wave(ax,30,y-14,95,10);wave(ax,30,y+13,95,10,TEAL,.6)
    txt(ax,77,109,'X',30,INK,bold=True)
    arrow(ax,(137,y),(180,y),MUTED)
    rect(ax,185,y-36,67,72,INK,BG);txt(ax,219,y,'E',32,bold=True)
    arrow(ax,(258,y),(299,y),MUTED)
    matrix(ax,309,y-32,58,65);txt(ax,338,109,'H',30,BLUE,bold=True)
    arrow(ax,(376,y),(418,y),MUTED)
    rect(ax,425,y-36,67,72,INK,BG);txt(ax,459,y,'P',32,bold=True)
    arrow(ax,(500,y),(545,y),MUTED)
    matrix(ax,554,y-32,65,65,TEAL);txt(ax,586,109,'Z',30,TEAL,bold=True)
    arrow(ax,(628,y),(787,y),MUTED)
    rect(ax,796,y-37,145,74,INK,BG);txt(ax,868,y,'LLM',31,bold=True)
    arrow(ax,(951,y),(1000,y),MUTED)
    ax.add_patch(Polygon([(1009,127),(1105,127),(1105,190),(1054,190),(1037,209),(1037,190),(1009,190)],closed=True,edgecolor=BLUE,facecolor=WHITE,lw=1.6))
    txt(ax,1057,y,'답',30,BLUE,bold=True)
    # Existing probe: H -> label readout.
    arrow(ax,(338,204),(338,274),BLUE,2,13)
    line(ax,302,330,368,280,TEAL,2.2)
    for x,z in [(305,314),(324,313),(341,293),(358,297)]:circ(ax,x,z,4,BLUE,BLUE,1)
    txt(ax,338,365,'SARL · 판독',27,BLUE,bold=True)
    # Existing BMLD stimulus-level intervention is read at H, not as an answer.
    wave(ax,27,286,86,10,BLUE);wave(ax,27,319,86,10,ORANGE,np.pi)
    arrow(ax,(77,269),(77,206),BLUE,1.7,12)
    txt(ax,91,365,'BMLD · 반응',27,BLUE,bold=True)
    # Existing zero-spatial variant at interface; don't label fixed-checkpoint ablation.
    rect(ax,668,210,56,48,BLUE,BG);txt(ax,696,234,'0',29,BLUE)
    arrow(ax,(696,209),(696,172),BLUE,1.8,12)
    txt(ax,666,287,'Spatial-Omni',27,BLUE,bold=True)
    txt(ax,666,321,'zero 기준선',27,BLUE)
    # Proposed matched replacement at Z with restoration; source details in notes.
    matrix(ax,556,216,51,44,ORANGE,3,3,1)
    arrow(ax,(580,213),(580,201),ORANGE,2,11,ls='--')
    arrow(ax,(606,239),(651,239),ORANGE,2,12,style='<->',ls='--')
    txt(ax,613,365,'제안 · 치환과 복구',27,ORANGE,bold=True)
    # Question-only reported by BAT: Q points to LLM. For question-only, X is omitted.
    txt(ax,858,76,'Q',29,BLUE,bold=True)
    arrow(ax,(858,96),(858,121),BLUE,1.8,13)
    txt(ax,983,76,'BAT · X 없이 Q',27,BLUE,bold=True)
    # Proposed paired audio intervention judged by correctly changing answer.
    for yy,lab,col,phase in [(262,'A',BLUE,0),(319,'B',ORANGE,.8)]:
        wave(ax,853,yy,83,11,col,phase)
        arrow(ax,(943,yy),(1000,yy),ORANGE,1.7,12,ls='--')
        rect(ax,1008,yy-20,61,40,col,BG,1.6)
        txt(ax,1038,yy,lab,27,col,bold=True)
    txt(ax,972,365,'제안 · 오디오 짝',27,ORANGE)
    save(fig,'causal-evaluation-map')

def spatial_scene(ax):
    # Same coordinate convention as the opening spatial-goal-3d drawing.
    O=np.array([191.,276.]);scale=40.
    def p(v):
        x,y,z=v;return O+scale*np.array([x-.62*y,-.33*y-z])
    def seg(a,b,c=RULE,lw=1.4,ls='-'):line(ax,*p(a),*p(b),c,lw,ls)
    def arr(a,b,c=MUTED,lw=1.7):arrow(ax,p(a),p(b),c,lw,12)
    for x in (-2,0,2,4):seg((x,-.5,0),(x,3.4,0),RULE,1)
    for yy in (0,1.5,3):seg((-2.4,yy,0),(4.1,yy,0),RULE,1)
    seg((-2.5,0,0),(0,0,0),MUTED,1.5)
    arr((0,0,0),(4.7,0,0));arr((0,0,0),(0,3.8,0));arr((0,0,0),(0,0,4.15))
    txt(ax,390,276,'$x$',27,MUTED);txt(ax,85,226,'$y$',27,MUTED);txt(ax,210,108,'$z$',27,MUTED)
    for x,n in [(-1.18,'1'),(1.18,'2')]:
        q=p((x,0,0));mic(ax,*q,.85);txt(ax,q[0],q[1]+40,'$M_'+n+'$',27)
    circ(ax,*O,3,INK,INK,1);txt(ax,O[0]-2,O[1]+20,'$O$',27)
    S=np.array([3.5,2.2,2.1]); S2=np.array([1.2,3.1,2.6]);P=S.copy();P[2]=0
    seg((0,0,0),P,TEAL,1.5,'--');seg(P,S,MUTED,1.5,'--');arr((0,0,0),S,BLUE,2.8)
    q=p(S);circ(ax,*q,8,BLUE,BLUE,1);txt(ax,q[0]+44,q[1]-10,'알람 A',27,BLUE,bold=True)
    q2=p(S2);circ(ax,*q2,8,ORANGE,BG,2);arrow(ax,(q[0]-10,q[1]-12),(q2[0]+12,q2[1]-7),ORANGE,2,12,ls='--')
    txt(ax,q2[0]-12,q2[1]-28,'B',27,ORANGE,bold=True)
    alpha=np.arctan2(S[1],S[0]);beta=np.arctan2(S[2],np.hypot(*S[:2]))
    pts=np.array([p((1.85*np.cos(a),1.85*np.sin(a),0))for a in np.linspace(0,alpha,48)])
    ax.plot(*pts.T,c=TEAL,lw=1.8)
    pts2=np.array([p((2.5*np.cos(b)*np.cos(alpha),2.5*np.cos(b)*np.sin(alpha),2.5*np.sin(b)))for b in np.linspace(0,beta,48)])
    ax.plot(*pts2.T,c=TEAL,lw=1.8)
    txt(ax,281,262,'$\\alpha$',27,TEAL);txt(ax,252,235,'$\\beta$',27,TEAL);txt(ax,211,210,'$r$',29,BLUE)
    q3=p((-2.3,1.1,1.5));circ(ax,*q3,5,MUTED,MUTED,1);txt(ax,q3[0]-7,q3[1]-27,'말소리',27,MUTED)

def closing_tests():
    fig,ax=canvas()
    txt(ax,204,29,'알람 위치 교환',28,BLUE,bold=True)
    spatial_scene(ax)
    txt(ax,204,372,'후속 실험 제안',27,ORANGE,bold=True)
    # Three observation stations, all proposed on the same frozen pipeline.
    stations=[(522,'H','좌표가 남나?'),(771,'Z','토큰에도 남나?'),(1020,'답','답이 바뀌나?')]
    for x,s,label in stations:
        txt(ax,x,42,label,29,TEAL,bold=True)
    arrow(ax,(387,211),(447,211),MUTED,2,14)
    matrix(ax,478,157,87,108,BLUE,4,6);txt(ax,522,117,'E → H',29,BLUE,bold=True)
    arrow(ax,(578,211),(691,211),MUTED,2,14);txt(ax,634,183,'P',30,INK,bold=True)
    matrix(ax,727,172,87,77,TEAL,4,4);txt(ax,771,117,'Z',29,TEAL,bold=True)
    arrow(ax,(825,211),(944,211),MUTED,2,14);txt(ax,884,183,'LLM',27,INK,bold=True)
    # Paired symbolic coordinate outputs, no invented model result.
    for yy,lab,col in [(162,'위치 A',BLUE),(235,'위치 B',ORANGE)]:
        rect(ax,951,yy-24,138,48,col,WHITE,1.7)
        txt(ax,1020,yy,lab,27,col,bold=True)
    for x in (522,771):
        arrow(ax,(x,273),(x,310),ORANGE,1.7,12,ls='--')
        txt(ax,x,338,'$\\alpha,\\;\\beta,\\;r$',30,TEAL)
        txt(ax,x,374,'같은 판독기',27,MUTED)
    txt(ax,1020,338,'정답도 A → B',27,ORANGE,bold=True)
    txt(ax,1020,374,'두 답 모두 검사',27,MUTED)
    save(fig,'causal-closing-tests')

if __name__=='__main__':
    encoder_criteria();evaluation_map();closing_tests()
