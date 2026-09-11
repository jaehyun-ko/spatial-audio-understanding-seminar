---
layout: "seminar-cover"
transition: "none"
causalStage: "main"
originSlide: 1
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
