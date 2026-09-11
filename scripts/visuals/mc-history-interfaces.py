"""Three light scientific architecture diagrams for MC Audio-LLM history.

Author-created explanatory schematics grounded in plans/EVIDENCE_P12_P23.md
and plans/CAUSAL_LLM_MODULES.md. No benchmark values or inferred activations.
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch
from matplotlib.font_manager import FontProperties

ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'public/diagrams'
FONT=FontProperties(fname=str(Path.home()/'Library/Fonts/Pretendard-Regular.otf'))
BOLD=FontProperties(fname=str(Path.home()/'Library/Fonts/Pretendard-SemiBold.otf'))
BG='#f6f8fa';INK='#142233';MUTED='#586879';BLUE='#1f5fae'
TEAL='#008b9a';ORANGE='#a95018';RULE='#d4dde7';SOFT='#e7eff9';SOFT_TEAL='#e0f0f1'
plt.rcParams.update({'svg.fonttype':'path','mathtext.fontset':'stix','svg.hashsalt':'mc-history-interfaces-v1'})

def canvas():
    f=plt.figure(figsize=(11.36,4.04),dpi=100,facecolor=BG)
    a=f.add_axes([0,0,1,1]);a.set(xlim=(0,1136),ylim=(404,0));a.axis('off')
    return f,a

def txt(a,x,y,t,size=25,c=INK,bold=False,ha='center'):
    return a.text(x,y,t,fontsize=size*.72,color=c,ha=ha,va='center',
                  fontproperties=BOLD if bold else FONT,linespacing=1.2)

def line(a,p,q,c=RULE,w=1.5,ls='-'):
    a.plot([p[0],q[0]],[p[1],q[1]],c=c,lw=w*.72,ls=ls)

def arrow(a,p,q,c=MUTED,w=2,ls='-'):
    a.add_patch(FancyArrowPatch(p,q,arrowstyle='-|>',mutation_scale=12,color=c,lw=w*.72,ls=ls))

def box(a,x,y,w,h,label,c=BLUE,fill=BG,size=25):
    a.add_patch(Rectangle((x,y),w,h,ec=c,fc=fill,lw=1.35))
    if label:txt(a,x+w/2,y+h/2,label,size,c,True)

def waves(a,x,y,w=102,stereo=True):
    ts=np.linspace(0,1,180)
    for dy,c,phase in ([(-14,BLUE,0),(14,TEAL,.6)] if stereo else [(0,BLUE,0)]):
        a.plot(x+ts*w,y+dy+12*np.sin(2*np.pi*4*ts+phase)*np.exp(-((ts-.5)/.3)**2),c=c,lw=1.6)

def audio_tokens(a,x,y):
    for col in range(5):
        for row in range(4):
            a.add_patch(Rectangle((x+col*22,y+row*15),16,10,ec='none',fc=TEAL,alpha=.30+.65*((col*3+row*5)%9)/8))

def save(f,name):
    OUT.mkdir(parents=True,exist_ok=True)
    f.canvas.draw();renderer=f.canvas.get_renderer();labels=[]
    for a in f.axes:
        for t in a.texts:
            b=t.get_window_extent(renderer)
            assert b.x0>=-1 and b.y0>=-1 and b.x1<=1137 and b.y1<=405,(name,t.get_text(),b.bounds)
            labels.append({'text':t.get_text(),'bounds':[round(v,1) for v in (b.x0,b.y0,b.x1,b.y1)]})
    (OUT/f'{name}.labels.json').write_text(json.dumps(labels,ensure_ascii=False,indent=2))
    f.savefig(OUT/f'{name}.svg',facecolor=BG,metadata={'Date':None})
    f.savefig(OUT/f'{name}.png',facecolor=BG,dpi=200)
    plt.close(f)

def interfaces():
    f,a=canvas()
    txt(a,91,25,'Motion · 2025',26,BLUE,True)
    txt(a,255,25,'학습된 지각 E',25,BLUE,True)
    txt(a,502,25,'예측 속성 JSON',25,BLUE,True)
    txt(a,771,25,'기존 텍스트 토큰',25,MUTED,True)
    waves(a,30,99,111);txt(a,85,153,'stereo',23,MUTED)
    arrow(a,(146,99),(190,99))
    box(a,196,67,122,66,'지각 인코더',BLUE,SOFT,24)
    arrow(a,(324,99),(364,99))
    box(a,369,59,262,83,'',BLUE,SOFT)
    txt(a,500,82,'Event  ·  DoA',25,BLUE)
    txt(a,500,116,'Distance  ·  Time',25,BLUE)
    arrow(a,(637,99),(678,99))
    for x,label,w in [(687,'{',30),(725,'event',74),(807,':',27),(842,'…',36)]:
        box(a,x,78,w,42,label,MUTED,BG,24)
    arrow(a,(886,99),(932,99))
    box(a,940,67,103,66,'LM',MUTED,BG,29)
    arrow(a,(1050,99),(1081,99));txt(a,1110,99,'답',26,INK,True)
    txt(a,984,155,'추가 학습 없이 연결',22,MUTED)
    line(a,(13,190),(1123,190))
    txt(a,89,221,'OWL · 2025',26,BLUE,True)
    txt(a,256,221,'학습된 지각 E',25,BLUE,True)
    txt(a,498,221,'연속 표현 정렬 P',25,TEAL,True)
    txt(a,769,221,r'연속 오디오 $Z$',25,TEAL,True)
    waves(a,30,291,111);txt(a,85,341,'binaural',23,MUTED)
    arrow(a,(146,291),(190,291))
    box(a,196,259,122,66,'SAGE',BLUE,SOFT,27)
    arrow(a,(324,291),(367,291))
    box(a,376,259,246,66,'Q-Former',TEAL,SOFT_TEAL,26)
    arrow(a,(630,291),(696,291))
    audio_tokens(a,714,264)
    arrow(a,(827,291),(893,291))
    box(a,899,259,122,66,'LM + LoRA',BLUE,SOFT,24)
    arrow(a,(1027,291),(1066,291));txt(a,1100,291,'답',26,INK,True)
    txt(a,1005,349,'CoT·답변 학습 지도',22,ORANGE)
    arrow(a,(1087,337),(1096,310),ORANGE,1.7,':')
    txt(a,568,382,'연속 임베딩을 입력에 추가  ≠  hidden width·어휘 수 확대',24,MUTED)
    save(f,'history-interfaces')

def bat():
    f,a=canvas()
    txt(a,139,24,'일반 오디오 언어화',27,BLUE,True)
    txt(a,499,24,'Pengi · 2023',25,MUTED)
    # A high-level reference architecture, not a claim that BAT copies Pengi.
    waves(a,29,97,110,stereo=False);txt(a,84,149,'audio',23,MUTED)
    arrow(a,(146,97),(201,97))
    box(a,210,65,185,64,'오디오 인코더',BLUE,SOFT,26)
    arrow(a,(403,97),(462,97))
    box(a,470,65,169,64,'연결 매핑',TEAL,SOFT_TEAL,26)
    arrow(a,(647,97),(706,97))
    audio_tokens(a,716,69)
    arrow(a,(830,97),(880,97))
    box(a,888,65,189,64,'LM 고정',MUTED,BG,27)
    line(a,(18,182),(1118,182))
    txt(a,126,214,'BAT · 2024',27,BLUE,True)
    txt(a,547,214,'공간 관측을 읽는 E와 공간 QA',26,BLUE,True)
    waves(a,29,286,110);txt(a,84,337,'binaural',23,MUTED)
    arrow(a,(146,286),(201,286))
    box(a,210,250,185,73,'Spatial-AST',BLUE,SOFT,26)
    arrow(a,(403,286),(462,286))
    box(a,470,250,169,73,'Projector',TEAL,SOFT_TEAL,26)
    arrow(a,(647,286),(706,286))
    audio_tokens(a,716,258)
    arrow(a,(830,286),(880,286))
    box(a,888,250,189,73,'LLaMA 2',BLUE,SOFT,27)
    # Dashed arrows depict training supervision, not runtime audio inputs.
    txt(a,291,385,'사건 · 방향 · 거리 지도',24,BLUE,True)
    arrow(a,(298,366),(300,329),BLUE,2,':')
    txt(a,778,385,'공간 QA  →  P·LM 적응',24,TEAL,True)
    line(a,(554,350),(981,350),TEAL,1.4,':')
    arrow(a,(554,350),(554,329),TEAL,1.7,':')
    arrow(a,(981,350),(981,329),TEAL,1.7,':')
    line(a,(778,364),(778,350),TEAL,1.4,':')
    save(f,'history-bat')

def encoder_branches():
    f,a=canvas()
    txt(a,127,42,'binaural',25,MUTED)
    arrow(a,(197,42),(253,42))
    box(a,261,17,97,50,'E',BLUE,SOFT,30)
    arrow(a,(366,42),(422,42))
    box(a,430,17,97,50,'P',TEAL,SOFT_TEAL,30)
    arrow(a,(535,42),(591,42))
    box(a,599,17,123,50,'LM',BLUE,SOFT,28)
    txt(a,934,42,'E를 바꾸는 두 접근',28,BLUE,True)
    line(a,(14,84),(1122,84))
    line(a,(567,106),(567,390))
    txt(a,277,116,'DSpAST · 특징과 과제별 선택',27,BLUE,True)
    txt(a,851,116,'OWL · 기하 보조 사전학습',27,BLUE,True)
    # DSpAST task branches use feature attention; patch/Transformer weights shared.
    box(a,16,197,107,109,'mel\nIPD·ILD\nGCC',MUTED,BG,24)
    arrow(a,(130,250),(161,250))
    line(a,(164,178),(164,323),BLUE,1.5)
    for y,label,c in [(179,'사건',BLUE),(251,'방향',TEAL),(323,'거리',TEAL)]:
        arrow(a,(164,y),(191,y),c,1.7)
        box(a,197,y-23,151,46,label+' attention',c,SOFT if c==BLUE else SOFT_TEAL,21)
        arrow(a,(355,y),(401,y),c,1.5)
        box(a,407,y-23,115,46,'공유 T',BLUE,SOFT,23)
        line(a,(529,y),(546,y),MUTED,1.4)
    line(a,(546,179),(546,323),MUTED,1.4)
    arrow(a,(546,323),(546,335),MUTED,1.5)
    txt(a,546,351,r'$H$',24,BLUE)
    txt(a,277,377,'T: 공유 Transformer · 세 표현 결합',23,BLUE)
    # OWL supervision is only used for E pretraining, not QA input.
    txt(a,786,163,'Depth + RIR 정답',24,ORANGE,True)
    txt(a,786,190,'사전학습에서만',22,ORANGE)
    arrow(a,(786,207),(786,225),ORANGE,1.8,':')
    waves(a,592,270,95)
    arrow(a,(692,270),(721,270))
    box(a,727,235,119,70,'SAGE',BLUE,SOFT,26)
    arrow(a,(853,270),(877,270))
    box(a,884,235,73,70,'P',TEAL,SOFT_TEAL,28)
    arrow(a,(964,270),(986,270))
    box(a,993,235,125,70,'LM + LoRA',BLUE,SOFT,22)
    txt(a,786,337,'QA: E 고정',23,MUTED)
    txt(a,998,337,'P + LoRA 학습',23,TEAL)
    txt(a,851,378,'QA 추론 입력은 바이노럴 오디오',24,BLUE)
    save(f,'history-encoder-branches')

if __name__=='__main__':
    interfaces();bat();encoder_branches()
    print('Generated 3 history diagrams (SVG, 2x PNG, checked label bounds).')
