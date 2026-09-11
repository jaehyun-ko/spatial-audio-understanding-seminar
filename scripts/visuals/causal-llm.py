"""Four original light-theme teaching figures; no experimental data.

Run from any directory with Python/numpy/matplotlib and Pretendard installed.
Outputs SVG (math and fonts as paths), 2x PNG, and label bounds for visual QA.
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch
from matplotlib.font_manager import FontProperties

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'public/diagrams'
FONT_DIR = Path.home() / 'Library/Fonts'
FONT = FontProperties(fname=str(FONT_DIR / 'Pretendard-Regular.otf'))
BOLD = FontProperties(fname=str(FONT_DIR / 'Pretendard-SemiBold.otf'))
BG = '#f6f8fa'; INK = '#142233'; MUTED = '#586879'
BLUE = '#1f5fae'; TEAL = '#008b9a'; ORANGE = '#a95018'
RULE = '#d4dde7'; SOFT = '#e7eff9'; SOFT_TEAL = '#e0f0f1'
plt.rcParams.update({'svg.fonttype': 'path', 'mathtext.fontset': 'stix', 'svg.hashsalt': 'causal-llm-v1'})


def canvas():
    f = plt.figure(figsize=(11.36, 4.04), dpi=100, facecolor=BG)
    a = f.add_axes([0, 0, 1, 1])
    a.set(xlim=(0, 1136), ylim=(404, 0)); a.axis('off')
    return f, a


def txt(a, x, y, t, size=25, c=INK, bold=False, ha='center'):
    # Convert specified pixel size to points at the 100-dpi design canvas.
    return a.text(x, y, t, fontsize=size * .72, color=c, ha=ha, va='center',
                  fontproperties=BOLD if bold else FONT, linespacing=1.28)


def line(a, x1, y1, x2, y2, c=RULE, w=2, ls='-'):
    a.plot([x1, x2], [y1, y2], color=c, lw=w * .72, ls=ls)


def arrow(a, p, q, c=MUTED, w=2):
    a.add_patch(FancyArrowPatch(p, q, arrowstyle='-|>', mutation_scale=14,
                              color=c, lw=w * .72))


def box(a, x, y, w, h, label='', c=BLUE, fill=BG, size=26):
    a.add_patch(Rectangle((x, y), w, h, ec=c, fc=fill, lw=1.5))
    if label:
        txt(a, x+w/2, y+h/2, label, size, c, True)


def matrix(a, x, y, rows=4, cols=6, c=BLUE, cell=12, gap=4):
    for r in range(rows):
        for k in range(cols):
            a.add_patch(Rectangle((x+k*(cell+gap), y+r*(cell+gap)), cell, cell,
                                  fc=c, ec='none', alpha=.25+.7*((r*3+k*5)%11)/10))


def wave(a, x, y, w=100, c=BLUE, phase=0):
    t=np.linspace(0, 1, 200)
    v=np.sin(2*np.pi*4*t+phase)*np.exp(-((t-.5)/.3)**2)
    a.plot(x+w*t, y+18*v, c=c, lw=1.8)


def token(a, x, y, w=24, h=52, c=BLUE, fade=1):
    a.add_patch(Rectangle((x, y), w, h, fc=c, ec='none', alpha=fade))
    for j in [1, 2, 3]:
        line(a, x+5, y+h*j/4, x+w-5, y+h*j/4, BG, 1)


def save(f, name):
    OUT.mkdir(parents=True, exist_ok=True)
    f.canvas.draw(); renderer=f.canvas.get_renderer(); records=[]
    for a in f.axes:
        for t in a.texts:
            b=t.get_window_extent(renderer)
            records.append({'text':t.get_text(), 'bounds':[round(v,1) for v in (b.x0,b.y0,b.x1,b.y1)]})
            assert b.x0>=-1 and b.y0>=-1 and b.x1<=1137 and b.y1<=405, (name,t.get_text(),b.bounds)
    (OUT/(name+'.labels.json')).write_text(json.dumps(records,ensure_ascii=False,indent=2))
    f.savefig(OUT/(name+'.svg'), facecolor=BG, metadata={'Date':None})
    f.savefig(OUT/(name+'.png'), facecolor=BG, dpi=200)
    plt.close(f)


def contract():
    f,a=canvas()
    txt(a,72,47,'관측',26,c=MUTED)
    wave(a,23,149,100,BLUE);wave(a,23,199,100,TEAL,.55)
    txt(a,72,250,r'$X$',32)
    box(a,156,137,106,83,'인코더\nE',BLUE,SOFT)
    arrow(a,(123,178),(150,178))
    arrow(a,(270,178),(304,178))
    matrix(a,315,139,5,6,BLUE,12,4)
    txt(a,360,251,r'$H\;[T\!\times\!d_e]$',30)
    arrow(a,(415,178),(450,178))
    box(a,458,137,122,83,'어댑터\nP',TEAL,SOFT_TEAL)
    arrow(a,(588,178),(623,178))
    for k in range(4): token(a,632+k*29,140,22,78,TEAL,.45+.18*k)
    txt(a,684,251,r'$Z\;[K\!\times\!d_{\rm LLM}]$',30)
    arrow(a,(752,178),(828,178))
    box(a,836,137,147,83,'',BLUE,SOFT)
    txt(a,909,163,'LLM',28,c=BLUE,bold=True)
    txt(a,909,197,'고정 또는 적응',21,c=BLUE)
    txt(a,909,25,'질문 임베딩',25,c=MUTED)
    for k in range(4):token(a,863+k*25,52,18,34,MUTED,.4+.17*k)
    arrow(a,(909,91),(909,131))
    arrow(a,(991,178),(1040,178))
    txt(a,1081,177,'답변',28,bold=True)
    line(a,153,285,415,285,BLUE,3)
    line(a,457,285,752,285,TEAL,3)
    line(a,832,285,1124,285,BLUE,3)
    txt(a,284,315,'의미·공간·시간 표현',24,c=BLUE)
    txt(a,605,315,'길이·차원·융합 정렬',24,c=TEAL)
    txt(a,978,315,'질문에 맞는 조건부 생성',24,c=BLUE)
    txt(a,568,376,'연속 오디오 토큰을 입력 시퀀스에 추가  ·  어휘 수와 임베딩 폭은 별개',25,c=MUTED)
    save(f,'causal-audio-llm-contract')


def small_trajectory(a, x, y, reverse=False):
    # Toy azimuth trajectories: source identities remain A/B, direction reverses.
    w=188;h=92
    line(a,x,y+h/2,x+w,y+h/2,RULE,1.5,':')
    arrow(a,(x,y+h+8),(x+w+5,y+h+8),MUTED,1.3)
    xs=np.array([x,x+w/2,x+w]); ys=np.array([y+h,y+h/2,y])
    if reverse:ys=ys[::-1]
    a.plot(xs,ys,c=BLUE,lw=2.4,marker='o',ms=5)
    a.plot(xs,2*y+h-ys,c=TEAL,lw=2.4,marker='s',ms=5,ls='--')
    txt(a,x+w+13,y+h+9,'t',24,c=MUTED)
    txt(a,x-8,y,'+',25,c=MUTED,ha='right')
    txt(a,x-8,y+h,'−',25,c=MUTED,ha='right')


def bottleneck():
    f,a=canvas()
    txt(a,288,25,'단순 시간 평균',28,bold=True)
    txt(a,873,25,'시간에 결속된 표현',28,bold=True)
    txt(a,879,53,'장면 1의 설명용 속성',24,c=MUTED)
    line(a,574,12,574,347)
    txt(a,155,71,'장면 1',25,c=BLUE,bold=True)
    txt(a,405,71,'장면 2',25,c=BLUE,bold=True)
    small_trajectory(a,61,102,False)
    small_trajectory(a,312,102,True)
    txt(a,50,71,'방향',24,c=MUTED)
    arrow(a,(155,222),(226,258),ORANGE)
    arrow(a,(405,222),(329,258),ORANGE)
    txt(a,284,283,r'$\bar{\theta}_A=\bar{\theta}_B=0$',32,c=ORANGE)
    txt(a,284,324,'두 장면의 평균이 같다',25,c=ORANGE)
    # Labeled spatial attributes in the toy illustration, not actual LLM tokens.
    txt(a,655,99,'음원',24,c=MUTED)
    for j in range(3):
        txt(a,754+j*145,83,r'$t_'+str(j+1)+'$',28,c=MUTED)
    txt(a,650,144,'A',30,c=BLUE,bold=True)
    txt(a,650,223,'B',30,c=TEAL,bold=True)
    for row,values,c in [(0,[-60,0,60],BLUE),(1,[60,0,-60],TEAL)]:
        for j,v in enumerate(values):
            x=709+j*145;y=114+row*79
            box(a,x,y,90,59,r'$'+str(v)+r'^\circ$',c,SOFT if row==0 else SOFT_TEAL,29)
            if j<2:arrow(a,(x+95,y+30),(x+135,y+30),c)
    txt(a,881,286,'ST-AudioLM: 의미 1 + 시간 40',25,c=BLUE)
    txt(a,881,324,'TWNM: 밀집 시계열을 전달',25,c=TEAL)
    txt(a,568,379,'교육용 반례  ·  순서 없는 평균에 한정하며 모든 전역 토큰의 한계를 뜻하지 않음',24,c=MUTED)
    save(f,'causal-token-bottleneck')


def training():
    f,a=canvas()
    for x in [374,763]:line(a,x,15,x,247)
    txt(a,185,31,'① 표현 사전학습',28,bold=True)
    txt(a,568,31,'② 연결 정렬',28,bold=True)
    txt(a,958,31,'③ 언어 적응',28,bold=True)
    # Learning supervision branches instead of a prose panel.
    box(a,45,111,109,83,'E',BLUE,SOFT,31)
    arrow(a,(164,152),(209,152),BLUE)
    line(a,214,104,214,196,BLUE,1.5)
    for y,label in [(101,'사건'),(150,'위치'),(199,'시간')]:
        arrow(a,(214,y),(250,y),BLUE)
        txt(a,303,y,label,27,c=BLUE)
    txt(a,184,246,'목적에 맞는 지도',24,c=MUTED)
    box(a,399,118,79,69,'E',MUTED,BG,30)
    arrow(a,(483,152),(503,152))
    box(a,508,118,87,69,'P',TEAL,SOFT_TEAL,30)
    arrow(a,(600,152),(620,152))
    box(a,625,118,109,69,'LLM',MUTED,BG,28)
    txt(a,438,218,'고정',24,c=MUTED)
    txt(a,552,218,'학습',24,c=TEAL)
    txt(a,680,218,'고정',24,c=MUTED)
    box(a,786,118,77,69,'E',MUTED,BG,30)
    arrow(a,(868,152),(883,152))
    box(a,888,118,77,69,'P',TEAL,SOFT_TEAL,30)
    arrow(a,(970,152),(985,152))
    box(a,990,118,119,69,'LLM',MUTED,BG,28)
    box(a,988,78,122,33,'LoRA 학습',BLUE,SOFT,24)
    txt(a,926,218,'학습',24,c=TEAL)
    txt(a,1050,218,'기본 고정',24,c=MUTED)
    line(a,21,270,1115,270)
    txt(a,38,311,'Spatial-Omni QA',25,c=BLUE,bold=True,ha='left')
    txt(a,690,311,'P  →  P + LoRA  →  P + LoRA + 공간 E',26)
    txt(a,38,367,'Sci-Phi QA',25,c=TEAL,bold=True,ha='left')
    txt(a,690,367,'공간 E + P + Spatial LoRA를 함께 학습',26)
    save(f,'causal-adapter-training')


def lora():
    f,a=canvas()
    txt(a,173,29,'P의 출력과 질문',27,bold=True)
    txt(a,620,29,r'$W=W_0+\frac{\alpha}{r}BA$',35,c=BLUE)
    txt(a,1008,29,'답변 생성',27,bold=True)
    txt(a,85,97,'오디오 Z',25,c=TEAL)
    for k in range(4):token(a,33+k*30,122,23,62,TEAL,.45+.17*k)
    txt(a,90,241,'질문',25,c=MUTED)
    for k in range(4):token(a,33+k*30,266,23,46,MUTED,.45+.17*k)
    # Concatenation into a single embedding stream, not a vocabulary expansion.
    line(a,167,152,189,152,TEAL)
    line(a,167,289,189,289,MUTED)
    line(a,190,152,190,289,MUTED)
    arrow(a,(195,220),(300,220))
    txt(a,245,273,r'$h$',31)
    # A magnified linear layer inside the LLM.
    a.add_patch(Rectangle((313,83),559,244,ec=RULE,fc=BG,lw=1.5))
    txt(a,588,107,'LLM 내부 선형층 하나',25,c=MUTED)
    line(a,325,220,365,220,MUTED)
    line(a,365,174,365,271,MUTED)
    arrow(a,(365,174),(420,174))
    box(a,428,140,208,68,r'$W_0$',MUTED,BG,34)
    txt(a,683,145,'고정',24,c=MUTED)
    line(a,638,174,743,174,MUTED)
    arrow(a,(365,271),(420,271),BLUE)
    box(a,428,242,69,58,r'$A$',BLUE,SOFT,32)
    arrow(a,(500,271),(562,271),BLUE)
    txt(a,532,247,r'$r$',26,c=BLUE)
    box(a,568,242,69,58,r'$B$',BLUE,SOFT,32)
    line(a,640,271,743,271,BLUE)
    txt(a,686,242,r'$\alpha/r$',26,c=BLUE)
    txt(a,689,299,'학습',24,c=BLUE)
    line(a,743,174,743,271,MUTED)
    a.add_patch(Circle((743,220),15,ec=BLUE,fc=BG,lw=1.5))
    txt(a,743,219,'+',25,c=BLUE)
    arrow(a,(763,220),(852,220))
    txt(a,822,185,r"$h'$",31)
    arrow(a,(880,220),(924,220))
    # A vocabulary distribution is illustrative, not a model output.
    for j,h in enumerate([18,39,74,27,12]):
        a.add_patch(Rectangle((941+j*31,224-h),19,h,fc=BLUE,ec='none',alpha=.9 if j==2 else .35))
    line(a,931,225,1101,225,MUTED,1.5)
    txt(a,1016,102,'후속 층·출력 헤드',24,c=MUTED)
    txt(a,1016,274,'기존 어휘',26,c=BLUE)
    txt(a,1016,310,'확률 분포',25,c=MUTED)
    txt(a,568,380,'P는 입력을 정렬하고  ·  LoRA는 LLM이 입력을 처리하는 선형층을 적응한다',25,c=MUTED)
    save(f,'causal-lora-reading')


if __name__ == '__main__':
    contract();bottleneck();training();lora()
    print('Generated four causal LLM bridge figures (1136×404 SVG, 2272×808 PNG).')
