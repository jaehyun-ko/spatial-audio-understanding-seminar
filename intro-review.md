---
theme: default
title: '도입부 2–7 · 공간 관측'
aspectRatio: 16/9
canvasWidth: 1280
colorSchema: light
transition: none
routerMode: hash
mdc: true
fonts:
  sans: Seminar Pretendard
  provider: none
layout: seminar
variant: figure
---

# 공간 오디오 이해의 목표

::body::
<ManimScene src="/animations/intro-sequence/s02.mp4" webm="/animations/intro-sequence/s02.webm" poster="/animations/intro-sequence/s02-start.png" print-poster="/animations/intro-sequence/s02-end.png" description="공간 오디오 이해의 목표: 같은 3차원 장면을 유지하는 설명용 애니메이션" />

::takeaway::
음원의 종류와 위치: 방위각·고도각·거리

::source::
MathWorks, Spherical Coordinates. 목표 좌표 정의이며 단일 TDoA의 3차원 복원을 뜻하지 않음.

<!--
[S02 발표 노트]
일반 음원 s(t)의 종류와 위치를 알아내는 것이 목표다. O는 마이크 쌍의 중점이고 M1=(-d/2,0,0), M2=(d/2,0,0)이다. 방위각 α는 xy 평면에서 +x에서 +y 방향, 고도각 β는 xy 평면에서 +z 방향, 거리 r는 O에서 음원까지의 유클리드 거리다. 두 마이크의 단일 도달 시간차만으로 세 좌표가 유일하게 복원되는 것은 아니다. 3차원 위치는 공통 사투영으로 표시하고 물리량은 투영 전 좌표로 계산한다. 다음에는 이 장면이 실제 입력 신호에 어떻게 나타나는지 본다.

[Sources]
- https://www.mathworks.com/help/phased/ug/spherical-coordinates.html
-->

---
layout: seminar
variant: figure
transition: none
---

# 두 채널 관측 신호

::body::
<ManimScene src="/animations/intro-sequence/s03.mp4" webm="/animations/intro-sequence/s03.webm" poster="/animations/intro-sequence/s03-start.png" print-poster="/animations/intro-sequence/s03-end.png" description="두 채널 관측 신호: 같은 3차원 장면을 유지하는 설명용 애니메이션" />

::takeaway::
같은 음원에서 출발한 소리, 서로 다른 두 관측

::source::
AGG-RL, ICLR 2026, Fig. 1(a) 기반 재구성. 직접음 모델 · 설명용 합성 신호 · 진폭 임의 단위.

<!--
[S03 발표 노트]
음원과 마이크의 위치를 유지한 채 전파 경로와 두 관측 파형을 동시에 보여준다. 각 경로 위 이동점과 파형의 노출은 같은 전파 시간으로 갱신된다. 이동점은 펄스의 기준 시점인 중심을 추적한다. ℓ_m=||p_s-p_m||, t_m=ℓ_m/c, c=343 m/s이며 직접음 신호는 x_m(t)=a_m s(t-t_m)이다. 진폭은 임의 단위이고 시간축은 ms다. 실제 녹음이나 모델의 예측 결과가 아닌 교육용 펄스다. 원문 Fig. 1(a)는 원거리 평면파를 설명하며 이 재구성은 유한 거리의 정확한 경로 길이로 그 관계를 설명한다. 다음에는 음원 위치를 움직여 두 관측의 차이를 확인한다.

[Sources]
- https://proceedings.iclr.cc/paper_files/paper/2026/file/ee860a9fa65a55a335754c557a5211de-Paper-Conference.pdf
-->

---
layout: seminar
variant: figure
transition: none
---

# 경로 차이와 시간차

::body::
<ManimScene src="/animations/intro-sequence/s04.mp4" webm="/animations/intro-sequence/s04.webm" poster="/animations/intro-sequence/s04-start.png" print-poster="/animations/intro-sequence/s04-end.png" description="경로 차이와 시간차: 같은 3차원 장면을 유지하는 설명용 애니메이션" />

::takeaway::
경로 차이에 따라 달라지는 도달 시간차

::source::
AGG-RL, ICLR 2026, Fig. 1(a), §2.1 기반. τ=t₂−t₁의 부호 관례 · 단일 직접음.

<!--
[S04 발표 노트]
거리 r와 고도각 β를 유지하고 방위각만 바꾼다. ℓ1, ℓ2, 도착 시점 t1, t2와 파형을 하나의 기하 상태에서 다시 계산한다. τ=t2-t1=(ℓ2-ℓ1)/c이므로 M2에 먼저 도착하면 τ가 음수다. 음원이 x<0인 방향으로 움직이면 부호가 반대로 바뀐다. 음원 위치가 정지한 각 상태를 비교하는 준정적 설명이며 이동 음원의 도플러 효과를 시뮬레이션하지 않는다. 다음에는 반사 경로와 다른 음원의 기여를 추가한다.

[Sources]
- https://proceedings.iclr.cc/paper_files/paper/2026/file/ee860a9fa65a55a335754c557a5211de-Paper-Conference.pdf
-->

---
layout: seminar
variant: figure
transition: none
---

# 잔향과 음원 혼합

::body::
<ManimScene src="/animations/intro-sequence/s05.mp4" webm="/animations/intro-sequence/s05.webm" poster="/animations/intro-sequence/s05-start.png" print-poster="/animations/intro-sequence/s05-end.png" description="잔향과 음원 혼합: 같은 3차원 장면을 유지하는 설명용 애니메이션" />

::takeaway::
직접음에 더해지는 반사음과 다른 음원의 기여

::source::
CCSR, arXiv:2312.00476v2, Fig. 1과 신호 모델 기반. 1차 벽 반사·두 음원의 설명용 확장.

<!--
[S05 발표 노트]
앞 장면에 벽과 1차 반사 경로를 추가하고, 다음으로 두 번째 음원을 추가한다. CCSR Fig. 1의 직접음, 초기 반사, 후기 잔향 구분과 채널별 전달함수라는 관점을 따른다. 화면에는 직접음과 1차 반사만 명시적으로 계산했으며 확산된 후기 잔향장 전체를 구현하지 않았다. y=3.8 m인 평면 벽에 대한 이미지 음원으로 반사점과 반사 경로 길이를 계산했다. 두 번째 음원은 별도 펄스이고 관측에 선형 합산된다. 일반식 x_m(t)=∑_k(h_mk*s_k)(t)+v_m(t)를 표시하며 이 예에서는 v_m=0이다. 실측 RIR이나 원문의 성능 결과를 재현한 그림이 아니다. 다음에는 직접음 상태로 돌아가 장치 배치의 영향만 분리한다.

[Sources]
- https://arxiv.org/html/2312.00476v2
-->

---
layout: seminar
variant: figure
transition: none
---

# 마이크 배열 기하

::body::
<ManimScene src="/animations/intro-sequence/s06.mp4" webm="/animations/intro-sequence/s06.webm" poster="/animations/intro-sequence/s06-start.png" print-poster="/animations/intro-sequence/s06-end.png" description="마이크 배열 기하: 같은 3차원 장면을 유지하는 설명용 애니메이션" />

::takeaway::
같은 음원 위치에서도 마이크 간격에 따라 달라지는 시간차

::source::
AGG-RL, ICLR 2026, Fig. 1(a), §3.2 기반. 음원·배열 중심·좌표계 고정, 마이크 간격만 변경.

<!--
[S06 발표 노트]
반사음과 다른 음원의 기여를 천천히 없애 직접음 비교 상태로 돌아온다. 음원 위치, 배열 중점 O, 기준 좌표계를 유지하고 두 마이크 간격 d만 1.2 m에서 0.6 m, 1.8 m, 다시 1.2 m로 바꾼다. 수치는 이 도해를 위한 예시이며 원문 실험 조건이 아니다. 변화한 p1,p2로 직접 경로를 다시 계산하므로 원거리 근사값과 유한 거리값을 혼용하지 않는다. 마이크 배열이 달라질 때 관측의 의미를 기하와 함께 해석해야 한다. 다음에는 이 관측에서 요구하는 표현과 의미 연결, 평가 관점을 정리한다.

[Sources]
- https://proceedings.iclr.cc/paper_files/paper/2026/file/ee860a9fa65a55a335754c557a5211de-Paper-Conference.pdf
-->

---
layout: seminar
variant: figure
transition: none
---

# 공간 표현·언어 결합·평가

::body::
<ManimScene src="/animations/intro-sequence/s07.mp4" webm="/animations/intro-sequence/s07.webm" poster="/animations/intro-sequence/s07-start.png" print-poster="/animations/intro-sequence/s07-end.png" description="공간 표현·언어 결합·평가: 같은 3차원 장면을 유지하는 설명용 애니메이션" />

::takeaway::
같은 장면에 적용하는 표현·의미 연결·검증의 관점

::source::
발표 범위의 개념도. 세 관점은 특정 논문의 단일 모델 구조나 필수 처리 순서를 뜻하지 않음.

<!--
[S07 발표 노트]
처음의 음원과 좌표 표시로 돌아온다. 첫째는 위치를 읽을 수 있는 공간 표현, 둘째는 음원의 종류와 공간 속성을 같은 대상에 연결하는 언어 결합, 셋째는 관측을 바꾸었을 때 판단이 적절하게 바뀌는지 확인하는 평가다. 화면의 세 행은 발표를 읽는 관점이며 모든 실제 시스템이 이 순서의 세 모듈로 구현된다는 뜻이 아니다. 거리와 3차원 방향을 모두 출력하는 모델만 다루는 것도 아니다. 다음 8번에서는 위치 목표 중 활성 방향 탐색부터 확대하여 살펴본다.

[Sources]

-->

