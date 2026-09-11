"""GCC-PHAT plot from the shared localization teaching scene, not paper results."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import FancyArrowPatch
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'public/diagrams'
D=np.load(OUT/'localization-simulation.npz')
t=D['times_s']; signals=D['signals']; freq=D['frequencies_hz']
G=D['raw_cross_spectra'][0]; phi=D['phat_cross_spectra'][0]
lags=D['gcc_lags_s']*1000; corr=D['gcc_phat'][0]
peak=float(lags[np.argmax(corr)]); corr=corr/np.max(corr)
BG,INK,MUTED='#f6f8fa','#142233','#586879';BLUE,TEAL,RULE='#1f5fae','#008b9a','#d4dde7'
FP={w:FontProperties(fname=str(Path.home()/f'Library/Fonts/Pretendard-{s}.otf')) for w,s in [(400,'Regular'),(600,'SemiBold')]}
plt.rcParams.update({'svg.fonttype':'path','mathtext.fontset':'stix','svg.hashsalt':'gcc-shared-scene-v2'})
f=plt.figure(figsize=(11.36,4.04),dpi=100,facecolor=BG);a=f.add_axes([0,0,1,1]);a.set(xlim=(0,1136),ylim=(404,0));a.axis('off')
def text(x,y,s,size=25,color=INK,bold=False,ha='center'):
 return a.text(x,y,s,fontsize=size*.72,fontproperties=FP[600 if bold else 400],color=color,ha=ha,va='center')
def line(x1,y1,x2,y2,color=RULE,width=1.4,style='-'):a.plot([x1,x2],[y1,y2],color=color,lw=width,ls=style)
def arrow(x1,y1,x2,y2):a.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=14,lw=1.5,color=MUTED))
for x,title in [(166,'두 채널 관측'),(567,'PHAT 가중'),(969,'시간차별 일치 점수')]:text(x,25,title,27,TEAL,True)
# Shared time axis, showing a short interval around the observed burst.
energy=np.sum(signals[:2]**2,axis=0);center=t[np.argmax(np.convolve(energy,np.ones(101)/101,mode='same'))]
start=np.floor((center-.005)*1000)/1000;stop=start+.010
sel=(t>=start)&(t<=stop);u=(t[sel]-start)*1000
amp=np.max(np.abs(signals[:2,sel]))
for signal,y,label,col in [(signals[0],138,r'$x_1$',BLUE),(signals[1],231,r'$x_2$',TEAL)]:
 line(38,y,298,y);a.plot(38+260*u/10,y-35*signal[sel]/amp,color=col,lw=1.3);text(16,y,label,25,col)
line(38,280,298,280)
for tick in [0,5,10]:
 x=38+260*tick/10;line(x,277,x,284,MUTED);text(x,306,str(tick),21,MUTED)
text(168,337,'구간 내 시간 (ms)',22,MUTED)
text(168,380,r'$\tau_{21}=t_2-t_1$',27,BLUE)
arrow(321,197,367,197)
text(568,82,r'$G_{21}=X_2X_1^*$',30)
x=418+298*freq/8000;mag=np.abs(G)/np.max(np.abs(G))
a.plot(x,238-105*mag,color=BLUE,lw=1.2);line(418,238,716,238)
text(568,116,'교차스펙트럼 크기',20,MUTED)
for tick in [0,4,8]:
 x=418+298*tick/8;line(x,236,x,242,MUTED);text(x,257,str(tick),18,MUTED)
text(568,282,'주파수 f (kHz)',20,MUTED)
text(568,329,r'$\Phi_{21}=\frac{G_{21}}{\max(|G_{21}|,\epsilon)}$',31)
text(568,379,'크기로 나누고 위상은 유지',24,MUTED)
arrow(746,197,792,197)
text(969,82,r'$C_{21}=\mathcal{F}^{-1}\{\Phi_{21}\}$',28)
text(969,117,rf'$\hat{{\tau}}_{{21}}={peak:.2f}\;\mathrm{{ms}}$',27,BLUE)
sel=(lags>=-4)&(lags<=4);xx=827+285*(lags[sel]+4)/8
a.plot(xx,281-126*corr[sel],color=BLUE,lw=1.7);line(827,281,1112,281)
xp=827+285*(peak+4)/8;line(xp,154,xp,281,TEAL,1.4,'--');a.plot([xp],[155],'o',ms=5,color=BLUE)
for tick in [-4,0,4]:
 x=827+285*(tick+4)/8;line(x,278,x,285,MUTED);text(x,306,str(tick),21,MUTED)
text(969,337,r'시간차 $\tau_{21}$ (ms)',22,MUTED)
text(969,380,'전체 곡선을 SRP에 전달',24,BLUE)
f.canvas.draw();renderer=f.canvas.get_renderer()
for label in a.texts:
 b=label.get_window_extent(renderer);assert b.x0>=-1 and b.y0>=-1 and b.x1<=1137 and b.y1<=405,(label.get_text(),b.bounds)
f.savefig(OUT/'gcc-phat.svg',facecolor=BG,metadata={'Date':None});f.savefig(OUT/'gcc-phat.png',facecolor=BG,dpi=200);plt.close(f)
(OUT/'gcc-phat.source.json').write_text(json.dumps({'kind':'computed synthetic example, not a reported experiment','sharedData':'localization-simulation.npz','pair':[2,1],'sign':'tau21=t2-t1; G21=X2*conj(X1)','estimatedTau21Ms':peak,'display':'shared amplitude scale for both channels; cross-spectrum magnitude and GCC peak each normalized for display','source':'https://www.mathworks.com/help/phased/ref/gccphat.html'},indent=2)+'\n')
print(f'Shared-scene GCC-PHAT peak {peak:.6f} ms')
