"""Educational 3-D azimuth/elevation/range geometry; no measured/model data."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Arc, FancyArrowPatch
from matplotlib import font_manager as fm
for w in ('Regular','SemiBold','Bold'):
    fm.fontManager.addfont(str(Path.home()/'Library/Fonts'/('Pretendard-'+w+'.otf')))
plt.rcParams.update({'font.family':'Pretendard','svg.fonttype':'path','mathtext.fontset':'stix','axes.unicode_minus':False})
BG='#f6f8fa'; INK='#142233'; MUTED='#586879'; BLUE='#1f5fae'; TEAL='#008b9a'; RULE='#d4dde7'
fig=plt.figure(figsize=(11.36,4.04),dpi=100,facecolor=BG)
ax=fig.add_axes([0,0,1,1],xlim=(0,1136),ylim=(404,0));ax.axis('off')
O=np.array([380.,318.]);scale=80.
def p(v):
    x,y,z=v;return O+scale*np.array([x-.62*y,-.33*y-z])
def line(a,b,**kw): ax.plot(*np.array([p(a),p(b)]).T,**kw)
def arrow(a,b,c=INK,lw=1.8,**kw): ax.add_patch(FancyArrowPatch(p(a),p(b),arrowstyle='-|>',mutation_scale=12,color=c,lw=lw,**kw))
def label(x,y,t,size=19,c=INK,**kw):ax.text(x,y,t,fontsize=size,color=c,va='center',**kw)
# A sparse perspective floor gives the explicit xy reference plane.
for x in np.arange(-3,5):line((x,-.7,0),(x,3.5,0),color=RULE,lw=.7,alpha=.65)
for y in np.arange(0,4):line((-3,y,0),(4.8,y,0),color=RULE,lw=.7,alpha=.65)
line((-3.2,0,0),(0,0,0),color=MUTED,lw=1.2)
arrow((0,0,0),(5,0,0),MUTED);arrow((0,0,0),(0,4.1,0),MUTED);arrow((0,0,0),(0,0,3.8),MUTED)
label(*p((5.22,0,0)),'$x$',size=22);label(*(p((0,4.2,0))+[-12,-6]),'$y$',size=22);label(*(p((0,0,3.8))+[18,0]),'$z$',size=22)
label(174,345,'수평면 $xy$',size=16,c=MUTED)
# Microphone centers lie EXACTLY on x, symmetric about O.
for x,name in [(-1.18,'M_1'),(1.18,'M_2')]:
    q=p((x,0,0));ax.add_patch(Circle(q,7,fc=BG,ec=INK,lw=2,zorder=9))
    ax.add_patch(Arc(q,23,25,theta1=0,theta2=180,ec=INK,lw=1.7,zorder=8))
    ax.plot([q[0],q[0]],[q[1]+12,q[1]+21],c=INK,lw=1.5)
    ax.plot([q[0]-8,q[0]+8],[q[1]+21,q[1]+21],c=INK,lw=1.5)
    label(q[0],q[1]+40,'$'+name+'$',size=18,ha='center')
ax.scatter(*O,s=22,c=INK,zorder=8);label(O[0]-17,O[1]+19,'$O$',size=17)
# Target source, its floor projection and the radial distance.
S=np.array([3.9,2.4,2.2]);P=S.copy();P[2]=0
line((0,0,0),P,color=TEAL,lw=1.6,ls=(0,(5,4)))
line(P,S,color=MUTED,lw=1.3,ls=(0,(4,4)))
arrow((0,0,0),S,BLUE,lw=3.2,zorder=5)
ax.scatter(*p(P),s=24,fc=BG,ec=TEAL,zorder=7)
q=p(S);ax.add_patch(Circle(q,10,fc=BLUE,ec=BG,lw=2,zorder=10))
for radius in [19,28]:ax.add_patch(Arc(q,radius*2,radius*2,theta1=-50,theta2=40,ec=BLUE,lw=1.5,alpha=.75))
label(q[0]+51,q[1]-6,'알람',size=27,c=BLUE,fontweight='bold')
label(q[0]+51,q[1]+25,'찾아야 할 음원',size=17,c=MUTED)
# Azimuth is +x toward +y, elevation is xy plane toward +z.
alpha=np.arctan2(S[1],S[0]);beta=np.arctan2(S[2],np.hypot(*S[:2]))
angles=np.linspace(0,alpha,64);pts=np.array([p((1.85*np.cos(a),1.85*np.sin(a),0))for a in angles]);ax.plot(*pts.T,c=TEAL,lw=2.5)
angles=np.linspace(0,beta,64);pts2=np.array([p((2.45*np.cos(b)*np.cos(alpha),2.45*np.cos(b)*np.sin(alpha),2.45*np.sin(b)))for b in angles]);ax.plot(*pts2.T,c=TEAL,lw=2.5)
# Greek symbols mark the actual arcs; longer labels use unobtrusive leaders.
a=pts[len(pts)//2];label(a[0]+17,a[1]-12,'$\\alpha$',size=21,c=TEAL)
b=pts2[len(pts2)//2];label(b[0]+7,b[1]-5,'$\\beta$',size=21,c=TEAL)
mid=(O+q)/2;label(mid[0]-10,mid[1]-10,'$r$',size=25,c=BLUE,ha='right')
# Competing speech source maintains the same two-source narrative as S08.
Q=p((-2.5,1.3,1.4));ax.scatter(*Q,s=85,c=MUTED,zorder=7)
for r in [13,21]:ax.add_patch(Arc(Q,2*r,2*r,theta1=145,theta2=215,ec=MUTED,lw=1.2))
label(Q[0]+25,Q[1]-3,'말소리',size=18,c=MUTED)
# Three concise readouts define the target coordinates without prose panels.
label(855,180,'Azimuth  $\\alpha$',size=22,c=TEAL)
label(855,215,'방위각 · 수평 회전',size=17,c=MUTED)
label(855,265,'Elevation  $\\beta$',size=22,c=TEAL)
label(855,300,'고도각 · 수평면 위 각도',size=17,c=MUTED)
label(855,350,'Distance  $r$',size=22,c=BLUE)
label(855,385,'거리 · 원점에서 음원까지',size=17,c=MUTED)
OUT=Path(__file__).resolve().parents[2]/'public/diagrams'
OUT.mkdir(exist_ok=True)
fig.savefig(OUT/'spatial-goal-3d.svg',facecolor=BG)
fig.savefig(OUT/'spatial-goal-3d.png',dpi=200,facecolor=BG)
plt.close(fig)
