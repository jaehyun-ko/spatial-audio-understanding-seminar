---
theme: default
title: '공간 소리를 듣고 판단하는 모델'
description: 'GCC-PHAT 시간차 추정과 SRP 좌표 탐색, Neural-SRP 응답 학습을 설명한 뒤 LLM 통합으로 연결한다: 본문 49장과 근거 부록 36장'
aspectRatio: 16/9
canvasWidth: 1280
colorSchema: light
transition: none
routerMode: hash
mdc: true
fonts:
  sans: Seminar Pretendard
  provider: none
layout: seminar-cover
drawings:
  persist: false
---

# 공간 소리를 듣고<br/>판단하는 모델

::identity::
<div class="seminar-brand"><img src="/iiplab-mark.png" alt="서강대학교 IIP Lab 심볼" /><div><div class="seminar-brand-name">서강대학교 지능정보처리 연구실</div><div class="seminar-brand-detail">Intelligent Information Processing Lab</div></div></div>

::subtitle::
마이크의 관측을 LLM의 답변으로 연결하는 조건

::source::
본문 49장 · 근거 부록 36장 · 27편의 설계와 검증 범위

<!--
[현재 S01 · 본문]
01 · 신호에서 좌표를 찾는 과정

[설명의 중심]
발표의 중심 질문은 공간 단서를 LLM의 답변까지 전달하고 사용하게 만드는 조건이다.

[연결]
다음에 확인할 질문: 출력 목표인 종류·방위각·고도각·거리를 좌표로 정의한다.

[상세 근거와 해석 범위]
[S1 발표 노트]
[설명 순서]
“소리를 들은 모델이 무엇이 어디에 있는지 판단하는 연구를 다룹니다. 같은 장면에 서로 다른 질문을 던지면서 각 연구의 설계와 확인된 능력을 비교하겠습니다.”

[경계·원문의 추가 자료]
생성·렌더링·로봇 행동은 독립 주제에서 제외한다. 기술들이 차례로 대체됐다는 역사적 계보를 주장하지 않는다.


범위: 청각 입력을 이용한 공간 판단. 기술 간 단선적 대체 역사나 생성·렌더링·로봇 행동의 개관을 뜻하지 않는다.
[Sources]
- https://iip.sogang.ac.kr/layouts/iiplab/top-logo.png
-->

---
layout: "seminar"
variant: "figure"
transition: "none"
chapter: "01 · 신호에서 좌표를 찾는 과정"
causalStage: "main"
originSlide: 2
---

# 공간 오디오 이해의 목표

::body::
<ManimScene src="/animations/intro-sequence/s02.mp4" webm="/animations/intro-sequence/s02.webm" poster="/animations/intro-sequence/s02-start.png" print-poster="/animations/intro-sequence/s02-end.png" description="공간 오디오 이해의 목표: 같은 3차원 장면을 유지하는 설명용 애니메이션" />

::takeaway::
음원의 종류와 위치: 방위각·고도각·거리

::source::
MathWorks, Spherical Coordinates. 목표 좌표 정의이며 단일 TDoA의 3차원 복원을 뜻하지 않음.

<!--
[현재 S02 · 본문]
01 · 신호에서 좌표를 찾는 과정

[설명의 중심]
출력 목표인 종류·방위각·고도각·거리를 좌표로 정의한다.

[연결]
다음에 확인할 질문: 같은 음원의 전파가 채널별 관측 차이가 되는 과정을 본다.

[상세 근거와 해석 범위]
[S2 발표 노트]
일반 음원 s(t)의 종류와 위치를 알아내는 것이 목표다. O는 마이크 쌍의 중점이고 M1=(-d/2,0,0), M2=(d/2,0,0)이다. 방위각 α는 xy 평면에서 +x에서 +y 방향, 고도각 β는 xy 평면에서 +z 방향, 거리 r는 O에서 음원까지의 유클리드 거리다. 두 마이크의 단일 도달 시간차만으로 세 좌표가 유일하게 복원되는 것은 아니다. 3차원 위치는 공통 사투영으로 표시하고 물리량은 투영 전 좌표로 계산한다. 다음에는 이 장면이 실제 입력 신호에 어떻게 나타나는지 본다.

[Sources]
- https://www.mathworks.com/help/phased/ug/spherical-coordinates.html
-->

---
layout: "seminar"
variant: "figure"
transition: "none"
chapter: "01 · 신호에서 좌표를 찾는 과정"
causalStage: "main"
originSlide: 3
---

# 두 채널 관측 신호

::body::
<ManimScene src="/animations/intro-sequence/s03.mp4" webm="/animations/intro-sequence/s03.webm" poster="/animations/intro-sequence/s03-start.png" print-poster="/animations/intro-sequence/s03-end.png" description="두 채널 관측 신호: 같은 3차원 장면을 유지하는 설명용 애니메이션" />

::takeaway::
같은 음원에서 출발한 소리, 서로 다른 두 관측

::source::
AGG-RL, ICLR 2026, Fig. 1(a) 기반 재구성. 직접음 모델 · 설명용 합성 신호 · 진폭 임의 단위.

<!--
[현재 S03 · 본문]
01 · 신호에서 좌표를 찾는 과정

[설명의 중심]
같은 음원의 전파가 채널별 관측 차이가 되는 과정을 본다.

[연결]
다음에 확인할 질문: 기하가 도달 시간차를 결정하므로 위치 계산의 물리적 근거가 생긴다.

[상세 근거와 해석 범위]
[S3 발표 노트]
음원과 마이크의 위치를 유지한 채 전파 경로와 두 관측 파형을 동시에 보여준다. 각 경로 위 이동점과 파형의 노출은 같은 전파 시간으로 갱신된다. 이동점은 펄스의 기준 시점인 중심을 추적한다. ℓ_m=||p_s-p_m||, t_m=ℓ_m/c, c=343 m/s이며 직접음 신호는 x_m(t)=a_m s(t-t_m)이다. 진폭은 임의 단위이고 시간축은 ms다. 실제 녹음이나 모델의 예측 결과가 아닌 교육용 펄스다. 원문 Fig. 1(a)는 원거리 평면파를 설명하며 이 재구성은 유한 거리의 정확한 경로 길이로 그 관계를 설명한다. 다음에는 음원 위치를 움직여 두 관측의 차이를 확인한다.

[Sources]
- https://proceedings.iclr.cc/paper_files/paper/2026/file/ee860a9fa65a55a335754c557a5211de-Paper-Conference.pdf
-->

---
layout: "seminar"
variant: "figure"
transition: "none"
chapter: "01 · 신호에서 좌표를 찾는 과정"
causalStage: "main"
originSlide: 4
---

# 경로 차이와 시간차

::body::
<ManimScene src="/animations/intro-sequence/s04.mp4" webm="/animations/intro-sequence/s04.webm" poster="/animations/intro-sequence/s04-start.png" print-poster="/animations/intro-sequence/s04-end.png" description="경로 차이와 시간차: 같은 3차원 장면을 유지하는 설명용 애니메이션" />

::takeaway::
경로 차이에 따라 달라지는 도달 시간차

::source::
AGG-RL, ICLR 2026, Fig. 1(a), §2.1 기반. τ=t₂−t₁의 부호 관례 · 단일 직접음.

<!--
[현재 S04 · 본문]
01 · 신호에서 좌표를 찾는 과정

[설명의 중심]
기하가 도달 시간차를 결정하므로 위치 계산의 물리적 근거가 생긴다.

[연결]
다음에 확인할 질문: 잔향과 다른 음원이 겹치면 단순한 직접음 관계를 읽기 어려워진다.

[상세 근거와 해석 범위]
[S4 발표 노트]
거리 r와 고도각 β를 유지하고 방위각만 바꾼다. ℓ1, ℓ2, 도착 시점 t1, t2와 파형을 하나의 기하 상태에서 다시 계산한다. τ=t2-t1=(ℓ2-ℓ1)/c이므로 M2에 먼저 도착하면 τ가 음수다. 음원이 x<0인 방향으로 움직이면 부호가 반대로 바뀐다. 음원 위치가 정지한 각 상태를 비교하는 준정적 설명이며 이동 음원의 도플러 효과를 시뮬레이션하지 않는다. 다음에는 반사 경로와 다른 음원의 기여를 추가한다.

[Sources]
- https://proceedings.iclr.cc/paper_files/paper/2026/file/ee860a9fa65a55a335754c557a5211de-Paper-Conference.pdf
-->

---
layout: "seminar"
variant: "figure"
transition: "none"
chapter: "01 · 신호에서 좌표를 찾는 과정"
causalStage: "main"
originSlide: 5
---

# 잔향과 음원 혼합

::body::
<ManimScene src="/animations/intro-sequence/s05.mp4" webm="/animations/intro-sequence/s05.webm" poster="/animations/intro-sequence/s05-start.png" print-poster="/animations/intro-sequence/s05-end.png" description="잔향과 음원 혼합: 같은 3차원 장면을 유지하는 설명용 애니메이션" />

::takeaway::
직접음에 더해지는 반사음과 다른 음원의 기여

::source::
CCSR, arXiv:2312.00476v2, Fig. 1과 신호 모델 기반. 1차 벽 반사·두 음원의 설명용 확장.

<!--
[현재 S05 · 본문]
01 · 신호에서 좌표를 찾는 과정

[설명의 중심]
잔향과 다른 음원이 겹치면 단순한 직접음 관계를 읽기 어려워진다.

[연결]
다음에 확인할 질문: 배열이 달라지면 같은 위치의 관측도 달라진다. 이 기하는 이후 학습 모델에서도 사라지지 않는다.

[상세 근거와 해석 범위]
[S5 발표 노트]
앞 장면에 벽과 1차 반사 경로를 추가하고, 다음으로 두 번째 음원을 추가한다. CCSR Fig. 1의 직접음, 초기 반사, 후기 잔향 구분과 채널별 전달함수라는 관점을 따른다. 화면에는 직접음과 1차 반사만 명시적으로 계산했으며 확산된 후기 잔향장 전체를 구현하지 않았다. y=3.8 m인 평면 벽에 대한 이미지 음원으로 반사점과 반사 경로 길이를 계산했다. 두 번째 음원은 별도 펄스이고 관측에 선형 합산된다. 일반식 x_m(t)=∑_k(h_mk*s_k)(t)+v_m(t)를 표시하며 이 예에서는 v_m=0이다. 실측 RIR이나 원문의 성능 결과를 재현한 그림이 아니다. 다음에는 직접음 상태로 돌아가 장치 배치의 영향만 분리한다.

[Sources]
- https://arxiv.org/html/2312.00476v2
-->

---
layout: "seminar"
variant: "figure"
transition: "none"
chapter: "01 · 신호에서 좌표를 찾는 과정"
causalStage: "main"
originSlide: 6
---

# 마이크 배열 기하

::body::
<ManimScene src="/animations/intro-sequence/s06.mp4" webm="/animations/intro-sequence/s06.webm" poster="/animations/intro-sequence/s06-start.png" print-poster="/animations/intro-sequence/s06-end.png" description="마이크 배열 기하: 같은 3차원 장면을 유지하는 설명용 애니메이션" />

::takeaway::
같은 음원 위치에서도 마이크 간격에 따라 달라지는 시간차

::source::
AGG-RL, ICLR 2026, Fig. 1(a), §3.2 기반. 음원·배열 중심·좌표계 고정, 마이크 간격만 변경.

<!--
[현재 S06 · 본문]
01 · 신호에서 좌표를 찾는 과정

[설명의 중심]
배열이 달라지면 같은 위치의 관측도 달라진다. 이 기하는 이후 학습 모델에서도 사라지지 않는다.

[연결]
다음에 확인할 질문: 두 채널의 위상 관계를 지연축 점수 곡선으로 바꾸고, 곡선의 최대점에서 시간차를 읽는다.

[상세 근거와 해석 범위]
[S6 발표 노트]
반사음과 다른 음원의 기여를 천천히 없애 직접음 비교 상태로 돌아온다. 음원 위치, 배열 중점 O, 기준 좌표계를 유지하고 두 마이크 간격 d만 1.2 m에서 0.6 m, 1.8 m, 다시 1.2 m로 바꾼다. 수치는 이 도해를 위한 예시이며 원문 실험 조건이 아니다. 변화한 p1,p2로 직접 경로를 다시 계산하므로 원거리 근사값과 유한 거리값을 혼용하지 않는다. 마이크 배열이 달라질 때 관측의 의미를 기하와 함께 해석해야 한다. 다음에는 GCC-PHAT으로 두 관측 신호에서 시간차를 찾는 계산을 설명한다.

[Sources]
- https://proceedings.iclr.cc/paper_files/paper/2026/file/ee860a9fa65a55a335754c557a5211de-Paper-Conference.pdf
-->

---
layout: "seminar"
variant: "figure"
chapter: "01 · 신호에서 좌표를 찾는 과정"
causalStage: "main"
---

# GCC-PHAT: 두 신호에서 시간차를 찾는다

::body::
<PaperFigure src="/diagrams/gcc-phat.svg" alt="같은 음원을 받은 두 채널의 교차스펙트럼을 크기로 나누고 역 FFT하여 시간차별 일치 점수를 구한다. 도입과 같은 tau21=t2-t1을 사용한다." caption="공유 기하에서 계산한 무반향 합성 신호 · τ₂₁=t₂−t₁ · 점수는 표시용 정규화" />

::takeaway::
**시간차별 일치 점수**를 계산한다. 최대점은 지연 추정값이고, 전체 곡선은 SRP의 입력이다.

::source::
Knapp·Carter, 1976 · MathWorks gccphat · 설명용 합성 신호, 논문 실험값 아님

<!--
[현재 S07 · 본문]
01 · 신호에서 좌표를 찾는 과정

[설명의 중심]
두 채널의 위상 관계를 지연축 점수 곡선으로 바꾸고, 곡선의 최대점에서 시간차를 읽는다.

[연결]
다음에 확인할 질문: 측정한 시간차는 같은 거리차를 갖는 후보 곡선을 정한다. 한 쌍으로는 좌표 하나를 정할 수 없다.

[상세 근거와 해석 범위]
[GCC-PHAT 설명]
배열 기하가 주어져도 음원 위치는 아직 모른다. 먼저 녹음한 두 신호를 얼마나 어긋나게 맞추면 잘 일치하는지 계산한다. 왼쪽은 같은 음원의 두 관측이다. FFT로 X1과 X2를 구한 다음 G21=X2·conj(X1)를 만든다. PHAT는 각 주파수의 교차스펙트럼을 그 크기로 나누어 위상 차이를 남긴다. 역 FFT 결과 C21(tau)가 시간차별 일치 점수다. epsilon은 거의 0인 주파수 성분의 나눗셈을 안정화한다.

[부호와 계산 조건]
앞 도입의 tau=t2−t1을 그대로 유지한 tau21 표기다. M1=(-0.65,0),M2=(0.65,0),ps=(0.6,1.6),c=343m/s인 높이를 고정한 2D 예시다. M2까지 경로가 더 짧으므로 tau21과 GCC21의 피크는 음수다. 세 마이크의 합성 신호, 교차스펙트럼, PHAT 스펙트럼과 지연축 점수는 localization-simulation.npz에 보존했다. 다음 세 장도 같은 신호와 기하로 계산한다. 파형은 공통 진폭 척도로 짧은 구간을 표시하고, 스펙트럼 크기와 지연 점수는 각각 표시용으로 정규화했다. 실측이나 학습망 결과가 아니다.

[PHAT가 하는 일]
큰 진폭의 주파수 성분이 상관값을 지배하는 영향을 줄인다. 잡음이나 반사음이 제거된다는 보장은 없다. 설명 그림은 무반향 단일 음원이며 실제 조건에서는 여러 피크가 생길 수 있다.

[좌표 탐색으로 연결]
GCC-PHAT의 출력 축은 x,y,z가 아니라 시간차다. 같은 시간차를 만드는 좌표가 여럿이므로 이 최대점만으로 위치 하나가 정해지지 않는다. 다음 장에서 거리차가 같은 위치들을 그린다. SRP는 쌍마다 가장 큰 피크를 먼저 확정하고 교점을 푸는 방법이 아니라 전체 곡선에서 후보 좌표의 점수를 읽고 합산한다.

[Sources]
- https://www.mathworks.com/help/phased/ref/gccphat.html
- https://arxiv.org/html/2403.09455v1
- https://www.ee.iitb.ac.in/course/~sachinnayak/finalpaper2.pdf
-->

---
layout: "seminar"
variant: "figure"
chapter: "01 · 신호에서 좌표를 찾는 과정"
causalStage: "main"
---

# 지연 하나에 대응하는 좌표는 여러 개다

::body::
<PaperFigure src="/diagrams/localization-tdoa-locus.svg" alt="x축 위 마이크 두 개에 대해 동일한 거리 차이를 갖는 쌍곡선을 수치 계산했다. 서로 다른 세 위치에서 마이크까지의 거리는 달라도 거리 차이 0.430m와 지연 -1.253ms는 같다.">
<template #caption>
<div>지연이 같은 후보 집합 · <MathInline tex="\|p-M_2\|-\|p-M_1\|=c\,\tau_{21}(p_s)" /></div>
</template>
</PaperFigure>

::takeaway::
GCC-PHAT로 얻은 **지연 하나**는 가능한 위치를 **쌍곡선으로 좁힌다**.

::source::
GCC-PHAT / Neural-SRP, 2024, §III-A · 좌표로 계산한 설명용 기하 · 높이 고정 2D 단면

<!--
[현재 S08 · 본문]
01 · 신호에서 좌표를 찾는 과정

[설명의 중심]
측정한 시간차는 같은 거리차를 갖는 후보 곡선을 정한다. 한 쌍으로는 좌표 하나를 정할 수 없다.

[연결]
다음에 확인할 질문: 후보 좌표에서 두 마이크까지 거리를 계산하고, 예상 지연의 GCC-PHAT 값을 읽는다.

[상세 근거와 해석 범위]
[BRIDGE: tdoa-locus 발표 노트]
[핵심 질문]
앞에서 배열의 좌표와 두 채널의 지연을 알았다. 그러면 음원의 좌표를 곧바로 결정할 수 있는가? 관측한 시간 차이를 거리 차이로 바꾸고, 그 거리 차이를 만족하는 후보 위치를 그린다.

[설명 순서]
x축 위 M1=(-0.65,0), M2=(0.65,0) 두 마이크를 그대로 사용한다. 음원 예시 ps=(0.6,1.6)에서 거리는 d1=2.030394m, d2=1.600781m다. M2에 먼저 도착하므로 도입과 같은 부호 tau21=t2-t1=(d2-d1)/343=-1.252516ms다. 오른쪽 막대는 실제 계산한 각 거리이며, 표시한 양의 간격은 d1-d2=0.429613m다. 아래 지연 수식에서는 그 반대 순서 d2-d1를 사용하므로 음수다.

다른 위치 pa=(0.300463...,0.6), pb=(0.935373...,2.6)에서도 같은 거리 차이가 유지된다. 두 대안 좌표의 정확한 값은 그림의 source.json에 보존했다. 이 점들은 임의로 그린 점이 아니라 쌍곡선 x=a sqrt(1+y²/b²), a=(d1-d2)/2, b=sqrt(0.65²-a²)에서 계산했다. 따라서 지연 하나를 얻는 것과 좌표 하나를 결정하는 것은 구별해야 한다. 이 예시에서 높은 GCC 값과 양립하는 위치들이 곡선으로 남는다.

[수식과 적용 범위]
tau_ij(p)=(||p-M_i||-||p-M_j||)/c, c=343m/s. 본문은 tau21=t2-t1를 사용하고 일반화할 때도 첨자와 상관 스펙트럼의 순서를 일치시킨다. 2D의 등거리차 곡선은 쌍곡선이다. 3D에서는 회전쌍곡면이므로 두 마이크의 단일 TDoA만으로 azimuth/elevation/distance 세 값을 유일하게 복원할 수 없다. 그림은 마이크와 음원 높이를 고정한 2D 단면이며, 쌍곡선 일부만 화면에 표시했다.

설명용 궤적은 생성 기하의 정확한 지연 tau21(ps)=-1.252516ms를 사용한다. 앞 GCC 그림에서 유한 지연 격자의 최대점으로 읽은 추정값은 -1.253906ms로, 16배 보간 격자 간격 0.003906ms 이내의 차이가 있다. 본문의 -1.253ms 표기는 정확한 기하 지연을 반올림한 값이다. 유한 FFT 격자의 추정값과 연속 기하를 엄밀히 같은 수치로 취급하지 않는다.


[출처와 데이터]
- https://www.mathworks.com/help/phased/ref/gccphat.html
- https://arxiv.org/html/2403.09455v1, §III-A, Eqs. 3–6
- public/diagrams/localization-tdoa-locus.source.json
- scripts/visuals/localization-geometry.py
직접 계산한 설명용 도해다. 논문 실험 결과나 실측 데이터로 제시하지 않는다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "01 · 신호에서 좌표를 찾는 과정"
causalStage: "main"
---

# 후보 좌표가 예측한 지연에서 상관값을 읽는다

::body::
<PaperFigure src="/diagrams/localization-srp-candidate.svg" alt="두 후보 위치에서 마이크까지의 거리를 계산하고, 거리 차이를 음속으로 나눈 예상 지연을 같은 GCC-PHAT 곡선에 대입한다. 실제 생성 위치 A의 점수는 약1이고 다른 후보 B의 점수는 약-0.01이다.">
<template #caption>
<div>좌표 <MathInline tex="p" /> → 거리 차이 → 기대 지연 <MathInline tex="\tau_{21}(p)" /> → 쌍 응답 <MathInline tex="R_{21}(p)" /></div>
</template>
</PaperFigure>

::takeaway::
SRP는 **후보 위치의 예상 지연**이 **관측 상관과 얼마나 맞는지** 평가한다.

::source::
Neural-SRP, 2024, §III-A, Eq. 3–6 · 동일 무반향 합성 신호의 GCC-PHAT · 높이 고정

<!--
[현재 S09 · 본문]
01 · 신호에서 좌표를 찾는 과정

[설명의 중심]
후보 좌표에서 두 마이크까지 거리를 계산하고, 예상 지연의 GCC-PHAT 값을 읽는다.

[연결]
다음에 확인할 질문: 마이크를 하나 더 놓아 세 쌍의 후보 점수를 합산하고 전체 공간 응답이 최대인 좌표를 선택한다.

[상세 근거와 해석 범위]
[BRIDGE: srp-candidate 발표 노트]
[핵심 질문]
지연 축의 곡선을 어떻게 공간 좌표의 점수로 바꾸는가? SRP의 핵심 한 연산을 후보 A와 B 두 개로 설명한다.

[설명 순서]
왼쪽에서 후보 pA=(0.6,1.6)를 선택한다. 알려진 두 마이크 좌표로 계산한 거리는 d1=2.030394m, d2=1.600781m다. 거리 차이를 음속으로 나누면 tau21(pA)=-1.252516ms다. 오른쪽의 GCC-PHAT 곡선에서 이 지연의 값을 읽으면 R21(pA)=0.999622...로 약 1이다.

두 번째 후보 pB=(-0.4,1.3)는 d1=1.323820m, d2=1.671077m를 예측한다. tau21(pB)=+1.012412ms로 A와 다른 지연이다. 동일한 GCC 곡선에서 읽은 값은 약 -0.01이다. A는 설명용 합성 신호를 생성한 위치여서 이 이상적인 예시에서 높은 점수가 나온다. B의 결과는 다른 관측을 사용한 비교가 아니라 같은 관측과 같은 곡선에서 읽는 위치만 바꾼 것이다.

[수식]
R21(p)=C21^PHAT(tau21(p)),
tau21(p)=(||p-M2||-||p-M1||)/c.
C21^PHAT(tau)=IFFT[X2(f) X1*(f)/|X2(f) X1*(f)|]의 tau 지연 값으로 정의하여 tau21=t2-t1 부호와 맞춘다. PHAT 값은 확률이 아니므로 음의 측엽도 가능하다. 이 설명에서는 대역에 포함된 주파수 빈 수로 IFFT를 정규화하여 완전히 맞는 이상적 지연의 응답이 1이 되도록 했다.

[계산 조건]
앞 GCC 그림과 뒤 SRP 지도는 같은 배열, 같은 음원, 같은 합성 신호를 재사용한다. fs=16kHz, N=8192(512ms), seed=20260911. 80ms 중심, 표준편차 6ms인 Gaussian envelope의 광대역 잡음을 만들고 100–4000Hz 대역을 남겼다. 각 채널은 Xi=S exp(-j2πf di/c)의 분수 지연으로 계산했다. 이는 512ms 주기의 spectral shift이며 신호 burst는 경계에서 충분히 떨어져 있다. 반사, 다중 음원, 마이크 오차, 센서 잡음은 추가하지 않은 이상적인 직접 경로 예시다.

각 쌍의 교차 스펙트럼을 실제로 계산하고 대역 안에서 PHAT 정규화한 뒤 16배 보간 IFFT를 수행했다. 기대 지연의 점수는 그 곡선을 선형 보간해서 읽었다. 16배 보간은 시간 축을 촘촘히 평가하는 계산이며 원 신호에 새 정보를 추가하는 조작이 아니다. 정확한 숫자와 배열은 source.json 및 localization-simulation.npz에 있다. 본문 숫자는 이해를 돕는 반올림값이며 보고된 논문 점수가 아니다.


[출처]
- https://arxiv.org/html/2403.09455v1, §III-A, Eqs. 3–6
- https://www.mathworks.com/help/phased/ref/gccphat.html
- public/diagrams/localization-srp-candidate.source.json
- public/diagrams/localization-simulation.npz
-->

---
layout: "seminar"
variant: "figure"
chapter: "01 · 신호에서 좌표를 찾는 과정"
causalStage: "main"
---

# 쌍별 응답을 합하고 가장 높은 좌표를 고른다

::body::
<PaperFigure src="/diagrams/localization-srp-sum.svg" alt="동일한 좌표 격자에서 실제 합성 GCC-PHAT로 계산한 R21,R31,R32 쌍별 응답과 그 합을 표시한다. 추가 마이크 M3로 서로 다른 쌍의 높은 응답이 만나는 위치가 강조되고 격자 최대값은 생성 위치0.60,1.60m다. 모든 지도는-1부터3까지 같은 색 척도다.">
<template #caption>
<div>추가 마이크 <MathInline tex="M_3=(-0.5,\,2.8)\,\mathrm m" /> · <MathInline tex="\mathcal P" />: 같은 높이의 1 cm 후보 격자</div>
</template>
</PaperFigure>

::takeaway::
**GCC-PHAT → 후보별 점수 → 쌍 합산 → 최대 좌표**, 이것이 SRP의 계산 흐름이다.

::source::
Neural-SRP, 2024, §III-A, Eq. 3–6 · 직접 경로 합성 계산 · 지도 간 동일 좌표·색 척도

<!--
[현재 S10 · 본문]
01 · 신호에서 좌표를 찾는 과정

[설명의 중심]
마이크를 하나 더 놓아 세 쌍의 후보 점수를 합산하고 전체 공간 응답이 최대인 좌표를 선택한다.

[연결]
다음에 확인할 질문: Neural-SRP: 쌍별 공간 응답을 학습한다

[상세 근거와 해석 범위]
[BRIDGE: srp-sum 발표 노트]
[핵심 질문]
앞에서 정의한 한 후보의 점수를 전체 좌표 격자로 확장하면 무엇이 보이며, 여러 마이크 쌍은 어떻게 결합되는가?

[설명 순서]
첫 지도는 이전 두 마이크 M1=(-0.65,0), M2=(0.65,0)의 관측에서 얻은 R21(p)다. 후보마다 tau21(p)를 계산해 같은 GCC-PHAT 곡선에서 값을 읽으면 지연이 같은 쌍곡선 능선이 나타난다. 이는 장식용으로 손으로 그린 능선이 아니다.

여기서 처음으로 x축 밖에 있는 M3=(-0.5,2.8)를 추가한다. 같은 음원 ps=(0.6,1.6)에서 M3까지의 거리는 1.627882m다. 두 번째 쌍 M3–M1의 지연은 tau31=-1.173504ms, 세 번째 쌍 M3–M2의 지연은 tau32=+0.079012ms다. 세 번째 지도는 두 마이크가 듣는 시점이 거의 같아 거의 등거리인 위치 주변이 높은 응답을 갖는다.

좌표 격자 P는 x∈[-1.2,1.4]m, y∈[-0.2,3.0]m에서 1cm 간격의 261×321점이다. 세 지도 모두 같은 좌표, 같은 실제 합성 신호, 같은 GCC 계산법을 사용했다. pair maps R21,R31,R32를 픽셀별로 그대로 더하여 R(p)=R21(p)+R31(p)+R32(p)를 만들고, P 안에서 argmax를 고른다. 결과는 (0.60,1.60)m다. 합성에 사용한 좌표가 격자에 정확히 포함돼 있어 이 이상적인 예시에서 일치한다. 이 숫자는 논문 성능이나 실측 오차가 아니다.

[색 척도와 수학적 범위]
네 지도 모두 -1부터3까지 동일한 절대 응답 색 척도를 사용했다. 개별 지도를 따로 정규화하지 않아, 한 쌍의 높은 응답보다 여러 쌍이 동시에 지지하는 합산점이 더 진해진다. PHAT 응답의 음의 측엽도 제거하지 않았다. 양의 주엽은 파랑, 음의 값은 약한 갈색으로 표시했다. 응답은 확률밀도가 아니며 합을 확률로 읽지 않는다.

세 쌍의 TDoA가 세 개의 독립 정보라는 뜻은 아니다. 이상적인 단일 음원에서는 tau31=tau32+tau21이므로 독립적인 차이는 두 개다. 비공선 마이크 세 개와 제한한 높이 고정 2D 격자에서 이 장면의 모호성을 해소한 예시이며 일반적인 3D 위치의 유일성을 보장하지 않는다. 잡음·반사·다중 음원에서는 쌍별 최대점이 서로 맞지 않거나 합산에 잘못된 큰 값이 남을 수 있다.


[출처와 재현]
- https://arxiv.org/html/2403.09455v1, §III-A, Eqs. 3–6
- https://www.mathworks.com/help/phased/ref/gccphat.html
- public/diagrams/localization-srp-sum.source.json
- public/diagrams/localization-spatial-maps.npz
- public/diagrams/localization-simulation.npz
- scripts/visuals/localization-geometry.py
-->

---
layout: "seminar"
variant: "figure"
chapter: "01 · 신호에서 좌표를 찾는 과정"
causalStage: "main"
---

# Neural-SRP: 쌍별 공간 응답을 학습한다

::body::
<PaperFigure src="/diagrams/causal-srp-neural.svg" alt="같은 채널쌍 관측에서 SRP는 기대 지연의 상관값으로 위치 응답을 계산하고 Neural-SRP는 같은 TDoA 능선을 목표로 쌍 응답을 학습한다. 두 방법 모두 모든 쌍의 응답을 합산하고 최대 위치를 선택한다.">
<template #caption>
<div>고정 계산 <MathInline tex="R_{ij}(p)=C_{ij}^{\rm PHAT}(\tau_{ij}(p))" /> · 학습 목표 <MathInline tex="Y_{ij}(p)=\exp\!\left[-\left(\frac{|\tau_{ij}(p)-\tau_{ij}(p_s)|}{\sigma_\tau}\right)^2\right]" /></div>
</template>
</PaperFigure>

::takeaway::
**쌍의 공간 응답을 학습**하고, **쌍 합산과 최대점 선택**은 유지한다.

::source::
Neural-SRP, 2024, §III–IV, Eq. 4–10 · 높이를 고정한 2D 위치 격자 · 지도는 설명용 계산

<!--
[현재 S11 · 본문]
01 · 신호에서 좌표를 찾는 과정

[설명의 중심]
Neural-SRP는 직접 좌표 회귀가 아니라 쌍별 위치 응답을 학습하고 합산 구조를 유지한다.

[연결]
다음에 확인할 질문: 학습한 쌍별 응답을 합치면 위치 피크가 달라진다

[상세 근거와 해석 범위]
[BRIDGE: srp-neural 발표 노트]
[핵심 질문]
고정 수식의 어느 연산을 학습으로 바꾸었는가? 앞의 SRP 설명과 같은 입력 관측·쌍 응답·합산·최대점이라는 자리를 유지해 차이를 읽는다.

[설명 순서]
SRP-PHAT에서는 알려진 배열과 후보 위치로 기대 TDoA를 계산하고, 그 지연의 PHAT 상관값을 읽는다. Neural-SRP는 채널쌍의 STFT 위상과 두 마이크의 절대좌표, 방 크기를 입력으로 받아 그 쌍의 전체 공간 응답을 예측한다. 원문 CNN-GRU 뒤의 late fusion에 메타데이터가 들어가며 출력은 25×25 위치 격자다. 후보 좌표는 타깃을 만드는 데 쓰이고 추론 입력은 아니다. 각 쌍에서 같은 가중치의 네트워크를 사용하고 모든 i<j 응답을 합하여 최대 위치를 선택한다.

[수식과 기하]
여기서 tau_ij(p)=(||p_i-p||-||p_j-p||)/c. 관측 상관의 부호와 일관되게 사용한다. 도입의 tau=t2−t1는 여기 표기의 tau_21에 해당한다. 여기서는 원문 C_ij와 대응하는 tau_ij=t_i−t_j를 사용하므로 같은 물리 관계에 첨자 순서가 반대임을 먼저 짚는다. 정답 위치 p_s와 지연이 같은 위치는 모두 큰 타깃 응답을 갖는다. 그래서 한 쌍의 목표는 점 중심 Gaussian이 아니라 같은 TDoA의 쌍곡선 능선이다. sigma_tau는 지연 단위의 폭을 명시하려고 발표에서 붙인 이름이다. 원문의 손실은 L1이며 마지막 응답 층에는 활성화가 없으므로 확률 지도로 부르지 않는다. 단일 쌍의 지연으로 3D azimuth/elevation/distance를 유일하게 구할 수 없다. 본 그림은 높이를 고정한 2D 단면이다.

[그림 조건]
지도는 설명을 위해 거리 차이로 생성한 25×25 격자다. 첫 쌍 마이크 (-0.65,0),(0.65,0), 추가 마이크 (-0.5,2.8), 설명용 음원 (0.6,1.6), 거리 차이 폭 0.11 m를 사용했다. 정량 실험이나 실제 학습망 출력을 재현하지 않았다. 위·아래에 같은 설명용 지도를 사용하여 학습 뒤의 성능 개선을 그림 자체로 주장하지 않는다. 아래의 변화는 쌍 응답 계산 방법이다.

[다른 학습 위치와 구별]
IPDnet은 복소 STFT에서 음원 트랙별 직접 경로 IPD를 학습하고, 알려진 기하의 IPD 템플릿과 내적하여 방향을 판독한다. 가변 배열 모델은 기준쌍 M−1개 사이의 중간 특징 평균·방송과 후단 템플릿 점수 평균을 사용한다. Neural-SRP의 모든 쌍 지도 직접 학습과 다른 위치에 학습을 넣는다.


[Sources]
- https://arxiv.org/html/2403.09455v1
- https://arxiv.org/html/2405.07021v1
- https://proceedings.iclr.cc/paper_files/paper/2026/file/ee860a9fa65a55a335754c557a5211de-Paper-Conference.pdf
-->

---
layout: "seminar"
variant: "figure"
chapter: "01 · 신호에서 좌표를 찾는 과정"
causalStage: "main"
originSlide: 10
---

# 학습한 쌍별 응답을 합치면 위치 피크가 달라진다

::body::
<PaperFigure src="/research/neural-srp-response-pair.svg" alt="Neural-SRP Fig. 1 왼쪽 NeuralSRP+ 오른쪽 SRP의 위치 응답" caption="왼쪽: NeuralSRP+ · 오른쪽: SRP. 원문 패널 재배치, 공유 x축은 두 패널 아래에 표시." />

::takeaway::
**쌍별 공간 응답을 학습하고 합산하는 설계**가 위치 피크를 바꾼 정성 예시다.

::source::
Grinstein et al., Neural-SRP, arXiv:2403.09455v1, Fig. 1. CC BY 4.0.

<!--
[현재 S12 · 본문]
01 · 신호에서 좌표를 찾는 과정

[설명의 중심]
그림은 학습 응답이 어떤 형태의 변화를 만들 수 있는지 보여 주는 정성 예시다.

[연결]
다음에 확인할 질문: 학습한 응답의 효과는 실녹음 적응 조건에서 확인한다

[상세 근거와 해석 범위]
[S12 발표 노트]
[설명 순서]
“같은 녹음에서 두 방법이 만든 공간 응답을 비교하겠습니다. 실제 녹음에 적응한 NeuralSRP+의 예시라는 조건을 먼저 확인하고, 음원 근처와 다른 영역의 응답을 살펴보겠습니다.”

[경계·원문의 추가 자료]
한 그림으로 전체 성능이나 무적응 실환경 전이를 입증하지 않는다. 적응 전후 모든 변형의 정량 비교는 별도 근거를 확보해 원문의 추가 자료에 둔다.


마이크 위치와 음원 정답 위치를 먼저 짚고 두 응답의 같은 공간을 비교한다. Neural-SRP는 쌍별 STFT 위상, 마이크 절대좌표, 방 크기로 위치 격자의 응답을 학습하고 쌍의 응답을 합산한다. 후보 위치 좌표는 학습 정답 구성에만 쓴다. 한 시각화가 정량 성능 또는 무적응 실환경 전이를 입증하지 않는다.
[Sources]
- https://arxiv.org/html/2403.09455v1
-->

---
layout: "seminar"
variant: "result"
chapter: "01 · 신호에서 좌표를 찾는 과정"
causalStage: "main"
originSlide: 11
---

# 학습한 응답의 효과는 실녹음 적응 조건에서 확인한다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">Recorded 4 · 한 방의 정지 단일 음성</p>
<PaperFigure src="/diagrams/result-11.svg" alt="평균 위치 오차 (m) ↓ 원문 수치 비교 그래프. SRP: 1.19; NeuralSRP+: 0.77" />
<p class="seminar-chart-note">실녹음 250개로 추가 학습 · 시험 2,500개 · <MathInline tex="T_{60}=800\,\mathrm{ms}" /></p>
</div>

::takeaway::
**250개 실녹음으로 추가 학습한 조건**에서 SRP보다 오차가 작았다.

::source::
Neural-SRP, arXiv:2403.09455v1, Table I. 원문 수치의 그래프 재구성.

<!--
[현재 S13 · 본문]
01 · 신호에서 좌표를 찾는 과정

[설명의 중심]
NeuralSRP+의 적응량과 시험 조건을 붙여, 학습 응답의 결과를 확인한다.

[연결]
다음에 확인할 질문: 좌표 다음에 무엇을 전달해야 하는가?

[상세 근거와 해석 범위]
[S13 발표 노트]
[설명 순서]
“쌍별 위상과 좌표, 방 크기로 학습한 응답을 합산하는 방법의 결과입니다. 이 조건에서는 오차가 줄었지만 NeuralSRP+는 실제 녹음으로 적응했으므로, 처음 만난 환경에서 무적응으로 얻은 성과라고 읽으면 안 됩니다.”

[경계·원문의 추가 자료]
Fig. 3 전체 구조와 Recorded 6 결과는 원문의 추가 자료이다. 후보 좌표는 학습 목표 구성에 쓰며 추론 입력이 아니라는 주석을 유지한다.


입력 길이는 0.5초. 네 마이크 조건의 위치 오차이며 각도 오차가 아니다. 후보 좌표는 추론 입력이 아니다. Recorded 6은 본문 비교에서 제외한다. 원문 서술의 상대 개선율은 표의 통상적 감소율과 달라 사용하지 않았다.
[Sources]
- https://arxiv.org/html/2403.09455v1

[시각화 전 표의 수치·조건 보존]
Recorded 4 · 한 방의 정지 단일 음성방법 | 평균 위치 오차 (m) ↓ | 
SRP | 1.19 | 
NeuralSRP+ | 0.77 | 

[조건]
평가 장면$T_{60}=800\,\mathrm{ms}$인 한 방 / 시험 녹음 2,500개

적응 범위합성 학습 뒤 250개 실녹음으로 추가 학습
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "01 · 신호에서 좌표를 찾는 과정"
causalStage: "main"
---

# 좌표 다음에 무엇을 전달해야 하는가?

::body::
<PaperFigure src="/diagrams/causal-readout-to-encoder.svg" alt="같은 공간 관측을 위치 좌표 하나로 전달하는 경우와 중간 표현 H를 보존하여 사건·위치·시간 관계 판독기에 전달하는 경우를 비교한다." caption="표현에 남은 정보는 인코더를 고정한 판독과 전체 미세조정을 구별해 확인" />

::takeaway::
LLM에 답변을 맡기려면 **사건·공간·시간을 담을 표현**도 필요하다.

::source::
발표자 연결 도해 · MC-SimCLR, CCSR, SFD, GRAM의 학습·평가 프로토콜에 근거

<!--
[현재 S14 · 본문]
01 · 신호에서 좌표를 찾는 과정

[설명의 중심]
SRP와 Neural-SRP의 위치 출력만으로는 어떤 소리가 언제 났는지 알 수 없다. 사건·공간·시간을 함께 담을 표현이 LLM 연결에 필요하다.

[연결]
다음에 확인할 질문: 공간 QA에서 기존 Audio-LM 확장과 동적 장면으로

[상세 근거와 해석 범위]
[BRIDGE: readout-to-encoder 발표 노트]
[핵심 질문]
위치 추정의 출력에서 재사용 가능한 표현의 평가로 왜 넘어가는가?

[설명 순서]
앞에서 SRP와 Neural-SRP로 후보 공간의 최대 응답 위치를 골랐다. 그러나 그 좌표만으로는 어떤 소리였는지, 언제 났는지 답할 수 없다. 여기부터는 위치 추정기의 출력을 넘어 여러 질문에 필요한 정보를 표현에 남기고 LLM에 전달하는 설계 문제를 다룬다. Neural-SRP 논문이 자신의 내부 특징의 범용성이나 LLM 연결을 입증했다는 뜻은 아니다. 연구사 지도와 두 입력 경로를 먼저 본 뒤 인코더 E, 어댑터 P, LLM 적응의 전체 구조를 살펴본다.
위쪽은 다음 단계에 위치 좌표만 전달하는 인터페이스다. 좌표는 원래 목적에 맞는 출력이지만 사건 종류나 방의 전달 특성까지 충분히 전달하는 형식은 아니다. 이는 모든 위치 추정기의 내부 특징에서 의미와 방 정보가 완전히 사라졌다고 주장하는 그림이 아니다. 아래쪽은 중간 표현 H=E(X)를 보존하고 서로 다른 판독기가 사건, 위치, 시간 관계를 읽게 하는 평가 설계다. 색깔이나 개별 h 성분을 특정 의미에 일대일로 대응시키지 않았다. 세 head는 질문의 예시이며 모든 원문이 세 과제를 모두 수행한다는 뜻도 아니다.

[학습에서 쓰는 특징과 최종 제품의 구분]
IPDnet은 예측한 DP-IPD를 후단 기하 템플릿 계산에 사용한다. SFD는 noisy/reverberant STFT에서 clean 비잔향 바이노럴 신호의 고정 공간 특징을 예측하도록 학습한다. 이후 특징 predictor를 제거하고 인코더를 DOA 모델의 초기값으로 사용한다. SFD는 별도 학습한 teacher network를 사용하지 않는다. 같은 공간 특징 예측이라도 그 특징을 직접 쓰는 것과 그 과제로 인코더를 훈련하는 것은 사용 목적이 다르다.

[검증 조건]
MC-SimCLR의 LP는 인코더를 고정하고 사건·방향 선형 head를 각각 학습한다. GRAM은 고정 표현에 얕은 downstream 판독기를 학습하여 여러 과제를 평가한다. CCSR의 LP와 전체 FT는 다른 질문이다. SFD의 저라벨 DOA 결과는 인코더를 갱신한 FT이며 frozen 범용 표현의 증거가 아니다. 방 특성을 읽으려는 경우에는 잔향도 목표 정보다. DOA에 방해가 되는 변화라고 모든 표현에서 무조건 지워야 한다고 말하지 않는다.


[Sources]
- https://arxiv.org/html/2309.15938v1
- https://arxiv.org/html/2312.00476v2
- https://arxiv.org/html/2508.20914v1
- https://arxiv.org/html/2506.00934v5
- https://arxiv.org/html/2405.07021v1
-->

---
layout: "seminar"
variant: "figure"
chapter: "02 · 공간 정보를 언어 모델에 연결하는 두 길"
causalStage: "main"
---

# 공간 QA에서 기존 Audio-LM 확장과 동적 장면으로

::body::
<PaperFigure src="/diagrams/history-map.svg" alt="최초 공개 연대와 개정판을 구분한 지도로, 초기 BAT에서 표현 개선·구조화 언어 전달·기존 Audio-LM 확장·시간 표현으로 연구 문제가 갈라지는 과정을 먼저 제시한다." />

::takeaway::
**공간 QA 연결 → 표현·전달 방식의 분화 → 기존 Audio-LM 확장 → 시간 구조**

::source::
BAT v1 §4 · DSpAST·Motion·OWL·Sci-Phi의 최초 공개본 · 2026 채택 버전은 노트 참조.

<!--
[현재 S15 · 본문]
02 · 공간 정보를 언어 모델에 연결하는 두 길

[설명의 중심]
최초 공개 연대와 개정판을 구분한 지도로, 초기 BAT에서 표현 개선·구조화 언어 전달·기존 Audio-LM 확장·시간 표현으로 연구 문제가 갈라지는 과정을 먼저 제시한다.

[연결]
다음에 확인할 질문: 언어로 기술해 넘길까, 오디오 표현을 직접 연결할까?

[상세 근거와 해석 범위]
[Sources]
- https://arxiv.org/html/2402.01591v1
- https://arxiv.org/abs/2509.13927
- https://arxiv.org/abs/2509.14666
- https://arxiv.org/abs/2509.26140
- https://arxiv.org/abs/2510.05542
- https://arxiv.org/abs/2601.02954
- https://arxiv.org/abs/2601.21124
- https://arxiv.org/abs/2602.16334
- https://arxiv.org/abs/2606.10738
- https://arxiv.org/abs/2606.14141

[그림]
이 그림은 원문 Methods에 근거한 교육용 재구성으로 실제 activation이나 성능 측정 그림이 아니다. 최초 공개 연대와 채택 버전은 plans/MC_AUDIO_LM_HISTORY.md에 구분하여 기록했다. 화살표는 그림 내부의 데이터 흐름이며 논문 간 성능 상승을 뜻하지 않는다.

[연구사와 발표 노트]
BAT는 2024-02-02 최초 공개됐으며 현재 결과는 v4를 사용한다. 초기 v1부터 Spatial-AST→projection→LLaMA2라는 공간 QA 구조가 있었다. 2025-09-17 DSpAST, 09-18 Motion, 09-30 OWL은 같은 달의 서로 다른 접근이다. DSpAST는 과제별 단서 표현, OWL은 기하 감독, Motion은 JSON을 통한 별도 reasoning LM 연결을 다룬다.
Sci-Phi는 2025-10-07 처음 공개됐으며 2026 저널 표기로 시작 연도를 바꾸지 않는다. 이후 PhaseCoder, TWNM, Spatial-Omni는 기존 의미·음성 경로와 공간 경로를 결합하지만 하나의 모델을 순차 개량한 직접 계보는 아니다. TWNM은 최초 공개 2026-01-06, 채택 v3는 05-10이다. v1의 binaural/GRPO와 v3의 FOA/SAPO를 구분한다. PhaseCoder 최초 01-28, 채택 v2 08-05; Spatial-Omni 최초 06-09, 채택 v2 09-07이다.
동적 장면 축에서 Dynamic QA 2026-02-18과 ST-AudioLM 06-12는 BAT encoder/backbone을 각각 확장한다고 원문이 명시한다. Motion→Dynamic QA→ST-AudioLM을 하나의 구현 계보로 연결하지 않는다. ELSA·SALM·CoSTALA는 audio–text alignment와 retrieval이라는 병행 과제이며 생성 LM 연결 모델로 분류하지 않는다. Dual-BEATs 2026-07-09는 전용 공간 encoder 없이 좌우 BEATs의 표현을 쓰는 제한된 진단 대안이며 세부 근거는 부록에 남겼다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "02 · 공간 정보를 언어 모델에 연결하는 두 길"
causalStage: "main"
---

# 언어로 기술해 넘길까, 오디오 표현을 직접 연결할까?

::body::
<PaperFigure src="/diagrams/history-interfaces.svg" alt="Motion은 예측 속성을 JSON으로, OWL은 SAGE의 연속 표현을 Q-Former로 전달한다. 입력 인터페이스와 LoRA 가중치 적응을 별도 축으로 구분한다." />

::takeaway::
**LM에 들어가는 정보의 형식**과 **LM 가중치를 학습하는 방식**은 서로 다른 선택이다.

::source::
Motion 2025 v1 §2.2 · OWL v1 §5, App. B.3 · PhaseCoder v2 §4.2, App. K.

<!--
[현재 S16 · 본문]
02 · 공간 정보를 언어 모델에 연결하는 두 길

[설명의 중심]
Motion은 예측 속성을 JSON으로, OWL은 SAGE의 연속 표현을 Q-Former로 전달한다. 입력 인터페이스와 LoRA 가중치 적응을 별도 축으로 구분한다.

[연결]
다음에 확인할 질문: 오디오 인코더 E의 표현 H를 어댑터 P가 연속 토큰 Z로 변환하고, LLM은 LoRA 등의 적응으로 질문과 오디오 입력을 함께 처리한다. 이후 논문을 이 구조의 선택으로 읽는다.

[상세 근거와 해석 범위]
[Sources]
- https://arxiv.org/html/2509.14666v1
- https://arxiv.org/html/2509.26140v1
- https://arxiv.org/html/2601.21124v2

[그림]
이 그림은 원문 Methods에 근거한 교육용 재구성으로 실제 activation이나 성능 측정 그림이 아니다. 최초 공개 연대와 채택 버전은 plans/MC_AUDIO_LM_HISTORY.md에 구분하여 기록했다. 화살표는 그림 내부의 데이터 흐름이며 논문 간 성능 상승을 뜻하지 않는다.

[연구사와 발표 노트]
위 경로는 지각 모델이 Event, DoA, SourceDistance, TimeFrames를 예측해 JSON으로 직렬화하고, 기존 텍스트 토큰을 통해 추론 LM에 전달한다. 지각 모델 DSAST는 학습한다. training-free는 추가 reasoning LM과의 결합을 뜻하며 모든 모듈이 학습 없이 작동한다는 의미가 아니다. AGM은 사전학습된 고정 모듈이다.
아래 OWL은 SAGE의 연속 오디오 특징을 Q-Former에서 query tokens로 만들고 LLaMA2에 연결한다. QA에서는 SAGE를 고정하고 Q-Former와 LoRA를 학습한다. 기하 depth/RIR은 encoder 사전학습용이며 추론 입력은 binaural audio다. CoT는 답변 형식과 학습 curriculum이고 외부 지각 결과를 JSON으로 넘기는 연결부가 아니다. OWL에 언어를 사용한 감독이 있다는 사실과 입력이 언어로 직렬화된다는 주장을 구분한다.
연속 오디오 임베딩 Z는 기존 LM 입력 폭에 맞춰진다. 입력 표현의 종류와 시퀀스 길이를 늘릴 수 있지만 어휘 수나 hidden width의 증가를 요구하지 않는다. LM을 고정하고 P만 연결하는 방법과 LM도 적응하는 방법은 이 입력 분류와 직교한다. 또한 PhaseCoder v2에는 수치 좌표 배열을 텍스트로 넘기는 zero-shot Gemma 기준선과 연속 spatial soft token+LoRA 학습 방법이 함께 있다. 이를 같은 학습량의 순수 인터페이스 통제로 해석하지 않는다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "02 · 공간 정보를 언어 모델에 연결하는 두 길"
causalStage: "main"
---

# 오디오 표현은 어떻게 LLM의 입력이 되는가

::body::
<PaperFigure src="/diagrams/causal-audio-llm-contract.svg" alt="다채널 파형 X가 인코더 E를 거쳐 T×de 표현 H가 되고 어댑터 P에서 K×dLLM 연속 오디오 토큰 Z가 된다. 질문 임베딩과 함께 고정하거나 적응한 LLM에 입력되어 답변을 생성한다." />

::takeaway::
**연속 오디오 입력의 연결**과 **LM 가중치의 적응**은 별개다. LoRA는 후자의 한 방법이다.

::source::
Spatial-Omni v2 §3 · PhaseCoder v2 §3.3 기반 교육용 재구성. 모델별 연결 순서는 다름.

<!--
[현재 S17 · 본문]
02 · 공간 정보를 언어 모델에 연결하는 두 길

[설명의 중심]
오디오 인코더 E의 표현 H를 어댑터 P가 연속 토큰 Z로 변환하고, LLM은 LoRA 등의 적응으로 질문과 오디오 입력을 함께 처리한다. 이후 논문을 이 구조의 선택으로 읽는다.

[연결]
다음에 확인할 질문: LoRA는 추가 연속 audio token을 읽는 LLM의 선형층을 저랭크로 적응하는 방식이다. token vocabulary 확장 자체가 아니다.

[상세 근거와 해석 범위]
[B-AUDIO-LLM-CONTRACT]
[Sources]
- https://arxiv.org/html/2606.10738v2
- https://arxiv.org/html/2601.21124v2
[그림]
public/diagrams/causal-audio-llm-contract.svg. scripts/visuals/causal-llm.py로 제작한 설명용 그림이다. 파형·격자·토큰 값은 실제 모델 출력이 아니다. 수식은 matplotlib mathtext 경로로 렌더했다.
[발표 노트]
X는 관측한 공간 오디오이다. E가 만드는 H는 인코더의 잠재 표현이다. T는 잠재 표현의 길이로, 모델에 따라 패치나 집계 토큰을 포함하므로 언제나 순수 시간 길이라는 뜻은 아니다. P는 이 표현을 LLM 입력 폭 d_LLM에 맞추고 필요하면 길이 K를 줄이거나 여러 스트림을 합친다. Q-Former, MLP, temporal shuffle와 융합 모듈이 모두 이 자리에 올 수 있다. 이후 Z는 질문 텍스트의 임베딩과 함께 디코더에 입력된다. 그림은 공통 분석 관점이며 실제 prepend/interleave와 경계 표지는 모델별로 다르다.
[정의]
LoRA는 연속 오디오 입력을 처리하는 LLM 선형층을 저랭크로 적응하는 방법이다. 이 발표의 구조도는 인코더·어댑터·LLM 적응을 구별하기 위한 공통 틀이며, 모든 Audio-LLM이 LoRA를 필수로 사용한다는 뜻은 아니다. 상세 수식과 학습 범위는 후반에서 확대한다.
연속 오디오 토큰이 기존 임베딩 차원의 입력 시퀀스에 추가된다. 새로운 어휘 항목을 추가하거나 LLM hidden width를 확대하는 것과 구분한다. PhaseCoder는 공간 soft token과 경계 표지를 구분하고, 경계 표지에 기존 미사용 token ID를 사용한다. “어댑터로 확장된 토큰 공간”이라는 모호한 표현 대신 “연속 오디오 임베딩으로 증강한 입력 시퀀스”라고 설명한다.
[해석 범위]
E가 관측에서 소실한 정보를 P나 LLM이 보장하여 복원한다는 의미가 아니다. LLM의 사전확률 추론과 오디오 정보의 보존을 구분한다. 이 구조는 연속 오디오 표현을 언어 디코더에 직접 연결하는 계열의 분석 틀이며 좌표 head, retrieval, 속성 JSON을 텍스트로 전달하는 시스템까지 필수 구조로 일반화하지 않는다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "02 · 공간 정보를 언어 모델에 연결하는 두 길"
causalStage: "main"
---

# LoRA는 LLM의 입력 처리 방식을 조정한다

::body::
<PaperFigure src="/diagrams/causal-lora-reading.svg" alt="오디오와 질문의 임베딩 입력이 LLM 내부의 고정 선형층 W0 경로와 저랭크 A,B 학습 경로를 지난다. W=W0+(alpha/r)BA로 두 경로를 합하고 후속 층과 출력 헤드를 통해 기존 어휘에서 답변을 생성한다." />

::takeaway::
**P는 연속 오디오 토큰을 만들고, LoRA는 이를 처리하는 LLM 가중치를 적응한다.**

::source::
LoRA v2 §4.1 · BAT v4 §4.2와 저자 공개 구현은 적응 방식이 다름. 교육용 재구성.

<!--
[현재 S18 · 본문]
02 · 공간 정보를 언어 모델에 연결하는 두 길

[설명의 중심]
LoRA는 추가 연속 audio token을 읽는 LLM의 선형층을 저랭크로 적응하는 방식이다. token vocabulary 확장 자체가 아니다.

[연결]
다음에 확인할 질문: 같은 사건의 위치·순서·환경을 바꾸며 보존할 정보와 무시할 변화를 구별한다.

[상세 근거와 해석 범위]
[B-LORA-READING]
[Sources]
- https://arxiv.org/abs/2106.09685v2
- https://arxiv.org/html/2402.01591v4
- https://github.com/X-LANCE/SLAM-LLM/tree/main/examples/seld_spatialsoundqa
- https://github.com/X-LANCE/SLAM-LLM/blob/main/examples/seld_spatialsoundqa/scripts/finetune_spatial-ast_qformer_llama_2_7b.sh
- https://arxiv.org/abs/2305.11834
[그림]
public/diagrams/causal-lora-reading.svg. LLM 내부 선형층 하나를 확대한 설명용 도식이다. 실제 모델의 activations나 어휘 확률을 측정한 그림이 아니다. 아래 학습 경로에는 alpha/r scaling을 표시했으며 후속 Transformer 층과 출력 헤드는 축약했다.
[발표 노트]
P가 만든 Z와 질문 임베딩은 이미 LLM과 같은 입력 폭을 가진 연속 벡터이다. LoRA는 이 입력의 어휘를 늘리는 모듈이 아니다. W0가 기존 선형층이고 W=W0+(alpha/r)BA로 업데이트를 제한한다. W0의 크기가 d_out×d_in이면 A는 r×d_in, B는 d_out×r이다. r은 학습 업데이트의 랭크로 토큰 개수나 어휘 수와 구분한다. h는 그림에서 선택한 선형층의 입력 hidden state이며 최초 입력 임베딩과 모든 내부층에서 그대로 같다는 뜻은 아니다.
모델에 따라 attention의 Q/K/V/O 또는 FFN 선형층 등에 LoRA를 적용하므로 “읽기 적응”은 조건을 처리하는 방식의 변화라는 뜻이다. 출력 헤드만 학습한다는 설명은 부정확하다. 생성은 후속 층과 출력 헤드를 통해 기존 어휘에 대한 확률을 얻는다. 별도의 special token 추가나 embedding/head 학습은 독립적인 구현 선택이다.
[논문별 예외]
BAT v4 본문은 LLaMA-Adapter V2의 zero-initialized attention, projection, norm/bias/scale 적응을 설명한다. 반면 저자 BAT 공개 SLAM-LLM 실행 설정은 frozen Spatial-AST+Q-Former+LLM LoRA를 사용한다. 논문 실험과 공개 구현을 같은 세부 구조로 합치지 않는다. LoRA가 필요하다는 일반 명제의 근거로 BAT를 사용하지 않는다.
Pengi 2023은 audio encoder와 mapping network를 학습하고 GPT2 언어 모델을 고정한다. 연속 오디오 입력을 추가하기 위해 LoRA가 반드시 필요한 것은 아니다. 이 일반 오디오 배경 사례가 공간 QA에서 같은 성능을 보장하는 것은 아니다.
[해석 범위]
P와 LoRA를 적응시켜도 E가 관측에서 잃어버린 정보가 보장 복원되는 것은 아니다. 학습 가능한 구조가 있다는 사실, 실제 해당 모듈의 성능 기여, 다른 조건으로 일반화하는 능력은 각각 별도로 검증한다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "02 · 공간 정보를 언어 모델에 연결하는 두 길"
causalStage: "main"
---

# LLM 전에 무엇이 읽혀야 하는가?

::body::
<PaperFigure src="/diagrams/causal-encoder-criteria.svg" alt="같은 알람의 위치 이동, 같은 좌표의 소리 교체, 같은 두 사건의 순서 교환을 각각 인코더 표현 H의 판독으로 연결한다. 기대하는 종류·위치·순서의 변화와 불변을 구분한다." caption="후속 실험 제안. = 는 유지, ↔ 는 조건에 맞는 변화. H는 인코더 표현." />

::takeaway::
같은 소리의 <strong>종류는 유지</strong>하고, 바뀐 <strong>위치와 순서는 읽혀야 한다.</strong>

::source::
SARL v2 · SALM v2 · SelectTSL v1 · CoSTALA v1의 관측 문제를 종합한 제안.

<!--
[현재 S19 · 본문]
02 · 공간 정보를 언어 모델에 연결하는 두 길

[설명의 중심]
같은 사건의 위치·순서·환경을 바꾸며 보존할 정보와 무시할 변화를 구별한다.

[연결]
다음에 확인할 질문: 대조·복원·관측 통계·clean 특징 목표는 서로 다른 정보를 남기려는 학습 선택이다.

[상세 근거와 해석 범위]
[Bridge: encoder-criteria]
[Sources]
- https://arxiv.org/html/2606.05544v2
- https://arxiv.org/html/2507.16724v2
- https://arxiv.org/html/2607.02343v1
- https://arxiv.org/html/2608.24374v1
- https://aclanthology.org/2022.cl-1.7/
[청중 질문]
오디오를 LLM에 넘기기 전에 encoder에서 확인해야 할 정보는 무엇인가?
[발표 노트]
모든 도형과 latent cell은 설명용이며 실험 결과가 아니다. 왼쪽은 같은 dry 알람의 위치만 바꾼다. 알람이라는 의미는 같고 정답 위치는 달라야 한다. 가운데는 위치를 고정하고 알람을 말소리로 교체한다. 좌표는 같고 종류는 달라야 한다. 오른쪽은 사건과 구간을 유지한 채 AB와 BA의 순서를 교환한다. 판독은 명시적인 학습 head/probe이며 LLM의 답변이 아니다.
H_frame, H_mean, adapter 뒤 Z를 구별해 같은 조건의 판독기를 학습한다. 선형 probe에서 못 읽는 것은 모든 정보가 사라졌다는 뜻이 아니다. 위치 민감성 또는 좌표 변환에 대한 equivariance와 의미 label의 invariance를 혼동하지 않는다. 수치나 성공률은 아직 측정하지 않았다.
[확장 통제]
두 소리의 의미–위치 결속은 종류 집합과 위치 집합을 유지하고 대응만 교환하여 측정한다. 종류와 위치를 개별적으로 맞히는 것만으로 공동 대응은 보장되지 않는다. 시간 순서 판독과 동일 종류 두 음원의 지속 identity 추적도 별개다. SelectTSL의 MOTA*는 ID switch를 제외하므로 후자를 증명하지 않는다. CoSTALA의 known segment duration을 자동 사건 경계 검출로 바꾸어 말하지 않는다.
[해석 범위]
그림의 2-mic 배치는 도입 장면의 관찰 좌표계를 회수한다. 두 채널의 단일 지연만으로 3차원 좌표를 유일하게 복원할 수 있다고 주장하지 않는다. 실제 실험에는 과제·배열·방에 맞는 식별 가능성과 train/test source·RIR 분리가 필요하다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "02 · 공간 정보를 언어 모델에 연결하는 두 길"
causalStage: "main"
---

# 학습 과제는 어떤 관계를 남기게 하는가?

::body::
<PaperFigure src="/diagrams/causal-encoder-objectives.svg" alt="같은 녹음의 두 구간을 가깝게 하는 MC-SimCLR, 두 분기의 마스크로 STFT를 복원하는 CCSR, 음향지도와 물리식을 통해 CSM을 복원하는 LAM, 오염 신호에서 clean 공간 특징을 예측하는 SFD의 네 학습 관계" caption="관측 관계와 학습 목표의 도해 · 각 목표의 효과는 후속 판독 실험으로 검증" />

::takeaway::
**위치·사건·방 정보가 남도록 과제를 설계**하고, **무엇을 읽을 수 있는지 따로 검사**한다.

::source::
MC-SimCLR §3 · CCSR Fig. 1 · LAM Eq. 4 · SFD Fig. 1 · 발표자 재구성 도해

<!--
[현재 S20 · 본문]
02 · 공간 정보를 언어 모델에 연결하는 두 길

[설명의 중심]
대조·복원·관측 통계·clean 특징 목표는 서로 다른 정보를 남기려는 학습 선택이다.

[연결]
다음에 확인할 질문: 사건과 방향이 남았는지는 고정 인코더로 읽어 본다

[상세 근거와 해석 범위]
[BRIDGE: encoder-objectives 발표 노트]
[핵심 질문]
정답 위치를 직접 주지 않는 학습이 공간 표현에 어떤 성질을 유도하는가? 네 방법은 각각 다른 관측 관계를 이용하며 한 과제가 다른 과제를 차례로 대체한 순서가 아니다.

[구간 간 일관성]
MC-SimCLR는 같은 다채널 녹음에서 뽑은 두 시간 구간의 표현을 가깝게 학습한다. 정지·비중첩 음원 조건에서 사건과 위치가 일관적이라는 가정이다. 채널 변환은 양쪽 positive crop에 일관되게 적용한다. 모든 채널 순열·회전에 무조건 불변이 되는 것이 목표라고 해석하지 않는다. 효과는 고정 인코더 사건·방향 LP 등 각 프로토콜에서 읽는다.

[채널 간 관계]
CCSR의 위쪽 마스크는 spatial encoder 입력에서 두 채널의 같은 시간 프레임을 함께 가린 것이다. 아래쪽은 spectral encoder의 상보 마스크로, 해당 시간에 한 채널이 보인다. 두 분기를 결합하여 dual-channel 복소 STFT를 출력하되 손실은 한 채널의 가려진 프레임에 적용한다. 검은 구멍이나 완전히 미관측인 새 채널을 생성하는 그림이 아니다. 관측 프레임의 내용과 다른 프레임에서의 전달 관계를 같이 이용한다. CCSR도 잡음·잔향을 다룬다. 복원 성과와 TDOA/T60/C50 판독 성과를 동일시하지 않는다.

[물리적 공간 구조]
LAM의 잠재 비음수 음향지도 x와 알려진 steering matrix A를 이용하여 C_hat=A diag(x) A^H로 CSM을 복원한다. 그림의 행렬은 Hermitian PSD covariance의 크기를 단순 도해한 것이며 측정 수치가 아니다. 실제 학습은 복원 MSE와 희소·평활 제약을 사용한다. 물리적 decoder가 해석 가능성을 유도하지만 역문제의 유일성이나 범용 의미 표현을 보장하지 않는다. 후속 DOA의 LE와 LR를 함께 읽는다. UpLAM의 특정 4→32채널 구성은 임의 배열 무학습 적용의 증거가 아니다.

[오염에 강한 단서]
SFD는 오염된 바이노럴 STFT를 인코더에 넣고, 대응하는 clean 비잔향 신호에서 고정 계산한 GCC·GCC-PHAT·CPSPhase 또는 ILD+IPD를 목표로 학습한다. 이들은 별도 모델 변형이다. 오른쪽의 clean 경로는 학습된 teacher network가 아니라 특징 계산이다. 아래 곡선은 공간 특징의 개념을 나타내며 모든 특징이 직선 위상 곡선이라는 뜻은 아니다. 이 예측 head는 사전학습 후 제거하고 인코더·DOA head를 FT한다. clean 목표 신호가 필요하다.

[다음 연결과 검증]
그림 제목의 '남기게 하는가'는 설계 의도에 관한 질문이다. 표현에 정보가 남았다는 결론은 실제 판독으로 확인해야 한다. frozen LP는 이미 접근 가능한 정보를 검사하고 전체 FT는 유용한 초기화인지를 검사한다. GRAM의 여러 소비자 판독, AT2SELD의 의미 결합 깊이 실험은 여기서 남은 질문을 각각 다른 방식으로 검사한다. 단일 과제 점수가 일반적인 언어 판단 능력을 보장하지 않는다.

[Sources]
- https://arxiv.org/html/2309.15938v1
- https://arxiv.org/html/2312.00476v2
- https://arxiv.org/html/2507.07066v1
- https://arxiv.org/html/2508.20914v1
- https://arxiv.org/html/2506.00934v5
- https://arxiv.org/html/2606.27751v1
-->

---
layout: "seminar"
variant: "result"
chapter: "02 · 공간 정보를 언어 모델에 연결하는 두 길"
causalStage: "main"
originSlide: 19
---

# 사건과 방향이 남았는지는 고정 인코더로 읽어 본다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">LP · 인코더 고정, 사건/방향 선형 판독기 각각 학습</p>
<PaperFigure src="/diagrams/result-19.svg" alt="사건 정확도 (%) ↑, 방위각 오차 (°) ↓ 원문 수치 비교 그래프. 사전학습 없음: 23.6, 83.1; MC-SimCLR · w/o DA: 33.0, 13.2" />
<p class="seminar-chart-note">4채널·정지·비중첩 · noisy split 38.8시간 사전학습 · clean 레이블로 LP</p>
</div>

::takeaway::
인코더를 고정한 판독에서 **사건과 방향 정보의 접근성**을 확인한다.

::source::
MC-SimCLR, arXiv:2309.15938v1, Table 1, LP. 원문 수치의 그래프 재구성.

<!--
[현재 S21 · 본문]
02 · 공간 정보를 언어 모델에 연결하는 두 길

[설명의 중심]
MC-SimCLR의 고정 인코더 LP는 인코더 표현에 접근 가능한 사건·방향 정보의 근거다.

[연결]
다음에 확인할 질문: BAT: 공간 지각의 표현을 질문의 입력으로 바꾼다

[상세 근거와 해석 범위]
[S21 발표 노트]
[설명 순서]
“이번에는 같은 인코더를 고정한 채 사건 종류와 방향을 각각 읽습니다. 추가 증강이 없는 사전학습과 사전학습하지 않은 조건을 비교하면, 두 판독의 개선을 서로 다른 지표로 확인할 수 있습니다.”

[경계·원문의 추가 자료]
증강 조합의 10.1°와 전체 미세조정 결과는 원문의 추가 자료이다. noDA를 최적 모델이라고 부르거나 사건 정확도와 방향 오차를 같은 지표로 합치지 않는다.


FSDnoisy18k를 공간화한 합성 데이터. w/o DA는 추가 데이터 augmentation 없는 대조 사전학습이다. FT 수치는 섞지 않는다. augmentation의 모든 조합이 모든 지표를 단조 개선하지 않는다. 이동·중첩·새 배열로의 재사용은 이 표가 평가하지 않는다.
[Sources]
- https://arxiv.org/html/2309.15938v1

[시각화 전 표의 수치·조건 보존]
LP · 인코더 고정, 사건/방향 선형 판독기 각각 학습사전학습 | 사건 정확도 (%) ↑ | 방위각 오차 (°) ↓ | 
없음 · Random | 23.6 | 83.1 | 
MC-SimCLR · w/o DA | 33.0 | 13.2 | 

[조건]
입력·장면4마이크 원형 배열, 지름 10 cm / 정지·비중첩 사건

사전학습·판독38.8시간 noisy split / clean split 레이블로 LP
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->


---
layout: "seminar"
variant: "figure"
chapter: "03 · 2024–2025: 공간 QA의 출발과 분화"
causalStage: "main"
---

# BAT: 공간 지각의 표현을 질문의 입력으로 바꾼다

::body::
<PaperFigure src="/diagrams/history-bat.svg" alt="일반 Audio-LM의 encoder→projection→LM 연결을 공간 지각에 적용한 초기 대표 모델이다. 공간 좌표를 텍스트로만 직렬화하는 모델이 아니며 기하 인코더 사전학습과 공간 QA 적응을 구별한다." />

::takeaway::
BAT의 전환은 **공간 속성을 배우던 인코더의 표현을 언어 질문에 재사용**한 데 있다.

::source::
Pengi 2023 §3 · BAT 최초 공개 v1 §4–5; 결과 장은 지정 v4 사용.

<!--
[현재 S22 · 본문]
03 · 2024–2025: 공간 QA의 출발과 분화

[설명의 중심]
일반 Audio-LM의 encoder→projection→LM 연결을 공간 지각에 적용한 초기 대표 모델이다. 공간 좌표를 텍스트로만 직렬화하는 모델이 아니며 기하 인코더 사전학습과 공간 QA 적응을 구별한다.

[연결]
다음에 확인할 질문: BAT 2024: 공간 입력은 관계 질문에 기여했는가?

[상세 근거와 해석 범위]
[Sources]
- https://arxiv.org/abs/2305.11834
- https://arxiv.org/html/2402.01591v1
- https://arxiv.org/html/2402.01591v4

[그림]
이 그림은 원문 Methods에 근거한 교육용 재구성으로 실제 activation이나 성능 측정 그림이 아니다. 최초 공개 연대와 채택 버전은 plans/MC_AUDIO_LM_HISTORY.md에 구분하여 기록했다. 화살표는 그림 내부의 데이터 흐름이며 논문 간 성능 상승을 뜻하지 않는다.

[연구사와 발표 노트]
Audio encoder의 특징을 연속 입력으로 바꾸어 언어 모델과 연결하는 틀은 일반 Audio-LM에도 있다. Pengi 2023은 학습 가능한 audio encoder와 mapping network로 frozen GPT2에 prefix를 연결한다. 이 배경 사례는 연속 오디오 입력 추가가 LM LoRA를 필수로 요구하지 않음을 보여주며 27개 핵심 공간 문헌의 추가 성능 비교로 세지 않는다.
BAT는 AudioMAE 기반 Spatial-AST에 binaural mel/IPD를 주고 사건·방향·거리의 지각 목표로 공간 표현을 학습한다. projection으로 text embedding 차원에 맞춘 출력 특징을 질문과 LLaMA2에 제공한다. 지각에서 다중 음원·관계 질문으로 확장하는 perception-to-reasoning 학습을 사용한다. BAT에도 다중 음원 C/D/E 질문이 있으므로 후속 논문의 정적 장면 한계를 단일 음원 전용이었다는 뜻으로 바꾸지 않는다.
BAT v1/v4 본문은 LLaMA-Adapter V2의 projection 및 zero-init attention, norm/bias/scale 등 적응을 설명한다. 공개 SLAM-LLM 실행 구성의 Q-Former+LoRA와 논문 결과를 동일한 세부 구현으로 합치지 않는다. 그림의 LM 적응은 이 공통 역할만 뜻한다. BAT의 연구사적 의미는 기존 음향 모델의 좌표 출력만 읽는 것을 넘어 공간 표현을 직접 질문 조건부 생성에 재사용하는 초기 공간 Audio-LM의 대표 틀이라는 점이다.
-->

---
layout: "seminar"
variant: "result"
chapter: "03 · 2024–2025: 공간 QA의 출발과 분화"
causalStage: "main"
originSlide: 39
---

# BAT 2024: 공간 입력은 관계 질문에 기여했는가?

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">SpatialSoundQA · 두 음원의 관계 Yes/No · 같은 최종 BAT</p>
<PaperFigure src="/diagrams/result-39.svg" alt="관계 질문 · 평균 BA (%) ↑ 원문 수치 비교 그래프. P · 질문만: 54.48; B + P · 바이노럴 + 질문: 76.89" />
</div>

::takeaway::
이 평가에서 **바이노럴 입력을 제공한 조건**의 관계 QA 점수가 더 높다.

::source::
BAT, arXiv:2402.01591v4, Table 4의 최종 BAT 두 입력 행. 원문 수치의 그래프 재구성.

<!--
[현재 S23 · 본문]
03 · 2024–2025: 공간 QA의 출발과 분화

[설명의 중심]
BAT Table 4는 question-only 대비 binaural input의 실제 추가 기여를 관찰한 근거다.

[연결]
다음에 확인할 질문: 같은 연결 틀에서, 인코더가 배워야 할 것을 바꾼다

[상세 근거와 해석 범위]
[S23]
[Sources]
- https://arxiv.org/html/2402.01591v4
[발표 노트]
표의 P는 prompt, B는 binaural을 뜻한다. 같은 최종 BAT에 질문만 주는 경우와 질문·오디오를 함께 주는 경우를 읽는다. Type E는 두 음원 관계의 Yes/No 질문이며 평균 balanced accuracy로 평가한다. 질문만으로도 54.48%가 남고 바이노럴을 제공하면 76.89%로 높아진다. 공간 인코더의 사전학습과 perception-to-reasoning 언어 연결 학습을 구분해야 한다.
[해석 범위]
AudioSet 원음을 SoundSpaces RIR로 공간화한 10초 합성 바이노럴 조건이다. mono 행은 stage III만 학습한 모델이므로 여기의 최종 three-stage 모델과 입력만 다른 통제가 아니다. 이 결과는 청각 관측의 유용성을 보이지만 특정 위상 단서의 인과효과는 분리하지 않는다.

[시각화 전 표의 수치·조건 보존]
SpatialSoundQA · 두 음원의 관계 Yes/No · 같은 최종 BAT

모델에 제공한 입력 | Type E 평균 BA (%) / 높을수록 좋음 | 

P · 질문만 | 54.48 | 

B + P · 바이노럴 + 질문 | 76.89 |
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "03 · 2024–2025: 공간 QA의 출발과 분화"
causalStage: "main"
---

# 같은 연결 틀에서, 인코더가 배워야 할 것을 바꾼다

::body::
<PaperFigure src="/diagrams/history-encoder-branches.svg" alt="2025년 DSpAST와 OWL은 BAT의 공간 표현 문제를 각각 과제별 단서 선택과 방 기하 감독으로 확장한다. 둘의 공통 기반과 다른 학습 개입을 먼저 보여 준 뒤 각 내부 비교를 읽는다." />

::takeaway::
같은 공간 QA 틀에서도 **어떤 신호 단서를 넣고 어떤 목표로 E를 학습하는지**가 다르다.

::source::
DSpAST v1 §2–4 · OWL v1 §4–5 · BAT 기반의 명시적 확장/참조.

<!--
[현재 S24 · 본문]
03 · 2024–2025: 공간 QA의 출발과 분화

[설명의 중심]
2025년 DSpAST와 OWL은 BAT의 공간 표현 문제를 각각 과제별 단서 선택과 방 기하 감독으로 확장한다. 둘의 공통 기반과 다른 학습 개입을 먼저 보여 준 뒤 각 내부 비교를 읽는다.

[연결]
다음에 확인할 질문: DSpAST 2025: 같은 LM 연결에서 인코더를 비교한다

[상세 근거와 해석 범위]
[Sources]
- https://arxiv.org/html/2509.13927v1
- https://arxiv.org/html/2509.26140v1

[그림]
이 그림은 원문 Methods에 근거한 교육용 재구성으로 실제 activation이나 성능 측정 그림이 아니다. 최초 공개 연대와 채택 버전은 plans/MC_AUDIO_LM_HISTORY.md에 구분하여 기록했다. 화살표는 그림 내부의 데이터 흐름이며 논문 간 성능 상승을 뜻하지 않는다.

[연구사와 발표 노트]
DSpAST는 BAT Spatial-AST를 확장하여 ILD/GCC 등의 특징, feature attention, 의미·방향·거리별 표현을 설계한다. patch embedding과 Transformer backbone 공유를 유지하며 사전학습 curriculum과 AdaCos loss도 달라진다. 따라서 이후 QA 비교를 attention 블록 하나의 인과 효과로 읽지 않는다. QA에서는 E를 고정하고 P와 LM LoRA를 학습한다.
OWL은 BAT의 mel/IPD 입력과 LLaMA2 연결을 참조하면서 SAGE의 사전학습에 depth와 RIR 재구성 감독을 도입한다. 이 정보는 사전학습에만 사용하며 QA 추론에서는 binaural audio만 받는다. E를 고정한 후 Q-Former와 LoRA를 학습하며 perceptual→relation→CoT curriculum을 쓴다. 두 논문이 LM 인터페이스의 큰 틀을 유지하면서 encoder가 남기는 공간 정보를 바꾼다는 질문으로 읽는다.
이후 DSpAST 장의 Table3는 같은 single-stage BAT 연결에서 encoder 설계/사전학습을 비교한 QA 결과이다. OWL 장의 Table5는 SAGE의 geometry loss에 따른 위치 판독 결과이며 QA 또는 LoRA 효과를 직접 비교한 표가 아니다. 두 평가의 결과 수준을 혼동하지 않는다.
-->

---
layout: "seminar"
variant: "result"
chapter: "03 · 2024–2025: 공간 QA의 출발과 분화"
causalStage: "main"
originSlide: 41
---

# DSpAST 2025: 같은 LM 연결에서 인코더를 비교한다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">합성 바이노럴 · single-stage BAT · 전체 질문 5 epochs, LoRA, greedy decoding</p>
<PaperFigure src="/diagrams/result-41.svg" alt="방향 정확도 (%) ↑
Type D · 8범주, DER (%) ↓
거리 오차 > 0.5 m, 관계 평균 BA (%) ↑
Type E 원문 수치 비교 그래프. SpatialAST: 34.80, 53.40, 74.04; DSpAST: 37.35, 48.51, 76.56" />
</div>

::takeaway::
LLM 인터페이스를 맞춘 비교에서 **인코더 설계·사전학습의 기여**를 읽는다.

::source::
DSpAST, arXiv:2509.13927v1, Table 3의 single-stage 두 행. ↑ 높을수록, ↓ 낮을수록 좋음.

<!--
[현재 S25 · 본문]
03 · 2024–2025: 공간 QA의 출발과 분화

[설명의 중심]
DSpAST의 matched QA interface 결과는 새 feature encoder의 기여에 해당한다. 특정 물리 단서 하나만 분리한 실험은 아니다.

[연결]
다음에 확인할 질문: OWL 2025: 기하 감독은 위치 추정에 기여했는가?

[상세 근거와 해석 범위]
[S25]
[Sources]
- https://arxiv.org/html/2509.13927v1
[발표 노트]
앞 장의 설계가 최종 언어 질문에도 유용한지 읽는다. 먼저 Type D의 목표 음원 방향 정확도는 34.80에서 37.35%로 높아지고, 거리 오차가 0.5m를 넘는 비율 DER는 53.40에서 48.51%로 낮아진다. 두 음원 관계 Type E의 평균 BA도 74.04에서 76.56%로 높아진다. 방향 정확도, 거리 실패 비율, 관계 판단은 서로 다른 지표라 단순 합산하지 않는다.
[해석 범위]
이 비교에서는 인코더 특징뿐 아니라 사전학습 curriculum과 AdaCos loss도 다르다. 차이 전체를 세 분기에 귀속할 수 없다. 원 BAT와 checkpoint 및 의미 평가 embedding이 달라 S23 수치와 직접 연결하지 않는다. 원문의 질문 유형 설명 일부 오기는 BAT의 유형 정의를 따른다.

[시각화 전 표의 수치·조건 보존]
합성 바이노럴 · single-stage BAT · 전체 질문 5 epochs, LoRA, greedy decoding

인코더 | 방향 정확도 (%) ↑ / Type D · 8범주 | DER (%) ↓ / 오차 > 0.5 m 비율 | 관계 평균 BA (%) ↑ / Type E | 

SpatialAST | 34.80 | 53.40 | 74.04 | 

DSpAST | 37.35 | 48.51 | 76.56 |
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->

---
layout: "seminar"
variant: "result"
chapter: "03 · 2024–2025: 공간 QA의 출발과 분화"
causalStage: "main"
originSlide: 44
---

# OWL 2025: 기하 감독은 위치 추정에 기여했는가?

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">BiDepth 합성 평가 · 추론 입력은 바이노럴 · 기하 지도 loss 비교</p>
<PaperFigure src="/diagrams/result-44.svg" alt="방향 MAE (°) ↓, 거리 DER (%) ↓ 원문 수치 비교 그래프. 바이노럴 loss · $\eta_2=0$: 26.32, 17.11; 전체 loss · $\eta_2=10^{-2}$: 21.67, 14.32" />
<p class="seminar-chart-note">DER: 거리 오차가 0.5 m를 넘는 비율</p>
</div>

::takeaway::
이 표의 개입은 **인코더의 geometry loss**다. 어댑터·LoRA·CoT 효과를 뜻하지 않는다.

::source::
OWL, arXiv:2509.26140v1, Table 5. DER: 거리 오차가 0.5 m를 넘는 비율.

<!--
[현재 S26 · 본문]
03 · 2024–2025: 공간 QA의 출발과 분화

[설명의 중심]
OWL Table 5는 SAGE의 geometry loss에 대한 공간 예측 ablation이다. projector나 CoT·LoRA의 효과로 섞지 않는다.

[연결]
다음에 확인할 질문: Motion 2025: 지각 결과를 JSON으로 넘기는 대안

[상세 근거와 해석 범위]
[S26]
[Sources]
- https://arxiv.org/html/2509.26140v1
[발표 노트]
여기서는 전체 QA 시스템의 성능 차이보다 좁게 SAGE loss를 비교한다. 바이노럴 항만 사용한 η₂=0과 기하 항을 포함한 η₂=10⁻² 조건이다. 방향 MAE는 26.32도에서 21.67도로, 거리 오차가 0.5m를 넘는 DER는 17.11%에서 14.32%로 줄었다. 낮은 값이 좋은 두 오차 지표를 함께 읽는다.
[해석 범위]
이 수치를 CoT나 projector의 효과로 섞지 않는다. 또한 모든 전이 지표가 좋아지는 것은 아니다. Table 2의 SSQA MAE는 geometry SAGE 18.47도가 Spatial-AST 17.94도보다 높다. Table 4 QA 전체 시스템 비교와 Table 6 CoT 비교는 별도의 실험이다.

[시각화 전 표의 수치·조건 보존]
BiDepth 합성 평가 · 추론 입력은 바이노럴 · 기하 지도 loss 비교

SAGE의 학습 조건 | 방향 MAE (°) / 낮을수록 좋음 | 거리 DER (%) / 낮을수록 좋음 | 

바이노럴 loss · $\eta_2=0$ | 26.32 | 17.11 | 

전체 loss · $\eta_2=10^{-2}$ | 21.67 | 14.32 |
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->

---
layout: "seminar"
variant: "result"
chapter: "03 · 2024–2025: 공간 QA의 출발과 분화"
causalStage: "main"
originSlide: 60
---

# Motion 2025: 지각 결과를 JSON으로 넘기는 대안

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">학습한 지각 결과 → JSON → 같은 Qwen-7B 추론 모델 · QA 정확도 (%) ↑</p>
<PaperFigure src="/diagrams/result-60.svg" alt="DoA·trajectory, Overall 원문 수치 비교 그래프. DSAST + Qwen7B: 35.8, 20.7; DSAST w/ AGM + Qwen7B: 26.4, 31.1" />
</div>

::takeaway::
AGM 결합 경로의 **전체 QA는 개선됐지만 방향·궤적 질문은 낮아졌다.**

::source::
Spatial Audio Motion Understanding and Reasoning, arXiv:2509.14666v1, Table 3. ↑ 높을수록 좋음.

<!--
[현재 S27 · 본문]
03 · 2024–2025: 공간 QA의 출발과 분화

[설명의 중심]
Motion 2025는 속성 추정과 LLM 추론을 잇는 경로로, 연속 audio token 결합과 구분한다.

[연결]
다음에 확인할 질문: 기존 Audio-LM을 살리고 공간 경로를 붙이는 문제

[상세 근거와 해석 범위]
[S27]
[Sources]
- https://arxiv.org/html/2509.14666v1
[발표 노트]
언어 모델이 원 파형을 직접 듣는 경로가 아니라 지각 모델의 시간별 예측을 JSON으로 읽는 구조다. 동일한 DeepSeek-R1-distilled Qwen-7B와 greedy decoding을 사용한 두 행을 고른다. DSAST에 AGM을 결합하면 Overall은 20.7에서 31.1%로 높아진다. 그러나 DoA·trajectory는 35.8에서 26.4%로 낮아진다. 이를 모든 움직임 질문의 개선으로 요약하지 않는다.
[해석 범위]
지각 인코더와 AGM은 학습하며 training-free는 추가 추론 LLM 연결에 관한 표현이다. stereo STARSS23 기반 시간별 예측을 사용하고 QA는 STARSS23 test metadata에서 만든 Boolean·single-answer MCQ다. 정답 속성을 넣는 oracle 결과와 혼합하지 않는다. Table 2 미관측 클래스 encoder 평가는 이 QA 표와 별개다. 본문 문장의 일부 모델명보다 정확한 표 행을 따른다.

[시각화 전 표의 수치·조건 보존]
학습한 지각 결과 → JSON → 같은 Qwen-7B 추론 모델 · QA 정확도 (%) ↑

지각 → 추론 경로 | DoA·trajectory | Overall | 

DSAST + Qwen7B | 35.8 | 20.7 | 

DSAST w/ AGM + Qwen7B | 26.4 | 31.1 |
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "04 · 2025–2026: 기존 Audio-LM에 공간 경로를 더한다"
causalStage: "main"
---

# 기존 Audio-LM을 살리고 공간 경로를 붙이는 문제

::body::
<PaperFigure src="/diagrams/history-extensions.svg" alt="Sci-Phi부터 기존 의미·음성 경로와 공간 경로의 병렬 결합이 중요한 설계 질문이 된다. PhaseCoder·Spatial-Omni·TWNM은 같은 모델의 순차 개선이 아니라 배열 기하·이식 절차·음원 결속에 대한 서로 다른 선택이다." />

::takeaway::
새 공간 경로를 붙인 뒤에는 **공간 정보의 기여와 기존 의미 능력**을 함께 확인해야 한다.

::source::
Sci-Phi v1 §3 · PhaseCoder v2 §3.3 · TWNM v3 §3 · Spatial-Omni v2 §3·5.

<!--
[현재 S28 · 본문]
04 · 2025–2026: 기존 Audio-LM에 공간 경로를 더한다

[설명의 중심]
Sci-Phi부터 기존 의미·음성 경로와 공간 경로의 병렬 결합이 중요한 설계 질문이 된다. PhaseCoder·Spatial-Omni·TWNM은 같은 모델의 순차 개선이 아니라 배열 기하·이식 절차·음원 결속에 대한 서로 다른 선택이다.

[연결]
다음에 확인할 질문: Sci-Phi 2025: 기존 의미 경로 옆에 공간 경로를 학습한다

[상세 근거와 해석 범위]
[Sources]
- https://arxiv.org/html/2510.05542v1
- https://arxiv.org/html/2601.21124v2
- https://arxiv.org/html/2601.02954v3
- https://arxiv.org/html/2606.10738v2

[그림]
이 그림은 원문 Methods에 근거한 교육용 재구성으로 실제 activation이나 성능 측정 그림이 아니다. 최초 공개 연대와 채택 버전은 plans/MC_AUDIO_LM_HISTORY.md에 구분하여 기록했다. 화살표는 그림 내부의 데이터 흐름이며 논문 간 성능 상승을 뜻하지 않는다.

[연구사와 발표 노트]
이 그림은 공통 설계 질문을 추상화한다. 구체적인 토큰 순서, 경로 고정 여부, projector의 융합 위치는 논문마다 다르다. 동일한 하나의 모델 계보로 읽지 않는다.
Sci-Phi는 Phi4-Multimodal의 기존 mono 의미 encoder/projector/audio LoRA를 고정하고 공간 encoder/projector/spatial LoRA를 학습한다. What/Where/When을 같은 음원에 결속하는 기술을 목표로 한다. PhaseCoder는 위상과 마이크 좌표를 공간 encoder에 입력하고 Gemma3n의 기존 USM audio tokens 앞에 spatial soft tokens를 추가한다. P와 Gemma LoRA를 학습하지만 공간 encoder의 QA 동결 여부는 확정하지 않는다.
TWNM 채택 v3는 FOA 공간 map과 Whisper 의미 feature를 dense hybrid projector로 결합한다. source-slot 감독용 출력과 실제 LM 입력인 dense features를 구분한다. Spatial-Omni는 여러 기존 Audio/Omni backbone의 의미 경로를 유지하면서 SO-Encoder와 공간 projector를 붙이고 P→P+LoRA→P+LoRA+공간 E의 학습 단계를 비교한다.
이후 상세 장은 이 질문별로 묶었으므로 날짜순의 성능 사다리가 아니다. 첫 공개 연대는 앞의 지도에, 세부 구현은 채택 버전에 귀속한다. PhaseCoder의 공간 지정 목표 전사 WER는 일반 의미 능력 보존 평가와 다르며 Spatial-Omni의 별도 일반 오디오 평가와도 구별한다.
-->

---
layout: "seminar"
variant: "method"
chapter: "04 · 2025–2026: 기존 Audio-LM에 공간 경로를 더한다"
causalStage: "main"
originSlide: 51
---

# Sci-Phi 2025: 기존 의미 경로 옆에 공간 경로를 학습한다

::body::
<PaperFigure src="/research/sciphi-core.png" alt="Sci-Phi Fig. 1. FOA의 공간 특징과 W 채널 spectral 특징을 두 인코더·projector로 Phi-4에 결합한 원문 구조" caption="공간 경로는 적응하고, 기존 mono 의미 인코더·projector·audio LoRA는 고정한다." />

::takeaway::
**기존 의미 경로는 고정**하고 공간 encoder·projector·LoRA를 적응한다.

::source::
Sci-Phi, arXiv:2510.05542v1, Fig. 1의 인코더·projector·LLM 경로 크롭.

<!--
[현재 S29 · 본문]
04 · 2025–2026: 기존 Audio-LM에 공간 경로를 더한다

[설명의 중심]
Sci-Phi는 고정된 의미 인코더·projector·audio LoRA를 유지하며 공간 인코더·projector·spatial LoRA를 적응하는 분기 설계다.

[연결]
다음에 확인할 질문: PhaseCoder: 특정 마이크 배열에 묶이지 않는 공간 입력

[상세 근거와 해석 범위]
[S29]
[Sources]
- https://arxiv.org/html/2510.05542v1
[발표 노트]
FOA 네 채널의 mel 특징과 W를 기준으로 계산한 intensity vector를 공간 인코더가 읽는다. 기존 mono 의미 인코더는 W 채널의 mel 특징만 읽는다. 두 경로의 projector가 언어 모델에 결합한다. 원문의 불 표식은 학습, 눈송이는 고정을 뜻한다. 공간 인코더와 공간 projector, spatial LoRA는 적응하고 기존 의미 인코더, 의미 projector, audio LoRA는 고정한다.
[해석 범위]
의미 경로를 구조적으로 유지한다는 사실만으로 모든 기존 언어·오디오 능력의 보존이 입증되지는 않는다. 비교 기준선은 고정 SELDNet 표현을 쓰며 Sci-Phi는 공간 encoder도 적응한다. 두 시스템 모두 장면 기술에 미세조정했다는 점이 근거 부록의 TupleScore 결과 해석의 전제다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "04 · 2025–2026: 기존 Audio-LM에 공간 경로를 더한다"
causalStage: "main"
originSlide: 47
---

# PhaseCoder: 특정 마이크 배열에 묶이지 않는 공간 입력

::body::
<PaperFigure src="/research/p2-phasecoder-v2-input.png" alt="PhaseCoder Fig. 2 상단. 약 13 ms 구간에서 네 마이크 채널의 파형과 채널 간 위상 차이를 보여 주는 원문 패널" caption="원문 Fig. 2 상단: 네 채널 파형. x축 시간(ms), y축 amplitude." />

::aside::
<section><span class="seminar-label semantic-input">공간 경로</span><p>다채널 오디오<br/>+ 마이크 좌표</p></section><section><span class="seminar-label ">의미 경로</span><p>기존 mono 오디오<br/>+ 텍스트 질문</p></section><section><span class="seminar-label semantic-geometry">명칭의 범위</span><p>배열 변화에 대응<br/>좌표는 계속 필요</p></section>

::takeaway::
PhaseCoder의 추론 입력에는 **다채널 오디오와 마이크 좌표**가 함께 필요하다.

::source::
PhaseCoder, arXiv:2601.21124v2, Fig. 2 상단 패널 크롭.

<!--
[현재 S30 · 본문]
04 · 2025–2026: 기존 Audio-LM에 공간 경로를 더한다

[설명의 중심]
PhaseCoder는 geometry-aware spatial tokens로 mono 경로를 확장한다.

[연결]
다음에 확인할 질문: PhaseCoder: 공간 QA와 목표 발화 전사의 절충

[상세 근거와 해석 범위]
[S30]
[Sources]
- https://arxiv.org/html/2601.21124v2
[발표 노트]
상단의 짧은 파형 구간에서 같은 음향 사건이 채널마다 서로 다른 관계로 관측되는 것을 본다. 같은 방향이라도 마이크의 수와 배치가 바뀌면 이런 관계가 달라진다. PhaseCoder는 다채널 오디오와 마이크 좌표를 받아 공간 토큰을 만들고, 기존 의미 오디오 경로와 함께 언어 모델에 제공한다. 그림의 아래 분류 head 결과는 이번 문제 관측과 분리하기 위해 크롭했다.
[해석 범위]
geometry-agnostic을 좌표가 필요 없다는 뜻으로 번역하지 않는다. 무지향·free-floating 마이크 배열 가정과 장치에 의한 산란 효과를 구분한다. 원문 Table 1의 실제 녹음 DOA는 인코더 평가이며 다음 QA 실험과 동일한 시험이 아니다.
-->

---
layout: "seminar"
variant: "result"
chapter: "04 · 2025–2026: 기존 Audio-LM에 공간 경로를 더한다"
causalStage: "main"
originSlide: 48
---

# PhaseCoder: 공간 QA와 목표 발화 전사의 절충

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">Gemma · Task 2 관계 Yes/No 정확도 (%) ↑ · 두 발화를 비중첩 연결</p>
<PaperFigure src="/diagrams/result-48.svg" alt="Synthetic 정확도 (%) ↑, RSL2019 정확도 (%) ↑ 원문 수치 비교 그래프. Baseline · mono: 48.44, 53.91; SFT · 공간 입력 + 학습: 76.76, 73.83" />
<p class="seminar-chart-note">반례 · RSL Task 4 mean WER: 42.90 → 48.41 (낮을수록 좋음)</p>
</div>

::takeaway::
**관계 QA와 공간 지정 목표 발화 전사**는 별도 과제로 확인해야 한다.

::source::
PhaseCoder, arXiv:2601.21124v2, Table 3. RSL QA는 train split 녹음에서 재구성.

<!--
[현재 S31 · 본문]
04 · 2025–2026: 기존 Audio-LM에 공간 경로를 더한다

[설명의 중심]
PhaseCoder Task 4는 공간으로 목표 화자를 골라 전사하는 과제다. WER는 선택·결속·전사의 오류를 함께 반영하며 일반 ASR 보존의 직접 지표가 아니다.

[연결]
다음에 확인할 질문: Spatial-Omni: 여러 기반 모델에 공간 경로를 이식한다

[상세 근거와 해석 범위]
[S31]
[Sources]
- https://arxiv.org/html/2601.21124v2
[발표 노트]
관계 Yes/No를 묻는 Task 2에서 Gemma baseline과 제안 SFT 시스템을 비교한다. 합성 평가의 정확도는 48.44에서 76.76%, RSL2019 재구성 QA는 53.91에서 73.83%로 높아진다. 그러나 목표 발화를 전사하는 RSL Task 4의 mean WER는 42.90에서 48.41로 악화한다. 서로 다른 과제를 합친 평균으로 이 상반된 결과를 가리지 않는다.
[해석 범위]
Baseline은 mono 입력이고 SFT에는 공간 입력과 추가 학습이 함께 들어가므로 공간 토큰만의 독립 인과효과가 아니다. Synthetic은 미사용 LibriSpeech·RIR·배열을 사용한다. RSL QA는 원 데이터 train split 녹음으로 재구성했으며 두 발화는 비중첩 연결이다. Gemma 의미 입력은 채널 평균이다. 원문은 WER>3.0 출력을 제외하므로 미필터 오류율을 보장하지 않는다.

[시각화 전 표의 수치·조건 보존]
Gemma · Task 2 관계 Yes/No 정확도 (%) ↑ · 두 발화를 비중첩 연결

시스템 조건 | Synthetic | RSL2019 | 

Baseline · mono | 48.44 | 53.91 | 

SFT · 공간 입력 + 학습 | 76.76 | 73.83 | 

반례　RSL Task 4 mean WER: 42.90 → 48.41 (낮을수록 좋음)
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
[과제 귀속 보완]
Task 4는 공간으로 지정한 목표 화자를 골라 전사하는 targeted transcription이다. WER는 선택·결속·전사 오류를 함께 반영하며 일반 ASR 또는 기존 의미 능력 보존을 직접 측정한 지표가 아니다.
-->

---
layout: "seminar"
variant: "method"
chapter: "04 · 2025–2026: 기존 Audio-LM에 공간 경로를 더한다"
causalStage: "main"
originSlide: 54
---

# Spatial-Omni: 여러 기반 모델에 공간 경로를 이식한다

::body::
<PaperFigure src="/research/spatialomni-core.png" alt="Spatial-Omni Fig. 1 오른쪽 경로. FOA 공간 encoder와 W 채널 audio encoder가 각각 projector를 거쳐 언어 입력에 결합" caption="Fig. 1 오른쪽 경로 크롭. 영상은 기존 backbone의 선택 경로이며 공간 QA의 추가 관측이 아니다." />

::aside::
<section><span class="seminar-label semantic-input">두 입력 경로</span><p>FOA → 공간 encoder<br/>W → 의미 encoder</p></section><section><span class="seminar-label semantic-geometry">학습 순서</span><p>projector 정렬<br/>→ LoRA 결합<br/>→ 공간 경로 적응</p></section>

::takeaway::
**projector 정렬 → LLM LoRA → 공간 경로 적응**으로 학습 문제를 나눈다.

::source::
Spatial-Omni, arXiv:2606.10738v2, Fig. 1 오른쪽 패널·§5.

<!--
[현재 S32 · 본문]
04 · 2025–2026: 기존 Audio-LM에 공간 경로를 더한다

[설명의 중심]
Spatial-Omni는 projector 정렬, LoRA, 공간 경로 적응을 나눠 학습하는 구체적인 사례다.

[연결]
다음에 확인할 질문: Spatial-Omni: 추가한 공간 입력의 기여를 확인한다

[상세 근거와 해석 범위]
[S32]
[Sources]
- https://arxiv.org/html/2606.10738v2
[발표 노트]
FOA 공간 관측은 SO-Encoder에 들어가고 W 채널은 기존 Audio Encoder로 들어간다. 별도의 projector가 공간 표현을 언어 토큰 차원에 맞춰 기존 오디오 및 텍스트 토큰과 결합한다. 원문의 전체 그림 중 결합 경로를 크롭했으며 SO-Encoder 내부 블록은 생략했다. 원본의 visual branch는 기반 멀티모달 모델의 구조이고 여기의 공간 QA에서 영상 정보를 새 관측으로 사용한다는 뜻은 아니다.
[해석 범위]
기본 학습은 projector 정렬, LLM LoRA 결합, 공간 encoder의 학습 가능한 부분을 포함한 적응으로 구성된다. 기존 의미 경로를 구조적으로 보존하는 것과 실제 일반 오디오 성능의 보존은 다르다. Fig. 5에서 MIX는 일부 성능을 회복하지만 완전 보존으로 말하지 않는다.

[기존 의미 능력]
기존 audio tower를 고정한 구조만으로 의미 능력의 보존을 보장하지 않는다. Spatial-Omni v2 Table 18과 MIX 비교가 별도의 일반 오디오 평가 근거다. PhaseCoder의 targeted transcription WER와 구별한다.
-->

---
layout: "seminar"
variant: "result"
chapter: "04 · 2025–2026: 기존 Audio-LM에 공간 경로를 더한다"
causalStage: "main"
originSlide: 55
---

# Spatial-Omni: 추가한 공간 입력의 기여를 확인한다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">SO-Bench · 같은 7B 계열 · greedy decoding · 점수는 모두 % (높을수록 좋음)</p>
<PaperFigure src="/diagrams/result-55.svg" alt="EAzi (%) ↑
방위각 오차 ≤ 20°, IS-Loc (%) ↑
위치로 음원 식별, RLR (%) ↑
상대 좌우 원문 수치 비교 그래프. SO-7B-zs · 공간 토큰 0: 13.06, 40.69, 47.15; SO-7B · 실제 공간 토큰: 76.38, 66.81, 72.97" />
</div>

::takeaway::
이 zero-spatial 비교는 **공간 입력 기여의 근거**이며 제거 시점·checkpoint 공유는 미명시다.

::source::
Spatial-Omni, arXiv:2606.10738v2, Table 2의 SO-7B-zs/SO-7B. MIX와 구분.

<!--
[현재 S33 · 본문]
04 · 2025–2026: 기존 Audio-LM에 공간 경로를 더한다

[설명의 중심]
Spatial-Omni의 zero-spatial 변형과 full 모델을 비교한다. 고정 checkpoint에서의 추론 시 제거 실험이라고 단정하지 않는다.

[연결]
다음에 확인할 질문: TWNM v3: 의미와 공간을 같은 음원에 묶는다

[상세 근거와 해석 범위]
[S33]
[Sources]
- https://arxiv.org/html/2606.10738v2
[발표 노트]
S33에서 구분한 세 질문으로 돌아간다. SO-7B-zs는 공간 토큰을 0으로 만든 조건이고 SO-7B는 실제 공간 토큰을 받는다. EAzi는 방위각 오차가 20도 안에 들어오는 비율, IS-Loc은 위치 기반 식별, RLR은 상대 좌우 판정이다. 선택한 세 점수가 실제 공간 토큰 조건에서 모두 높다. 같은 7B 계열의 내부 비교로 읽는다.
[해석 범위]
입력 ablation이 공간 정보의 유용성을 보이지만 특정 phase 기전을 입증하지 않는다. SO-7B와 MIX를 섞지 않는다. 복합 MH 점수는 22.52/39.93으로 여전히 어렵다. 일반 오디오 성능의 완전 보존이나 임의 배열 일반화는 이 실험으로 주장할 수 없다. SC의 WER는 낮을수록 좋은 별도 지표다.

[시각화 전 표의 수치·조건 보존]
SO-Bench · 같은 7B 계열 · greedy decoding · 점수는 모두 % (높을수록 좋음)

모델·공간 입력 | EAzi / 방위각 오차 ≤ 20° | IS-Loc / 위치로 음원 식별 | RLR / 상대 좌우 | 

SO-7B-zs · 토큰 0 | 13.06 | 40.69 | 47.15 | 

SO-7B · 실제 토큰 | 76.38 | 66.81 | 72.97 |
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.

[원문 확인 보완]
Spatial-Omni v2 §5.3과 Appendix E.2는 zero/null spatial token을 사용한 변형을 명시하지만, 적용 시점이 학습부터인지 추론만인지와 checkpoint 공유 여부는 명시하지 않는다. 고정 checkpoint의 추론 시 제거 ablation으로 단정하지 않는다.
-->

---
layout: "seminar"
variant: "method"
chapter: "04 · 2025–2026: 기존 Audio-LM에 공간 경로를 더한다"
causalStage: "main"
originSlide: 57
---

# TWNM v3: 의미와 공간을 같은 음원에 묶는다

::body::
<PaperFigure src="/research/p2-twnm-v3-fig2.png" alt="TWNM Fig. 2 원문 구조. FOA spatial encoder와 semantic encoder, hybrid projector와 단계별 언어 학습" caption="v3: 공간 encoder 학습·적응 → projector 정렬 → SFT → SAPO." />

::takeaway::
**source slots로 감독**하지만, LLM에는 의미 경로와 결합한 **dense 특징**을 보낸다.

::source::
The World is Not Mono, arXiv:2601.02954v3, Fig. 2·§4.1–4.2. v3의 FOA·SAPO.

<!--
[현재 S34 · 본문]
04 · 2025–2026: 기존 Audio-LM에 공간 경로를 더한다

[설명의 중심]
TWNM의 source slots는 학습 감독이고 실제 hybrid projector에는 dense encoder map이 전달된다.

[연결]
다음에 확인할 질문: TWNM의 connector 설계 비교는 adapter가 단순 차원 변환 이상의 선택임을 보여 준다. semantic-judge 점수이며 checkpoint·학습 예산을 완전히 맞췄다는 조건은 미명시다.

[상세 근거와 해석 범위]
[S34]
[Sources]
- https://arxiv.org/html/2601.02954v3
[발표 노트]
원문의 왼쪽은 FOA 오디오를 공간 경로와 의미 경로로 나누고, 가운데 hybrid projector가 두 표현을 결합하는 구조다. 의미 경로는 W 채널의 고정 Whisper-small이고 공간 encoder는 최대 세 source slots와 방향·거리·사건·존재 여부를 지도 학습한다. 다만 pooled slot head만 LLM에 보내는 것은 아니다. §4.1은 dense encoder map을 의미 경로 길이에 맞춰 결합한다고 설명한다.
[해석 범위]
그림의 Stage 1은 공간 인코더 학습·적응, Stage 2는 projector 정렬, Stage 3은 SFT, Stage 4는 SAPO다. v3의 FOA와 SAPO를 초기 버전의 binaural·GRPO로 바꾸지 않는다. source slots에 의한 내부 지도와 명시적인 scene graph 출력도 다르다.
-->

---
layout: "seminar"
variant: "result"
chapter: "04 · 2025–2026: 기존 Audio-LM에 공간 경로를 더한다"
causalStage: "main"
---

# 토큰을 결합하는 설계에 따라 결과가 달라졌다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">TWNM · ASA 평가 · semantic-judge · 원문 보고 Overall · 최종 SAPO 이전</p>
<PaperFigure src="/diagrams/causal-module-evidence.svg" alt="TWNM v3 Appendix G Table 15 connector 비교. Overall: P0 Single MLP 39.20, P1 Dual Tower 46.40, P2 Dense Hybrid 52.10 퍼센트" />
<p class="seminar-chart-note">동일 checkpoint·학습 예산의 완전 통제는 미명시 · 별도 exact-MCQA 점수와 채점법이 다름</p>
</div>

::takeaway::
어댑터에서는 **어떤 특징을 나누고 결합하는가**도 학습 설계의 일부다.

::source::
The World is Not Mono, arXiv:2601.02954v3, Appendix G, Table 15. 보고 수치 그대로 재구성.

<!--
[현재 S35 · 본문]
04 · 2025–2026: 기존 Audio-LM에 공간 경로를 더한다

[설명의 중심]
TWNM의 connector 설계 비교는 adapter가 단순 차원 변환 이상의 선택임을 보여 준다. semantic-judge 점수이며 checkpoint·학습 예산을 완전히 맞췄다는 조건은 미명시다.

[연결]
다음에 확인할 질문: TWNM v3: 연결 이후에는 답변 학습 목표도 달라진다

[상세 근거와 해석 범위]
[이번 장의 역할]
인코더·어댑터·언어 모델의 전체 구조를 이해한 뒤, 어댑터를 단순 차원 변환의 부품으로만 다루지 않는 근거를 보인다. TWNM의 Appendix G Table 15는 P0: Single MLP, P1: Dual Tower, P2: Dense Hybrid 연결 설계를 비교한다. Overall은 각각 39.20, 46.40, 52.10%다. ASA 평가에 대해 원문이 보고한 Overall이다. L1/L2/L3의 단순 평균으로 만들지 않는다.

이 표의 semantic-answer judge는 질문·선지·gold·생성 답변을 받는 Gemini 3 Flash이며 audio/RTSD를 직접 보지 않는다. 최종 SAPO 이전의 진단이다. 다음 장의 main Table 5에서 SFT/SAPO를 비교한 exact MCQA와 채점법이 다르므로 숫자의 높낮이를 두 표 사이에서 비교하지 않는다.

원문은 projector ablation이라고 명명하지만 각 행의 encoder checkpoint, LLM checkpoint, 학습 예산과 seed가 완전히 같은지 별도 명시하지 않는다. 따라서 연결 설계별 보고 결과로 해석한다. P만 바꾸고 나머지를 완벽히 고정한 인과 실험이라고 강화하지 않는다. 앞서 살펴본 DSpAST는 같은 QA 인터페이스의 인코더 비교, OWL은 인코더 사전학습 loss 비교였다. 다음 장에서는 SFT와 SAPO의 답변 학습 목표를 비교한다.

[원문 산술의 한계]
본문의 수준별 문항 수 385/279/336으로 Table 15의 수준별 점수를 가중해도 이 Overall과 일치하지 않는다. P0/P1/P2 재계산은 약 39.45/46.78/52.41이며 보고값 39.20/46.40/52.10과 다르다. 평가 집계 또는 분모의 차이는 원문만으로 해결하지 못했다. 슬라이드는 보고 Overall 세 개를 그대로 인용하며 정확한 성공 문항 수로 역산하지 않는다.

[Sources]
- https://arxiv.org/html/2601.02954v3
-->

---
layout: "seminar"
variant: "result"
chapter: "04 · 2025–2026: 기존 Audio-LM에 공간 경로를 더한다"
causalStage: "main"
originSlide: 58
---

# TWNM v3: 연결 이후에는 답변 학습 목표도 달라진다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">ASA benchmark · 최대 3음원 합성 FOA · exact MCQA · 단일 실행 · 정확도 (%) ↑</p>
<PaperFigure src="/diagrams/result-58.svg" alt="L1 · 지각, L2 · 관계 연결, L3 · 복합 질의 원문 수치 비교 그래프. TWNM-SFT: 65.19, 70.61, 51.19; TWNM-SAPO: 63.64, 69.89, 79.76" />
</div>

::takeaway::
**복합 질의의 개선**과 기초 지각·관계 연결의 소폭 하락이 함께 나타난다.

::source::
The World is Not Mono, arXiv:2601.02954v3, Table 5. ↑ 높을수록 좋음.

<!--
[현재 S36 · 본문]
04 · 2025–2026: 기존 Audio-LM에 공간 경로를 더한다

[설명의 중심]
TWNM SFT→SAPO는 복합 질의가 좋아져도 기본 지각·관계 연결이 낮아지는 trade-off를 드러낸다.

[연결]
다음에 확인할 질문: 움직임을 묻기 시작하면 시간 구조가 필요하다

[상세 근거와 해석 범위]
[S36]
[Sources]
- https://arxiv.org/html/2601.02954v3
[발표 노트]
가장 큰 변화는 L3의 51.19에서 79.76% 상승이다. 그러나 앞의 두 열도 읽으면 L1은 65.19에서 63.64%, L2는 70.61에서 69.89%로 소폭 낮아졌다. 따라서 최종 정책 학습이 모든 능력을 동시에 개선했다고 요약하지 않는다. 같은 exact MCQA 프로토콜의 단일 실행 결과다.
[해석 범위]
평가의 렌더 장면, 공간 구성, 질문과 정답은 학습에서 분리했지만 dry-source clip identity는 중복될 수 있다. 새로운 음원 정체성에 대한 전이라고 부르지 않는다. STARSS23 QA는 encoder 적응 녹음과 분리되지 않아 recording-disjoint 전이도 아니다. strict pick-letter audit를 사용한 corrupted-input 통제는 본문의 full-FOA exact score와 동일한 채점 효과 크기로 합치지 않는다.

[시각화 전 표의 수치·조건 보존]
ASA benchmark · 최대 3음원 합성 FOA · exact MCQA · 단일 실행 · 정확도 (%) ↑

학습 단계 | L1 / 지각 | L2 / 관계 연결 | L3 / 복합 질의 | 

TWNM-SFT | 65.19 | 70.61 | 51.19 | 

TWNM-SAPO | 63.64 | 69.89 | 79.76 |
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "05 · 2025–2026: 정적 위치에서 이동과 시간 관계로"
causalStage: "main"
---

# 움직임을 묻기 시작하면 시간 구조가 필요하다

::body::
<PaperFigure src="/diagrams/history-dynamics.svg" alt="Motion의 명시적 시계열과 BAT 계열 Dynamic QA·ST-AudioLM의 연속 토큰 경로를 나란히 비교한다. BAT에서 후자의 backbone 계승은 원문 명시이며 세 논문 사이의 직선적인 성능 발전으로 그리지 않는다." />

::takeaway::
정적 위치 다음에는 **어느 음원이 언제 움직였는지**를 전달하는 방식이 쟁점이 된다.

::source::
Motion v1 §2.2 · Dynamic Source Movements v1 §3.2 · ST-AudioLM v1 §2·4·5.1.

<!--
[현재 S37 · 본문]
05 · 2025–2026: 정적 위치에서 이동과 시간 관계로

[설명의 중심]
Motion의 명시적 시계열과 BAT 계열 Dynamic QA·ST-AudioLM의 연속 토큰 경로를 나란히 비교한다. BAT에서 후자의 backbone 계승은 원문 명시이며 세 논문 사이의 직선적인 성능 발전으로 그리지 않는다.

[연결]
다음에 확인할 질문: 차원을 맞추는 것만으로 충분하지 않다. 압축과 pooling이 source·time 관계를 잃게 할 수 있으므로 전달 구조를 정한다.

[상세 근거와 해석 범위]
[Sources]
- https://arxiv.org/html/2509.14666v1
- https://arxiv.org/html/2602.16334v1
- https://arxiv.org/html/2606.14141v1

[그림]
이 그림은 원문 Methods에 근거한 교육용 재구성으로 실제 activation이나 성능 측정 그림이 아니다. 최초 공개 연대와 채택 버전은 plans/MC_AUDIO_LM_HISTORY.md에 구분하여 기록했다. 화살표는 그림 내부의 데이터 흐름이며 논문 간 성능 상승을 뜻하지 않는다.

[연구사와 발표 노트]
상단의 작은 궤적은 같은 질문을 설명하기 위한 합성 도형으로 모델의 실제 출력이 아니다. Motion 2025는 학습 지각 모델이 추정한 시간별 사건·방향·거리 정보를 JSON으로 추론 모델에 전달한다. Dynamic QA 2026은 BAT encoder의 penultimate layer를 시간 인식으로 바꾸고 Q-Former와 Qwen3-4B를 연결한다. AGM mask는 질문 관련 시간 구간을 고르는 추론 전처리이며 원래 파형에서 다른 시간 구간을 0으로 만든다.
ST-AudioLM은 BAT의 Spatial-AST backbone을 FOA에 맞추고 semantic/static/dynamic token을 지도 학습한다. QA에서 고정 encoder의 semantic1+dynamic40을 MLP connector와 LoRA에 연결한다. 단순 pooling의 교육용 반례와 원문의 실제41-token 비교를 이어서 본다.
Dynamic QA와 ST-AudioLM의 BAT 기반 확장은 원문이 명시하지만 Motion→Dynamic→ST의 단일 계보를 뜻하지 않는다. ST-AudioLM은 Dynamic QA를 concurrent work로 구분한다. 다음 수치들은 각각의 원문 평가 내부 비교이며 서로 다른 데이터셋과 질문을 한 성능 그래프로 합치지 않는다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "05 · 2025–2026: 정적 위치에서 이동과 시간 관계로"
causalStage: "main"
---

# 시간 평균은 서로 다른 이동을 같게 만들 수 있다

::body::
<PaperFigure src="/diagrams/causal-token-bottleneck.svg" alt="두 음원 A와 B의 이동 방향이 반대인 두 장면은 각 음원의 단순 평균 방향이 모두 0으로 같아진다. 사건별 시간 속성을 남기면 장면1의 A는 -60,0,60도이고 B는60,0,-60도로 구분된다." />

::takeaway::
이동 질문에 답하려면 **사건·위치·시간의 대응을 전달하는 표현**이 필요하다.

::source::
교육용 평균 반례 · ST-AudioLM v1 §4.1–4.2 · TWNM v3 §4.1. 실제 토큰은 연속 임베딩.

<!--
[현재 S38 · 본문]
05 · 2025–2026: 정적 위치에서 이동과 시간 관계로

[설명의 중심]
차원을 맞추는 것만으로 충분하지 않다. 압축과 pooling이 source·time 관계를 잃게 할 수 있으므로 전달 구조를 정한다.

[연결]
다음에 확인할 질문: Dynamic QA 2026: 질문에 필요한 시간 구간을 고른다

[상세 근거와 해석 범위]
[B-TOKEN-BOTTLENECK]
[Sources]
- https://arxiv.org/html/2606.14141v1
- https://arxiv.org/html/2601.02954v3
[그림]
public/diagrams/causal-token-bottleneck.svg. 실험 결과가 아닌 교육용 반례이다. 청색 실선 A, 청록 점선 B를 두 장면에서 같은 사건으로 유지했다. 장면1은 A:-60→0→60도, B:60→0→-60도이며 장면2는 각각 역순이다. 이 범위는 각도 wrap 문제가 없고, 방향의 단순 시간 평균은 각 음원 모두0도이다. 서로 다른 운동을 같은 평균으로 매핑하는 구체적인 예이다.
[발표 노트]
파란 소리가 어느 쪽으로 움직였는지 물으면 두 장면의 정답이 다르다. 단순 평균만 전달하면 두 장면을 구분할 근거가 없다. 오른쪽은 장면1의 사건과 시간을 명시적으로 대응시킨 설명용 속성 표이다. 실제 모델이 이 숫자 표나 두 개의 명시적인 source token을 LLM에 넣는다는 뜻이 아니다. 시간 해상도와 사건 정보를 유지하는 연속 표현이 이 대응을 학습할 수 있게 해야 한다.
[논문 연결]
ST-AudioLM은 10초에서 의미1+시간40=41개의 토큰을 MLP로 LLM에 전달한다. 전역 DoA/거리 토큰은 encoder 지도에 쓰지만 LLM 입력에서는 제외한다. 정적 Spatial-AST 비교도 같은41개 토큰이므로 결과 차이를 토큰 개수 증가로 설명하지 않는다. 동적 지도, temporal attention, semantic distillation/replay가 함께 바뀐다.
TWNM은 encoder에 source-slot 지도를 사용하지만 LLM 입력은 의미·공간 밀집 시계열을 융합한 연속 토큰이다. LLM이 source slot3개 또는 명시 scene graph를 직접 입력받는 그림으로 대체하지 않는다.
[해석 범위]
이 그림은 순서 정보가 없는 단순 평균의 반례이다. 학습한 전역 토큰은 시간 순서 자체를 인코딩할 수 있으므로 모든 전역 표현이 이동을 표현할 수 없다는 증명이 아니다. 토큰 길이가 길다는 사실만으로 올바른 사건 결속을 보장하지도 않는다. 실제 성능은 같은 프로토콜의 통제로 확인한다.
-->

---
layout: "seminar"
variant: "result"
chapter: "05 · 2025–2026: 정적 위치에서 이동과 시간 관계로"
causalStage: "main"
originSlide: 61
---

# Dynamic QA 2026: 질문에 필요한 시간 구간을 고른다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">합성 이동 stereo · Qwen3-4B · Overall 정확도 (%) ↑ · GT는 정답 구간 참고 조건</p>
<PaperFigure src="/diagrams/result-61.svg" alt="NoMask, AGM mask, GT mask 원문 수치 비교 그래프. Thinking: 54.3, 55.0, 56.1; Non-Thinking: 54.1, 54.0, 54.1" />
<p class="seminar-chart-note">구간 밖을 0으로 masking · 같은 구간의 간섭 음원을 분리하는 것은 아님</p>
</div>

::takeaway::
masking과 thinking의 **결합 효과는 조건에 따라 다르며 전체 개선 폭은 제한적**이다.

::source::
Spatial Audio Question Answering and Reasoning on Dynamic Source Movements, arXiv:2602.16334v1, Table 3.

<!--
[현재 S39 · 본문]
05 · 2025–2026: 정적 위치에서 이동과 시간 관계로

[설명의 중심]
Dynamic QA는 mask 조건과 reasoning mode를 분리해 비교한다.

[연결]
다음에 확인할 질문: ST-AudioLM 2026: 시간별 음원 상태를 토큰으로 남긴다

[상세 근거와 해석 범위]
[S39]
[Sources]
- https://arxiv.org/html/2602.16334v1
[발표 노트]
한 번에 한 조건만 바꿔 읽는다. Thinking 행에서는 NoMask 54.3, AGM 55.0, 정답 구간 GT 56.1%다. Non-Thinking 행에서는 54.1, 54.0, 54.1%로 거의 변하지 않는다. 같은 mask의 두 행을 비교하면 thinking의 효과도 볼 수 있다. Overall은 Yes/No, MCQ, open 질문을 포함한다.
[해석 범위]
AudioSet strong-labeled 원음에 움직임을 부여한 합성 stereo 평가다. 시간 정보를 확장한 BAT 계열 encoder, Q-Former, Qwen3-4B를 학습하고 AGM은 추론 전처리다. GT는 배포 가능한 관측이 아니라 정답 이벤트 구간을 제공한 참고 조건이다. 시간 mask는 구간 밖 파형을 0으로 하므로 같은 구간의 간섭 음원을 완전히 제거하지 못한다. 수치 차이를 통계적 유의성이나 rationale의 청각적 충실성 증명으로 바꾸지 않는다.

[시각화 전 표의 수치·조건 보존]
합성 이동 stereo · Qwen3-4B · Overall 정확도 (%) ↑ · GT는 정답 구간 참고 조건

출력 설정 | NoMask | AGM mask | GT mask | 

Thinking | 54.3 | 55.0 | 56.1 | 

Non-Thinking | 54.1 | 54.0 | 54.1 | 

시간 mask는 구간 밖을 0으로 만든다. 같은 구간의 간섭 음원까지 분리하지는 않는다.
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->

---
layout: "seminar"
variant: "method"
chapter: "05 · 2025–2026: 정적 위치에서 이동과 시간 관계로"
causalStage: "main"
originSlide: 63
---

# ST-AudioLM 2026: 시간별 음원 상태를 토큰으로 남긴다

::body::
<PaperFigure src="/research/p2-staudiolm-v1-fig1.png" alt="ST-AudioLM Fig. 1. 의미 token과 dynamic trajectory token을 만드는 encoder 및 frozen encoder에서 connector와 LoRA로 이어지는 QA 구조" caption="왼쪽: 궤적 지도 학습. 오른쪽: 고정 ST-Audio Encoder + 학습하는 connector·LoRA." />

::takeaway::
고정 인코더의 **의미·궤적 토큰**을 학습하는 connector와 LoRA로 연결한다.

::source::
ST-AudioLM, arXiv:2606.14141v1, Fig. 1. 원문 방법 그림.

<!--
[현재 S40 · 본문]
05 · 2025–2026: 정적 위치에서 이동과 시간 관계로

[설명의 중심]
ST-AudioLM은 의미 토큰과 동적 궤적 토큰을 고정 encoder에서 꺼내 connector·LoRA로 연결한다.

[연결]
다음에 확인할 질문: ST-AudioLM: 같은 41개 토큰에서도 시간 표현이 다르다

[상세 근거와 해석 범위]
[S40]
[Sources]
- https://arxiv.org/html/2606.14141v1
[발표 노트]
왼쪽의 encoder는 사건 의미 토큰과 정적 위치 토큰, 시간 구간별 동적 궤적 토큰을 만든다. 궤적 토큰은 activity, direction, distance의 지도 학습으로 시간 정보를 유지한다. 오른쪽 QA 경로에서는 고정 ST-Audio Encoder가 의미 토큰 하나와 dynamic trajectory 토큰을 내보내고, 학습 가능한 두 층 MLP connector와 LoRA가 이를 언어 입력에 연결한다.
[해석 범위]
이 구조도는 방법을 설명하며 실제 움직임 예측 성공의 근거를 대신하지 않는다. 정적 encoder를 시간 구간별로 반복 적용하는 것과 궤적 지도 학습을 같은 방법으로 그리지 않는다. encoder Table 3와 실제 녹음 적응 결과는 다음 조합 QA 평가와 별개다.
-->

---
layout: "seminar"
variant: "result"
chapter: "05 · 2025–2026: 정적 위치에서 이동과 시간 관계로"
causalStage: "main"
originSlide: 64
---

# ST-AudioLM: 같은 41개 토큰에서도 시간 표현이 다르다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">ST-AudioQA Type C · FOA, OLMo2, 41-token 인터페이스 · controlled-answer accuracy (0–100) ↑</p>
<PaperFigure src="/diagrams/result-64.svg" alt="시간 관계
Temp. rel., 이동 조건
Move-spat., 궤적 관계
Traj. rel., 평균 원문 수치 비교 그래프. Spatial-AST-FOA + OLMo2: 80.4, 55.2, 54.3, 63.3; ST-AudioLM: 86.0, 55.8, 60.6, 67.5" />
</div>

::takeaway::
같은 41-token 인터페이스에서도 **시간 구조를 배운 표현**의 평균 성과가 달랐다.

::source::
ST-AudioLM, arXiv:2606.14141v1, Table 5. ↑ 높을수록 좋음.

<!--
[현재 S41 · 본문]
05 · 2025–2026: 정적 위치에서 이동과 시간 관계로

[설명의 중심]
같은 FOA·OLMo2·41-token 인터페이스 비교에서 encoder의 시간 구조 차이를 본다. connector 하나의 효과로 귀속하지 않는다.

[연결]
다음에 확인할 질문: H의 정보 접근성, Z의 전달, 답변의 오디오 의존을 서로 다른 관측·개입으로 시험한다.

[상세 근거와 해석 범위]
[S41]
[Sources]
- https://arxiv.org/html/2606.14141v1
[발표 노트]
같은 FOA 계열 입력과 OLMo2, 41-token 인터페이스를 사용하는 QA 학습 비교다. baseline은 정적 FOA encoder, ST-AudioLM은 궤적 지도를 학습한 표현을 사용한다. 평균은 63.3에서 67.5로 높아진다. 그러나 ST-AudioLM의 시간 관계 86.0에 비해 이동 조건 관계는 55.8, 두 음원 궤적 관계는 60.6이다. 평균만 보면 남는 난도를 놓칠 수 있다.
[해석 범위]
값은 통제된 답 형식의 0–100 정확도다. 모든 encoder 지표 우세나 밀집한 현실 장면의 해결을 뜻하지 않는다. BAT는 같은 scene metadata를 바이노럴로 렌더링해 받으므로 동일 입력 ablation이 아니다. Table 4 기본·두 음원 QA와 Table 3 encoder 및 실제 녹음 적응은 각각 따로 읽는다.

[시각화 전 표의 수치·조건 보존]
ST-AudioQA Type C · FOA, OLMo2, 41-token 인터페이스 · controlled-answer accuracy (0–100) ↑

QA 학습 모델 | 시간 관계 / Temp. rel. | 이동 조건 / Move-spat. | 궤적 관계 / Traj. rel. | 평균 | 

Spatial-AST-FOA / + OLMo2 | 80.4 | 55.2 | 54.3 | 63.3 | 

ST-AudioLM | 86.0 | 55.8 | 60.6 | 67.5 |
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "06 · 표현에서 답변까지 무엇을 확인해야 하나"
causalStage: "main"
---

# 읽히는 정보가 답에도 쓰이는가?

::body::
<PaperFigure src="/diagrams/causal-evaluation-map.svg" alt="입력 X, 인코더 E의 H, projector P의 Z, LLM과 답으로 이어지는 공통 관측 지도. SARL 판독은 H, BMLD 자극 반응은 X에서 H, Spatial-Omni zero 기준선은 공간 token 인터페이스, BAT 질문만 조건은 X 없이 Q에 배치한다. 주황 점선은 token 치환·복구와 오디오 짝 비교의 미실행 제안이다." caption="각 문헌의 관측 위치를 겹쳐 그린 지도. E: 인코더 · P: adapter · Q: 질문." />

::takeaway::
<strong>판독, 자극 반응, token 비교, 답변 변화</strong>는 서로 다른 증거다.

::source::
SARL v2 §3 · BMLD v1 §2 · Spatial-Omni v2 §5.3·App. E · BAT v4 Table 4.

<!--
[현재 S42 · 본문]
06 · 표현에서 답변까지 무엇을 확인해야 하나

[설명의 중심]
H의 정보 접근성, Z의 전달, 답변의 오디오 의존을 서로 다른 관측·개입으로 시험한다.

[연결]
다음에 확인할 질문: 문장으로만 넘기면 공간 단서가 얼마나 남는가?

[상세 근거와 해석 범위]
[Bridge: causal-evaluation]
[Sources]
- https://arxiv.org/html/2606.05544v2
- https://arxiv.org/html/2606.14820v1
- https://arxiv.org/html/2606.10738v2
- https://arxiv.org/html/2402.01591v4
- https://arxiv.org/html/2510.24693v2
- https://arxiv.org/html/2601.02391v1
- https://aclanthology.org/2021.tacl-1.10/
- https://aclanthology.org/2025.findings-acl.674/
[청중 질문]
표현의 정보를 읽는 것과 모델이 실제 답변에 사용하는 것을 어떻게 구분하는가?
[발표 노트]
이 그림은 한 모델의 구조도가 아니다. 서로 다른 모델·실험을 공통 X→E(H)→P(Z)→L(Z,Q)→답 좌표에 놓은 관측 지도다. 파랑은 보고된 관측 위치이고 주황 점선은 후속 제안이다. latent cell과 선형 판독 산점은 모식도이며 측정 결과가 아니다.
SARL Fig. 2는 고정 H의 선형 판독이고 Fig. 3의 source/room 변화 민감도와 구분한다. 둘 다 LLM이 해당 정보를 소비했는지는 검사하지 않는다. BMLD는 X의 표적 위상을 바꾼 뒤 H의 거리비 반응을 읽는다. 그림의 두 sinusoid는 표적 위상의 설명용 표시이고, 실제 자극은 같은 잡음 n으로 N0=(n,n), S0N0=(n+s,n+s), SπN0=(n+s,n−s)를 구성한다. 오른쪽 혼합음 전체가 뒤집히는 것이 아니다. 이는 인간 탐지 역치나 QA 점수가 아니다.
Spatial-Omni v2 §5.3은 SO-7B-zs가 zero spatial tokens를 사용한다고, Appendix E의 baseline 설명은 null spatial token을 LLM에 공급한다고 쓴다. 학습부터 zero인지 추론 시만 zero인지, SO-7B와 동일 checkpoint인지 명시하지 않는다. 따라서 ‘zero 기준선’으로만 표현하며 고정 checkpoint token 제거 실험으로 단정하지 않는다.
BAT Table 4 P는 실제 질문만 조건이다. 그림의 X→LLM 경로는 일반 오디오+질문 흐름이며 BAT P 조건에서는 X가 제외된다. STAR-Bench Table 2의 기준은 Random Guess이므로 STAR를 question-only 실험이라 부르지 않는다. STAR의 caption 대조 역시 질문만 조건이 아니다. WearVox는 전체 SLLM의 실녹음 검증으로, E만의 향상이나 특정 phase 사용을 직접 보여주지 않는다.
[주황 점선: 미실행 제안]
동일 checkpoint에서 Z를 위치가 다른 짝의 토큰으로 치환하고 정상 token으로 복구한다. 공간 관련 token 제거, 같은 수의 무작위 token 제거, 길이·norm·분포 대조를 함께 설계한다. 다른 의미 task까지 무너지는 일반 손상과 구분한다. H와 Z를 동일 probe로 판독하면 경계를 지나는 정보의 접근 가능성도 비교할 수 있다.
오디오 짝 비교는 같은 질문에서 위치 A·B의 정답이 각각 달라지는 쌍을 둘 다 맞히는지 확인한다. 단순히 답이 달라지는 것은 성공이 아니다. 새 수치를 만들지 않았고 어떠한 제안 실험도 수행했다고 주장하지 않는다.
[해석 범위]
probe 성능, cue sensitivity, LLM의 정보 사용을 같은 지표로 합치지 않는다. 다른 논문의 결과를 한 시스템이 통과한 보장 사다리로 그리지 않는다. 언어 분야의 amnesic probing은 실험 설계의 방법론적 참고이며 공간 오디오에서 검증된 결과가 아니다.
-->

---
layout: "seminar"
variant: "method"
chapter: "06 · 표현에서 답변까지 무엇을 확인해야 하나"
causalStage: "main"
originSlide: 68
---

# 문장으로만 넘기면 공간 단서가 얼마나 남는가?

::body::
<PaperFigure src="/research/star-caption-panel.png" alt="STAR-Bench의 청각 입력과 텍스트 캡션 기반 추론 비교" caption="STAR-Bench Fig. 1의 audio/caption 비교 패널." />

::aside::
<section><span class="seminar-label">문장에 남은 정보</span><p>소리 · 사건</p></section><section><span class="seminar-label">따로 확인할 정보</span><p>방향 · 미세한 시간 관계</p></section>

::takeaway::
평가하려는 단서가 <strong>설명문에 보존되는지</strong>부터 확인한다.

::source::
STAR-Bench, arXiv:2510.24693v2, Fig. 1 관련 패널 크롭.

<!--
[현재 S43 · 본문]
06 · 표현에서 답변까지 무엇을 확인해야 하나

[설명의 중심]
STAR의 caption 분석은 audio→text 중간 경로가 무엇을 놓칠 수 있는지 보여 준다. 모든 adapter의 token bottleneck 측정으로 일반화하지 않는다.

[연결]
다음에 확인할 질문: 같은 표현에서도 속성마다 읽히는 정도가 다르다

[상세 근거와 해석 범위]
[S43]
[Sources]
- https://arxiv.org/html/2510.24693v2
[청중 질문]
‘말소리와 알람이 있다’는 문장만 받았을 때도 방향·미세한 시간 질문에 답할 수 있는가?
[발표 노트]
원음을 듣는 조건과 문장으로 전달받는 조건을 읽는다. 문장에 남은 내용, 사라진 공간·시간 정보를 가른다. 설명의 충분성과 모델 능력을 동시에 바꾸면 원인을 하나로 정할 수 없음을 설명한다.
캡션 비교는 특정 채널이나 위상 단서만 제거하는 통제가 아니다. 설명의 정보량과 모델의 능력이 함께 바뀌므로 점수 차이를 한 음향 기전의 효과로 해석하지 않는다.
[해석 범위]
캡션은 무음·채널 위상 제거와 같은 통제가 아니다. 모든 문장은 공간 정보를 잃는다는 주장도 하지 않는다. 도입 알람 장면을 쓸 경우 ‘발표자 설명용’으로 표시한다.
[시각화 전 상세 본문 — 발표 설명용 보존]
STAR-Bench Fig. 1의 audio/caption 비교 패널.


[보조 설명]
설명문에 남은 것어떤 소리가 있었는지
어떤 사건을 기술했는지

따로 확인할 것방향과 미세한 시간 관계가
문장에도 보존됐는가?


[핵심 결론]
평가하려는 단서가 설명문에 보존되는지부터 확인한다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "06 · 표현에서 답변까지 무엇을 확인해야 하나"
causalStage: "main"
originSlide: 73
---

# 같은 표현에서도 속성마다 읽히는 정도가 다르다

::body::
<PaperFigure src="/research/sarl-summary.svg" alt="SARL에서 사건 의미, 위치, 방 특성의 정규화 접근성을 비교한 원문 막대그래프" ><template #caption>의미 · 위치 · 방의 정규화 판독 점수. 원문 축과 요인 범례 유지.</template></PaperFigure>

::takeaway::
고정 인코더의 **같은 판독 규칙**으로 의미·위치·방 정보의 접근성을 비교한다.

::source::
SARL, arXiv:2606.05544v2, Fig. 2. 민감도의 정의는 Fig. 3과 구별.

<!--
[현재 S44 · 본문]
06 · 표현에서 답변까지 무엇을 확인해야 하나

[설명의 중심]
SARL Fig. 2는 고정 표현에서 사건·위치·방 요인이 얼마나 읽히는지 비교한다. 입력 변화 민감도와의 구별은 별도 정의이며 이 한 그림이 두 지표를 직접 비교하는 것은 아니다.

[연결]
다음에 확인할 질문: 같은 잡음에서 표적 위상을 바꾸고 표현을 읽는다

[상세 근거와 해석 범위]
[S44]
[Sources]
- https://arxiv.org/html/2606.05544v2
[청중 질문]
입력 변화에 표현이 크게 움직이면 그 속성을 정확히 읽을 수 있는가?
[발표 노트]
우연 기준과 요인 그룹을 먼저 읽고, 같은 표현도 무엇을 읽느냐에 따라 결과가 달라짐을 설명한다. 이어 perturbation distance는 목표 라벨을 판독한 점수가 아니라는 차이를 묻는다.
먼저 정규화의 무작위 기준과 세 그룹을 읽는다. source의 전체 평균을 순수 위치 점수라고 부르지 않는다. 입력과 학습 데이터가 다른 모델들을 학습 목표 하나의 ablation처럼 비교하지 않는다. Fig. 3의 perturbation distance는 라벨을 판독한 점수와 다르며, 이 연구에서 시험하지 않은 공간 LLM의 실패를 주장하지 않는다.
[해석 범위]
서로 다른 mono/binaural/FOA 모델 비교는 학습 목표 하나의 통제가 아니다. 전체 source 평균을 순수 위치 성능이라 부르지 않는다. 이 연구가 시험하지 않은 공간 LLM을 실패 칸에 넣지 않는다.
[시각화 전 상세 본문 — 발표 설명용 보존]
의미 / 위치(방위·고도·거리) / 방( \mathrm{RT}_{60} ·부피·형상). 원문 정규화 축과 입력 범례 유지.

[핵심 결론]
입력 변화에 대한 민감도와 목표 요인의 판독 가능성은 같은 측정이 아니다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "06 · 표현에서 답변까지 무엇을 확인해야 하나"
causalStage: "main"
originSlide: 74
---

# 같은 잡음에서 표적 위상을 바꾸고 표현을 읽는다

::body::
<PaperFigure src="/diagrams/p3-bmld-stimulus-waveforms.svg" alt="동일한 잡음을 공유한 두 채널의 파형. 잡음만, 양쪽 n+s, 왼쪽 n+s와 오른쪽 n-s 조건을 비교하고 잡음 기준 표현 거리비를 측정한다" caption="설명용 합성 파형(시간·진폭 임의 단위) · 고정 인코더 · final-block 평균 pooling" />

::takeaway::
측정값은 <strong>잡음 기준 임베딩 거리비</strong>이며, 인간의 탐지 역치와 구별한다.

::source::
Interference/BMLD, arXiv:2606.14820v1, §2 자극 정의 재구성.

<!--
[현재 S45 · 본문]
06 · 표현에서 답변까지 무엇을 확인해야 하나

[설명의 중심]
BMLD는 같은 noise를 유지하며 오른쪽 target 위상만 반전한다. 입력 개입의 해석 가능한 사례다.

[연결]
다음에 확인할 질문: 표현의 단서 반응은 LLM의 답변 사용과 다르다

[상세 근거와 해석 범위]
[S45]
[Sources]
- https://arxiv.org/html/2606.14820v1
[청중 질문]
잡음 속 순음의 양이 위상 관계가 달라지면 고정 표현도 다르게 반응하는가?
[발표 노트]
noise-only 기준을 제시하고 동위상/역위상 표적을 더한다. 고정 인코더와 pooling을 통과한 후 두 표적 조건이 noise 표현에서 얼마나 떨어지는지 비교한다. 거리 비에 로그를 취한 값이 연구의 BMLD 유사 지표임을 설명한다.
n은 두 귀와 조건들에서 공유하는 동일 잡음, s는 표적 순음이다. 지표는 20 log10[d(antiphase,noise)/d(diotic,noise)]다. 양의 값은 역위상 표적 조건이 이 표현에서 기준 잡음과 더 멀어졌음을 뜻한다. phase flip은 오른쪽 혼합의 파형·간섭 무늬도 함께 바꾸므로 인코더 내부의 위상 비교만 조작한 실험은 아니다.
[해석 범위]
표적의 위상을 바꾸면 오른쪽 혼합 파형과 간섭 무늬도 달라진다. 단일 조작이 내부 위상 비교만 바꾸는 것은 아니다. 사람의 dB threshold 및 EC 모델 기준과 임베딩 거리비를 같은 성능 척도로 등치하지 않는다.
[시각화 전 상세 본문 — 발표 설명용 보존]
자극 | 왼쪽 채널 | 오른쪽 채널 | 
N_0  · 기준 |  n  |  n  | 
S_0N_0  · 동위상 |  s + n  |  s + n  | 
S_{\pi}N_0  · 역위상 |  s + n  |  -s + n  | 
같은 noise seed · 고정 인코더 · final-block 평균 pooling


[핵심 결론]
측정값은 noise 기준 임베딩 거리의 비이며, 인간의 탐지 역치와 구별한다.
-->

---
layout: "seminar"
variant: "result"
chapter: "06 · 표현에서 답변까지 무엇을 확인해야 하나"
causalStage: "main"
originSlide: 75
---

# 표현의 단서 반응은 LLM의 답변 사용과 다르다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">500 Hz · SNR −14 dB · 고정 인코더, 모델별 전처리 · 100 seeds/cell</p>
<PaperFigure src="/diagrams/result-75.svg" alt="표현 거리비 지표 (dB) 원문 수치 비교 그래프. Spatial-AST: 6.8*; DSpAST: 7.0*; GRAM-T: 2.1*; WavJEPA: 0.5*" />
<p class="seminar-chart-note">* 원표의 FDR 보정 표시(<MathInline tex="q=0.05" />) · 양수: 역위상 조건의 표현 거리가 더 큼</p>
</div>

::takeaway::
이 표현 거리 반응만으로 **LLM이 같은 단서를 사용한다**고 말할 수는 없다.

::source::
Interference/BMLD, arXiv:2606.14820v1, Table 1·§2.3. 원문 수치·별표 유지.

<!--
[현재 S46 · 본문]
06 · 표현에서 답변까지 무엇을 확인해야 하나

[설명의 중심]
임베딩 거리비 반응을 확인해도 인간 역치나 최종 LLM의 공간 추론이 증명되지는 않는다.

[연결]
다음에 확인할 질문: 현장 응답 대상은 전체 시스템으로 검증한다

[상세 근거와 해석 범위]
[S46]
[Sources]
- https://arxiv.org/html/2606.14820v1
[청중 질문]
모델별 양의 반응이 보이면 모두 사람처럼 잡음 속 소리를 더 잘 듣는가?
[발표 노트]
S45의 두 거리를 회수하고 양수/음수의 뜻을 설명한다. 선택 모델들의 반응을 같은 자극에서 읽되 내부 전처리는 다름을 표시한다. 왼쪽 채널만 쓰는 mono 대조군은 입력이 변하지 않아 구성상0이라는 점을 말한다.
Table 1의 네 값과 별표를 보존했다. 원문은 sign-flip permutation을 5,000회 이상 수행하고 Benjamini–Hochberg FDR 보정을 적용한다. 95% bootstrap CI는 2,000회 이상 resampling으로 구한다. 단일채널 대조는 왼쪽 입력이 동일하여 구성상 0이며, EC=15.7 dB는 인간 실측 역치가 아닌 분석적 참조다. 한 주파수·SNR를 모든 자극이나 자연 장면으로 확대하지 않는다.
[해석 범위]
EC=15.7을 인간 실측 역치나 모델의 목표 정답으로 제시하지 않는다. 한 조건의 값으로 주파수 전역 일반화를 하지 않는다. 전체 모델/주파수 곡선과 pooling 비교는 원문의 추가 자료으로 보낸다.

[시각화 전 표의 수치·조건 보존]
500 Hz · SNR −14 dB · 고정 인코더, 모델별 전처리 · 100 seeds/cell인코더 | 표현 거리비 지표 (dB) | 
Spatial-AST | 6.8* | 
DSpAST | 7.0* | 
GRAM-T | 2.1* | 
WavJEPA | 0.5* | 
* 원표의 FDR 보정 유의성 표시($q=0.05$). 양수는 역위상 조건의 거리가 더 큼.
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->

---
layout: "seminar"
variant: "result"
chapter: "06 · 표현에서 답변까지 무엇을 확인해야 하나"
causalStage: "main"
originSlide: 71
---

# 현장 응답 대상은 전체 시스템으로 검증한다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">기기에게 건넨 말인가? · WearVox · Side Talk Rejection 정확도 (%) ↑</p>
<PaperFigure src="/diagrams/result-71.svg" alt="Side Talk Rejection 정확도 (%) ↑ 원문 수치 비교 그래프. SC · beamformed: 85.4; MC · 채널 0 + beamformed: 93.9" />
<p class="seminar-chart-note">MC는 두 채널을 interleave · 원시 전체 배열의 동시 입력은 아님</p>
</div>

::takeaway::
이 <strong>추가 채널·시스템 학습 조건</strong>에서 실제 응답 대상 판단이 개선됐다.

::source::
WearVox, arXiv:2601.02391v1, Fig. 2·Table 4. 원표의 85.4를 채택.

<!--
[현재 S47 · 본문]
06 · 표현에서 답변까지 무엇을 확인해야 하나

[설명의 중심]
WearVox의 SC/MC 비교는 실환경 시스템의 응답 대상 판단이다. 채널 구성 외 설정과 실제 자료 조건도 함께 읽는다.

[연결]
다음에 확인할 질문: 연구사의 공통 질문은 공간 정보가 어디서 사라지는가다

[상세 근거와 해석 범위]
[S47]
[Sources]
- https://arxiv.org/html/2601.02391v1
[청중 질문]
이 논문의 ‘다채널’은 어떤 신호를 더 받는다는 뜻인가?
[발표 노트]
Fig. 2를 근거로 입력 차이를 말로 설명한 다음 표를 읽는다. 합성 다채널 학습과 실제 WearVox 시험을 구별한다. 같은 종류의 질문에서 추가 채널·시스템 구성이 어떤 이득을 보고했는지 한정한다.
음성 인코더를 고정하고 projection과 언어 모델을 학습한다. 실측 RIR을 활용한 합성 다채널 학습과 실제 착용자 시험을 구분한다. 채널0의 SNR, beamforming, 학습 조건이 함께 바뀌므로 위상만의 효과로 분리한 통제가 아니다. 서론의 85.6 대신 Table 4의 85.4를 사용했다.
[해석 범위]
모든 원시 마이크 채널의 동시 입력으로 그리지 않는다. 채널0의 SNR·beamforming·학습 변경이 함께 있으므로 phase-only 통제가 아니다. 초록/서론의 85.6이 아니라 Table 4의 85.4를 사용한다. 다른 응용 과제는 원문의 추가 자료 밖 참고로 남긴다.

[시각화 전 표의 수치·조건 보존]
실제 WearVox 시험 · Side Talk Rejection 정확도 (%) ↑입력·시스템 | 정확도 | 
SC · beamformed 채널 | 85.4 | 
MC · 채널 0 + beamformed | 93.9 | 
MC는 두 채널을 interleave한다. 원시 전체 배열의 동시 입력은 아니다.
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "06 · 표현에서 답변까지 무엇을 확인해야 하나"
causalStage: "main"
---

# 연구사의 공통 질문은 공간 정보가 어디서 사라지는가다

::body::
<table class="seminar-compact" style="font-size:24px;line-height:1.3">
<colgroup><col style="width:36%"/><col style="width:38%"/><col style="width:26%"/></colgroup>
<thead><tr><th>연구에서 바뀐 질문</th><th>정보가 넘어가는 경계</th><th>필요한 확인</th></tr></thead>
<tbody>
<tr><th scope="row">BAT: 위치에서 관계 질문으로</th><td>E → P → LM</td><td>질문만 / 오디오 추가</td></tr>
<tr><th scope="row">DSpAST · OWL: 무엇을 배울까</th><td>물리 단서·기하 지도 → E</td><td>E 판독과 QA 구분</td></tr>
<tr><th scope="row">Motion: 예측을 언어로 넘길까</th><td>속성 시계열 → JSON → LM</td><td>예측 오류·정보 누락</td></tr>
<tr><th scope="row">기존 Audio-LM: 공간을 더할까</th><td>의미 + 공간 → P → LM</td><td>공간 기여·의미 능력</td></tr>
<tr><th scope="row">Dynamic · ST: 이동을 묻는다면</th><td>사건·시간·음원 → 토큰</td><td>시간·정체성 결속</td></tr>
</tbody>
</table>

::takeaway::
각 논문을 **무엇을 남기고, 무엇을 넘기며, 답에 무엇을 쓰게 했는가**로 연결해 읽는다.

::source::
27편의 설계·평가 종합 · 연구사와 명시적 계승 근거는 발표 노트 및 근거 부록.

<!--
[현재 S48 · 본문]
06 · 표현에서 답변까지 무엇을 확인해야 하나

[설명의 중심]
BAT의 QA 연결, DSpAST·OWL의 공간 인코더, Motion의 구조화 언어 전달, 기존 Audio-LM의 공간 확장, 동적 장면 토큰이라는 문제 변화를 인코더·연결·언어 사용의 평가 기준으로 회수한다.

[연결]
다음에 확인할 질문: 같은 공간 장면을 유지한 통제 실험으로 H→Z→답의 연결을 확인하는 다음 연구 질문을 제안한다.

[상세 근거와 해석 범위]
[Sources]
- https://arxiv.org/html/2402.01591v1
- https://arxiv.org/html/2509.13927v1
- https://arxiv.org/html/2509.26140v1
- https://arxiv.org/html/2509.14666v1
- https://arxiv.org/html/2510.05542v1
- https://arxiv.org/html/2606.14141v1

[그림]
이 표는 원문 Methods에 근거한 연구 질문과 평가 기준의 정리다. PPT에서도 native table로 내보낸다. 최초 공개 연대와 채택 버전은 plans/MC_AUDIO_LM_HISTORY.md에 구분하여 기록했다. 화살표는 그림 내부의 데이터 흐름이며 논문 간 성능 상승을 뜻하지 않는다.

[연구사와 발표 노트]
공간 신호처리에서는 지연 관계를 후보 좌표의 응답으로 바꾸고 합산했다. Neural-SRP는 그 쌍별 응답 생성기를 학습하되 합산과 좌표 선택을 유지했다. 다음 단계는 이 출력 좌표만으로 사건·시간·관계 질문에 충분한가이다.
BAT는 공간 속성을 학습한 encoder의 표현을 언어 질문에 연결했다. DSpAST와 OWL은 같은 틀의 표현 사전학습과 입력 단서를 다시 설계했다. Motion은 명시적인 예측 속성 언어화를 통해 별도 추론 LM과 연결하는 다른 선택이다. Sci-Phi·PhaseCoder·Spatial-Omni·TWNM은 이미 풍부한 의미·음성 경로가 있는 모델에 공간 경로를 더하면서 결속, 배열 조건, 이식과 학습을 묻는다. Dynamic QA·ST-AudioLM에서는 표현의 시간 구조가 새로운 요구가 된다.
이러한 문제의 확대가 인코더·연결부·LM의 평가 기준을 정한다. E의 고정 판독에 공간 정보가 읽힌다는 사실만으로 LM이 그것을 쓴다고 보장하지 않는다. JSON과 연속 token의 전달 범위, 질문만 기준선과 오디오 입력의 차이, 단서 개입에 따른 답의 변화, 기존 능력 보존을 구분한다. 마지막 장은 동일 장면의 H→Z/JSON→답을 함께 검사하는 앞으로의 실험 제안이며 이번 작업에서 수행한 모델 실험이 아니다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "06 · 표현에서 답변까지 무엇을 확인해야 하나"
causalStage: "main"
---

# 같은 장면에서 표현·토큰·답을 함께 검사한다

::body::
<PaperFigure src="/diagrams/causal-closing-tests.svg" alt="x축 위 두 마이크 M1과 M2의 중점 O를 원점으로 알람 A의 방위각 alpha, 고도각 beta, 거리 r를 정의한다. 같은 알람의 위치를 B로 옮긴 후 H와 Z에서 같은 판독기로 좌표를 읽고 LLM의 두 답을 정답 A와 B에 각각 대조하는 미실행 제안이다." caption="후속 실험 제안. 같은 모델·질문에서 알람만 이동하고 말소리는 유지한다." />

::takeaway::
<strong>좌표가 남고, token에 전달되고, 그 변화가 올바른 답으로 이어지는지</strong> 확인한다.

::source::
문헌 종합 기반 실험 제안 · SARL/BMLD/Spatial-Omni/BAT의 관측 범위를 구분.

<!--
[현재 S49 · 본문]
06 · 표현에서 답변까지 무엇을 확인해야 하나

[설명의 중심]
같은 공간 장면을 유지한 통제 실험으로 H→Z→답의 연결을 확인하는 다음 연구 질문을 제안한다.

[연결]
본문은 여기서 마친다. 다음 장부터는 질문별 근거 부록이며 필요한 비교를 선택해 열어 본다.

[상세 근거와 해석 범위]
[Bridge: closing-tests]
[Sources]
- https://arxiv.org/html/2606.05544v2
- https://arxiv.org/html/2606.14820v1
- https://arxiv.org/html/2606.10738v2
- https://arxiv.org/html/2402.01591v4
- https://aclanthology.org/2021.tacl-1.10/
[청중 질문]
다음에 하나의 시스템에서 어떤 세 가지 시험을 연결해야 하는가?
[발표 노트]
후속 실험 제안이며 결과는 없다. 왼쪽은 발표 도입의 동일한 알람·말소리 장면이다. 두 마이크는 x축 위 −d/2와 +d/2에 놓이며 중점 O가 원점이다. 방위각 α는 +x에서 +y 방향의 수평 회전, 고도각 β는 xy면에서 +z 방향, r은 O에서 알람까지의 거리다. 파란 A와 주황 B는 같은 알람의 서로 다른 위치이며 실제 예측 결과나 수치가 아니다.
1) 같은 encoder checkpoint의 H에서 각 좌표와 의미를 읽는다. 2) 같은 판독 조건을 adapter 뒤 Z에도 적용한다. 3) 질문을 고정하고 오디오 위치만 바꾼 쌍의 두 답을 모두 정답과 대조한다. ‘무슨 소리인가’라는 의미 질의는 그대로 유지돼야 한다. H·Z의 블록 색은 설명용이며 실측 임베딩이 아니다.
이후 Z 치환·제거와 정상 token 복구, 동일 예산의 무작위 제거, 질문만 및 오디오 치환 대조를 추가하면 단순 정보 존재와 실제 사용을 더 구분할 수 있다. probe가 높지만 답이 틀리면 과제 정렬·정보 사용을 의심할 수 있으나 원인을 확정하지 않는다. 새 방·배열·실녹음 전이와 원래 의미 성능을 별도로 검증한다.
[해석 범위]
두 마이크의 한 TDOA만으로 α·β·r가 유일하게 결정된다고 주장하지 않는다. 필요한 정보는 배열/입력/학습 조건에서 식별 가능한지 먼저 정해야 한다. 타 논문의 세 결과를 이어 한 모델의 충분조건이 증명됐다는 결론으로 만들지 않는다. 단서 반응은 사람 역치가 아니며, 선형 probe 성공은 LLM의 사용을 보장하지 않는다.
[마지막 말]
목표는 좋은 답 하나가 아니라, 어떤 공간 정보가 어디까지 남고 어떤 답에 쓰이는지 관찰 가능한 공간 표현이다.
-->


---
layout: "seminar-section"
chapter: "근거 부록"
causalStage: "appendix"
---

# 근거 부록

::context::
본문의 질문을 더 자세히 확인할 때

::bridge::
A 관측과 인코더 · B 의미와 공간의 정렬<br/>
C 공간 Audio-LM의 세부 설계 · D 시간 정보의 전달 · E 답변의 근거

::source::
27편의 지정 원문 버전 · 실험 조건·수치·반례를 보존한 선택 자료

<!--
[현재 S50 · 근거 부록]
근거 부록

[설명의 중심]
본문은 49장에서 마쳤으며 이후는 질문에 따라 선택해 보는 상세 근거다.

[연결]
이 장은 본문의 근거 부록 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[근거 부록의 사용]
본문은 앞의 49장에서 마쳤다. 이 부록은 논문을 순서대로 추가 발표하기 위한 두 번째 본문이 아니다. 질문이 나오면 해당 설계 경계나 검증 조건으로 이동해 필요한 그림·표를 확인한다. 다섯 구역은 관측과 인코더, 의미와 공간 결속, 토큰으로 보내는 관측, 시간 정보 전달, 답변의 근거다. 장 번호와 논문별 연결은 CAUSAL_DECK_ORDER와 본문 근거 대장에 기록한다. 모든 수치는 기존 지정 원문의 조건에 한정한다. 설명용 범위·발표자 정리.
-->

---
layout: "seminar"
variant: "figure"
chapter: "근거 부록 A · 관측과 인코더"
causalStage: "appendix"
originSlide: 29
---

# 사전학습 목표와 표현의 재사용 시험을 분리한다

::body::
<PaperFigure src="/diagrams/p1-pretrain-probe.svg" alt="마스킹 복원 사전학습 인코더를 고정한 뒤 새 과제 정답으로 판독기를 학습하는 두 단계 프로토콜" caption="고정 판독 프로토콜 · 실녹음 전체 미세조정은 별도 평가" />

::takeaway::
**마스킹은 학습 목표**, 고정 인코더의 여러 과제 판독은 **재사용을 확인하는 시험**이다.

::source::
GRAM, arXiv:2506.00934v5, Fig. 1·HEAR 평가 프로토콜 기반 재구성.

<!--
[현재 S51 · 근거 부록]
근거 부록 A · 관측과 인코더

[설명의 중심]
GRAM은 마스킹 목표를 수행한 뒤 고정 표현으로 여러 출력을 판독한다. 학습 손실을 정보 보존의 직접 지표로 대신하지 않는다.

[연결]
이 장은 본문의 A · 관측과 인코더 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S51 발표 노트]
[설명 순서]
“사전학습에서 모델이 받는 과제와 후속 평가에서 판독기가 받는 정답은 다릅니다. 고정 특징 평가를 중심으로 읽되, 원문에 있는 전체 미세조정 비교는 별도 조건으로 구분하겠습니다.”

[경계·원문의 추가 자료]
모든 보고 결과가 고정 인코더라고 단정하지 않는다. 판독기의 용량과 학습 데이터량을 함께 기록하고 마스킹 세부 구현은 원문의 추가 자료으로 보낸다.


사전학습은 마스킹 autoencoding을 사용한다. Ambisonics는 4채널 mel 및 intensity vector, binaural은 두 귀의 mel을 다룬다. HEAR 방식에서 고정 인코더와 지도 판독기를 사용한다.
[Sources]
- https://arxiv.org/html/2506.00934v5

[시각화 전 본문 설명]
마스킹 사전학습
가린 관측을 예측하며 인코더 학습
고정 표현 추출
후속 과제에서 인코더 가중치 고정
라벨을 쓰는 판독
과제별 판독기 학습 → 방향 등 출력
입력 변형
Binaural / Ambisonics / Clean
따로 읽을 결과
실녹음 전체 미세조정은 별도의 평가

[설명 그림의 범위]
발표자 제작 SVG. 개념의 관계를 읽기 위한 도식이며 원문의 실험 관측이나 모델 추정값을 그린 결과가 아니다.
교육 참고: Dive into Deep Learning §14.2 Fine-Tuning, pretrained features와 새 출력층의 구별 및 고정 특징 평가. 각 논문의 프로토콜은 기존 출처와 노트가 기준이다.
- https://d2l.ai/chapter_computer-vision/fine-tuning.html
-->

---
layout: "seminar"
variant: "method"
chapter: "근거 부록 A · 관측과 인코더"
causalStage: "appendix"
originSlide: 25
---

# 공간 단서를 목표로 배운 초기화는 잡음에서 시험한다

::body::
<PaperFigure src="/research/sfd-1h-plot.svg" alt="SFD Fig. 2의 1시간 라벨 조건. x축 SNR dB, y축 DOA MAE 도. 원본 곡선과 축을 보존한 패널" />

::aside::
<section>
<span class="seminar-label">1시간 라벨 · 전체 미세조정</span>
<div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;font-size:20px"><span style="width:26px;border-top:3px solid #0072b2;flex:none"></span><span>GCC-PHAT-DNN</span></div><div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;font-size:20px"><span style="width:26px;border-top:3px solid #d55e00;flex:none"></span><span>GCC-DNN</span></div><div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;font-size:20px"><span style="width:26px;border-top:3px solid #009e73;flex:none"></span><span>STFT-DNN</span></div><div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;font-size:20px"><span style="width:26px;border-top:3px solid #f0e442;flex:none"></span><span>SFD-CPSPhase</span></div><div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;font-size:20px"><span style="width:26px;border-top:3px solid #cc79a7;flex:none"></span><span>SFD-GCC</span></div><div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;font-size:20px"><span style="width:26px;border-top:3px solid #999999;flex:none"></span><span>SFD-GCC-PHAT</span></div><div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;font-size:20px"><span style="width:26px;border-top:3px solid #56b4e9;flex:none"></span><span>SFD-ILD+IPD</span></div><p style="font-size:20px;margin-top:16px">x: SNR (dB)<br/>y: DOA MAE (°), 낮을수록 좋음</p>
</section>

::takeaway::
이 결과는 **공간 특징 사전학습 후 전체 미세조정**의 근거다. 고정 표현 판독과는 다르다.

::source::
SFD, arXiv:2508.20914v1, Fig. 2의 1h 패널. 원본 벡터 크롭·범례 재배치.

<!--
[현재 S52 · 근거 부록]
근거 부록 A · 관측과 인코더

[설명의 중심]
SFD는 clean 공간 특징 목표를 쓰지만 이 그림의 성과는 저라벨 전체 미세조정 조건이다. 앞의 frozen probe와 구별한다.

[연결]
이 장은 본문의 A · 관측과 인코더 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S52 발표 노트]
[설명 순서]
“여기서는 라벨 시간과 백본을 맞추고 초기화만 비교하겠습니다. 사전학습 이후 인코더도 DOA에 맞춰 바뀌므로, 이 결과는 적응에 유용한 초기 표현의 증거로 읽어야 합니다.”

[경계·원문의 추가 자료]
Table 2의 1시간·10시간 표기 충돌 때문에 그 표는 사용하지 않는다. 10분 패널과 다른 변형은 원문의 추가 자료이며 서로 다른 데이터 조건의 수치를 섞지 않는다.


주비교는 STFT-DNN(녹색)과 SFD-CPSPhase(노랑). 두 모델은 STFT 입력, 545k 파라미터와 1시간 라벨 학습량을 공유한다. SFD는 LibriSpeech 원음 960시간 기반 사전학습을 추가로 사용하고 인코더와 DOA head를 함께 미세조정한다. 단일 정지 음성·합성 바이노럴, HRTF 피험자 분리. 평가 잡음은 학습과 같은 종류의 다른 클립. 원래 나머지 곡선과 범례를 보존했다. 곡선으로 정밀 수치를 만들지 않는다. Table 2의 caption 1h/본문10h 충돌 때문에 해당 표는 본문에서 쓰지 않는다.
[Sources]
- https://arxiv.org/html/2508.20914v1
-->

---
layout: "seminar"
variant: "figure"
chapter: "근거 부록 A · 관측과 인코더"
causalStage: "appendix"
originSlide: 12
---

# 배열 좌표와 후보 격자는 서로 다른 변경이다

::body::
<PaperFigure src="/diagrams/p1-query-grid.svg" alt="같은 녹음과 마이크 배열을 유지하며 후보 방향 목록을 성긴 격자에서 촘촘한 격자로 바꾼 기하" caption="마이크 배열은 고정 · 질의할 후보 방향의 간격과 개수만 변경" />

::takeaway::
**배열 기하**와 **후보 방향 격자**는 독립적으로 달라질 수 있다.

::source::
AGG-RL, ICLR 2026. 설명용 재구성.

<!--
[현재 S53 · 근거 부록]
근거 부록 A · 관측과 인코더

[설명의 중심]
새 채널 기하와 새 후보 방향 목록은 서로 다른 일반화 요구다.

[연결]
이 장은 본문의 A · 관측과 인코더 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S53 발표 노트]
[설명 순서]
“앞에서는 녹음하는 마이크 배치를 바꿨지만, 여기서는 같은 녹음에 물어볼 방향 목록을 바꿉니다. 출력 칸이 고정된 모델과 후보 방향을 조건으로 받는 모델은 이 요구를 다르게 다룹니다.”

[경계·원문의 추가 자료]
후보 수 증가를 각도 정확도의 자동 향상으로 표현하지 않는다. 임의 격자와 임의 실제 배열 모두에 대한 보장도 주장하지 않는다.


AGG-RL §2.2 기반 설명용 재구성. 앞의 배열 변경과 이번 후보 목록 변경을 분리한다. 후보 수를 늘린다고 각도 정확도가 자동 향상되지는 않는다. 고정 출력 칸과 후보 조건 입력이라는 설계의 차이를 설명하되 임의 배열 전체에 대한 보장으로 확대하지 않는다.
[Sources]
- https://proceedings.iclr.cc/paper_files/paper/2026/file/ee860a9fa65a55a335754c557a5211de-Paper-Conference.pdf

[시각화 전 본문 설명]
관측 조건마이크 배열
어디에서 소리를 받는가
질의 조건후보 격자
어떤 방향들을 물어보는가
이번 변화같은 녹음
후보 방향의 간격·개수만 변경

[설명 그림의 범위]
발표자 제작 SVG. 개념의 관계를 읽기 위한 도식이며 원문의 실험 관측이나 모델 추정값을 그린 결과가 아니다.
-->

---
layout: "seminar"
variant: "method"
chapter: "근거 부록 A · 관측과 인코더"
causalStage: "appendix"
originSlide: 13
---

# AGG-RL: 기하와 후보 방향의 정합

::body::
<PaperFigure src="/research/agg-rl-overall.png" alt="AGG-RL Fig. 2 오디오와 마이크 기하의 표현을 후보 방향 표현과 비교하는 구조" />

::aside::
<section><span class="seminar-label semantic-input">관측 경로</span><p>다채널 오디오 + 마이크 좌표</p></section>
<section><span class="seminar-label semantic-geometry">후보 경로</span><p>판정할 방향 격자</p></section>
<section><span class="seminar-label semantic-result">표현의 비교</span><p>두 표현의 정합으로 공간 응답 계산</p></section>

::takeaway::
후보 방향도 입력으로 받아 **후보별 공간 응답**을 계산한다.

::source::
Baek et al., AGG-RL, ICLR 2026, Fig. 2 / 공식 프로젝트 그림.

<!--
[현재 S54 · 근거 부록]
근거 부록 A · 관측과 인코더

[설명의 중심]
AGG-RL은 오디오·기하·후보 격자 정합이라는 다른 설계 질문을 다룬다. 원형 Neural-SRP와 재구현 차이를 구별한다.

[연결]
이 장은 본문의 A · 관측과 인코더 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S54 발표 노트]
[설명 순서]
“그림에서 먼저 오디오와 마이크 좌표가 들어오는 경로, 후보 방향이 들어오는 경로를 나눠 보겠습니다. 이들이 만드는 표현을 비교해 각 후보의 응답을 계산하는 것이 이번 설계의 핵심입니다.”

[경계·원문의 추가 자료]
LNuDFT·rMPE를 학습 목표라고 부르지 않는다. 모든 내부 층과 손실 유도는 원문의 추가 자료이며 구조만으로 일반화 성능을 결론내리지 않는다.


LNuDFT는 주파수 단서 처리, rMPE는 마이크 상대 기하 표현과 연결한다. 둘은 학습 목표 이름이 아니다. 그림의 전체 층을 모두 읽기보다 입력 경로와 두 표현의 정합을 짚는다. 성능은 다음 실험 조건에서 따로 확인한다.
[Sources]
- https://proceedings.iclr.cc/paper_files/paper/2026/file/ee860a9fa65a55a335754c557a5211de-Paper-Conference.pdf

[원형과 재구현의 구별]
Neural-SRP 2024 원형은 STFT 위상·쌍 좌표·방 크기로 25×25 2D 위치 응답을 예측한다. AGG-RL 2026 §4.1의 Neural-SRP는 time-domain GCC-PHAT 입력·Fibonacci DOA 격자·다중 spatial spectra로 수정된 재구현이다. 앞의 Recorded 4 위치 오차와 여기 Dynamic-U DOA 결과는 한 checkpoint의 단계적 향상이나 동일 과제의 연속 성능 비교가 아니다.
-->

---
layout: "seminar"
variant: "result"
chapter: "근거 부록 A · 관측과 인코더"
causalStage: "appendix"
originSlide: 14
---

# 기하 정합의 효과는 미노출 채널 수로 시험한다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">Dynamic-U · 학습 4–12채널 / 시험 13–16채널</p>
<PaperFigure src="/diagrams/result-14.svg" alt="방향 MAE (°) ↓, $\mathrm{ACC}_{10}$ (%) ↑ 원문 수치 비교 그래프. 기본 Neural-SRP: 21.18, 45.51; AGG 적용: 19.05, 54.13" />
<p class="seminar-chart-note">합성 · 최대 두 정지 화자 · Dynamic-S에서는 두 지표가 개선되지 않음</p>
</div>

::takeaway::
AGG-RL의 **DOA 재구현 안에서** 정합의 효과를 비교한다. 원형의 2D 위치 실험과는 구별한다.

::source::
AGG-RL, ICLR 2026, Table 3, Neural-SRP without/with AGG-RL. 원문 수치의 그래프 재구성.

<!--
[현재 S55 · 근거 부록]
근거 부록 A · 관측과 인코더

[설명의 중심]
동일 재구현 안에서 AGG 유무를 비교한다. 앞의 2D 위치 실험과 이 DOA 실험을 연속 성능 향상처럼 읽지 않는다.

[연결]
이 장은 본문의 A · 관측과 인코더 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S55 발표 노트]
[설명 순서]
“여기서 Dynamic은 음원 이동이 아니라 배열 조건입니다. 같은 기준 모델의 정합 유무를 비교하면 미관측 채널 수에서 이득이 있지만, 학습 채널 수 범위인 Dynamic-S에서는 개선되지 않습니다.”

[경계·원문의 추가 자료]
모든 배열 일반화의 보장으로 읽지 않는다. Proposed 전체 시스템, Dynamic-S 상세, Table 4 격자 수와 Table 5 비용은 별도 원문의 추가 자료이다.


Dynamic은 음원 이동이 아니라 배열 조건을 뜻한다. ACC10은 10° 이내의 비율. 원표의 MAE ±는 95% 신뢰구간이며 여기서는 점추정만 표시했다. 전체 Proposed 모델의 성과를 AGG 하나의 효과로 대체하지 않는다.
[Sources]
- https://proceedings.iclr.cc/paper_files/paper/2026/file/ee860a9fa65a55a335754c557a5211de-Paper-Conference.pdf

[시각화 전 표의 수치·조건 보존]
Dynamic-U · 학습 4–12채널 / 시험 13–16채널Neural-SRP | MAE (°) ↓ | $\mathrm{ACC}_{10}$ (%) ↑ | 
기본 모델 | 21.18 | 45.51 | 
AGG 적용 | 19.05 | 54.13 | 

[조건]
합성 평가최대 두 정지 화자 / TIMIT 음성·ESC-50 잡음

조건의 경계Dynamic-S에서는 두 지표가 개선되지 않았다.
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.

[원형과 재구현의 구별]
Neural-SRP 2024 원형은 STFT 위상·쌍 좌표·방 크기로 25×25 2D 위치 응답을 예측한다. AGG-RL 2026 §4.1의 Neural-SRP는 time-domain GCC-PHAT 입력·Fibonacci DOA 격자·다중 spatial spectra로 수정된 재구현이다. 앞의 Recorded 4 위치 오차와 여기 Dynamic-U DOA 결과는 한 checkpoint의 단계적 향상이나 동일 과제의 연속 성능 비교가 아니다.

[시험 축]
후보 재질의 기능과 구별하여, 이번 정량 비교는 미노출 채널 수를 검사한다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "근거 부록 A · 관측과 인코더"
causalStage: "appendix"
originSlide: 16
---

# 입력 형식이 다르면 보존된 단서도 다르다

::body::
<PaperFigure src="/diagrams/p1-input-representations.svg" alt="물리적 위치의 마이크 배열과 두 귀 관측 및 구면조화 FOA 기저 성분을 구별한 그림" caption="FOA는 구면조화 기저 성분 표현 · 기저의 형태는 설명용 단면" />

::takeaway::
**추론 때 주는 정보**와 **학습 정답을 만드는 정보**를 나눠 읽는다.

::source::
AGG-RL, ICLR 2026; SFD, arXiv:2508.20914v1; GRAM, arXiv:2506.00934v5. 설명용 재구성.

<!--
[현재 S56 · 근거 부록]
근거 부록 A · 관측과 인코더

[설명의 중심]
배열·binaural·FOA는 다른 관측 계약이다.

[연결]
이 장은 본문의 A · 관측과 인코더 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S56 발표 노트]
[설명 순서]
“마이크 배열의 채널, 두 귀의 관측, FOA의 공간 성분은 같은 종류의 채널 목록이 아닙니다. 또한 오디오를 해석할 때 주는 정보와 학습 정답을 만드는 정보도 나눠 보아야 합니다.”

[경계·원문의 추가 자료]
FOA를 마이크 네 개라고 설명하지 않는다. 모든 모델에 좌표나 깊이가 추론 입력으로 들어간다는 보편 도식도 피한다.


배열에서 절대/상대 좌표는 방법에 따라 입력이 된다. 바이노럴의 HRTF가 언제나 별도 추론 텐서로 제공된다는 의미는 아니다. FOA는 구면조화 기저 성분 표현이다. 깊이 정보도 어떤 방법에서는 학습 지도에만 사용되므로 보편적인 추론 입력으로 그리지 않는다.
[Sources]
- https://proceedings.iclr.cc/paper_files/paper/2026/file/ee860a9fa65a55a335754c557a5211de-Paper-Conference.pdf
- https://arxiv.org/html/2508.20914v1
- https://arxiv.org/html/2506.00934v5

[시각화 전 본문 설명]
오디오 관측과 기하·지도 정보는 별개의 조건
입력 형식 | 채널이 뜻하는 것 | 추가 정보의 역할
마이크 배열 | 서로 다른 위치의 관측 | 좌표: 방법에 따라 추론 입력
바이노럴 | 두 귀의 관측 | HRTF: 청자별 전달 특성
FOA | 구면조화의 1차 성분 | 네 개의 점 마이크와 다름

[설명 그림의 범위]
발표자 제작 SVG. 개념의 관계를 읽기 위한 도식이며 원문의 실험 관측이나 모델 추정값을 그린 결과가 아니다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "근거 부록 A · 관측과 인코더"
causalStage: "appendix"
originSlide: 15
---

# 좌표에 사건 이름까지 붙이면 SELD가 된다

::body::
<PaperFigure src="/diagrams/p1-seld-timeline.svg" alt="말소리와 알람의 활성 시간 구간을 방향 화살표와 연결한 SELD 출력 형식" caption="고정 클래스 SELD · 정적 두 음원의 설명용 예시" />

::takeaway::
방향에 **사건 종류와 활성 시점**을 연결한 출력이 SELD다.

::source::
SELD 출력 형식의 설명용 예시. 실제 추정 결과가 아님.

<!--
[현재 S57 · 근거 부록]
근거 부록 A · 관측과 인코더

[설명의 중심]
고정 클래스 SELD도 사건과 위치를 연결한다. LLM 이전 설계의 범위를 확인한다.

[연결]
이 장은 본문의 A · 관측과 인코더 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S57 발표 노트]
[설명 순서]
“지금 요구하는 것은 방향 목록에 사건 종류와 활성 시점을 연결한 출력입니다. 이 결합은 SELD도 다루므로, 본문에서 논의한 언어 모델이 처음 가능하게 만든 능력으로 설명하지 않겠습니다.”

[경계·원문의 추가 자료]
고정 클래스 SELD를 자유 어휘 질의나 자유형 답변과 동일시하지 않는다. 평가 지표의 세부 정의는 실제 결과를 읽을 때 소개한다.


고정 클래스 sound event localization and detection을 설명한다. 의미와 위치의 결합이 LLM 등장 후 처음 가능해진 것은 아니다. 자유 어휘 질의 또는 자유형 답변 생성과는 출력 계약이 다르다.
[Sources]
- https://arxiv.org/html/2606.27751v1

[시각화 전 본문 설명]
같은 설명용 두 음원 장면
음원 | 사건 종류 | 활성 시점 | 방향
음원 A | 말소리 | 말하는 동안 | 왼쪽
음원 B | 알람 | 울리는 동안 | 오른쪽

[설명 그림의 범위]
발표자 제작 SVG. 개념의 관계를 읽기 위한 도식이며 원문의 실험 관측이나 모델 추정값을 그린 결과가 아니다.
교육 참고: DCASE 2019 공식 SELD 과제 정의의 사건 클래스·onset/offset·DOA 대응. 타임라인은 임의 시각과 활동 구간의 설명용 장면이다.
- https://dcase.community/challenge2019/task-sound-event-localization-and-detection
-->

---
layout: "seminar"
variant: "figure"
chapter: "근거 부록 A · 관측과 인코더"
causalStage: "appendix"
originSlide: 23
---

# 위치 오차는 검출 범위와 함께 읽어야 한다

::body::
<PaperFigure src="/research/p1-lam-threshold.svg" alt="LAM Fig. 3 같은 UpLAM GRU-MHSA의 검출 threshold에 따른 LE와 LR" caption="STARSS dev-test-sony: 실선이 평가 곡선. 점선은 검증, 녹색선은 기본 임계값 0.5." />

::takeaway::
임계값을 낮추면 **재현율과 위치 오차가 함께 높아질 수 있다.**

::source::
LAM, arXiv:2507.07066v1, Fig. 3. 원문 벡터; LE (°) ↓, LR (%) ↑.

<!--
[현재 S58 · 근거 부록]
근거 부록 A · 관측과 인코더

[설명의 중심]
LAM은 잠재 지도를 읽는 threshold에 따라 LE/LR이 달라진다.

[연결]
이 장은 본문의 A · 관측과 인코더 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S58 발표 노트]
[설명 순서]
“여기서는 두 모델의 우열이 아니라 같은 모델의 검출 기준을 바꿉니다. 놓치는 음원과 위치 오차가 어떻게 함께 달라지는지 보면서, 기본 임계값에서 얻은 결과의 의미를 확인하겠습니다.”

[경계·원문의 추가 자료]
곡선의 여러 점을 서로 다른 모델로 설명하지 않는다. Table 2의 모델 비교는 원문의 추가 자료이며, 이 결과를 음원 종류나 자연어 이해로 확대하지 않는다.


두 패널은 두 모델이 아니라 같은 UpLAM + GRU-MHSA의 LE와 LR이다. 실선 evaluation만 주근거로 읽고 점선 validation을 시험 성과로 혼동하지 않는다. LE는 낮을수록, LR은 높을수록 좋다. Eigenscape 10시간+SpatialScaper 합성 10시간으로 CSM 복원을 학습했다. 후속 DOA 판독기는 STARSS dev-train-tau/sony와 companion synthetic data로 지도학습하고 dev-test-tau로 검증했다. 기본 임계값0.5의 평가 표값은 LE18.65°, LR57.6%; 곡선에서 새 수치를 추정하지 않았다.
[Sources]
- https://arxiv.org/html/2507.07066v1
-->

---
layout: "seminar"
variant: "method"
chapter: "근거 부록 A · 관측과 인코더"
causalStage: "appendix"
originSlide: 24
---

# 공간 단서를 목표로 정해 인코더를 학습한다

::body::
<PaperFigure src="/research/sfd-framework.svg" alt="SFD Fig. 1 오염된 바이노럴 입력에서 깨끗한 공간 특징을 예측한 뒤 DOA 미세조정" />

::aside::
<section><span class="seminar-label semantic-input">모델 입력</span><p>잡음·잔향이 섞인 바이노럴 STFT</p></section>
<section><span class="seminar-label semantic-geometry">사전학습 목표</span><p>clean 신호에서 계산한 공간 특징</p></section>
<section><span class="seminar-label semantic-result">후속 과제</span><p>특징 예측기를 버리고 DOA에 미세조정</p></section>

::takeaway::
오염된 입력으로 **깨끗한 비잔향 신호의 공간 특징**을 예측한다.

::source::
SFD, arXiv:2508.20914v1, Fig. 1. 원문 벡터.

<!--
[현재 S59 · 근거 부록]
근거 부록 A · 관측과 인코더

[설명의 중심]
SFD의 학습 목표는 별도 teacher network가 아니라 clean audio의 공간 특징이다.

[연결]
이 장은 본문의 A · 관측과 인코더 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S59 발표 노트]
[설명 순서]
“이 방법은 모델이 복원할 대상을 원래 파형 전체 대신 공간 특징으로 정합니다. 깨끗한 신호에서 얻은 목표를 오염된 입력으로 예측하게 한 뒤 DOA 과제에 적응합니다.”

[경계·원문의 추가 자료]
GCC·GCC-PHAT·CPS 위상·ILD/IPD를 모두 한 손실로 합쳐 학습했다고 설명하지 않는다. 세부 목표 수식은 해당 결과 해석에 필요한 것만 남긴다.


GCC, GCC-PHAT, CPSPhase, ILD+IPD는 각각 별도의 특징 목표 변형이다. 여러 목표를 한 손실로 모두 결합한 모델로 설명하지 않는다. 별도 학습된 teacher network가 아니라 clean 비잔향 바이노럴 신호의 분석적 특징 추출이다. DOA 라벨이 없어도 clean target은 필요하다.
[Sources]
- https://arxiv.org/html/2508.20914v1
-->

---
layout: "seminar"
variant: "result"
chapter: "근거 부록 A · 관측과 인코더"
causalStage: "appendix"
originSlide: 21
---

# 복원이 모든 물리량의 보존을 보장하지는 않는다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">학습 방 8개 · 검증/시험 각 20개 방 · 4회 평균</p>
<PaperFigure src="/diagrams/result-21.svg" alt="TDoA MAE (samples) ↓ 원문 수치 비교 그래프. 처음부터 지도학습: 0.40; 사전학습 + 전체 미세조정: 0.28" />
<p class="seminar-chart-note"><MathInline tex="C_{50}" /> MAE는 1.14 → 1.21 dB로 증가 · 두 마이크·단일 정지 음성</p>
</div>

::takeaway::
TDoA 오차는 줄었지만 **모든 공간 지표가 개선된 것은 아니다.**

::source::
CCSR, arXiv:2312.00476v2, Table III, 8-room condition. 원문 수치의 그래프 재구성.

<!--
[현재 S60 · 근거 부록]
근거 부록 A · 관측과 인코더

[설명의 중심]
CCSR은 전체 미세조정에서 TDoA는 개선하지만 C50는 악화한다.

[연결]
이 장은 본문의 A · 관측과 인코더 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S60 발표 노트]
[설명 순서]
“여기서는 후속 조건에서 처음부터 학습한 경우와 전체 미세조정한 경우를 비교합니다. TDoA는 개선됐지만 C50 오차는 1.14 dB에서 1.21 dB로 증가해, 모든 지표가 함께 좋아지지는 않았습니다.”

[경계·원문의 추가 자료]
C50 반례를 짧은 주석으로 남긴다. frozen의 TDoA 1.49와 T60 상세는 원문의 추가 자료이며, 전체 적응 결과를 고정 표현의 선형 접근성으로 표현하지 않는다.


전체 downstream 모델을 업데이트한 fine-tuning 비교다. 고정 인코더의 TDoA 1.49 samples와 섞어 사전학습 이득을 계산하지 않는다. C50는 초기 50 ms와 후기 에너지 비율의 명료도 지표이며 여기서는 dB MAE를 비교한다. CCSR도 잡음과 잔향을 포함한다.
[Sources]
- https://arxiv.org/html/2312.00476v2

[시각화 전 표의 수치·조건 보존]
학습 방 8개 · 검증/시험 각 20개 방 · 4회 평균학습 설정 | TDoA MAE (samples) ↓ | 
처음부터 지도학습 | 0.40 | 
사전학습 + 전체 미세조정 | 0.28 | 

[조건]
평가 입력두 마이크, 단일 정지 음성 / 합성 잔향·SNR 15–30 dB

함께 읽을 반례$C_{50}$ MAE: 1.14 → 1.21 dB / 오히려 증가
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "근거 부록 A · 관측과 인코더"
causalStage: "appendix"
originSlide: 30
---

# 고정 표현의 위치 판독으로 재사용을 확인한다

::body::
<PaperFigure src="/research/p1-gram-doa.svg" alt="GRAM Fig. 3(A) SC-5와 ESC-50의 고정 표현 DOA 오차 boxplot과 원본 범례" caption="합성 자연 장면 · 고정 인코더 + 지도 판독기. 중앙선: 중앙값, 상자: 사분위 범위." />

::takeaway::
**중앙값과 퍼짐**, 그리고 모델마다 다른 입력 조건을 함께 읽는다.

::source::
GRAM, arXiv:2506.00934v5, Fig. 3(A). 원본 벡터 크롭·범례 재배치.

<!--
[현재 S61 · 근거 부록]
근거 부록 A · 관측과 인코더

[설명의 중심]
GRAM의 median·IQR과 native input 조건을 보존해 판독 범위를 읽는다.

[연결]
이 장은 본문의 A · 관측과 인코더 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S61 발표 노트]
[설명 순서]
“먼저 각 분포가 어떤 입력에서 나온 고정 특징인지 확인하겠습니다. 중앙값과 퍼짐을 함께 읽되, 입력까지 통제한 동일 조건의 사전학습 제거 실험으로 해석하지는 않겠습니다.”

[경계·원문의 추가 자료]
T60과 STARSS23 전체 미세조정은 원문의 추가 자료이다. TAU2019 측정 RIR 합성을 전체 실제 녹음이라 부르거나 실녹음 적응 결과를 고정 판독과 합치지 않는다.


GRAM-Ambisonics와 SpatialAST(supervised)를 중심으로 읽되 원래 입력과 학습 데이터가 다르다는 것을 명시한다. GRAM-Bin.Patch/Time은 바이노럴, GRAM-Ambisonics는 FOA, GRAM-Clean은 clean 음원 학습 조건이다. SC-5 음성과 ESC-50 환경음을 공간화한 합성 자연 장면에서 고정 특징으로 판독했다. 원본 box는 first/third quartile, center line median, whiskers1.5IQR다. 평균 막대로 바꾸거나 수치를 눈대중으로 읽지 않았다. 입력까지 통제한 masking ablation이 아니다.
[Sources]
- https://arxiv.org/html/2506.00934v5
-->

---
layout: "seminar"
variant: "figure"
chapter: "근거 부록 B · 의미와 공간의 정렬"
causalStage: "appendix"
originSlide: 32
---

# “뒤쪽의 알람”은 종류와 위치가 함께 맞아야 한다

::body::
<PaperFigure src="/diagrams/p1-spatial-language.svg" alt="청자 뒤 알람 관측과 동일한 소리 이름에 앞쪽 또는 뒤쪽 공간 표현을 붙인 두 문장 후보" caption="설명용 문장 후보 · 실제 모델의 정합 점수나 성공 예시가 아님" />

::takeaway::
ELSA의 검색용 문장 정렬은 **사건과 위치를 함께 맞추는 요구**를 보여 준다.

::source::
ELSA의 공간 오디오–언어 정렬 문제에 기반한 설명용 후보. 실제 모델 점수가 아님.

<!--
[현재 S62 · 근거 부록]
근거 부록 B · 의미와 공간의 정렬

[설명의 중심]
ELSA의 검색은 어떤 의미 결속을 토큰에 남겨야 할지 보여 준다. 생성형 LLM의 성과는 아니다.

[연결]
이 장은 본문의 B · 의미와 공간의 정렬 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S62 발표 노트]
[설명 순서]
“여기서는 자유롭게 답을 생성하는 대신 후보 문장과 녹음이 얼마나 맞는지 비교합니다. 소리 이름이 같은 문장도 위치가 다르면 다른 대응으로 구별해야 합니다.”

[경계·원문의 추가 자료]
설명용 후보의 성공을 ELSA의 실험 결과로 표시하지 않는다. 프롬프트 분류·검색과 생성형 QA는 출력 방식부터 다르다.


C32. 요구 출력은 후보 문장의 선택 또는 정합 점수다. 임의의 점수를 넣지 않았다. ELSA의 prompt 분류와 검색은 자유롭게 답변을 생성하는 QA와 다르다. 근거 부록의 ELSA 결과 장에서 동일 모델의 합성/실녹음 방향 분류를 확인한다.
[Sources]
- https://papers.neurips.cc/paper_files/paper/2024/file/3acc054949b6948d4444b35d412cab56-Paper-Conference.pdf

[시각화 전 본문 설명]
관측공간 오디오
알람 소리 + 위치 단서
문장 후보 A앞쪽의 알람
같은 종류, 다른 방향
문장 후보 B뒤쪽의 알람
위치 표현까지 맞는가

[설명 그림의 범위]
발표자 제작 SVG. 개념의 관계를 읽기 위한 도식이며 원문의 실험 관측이나 모델 추정값을 그린 결과가 아니다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "근거 부록 B · 의미와 공간의 정렬"
causalStage: "appendix"
originSlide: 34
---

# 의미와 공간을 따로 배우고 같은 음원에 연결한다

::body::
<PaperFigure src="/diagrams/p1-salm-factorization.svg" alt="같은 알람의 위치 변화와 omni 의미 분기 및 FOA 공간 분기의 서로 다른 caption 정렬 목표" caption="원래 caption과 공간 caption을 구별하는 분기 역할의 개념도" />

::takeaway::
SALM은 **의미·공간을 각각 감독하고 결합**한다. LLM의 답변 생성과는 다른 정렬 문제다.

::source::
SALM, arXiv:2507.16724v2, Fig. 1 기반 분기 역할 재구성.

<!--
[현재 S63 · 근거 부록]
근거 부록 B · 의미와 공간의 정렬

[설명의 중심]
SALM의 구조화 정렬은 사건 의미와 위치를 어떤 감독으로 결합할지 보여 준다.

[연결]
이 장은 본문의 B · 의미와 공간의 정렬 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S63 발표 노트]
[설명 순서]
“같은 알람을 다른 위치로 옮기면 소리의 종류는 유지되지만 공간 속성은 바뀝니다. SALM은 이 차이를 표현의 분리와 언어 정렬이라는 설계 선택으로 다룹니다.”

[경계·원문의 추가 자료]
두 분기를 만들었다는 사실만으로 완전한 요인 분리를 입증했다고 말하지 않는다. 임베딩 편집은 본문의 파형 생성 성과로 쓰지 않는다.


그림은 같은 알람의 위치를 바꾼 설명용 사고실험이다. SALM은 semantic/text를 CLAP으로, 공간 DOA 분기를 PSELDNet으로 초기화한다. omni semantic branch와 FOA spatial branch를 결합하며 원래 caption과 spatial caption을 구별한다. 분기 구조 자체가 통계적 독립성이나 완전한 요인 분리를 입증하지 않는다. 임베딩 조작을 파형 편집 성과로 확대하지 않는다.
[Sources]
- https://arxiv.org/html/2507.16724v2

[시각화 전 본문 설명]
공통 소리알람
장소가 달라도 종류는 유지
의미 분기omni 채널
원래 caption과 정렬
공간 분기FOA 전체
공간 caption·방향과 연결

[설명 그림의 범위]
발표자 제작 SVG. 개념의 관계를 읽기 위한 도식이며 원문의 실험 관측이나 모델 추정값을 그린 결과가 아니다.
-->

---
layout: "seminar"
variant: "result"
chapter: "근거 부록 B · 의미와 공간의 정렬"
causalStage: "appendix"
originSlide: 35
---

# 의미 정렬을 더하면 검색과 위치 판독이 어떻게 바뀌나

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">동일 SALM · 합성 FOA sClotho 평가</p>
<PaperFigure src="/diagrams/result-35.svg" alt="T2A R@1 (%) ↑, A2T R@1 (%) ↑, 위치 오차 (°) ↓ 원문 수치 비교 그래프. $L_{\mathrm{sCL}}+L_{\mathrm{DOA}}$: 9.1, 9.6, 1.8; 위 조건 + $L_{\mathrm{CL}}$: 10.5, 10.4, 1.6" />
</div>

::takeaway::
**의미 정렬 loss의 기여**를 본 결과다. LLM·LoRA의 효과를 측정한 표가 아니다.

::source::
SALM, arXiv:2507.16724v2, Table 1, sClotho. 원문 수치의 그래프 재구성.

<!--
[현재 S64 · 근거 부록]
근거 부록 B · 의미와 공간의 정렬

[설명의 중심]
SALM의 동일 모델 loss 비교로 의미 목표의 기여를 본다. adapter/LoRA ablation과 구별한다.

[연결]
이 장은 본문의 B · 의미와 공간의 정렬 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S64 발표 노트]
[설명 순서]
“다른 모델의 순위가 아니라 같은 SALM의 학습 목표 한 가지를 비교합니다. 검색 점수는 높아지고 위치 오차는 낮아졌지만, 이는 같은 원문 조건에서 관측한 변화입니다.”

[경계·원문의 추가 자료]
두 검색 방향을 정의하고 지표의 좋은 방향을 표시한다. 실측 SRIR·표현 편집·다른 모델 순위는 원문의 추가 자료이며, 자연어 복합 추론의 증거로 확대하지 않는다.


T2A는 텍스트→오디오, A2T는 오디오→텍스트 검색이다. R@1은 정답이 최상위 후보에 있는 비율. LCL은 원래 caption과 semantic embedding의 대조 목표다. LsCL은 공간 caption을 사용한 대조 목표, LDOA는 지도 방향 목표다. 위치 오차는 지도 DOA loss로 학습한 MLP의 오차로, ELSA의 zero-shot prompt 방향 분류와 다른 프로토콜이다. 두 행은 SALM-s 같은 다른 모델을 섞지 않았다.
[Sources]
- https://arxiv.org/html/2507.16724v2

[시각화 전 표의 수치·조건 보존]
동일 SALM · 합성 FOA sClotho 평가SALM의 학습 목표 | T2A R@1 (%) ↑ | A2T R@1 (%) ↑ | 위치 오차 (°) ↓ | 
$L_{\mathrm{sCL}}+L_{\mathrm{DOA}}$ | 9.1 | 9.6 | 1.8 | 
위 조건 + $L_{\mathrm{CL}}$ | 10.5 | 10.4 | 1.6 |
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "근거 부록 B · 의미와 공간의 정렬"
causalStage: "appendix"
originSlide: 26
---

# 의미 특징은 공간 경로의 어느 깊이에서 합칠까?

::body::
<PaperFigure src="/diagrams/p1-fusion-depth.svg" alt="같은 공간 처리 경로에서 태깅 의미 특징을 낮은 수준과 높은 수준에 연결하는 두 대안" caption="일반 오디오 태깅 사전학습 특징의 결합 위치 비교" />

::takeaway::
AT2SELD는 **의미·공간 특징의 결합 위치**를 비교한다.

::source::
AT2SELD, arXiv:2606.27751v1, Fig. 25 기반 결합 위치 재구성.

<!--
[현재 S65 · 근거 부록]
근거 부록 B · 의미와 공간의 정렬

[설명의 중심]
AT2SELD는 고정 클래스 SELD에서 semantic–spatial 결합 위치를 시험한다.

[연결]
이 장은 본문의 B · 의미와 공간의 정렬 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S65 발표 노트]
[설명 순서]
“앞의 SELD는 소리 종류와 위치를 함께 출력했습니다. 이 연구는 일반 오디오 태깅에서 얻은 의미 정보를 그 예측 과정의 어디에 연결하는 것이 유용한지 묻습니다.”

[경계·원문의 추가 자료]
의미 분류기가 정확하면 음원과 방향의 대응도 자동으로 해결된다고 주장하지 않는다. 고정 클래스 SELD 적응을 자유 어휘 질의응답과 구별한다.


이 연구 보고서에서 쓰는 AT2SELD 명칭을 따른다. 공간 경로의 초반에 결합할지 후반에 결합할지가 이번 설계 질문이다. 의미 분류가 가능하다고 사건-방향 대응이 자동으로 보장되지 않는다. 자유 어휘나 자유형 QA 모델이 아니다.
[Sources]
- https://arxiv.org/html/2606.27751v1

[시각화 전 본문 설명]
공간 경로
FOA 입력 → 공간 단서 처리 → SELD 출력
early 결합
낮은 수준의 특징에서 의미 경로 연결
late 결합
높은 수준의 특징에서 의미 경로 연결
의미 경로의 출발점
일반 오디오 태깅 사전학습
최종 출력
고정 클래스 사건·활성·위치

[설명 그림의 범위]
발표자 제작 SVG. 개념의 관계를 읽기 위한 도식이며 원문의 실험 관측이나 모델 추정값을 그린 결과가 아니다.
-->

---
layout: "seminar"
variant: "result"
chapter: "근거 부록 B · 의미와 공간의 정렬"
causalStage: "appendix"
originSlide: 27
---

# 결합 위치의 효과도 학습 조건에 달려 있다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">STARSS23 · Stage 3의 강한 dropout을 공유</p>
<PaperFigure src="/diagrams/result-27.svg" alt="Test SELD ↓ 원문 수치 비교 그래프. no-stitch · cs00: 0.708; late-only · cs01: 0.624" />
<p class="seminar-chart-note">최적 validation 체크포인트로 test · 무결합 기준도 Stage 2보다 저하된 조건</p>
</div>

::takeaway::
이 Stage 3 조건에서 **late-only의 SELD 점수가 낮았다.**

::source::
AT2SELD, arXiv:2606.27751v1, Table 11–12. 원문 수치의 그래프 재구성.

<!--
[현재 S66 · 근거 부록]
근거 부록 B · 의미와 공간의 정렬

[설명의 중심]
AT2SELD late 결합의 이득은 강한 dropout이라는 같은 조건 안의 결과다.

[연결]
이 장은 본문의 B · 의미와 공간의 정렬 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S66 발표 노트]
[설명 순서]
“이 차이는 원문의 특정 학습 단계와 dropout 조건에서 읽어야 합니다. 그 안에서 late-only 결합이 점수를 낮췄다고 말할 수 있지만, 의미 결합이 모든 학습 조건에서 우월하다는 결론은 아닙니다.”

[경계·원문의 추가 자료]
전체 설정 탐색과 다른 학습 단계는 원문의 추가 자료이다. 다른 조건의 최상위 행을 이번 기준선과 짝짓거나 범용 표현의 성과로 확대하지 않는다.


FOA 공간 경로와 pretrained audio-tagging 의미 경로를 사용한다. 이 표는 frozen probe가 아니다. Stage3 no-stitch는 unregularized Stage2보다 악화됐으므로, 강한 정규화 안에서의 성능 회복을 모든 공간 전용 모델에 대한 우위로 확대하지 않는다. early-only와 early+late는 원문의 추가 자료의 별도 비교다.
[Sources]
- https://arxiv.org/html/2606.27751v1

[시각화 전 표의 수치·조건 보존]
STARSS23 · Stage 3의 강한 dropout을 공유결합 설정 | Test SELD ↓ | 
no-stitch · cs00 | 0.708 | 
late-only · cs01 | 0.624 | 

[조건]
학습·선택지도 SELD 적응 / 최적 validation 체크포인트로 test

비교의 범위무결합 기준 자체가 Stage 2보다 저하된 조건
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->

---
layout: "seminar"
variant: "result"
chapter: "근거 부록 B · 의미와 공간의 정렬"
causalStage: "appendix"
originSlide: 33
---

# 언어 정렬도 실제 녹음에서 따로 검사한다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">동일 ELSA · 문장 template와 audio embedding의 cosine similarity</p>
<PaperFigure src="/diagrams/result-33.svg" alt="4방향 정확도 (%) ↑ 원문 수치 비교 그래프. S-Clotho · 합성: 92.0; S-AC · 합성: 92.8; S-RWD · 실녹음: 35.8" />
<p class="seminar-chart-note">S-RWD: 실제 5개 방, 70개 샘플</p>
</div>

::takeaway::
이 작은 실녹음 평가에서 **합성보다 방향 분류 정확도가 낮았다.**

::source::
ELSA, NeurIPS 2024, Table 2. arXiv v1과 출판본 수치 일치 확인.

<!--
[현재 S67 · 근거 부록]
근거 부록 B · 의미와 공간의 정렬

[설명의 중심]
ELSA의 공간 문장 정렬은 합성→실녹음 전이 격차가 남는다.

[연결]
이 장은 본문의 B · 의미와 공간의 정렬 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S67 발표 노트]
[설명 순서]
“ELSA는 공간 정보를 담은 오디오와 텍스트를 함께 정렬합니다. 같은 방향 후보를 사용해도 합성과 실제 녹음에서 정확도가 달라지므로, 이 차이를 포함해 재사용 범위를 읽겠습니다.”

[경계·원문의 추가 자료]
Table 2에 없는 기준선을 만들지 않는다. CLAP의 Appendix A Table 7은 입력 조건을 표시해 원문의 추가 자료에 두며, 합성·실제 차이를 단일 원인의 효과로 단정하지 않는다.


방향 후보 네 클래스를 cosine similarity로 비교한 동일 모델의 prompt 분류다. 연속 각도 회귀나 자유형 QA 점수가 아니다. ELSA는 전체 구성요소를 갱신하며 spatial branch는 지도 공간 사전학습으로 초기화한다. 원문 Table2에는 baseline이 없다. NeurIPS 출판본 PDF p7 Table2에서92.0%,92.8%,35.8%를 대조해 확인했다. 작은 S-RWD와 합성의 차이를 하나의 원인으로 설명하지 않는다.
[Sources]
- https://papers.neurips.cc/paper_files/paper/2024/file/3acc054949b6948d4444b35d412cab56-Paper-Conference.pdf

[시각화 전 표의 수치·조건 보존]
동일 ELSA · 문장 template와 audio embedding의 cosine similarity평가 데이터 | 관측 조건 | 4방향 정확도 (%) ↑ | 
S-Clotho | 합성 | 92.0 | 
S-AC | 합성 | 92.8 | 
S-RWD | 실녹음 | 35.8 | 

[조건]
학습 방식공간화한 오디오·문장의 대조 정렬

실녹음 크기S-RWD: 5개 방, 70개 샘플
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->

---
layout: "seminar"
variant: "method"
chapter: "근거 부록 B · 의미와 공간의 정렬"
causalStage: "appendix"
originSlide: 36
---

# 문장으로 고른 음원의 위치만 읽을 수 있나?

::body::
<PaperFigure src="/research/p1-selecttsl-problem.png" alt="SelectTSL Fig. 1 모든 음원 위치와 prompt로 지정한 speech 위치를 찾는 과제 비교" />

::aside::
<section><span class="seminar-label semantic-input">목표를 지정하는 입력</span><p>텍스트 및/또는 1초 예시 오디오</p></section>
<section><span class="seminar-label semantic-result">찾아야 할 출력</span><p>프레임별 목표 수 0 / 1 / 2와 DOA</p></section>

::takeaway::
SelectTSL의 출력은 **지정한 목표의 활성 수와 방향**이다.

::source::
SelectTSL, arXiv:2607.02343v1, Fig. 1. CC BY 4.0.

<!--
[현재 S68 · 근거 부록]
근거 부록 B · 의미와 공간의 정렬

[설명의 중심]
SelectTSL은 생성 LLM 없이 prompt 조건으로 목표 음원을 골라 위치를 읽는다.

[연결]
이 장은 본문의 B · 의미와 공간의 정렬 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S68 발표 노트]
[설명 순서]
“앞의 정렬에서는 오디오와 문장의 대응을 평가했지만, 여기서는 요청한 소리의 위치를 직접 출력합니다. 목표가 없거나 여러 개일 수도 있으므로, 선택과 활성 수 판단도 과제의 일부가 됩니다.”

[경계·원문의 추가 자료]
파형을 분리해 생성하는 과제로 소개하지 않는다. full model의 텍스트·예시 오디오 조건을 텍스트만 쓰는 시스템으로 축약하지 않는다.


다음 결과에서 Full은 text+audio cue를 함께 받는다. 원문 문제 그림의 prompt는 speech이며 앞서 사용한 알람 사고실험과 별개다. 내부 extraction 모듈의 selection 학습은 설명하되 출력 파형의 생성 성능이 본문의 주제는 아니다. 원문 MOTA*에는 ID-switch 벌점이 없어 음원 정체성 추적의 근거로 삼지 않는다.
[Sources]
- https://arxiv.org/html/2607.02343v1
-->

---
layout: "seminar"
variant: "result"
chapter: "근거 부록 B · 의미와 공간의 정렬"
causalStage: "appendix"
originSlide: 37
---

# 목표 선택 뒤에도 IPD 경로의 기여가 남았다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">text + 1초 audio cue 유지 · 같은 목표 입력 조건</p>
<PaperFigure src="/diagrams/result-37.svg" alt="MAE (°) ↓, F1 ↑ 원문 수치 비교 그래프. Full: 0.98, 0.96; IPD Enhancer 제거 · A1: 2.10, 0.83" />
<p class="seminar-chart-note">MAE는 true positive만 계산 · F1과 함께 해석</p>
</div>

::takeaway::
목표 입력을 유지한 비교에서 **위상 정보 강화 경로의 기여**가 나타났다.

::source::
SelectTSL, arXiv:2607.02343v1, Table VI. F1은 0–1 척도. 원문 수치의 그래프 재구성.

<!--
[현재 S69 · 근거 부록]
근거 부록 B · 의미와 공간의 정렬

[설명의 중심]
SelectTSL의 IPD enhancer 제거 결과는 prompt와 물리 단서의 역할을 구별한다.

[연결]
이 장은 본문의 B · 의미와 공간의 정렬 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S69 발표 노트]
[설명 순서]
“같은 목표 입력을 둔 채 IPD Enhancer를 제거한 조건을 비교하겠습니다. 오차와 F1의 변화는 해당 경로의 기여를 보여주지만, 다른 입력 단서의 도움까지 없앴다는 뜻은 아닙니다.”

[경계·원문의 추가 자료]
A4 직접 입력과 OSPAT는 원문의 추가 자료이다. MAE는 true positive 조건이며, Table III의 MOTA*·Recall 불일치와 실측 RIR 정적 합성이라는 범위를 유지한다.


주 실험은 5초 clip, SNR−5~5dB, 방위각[0,180), 프레임별 목표 수0/1/2 조건이다. Selection, DOA, cardinality를 함께 학습한다. MAE는 검출된 true positive 오차로 미검출을 직접 벌하지 않는다. TableVI Full/A1의 F1은0.96/0.83이며 퍼센트로 옮기지 않았다. A4, OSPA-T는 별도 원문의 추가 자료이다. TableIII의 일부 P/R·MOTA* 불일치가 있어 이를 새로운 정량 근거로 사용하지 않는다. TAU-SRIR는 측정 RIR 합성이므로 현장 이동 혼합 녹음으로 설명하지 않는다.
[Sources]
- https://arxiv.org/html/2607.02343v1

[시각화 전 표의 수치·조건 보존]
text + 1초 audio cue 유지 · 같은 목표 입력 조건SelectTSL 설정 | MAE (°) ↓ | F1 ↑ | 
Full | 0.98 | 0.96 | 
IPD Enhancer 제거 · A1 | 2.10 | 0.83 | 

[조건]
합성 주 실험4×4×2 m 방 · $T_{60}=0.2\,\mathrm{s}$ / 마이크 간격 20 cm

오차의 분모MAE는 true positive만 계산 / F1을 함께 읽어야 한다.
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->

---
layout: "seminar"
variant: "focus"
chapter: "근거 부록 B · 의미와 공간의 정렬"
causalStage: "appendix"
originSlide: 65
---

# 시간과 위치를 바꾼 문장은 다른 정답이다

::body::
<PaperFigure src="/diagrams/p2-s65-event-negatives.png" alt="시간의 먼저와 나중, 공간의 왼쪽과 오른쪽 격자에서 기준 사건열, 순서 반전, 위치 교환을 비교한다." caption="사건 배치 재구성 · 화살표는 시간" />

::takeaway::
같은 두 소리도 **발생 순서·각 사건의 방향**이 달라지면 설명문과의 대응이 바뀐다.

::source::
CoSTALA, arXiv:2608.24374v1, §2.1 기반 설명용 재구성 C65. 겹치지 않는 두 FOA 사건·8방향.

<!--
[현재 S70 · 근거 부록]
근거 부록 B · 의미와 공간의 정렬

[설명의 중심]
CoSTALA는 시간 순서·위치 결속을 hard negative로 정렬한다.

[연결]
이 장은 본문의 B · 의미와 공간의 정렬 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S70]
[Sources]
- https://arxiv.org/html/2608.24374v1
[시각 자료]
직접 제작한 강의용 벡터 도식을 삽입했다. 원문 결과·예측을 재현한 그림이 아니며 기존 해석 범위와 평가 조건을 유지한다. SVG 원본과 2배 해상도 PNG는 public/diagrams에 보관한다.
[발표 노트]
설명문과 잘 맞는 오디오를 검색하는 문제로 읽는다. 기준 사건열은 알람이 왼쪽에서 먼저 울리고 말소리가 오른쪽에서 나중에 난다. Temporal negative는 소리와 위치는 그대로 두고 순서를 뒤집는다. Spatial negative는 사건 순서를 유지하며 각 소리의 위치를 바꾼다. 화살표는 발생 순서를 뜻하며 한 음원의 이동 경로를 나타내지 않는다.
[해석 범위]
CoSTALA의 범위는 겹치지 않는 두 합성 FOA 사건과 8방향이다. 화면은 §2.1의 negative 구성을 설명하는 예다. 자유형 QA, 연속 음원 추적, 겹친 음원 분리의 성공 사례가 아니다. Fig. 1과 Fig. 2는 contrastive·local·consistency 학습의 방법 그림이며 실제 검색 결과와 구분한다.
-->

---
layout: "seminar"
variant: "result"
chapter: "근거 부록 B · 의미와 공간의 정렬"
causalStage: "appendix"
originSlide: 66
---

# 순서·위치 정렬은 검색으로도 시험할 수 있다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">두 합성 FOA 사건 · Global Text-to-Audio 검색 · <MathInline tex="E_{\mathrm{global}}\leftrightarrow T_{\mathrm{st}}" />의 cosine similarity</p>
<PaperFigure src="/diagrams/result-66.svg" alt="Global T2A R@1 (%) ↑ 원문 수치 비교 그래프. 대조 학습만 · $L_{\mathrm{cl}}$: 5.84; 전체 · $L_{\mathrm{cl}}+L_{\mathrm{st}}+L_{\mathrm{local}}+L_{\mathrm{consist}}$: 8.10" />
</div>

::takeaway::
전체 loss는 **이 사건열 검색을 개선**했으며, 연속 이동 추적은 별도 검증이 필요하다.

::source::
CoSTALA, arXiv:2608.24374v1, Table 2·§3.1. R@1: 정답을 첫 후보로 검색한 비율.

<!--
[현재 S71 · 근거 부록]
근거 부록 B · 의미와 공간의 정렬

[설명의 중심]
CoSTALA retrieval은 생성형 LLM의 LoRA/QA 성과가 아니다.

[연결]
이 장은 본문의 B · 의미와 공간의 정렬 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S71]
[Sources]
- https://arxiv.org/html/2608.24374v1
[발표 노트]
Table 2의 contrastive-only와 전체 loss 두 행에서 Global Text-to-Audio R@1만 선택한다. 사건별 local alignment와 consistency 등을 포함한 전체 조건에서 5.84에서 8.10%로 높아진다. §3.1은 E_global과 T_st의 cosine similarity로 검색한다고 명시한다. Fig. 2의 최종 E_st를 직접 평가한 표라고 설명하지 않는다.
[해석 범위]
여러 loss를 함께 바꿨으므로 단일 loss의 독립 인과효과는 분리되지 않는다. Soft slicing은 원 segment duration을 사용하며 자동 사건 경계 추정의 성공은 확인하지 않았다. 의미 전용 열을 모든 의미 지표의 보존으로 확대하지 않는다. 새로운 음원·방 분할 일반화와 연속 이동 추적, 겹친 음원 분리, 자유형 QA는 별도 검증이 필요하다.
[이해 확인과 전환]
“사건 순서를 잘 검색하면 움직이는 음원도 잘 추적할까요?”에 대해 평가 대상이 달라 별도 검증이 필요하다고 답을 회수한다.

[시각화 전 표의 수치·조건 보존]
두 합성 FOA 사건 · Global Text-to-Audio 검색 · $E_{\mathrm{global}}\leftrightarrow T_{\mathrm{st}}$의 cosine similarity

CoSTALA 학습 loss | Global T2A R@1 (%) / 높을수록 좋음 | 

대조 학습만 · $L_{\mathrm{cl}}$ | 5.84 | 

전체 · $L_{\mathrm{cl}}+L_{\mathrm{st}}+L_{\mathrm{local}}+L_{\mathrm{consist}}$ | 8.10 |
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->

---
layout: "seminar"
variant: "focus"
chapter: "근거 부록 C · 공간 Audio-LM의 세부 설계"
causalStage: "appendix"
originSlide: 40
---

# 인코더가 같은 관측에서 과제별 특징을 고르게 한다

::body::
<PaperFigure src="/diagrams/p2-s40-feature-selection.png" alt="바이노럴 파형의 여러 특징을 과제별로 가중하고 공유 파라미터의 세 경로로 사건, 방향, 거리를 읽는 구조." caption="설계 재구성 · 가중 막대는 설명용" />

::takeaway::
DSpAST는 **과제별 특징 선택**을 위해 사건·방향·거리의 정보 경로를 나눈다.

::source::
DSpAST, arXiv:2509.13927v1, §3.2·Fig. 1 기반 설명용 재구성 C40.

<!--
[현재 S72 · 근거 부록]
근거 부록 C · 공간 Audio-LM의 세부 설계

[설명의 중심]
DSpAST는 audio feature를 어떻게 선택할지 encoder 단계의 설계다.

[연결]
이 장은 본문의 C · 공간 Audio-LM의 세부 설계 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S72]
[Sources]
- https://arxiv.org/html/2509.13927v1
[시각 자료]
직접 제작한 강의용 벡터 도식을 삽입했다. 원문 결과·예측을 재현한 그림이 아니며 기존 해석 범위와 평가 조건을 유지한다. SVG 원본과 2배 해상도 PNG는 public/diagrams에 보관한다.
[발표 노트]
하나의 바이노럴 관측에 세 종류의 질문을 붙인다. 사건 이름을 구분하는 정보와 방향·거리를 구분하는 정보가 동일한 중요도를 가져야 할 이유는 없다. DSpAST는 여러 입력 특징의 가중과 과제별 분기를 통해 이 차이를 설계에 반영한다. 그림의 공유 backbone은 Transformer와 patch embedding이 파라미터를 공유한다는 뜻이다. 독립된 대형 인코더 세 개로 설명하지 않는다.
[해석 범위]
화면은 §3.2의 설계 의도를 재구성한 개념도다. Fig. 1은 방법 그림이며 Fig. 2의 평균 attention도 단서 사용의 인과 검증은 아니다. 실제 개선에는 추가 특징, 사전학습 curriculum, AdaCos loss 변경이 함께 포함된다.
-->

---
layout: "seminar"
variant: "method"
chapter: "근거 부록 C · 공간 Audio-LM의 세부 설계"
causalStage: "appendix"
originSlide: 43
---

# 기하 지도는 인코더에 배우고, QA에서는 오디오만 읽는다

::body::
<PaperFigure src="/research/p2-owl-v1-fig4.png" alt="OWL Fig. 4 원문 구조. 왼쪽 SAGE의 깊이와 RIR 보조 학습, 오른쪽 바이노럴 오디오를 받는 OWL 추론" caption="왼쪽: depth·RIR로 SAGE 학습. 오른쪽: 고정 음향 인코더 → projector → LLM." />

::takeaway::
**기하 지도는 인코더 학습에**, projector·LoRA는 그 표현을 사용하는 QA 학습에 쓴다.

::source::
OWL, arXiv:2509.26140v1, Fig. 4. 원문 구조도.

<!--
[현재 S73 · 근거 부록]
근거 부록 C · 공간 Audio-LM의 세부 설계

[설명의 중심]
OWL은 SAGE 표현 학습과 frozen encoder→projector→LLM LoRA QA 학습을 분리한다.

[연결]
이 장은 본문의 C · 공간 Audio-LM의 세부 설계 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S73]
[Sources]
- https://arxiv.org/html/2509.26140v1
[발표 노트]
원문 왼쪽 SAGE와 오른쪽 OWL을 구분한다. SAGE에서는 깊이와 음향 표현으로 RIR을 복원하는 보조 학습이 음향 표현에 영향을 준다. OWL의 추론 경로에는 바이노럴 음향 인코더가 만든 표현이 남고, 이를 projector로 언어 모델에 연결한다. OWL QA 학습에서는 SAGE 음향 인코더를 고정하고 projector와 LLM LoRA를 학습한다.
[해석 범위]
학습 그림의 depth와 RIR을 추론 입력 목록에 넣지 않는다. 구조도는 어떤 경로를 설계했는지 보여 주며 그 자체가 기하 이해 성공의 근거는 아니다. Q-Former 상세와 CoT curriculum의 효과는 본문의 loss 비교와 구분한다.
-->

---
layout: "seminar"
variant: "focus"
chapter: "근거 부록 C · 공간 Audio-LM의 세부 설계"
causalStage: "appendix"
originSlide: 45
---

# 좌우 음량만 주는 입력으로 무엇을 시험하나?

::body::
<PaperFigure src="/diagrams/p2-s45-gain-waveforms.png" alt="동일한 파형에서 좌우 gain만 바꾼 Left, Center, Right의 세 예. 파형의 시간 구조는 유지되고 진폭만 변한다.">
  <template #caption><MathInline tex="L=g_L\,x" /> · <MathInline tex="R=g_R\,x" /> · 같은 모노 원음, gain만 변경 · 두 BEATs 경로 고정</template>
</PaperFigure>

::takeaway::
Dual-BEATs는 **제한된 좌우 레벨 차이**를 읽는 stereo 분류를 다룬다.

::source::
Dual-BEATs, arXiv:2607.08800v1, §3.2·Appendix A.3 기반 설명용 재구성 C45.

<!--
[현재 S74 · 근거 부록]
근거 부록 C · 공간 Audio-LM의 세부 설계

[설명의 중심]
Dual-BEATs의 amplitude panning은 실제 배열의 위상·기하 입력과 다른 제한된 관측이다.

[연결]
이 장은 본문의 C · 공간 Audio-LM의 세부 설계 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S74]
[Sources]
- https://arxiv.org/html/2607.08800v1
[시각 자료]
직접 제작한 강의용 벡터 도식을 삽입했다. 원문 결과·예측을 재현한 그림이 아니며 기존 해석 범위와 평가 조건을 유지한다. SVG 원본과 2배 해상도 PNG는 public/diagrams에 보관한다.
Csound FLOSS Manual의 Panning and Spatialization 장에서 같은 신호를 채널별 이득으로 나누는 설명 방식을 참고했다: https://www.csound-tutorial.net/floss_manual/Release04/Cs_FM_04_ScrapBook/b-panning-and-spatialization.html . 그림의 진폭 비는 설명용이며 논문의 gain 범위나 pan law를 수치로 재현하지 않았다.
[발표 노트]
이번에는 방이나 실제 마이크 배열을 추정하는 문제를 잠시 내려놓고 입력 생성 조건을 제한한다. 하나의 모노 원음에 좌우 gain을 적용한다. 소리 내용은 같지만 채널 크기가 달라지고, 모델은 Left/Center/Right를 분류한다. 고정된 두 BEATs 경로가 각각 좌우 채널을 읽으며 projector와 언어 adaptation은 학습한다. 화면은 입력을 만드는 방법의 설명이고 실제 공간 신호나 모델 출력 그래프가 아니다.
[해석 범위]
amplitude panning을 HRTF가 반영된 물리적 방향 변화, 위상 활용, 방 잔향 또는 새로운 배열 전이와 동일시하지 않는다. 정규화가 어떤 단서를 지웠는지의 기전은 결과표 하나로 입증되지 않는다.
-->

---
layout: "seminar"
variant: "result"
chapter: "근거 부록 C · 공간 Audio-LM의 세부 설계"
causalStage: "appendix"
originSlide: 46
---

# 전처리가 단서를 바꾸면 점수도 달라진다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">OLMo-3-7B + Dual-BEATs · Direction-First · 방향 정확도 (%) ↑</p>
<PaperFigure src="/diagrams/result-46.svg" alt="PA = 0.00, PA = 0.50 원문 수치 비교 그래프. Dither Off: 99.5, 37.9; Dither On · DA = 0.05: 99.0, 97.1" />
</div>

::takeaway::
PA = 0.50에서는 크게 개선됐고, **PA = 0.00에서는 소폭 낮아졌다.**

::source::
Dual-BEATs, arXiv:2607.08800v1, Table 1. ↑ 높을수록 좋음. On: 채널별 독립 dither.

<!--
[현재 S75 · 근거 부록]
근거 부록 C · 공간 Audio-LM의 세부 설계

[설명의 중심]
Dual-BEATs의 dither 효과는 panning 조건에 의존한다.

[연결]
이 장은 본문의 C · 공간 Audio-LM의 세부 설계 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S75]
[Sources]
- https://arxiv.org/html/2607.08800v1
[발표 노트]
같은 backbone과 출력 순서를 고정하고 각 PA 안에서 dither Off와 On을 읽는다. PA=0.50은 약한 채널의 gain이 0.5인 조건이며 Center를 뜻하지 않는다. 독립 dither의 진폭 DA는 0.05다. 이 조건의 방향 정확도는 37.9에서 97.1%로 높아진다. 반면 PA=0.00에서는 99.5에서 99.0%로 소폭 낮아진다. 따라서 모든 PA에서 일률적 이득이라고 말하지 않는다.
[해석 범위]
표의 97.1을 사용하며 초록의 97.2와 혼합하지 않는다. 학습·평가 random seed는 분리되지만 미관측 panning의 일반화가 새 HRTF·배열·잔향 전이는 아니다. semantic F1 저하 역시 공간 성과에 묻어 없애지 않는다. Table 1과 Fig. 2의 학습·평가 PA 조건은 구분해야 한다.

[시각화 전 표의 수치·조건 보존]
OLMo-3-7B + Dual-BEATs · Direction-First · 방향 정확도 (%) ↑

평가 PA | Dither Off | Dither On / DA = 0.05 | 

0.00 | 99.5 | 99.0 | 

0.50 | 37.9 | 97.1 |
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "근거 부록 C · 공간 Audio-LM의 세부 설계"
causalStage: "appendix"
originSlide: 42
---

# 방 기하 지도는 학습 때만 사용할 수 있다

::body::
<PaperFigure src="/research/p2-owl-v1-fig2.png" alt="BiDepth 원문 Fig. 2. 청취자 관점 깊이 영상과 같은 장면의 바이노럴 음향 시뮬레이션" caption="왼쪽: 깊이 지도. 오른쪽: 청취자·음원 배치와 바이노럴 합성 장면." />

::aside::
<section><span class="seminar-label semantic-geometry">학습할 때</span><p>깊이와 RIR 정답으로<br/>기하적 제약을 제공</p></section><section><span class="seminar-label semantic-input">추론할 때</span><p>바이노럴 오디오와<br/>언어 질문을 제공</p></section>

::takeaway::
**깊이·RIR은 학습 지도**, 질문에 답할 때의 관측은 바이노럴 오디오다.

::source::
OWL, arXiv:2509.26140v1, Fig. 2. 원문 그림.

<!--
[현재 S76 · 근거 부록]
근거 부록 C · 공간 Audio-LM의 세부 설계

[설명의 중심]
OWL의 depth/RIR은 표현 학습용이고 QA 추론의 추가 시각 입력이 아니다.

[연결]
이 장은 본문의 C · 공간 Audio-LM의 세부 설계 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S76]
[Sources]
- https://arxiv.org/html/2509.26140v1
[발표 노트]
소리는 음원뿐 아니라 방과 전파 경로에 의해 달라진다. BiDepth는 같은 청취 위치에서 기하와 음향을 연결하는 합성 데이터다. 왼쪽의 depth는 청취자 관점의 공간 기하를, 오른쪽은 청취자와 음원 배치에 따른 바이노럴 관측을 나타낸다. SAGE는 이런 학습 장면의 depth와 RIR 정보를 보조 지도에 사용한다.
[해석 범위]
깊이 영상을 추론 시에도 제공하는 시청각 QA로 소개하지 않는다. 합성 장면의 기하 지도를 이용한 학습과 실제 방에서의 일반화는 별개다. 저자가 기술한 room/source 분할이 곧 현실 환경 전반의 일반화 보장은 아니다.
-->

---
layout: "seminar"
variant: "focus"
chapter: "근거 부록 C · 공간 Audio-LM의 세부 설계"
causalStage: "appendix"
originSlide: 50
---

# 사건 이름과 속성을 같은 음원에 묶는다

::body::
<PaperFigure src="/diagrams/p2-s50-scene-attributes.png" alt="방 안의 알람과 말소리에서 청취자로 이어지는 방향과 거리, 음원별 발생 구간, 방과 배경 속성의 연결." caption="출력 형식 재구성 · 실제 생성 응답 아님" />

::takeaway::
각 소리의 내용·시간·공간 속성이 **같은 음원에 붙어 있어야** 설명이 일관된다.

::source::
Sci-Phi, arXiv:2510.05542v1, §3.3 출력 형식 기반 설명용 재구성 C50.

<!--
[현재 S77 · 근거 부록]
근거 부록 C · 공간 Audio-LM의 세부 설계

[설명의 중심]
Sci-Phi는 종류·방향·거리를 같은 source record에 묶는 요구를 다룬다.

[연결]
이 장은 본문의 C · 공간 Audio-LM의 세부 설계 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S77]
[Sources]
- https://arxiv.org/html/2510.05542v1
[시각 자료]
직접 제작한 강의용 벡터 도식을 삽입했다. 원문 결과·예측을 재현한 그림이 아니며 기존 해석 범위와 평가 조건을 유지한다. SVG 원본과 2배 해상도 PNG는 public/diagrams에 보관한다.
[발표 노트]
Sci-Phi는 질문 하나의 짧은 답 대신 장면 전체의 속성을 한 번에 생성한다. 방향성 음원마다 설명, 발생 구간, 방향, 거리, 음압, 명료도를 연결하고 비방향성 배경과 방 특성은 장면 단위로 기술한다. 화면의 항목은 출력 형식을 설명하며 모델이 실제로 생성한 응답은 아니다. 데이터의 방향성 음원 수는 최대 네 개다.
[해석 범위]
방과 배경 속성은 모델이 추정하는 값이다. 이를 직접 관측된 사실처럼 읽거나 모든 자유형 장면에 검증된 출력으로 확대하지 않는다. 각 필드를 따로 맞히는 것과 같은 음원에 올바로 대응시키는 것은 다르다. 예를 들어 알람의 왼쪽 위치를 말소리에 붙이면 소리 목록과 방향 목록은 맞아도 장면 기술이 틀리다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "근거 부록 C · 공간 Audio-LM의 세부 설계"
causalStage: "appendix"
originSlide: 52
---

# 속성이 맞아도 음원을 잘못 연결하면 틀린 답이다

::body::
<PaperFigure src="/research/p2-sciphi-v1-tuplescore.png" alt="Sci-Phi Fig. 2 TupleScore 원본 패널. SELDNet+Phi-4 MC FT와 Sci-Phi의 합성 RIR 및 실측 RIR 조건, diamond는 1–4음원 평균" caption="원본 점·축 보존. 오른쪽 두 모델의 ◆·◇(1–4음원 평균)를 비교한다." />

::aside::
<section><span class="seminar-label ">TupleScore · 0–1, 높을수록 좋음</span><p>What × Where × When의<br/>기하평균</p></section><section><span class="seminar-label semantic-geometry">RIR 조건을 분리</span><p>◆ 합성 RIR<br/>◇ 실측 RIR로 합성</p></section><section><span class="seminar-label ">이번에 읽는 비교</span><p>SELDNet+Phi-4 (MC, FT)<br/>↔ Sci-Phi</p></section>

::takeaway::
같은 RIR 조건에서 **Sci-Phi의 평균 TupleScore가 미세조정 기준선보다 높다.**

::source::
Sci-Phi, arXiv:2510.05542v1, Fig. 2 TupleScore 패널 크롭·§4. 정밀값을 추정해 재작성하지 않음.

<!--
[현재 S78 · 근거 부록]
근거 부록 C · 공간 Audio-LM의 세부 설계

[설명의 중심]
Sci-Phi TupleScore는 What×Where×When의 결속을 보며 단순히 속성 정답 수만 세지 않는다.

[연결]
이 장은 본문의 C · 공간 Audio-LM의 세부 설계 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S78]
[Sources]
- https://arxiv.org/html/2510.05542v1
[발표 노트]
먼저 이름과 방향을 바꿔 붙인 예를 떠올린다. 알람은 왼쪽이고 말소리는 오른쪽인데 출력이 이 연결을 뒤집었다면 이름 목록과 방향 목록이 각각 맞아도 장면 설명은 틀리다. TupleScore는 What·Where·When의 기하평균으로 음원 단위 공통 대응을 정한다. 원문 패널의 오른쪽 두 모델, SELDNet+Phi-4 (MC, FT)와 Sci-Phi를 선택한다. ◆는 synthetic-RIR, ◇는 real-RIR의 1–4음원 전체 평균이다. 두 조건 모두 Sci-Phi의 평균이 더 높다.
[해석 범위]
원본 축과 점을 보존하기 위해 mono 및 ○·□도 남겼지만 이 장의 비교는 두 모델의 diamond에 한정한다. ○는 한 음원, □는 네 음원이며 평균으로 읽지 않는다. 두 모델 모두 장면 기술에 미세조정했고 baseline은 공간 encoder 고정, Sci-Phi는 적응한다. 실측 RIR은 실제 배경을 더해 합성한 장면이지 현장 혼합음 녹음이 아니다. real-RIR는 수평 방향 위주이며 방 크기와 배경 라벨이 없다. Table 2의 OM/OS는 채점 원칙이고 모델 ablation이 아니다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "근거 부록 C · 공간 Audio-LM의 세부 설계"
causalStage: "appendix"
originSlide: 56
---

# 지각·음원 결속·복합 질의를 나눠 측정한다

::body::
<div style="display:grid;grid-template-columns:480px 1fr;gap:38px;height:100%">
<PaperFigure src="/research/p2-twnm-v3-scene.png" alt="TWNM Fig. 4의 청취자 중심 장면 부분. 음원과 방향의 관계를 나타내는 설명 도해" caption="원문 Fig. 4 장면 크롭 · 모델 입력이나 생성 결과가 아닌 개념 예시" />
<div style="display:flex;flex-direction:column;justify-content:center;gap:23px">
<section><span class="seminar-label">L1 · 지각</span><p>어떤 소리가 들리는가?</p></section>
<section><span class="seminar-label">L2 · 음원과 속성 연결</span><p>어떤 소리가 그 위치에 있는가?</p></section>
<section><span class="seminar-label">L3 · 질문 조건을 적용</span><p>청취자 방향이 바뀌면 답도 바뀌는가?</p></section>
<p class="seminar-figure-note">질문은 평가 정의를 설명하는 재구성이다.</p>
</div></div>

::takeaway::
세 층위는 **무엇을 평가하는지의 구분**이며, 모델이 출력하는 명시적 그래프가 아니다.

::source::
The World is Not Mono, arXiv:2601.02954v3, Fig. 4 장면 부분·§3.

<!--
[현재 S79 · 근거 부록]
근거 부록 C · 공간 Audio-LM의 세부 설계

[설명의 중심]
TWNM의 질문 수준은 LLM 학습 후의 trade-off를 펼쳐 보는 기준이다.

[연결]
이 장은 본문의 C · 공간 Audio-LM의 세부 설계 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S79]
[Sources]
- https://arxiv.org/html/2601.02954v3
[발표 노트]
같은 청취자 기준의 장면에서 필요한 답의 종류를 차례로 바꾼다. L1은 사건 종류나 위치 같은 개별 관측을 읽고, L2는 어떤 속성이 어느 음원에 속하는지 연결한다. L3는 관찰자 회전, 음원 제거, 복합 조건 등의 질문을 적용한다. 화면의 그림은 Fig. 4에서 청취자 중심 장면을 선택한 도해이며 오른쪽은 과제 정의를 설명하는 한국어 질문이다.
[해석 범위]
원문 도해는 네 개의 기호를 보이는 개념 예시지만 실제 모델의 source slots와 주평가 합성 장면은 최대 세 음원이다. 예시 그림과 숨겨진 scene metadata는 모델의 추론 입력이 아니다. 정답 생성에 사용하는 metadata와 audio-only 질문 입력을 구분한다. 그래프 기호는 평가 목표의 정의이며 명시적 scene graph 출력이 아니다. L3 점수를 순수 공간 추론 능력 전체로 해석하지 않는다.
-->

---
layout: "seminar"
variant: "focus"
chapter: "근거 부록 D · 시간 정보의 전달"
causalStage: "appendix"
originSlide: 59
---

# 시간을 줄이기 전에 질문이 요구하는 정보를 정한다

::body::
<PaperFigure src="/diagrams/p2-s59-time-requirements.png" alt="사건의 시간 막대, 한 음원의 연속 위치 곡선, 질문 관련 시간 구간을 나란히 보여 주는 세 시간 관계." caption="설명용 시간축 · 실제 모델 예측 아님" />

::takeaway::
**순서·연속 이동·질의 구간**은 서로 다른 시간 정보의 요구다.

::source::
Motion 2025, arXiv:2509.14666v1, Table 1; Dynamic QA, arXiv:2602.16334v1, Table 2 기반 C59.

<!--
[현재 S80 · 근거 부록]
근거 부록 D · 시간 정보의 전달

[설명의 중심]
사건 순서·연속 궤적·질문 관련 구간을 구분한다.

[연결]
이 장은 본문의 D · 시간 정보의 전달 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S80]
[Sources]
- https://arxiv.org/html/2509.14666v1
- https://arxiv.org/html/2602.16334v1
[시각 자료]
직접 제작한 강의용 벡터 도식을 삽입했다. 원문 결과·예측을 재현한 그림이 아니며 기존 해석 범위와 평가 조건을 유지한다. SVG 원본과 2배 해상도 PNG는 public/diagrams에 보관한다.
[발표 노트]
알람이 말소리보다 먼저 울렸는지는 사건 순서다. 같은 알람의 위치가 왼쪽에서 오른쪽으로 바뀌었는지는 연속 이동이다. 알람이 울린 특정 구간에만 답해야 하는 경우는 질문 관련 시간 선택이다. 이 세 질문은 시간 이해라는 말 안에 함께 들어갈 수 있지만 서로 다른 관측과 평가가 필요하다.
[해석 범위]
화면은 논문의 질문 범주를 설명하기 위한 재구성이지 실제 오디오나 예측 궤적이 아니다. 두 사건이 순서대로 발생했다고 해서 한 음원이 이동한 것은 아니다. 세 축을 발전 단계나 성능 순위로 만들지 않는다. 본문에서 Motion과 Dynamic QA는 움직임·구간 선택, ST-AudioLM은 시간별 공간 상태를 다뤘다. 근거 부록의 CoSTALA는 사건 순서의 검색을 다룬다.
-->

---
layout: "seminar"
variant: "focus"
chapter: "근거 부록 D · 시간 정보의 전달"
causalStage: "appendix"
originSlide: 62
---

# 교차하는 궤적에도 음원 정체성이 남아야 한다

::body::
<PaperFigure src="/diagrams/p2-s62-source-trajectories.png" alt="시간을 따라 교차하는 알람 A와 말소리 B의 좌우 위치 곡선. 나중 시점에서 A는 오른쪽, B는 왼쪽에 있다." caption="좌우 위치–시간 재구성 · 실제 예측 아님" />

::takeaway::
각 순간의 위치를 넘어 **음원 정체성과 시간별 공간 상태**를 함께 유지해야 한다.

::source::
ST-AudioLM, arXiv:2606.14141v1, ST-AudioQA Table 1 기반 설명용 재구성 C62. 실제 예측 아님.

<!--
[현재 S81 · 근거 부록]
근거 부록 D · 시간 정보의 전달

[설명의 중심]
ST-AudioLM이 시간별 source 상태를 전달해야 하는 이유다.

[연결]
이 장은 본문의 D · 시간 정보의 전달 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S81]
[Sources]
- https://arxiv.org/html/2606.14141v1
[시각 자료]
직접 제작한 강의용 벡터 도식을 삽입했다. 원문 결과·예측을 재현한 그림이 아니며 기존 해석 범위와 평가 조건을 유지한다. SVG 원본과 2배 해상도 PNG는 public/diagrams에 보관한다.
[발표 노트]
한 시점의 방향 추정이 맞아도 다음 시점에 음원 정체성이 바뀌면 관계 질문을 틀릴 수 있다. 화면에서 알람 A와 말소리 B는 계속 같은 이름을 유지한다. 질문은 특정 소리가 움직인 뒤의 관계를 요구하므로 음원 정체성, 참조 시점, 시간별 공간 상태를 함께 읽어야 한다. 그림의 방향은 이해를 위한 단순 예이며 실제 모델 궤적이나 생성 결과가 아니다.
[해석 범위]
ST-AudioQA는 통제된 한·두 음원 합성 장면으로 구성한다. 이런 성과를 밀집한 현실 동적 장면이나 연속 대화의 해결로 확대하지 않는다. 정적인 위치 설명과 움직임에 조건을 둔 관계 질문은 서로 다른 출력 요구다.
-->

---
layout: "seminar"
variant: "result"
chapter: "근거 부록 E · 답변의 근거"
causalStage: "appendix"
originSlide: 69
---

# 선택형 점수는 우연 기준부터 확인한다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">세 선택지 MCQA · Gemini 2.5 Pro, 2025년 6월 업데이트 · AA (%) ↑</p>
<PaperFigure src="/diagrams/result-69.svg" alt="Localization, Relation, Trajectory 원문 수치 비교 그래프. 무작위 선택: 33.33, 33.33, 33.33; Gemini 2.5 Pro: 40.87, 48.97, 45.28" />
<p class="seminar-chart-note">AA: 반복 prompt 변형 실행의 평균 정확도</p>
</div>

::takeaway::
보고된 버전은 우연 기준보다 높았으며, <strong>공간 과제마다 점수가 달랐다.</strong>

::source::
STAR-Bench, arXiv:2510.24693v2, Table 2 선택 열. ↑ 높을수록 좋음.

<!--
[현재 S82 · 근거 부록]
근거 부록 E · 답변의 근거

[설명의 중심]
STAR의 random guess는 question-only model과 다른 기준이다.

[연결]
이 장은 본문의 E · 답변의 근거 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S82]
[Sources]
- https://arxiv.org/html/2510.24693v2
[청중 질문]
벤치마크의 낮은 평균은 어떤 종류의 질문에서 나온 것인가?
[발표 노트]
평가 모델의 버전과 질문 형식을 먼저 밝힌다. 우연 기준선을 읽고 과제별 점수를 비교한다. AA는 반복 실행 평균이고 ACR는 매번 맞힌 문항 비율임을 한 문장으로 구별한다.
이 표는 audio/caption ablation 결과표가 아니다. ACR는 모든 반복 실행에서 맞힌 문항의 비율이며 AA와 구별한다. 통계적 유의성, 위상 처리 기전 또는 최신 모든 모델의 능력을 이 숫자만으로 결론내리지 않는다.
[해석 범위]
숫자는 효과의 통계적 유의성이나 phase 사용을 입증하지 않는다. BAT의 0점 등을 기전 붕괴의 증거로 크게 쓰지 않는다. 서로 다른 입력 지원·전처리·응답 형식 적합성이 개입할 수 있다. 전체 19모델 순위표와 ACR는 원문의 추가 자료이다.

[시각화 전 표의 수치·조건 보존]
세 선택지 MCQA · Gemini 2.5 Pro, 2025년 6월 업데이트 · AA (%) ↑평가 조건 | Localization | Relation | Trajectory | 
무작위 선택 | 33.33 | 33.33 | 33.33 | 
Gemini 2.5 Pro | 40.87 | 48.97 | 45.28 | 
AA: 반복 prompt 변형 실행의 평균 정확도
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->

---
layout: "seminar"
variant: "method"
chapter: "근거 부록 E · 답변의 근거"
causalStage: "appendix"
originSlide: 70
---

# 현장에서는 말의 내용과 응답 대상이 갈린다

::body::
<PaperFigure src="/research/wearvox-side-talk-panel.png" alt="착용자의 발화가 기기에게 향한 것인지 다른 사람에게 향한 것인지 구별하는 side-talk 사례" caption="WearVox Fig. 1의 side-talk rejection 문제 패널." />

::aside::
<section><span class="seminar-label">기기에게 한 말</span><p>응답</p></section><section><span class="seminar-label">주변 사람끼리의 말</span><p>비응답</p></section>

::takeaway::
실제 착용자 장면에서는 <strong>발화의 응답 대상</strong>을 구별해야 한다.

::source::
WearVox, arXiv:2601.02391v1, Fig. 1의 side-talk 패널 크롭.

<!--
[현재 S83 · 근거 부록]
근거 부록 E · 답변의 근거

[설명의 중심]
WearVox는 내용 전사만으로 해결되지 않는 기기 응답 대상의 문제를 보여 준다.

[연결]
이 장은 본문의 E · 답변의 근거 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S83]
[Sources]
- https://arxiv.org/html/2601.02391v1
[청중 질문]
인식 가능한 말이 들렸다는 이유만으로 음성 기기가 응답해야 하는가?
[발표 노트]
기기를 향한 발화와 주변 사람끼리의 대화를 대비한다. 내용 인식은 두 경우 모두 가능해도 요구 출력은 응답/비응답으로 다름을 설명한다. 웨어러블 실제 녹음과 앞 합성 공간 QA의 평가 조건 차이를 짚는다.
사용자 발화의 의미와 방향·채널 관측이 어떤 정보를 제공할 수 있는지 문제를 설명한다. 문제 그림 자체를 정확도나 특정 모델의 성공 사례로 해석하지 않는다.
[해석 범위]
WearVox를 앞 공간 LLM들의 실환경 전이 시험이라고 소개하지 않는다. 실제 사용 조건이라는 별도 검증 축이다. 주변 대화의 의도를 음향만으로 언제나 유일하게 알 수 있다고도 하지 않는다.
[시각화 전 상세 본문 — 발표 설명용 보존]
WearVox Fig. 1의 side-talk rejection 문제 패널.


[보조 설명]
내용만으로는 부족한 질문발화를 전사해도
누구에게 한 말인지는 남는다.

요구하는 출력응답할 발화인지
주변 대화인지 판단한다.


[핵심 결론]
실제 착용자 장면에서는 발화의 응답 대상을 구별해야 한다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "근거 부록 E · 답변의 근거"
causalStage: "appendix"
originSlide: 72
---

# 고정 인코더 위에 선형 판독기만 학습한다

::body::
<PaperFigure src="/diagrams/p3-sarl-linear-readout.svg" alt="합성 공간 장면이 고정 오디오 인코더를 지나고 시간 평균 표현에서 사건, 방위, 고도, 거리, 잔향, 부피, 형상을 각각 선형 판독하는 구조" caption="SARL 프로토콜 재구성 · 모델별 입력 형식 · 판독 20 epochs · 무작위 0, 완전 1" />

::takeaway::
<strong>인코더는 고정하고, 공간 요인의 판독기만 학습한다.</strong>

::source::
SARL, arXiv:2606.05544v2, §3·Table 1 기반 프로토콜 재구성.

<!--
[현재 S84 · 근거 부록]
근거 부록 E · 답변의 근거

[설명의 중심]
SARL의 linear accessibility는 인코더를 고정하고 라벨로 판독기를 학습한 증거다.

[연결]
이 장은 본문의 E · 답변의 근거 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S84]
[Sources]
- https://arxiv.org/html/2606.05544v2
[청중 질문]
같은 음원도 위치·방이 달라질 때 인코더에 어떤 정보가 남는가?
[발표 노트]
S18의 고정/학습 범위를 회수한다. 범주 과제의 macro-F1과 연속량을 구간화한 판독 점수를 설명한다. 마지막으로 무작위 기준 0, 완전 성능 1의 정규화가 raw accuracy가 아님을 밝힌다.
범주 과제는 macro-F1, 연속량은 구간화·soft label 후 1−MAE/R을 계산하며 무작위 기준 b에 대해 (x−b)/(1−b)로 정규화한다. raw accuracy가 아니다. source와 room 과제군의 생성 파이프라인도 다르며, 한 요인의 낮은 선형 점수는 pooling 전 정보나 비선형 판독 가능성까지 부정하지 않는다.
[해석 범위]
source와 room 과제군은 생성 파이프라인도 달라 순수 요인 난이도만 비교하는 것이 아니다. 하나의 낮은 점수로 pooling 전 정보나 비선형 판독 가능성까지 부정하지 않는다. 수식과 모델별 입력 목록은 원문의 추가 자료이다.
[시각화 전 상세 본문 — 발표 설명용 보존]
관측단일 음원 10초 합성 오디오 · 모델별 전처리

고정하는 부분오디오 인코더 · 시간 평균 pooling

학습하는 부분요인별 선형 판독기 · 20 epochs


[보조 설명]
읽는 요인사건, 방향, 거리
\mathrm{RT}_{60} , 방 부피, 형상

점수의 기준무작위 = 0
완전 성능 = 1


[핵심 결론]
선형 판독은 특정 pooling 뒤에서 정보가 얼마나 쉽게 읽히는지 시험한다.
-->

---
layout: "seminar"
variant: "result"
chapter: "근거 부록 E · 답변의 근거"
causalStage: "appendix"
originSlide: 76
---

# 단서를 제거하며 남은 반응의 원인을 좁힌다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">GRAM-T · 20개 주파수 × SNR cell 중 유의한 반응 비율 (%)</p>
<PaperFigure src="/diagrams/result-76.svg" alt="유의한 반응 비율 (%) 원문 수치 비교 그래프. 원신호: 100, 0; 고역통과 > 2 kHz: 100, 0; Mel 대역 ILD 제거: 100, 0; 50 Hz 포락선 vocoding: 50, 25" />
<p class="seminar-chart-note">Vocoded 75% = 50% + 25% · 정확도가 아닌 유의 반응 비율</p>
</div>

::takeaway::
파형 변형의 부수 변화까지 고려해 <strong>가능한 설명의 범위</strong>를 좁힌다.

::source::
Interference/BMLD, arXiv:2606.14820v1, Fig. 3의 GRAM-T 원문 값 재작성.

<!--
[현재 S85 · 근거 부록]
근거 부록 E · 답변의 근거

[설명의 중심]
BMLD 단서 제거는 표현의 반응을 설명하며 accuracy를 재는 실험이 아니다.

[연결]
이 장은 본문의 E · 답변의 근거 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S85]
[Sources]
- https://arxiv.org/html/2606.14820v1
[청중 질문]
위상 조건 반응이 다른 간섭 단서에도 의존한다면 어디까지 주장할 수 있는가?
[발표 노트]
무엇을 변형했는지 먼저 설명한다. 예를 들어 vocoded 75%는 50% unmasking+25% reversal이며 정확도75%가 아님을 읽는다. 파형 변형의 부수 변화도 있으므로 ‘phase 사용 증명’과 ‘phase가 전혀 없음’ 양쪽 단정을 피한다.
Unmasking은 양의 유의 반응, reversal은 음의 유의 반응이다. 두 비율을 분리해야 total 75%를 성능 정확도로 잘못 읽지 않는다. 원문 그림의 GRAM-T 네 조건과 양·음 방향을 표로 재작성했다. 파형 조작은 하나의 내부 기전을 유일하게 복원하지 않으며, phase 사용의 완전한 증명이나 phase 정보 부재로 단정하지 않는다. 추가 채널별 대조, 같은 parser 조건, 다른 pooling·판독은 후속 통제 제안이며 이 슬라이드가 보고하는 실행 결과가 아니다.
[해석 범위]
후속 제안으로 제시한 채널별 대조·동일 parser·추가 pooling/판독 실험은 미실행이다. 이 결과는 배열 일반화나 모든 질문 응답 모델의 인과 추론을 시험하지 않는다. 상세 유의성 검정은 원문의 추가 자료이다.

[시각화 전 표의 수치·조건 보존]
GRAM-T · 20개 주파수 × SNR cell 중 유의한 반응 비율 (%)파형 조건 | Unmasking | Reversal | 
원신호 | 100 | 0 | 
고역통과 > 2 kHz | 100 | 0 | 
Mel 대역 ILD 제거 | 100 | 0 | 
50 Hz 포락선 vocoding | 50 | 25 | 
Vocoded 75% = 50% + 25% · 75% 정확도를 뜻하지 않는다.
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->
