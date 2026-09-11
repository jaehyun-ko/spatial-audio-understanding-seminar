"""Research-history teaching figures; dates are first public release, not adopted version."""
import importlib.util
from pathlib import Path
s=importlib.util.spec_from_file_location('base',Path(__file__).with_name('causal-llm.py'));b=importlib.util.module_from_spec(s);s.loader.exec_module(b)
canvas,txt,line,arrow,box,token,save=b.canvas,b.txt,b.line,b.arrow,b.box,b.token,b.save
BLUE,TEAL,INK,MUTED,BG,SOFT,RULE,ORANGE=b.BLUE,b.TEAL,b.INK,b.MUTED,b.BG,b.SOFT,b.RULE,b.ORANGE

def history():
 f,a=canvas()
 # Columns are episodes, not a linear metric or uniform time axis.
 xs=[18,238,553,858];ws=[196,289,278,260]
 for x,w,date in zip(xs,ws,['2024.02','2025.09','2025.10–2026.06','2026.02–06']):
  txt(a,x,22,date,24,BLUE,True,ha='left');line(a,x,49,x+w,49,BLUE,3)
 txt(a,18,90,'공간 QA 연결',27,INK,True,ha='left')
 box(a,18,133,196,85,'BAT',BLUE,SOFT,30)
 txt(a,116,260,'공간 E → P → LM',21,BLUE)
 txt(a,116,306,'정적 장면의 관계',22,MUTED)
 txt(a,238,90,'같은 시기의 분화',27,INK,True,ha='left')
 box(a,238,128,289,66,'DSpAST · OWL',BLUE,SOFT,25)
 txt(a,382,218,'과제별 단서 · 기하 감독',23,BLUE)
 box(a,238,258,289,58,'Motion: JSON → LM',TEAL,b.SOFT_TEAL,24)
 txt(a,382,342,'명시적 사건·좌표 시계열',22,TEAL)
 txt(a,553,90,'기존 Audio-LM 확장',27,INK,True,ha='left')
 txt(a,692,148,'Sci-Phi  ·  PhaseCoder',23,BLUE,True)
 txt(a,692,186,'TWNM*  ·  Spatial-Omni',23,BLUE,True)
 box(a,562,229,260,87,'의미 경로 + 공간 경로',TEAL,b.SOFT_TEAL,23)
 txt(a,692,344,'기하 · 음원 결속 · 이식',22,MUTED)
 txt(a,858,90,'동적 장면의 표현',27,INK,True,ha='left')
 txt(a,988,151,'Dynamic QA',25,BLUE,True)
 txt(a,988,198,'ST-AudioLM',25,BLUE,True)
 box(a,858,243,260,73,'시간·궤적을 토큰에',TEAL,b.SOFT_TEAL,24)
 txt(a,988,343,'BAT 기반을 각각 확장',22,MUTED)
 txt(a,568,386,'최초 공개 시점 · 연구 질문별 묶음   |   *TWNM의 FOA·SAPO는 2026.05 v3',21,MUTED)
 save(f,'history-map')

def extensions():
 f,a=canvas()
 txt(a,153,25,'기존 의미·음성 경로',25,BLUE,True)
 txt(a,153,219,'새 공간 경로',25,TEAL,True)
 box(a,24,73,124,65,'의미 E',BLUE,SOFT,26);arrow(a,(155,106),(192,106),BLUE);box(a,199,73,100,65,'P',BLUE,SOFT,28)
 box(a,24,263,124,65,'공간 E',TEAL,b.SOFT_TEAL,26);arrow(a,(155,296),(192,296),TEAL);box(a,199,263,100,65,'P',TEAL,b.SOFT_TEAL,28)
 for y,c in [(94,BLUE),(284,TEAL)]:
  arrow(a,(307,y+12),(347,y+12),c)
  for k in range(3):token(a,354+k*26,y-9,19,44,c,.55+.2*k)
 line(a,445,106,475,106,BLUE);line(a,445,296,475,296,TEAL);line(a,475,106,475,296,MUTED)
 arrow(a,(476,202),(511,202));box(a,519,158,134,88,'Audio-LM',BLUE,SOFT,26)
 txt(a,585,294,'LM 적응',24,BLUE,True)
 txt(a,585,326,'예: LoRA',22,MUTED)
 line(a,688,6,688,351)
 for y,name,question in [(38,'Sci-Phi · 2025.10','기존 의미 경로를 고정하고 확장'),(116,'PhaseCoder · 2026.01','채널 위상과 마이크 좌표를 연결'),(194,'TWNM · v3 2026.05','의미·공간의 밀집 특징을 융합'),(272,'Spatial-Omni · 2026.06','여러 기반 모델에 단계적으로 이식')]:
  txt(a,716,y,name,24,TEAL,True,ha='left');txt(a,716,y+34,question,22,INK,ha='left')
 txt(a,568,384,'공통 설계 문제의 비교 · 서로를 순차 개량한 모델이라는 뜻은 아님',23,MUTED)
 save(f,'history-extensions')

def dynamics():
 f,a=canvas()
 for x in [367,758]:line(a,x,12,x,347)
 columns=[(181,'Motion · 2025.09','예측 속성을 명시'),(562,'Dynamic QA · 2026.02','시간 인식 특징을 연결'),(947,'ST-AudioLM · 2026.06','궤적을 지도하고 토큰화')]
 for x,title,sub in columns:txt(a,x,26,title,25,BLUE,True);txt(a,x,67,sub,24,INK,True)
 # Same toy trajectory, three representations. Not measured model outputs.
 for x in [66,448,833]:
  arrow(a,(x,167),(x+232,167),MUTED,1)
  for j,v in enumerate([-.7,-.1,.8]):
   a.plot(x+18+j*86,132-v*29,'o',color=TEAL,ms=7)
  a.plot([x+18,x+104,x+190],[152,135,109],color=TEAL,lw=2)
 txt(a,181,201,'event · azimuth(t) · distance(t)',20,TEAL)
 box(a,53,238,256,61,'JSON → 텍스트 LM',TEAL,b.SOFT_TEAL,24)
 txt(a,181,333,'추론 LM 연결은 training-free',21,MUTED)
 txt(a,562,200,'시간 특징 → Q-Former',23,TEAL)
 box(a,424,238,276,61,'오디오 토큰 → Qwen3',BLUE,SOFT,23)
 txt(a,562,333,'구간 mask · thinking 비교',22,MUTED)
 txt(a,947,201,'사건 · 활동 · 방향 · 거리',23,TEAL)
 box(a,813,238,268,61,'의미 1 + 시간 40 → LM',BLUE,SOFT,23)
 txt(a,947,333,'같은 41-token 기준선과 비교',22,MUTED)
 txt(a,568,384,'상단 궤적은 설명용 · Dynamic QA와 ST-AudioLM은 BAT 기반을 각각 확장',22,MUTED)
 save(f,'history-dynamics')

def synthesis():
 f,a=canvas()
 # Problems on left; observable interface and test on right. One row per historical turn.
 for x,label in [(10,'연구에서 바뀐 질문'),(408,'정보가 넘어가는 경계'),(838,'필요한 확인')]:txt(a,x,23,label,25,BLUE,True,ha='left')
 rows=[('BAT: 위치에서 관계 질문으로','E → P → LM','질문만 / 오디오 추가'),('DSpAST · OWL: 무엇을 배울까','물리 단서·기하 지도 → E','같은 LM에서 E 비교'),('Motion: 예측을 언어로 넘길까','속성 시계열 → JSON → LM','예측 오류·표현의 누락'),('기존 Audio-LM: 공간을 더할까','의미 + 공간 → P → LM','공간 기여·의미 능력'),('Dynamic · ST: 이동을 묻는다면','사건·시간·음원 → 토큰','시간·정체성 결속')]
 for i,(problem,interface,test) in enumerate(rows):
  y=84+i*64;line(a,10,y+34,1123,y+34)
  txt(a,10,y,problem,23,INK,True,ha='left');txt(a,408,y,interface,23,TEAL,ha='left');txt(a,838,y,test,22,INK,ha='left')
 save(f,'history-synthesis')

history();extensions();dynamics();synthesis()
print('Generated 4 MC history spine diagrams')
