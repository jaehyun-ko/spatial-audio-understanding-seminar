"""Numerically computed localization teaching figures.

Import simulation() to reuse identical synthetic direct-path signals for GCC-PHAT.
These are teaching calculations, not room measurements or neural predictions.
"""
from pathlib import Path
from tempfile import TemporaryDirectory
import argparse, json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.font_manager import FontProperties
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parents[2]
BG='#f6f8fa'; INK='#142233'; MUTED='#586879'; BLUE='#1f5fae'
TEAL='#008b9a'; RULE='#d4dde7'; ORANGE='#a95018'
MIC=np.array([[-.65,0.],[.65,0.],[-.5,2.8]])
SOURCE=np.array([.6,1.6]); C=343.
PAIRS=np.array([[1,0],[2,0],[2,1]]); PAIR_NAMES=['21','31','32']
SOURCES=[
    {'title':'Neural-SRP, §III-A, Eqs. 3–6','url':'https://arxiv.org/html/2403.09455v1'},
    {'title':'MathWorks, gccphat','url':'https://www.mathworks.com/help/phased/ref/gccphat.html'},
]
plt.rcParams.update({'svg.fonttype':'path','mathtext.fontset':'stix','svg.hashsalt':'localization-geometry-v1'})

def simulation():
    """Shared direct-path signals and computed GCC-PHAT.

    r_ij(lag)=IFFT[X_i conj(X_j)/abs(X_i conj(X_j))] peaks at tau_ij=t_i-t_j.
    Spectra use one-sided NumPy rFFT. PHAT is zero outside 100–4000 Hz.
    Oversampled IFFT is normalized by retained bin count, so exact alignment
    yields 1. Circular fractional shifts have 512 ms period; the localized
    burst is far from the boundary. This is an explicit synthetic idealization.
    """
    fs=16000; nfft=8192; interpolation=16
    rng=np.random.default_rng(20260911)
    times=np.arange(nfft)/fs
    base=rng.normal(size=nfft)*np.exp(-.5*((times-.080)/.006)**2)
    frequencies=np.fft.rfftfreq(nfft,1/fs)
    band=(frequencies>=100)&(frequencies<=4000)
    source_spectrum=np.fft.rfft(base)*band
    source_spectrum/=np.max(np.abs(np.fft.irfft(source_spectrum,n=nfft)))
    source_signal=np.fft.irfft(source_spectrum,n=nfft)
    distances=np.linalg.norm(MIC-SOURCE,axis=1); travel=distances/C
    spectra=source_spectrum[None,:]*np.exp(-2j*np.pi*travel[:,None]*frequencies[None,:])
    signals=np.fft.irfft(spectra,n=nfft,axis=1)
    raw_cross=np.array([spectra[i]*spectra[j].conj() for i,j in PAIRS])
    phat_cross=np.zeros_like(raw_cross)
    phat_cross[:,band]=raw_cross[:,band]/np.abs(raw_cross[:,band])
    long_n=nfft*interpolation
    lags=(np.arange(long_n)-long_n//2)/(fs*interpolation)
    gcc=np.fft.fftshift(np.fft.irfft(phat_cross,n=long_n,axis=1),axes=1)
    gcc/=2*int(band.sum())/long_n
    delays=np.array([travel[i]-travel[j] for i,j in PAIRS])
    peaks=lags[np.argmax(gcc,axis=1)]
    assert np.max(np.abs(peaks-delays))<=1/(fs*interpolation)
    return {
        'fs':np.array(fs),'nfft':np.array(nfft),'interpolation':np.array(interpolation),
        'times_s':times,'source_signal':source_signal,'frequencies_hz':frequencies,
        'spectra':spectra,'signals':signals,'gcc_lags_s':lags,'gcc_phat':gcc,
        'pairs21_31_32':PAIRS,'raw_cross_spectra':raw_cross,'phat_cross_spectra':phat_cross,
        'microphone_coordinates_m':MIC,'source_coordinates_m':SOURCE,
        'distances_m':distances,'travel_times_s':travel,'true_pair_delays_s':delays,
        'gcc_peak_delays_s':peaks,'sound_speed_m_s':np.array(C),'passband_hz':np.array([100,4000]),
    }

def delay(point,pair=0):
    p=np.asarray(point);i,j=PAIRS[pair]
    return (np.linalg.norm(p-MIC[i],axis=-1)-np.linalg.norm(p-MIC[j],axis=-1))/C

def response(sim,points,pair=0):
    return np.interp(delay(points,pair),sim['gcc_lags_s'],sim['gcc_phat'][pair])

class Figures:
    def __init__(self,output):
        self.output=output;output.mkdir(parents=True,exist_ok=True)
        self.font_temp=TemporaryDirectory(prefix='localization-fonts-');self.font={}
        for weight,style in [(400,'Regular'),(600,'SemiBold')]:
            ft=TTFont(ROOT/f'public/fonts/Pretendard-{style}.woff2');ft.flavor=None
            path=Path(self.font_temp.name)/f'{style}.ttf';ft.save(path)
            self.font[weight]=FontProperties(fname=str(path))
        self.sim=simulation()
        np.savez_compressed(output/'localization-simulation.npz',**self.sim)

    def canvas(self):
        f=plt.figure(figsize=(11.36,4.04),dpi=100,facecolor=BG)
        a=f.add_axes([0,0,1,1]);a.set(xlim=(0,1136),ylim=(404,0));a.axis('off')
        return f,a

    def txt(self,a,x,y,t,size=24,c=INK,bold=False,ha='center'):
        return a.text(x,y,t,fontsize=size*.72,color=c,ha=ha,va='center',
                      fontproperties=self.font[600 if bold else 400],linespacing=1.2)

    def arrow(self,a,p,q,c=MUTED,w=2):
        a.add_patch(FancyArrowPatch(p,q,arrowstyle='-|>',mutation_scale=12,color=c,lw=w*.72))

    def axes(self,f,pos,xlim,ylim):
        a=f.add_axes(pos,facecolor=BG);a.set(xlim=xlim,ylim=ylim,aspect='equal')
        a.spines[['top','right']].set_visible(False);a.spines[['left','bottom']].set_color(RULE)
        a.tick_params(color=RULE,labelcolor=MUTED,labelsize=13,length=3)
        for label in a.get_xticklabels()+a.get_yticklabels():label.set_fontproperties(self.font[400])
        return a

    def mic(self,a,inds=(0,1),small=False):
        for i in inds:
            a.scatter(*MIC[i],s=42 if small else 95,marker='s',c=TEAL,edgecolors=BG,linewidths=1.2,zorder=6)
            a.annotate(r'$M_%d$'%(i+1),MIC[i],xytext=(0,-15 if small else -19),textcoords='offset points',
                       ha='center',color=TEAL,fontsize=12 if small else 17,zorder=7)

    def save(self,f,name,data):
        f.canvas.draw();renderer=f.canvas.get_renderer();labels=[]
        for a in f.axes:
            for t in a.texts:
                box=t.get_window_extent(renderer)
                if not t.get_visible():continue
                assert box.x0>=-1 and box.y0>=-1 and box.x1<=1137 and box.y1<=405,(name,t.get_text(),box.bounds)
                labels.append({'text':t.get_text(),'bounds':[round(v,2) for v in (box.x0,box.y0,box.x1,box.y1)]})
        f.savefig(self.output/f'{name}.svg',facecolor=BG,metadata={'Date':None})
        f.savefig(self.output/f'{name}.png',facecolor=BG,dpi=200)
        common={
            'kind':'authored scientific teaching figure from direct-path synthetic signals',
            'not':'not measured room data; not published experimental numbers; not learned Neural-SRP output',
            'coordinates':'height-fixed 2D section; microphone and source coordinates in metres',
            'microphones_m':MIC.tolist(),'source_m':SOURCE.tolist(),'sound_speed_m_s':C,
            'sign':'tau_ij=t_i-t_j=(distance_i-distance_j)/c; tau21=t2-t1',
            'signal':{'fs_hz':16000,'samples':8192,'seed':20260911,'burst_center_s':.080,'gaussian_envelope_sigma_s':.006,
                      'passband_hz':[100,4000],'fractional_delay':'exact spectral circular shift, 512 ms period',
                      'gcc':'IFFT[X_i conj(X_j)/abs(X_i conj(X_j))] on retained passband; zero otherwise',
                      'interpolation':16,'normalization':'2 times passband-bin count divided by inverse FFT length',
                      'data_file':'localization-simulation.npz'},
            'true_pair_delays_ms':dict(zip(PAIR_NAMES,(self.sim['true_pair_delays_s']*1000).tolist())),
            'sources':SOURCES,'labels':labels,**data}
        (self.output/f'{name}.source.json').write_text(json.dumps(common,ensure_ascii=False,indent=2))
        plt.close(f)

    def tdoa_locus(self):
        f,a=self.canvas()
        self.txt(a,252,25,'한 지연에 대응하는 위치들',27,BLUE,True)
        self.txt(a,824,25,r'거리 차이 $d_1-d_2$는 같다',27,BLUE,True)
        ax=self.axes(f,[.048,.145,.39,.70],(-1.15,2.1),(-.43,3.05))
        ax.set_xticks([-1,0,1,2]);ax.set_yticks([0,1,2,3]);ax.axhline(0,c=RULE,lw=1,zorder=0)
        dd=self.sim['distances_m'][0]-self.sim['distances_m'][1]
        hyper_a=dd/2;hyper_b=np.sqrt(.65**2-hyper_a**2)
        yy=np.linspace(-.3,3.1,500);xx=hyper_a*np.sqrt(1+yy**2/hyper_b**2)
        ax.plot(xx,yy,c=BLUE,lw=2.8)
        alt_y=np.array([.6,2.6]);alt_x=hyper_a*np.sqrt(1+alt_y**2/hyper_b**2)
        pts=np.array([[alt_x[0],alt_y[0]],SOURCE,[alt_x[1],alt_y[1]]])
        labels=[r'$p_a$',r'$p_s$',r'$p_b$']
        for p,l in zip(pts,labels):
            if l==r'$p_s$':
                ax.scatter(*p,s=135,marker='*',c=BLUE,zorder=9)
                for mic in MIC[:2]:ax.plot([mic[0],p[0]],[mic[1],p[1]],c=MUTED,alpha=.6,lw=1.5,ls='--')
            else:ax.scatter(*p,s=65,facecolors=BG,edgecolors=BLUE,linewidth=2,zorder=8)
            ax.annotate(l,p,xytext=(12,3),textcoords='offset points',color=BLUE,fontsize=19)
        self.mic(ax)
        self.txt(a,470,353,'x [m]',20,MUTED);self.txt(a,39,67,'y [m]',20,MUTED)
        self.txt(a,248,388,'높이를 고정한 2D 단면',21,MUTED)
        bar_x=629;scale=124;distances=[]
        for point,label,y in zip(pts,labels,[98,197,296]):
            d=np.linalg.norm(MIC[:2]-point,axis=1);distances.append(d.tolist())
            self.txt(a,574,y-1,label,28,BLUE,True)
            for k,col,dy in [(0,MUTED,-14),(1,TEAL,14)]:
                a.plot([bar_x,bar_x+d[k]*scale],[y+dy,y+dy],c=col,lw=6,solid_capstyle='butt')
                self.txt(a,611,y+dy,r'$d_%d$'%(k+1),20,col,ha='right')
            left=bar_x+d[1]*scale;right=bar_x+d[0]*scale
            a.plot([left,left],[y-25,y+25],c=ORANGE,lw=1,ls=':')
            a.plot([right,right],[y-25,y+25],c=ORANGE,lw=1,ls=':')
            a.annotate('',xy=(left,y),xytext=(right,y),arrowprops={'arrowstyle':'|-|','color':ORANGE,'lw':1.5})
            self.txt(a,(left+right)/2,y-39,f'{dd:.3f} m',21,ORANGE)
        self.txt(a,831,371,r'$\tau_{21}=(d_2-d_1)/c=$'+f" {self.sim['true_pair_delays_s'][0]*1000:.3f} ms",28,BLUE)
        self.save(f,'localization-tdoa-locus',{'alternative_positions_m':pts.tolist(),'distances_for_rows_m':distances,
            'equal_distance_difference_m':-float(dd),'physical_locus':'positive-x hyperbola branch for d2-d1<0; height-fixed problem'})

    def srp_candidate(self):
        f,a=self.canvas()
        self.txt(a,209,25,'후보 좌표',27,BLUE,True)
        self.txt(a,562,25,'거리 → 기대 지연',27,BLUE,True)
        self.txt(a,940,25,'그 지연의 상관값',27,BLUE,True)
        ax=self.axes(f,[.045,.19,.305,.65],(-1.05,1.35),(-.40,2.05))
        ax.set_xticks([-1,0,1]);ax.set_yticks([0,1,2]);ax.axhline(0,c=RULE,lw=1)
        alt=np.array([-.4,1.3])
        for point,col,label,ls in [(SOURCE,BLUE,r'$p_A$','-'),(alt,ORANGE,r'$p_B$','--')]:
            for mic in MIC[:2]:ax.plot([mic[0],point[0]],[mic[1],point[1]],c=col,lw=1.7,ls=ls,alpha=.8)
            ax.scatter(*point,s=90,c=col,zorder=5)
            ax.annotate(label,point,xytext=(8,9),textcoords='offset points',color=col,fontsize=19)
        self.mic(ax)
        self.txt(a,353,352,'x [m]',20,MUTED);self.txt(a,35,67,'y [m]',20,MUTED)
        self.arrow(a,(378,187),(414,187));rows=[]
        for point,col,label,y in [(SOURCE,BLUE,r'$p_A=(0.6,1.6)$',112),(alt,ORANGE,r'$p_B=(-0.4,1.3)$',270)]:
            d=np.linalg.norm(MIC[:2]-point,axis=1);tau=delay(point);score=response(self.sim,point)
            rows.append({'coordinate_m':point.tolist(),'distances_m':d.tolist(),'predicted_delay_ms':float(tau*1000),'gcc_score':float(score)})
            self.txt(a,550,y-35,label,25,col,True)
            self.txt(a,550,y+1,rf'$({d[1]:.3f}-{d[0]:.3f})/343$',25,col)
            self.txt(a,550,y+43,rf'$\tau_{{21}}={tau*1000:+.3f}\;\mathrm{{ms}}$',26,col,True)
        self.arrow(a,(691,187),(731,187))
        curve=f.add_axes([.674,.27,.302,.56],facecolor=BG)
        curve.set_xlim(-3.8,3.8);curve.set_ylim(-.3,1.16)
        curve.spines[['top','right']].set_visible(False);curve.spines[['bottom','left']].set_color(RULE)
        curve.tick_params(color=RULE,labelcolor=MUTED,labelsize=13)
        curve.set_xticks([-3,0,3]);curve.set_yticks([0,1]);curve.axhline(0,c=RULE,lw=1)
        lags=self.sim['gcc_lags_s']*1000;vis=(lags>-3.8)&(lags<3.8)
        curve.plot(lags[vis],self.sim['gcc_phat'][0,vis],c=MUTED,lw=1.8)
        for row,col,label in zip(rows,[BLUE,ORANGE],['A','B']):
            tau=row['predicted_delay_ms'];score=row['gcc_score']
            curve.vlines(tau,-.29,score,colors=col,ls='--',lw=1.8);curve.scatter(tau,score,c=col,s=72,zorder=4)
            curve.annotate(f'{label}: {score:.2f}',(tau,score),xytext=(12,7 if label=='A' else 18),textcoords='offset points',color=col,fontsize=16)
        self.txt(a,1112,338,r'$\tau$ [ms]',20,MUTED,ha='right')
        self.txt(a,949,372,r'$R_{21}(p)=C_{21}^{\mathrm{PHAT}}(\tau_{21}(p))$',28,BLUE)
        self.txt(a,241,386,'A는 생성에 사용한 음원 위치',21,MUTED)
        self.save(f,'localization-srp-candidate',{'candidate_rows':rows,'gcc_curve':'same actual synthetic GCC-PHAT reused in all spatial maps'})

    def srp_sum(self):
        f,a=self.canvas()
        gx=np.linspace(-1.2,1.4,261);gy=np.linspace(-.2,3.0,321)
        xx,yy=np.meshgrid(gx,gy);grid=np.stack([xx,yy],axis=-1)
        maps=np.array([response(self.sim,grid,k) for k in range(3)]);summed=maps.sum(axis=0)
        iy,ix=np.unravel_index(np.argmax(summed),summed.shape);winner=[float(gx[ix]),float(gy[iy])]
        cmap=LinearSegmentedColormap.from_list('gcc_signed',[(0,'#decbbb'),(.25,BG),(.50,'#98b9df'),(1,BLUE)])
        norm=plt.Normalize(-1,3)
        positions=[.028,.268,.508,.748]
        titles=[r'$R_{21}(p)$',r'$R_{31}(p)$',r'$R_{32}(p)$',r'$R(p)=\sum R_{ij}(p)$']
        for k,(pos,title,z) in enumerate(zip(positions,titles,[*maps,summed])):
            self.txt(a,(pos+.098)*1136,28,title,28,BLUE,True)
            ax=self.axes(f,[pos,.255,.196,.585],(-1.2,1.4),(-.2,3.0))
            ax.imshow(z,extent=(-1.2,1.4,-.2,3),origin='lower',interpolation='nearest',cmap=cmap,norm=norm,aspect='equal')
            ax.set_xticks([-1,0,1]);ax.set_yticks([0,1,2,3]);ax.tick_params(labelsize=11)
            if k:ax.set_yticklabels([])
            self.mic(ax,inds=tuple(PAIRS[k]) if k<3 else (0,1,2),small=True)
            if k==3:
                ax.scatter(*winner,s=135,marker='*',c=ORANGE,edgecolors=BG,linewidth=.9,zorder=12)
                ax.annotate(r'$\hat p$',winner,xytext=(12,4),textcoords='offset points',color=ORANGE,fontsize=18,zorder=13)
            if k<3:self.txt(a,(pos+.222)*1136,181,'+' if k<2 else '=',32,MUTED,True)
        self.txt(a,568,342,'동일 좌표 격자 · 모든 지도에 같은 색 척도',21,MUTED)
        self.txt(a,56,379,'높이 고정',20,MUTED,ha='left')
        self.txt(a,460,382,r'$\hat p=\arg\max_{p\in\mathcal{P}} R(p)$',28,BLUE)
        self.txt(a,826,381,rf'$\hat p=({winner[0]:.2f},\,{winner[1]:.2f})\;\mathrm{{m}}$',28,BLUE,True)
        cax=f.add_axes([.958,.234,.012,.596])
        cb=f.colorbar(plt.cm.ScalarMappable(norm=norm,cmap=cmap),cax=cax,ticks=[-1,0,1,2,3])
        cb.outline.set_edgecolor(RULE);cb.ax.tick_params(labelsize=12,color=RULE,labelcolor=MUTED)
        self.save(f,'localization-srp-sum',{'grid':{'x_bounds_m':[-1.2,1.4],'y_bounds_m':[-.2,3.0],'shape':[321,261],'spacing_m':.01},
            'map_formula':'R_ij(p)=linear interpolation of computed GCC-PHAT at tau_ij(p)',
            'sum_formula':'R=R21+R31+R32','shared_color_limits':[-1,3],'grid_argmax_m':winner,
            'source_error_m':float(np.linalg.norm(np.array(winner)-SOURCE)),
            'map_extrema':[{'pair':n,'min':float(z.min()),'max':float(z.max())} for n,z in zip(PAIR_NAMES,maps)],
            'summed_min':float(summed.min()),'summed_max':float(summed.max()),
            'caveat':'three non-collinear microphones disambiguate this synthetic scene on this restricted 2D grid; not a general 3D uniqueness guarantee'})
        np.savez_compressed(self.output/'localization-spatial-maps.npz',grid_x_m=gx,grid_y_m=gy,pair_maps=maps,sum_map=summed)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir',type=Path,default=ROOT/'public/diagrams')
    figures=Figures(parser.parse_args().output_dir.resolve())
    figures.tdoa_locus();figures.srp_candidate();figures.srp_sum()
    print('Generated 3 numerically computed localization figures with bounds checks.')
    print(json.dumps({'distances_m':figures.sim['distances_m'].tolist(),
                      'pair_delays_ms':(figures.sim['true_pair_delays_s']*1000).tolist()},indent=2))

if __name__=='__main__':main()
