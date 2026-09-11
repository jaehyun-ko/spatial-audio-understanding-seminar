"""Original causal teaching diagrams, not measured model outputs.
Run from any working directory; default output is this repository's public/diagrams.
"""
from pathlib import Path
from tempfile import TemporaryDirectory
import argparse, json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch
from matplotlib.font_manager import FontProperties
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parents[2]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output-dir', type=Path, default=ROOT/'public/diagrams')
OUT = parser.parse_args().output_dir.resolve(); OUT.mkdir(parents=True, exist_ok=True)
# Decompress repository-owned WOFF2 files; no machine-specific font paths.
FONT_TEMP = TemporaryDirectory(prefix='causal-signal-fonts-')
FONT_PROPS = {}
for weight, style in [(400, 'Regular'), (600, 'SemiBold')]:
    font = TTFont(ROOT/f'public/fonts/Pretendard-{style}.woff2'); font.flavor = None
    font_path = Path(FONT_TEMP.name)/f'{style}.ttf'; font.save(font_path)
    FONT_PROPS[weight] = FontProperties(fname=str(font_path))
BG='#f6f8fa'; INK='#142233'; MUTED='#586879'; BLUE='#1f5fae'; TEAL='#008b9a'; RULE='#d4dde7'; SOFT='#e7eff9'; ORANGE='#a95018'
plt.rcParams.update({'svg.fonttype':'path','mathtext.fontset':'stix','svg.hashsalt':'causal-signal-v1'})

def canvas():
    f=plt.figure(figsize=(11.36,4.04),dpi=100,facecolor=BG)
    a=f.add_axes([0,0,1,1]); a.set(xlim=(0,1136),ylim=(404,0)); a.axis('off'); return f,a

def txt(a,x,y,t,size=24,c=INK,bold=False,ha='center'):
    return a.text(x,y,t,fontsize=size*.72,color=c,ha=ha,va='center',fontproperties=FONT_PROPS[600 if bold else 400],linespacing=1.3)

def line(a,p,q,c=RULE,w=2,ls='-'):
    a.plot([p[0],q[0]],[p[1],q[1]],color=c,lw=w*.72,ls=ls)

def arrow(a,p,q,c=MUTED,w=2):
    a.add_patch(FancyArrowPatch(p,q,arrowstyle='-|>',mutation_scale=13,color=c,lw=w*.72))

def box(a,x,y,w,h,label,c=BLUE):
    a.add_patch(Rectangle((x,y),w,h,ec=c,fc=BG,lw=1.6)); txt(a,x+w/2,y+h/2,label,24,c,True)

def wave(a,x,y,w=130,c=BLUE,phase=0,noisy=False,amp=17):
    t=np.linspace(0,1,230)
    v=np.sin(2*np.pi*4*(t-phase))*np.exp(-((t-phase-.46)/.22)**2)
    if noisy: v += .17*np.sin(2*np.pi*29*t)+.12*np.sin(2*np.pi*17*t+.3)
    a.plot(x+w*t,y-amp*v,c=c,lw=1.8)

def matrix(a,x,y,n=4,cell=13,c=BLUE):
    for row in range(n):
        for col in range(n):
            a.add_patch(Rectangle((x+col*(cell+3),y+row*(cell+3)),cell,cell,fc=c,ec='none',alpha=.22+.7*((row*3+col*7)%13)/12))

def covariance(a,x,y,cell=15,c=BLUE):
    # Magnitude of a Hermitian positive-semidefinite covariance, for illustration.
    v=np.exp(1j*np.arange(4)*.72)
    C=np.outer(v,v.conj())+.35*np.eye(4)
    C/=np.max(np.abs(C))
    for row in range(4):
        for col in range(4):
            a.add_patch(Rectangle((x+col*(cell+3),y+row*(cell+3)),cell,cell,fc=c,ec='none',alpha=.18+.7*abs(C[row,col])))

def location(a,x,y,c=BLUE):
    line(a,(x-42,y+34),(x+48,y+34),MUTED); line(a,(x-42,y+34),(x-42,y-36),MUTED)
    line(a,(x+8,y-13),(x+8,y+34),RULE,1.5,':');line(a,(x-42,y-13),(x+8,y-13),RULE,1.5,':')
    a.add_patch(Circle((x+8,y-13),7,fc=c,ec=BG,lw=1.6))

def response(a,x,y,w=142,h=102,combined=False):
    # Same illustrative, physically defined maps in both rows; no improvement claim.
    gx=np.linspace(-2,2,25); gy=np.linspace(-.4,3.6,25)
    xx,yy=np.meshgrid(gx,gy); ps=np.array([.6,1.6]); m=[np.array([-.65,0]),np.array([.65,0]),np.array([-.5,2.8])]
    z=np.zeros_like(xx)
    for i,j in ([(0,1),(0,2),(1,2)] if combined else [(0,1)]):
        dd=np.hypot(xx-m[i][0],yy-m[i][1])-np.hypot(xx-m[j][0],yy-m[j][1])
        target=np.linalg.norm(ps-m[i])-np.linalg.norm(ps-m[j])
        z += np.exp(-((dd-target)/.11)**2)
    from matplotlib.colors import LinearSegmentedColormap
    cmap=LinearSegmentedColormap.from_list('lightblue',[BG,'#dce8f5',BLUE])
    # A vector mesh preserves sharpness in the standalone SVG.
    a.pcolormesh(x+np.linspace(0,w,26),y+np.linspace(h,0,26),z,cmap=cmap,vmin=0,vmax=float(z.max()) if combined else 1,shading='flat',rasterized=False)
    a.add_patch(Rectangle((x,y),w,h,ec=RULE,fc='none',lw=1.0))
    if combined:
        iy,ix=np.unravel_index(np.argmax(z),z.shape)
        a.add_patch(Circle((x+(ix+.5)/25*w,y+h-(iy+.5)/25*h),3.5,fc=BLUE,ec=BG,lw=.8))
    for px,py in m if combined else m[:2]:
        a.add_patch(Circle((x+(px+2)/4*w,y+h-(py+.4)/4*h),3.3,fc=TEAL,ec=BG,lw=.8))

def save(f,name):
    f.canvas.draw(); renderer=f.canvas.get_renderer(); labels=[]
    for a in f.axes:
        for t in a.texts:
            b=t.get_window_extent(renderer)
            assert b.x0>=-1 and b.y0>=-1 and b.x1<=1137 and b.y1<=405,(name,t.get_text(),b.bounds)
            labels.append({'label':t.get_text(),'bounds':[round(v,1) for v in (b.x0,b.y0,b.x1,b.y1)]})
    f.savefig(OUT/f'{name}.svg',facecolor=BG,metadata={'Date':None})
    f.savefig(OUT/f'{name}.png',facecolor=BG,dpi=200)
    (OUT/f'{name}.labels.json').write_text(json.dumps(labels,ensure_ascii=False,indent=2))
    plt.close(f)

# 1. Only pair-response estimation changes; aggregation and argmax are kept.
f,a=canvas()
for x,t in [(98,'같은 관측'),(320,'쌍 응답을 만드는 방법'),(566,'쌍별 지도'),(804,'모든 쌍 합산'),(1028,'최대점')]: txt(a,x,25,t,24,MUTED,True)
line(a,(0,203),(1136,203))
for yy,learned in [(128,False),(308,True)]:
    wave(a,24,yy-20,142,BLUE); wave(a,24,yy+22,142,TEAL,.045)
    arrow(a,(178,yy),(228,yy))
    if not learned:
        txt(a,330,67,'SRP · 고정 계산',25,BLUE,True)
        t=np.linspace(-1,1,180); v=.9*np.exp(-((t-.25)/.15)**2)+.23*np.exp(-((t+.48)/.18)**2)
        a.plot(247+(t+1)*88,164-59*v,c=BLUE,lw=2)
        line(a,(247,164),(424,164),RULE)
        line(a,(357,99),(357,169),TEAL,1.8,':')
        a.add_patch(Circle((357,111),4,fc=TEAL,ec=TEAL))
        txt(a,332,187,'기대 지연에서 읽기',24)
    else:
        txt(a,329,247,'Neural-SRP · 학습',25,BLUE,True)
        box(a,248,280,178,52,'쌍 지도 예측')
        txt(a,330,363,'위상 + 좌표·방 크기',24,MUTED)
    arrow(a,(439,yy),(481,yy))
    response(a,495,yy-51)
    arrow(a,(650,yy),(704,yy)); txt(a,678,yy-34,'+',28,TEAL,True)
    response(a,721,yy-51,166,102,True)
    arrow(a,(901,yy),(959,yy))
    location(a,1029,yy)
    txt(a,1030,yy+63,r'$\hat{p}=\arg\max_p R(p)$',24,BLUE)
txt(a,569,381,'같은 TDoA 능선',24,TEAL,True)
save(f,'causal-srp-neural')

# 2. What is transmitted is the pedagogical variable, not a universal architecture.
f,a=canvas()
txt(a,106,28,'같은 공간 관측',25,TEAL,True)
for yy,c,phase in [(146,BLUE,0),(202,TEAL,.045)]: wave(a,25,yy,151,c,phase)
arrow(a,(190,175),(230,175));line(a,(233,101),(233,298),MUTED)
arrow(a,(233,101),(293,101));arrow(a,(233,298),(293,298))
txt(a,430,29,'위치 좌표만 전달',28,BLUE,True)
box(a,294,65,172,73,'')
txt(a,380,87,'SRP',23,BLUE,True);txt(a,380,115,'Neural-SRP',23,BLUE,True)
arrow(a,(468,102),(559,102))
location(a,614,102);txt(a,706,103,r'$(\hat{x},\hat{y})$',32,BLUE)
line(a,(778,102),(821,102),ORANGE,2,':')
txt(a,966,84,'무슨 소리였나?',27,ORANGE,True);txt(a,966,127,'언제 났나?',27,ORANGE,True)
txt(a,521,170,'이 좌표만 다음 단계에 전달',24,MUTED)
line(a,(283,207),(1136,207))
txt(a,465,240,'중간 표현을 보존해 전달',28,BLUE,True)
box(a,304,275,151,53,'인코더 E')
arrow(a,(470,300),(513,300));matrix(a,527,274,4,13)
txt(a,616,302,r'$H$',34,BLUE)
arrow(a,(644,300),(688,300))
line(a,(692,250),(692,359),MUTED)
for yy,label in [(250,'사건 판독'),(304,'위치 판독'),(359,'시간 관계 판독')]:
    arrow(a,(692,yy),(742,yy));box(a,752,yy-20,190,40,label)
    arrow(a,(955,yy),(990,yy))
    if yy==250:
        a.add_patch(Circle((1050,yy+12),4,fc=BLUE,ec=BLUE))
        a.plot([1028,1035,1036,1041,1050,1059,1064,1065,1072],[yy+7,yy-1,yy-10,yy-17,yy-21,yy-17,yy-10,yy-1,yy+7],c=BLUE,lw=2)
        line(a,(1028,yy+7),(1072,yy+7),BLUE,2)
    elif yy==304:
        arrow(a,(1022,yy+13),(1074,yy-12),TEAL,3)
        a.add_patch(Circle((1022,yy+13),4,fc=TEAL,ec=TEAL))
    else:
        arrow(a,(1006,yy+9),(1093,yy+9),MUTED,1.5)
        for xx,cc in [(1022,BLUE),(1070,TEAL)]:
            a.add_patch(Circle((xx,yy+9),4,fc=cc,ec=BG))
            line(a,(xx,yy+4),(xx,yy-12),cc,2)
txt(a,475,382,'남아 있는지는 판독 실험으로 확인',24,MUTED)
save(f,'causal-readout-to-encoder')

# 3. Four pretext relationships drawn as signals, masks and physical reconstruction.
f,a=canvas()
for x in [283,568,853]: line(a,(x,12),(x,391))
for x,t in [(141,'구간 간 일관성'),(426,'채널 간 관계'),(711,'물리적 공간 구조'),(995,'오염에 강한 단서')]:txt(a,x,31,t,27,BLUE,True)
# Same recording crops.
for yy,c in [(111,BLUE),(157,TEAL)]: wave(a,24,yy,230,c,amp=19)
for xx,c in [(43,BLUE),(173,TEAL)]:
    a.add_patch(Rectangle((xx,81),58,105,fc='none',ec=c,lw=2))
arrow(a,(72,199),(109,246),BLUE);arrow(a,(202,199),(173,246),TEAL)
a.add_patch(Circle((116,259),10,fc=BLUE,ec=BG));a.add_patch(Circle((167,259),10,fc=TEAL,ec=BG))
arrow(a,(127,259),(143,259),BLUE);arrow(a,(156,259),(144,259),TEAL)
txt(a,141,307,'같은 녹음의 두 구간',24);txt(a,141,340,'표현을 가깝게',24,TEAL,True)
txt(a,141,382,'MC-SimCLR',24,MUTED)
# Actual two branch mask semantics; show frames not frequency bins.
def frames(x,y,mask,row,c):
    for j in range(8):
        fill=BG if j in mask else c
        a.add_patch(Rectangle((x+j*25,y),19,19,fc=fill,ec=RULE if j in mask else c,lw=1,alpha=1 if j in mask else .75))
        if j in mask:line(a,(x+j*25+3,y+16),(x+j*25+16,y+3),RULE,1)
txt(a,426,82,'함께 가림',24)
for r,c in [(0,BLUE),(1,TEAL)]:frames(329,107+r*26,[2,3,6],r,c)
txt(a,426,194,'번갈아 가림',24)
for r,c in [(0,BLUE),(1,TEAL)]:frames(329,217+r*26,list(range(r,8,2)),r,c)
arrow(a,(425,275),(425,293))
frames(329,307,[],0,BLUE)
txt(a,426,350,'가린 STFT 복원',24,TEAL,True);txt(a,426,382,'CCSR',24,MUTED)
# CSM -> map -> physical covariance reconstruction.
txt(a,638,84,'관측 CSM',24)
covariance(a,603,105,15,BLUE);arrow(a,(683,141),(730,141))
a.add_patch(Circle((781,140),39,fc='none',ec=RULE,lw=1.5))
for ang in np.linspace(0,np.pi*2,15,endpoint=False):
    radius=16+19*np.exp(-((ang-1.4)/.52)**2)
    line(a,(781,140),(781+radius*np.cos(ang),140-radius*np.sin(ang)),BLUE,2)
txt(a,781,204,'음향지도',24,BLUE,True)
arrow(a,(781,226),(781,259),TEAL)
covariance(a,750,277,13,TEAL)
arrow(a,(726,307),(676,307),TEAL)
txt(a,640,281,r'$\hat C$',28,TEAL)
txt(a,640,316,'복원',24,TEAL,True)
txt(a,711,351,r'$\hat C=A\,\mathrm{diag}(x)\,A^{H}$',24,TEAL)
txt(a,711,382,'LAM',24,MUTED)
# Noisy feature prediction and a separately computed clean target.
txt(a,914,84,'오염',24);txt(a,1072,84,'clean',24,TEAL,True)
wave(a,869,132,94,BLUE,noisy=True,amp=20);wave(a,1021,132,100,TEAL,amp=20)
arrow(a,(913,168),(913,211));arrow(a,(1070,168),(1070,211),TEAL)
matrix(a,884,226,3,16,BLUE)
line(a,(1036,278),(1111,278),RULE);line(a,(1036,278),(1036,222),RULE)
line(a,(1040,271),(1105,230),TEAL,3)
arrow(a,(950,251),(1018,251),BLUE)
txt(a,995,316,'clean 특징을 목표로',24)
txt(a,995,350,'공간 단서 회수',24,TEAL,True)
txt(a,995,382,'SFD',24,MUTED)
save(f,'causal-encoder-objectives')
FONT_TEMP.cleanup()
print('Generated 3 causal-signal diagrams with label-bound checks.')
