---
theme: default
title: '공간 소리를 듣고 판단하는 모델'
description: '공간 단서, 표현 학습, 공간 언어 모델과 평가를 연결하는 78장 학술 세미나'
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
공간 단서에서 표현 학습, 언어 정렬과 판단 평가까지

::source::
공간 오디오 이해 · 27편의 연구와 평가 조건

<!--
[S01 발표 노트]
[설명 순서]
“소리를 들은 모델이 무엇이 어디에 있는지 판단하는 연구를 다룹니다. 같은 장면에 서로 다른 질문을 던지면서 각 연구의 설계와 확인된 능력을 비교하겠습니다.”

[경계·부록]
생성·렌더링·로봇 행동은 독립 주제에서 제외한다. 기술들이 차례로 대체됐다는 역사적 계보를 주장하지 않는다.

[다음 연결]
“먼저 모델이 답해야 할 질문 하나를 실제로 떠올려 보겠습니다.”

범위: 청각 입력을 이용한 공간 판단. 기술 간 단선적 대체 역사나 생성·렌더링·로봇 행동의 개관을 뜻하지 않는다.
[Sources]
- https://iip.sogang.ac.kr/layouts/iiplab/top-logo.png
-->


---
layout: seminar
variant: figure
transition: none
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

---
layout: seminar
variant: figure
---

# 먼저 소리가 있는 방향들을 찾는다

::body::
<PaperFigure src="/diagrams/p1-direction-then-event.svg" alt="혼합 관측의 활성 방향 후보 두 개와 각 후보에 알람이라는 사건 이름을 연결하는 별도 질문" caption="설명용 공간 응답 · 실제 모델 점수가 아님" />

::takeaway::
**활성 방향을 찾는 일**과 **소리 이름을 연결하는 일**은 구별된다.

::source::
발표자 설명용 개념도. 실제 모델 출력이 아님.

<!--
[S08 발표 노트]
[설명 순서]
“전체 위치 목표 중, 우선 어느 방향에 소리가 있는지를 출력하는 문제부터 생각하겠습니다. 이 후보에 알람이라는 이름을 연결해야 처음의 질문까지 답할 수 있으므로, 뒤에서는 출력의 요구를 조금씩 바꾸겠습니다.”

[경계·부록]
모든 실제 시스템이 이 순서의 두 모듈로 구현된다고 주장하지 않는다. 기술의 발전 단계가 아니라 발표를 위한 과제 구분이다.

[다음 연결]
“방향 후보를 비교하려면 각 후보가 예측하는 지연과 실제 관측을 맞춰볼 수 있습니다.”

C08. 같은 두 음원 장면에서 출력의 요구를 바꾼 것이다. 모든 시스템이 반드시 후보 탐색과 사건 결합의 두 단계 구조를 갖는다는 주장이 아니다.

[시각화 전 본문 설명]
입력혼합음
말소리 + 알람
위치 출력{왼쪽, 오른쪽}
소리 이름 없는 활성 방향 후보
추가 질문어느 쪽이 알람?
사건과 방향의 대응이 필요

[설명 그림의 범위]
발표자 제작 SVG. 개념의 관계를 읽기 위한 도식이며 원문의 실험 관측이나 모델 추정값을 그린 결과가 아니다.
-->


---
layout: seminar
variant: figure
---

# 후보 방향이 예측한 지연과 관측을 맞춘다

::body::
<PaperFigure src="/diagrams/p1-candidate-delay-match.svg" alt="후보 방향과 배열에서 얻은 지연을 쌍별 관측 관계에 대조한 뒤 공간 응답으로 합산하는 도식" caption="지연과 공간 응답의 설명용 도식 · 실험 수치가 아님" />

::takeaway::
각 후보가 설명하는 **채널 관계의 일치**를 모아 위치를 고른다.

::source::
Neural-SRP, arXiv:2403.09455v1; AGG-RL, ICLR 2026. 설명용 재구성.

<!--
[S09 발표 노트]
[설명 순서]
“후보 방향을 하나 정하면 배열 기하로부터 기대하는 지연 관계를 계산할 수 있습니다. 기존 방법은 이러한 일치를 계산하고, IPDnet 같은 방법은 직접음 IPD라는 중간 목표를 학습합니다.”

[경계·부록]
IPDnet은 기초 비교 사례이며 추가 중심 논문으로 확대하지 않는다. MUSIC의 부분공간 유도와 모든 고전 방법의 분류는 부록으로 보낸다.

[다음 연결]
“관측이 복잡할 때 이 공간 응답 자체를 학습하면 어떤 변화가 생길까요?”

C09. GCC-PHAT의 교차상관에서 후보 지연의 값을 읽고 SRP에서 여러 쌍을 모으는 직관이다. IPDnet을 모든 학습 위치 추정기와 동일시하지 않는다. MUSIC 부분공간 유도나 모든 고전 방법의 분류는 다루지 않는다.
[Sources]
- https://arxiv.org/html/2403.09455v1
- https://proceedings.iclr.cc/paper_files/paper/2026/file/ee860a9fa65a55a335754c557a5211de-Paper-Conference.pdf

[시각화 전 본문 설명]
후보 방향 + 배열 좌표
각 마이크 쌍에서 기대되는 지연
쌍별 관측과 대조
예측한 관계와 얼마나 일치하는가
여러 쌍의 일치 합산
후보별 공간 응답 → 위치 선택
계산하는 응답
GCC/SRP는 지연의 일치를 직접 계산한다.
학습하는 중간 목표
IPDnet은 직접음 IPD를 예측한다.

[설명 그림의 범위]
발표자 제작 SVG. 개념의 관계를 읽기 위한 도식이며 원문의 실험 관측이나 모델 추정값을 그린 결과가 아니다.
-->


---
layout: seminar
variant: figure
---

# 학습한 공간 응답은 어떻게 달라 보일까?

::body::
<PaperFigure src="/research/neural-srp-response-pair.svg" alt="Neural-SRP Fig. 1 왼쪽 NeuralSRP+ 오른쪽 SRP의 위치 응답" caption="왼쪽: NeuralSRP+ · 오른쪽: SRP. 원문 패널 재배치, 공유 x축은 두 패널 아래에 표시." />

::takeaway::
이 그림은 <strong>실녹음에 적응한 NeuralSRP+</strong>의 정성적 예시다.

::source::
Grinstein et al., Neural-SRP, arXiv:2403.09455v1, Fig. 1. CC BY 4.0.

<!--
[S10 발표 노트]
[설명 순서]
“같은 녹음에서 두 방법이 만든 공간 응답을 비교하겠습니다. 실제 녹음에 적응한 NeuralSRP+의 예시라는 조건을 먼저 확인하고, 음원 근처와 다른 영역의 응답을 살펴보겠습니다.”

[경계·부록]
한 그림으로 전체 성능이나 무적응 실환경 전이를 입증하지 않는다. 적응 전후 모든 변형의 정량 비교는 별도 근거를 확보해 부록에 둔다.

[다음 연결]
“쌍별 응답을 학습해 합산한 방법이 실제 위치 오차도 줄였는지 확인하겠습니다.”

마이크 위치와 음원 정답 위치를 먼저 짚고 두 응답의 같은 공간을 비교한다. Neural-SRP는 쌍별 STFT 위상, 마이크 절대좌표, 방 크기로 위치 격자의 응답을 학습하고 쌍의 응답을 합산한다. 후보 위치 좌표는 학습 정답 구성에만 쓴다. 한 시각화가 정량 성능 또는 무적응 실환경 전이를 입증하지 않는다.
[Sources]
- https://arxiv.org/html/2403.09455v1
-->


---
layout: seminar
variant: result
---

# Recorded 4에서 실제 위치 오차가 줄었다

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
[S11 발표 노트]
[설명 순서]
“쌍별 위상과 좌표, 방 크기로 학습한 응답을 합산하는 방법의 결과입니다. 이 조건에서는 오차가 줄었지만 NeuralSRP+는 실제 녹음으로 적응했으므로, 처음 만난 환경에서 무적응으로 얻은 성과라고 읽으면 안 됩니다.”

[경계·부록]
Fig. 3 전체 구조와 Recorded 6 결과는 부록이다. 후보 좌표는 학습 목표 구성에 쓰며 추론 입력이 아니라는 주석을 유지한다.

[다음 연결]
“고정된 위치 격자를 예측하는 방식과 달리, 후보 방향 목록 자체도 바꾸고 싶다면 어떨까요?”

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
layout: seminar
variant: figure
---

# 마이크 배치와 후보 방향 목록은 다른 조건이다

::body::
<PaperFigure src="/diagrams/p1-query-grid.svg" alt="같은 녹음과 마이크 배열을 유지하며 후보 방향 목록을 성긴 격자에서 촘촘한 격자로 바꾼 기하" caption="마이크 배열은 고정 · 질의할 후보 방향의 간격과 개수만 변경" />

::takeaway::
**배열 기하**와 **후보 방향 격자**는 독립적으로 달라질 수 있다.

::source::
AGG-RL, ICLR 2026. 설명용 재구성.

<!--
[S12 발표 노트]
[설명 순서]
“앞에서는 녹음하는 마이크 배치를 바꿨지만, 여기서는 같은 녹음에 물어볼 방향 목록을 바꿉니다. 출력 칸이 고정된 모델과 후보 방향을 조건으로 받는 모델은 이 요구를 다르게 다룹니다.”

[경계·부록]
후보 수 증가를 각도 정확도의 자동 향상으로 표현하지 않는다. 임의 격자와 임의 실제 배열 모두에 대한 보장도 주장하지 않는다.

[다음 연결]
“AGG-RL은 오디오와 마이크 기하에 더해 후보 방향도 모델에 제공합니다.”

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
layout: seminar
variant: method
---

# AGG-RL은 오디오·기하·후보 방향을 정합한다

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
[S13 발표 노트]
[설명 순서]
“그림에서 먼저 오디오와 마이크 좌표가 들어오는 경로, 후보 방향이 들어오는 경로를 나눠 보겠습니다. 이들이 만드는 표현을 비교해 각 후보의 응답을 계산하는 것이 이번 설계의 핵심입니다.”

[경계·부록]
LNuDFT·rMPE를 학습 목표라고 부르지 않는다. 모든 내부 층과 손실 유도는 부록이며 구조만으로 일반화 성능을 결론내리지 않는다.

[다음 연결]
“이제 설계 의도가 실제로 평가한 새 배열 조건에서 어떤 결과를 냈는지 확인하겠습니다.”

LNuDFT는 주파수 단서 처리, rMPE는 마이크 상대 기하 표현과 연결한다. 둘은 학습 목표 이름이 아니다. 그림의 전체 층을 모두 읽기보다 입력 경로와 두 표현의 정합을 짚는다. 성능은 다음 실험 조건에서 따로 확인한다.
[Sources]
- https://proceedings.iclr.cc/paper_files/paper/2026/file/ee860a9fa65a55a335754c557a5211de-Paper-Conference.pdf
-->


---
layout: seminar
variant: result
---

# 처음 보는 채널 수에서 AGG가 도움이 될까?

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">Dynamic-U · 학습 4–12채널 / 시험 13–16채널</p>
<PaperFigure src="/diagrams/result-14.svg" alt="방향 MAE (°) ↓, $\mathrm{ACC}_{10}$ (%) ↑ 원문 수치 비교 그래프. 기본 Neural-SRP: 21.18, 45.51; AGG 적용: 19.05, 54.13" />
<p class="seminar-chart-note">합성 · 최대 두 정지 화자 · Dynamic-S에서는 두 지표가 개선되지 않음</p>
</div>

::takeaway::
**학습보다 채널이 많은 Dynamic-U**에서 두 지표가 개선됐다.

::source::
AGG-RL, ICLR 2026, Table 3, Neural-SRP without/with AGG-RL. 원문 수치의 그래프 재구성.

<!--
[S14 발표 노트]
[설명 순서]
“여기서 Dynamic은 음원 이동이 아니라 배열 조건입니다. 같은 기준 모델의 정합 유무를 비교하면 미관측 채널 수에서 이득이 있지만, 학습 채널 수 범위인 Dynamic-S에서는 개선되지 않습니다.”

[경계·부록]
모든 배열 일반화의 보장으로 읽지 않는다. Proposed 전체 시스템, Dynamic-S 상세, Table 4 격자 수와 Table 5 비용은 별도 부록이다.

[다음 연결]
“위치를 찾았다면, 각 위치에 어떤 종류의 소리가 있는지도 함께 출력할 수 있을까요?”

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
-->


---
layout: seminar
variant: figure
---

# SELD는 사건과 위치를 함께 출력한다

::body::
<PaperFigure src="/diagrams/p1-seld-timeline.svg" alt="말소리와 알람의 활성 시간 구간을 방향 화살표와 연결한 SELD 출력 형식" caption="고정 클래스 SELD · 정적 두 음원의 설명용 예시" />

::takeaway::
방향에 **사건 종류와 활성 시점**을 연결한 출력이 SELD다.

::source::
SELD 출력 형식의 설명용 예시. 실제 추정 결과가 아님.

<!--
[S15 발표 노트]
[설명 순서]
“지금 요구하는 것은 방향 목록에 사건 종류와 활성 시점을 연결한 출력입니다. 이 결합은 SELD도 다루므로, 뒤에서 언어 모델이 등장한다고 처음 가능해지는 능력으로 설명하지 않겠습니다.”

[경계·부록]
고정 클래스 SELD를 자유 어휘 질의나 자유형 답변과 동일시하지 않는다. 평가 지표의 세부 정의는 실제 결과를 읽을 때 소개한다.

[다음 연결]
“이런 출력을 배우는 연구들은 같은 형식의 오디오를 입력으로 쓰고 있을까요?”

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
layout: seminar
variant: figure
---

# 채널 형식과 추가 정보를 구분한다

::body::
<PaperFigure src="/diagrams/p1-input-representations.svg" alt="물리적 위치의 마이크 배열과 두 귀 관측 및 구면조화 FOA 기저 성분을 구별한 그림" caption="FOA는 구면조화 기저 성분 표현 · 기저의 형태는 설명용 단면" />

::takeaway::
**추론 때 주는 정보**와 **학습 정답을 만드는 정보**를 나눠 읽는다.

::source::
AGG-RL, ICLR 2026; SFD, arXiv:2508.20914v1; GRAM, arXiv:2506.00934v5. 설명용 재구성.

<!--
[S16 발표 노트]
[설명 순서]
“마이크 배열의 채널, 두 귀의 관측, FOA의 공간 성분은 같은 종류의 채널 목록이 아닙니다. 또한 오디오를 해석할 때 주는 정보와 학습 정답을 만드는 정보도 나눠 보아야 합니다.”

[경계·부록]
FOA를 마이크 네 개라고 설명하지 않는다. 모든 모델에 좌표나 깊이가 추론 입력으로 들어간다는 보편 도식도 피한다.

[다음 연결]
“입력 조건을 구별했으니, 이제 어떤 부분을 학습하고 무엇을 고정한 채 평가하는지 정하겠습니다.”

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
layout: seminar
variant: figure
---

# 점수를 읽기 전에 무엇을 학습했는지 확인한다

::body::
<PaperFigure src="/diagrams/p1-frozen-finetune.svg" alt="고정 인코더와 판독기만의 업데이트 경로 및 전체 인코더와 판독기의 업데이트 경로 비교" caption="판독기는 두 경우 모두 후속 과제의 정답으로 학습" />

::takeaway::
인코더를 고정해도 **판독기는 후속 과제의 정답으로 학습한다.**

::source::
MC-SimCLR·CCSR·GRAM의 평가 프로토콜을 기준으로 재구성.

<!--
[S17 발표 노트]
[설명 순서]
“고정 인코더 평가는 이미 만든 특징에서 제한된 판독기가 무엇을 읽는지 묻습니다. 전체 미세조정은 표현 자체도 바꾸므로, 적응 후 시스템 성능이라는 다른 질문에 답합니다.”

[경계·부록]
선형·비선형 판독기의 용량을 무시하지 않는다. 고정 여부와 추가 데이터 조건은 앞으로 각 결과 장에서 다시 확인한다.

[다음 연결]
“먼저 같은 장면을 반복 관측했을 때 무엇을 같게 배우도록 할지 살펴보겠습니다.”

선형 판독과 비선형 판독은 접근 가능한 정보와 용량이 다르다. 인코더 고정은 zero-shot을 뜻하지 않는다. 같은 입력과 레이블 조건을 비교할 때에도 판독기 종류를 표시해야 한다.
[Sources]
- https://arxiv.org/html/2309.15938v1
- https://arxiv.org/html/2312.00476v2
- https://arxiv.org/html/2506.00934v5

[시각화 전 본문 설명]
같은 후속 출력이어도 평가 질문은 다르다
평가 방식 | 인코더 | 판독기 | 해석
고정 표현 판독 | 고정 | 정답으로 학습 | 특징에서 읽을 수 있는 정보
전체 미세조정 | 업데이트 | 정답으로 학습 | 적응 후 과제 성능

[설명 그림의 범위]
발표자 제작 SVG. 개념의 관계를 읽기 위한 도식이며 원문의 실험 관측이나 모델 추정값을 그린 결과가 아니다.
교육 참고: Dive into Deep Learning §14.2 Fine-Tuning, pretrained features와 새 출력층의 구별 및 고정 특징 평가. 각 논문의 프로토콜은 기존 출처와 노트가 기준이다.
- https://d2l.ai/chapter_computer-vision/fine-tuning.html
-->


---
layout: seminar
variant: figure
---

# 같은 녹음의 두 구간을 가깝게 배운다

::body::
<PaperFigure src="/diagrams/p1-contrastive-crops.svg" alt="한 다채널 녹음의 두 시간 구간을 잘라 공유 인코더로 표현한 뒤 가까이 학습하는 대조 학습 도식" caption="정지 음원 · 사건이 겹치지 않는 장면 · 채널의 대응 유지" />

::takeaway::
시간이 달라도 유지되는 **사건·공간 관계**를 학습 목표로 쓴다.

::source::
MC-SimCLR, arXiv:2309.15938v1, Fig. 1 기반 과제 재구성.

<!--
[S18 발표 노트]
[설명 순서]
“음원이 움직이지 않는 동안 같은 녹음의 서로 다른 구간을 관측한다고 생각하겠습니다. 이 방법은 그 구간들을 가깝게 학습하면서 반복 관측에 남는 정보를 표현에 담으려 합니다.”

[경계·부록]
임의의 단일 채널 둘을 양성 쌍으로 묶는다고 설명하지 않는다. 정지 음원 가정을 이동 장면까지 자동 확장하지 않는다.

[다음 연결]
“그 목표가 사건과 방향을 읽는 데 도움이 됐는지는 후속 판독으로 확인해야 합니다.”

같은 다채널 녹음에서 시간 구간을 뽑되 채널을 일관되게 다룬다. 인코더에 전달하는 파형 내용이 같다는 뜻은 아니다. 채널 shuffle 등 모든 augmentation이 공간 단서를 보존한다고 일반화하지 않는다.
[Sources]
- https://arxiv.org/html/2309.15938v1

[시각화 전 본문 설명]
한 다채널 녹음
정지한 음원 · 채널 관계 유지
서로 다른 시간 구간
구간 A ↔ 구간 B를 양성 쌍으로 선택
MC-SimCLR의 대조 학습
두 구간의 표현을 가깝게 정렬
핵심 가정
음원이 정지하고 사건이 겹치지 않는 장면
평가할 정보
소리의 종류 + 방위각

[설명 그림의 범위]
발표자 제작 SVG. 개념의 관계를 읽기 위한 도식이며 원문의 실험 관측이나 모델 추정값을 그린 결과가 아니다.
-->


---
layout: seminar
variant: result
---

# 고정 표현에서 사건과 방향을 읽을 수 있을까?

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">LP · 인코더 고정, 사건/방향 선형 판독기 각각 학습</p>
<PaperFigure src="/diagrams/result-19.svg" alt="사건 정확도 (%) ↑, 방위각 오차 (°) ↓ 원문 수치 비교 그래프. 사전학습 없음: 23.6, 83.1; MC-SimCLR · w/o DA: 33.0, 13.2" />
<p class="seminar-chart-note">4채널·정지·비중첩 · noisy split 38.8시간 사전학습 · clean 레이블로 LP</p>
</div>

::takeaway::
이 합성 평가에서는 **사건 정확도와 방향 판독**이 함께 개선됐다.

::source::
MC-SimCLR, arXiv:2309.15938v1, Table 1, LP. 원문 수치의 그래프 재구성.

<!--
[S19 발표 노트]
[설명 순서]
“이번에는 같은 인코더를 고정한 채 사건 종류와 방향을 각각 읽습니다. 추가 증강이 없는 사전학습과 사전학습하지 않은 조건을 비교하면, 두 판독의 개선을 서로 다른 지표로 확인할 수 있습니다.”

[경계·부록]
증강 조합의 10.1°와 전체 미세조정 결과는 부록이다. noDA를 최적 모델이라고 부르거나 사건 정확도와 방향 오차를 같은 지표로 합치지 않는다.

[다음 연결]
“서로 다른 구간을 가깝게 만드는 대신, 관측 일부를 복원하게 하면 무엇을 배우게 될까요?”

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
layout: seminar
variant: figure
---

# CCSR은 가린 STFT 관측을 복원한다

::body::
<PaperFigure src="/diagrams/p1-ccsr-masking.svg" alt="CCSR의 같은 프레임 공동 마스킹과 상보 마스킹을 채널별 STFT 격자로 구별한 복원 목표 도식" caption="마스크 패턴은 설명용 · 두 표현을 결합해 가린 STFT 프레임 복원" />

::takeaway::
공간 관계와 소리 내용을 함께 써서 **관측 일부를 복원**한다.

::source::
Yang & Li, CCSR, arXiv:2312.00476v2, Fig. 1·§IV-A 기반 복원 목표 개념도.

<!--
[S20 발표 노트]
[설명 순서]
“먼저 어떤 관측을 정답으로 복원하는지 보겠습니다. 두 분기는 가리는 방식이 다르므로, 한 채널의 빈칸을 다른 채널로 채우는 단순 그림을 전체 구현이라고 읽으면 안 됩니다.”

[경계·부록]
단순화한 그림에는 복원 목표 개념도라는 표기를 남긴다. 세부 마스크 구조는 부록이며, 복원 성공만으로 원하는 공간 정보를 쉽게 판독한다고 단정하지 않는다.

[다음 연결]
“따라서 복원 손실과 별도로, 실제 후속 공간 과제에서의 효과를 보겠습니다.”

원문 §IV-A의 분리된 spatial/spectral encoder masking을 요약했다. 한 채널 전체가 영구적으로 미관측인 경우의 생성 과제가 아니다. 두 표현을 결합해 decoder가 마스크된 STFT 프레임을 복원한다. 정적 RIR 가정. 복원 손실 자체가 후속 판독 정확도는 아니다.
[Sources]
- https://arxiv.org/html/2312.00476v2

[시각화 전 본문 설명]
공간 분기
두 채널의 같은 프레임을 가린다
스펙트럼 분기
서로 상보적인 프레임을 보여 준다
복원 목표
가려진 한 채널의 STFT를 예측한다
공간 단서
두 채널이 함께 보이는 프레임의 전달 관계
내용 단서
복원할 시점에 보이는 다른 채널의 신호

[설명 그림의 범위]
발표자 제작 SVG. 개념의 관계를 읽기 위한 도식이며 원문의 실험 관측이나 모델 추정값을 그린 결과가 아니다.
-->


---
layout: seminar
variant: result
---

# 복원 사전학습은 TDoA 적응을 도왔다

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
[S21 발표 노트]
[설명 순서]
“여기서는 후속 조건에서 처음부터 학습한 경우와 전체 미세조정한 경우를 비교합니다. TDoA는 개선됐지만 C50 오차는 1.14 dB에서 1.21 dB로 증가해, 모든 지표가 함께 좋아지지는 않았습니다.”

[경계·부록]
C50 반례를 짧은 주석으로 남긴다. frozen의 TDoA 1.49와 T60 상세는 부록이며, 전체 적응 결과를 고정 표현의 선형 접근성으로 표현하지 않는다.

[다음 연결]
“복원의 대상은 파형 관측뿐 아니라 채널 간 관계를 나타내는 통계가 될 수도 있습니다.”

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
layout: seminar
variant: method
---

# LAM은 채널 관계를 잠재 음향지도로 설명한다

::body::
<PaperFigure src="/research/p1-lam-method.png" alt="LAM Fig. 2 채널 공분산에서 잠재 음향지도를 거쳐 관측을 복원하는 구조" />

::aside::
<section><span class="seminar-label semantic-input">관측</span><p>채널 간 이차 관계인 공분산(CSM)</p></section>
<section><span class="seminar-label semantic-result">잠재 지도</span><p>음향 에너지의 공간 분포</p></section>
<section><span class="seminar-label semantic-geometry">복원 경로</span><p>알려진 steering matrix를 사용</p></section>

::takeaway::
방향 라벨 대신 **관측된 채널 공분산의 복원**으로 지도를 학습한다.

::source::
LAM, arXiv:2507.07066v1, Fig. 2. 원문 그림.

<!--
[S22 발표 노트]
[설명 순서]
“모든 장면에 방향 정답을 붙이는 대신, 실제로 관측한 채널 관계를 설명하도록 학습할 수 있습니다. LAM에서는 그 관측을 복원하는 과정에 잠재 음향지도가 들어갑니다.”

[경계·부록]
공분산 복원용 지도를 모든 의미 과제에 재사용하는 범용 표현이라고 부르지 않는다. 전체 수학 유도와 복원 경로의 내부 층은 부록이다.

[다음 연결]
“이 지도가 실제 방향을 얼마나 정확하고 빠짐없이 읽어내는지 확인하겠습니다.”

도착 방향을 정답으로 붙이지 않고 관측 공분산을 복원하는 사전학습이다. LAM의 잠재 SAM은 의미의 범용성을 직접 입증하지 않는다. UpLAM은 4채널에서 32채널 공분산 표현으로 올리는 학습된 변형으로, 임의 미지 배열을 무학습 처리한다는 뜻이 아니다.
[Sources]
- https://arxiv.org/html/2507.07066v1
-->


---
layout: seminar
variant: figure
---

# 검출 임계값에 따라 위치 오차와 재현율이 달라진다

::body::
<PaperFigure src="/research/p1-lam-threshold.svg" alt="LAM Fig. 3 같은 UpLAM GRU-MHSA의 검출 threshold에 따른 LE와 LR" caption="STARSS dev-test-sony: 실선이 평가 곡선. 점선은 검증, 녹색선은 기본 임계값 0.5." />

::takeaway::
임계값을 낮추면 **재현율과 위치 오차가 함께 높아질 수 있다.**

::source::
LAM, arXiv:2507.07066v1, Fig. 3. 원문 벡터; LE (°) ↓, LR (%) ↑.

<!--
[S23 발표 노트]
[설명 순서]
“여기서는 두 모델의 우열이 아니라 같은 모델의 검출 기준을 바꿉니다. 놓치는 음원과 위치 오차가 어떻게 함께 달라지는지 보면서, 기본 임계값에서 얻은 결과의 의미를 확인하겠습니다.”

[경계·부록]
곡선의 여러 점을 서로 다른 모델로 설명하지 않는다. Table 2의 모델 비교는 부록이며, 이 결과를 음원 종류나 자연어 이해로 확대하지 않는다.

[다음 연결]
“관측을 복원하는 목표와 달리, 깨끗한 공간 특징을 명시적인 정답으로 줄 수도 있습니다.”

두 패널은 두 모델이 아니라 같은 UpLAM + GRU-MHSA의 LE와 LR이다. 실선 evaluation만 주근거로 읽고 점선 validation을 시험 성과로 혼동하지 않는다. LE는 낮을수록, LR은 높을수록 좋다. Eigenscape 10시간+SpatialScaper 합성 10시간으로 CSM 복원을 학습했다. 후속 DOA 판독기는 STARSS dev-train-tau/sony와 companion synthetic data로 지도학습하고 dev-test-tau로 검증했다. 기본 임계값0.5의 평가 표값은 LE18.65°, LR57.6%; 곡선에서 새 수치를 추정하지 않았다.
[Sources]
- https://arxiv.org/html/2507.07066v1
-->


---
layout: seminar
variant: method
---

# SFD는 깨끗한 공간 특징을 목표로 삼는다

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
[S24 발표 노트]
[설명 순서]
“이 방법은 모델이 복원할 대상을 원래 파형 전체 대신 공간 특징으로 정합니다. 깨끗한 신호에서 얻은 목표를 오염된 입력으로 예측하게 한 뒤 DOA 과제에 적응합니다.”

[경계·부록]
GCC·GCC-PHAT·CPS 위상·ILD/IPD를 모두 한 손실로 합쳐 학습했다고 설명하지 않는다. 세부 목표 수식은 해당 결과 해석에 필요한 것만 남긴다.

[다음 연결]
“이런 목표 선택이 같은 DOA 미세조정 조건에서 어떤 차이를 만들었을까요?”

GCC, GCC-PHAT, CPSPhase, ILD+IPD는 각각 별도의 특징 목표 변형이다. 여러 목표를 한 손실로 모두 결합한 모델로 설명하지 않는다. 별도 학습된 teacher network가 아니라 clean 비잔향 바이노럴 신호의 분석적 특징 추출이다. DOA 라벨이 없어도 clean target은 필요하다.
[Sources]
- https://arxiv.org/html/2508.20914v1
-->


---
layout: seminar
variant: method
---

# 깨끗한 특징을 배운 초기화는 잡음에 도움이 될까?

::body::
<PaperFigure src="/research/sfd-1h-plot.svg" alt="SFD Fig. 2의 1시간 라벨 조건. x축 SNR dB, y축 DOA MAE 도. 원본 곡선과 축을 보존한 패널" />

::aside::
<section>
<span class="seminar-label">1시간 라벨 · 전체 미세조정</span>
<div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;font-size:20px"><span style="width:26px;border-top:3px solid #0072b2;flex:none"></span><span>GCC-PHAT-DNN</span></div><div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;font-size:20px"><span style="width:26px;border-top:3px solid #d55e00;flex:none"></span><span>GCC-DNN</span></div><div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;font-size:20px"><span style="width:26px;border-top:3px solid #009e73;flex:none"></span><span>STFT-DNN</span></div><div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;font-size:20px"><span style="width:26px;border-top:3px solid #f0e442;flex:none"></span><span>SFD-CPSPhase</span></div><div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;font-size:20px"><span style="width:26px;border-top:3px solid #cc79a7;flex:none"></span><span>SFD-GCC</span></div><div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;font-size:20px"><span style="width:26px;border-top:3px solid #999999;flex:none"></span><span>SFD-GCC-PHAT</span></div><div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;font-size:20px"><span style="width:26px;border-top:3px solid #56b4e9;flex:none"></span><span>SFD-ILD+IPD</span></div><p style="font-size:20px;margin-top:16px">x: SNR (dB)<br/>y: DOA MAE (°), 낮을수록 좋음</p>
</section>

::takeaway::
이 저라벨 조건에서 **SFD-CPSPhase가 STFT-DNN보다 낮은 오차**를 보인다.

::source::
SFD, arXiv:2508.20914v1, Fig. 2의 1h 패널. 원본 벡터 크롭·범례 재배치.

<!--
[S25 발표 노트]
[설명 순서]
“여기서는 라벨 시간과 백본을 맞추고 초기화만 비교하겠습니다. 사전학습 이후 인코더도 DOA에 맞춰 바뀌므로, 이 결과는 적응에 유용한 초기 표현의 증거로 읽어야 합니다.”

[경계·부록]
Table 2의 1시간·10시간 표기 충돌 때문에 그 표는 사용하지 않는다. 10분 패널과 다른 변형은 부록이며 서로 다른 데이터 조건의 수치를 섞지 않는다.

[다음 연결]
“공간 특징을 직접 가르치는 것과 달리, 이미 배운 소리 의미를 공간 판단에 연결하는 선택도 있습니다.”

주비교는 STFT-DNN(녹색)과 SFD-CPSPhase(노랑). 두 모델은 STFT 입력, 545k 파라미터와 1시간 라벨 학습량을 공유한다. SFD는 LibriSpeech 원음 960시간 기반 사전학습을 추가로 사용하고 인코더와 DOA head를 함께 미세조정한다. 단일 정지 음성·합성 바이노럴, HRTF 피험자 분리. 평가 잡음은 학습과 같은 종류의 다른 클립. 원래 나머지 곡선과 범례를 보존했다. 곡선으로 정밀 수치를 만들지 않는다. Table 2의 caption 1h/본문10h 충돌 때문에 해당 표는 본문에서 쓰지 않는다.
[Sources]
- https://arxiv.org/html/2508.20914v1
-->


---
layout: seminar
variant: figure
---

# 의미 특징을 공간 경로의 어디에 연결할까?

::body::
<PaperFigure src="/diagrams/p1-fusion-depth.svg" alt="같은 공간 처리 경로에서 태깅 의미 특징을 낮은 수준과 높은 수준에 연결하는 두 대안" caption="일반 오디오 태깅 사전학습 특징의 결합 위치 비교" />

::takeaway::
AT2SELD는 **의미·공간 특징의 결합 위치**를 비교한다.

::source::
AT2SELD, arXiv:2606.27751v1, Fig. 25 기반 결합 위치 재구성.

<!--
[S26 발표 노트]
[설명 순서]
“앞의 SELD는 소리 종류와 위치를 함께 출력했습니다. 이 연구는 일반 오디오 태깅에서 얻은 의미 정보를 그 예측 과정의 어디에 연결하는 것이 유용한지 묻습니다.”

[경계·부록]
의미 분류기가 정확하면 음원과 방향의 대응도 자동으로 해결된다고 주장하지 않는다. 고정 클래스 SELD 적응을 자유 어휘 질의응답과 구별한다.

[다음 연결]
“의미 특징을 연결하지 않은 조건과 연결한 조건을 같은 평가에서 비교해 보겠습니다.”

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
layout: seminar
variant: result
---

# 강한 dropout 조건에서는 late 결합이 도움이 됐다

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
[S27 발표 노트]
[설명 순서]
“이 차이는 원문의 특정 학습 단계와 dropout 조건에서 읽어야 합니다. 그 안에서 late-only 결합이 점수를 낮췄다고 말할 수 있지만, 의미 결합이 모든 학습 조건에서 우월하다는 결론은 아닙니다.”

[경계·부록]
전체 설정 탐색과 다른 학습 단계는 부록이다. 다른 조건의 최상위 행을 이번 기준선과 짝짓거나 범용 표현의 성과로 확대하지 않는다.

[다음 연결]
“지금까지의 과제별 적응과 구별해, 하나의 고정 표현을 여러 판단에 사용하는 평가를 보겠습니다.”

FOA 공간 경로와 pretrained audio-tagging 의미 경로를 사용한다. 이 표는 frozen probe가 아니다. Stage3 no-stitch는 unregularized Stage2보다 악화됐으므로, 강한 정규화 안에서의 성능 회복을 모든 공간 전용 모델에 대한 우위로 확대하지 않는다. early-only와 early+late는 부록의 별도 비교다.
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
layout: seminar
variant: figure
---

# GRAM은 복합 장면에서 공통 표현을 배운다

::body::
<PaperFigure src="/research/gram-scene.png" alt="GRAM Fig. 1 자연스러운 공간 장면 생성과 자기지도 학습" caption="Fig. 1(A) 장면 생성 패널. 여러 음원과 직접음·반사 경로를 함께 구성한다." />

::takeaway::
한 공간 관측에서 **소리 의미·방향·방 음향**을 읽는 표현을 준비한다.

::source::
GRAM, arXiv:2506.00934v5, Fig. 1. CC BY-NC-SA 4.0.

<!--
[S28 발표 노트]
[설명 순서]
“이번 목표는 특정 방향 출력에만 맞추는 데서 범위를 바꿉니다. 복합 장면을 보고 배운 인코더가 서로 다른 일반·공간 오디오 과제에서 읽을 수 있는 정보를 남기는지 살펴보겠습니다.”

[경계·부록]
복합 장면을 학습했다는 사실만으로 모든 다중 음원 관계를 판단한다고 주장하지 않는다. 장면 생성과 실제 녹음 평가의 역할을 분리한다.

[다음 연결]
“그 관측을 어떻게 학습하고, 고정된 특징을 어떤 방식으로 읽을까요?”

Fig1 A의 SoundSpaces2.0·Matterport3D 기반 자연 장면 생성과 Fig1 B의 학습 경로는 역할이 다르다. 여기서는 장면을 먼저 읽고 다음 장에서 마스킹과 후속 판독을 분리한다. 복합 장면 학습만으로 모든 음원 간 관계 추론이 검증된 것은 아니다. 생성 장면과 실녹음 평가의 조건도 구별한다.
[Sources]
- https://arxiv.org/html/2506.00934v5
-->


---
layout: seminar
variant: figure
---

# 사전학습 과제와 후속 판독은 다르다

::body::
<PaperFigure src="/diagrams/p1-pretrain-probe.svg" alt="마스킹 복원 사전학습 인코더를 고정한 뒤 새 과제 정답으로 판독기를 학습하는 두 단계 프로토콜" caption="고정 판독 프로토콜 · 실녹음 전체 미세조정은 별도 평가" />

::takeaway::
GRAM의 고정 판독은 **새 정답으로 판독기를 학습하는 평가**다.

::source::
GRAM, arXiv:2506.00934v5, Fig. 1·HEAR 평가 프로토콜 기반 재구성.

<!--
[S29 발표 노트]
[설명 순서]
“사전학습에서 모델이 받는 과제와 후속 평가에서 판독기가 받는 정답은 다릅니다. 고정 특징 평가를 중심으로 읽되, 원문에 있는 전체 미세조정 비교는 별도 조건으로 구분하겠습니다.”

[경계·부록]
모든 보고 결과가 고정 인코더라고 단정하지 않는다. 판독기의 용량과 학습 데이터량을 함께 기록하고 마스킹 세부 구현은 부록으로 보낸다.

[다음 연결]
“이 고정 표현에서 위치 같은 공간 요인을 실제로 얼마나 읽을 수 있는지 확인하겠습니다.”

사전학습은 마스킹 autoencoding을 사용한다. Ambisonics는 4채널 mel 및 intensity vector, binaural은 두 귀의 mel을 다룬다. HEAR 방식에서 고정 인코더와 지도 판독기를 사용한다. 논문 모든 결과가 고정 인코더는 아니며 STARSS23 fine-tuning 비교를 다음 고정 판독 결과와 섞지 않는다.
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
layout: seminar
variant: figure
---

# 고정 표현의 DOA 오차 분포를 읽는다

::body::
<PaperFigure src="/research/p1-gram-doa.svg" alt="GRAM Fig. 3(A) SC-5와 ESC-50의 고정 표현 DOA 오차 boxplot과 원본 범례" caption="합성 자연 장면 · 고정 인코더 + 지도 판독기. 중앙선: 중앙값, 상자: 사분위 범위." />

::takeaway::
**중앙값과 퍼짐**, 그리고 모델마다 다른 입력 조건을 함께 읽는다.

::source::
GRAM, arXiv:2506.00934v5, Fig. 3(A). 원본 벡터 크롭·범례 재배치.

<!--
[S30 발표 노트]
[설명 순서]
“먼저 각 분포가 어떤 입력에서 나온 고정 특징인지 확인하겠습니다. 중앙값과 퍼짐을 함께 읽되, 입력까지 통제한 동일 조건의 사전학습 제거 실험으로 해석하지는 않겠습니다.”

[경계·부록]
T60과 STARSS23 전체 미세조정은 부록이다. TAU2019 측정 RIR 합성을 전체 실제 녹음이라 부르거나 실녹음 적응 결과를 고정 판독과 합치지 않는다.

[다음 연결]
“이제 여섯 학습 목표를 비교하되, 실제로 어떻게 적응하고 무엇을 평가했는지도 함께 보겠습니다.”

GRAM-Ambisonics와 SpatialAST(supervised)를 중심으로 읽되 원래 입력과 학습 데이터가 다르다는 것을 명시한다. GRAM-Bin.Patch/Time은 바이노럴, GRAM-Ambisonics는 FOA, GRAM-Clean은 clean 음원 학습 조건이다. SC-5 음성과 ESC-50 환경음을 공간화한 합성 자연 장면에서 고정 특징으로 판독했다. 원본 box는 first/third quartile, center line median, whiskers1.5IQR다. 평균 막대로 바꾸거나 수치를 눈대중으로 읽지 않았다. 입력까지 통제한 masking ablation이 아니다.
[Sources]
- https://arxiv.org/html/2506.00934v5
-->


---
layout: seminar
variant: figure
---

# 학습 목표와 확인한 재사용 범위는 다르다

::body::
<PaperFigure src="/diagrams/p1-protocol-map.svg" alt="여섯 연구의 학습 목표에서 고정 및 업데이트 모듈을 거쳐 실제 판독 출력으로 이어지는 평가 경로" caption="각 연구에서 본문에 제시한 평가 범위 · 논문 간 순위가 아님" />

::takeaway::
목표 이름보다 **어떤 모듈을 바꾸고 어떤 출력을 평가했는지**가 중요하다.

::source::
MC-SimCLR·CCSR·SFD·GRAM·LAM·AT2SELD의 선택 실험 종합. 논문 간 순위가 아님.

<!--
[S31 발표 노트]
[설명 순서]
“같은 사전학습이라는 이름 아래에도 복원 대상과 후속 평가 방식은 다릅니다. 각 행에서 어떤 모듈을 바꿨고 어떤 출력을 읽었는지 확인하면서, 서로 다른 실험을 하나의 순위로 합치지 않겠습니다.”

[경계·부록]
인코더마다 과제·입력·판독기가 다른 숫자를 나란히 등수로 만들지 않는다. 전체 비교 수치와 모든 목표 변형은 부록으로 보낸다.

[다음 연결]
“지금까지 수치나 클래스 이름으로 읽던 표현을, 소리와 공간을 함께 말하는 문장에도 대응시킬 수 있을까요?”

표의 각 셀은 위/아래 연구와 같은 순서로 대응한다. MC-SimCLR와 GRAM의 판독기 용량은 동일하다고 가정하지 않는다. LAM 지도 DOA 판독과 K-means 판독을 섞지 않는다. AT2SELD는 일반 태깅 의미 표현을 공간 과제에 연결하는 지도 적응이다. 서로 다른 입력·과제·데이터의 숫자를 통합 순위로 만들지 않는다.
[Sources]
- https://arxiv.org/html/2309.15938v1
- https://arxiv.org/html/2312.00476v2
- https://arxiv.org/html/2508.20914v1
- https://arxiv.org/html/2506.00934v5
- https://arxiv.org/html/2507.07066v1
- https://arxiv.org/html/2606.27751v1

[시각화 전 본문 설명]
본문에서 제시한 비교의 범위
연구 | 사전학습의 목표 | 이번 평가의 업데이트 | 읽어낸 출력
MC-SimCLR / GRAM | 구간 간 대조 / 마스킹 복원 | 고정 인코더 + 판독기 학습 | 사건·방위각 / 방향 분포
CCSR / SFD | STFT 복원 / clean 공간 특징 | 전체 미세조정 | TDoA / DOA
LAM / AT2SELD | 공분산 복원 / 오디오 태깅 전이 | 지도 DOA 판독 / 지도 SELD 적응 | DOA·재현율 / 사건·위치

[설명 그림의 범위]
발표자 제작 SVG. 개념의 관계를 읽기 위한 도식이며 원문의 실험 관측이나 모델 추정값을 그린 결과가 아니다.
각 행은 연구의 전체 구현도가 아니라 본문에서 선택한 평가 프로토콜이다. CCSR/SFD의 파랑 밑줄은 인코더와 판독기 모두 업데이트함을 표시한다. LAM은 supervised DOA 판독, AT2SELD는 supervised SELD 적응이며 LAM의 모든 가중치 고정 여부를 새로 단정하지 않는다.
-->


---
layout: seminar
variant: figure
---

# “뒤쪽의 알람”이라는 문장과 관측을 맞춘다

::body::
<PaperFigure src="/diagrams/p1-spatial-language.svg" alt="청자 뒤 알람 관측과 동일한 소리 이름에 앞쪽 또는 뒤쪽 공간 표현을 붙인 두 문장 후보" caption="설명용 문장 후보 · 실제 모델의 정합 점수나 성공 예시가 아님" />

::takeaway::
문장과 오디오의 대응에는 **소리 의미와 위치 표현**이 모두 필요하다.

::source::
ELSA의 공간 오디오–언어 정렬 문제에 기반한 설명용 후보. 실제 모델 점수가 아님.

<!--
[S32 발표 노트]
[설명 순서]
“여기서는 자유롭게 답을 생성하는 대신 후보 문장과 녹음이 얼마나 맞는지 비교합니다. 소리 이름이 같은 문장도 위치가 다르면 다른 대응으로 구별해야 합니다.”

[경계·부록]
설명용 후보의 성공을 ELSA의 실험 결과로 표시하지 않는다. 프롬프트 분류·검색과 생성형 QA는 출력 방식부터 다르다.

[다음 연결]
“ELSA는 공간 정보가 포함된 오디오와 텍스트를 어떻게 함께 학습할까요?”

C32. 요구 출력은 후보 문장의 선택 또는 정합 점수다. 임의의 점수를 넣지 않았다. ELSA의 prompt 분류와 검색은 자유롭게 답변을 생성하는 QA와 다르다. 다음 슬라이드에서 실제 동일 모델의 합성/실녹음 방향 분류를 확인한다.
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
layout: seminar
variant: result
---

# ELSA의 방향 분류에는 합성–실녹음 차이가 남았다

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
[S33 발표 노트]
[설명 순서]
“ELSA는 공간 정보를 담은 오디오와 텍스트를 함께 정렬합니다. 같은 방향 후보를 사용해도 합성과 실제 녹음에서 정확도가 달라지므로, 이 차이를 포함해 재사용 범위를 읽겠습니다.”

[경계·부록]
Table 2에 없는 기준선을 만들지 않는다. CLAP의 Appendix A Table 7은 입력 조건을 표시해 부록에 두며, 합성·실제 차이를 단일 원인의 효과로 단정하지 않는다.

[다음 연결]
“소리 의미와 공간 정보가 함께 맞아야 한다면, 두 정보를 나눠 정렬하는 선택도 가능합니다.”

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
layout: seminar
variant: figure
---

# SALM은 소리 의미와 공간 정보를 나눠 정렬한다

::body::
<PaperFigure src="/diagrams/p1-salm-factorization.svg" alt="같은 알람의 위치 변화와 omni 의미 분기 및 FOA 공간 분기의 서로 다른 caption 정렬 목표" caption="원래 caption과 공간 caption을 구별하는 분기 역할의 개념도" />

::takeaway::
같은 소리가 이동하면 **의미는 유지되고 공간 속성은 바뀐다.**

::source::
SALM, arXiv:2507.16724v2, Fig. 1 기반 분기 역할 재구성.

<!--
[S34 발표 노트]
[설명 순서]
“같은 알람을 다른 위치로 옮기면 소리의 종류는 유지되지만 공간 속성은 바뀝니다. SALM은 이 차이를 표현의 분리와 언어 정렬이라는 설계 선택으로 다룹니다.”

[경계·부록]
두 분기를 만들었다는 사실만으로 완전한 요인 분리를 입증했다고 말하지 않는다. 임베딩 편집은 본문의 파형 생성 성과로 쓰지 않는다.

[다음 연결]
“같은 SALM에서 정렬 목표를 하나 더하면 검색과 위치 판독에 어떤 변화가 생기는지 보겠습니다.”

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
layout: seminar
variant: result
---

# 의미 정렬 목표를 더했을 때 무엇이 달라졌나?

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">동일 SALM · 합성 FOA sClotho 평가</p>
<PaperFigure src="/diagrams/result-35.svg" alt="T2A R@1 (%) ↑, A2T R@1 (%) ↑, 위치 오차 (°) ↓ 원문 수치 비교 그래프. $L_{\mathrm{sCL}}+L_{\mathrm{DOA}}$: 9.1, 9.6, 1.8; 위 조건 + $L_{\mathrm{CL}}$: 10.5, 10.4, 1.6" />
</div>

::takeaway::
이 비교에서는 **두 검색 점수와 지도 위치 오차**가 모두 개선됐다.

::source::
SALM, arXiv:2507.16724v2, Table 1, sClotho. 원문 수치의 그래프 재구성.

<!--
[S35 발표 노트]
[설명 순서]
“다른 모델의 순위가 아니라 같은 SALM의 학습 목표 한 가지를 비교합니다. 검색 점수는 높아지고 위치 오차는 낮아졌지만, 이는 같은 원문 조건에서 관측한 변화입니다.”

[경계·부록]
두 검색 방향을 정의하고 지표의 좋은 방향을 표시한다. 실측 SRIR·표현 편집·다른 모델 순위는 부록이며, 자연어 복합 추론의 증거로 확대하지 않는다.

[다음 연결]
“문장 후보 중 맞는 것을 찾는 대신, 문장으로 지정한 소리의 위치만 직접 출력할 수도 있습니다.”

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
layout: seminar
variant: method
---

# 모든 음원이 아니라 원하는 소리만 찾는다

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
[S36 발표 노트]
[설명 순서]
“앞의 정렬에서는 오디오와 문장의 대응을 평가했지만, 여기서는 요청한 소리의 위치를 직접 출력합니다. 목표가 없거나 여러 개일 수도 있으므로, 선택과 활성 수 판단도 과제의 일부가 됩니다.”

[경계·부록]
파형을 분리해 생성하는 과제로 소개하지 않는다. full model의 텍스트·예시 오디오 조건을 텍스트만 쓰는 시스템으로 축약하지 않는다.

[다음 연결]
“이 목표 판단에서 채널 간 위상 정보를 강화한 경로가 어떤 역할을 했는지 확인하겠습니다.”

다음 결과에서 Full은 text+audio cue를 함께 받는다. 원문 문제 그림의 prompt는 speech이며 앞서 사용한 알람 사고실험과 별개다. 내부 extraction 모듈의 selection 학습은 설명하되 출력 파형의 생성 성능이 본문의 주제는 아니다. 원문 MOTA*에는 ID-switch 벌점이 없어 음원 정체성 추적의 근거로 삼지 않는다.
[Sources]
- https://arxiv.org/html/2607.02343v1
-->


---
layout: seminar
variant: result
---

# IPD Enhancer를 빼면 위치와 검출이 함께 나빠졌다

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
[S37 발표 노트]
[설명 순서]
“같은 목표 입력을 둔 채 IPD Enhancer를 제거한 조건을 비교하겠습니다. 오차와 F1의 변화는 해당 경로의 기여를 보여주지만, 다른 입력 단서의 도움까지 없앴다는 뜻은 아닙니다.”

[경계·부록]
A4 직접 입력과 OSPAT는 부록이다. MAE는 true positive 조건이며, Table III의 MOTA*·Recall 불일치와 실측 RIR 정적 합성이라는 범위를 유지한다.

[다음 연결]
“다음 회차에서는 같은 공간 정보를 질문에 맞는 답변으로 읽는 방식과 그 조건을 살펴보겠습니다.”

주 실험은 5초 clip, SNR−5~5dB, 방위각[0,180), 프레임별 목표 수0/1/2 조건이다. Selection, DOA, cardinality를 함께 학습한다. MAE는 검출된 true positive 오차로 미검출을 직접 벌하지 않는다. TableVI Full/A1의 F1은0.96/0.83이며 퍼센트로 옮기지 않았다. A4, OSPA-T는 별도 부록이다. TableIII의 일부 P/R·MOTA* 불일치가 있어 이를 새로운 정량 근거로 사용하지 않는다. TAU-SRIR는 측정 RIR 합성이므로 현장 이동 혼합 녹음으로 설명하지 않는다. 다음 회차는 질문에 따른 답변 생성과 그 평가 조건으로 연결한다.
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
layout: seminar
variant: focus
---

# 같은 소리라도 위치를 바꾸면 답이 달라진다

::body::
<PaperFigure src="/diagrams/p2-s38-position-swap.png" alt="같은 두 음원의 좌우 위치를 교환한 두 장면. 청취자의 왼쪽 소리가 알람에서 말소리로 바뀐다." caption="설명용 장면 · 실제 모델 응답 아님" />

::takeaway::
BAT는 **음원과 위치의 대응**을 질문별 답변으로 읽도록 학습한다.

::source::
BAT, arXiv:2402.01591v4, Table 1 기반 설명용 재구성 C38. 실제 모델 출력 아님.

<!--
[S38]
[Sources]
- https://arxiv.org/html/2402.01591v4
[시각 자료]
직접 제작한 강의용 벡터 도식을 삽입했다. 원문 결과·예측을 재현한 그림이 아니며 기존 해석 범위와 평가 조건을 유지한다. SVG 원본과 2배 해상도 PNG는 public/diagrams에 보관한다.
[발표 노트]
앞서 SELD 역시 사건과 위치를 함께 추정했다. 언어 모델이 음원과 위치의 연결을 처음 도입한 것은 아니다. 이 장면에서는 소리의 목록을 유지한 채 위치만 교환했다. 왼쪽 소리를 묻는 질문의 정답이 바뀌므로, 알람과 말소리라는 종류만 알아서는 답할 수 없다. BAT는 위치로 음원을 고르기, 특정 음원의 위치 답하기, 두 음원의 관계 질문을 정해진 유형으로 학습한다.
[해석 범위]
화면은 Table 1의 질문 정의를 설명하는 재구성이며 실제 합성 음원이나 모델 예측을 시각화한 결과가 아니다. 학습 범위는 합성 단일·두 음원과 지정 질문 유형이다. 이를 모든 자유형 공간 대화의 해결로 확대하지 않는다.
[전환]
이런 질문에서 실제 청각 입력이 얼마나 도움이 되는지 같은 BAT의 입력 조건을 비교한다.
-->


---
layout: seminar
variant: result
---

# BAT: 질문에 바이노럴 관측을 더하면

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
[S39]
[Sources]
- https://arxiv.org/html/2402.01591v4
[발표 노트]
표의 P는 prompt, B는 binaural을 뜻한다. 같은 최종 BAT에 질문만 주는 경우와 질문·오디오를 함께 주는 경우를 읽는다. Type E는 두 음원 관계의 Yes/No 질문이며 평균 balanced accuracy로 평가한다. 질문만으로도 54.48%가 남고 바이노럴을 제공하면 76.89%로 높아진다. 공간 인코더의 사전학습과 perception-to-reasoning 언어 연결 학습을 구분해야 한다.
[해석 범위]
AudioSet 원음을 SoundSpaces RIR로 공간화한 10초 합성 바이노럴 조건이다. mono 행은 stage III만 학습한 모델이므로 여기의 최종 three-stage 모델과 입력만 다른 통제가 아니다. 이 결과는 청각 관측의 유용성을 보이지만 특정 위상 단서의 인과효과는 분리하지 않는다.
[전환]
사건 이름과 방향·거리는 같은 특징을 같은 비율로 읽어도 되는지 DSpAST의 설계를 살펴본다.

[시각화 전 표의 수치·조건 보존]
SpatialSoundQA · 두 음원의 관계 Yes/No · 같은 최종 BAT

모델에 제공한 입력 | Type E 평균 BA (%) / 높을수록 좋음 | 

P · 질문만 | 54.48 | 

B + P · 바이노럴 + 질문 | 76.89 |
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->


---
layout: seminar
variant: focus
---

# DSpAST: 같은 관측에서 다른 특징을 읽는다

::body::
<PaperFigure src="/diagrams/p2-s40-feature-selection.png" alt="바이노럴 파형의 여러 특징을 과제별로 가중하고 공유 파라미터의 세 경로로 사건, 방향, 거리를 읽는 구조." caption="설계 재구성 · 가중 막대는 설명용" />

::takeaway::
DSpAST는 **과제별 특징 선택**을 위해 사건·방향·거리의 정보 경로를 나눈다.

::source::
DSpAST, arXiv:2509.13927v1, §3.2·Fig. 1 기반 설명용 재구성 C40.

<!--
[S40]
[Sources]
- https://arxiv.org/html/2509.13927v1
[시각 자료]
직접 제작한 강의용 벡터 도식을 삽입했다. 원문 결과·예측을 재현한 그림이 아니며 기존 해석 범위와 평가 조건을 유지한다. SVG 원본과 2배 해상도 PNG는 public/diagrams에 보관한다.
[발표 노트]
하나의 바이노럴 관측에 세 종류의 질문을 붙인다. 사건 이름을 구분하는 정보와 방향·거리를 구분하는 정보가 동일한 중요도를 가져야 할 이유는 없다. DSpAST는 여러 입력 특징의 가중과 과제별 분기를 통해 이 차이를 설계에 반영한다. 그림의 공유 backbone은 Transformer와 patch embedding이 파라미터를 공유한다는 뜻이다. 독립된 대형 인코더 세 개로 설명하지 않는다.
[해석 범위]
화면은 §3.2의 설계 의도를 재구성한 개념도다. Fig. 1은 방법 그림이며 Fig. 2의 평균 attention도 단서 사용의 인과 검증은 아니다. 실제 개선에는 추가 특징, 사전학습 curriculum, AdaCos loss 변경이 함께 포함된다.
[전환]
같은 single-stage BAT의 질문 결과에서 SpatialAST와 DSpAST를 비교한다.
-->


---
layout: seminar
variant: result
---

# DSpAST: 방향·거리·관계의 변화를 따로 읽는다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">합성 바이노럴 · single-stage BAT · 전체 질문 5 epochs, LoRA, greedy decoding</p>
<PaperFigure src="/diagrams/result-41.svg" alt="방향 정확도 (%) ↑
Type D · 8범주, DER (%) ↓
거리 오차 > 0.5 m, 관계 평균 BA (%) ↑
Type E 원문 수치 비교 그래프. SpatialAST: 34.80, 53.40, 74.04; DSpAST: 37.35, 48.51, 76.56" />
</div>

::takeaway::
선택한 세 지표는 개선됐지만, **분기 하나의 효과로 분리한 비교는 아니다.**

::source::
DSpAST, arXiv:2509.13927v1, Table 3의 single-stage 두 행. ↑ 높을수록, ↓ 낮을수록 좋음.

<!--
[S41]
[Sources]
- https://arxiv.org/html/2509.13927v1
[발표 노트]
앞 장의 설계가 최종 언어 질문에도 유용한지 읽는다. 먼저 Type D의 목표 음원 방향 정확도는 34.80에서 37.35%로 높아지고, 거리 오차가 0.5m를 넘는 비율 DER는 53.40에서 48.51%로 낮아진다. 두 음원 관계 Type E의 평균 BA도 74.04에서 76.56%로 높아진다. 방향 정확도, 거리 실패 비율, 관계 판단은 서로 다른 지표라 단순 합산하지 않는다.
[해석 범위]
이 비교에서는 인코더 특징뿐 아니라 사전학습 curriculum과 AdaCos loss도 다르다. 차이 전체를 세 분기에 귀속할 수 없다. 원 BAT와 checkpoint 및 의미 평가 embedding이 달라 S39 수치와 직접 연결하지 않는다. 원문의 질문 유형 설명 일부 오기는 BAT의 유형 정의를 따른다.
[전환]
특징 구조를 바꾸는 선택과 구분해, 공간 표현에 기하 정보를 학습 지도로 제공하는 OWL로 이동한다.

[시각화 전 표의 수치·조건 보존]
합성 바이노럴 · single-stage BAT · 전체 질문 5 epochs, LoRA, greedy decoding

인코더 | 방향 정확도 (%) ↑ / Type D · 8범주 | DER (%) ↓ / 오차 > 0.5 m 비율 | 관계 평균 BA (%) ↑ / Type E | 

SpatialAST | 34.80 | 53.40 | 74.04 | 

DSpAST | 37.35 | 48.51 | 76.56 |
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->


---
layout: seminar
variant: figure
---

# OWL: 방의 기하를 학습 지도에 쓴다

::body::
<PaperFigure src="/research/p2-owl-v1-fig2.png" alt="BiDepth 원문 Fig. 2. 청취자 관점 깊이 영상과 같은 장면의 바이노럴 음향 시뮬레이션" caption="왼쪽: 깊이 지도. 오른쪽: 청취자·음원 배치와 바이노럴 합성 장면." />

::aside::
<section><span class="seminar-label semantic-geometry">학습할 때</span><p>깊이와 RIR 정답으로<br/>기하적 제약을 제공</p></section><section><span class="seminar-label semantic-input">추론할 때</span><p>바이노럴 오디오와<br/>언어 질문을 제공</p></section>

::takeaway::
**깊이·RIR은 학습 지도**, 질문에 답할 때의 관측은 바이노럴 오디오다.

::source::
OWL, arXiv:2509.26140v1, Fig. 2. 원문 그림.

<!--
[S42]
[Sources]
- https://arxiv.org/html/2509.26140v1
[발표 노트]
소리는 음원뿐 아니라 방과 전파 경로에 의해 달라진다. BiDepth는 같은 청취 위치에서 기하와 음향을 연결하는 합성 데이터다. 왼쪽의 depth는 청취자 관점의 공간 기하를, 오른쪽은 청취자와 음원 배치에 따른 바이노럴 관측을 나타낸다. SAGE는 이런 학습 장면의 depth와 RIR 정보를 보조 지도에 사용한다.
[해석 범위]
깊이 영상을 추론 시에도 제공하는 시청각 QA로 소개하지 않는다. 합성 장면의 기하 지도를 이용한 학습과 실제 방에서의 일반화는 별개다. 저자가 기술한 room/source 분할이 곧 현실 환경 전반의 일반화 보장은 아니다.
[전환]
학습 시만 존재하는 기하 정보가 음향 표현에 어떻게 연결되는지 Fig. 4의 경로를 읽는다.
-->


---
layout: seminar
variant: method
---

# SAGE의 보조 학습은 OWL 추론과 구분된다

::body::
<PaperFigure src="/research/p2-owl-v1-fig4.png" alt="OWL Fig. 4 원문 구조. 왼쪽 SAGE의 깊이와 RIR 보조 학습, 오른쪽 바이노럴 오디오를 받는 OWL 추론" caption="왼쪽: depth·RIR로 SAGE 학습. 오른쪽: 고정 음향 인코더 → projector → LLM." />

::takeaway::
OWL QA 학습에서는 **SAGE 음향 인코더를 고정**하고 언어 연결을 학습한다.

::source::
OWL, arXiv:2509.26140v1, Fig. 4. 원문 구조도.

<!--
[S43]
[Sources]
- https://arxiv.org/html/2509.26140v1
[발표 노트]
원문 왼쪽 SAGE와 오른쪽 OWL을 구분한다. SAGE에서는 깊이와 음향 표현으로 RIR을 복원하는 보조 학습이 음향 표현에 영향을 준다. OWL의 추론 경로에는 바이노럴 음향 인코더가 만든 표현이 남고, 이를 projector로 언어 모델에 연결한다. OWL QA 학습에서는 SAGE 음향 인코더를 고정하고 projector와 LLM LoRA를 학습한다.
[해석 범위]
학습 그림의 depth와 RIR을 추론 입력 목록에 넣지 않는다. 구조도는 어떤 경로를 설계했는지 보여 주며 그 자체가 기하 이해 성공의 근거는 아니다. Q-Former 상세와 CoT curriculum의 효과는 본문의 loss 비교와 구분한다.
[전환]
다른 QA 시스템의 순위가 아니라, 같은 BiDepth의 loss 조건을 바꾼 실험으로 기하 지도의 기여를 읽는다.
-->


---
layout: seminar
variant: result
---

# SAGE: 기하 학습 항과 공간 예측 오차

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">BiDepth 합성 평가 · 추론 입력은 바이노럴 · 기하 지도 loss 비교</p>
<PaperFigure src="/diagrams/result-44.svg" alt="방향 MAE (°) ↓, 거리 DER (%) ↓ 원문 수치 비교 그래프. 바이노럴 loss · $\eta_2=0$: 26.32, 17.11; 전체 loss · $\eta_2=10^{-2}$: 21.67, 14.32" />
<p class="seminar-chart-note">DER: 거리 오차가 0.5 m를 넘는 비율</p>
</div>

::takeaway::
이 BiDepth 비교에서 **기하 학습 항을 포함한 조건**의 방향·거리 오차가 낮다.

::source::
OWL, arXiv:2509.26140v1, Table 5. DER: 거리 오차가 0.5 m를 넘는 비율.

<!--
[S44]
[Sources]
- https://arxiv.org/html/2509.26140v1
[발표 노트]
여기서는 전체 QA 시스템의 성능 차이보다 좁게 SAGE loss를 비교한다. 바이노럴 항만 사용한 η₂=0과 기하 항을 포함한 η₂=10⁻² 조건이다. 방향 MAE는 26.32도에서 21.67도로, 거리 오차가 0.5m를 넘는 DER는 17.11%에서 14.32%로 줄었다. 낮은 값이 좋은 두 오차 지표를 함께 읽는다.
[해석 범위]
이 수치를 CoT나 projector의 효과로 섞지 않는다. 또한 모든 전이 지표가 좋아지는 것은 아니다. Table 2의 SSQA MAE는 geometry SAGE 18.47도가 Spatial-AST 17.94도보다 높다. Table 4 QA 전체 시스템 비교와 Table 6 CoT 비교는 별도의 실험이다.
[전환]
기하 추정과 다른 문제로 옮겨, 기존 의미 인코더가 채널 레벨 차이를 얼마나 보존하는지 살펴본다.

[시각화 전 표의 수치·조건 보존]
BiDepth 합성 평가 · 추론 입력은 바이노럴 · 기하 지도 loss 비교

SAGE의 학습 조건 | 방향 MAE (°) / 낮을수록 좋음 | 거리 DER (%) / 낮을수록 좋음 | 

바이노럴 loss · $\eta_2=0$ | 26.32 | 17.11 | 

전체 loss · $\eta_2=10^{-2}$ | 21.67 | 14.32 |
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->


---
layout: seminar
variant: focus
---

# Dual-BEATs: 같은 소리의 좌우 gain만 바꾼다

::body::
<PaperFigure src="/diagrams/p2-s45-gain-waveforms.png" alt="동일한 파형에서 좌우 gain만 바꾼 Left, Center, Right의 세 예. 파형의 시간 구조는 유지되고 진폭만 변한다.">
  <template #caption><MathInline tex="L=g_L\,x" /> · <MathInline tex="R=g_R\,x" /> · 같은 모노 원음, gain만 변경 · 두 BEATs 경로 고정</template>
</PaperFigure>

::takeaway::
Dual-BEATs는 **제한된 좌우 레벨 차이**를 읽는 stereo 분류를 다룬다.

::source::
Dual-BEATs, arXiv:2607.08800v1, §3.2·Appendix A.3 기반 설명용 재구성 C45.

<!--
[S45]
[Sources]
- https://arxiv.org/html/2607.08800v1
[시각 자료]
직접 제작한 강의용 벡터 도식을 삽입했다. 원문 결과·예측을 재현한 그림이 아니며 기존 해석 범위와 평가 조건을 유지한다. SVG 원본과 2배 해상도 PNG는 public/diagrams에 보관한다.
Csound FLOSS Manual의 Panning and Spatialization 장에서 같은 신호를 채널별 이득으로 나누는 설명 방식을 참고했다: https://www.csound-tutorial.net/floss_manual/Release04/Cs_FM_04_ScrapBook/b-panning-and-spatialization.html . 그림의 진폭 비는 설명용이며 논문의 gain 범위나 pan law를 수치로 재현하지 않았다.
[발표 노트]
이번에는 방이나 실제 마이크 배열을 추정하는 문제를 잠시 내려놓고 입력 생성 조건을 제한한다. 하나의 모노 원음에 좌우 gain을 적용한다. 소리 내용은 같지만 채널 크기가 달라지고, 모델은 Left/Center/Right를 분류한다. 고정된 두 BEATs 경로가 각각 좌우 채널을 읽으며 projector와 언어 adaptation은 학습한다. 화면은 입력을 만드는 방법의 설명이고 실제 공간 신호나 모델 출력 그래프가 아니다.
[해석 범위]
amplitude panning을 HRTF가 반영된 물리적 방향 변화, 위상 활용, 방 잔향 또는 새로운 배열 전이와 동일시하지 않는다. 정규화가 어떤 단서를 지웠는지의 기전은 결과표 하나로 입증되지 않는다.
[전환]
각 채널에 작은 독립 잡음을 더한 dither 조건의 결과를 같은 panning 안에서 비교한다.
-->


---
layout: seminar
variant: result
---

# Dither의 효과는 panning 조건에 따라 달라진다

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
[S46]
[Sources]
- https://arxiv.org/html/2607.08800v1
[발표 노트]
같은 backbone과 출력 순서를 고정하고 각 PA 안에서 dither Off와 On을 읽는다. PA=0.50은 약한 채널의 gain이 0.5인 조건이며 Center를 뜻하지 않는다. 독립 dither의 진폭 DA는 0.05다. 이 조건의 방향 정확도는 37.9에서 97.1%로 높아진다. 반면 PA=0.00에서는 99.5에서 99.0%로 소폭 낮아진다. 따라서 모든 PA에서 일률적 이득이라고 말하지 않는다.
[해석 범위]
표의 97.1을 사용하며 초록의 97.2와 혼합하지 않는다. 학습·평가 random seed는 분리되지만 미관측 panning의 일반화가 새 HRTF·배열·잔향 전이는 아니다. semantic F1 저하 역시 공간 성과에 묻어 없애지 않는다. Table 1과 Fig. 2의 학습·평가 PA 조건은 구분해야 한다.
[전환]
입력 레벨 차이의 문제와 구별해 마이크 수와 배치 자체가 바뀌는 PhaseCoder를 살펴본다.

[시각화 전 표의 수치·조건 보존]
OLMo-3-7B + Dual-BEATs · Direction-First · 방향 정확도 (%) ↑

평가 PA | Dither Off | Dither On / DA = 0.05 | 

0.00 | 99.5 | 99.0 | 

0.50 | 37.9 | 97.1 |
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->


---
layout: seminar
variant: figure
---

# PhaseCoder: 채널 관계에 마이크 좌표를 더한다

::body::
<PaperFigure src="/research/p2-phasecoder-v2-input.png" alt="PhaseCoder Fig. 2 상단. 약 13 ms 구간에서 네 마이크 채널의 파형과 채널 간 위상 차이를 보여 주는 원문 패널" caption="원문 Fig. 2 상단: 네 채널 파형. x축 시간(ms), y축 amplitude." />

::aside::
<section><span class="seminar-label semantic-input">공간 경로</span><p>다채널 오디오<br/>+ 마이크 좌표</p></section><section><span class="seminar-label ">의미 경로</span><p>기존 mono 오디오<br/>+ 텍스트 질문</p></section><section><span class="seminar-label semantic-geometry">명칭의 범위</span><p>배열 변화에 대응<br/>좌표는 계속 필요</p></section>

::takeaway::
PhaseCoder의 추론 입력에는 **다채널 오디오와 마이크 좌표**가 함께 필요하다.

::source::
PhaseCoder, arXiv:2601.21124v2, Fig. 2 상단 패널 크롭.

<!--
[S47]
[Sources]
- https://arxiv.org/html/2601.21124v2
[발표 노트]
상단의 짧은 파형 구간에서 같은 음향 사건이 채널마다 서로 다른 관계로 관측되는 것을 본다. 같은 방향이라도 마이크의 수와 배치가 바뀌면 이런 관계가 달라진다. PhaseCoder는 다채널 오디오와 마이크 좌표를 받아 공간 토큰을 만들고, 기존 의미 오디오 경로와 함께 언어 모델에 제공한다. 그림의 아래 분류 head 결과는 이번 문제 관측과 분리하기 위해 크롭했다.
[해석 범위]
geometry-agnostic을 좌표가 필요 없다는 뜻으로 번역하지 않는다. 무지향·free-floating 마이크 배열 가정과 장치에 의한 산란 효과를 구분한다. 원문 Table 1의 실제 녹음 DOA는 인코더 평가이며 다음 QA 실험과 동일한 시험이 아니다.
[전환]
공간 입력을 언어 모델에 결합한 조건의 관계 QA를 읽고 전사 성능의 반례도 남긴다.
-->


---
layout: seminar
variant: result
---

# PhaseCoder: 관계 QA 개선과 전사 오류는 별개다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">Gemma · Task 2 관계 Yes/No 정확도 (%) ↑ · 두 발화를 비중첩 연결</p>
<PaperFigure src="/diagrams/result-48.svg" alt="Synthetic 정확도 (%) ↑, RSL2019 정확도 (%) ↑ 원문 수치 비교 그래프. Baseline · mono: 48.44, 53.91; SFT · 공간 입력 + 학습: 76.76, 73.83" />
<p class="seminar-chart-note">반례 · RSL Task 4 mean WER: 42.90 → 48.41 (낮을수록 좋음)</p>
</div>

::takeaway::
공간 입력과 SFT를 결합하면 **관계 QA는 개선되지만 전사까지 함께 좋아지지는 않는다.**

::source::
PhaseCoder, arXiv:2601.21124v2, Table 3. RSL QA는 train split 녹음에서 재구성.

<!--
[S48]
[Sources]
- https://arxiv.org/html/2601.21124v2
[발표 노트]
관계 Yes/No를 묻는 Task 2에서 Gemma baseline과 제안 SFT 시스템을 비교한다. 합성 평가의 정확도는 48.44에서 76.76%, RSL2019 재구성 QA는 53.91에서 73.83%로 높아진다. 그러나 목표 발화를 전사하는 RSL Task 4의 mean WER는 42.90에서 48.41로 악화한다. 서로 다른 과제를 합친 평균으로 이 상반된 결과를 가리지 않는다.
[해석 범위]
Baseline은 mono 입력이고 SFT에는 공간 입력과 추가 학습이 함께 들어가므로 공간 토큰만의 독립 인과효과가 아니다. Synthetic은 미사용 LibriSpeech·RIR·배열을 사용한다. RSL QA는 원 데이터 train split 녹음으로 재구성했으며 두 발화는 비중첩 연결이다. Gemma 의미 입력은 채널 평균이다. 원문은 WER>3.0 출력을 제외하므로 미필터 오류율을 보장하지 않는다.
[전환]
지금까지의 모델은 입력과 학습 조건이 다르므로 비교 계약을 정리한다.

[시각화 전 표의 수치·조건 보존]
Gemma · Task 2 관계 Yes/No 정확도 (%) ↑ · 두 발화를 비중첩 연결

시스템 조건 | Synthetic | RSL2019 | 

Baseline · mono | 48.44 | 53.91 | 

SFT · 공간 입력 + 학습 | 76.76 | 73.83 | 

반례　RSL Task 4 mean WER: 42.90 → 48.41 (낮을수록 좋음)
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->


---
layout: seminar
variant: compare
---

# 비교할 때는 입력과 학습 범위를 함께 읽는다

::body::
<PaperFigure src="/diagrams/p2-s49-learning-inference.png" alt="학습과 추론의 경계를 정렬한 그림. OWL의 깊이 지도는 학습에서 끝나며 PhaseCoder의 마이크 좌표는 추론에서 필요하다." caption="학습/추론 조건 비교 · 성능 순위 아님" />

::takeaway::
OWL의 **깊이는 학습 지도**, PhaseCoder의 **좌표는 추론 입력**이다.

::source::
P12–P16의 방법·학습 조건 종합. 성능 순위가 아닌 비교 조건표 C49.

<!--
[S49]
[Sources]
- https://arxiv.org/html/2402.01591v4
- https://arxiv.org/html/2509.13927v1
- https://arxiv.org/html/2509.26140v1
- https://arxiv.org/html/2601.21124v2
- https://arxiv.org/html/2607.08800v1
[시각 자료]
직접 제작한 강의용 벡터 도식을 삽입했다. 원문 결과·예측을 재현한 그림이 아니며 기존 해석 범위와 평가 조건을 유지한다. SVG 원본과 2배 해상도 PNG는 public/diagrams에 보관한다.
[발표 노트]
같은 공간 오디오 모델이라는 이름만으로 같은 문제를 푼다고 보기 어렵다. BAT와 DSpAST는 합성 바이노럴 표현의 사전학습을 QA 연결에 사용한다. OWL은 깊이·RIR로 학습한 인코더를 QA 단계에서 고정한다. Dual-BEATs의 두 의미 인코더는 고정이며 panning·dither 실험이다. PhaseCoder는 추론에서도 마이크 좌표를 필요로 한다.
[해석 범위]
BAT와 DSpAST를 한 행으로 묶었지만 인코더 특징과 사전학습의 변경을 동일시하지 않는다. 각 연구의 고정 모듈과 언어 adaptation 범위는 다르다. 전처리가 다르면 일반화라는 말이 가리키는 평가 대상도 달라진다. 이 표는 모델 간 통합 성능 순위를 만들지 않는다.
[전환]
한 질문의 답에서 여러 음원의 속성을 함께 기술하는 Sci-Phi의 출력으로 이동한다.
-->


---
layout: seminar
variant: focus
---

# Sci-Phi: 음원별 속성과 환경을 함께 기술한다

::body::
<PaperFigure src="/diagrams/p2-s50-scene-attributes.png" alt="방 안의 알람과 말소리에서 청취자로 이어지는 방향과 거리, 음원별 발생 구간, 방과 배경 속성의 연결." caption="출력 형식 재구성 · 실제 생성 응답 아님" />

::takeaway::
각 소리의 내용·시간·공간 속성이 **같은 음원에 붙어 있어야** 설명이 일관된다.

::source::
Sci-Phi, arXiv:2510.05542v1, §3.3 출력 형식 기반 설명용 재구성 C50.

<!--
[S50]
[Sources]
- https://arxiv.org/html/2510.05542v1
[시각 자료]
직접 제작한 강의용 벡터 도식을 삽입했다. 원문 결과·예측을 재현한 그림이 아니며 기존 해석 범위와 평가 조건을 유지한다. SVG 원본과 2배 해상도 PNG는 public/diagrams에 보관한다.
[발표 노트]
Sci-Phi는 질문 하나의 짧은 답 대신 장면 전체의 속성을 한 번에 생성한다. 방향성 음원마다 설명, 발생 구간, 방향, 거리, 음압, 명료도를 연결하고 비방향성 배경과 방 특성은 장면 단위로 기술한다. 화면의 항목은 출력 형식을 설명하며 모델이 실제로 생성한 응답은 아니다. 데이터의 방향성 음원 수는 최대 네 개다.
[해석 범위]
방과 배경 속성은 모델이 추정하는 값이다. 이를 직접 관측된 사실처럼 읽거나 모든 자유형 장면에 검증된 출력으로 확대하지 않는다. 각 필드를 따로 맞히는 것과 같은 음원에 올바로 대응시키는 것은 다르다. 예를 들어 알람의 왼쪽 위치를 말소리에 붙이면 소리 목록과 방향 목록은 맞아도 장면 기술이 틀리다.
[전환]
이 출력을 만들기 위해 FOA 공간 입력과 W 채널 의미 입력을 어떻게 결합하는지 본다.
-->


---
layout: seminar
variant: method
---

# Sci-Phi: FOA 공간 경로와 W 채널 의미 경로

::body::
<PaperFigure src="/research/sciphi-core.png" alt="Sci-Phi Fig. 1. FOA의 공간 특징과 W 채널 spectral 특징을 두 인코더·projector로 Phi-4에 결합한 원문 구조" caption="공간 경로는 적응하고, 기존 mono 의미 인코더·projector·audio LoRA는 고정한다." />

::takeaway::
FOA의 **공간 특징**과 W 채널의 **의미 특징**을 별도 경로로 언어 모델에 전달한다.

::source::
Sci-Phi, arXiv:2510.05542v1, Fig. 1의 인코더·projector·LLM 경로 크롭.

<!--
[S51]
[Sources]
- https://arxiv.org/html/2510.05542v1
[발표 노트]
FOA 네 채널의 mel 특징과 W를 기준으로 계산한 intensity vector를 공간 인코더가 읽는다. 기존 mono 의미 인코더는 W 채널의 mel 특징만 읽는다. 두 경로의 projector가 언어 모델에 결합한다. 원문의 불 표식은 학습, 눈송이는 고정을 뜻한다. 공간 인코더와 공간 projector, spatial LoRA는 적응하고 기존 의미 인코더, 의미 projector, audio LoRA는 고정한다.
[해석 범위]
의미 경로를 구조적으로 유지한다는 사실만으로 모든 기존 언어·오디오 능력의 보존이 입증되지는 않는다. 비교 기준선은 고정 SELDNet 표현을 쓰며 Sci-Phi는 공간 encoder도 적응한다. 두 시스템 모두 장면 기술에 미세조정했다는 점이 다음 결과 해석의 전제다.
[전환]
여러 속성을 출력한 뒤에는 같은 음원에 올바로 연결됐는지 함께 채점해야 한다.
-->


---
layout: seminar
variant: figure
---

# Sci-Phi: 속성을 같은 음원에 묶어 평가한다

::body::
<PaperFigure src="/research/p2-sciphi-v1-tuplescore.png" alt="Sci-Phi Fig. 2 TupleScore 원본 패널. SELDNet+Phi-4 MC FT와 Sci-Phi의 합성 RIR 및 실측 RIR 조건, diamond는 1–4음원 평균" caption="원본 점·축 보존. 오른쪽 두 모델의 ◆·◇(1–4음원 평균)를 비교한다." />

::aside::
<section><span class="seminar-label ">TupleScore · 0–1, 높을수록 좋음</span><p>What × Where × When의<br/>기하평균</p></section><section><span class="seminar-label semantic-geometry">RIR 조건을 분리</span><p>◆ 합성 RIR<br/>◇ 실측 RIR로 합성</p></section><section><span class="seminar-label ">이번에 읽는 비교</span><p>SELDNet+Phi-4 (MC, FT)<br/>↔ Sci-Phi</p></section>

::takeaway::
같은 RIR 조건에서 **Sci-Phi의 평균 TupleScore가 미세조정 기준선보다 높다.**

::source::
Sci-Phi, arXiv:2510.05542v1, Fig. 2 TupleScore 패널 크롭·§4. 정밀값을 추정해 재작성하지 않음.

<!--
[S52]
[Sources]
- https://arxiv.org/html/2510.05542v1
[발표 노트]
먼저 이름과 방향을 바꿔 붙인 예를 떠올린다. 알람은 왼쪽이고 말소리는 오른쪽인데 출력이 이 연결을 뒤집었다면 이름 목록과 방향 목록이 각각 맞아도 장면 설명은 틀리다. TupleScore는 What·Where·When의 기하평균으로 음원 단위 공통 대응을 정한다. 원문 패널의 오른쪽 두 모델, SELDNet+Phi-4 (MC, FT)와 Sci-Phi를 선택한다. ◆는 synthetic-RIR, ◇는 real-RIR의 1–4음원 전체 평균이다. 두 조건 모두 Sci-Phi의 평균이 더 높다.
[해석 범위]
원본 축과 점을 보존하기 위해 mono 및 ○·□도 남겼지만 이 장의 비교는 두 모델의 diamond에 한정한다. ○는 한 음원, □는 네 음원이며 평균으로 읽지 않는다. 두 모델 모두 장면 기술에 미세조정했고 baseline은 공간 encoder 고정, Sci-Phi는 적응한다. 실측 RIR은 실제 배경을 더해 합성한 장면이지 현장 혼합음 녹음이 아니다. real-RIR는 수평 방향 위주이며 방 크기와 배경 라벨이 없다. Table 2의 OM/OS는 채점 원칙이고 모델 ablation이 아니다.
[전환]
전체 장면 기술과 구별해 위치 기반 식별과 상대 관계 질문을 따로 정의한 Spatial-Omni를 본다.
-->


---
layout: seminar
variant: figure
---

# Spatial-Omni: 추정·식별·관계는 다른 질문이다

::body::
<div style="display:grid;grid-template-columns:340px 1fr;gap:42px;height:100%">
<PaperFigure src="/research/p2-spatialomni-v2-fig2a.png" alt="Spatial-Omni Fig. 2a 원문 과제 분류도. 공간 검출 및 위치 추정, 공간 관계 이해, 복합 추론 범주" caption="원문 Fig. 2(a): 과제 분류" />
<div style="display:flex;flex-direction:column;justify-content:center;gap:22px">
<section><span class="seminar-label">EAzi · 위치 추정</span><p>“알람은 어느 방향인가?”</p></section>
<section><span class="seminar-label">IS-Loc · 위치로 음원 식별</span><p>“왼쪽에서 나는 소리는 무엇인가?”</p></section>
<section><span class="seminar-label">RLR · 두 음원의 상대 좌우</span><p>“알람은 말소리보다 왼쪽에 있는가?”</p></section>
<p class="seminar-figure-note">오른쪽 질문은 과제 정의에 따른 설명용 재구성이다.</p>
</div></div>

::takeaway::
위치를 추정하는 능력과 **그 위치의 소리를 고르거나 비교하는 능력**을 따로 평가한다.

::source::
Spatial-Omni, arXiv:2606.10738v2, Fig. 2(a)·과제 정의. 질문은 C53 재구성.

<!--
[S53]
[Sources]
- https://arxiv.org/html/2606.10738v2
[발표 노트]
왼쪽 원문 Fig. 2(a)는 개별 질문의 실제 사례가 아니라 SO-Bench의 과제를 분류한 원형도다. 오른쪽 질문은 발표자가 정의를 설명하기 위해 재구성했다. EAzi는 목표 음원의 방위각을 추정하고, IS-Loc은 위치 조건에 맞는 소리를 고르며, RLR은 두 음원의 상대적 좌우 관계를 답한다. 이름과 위치의 대응은 뒤의 두 과제에서 직접 필요하다.
[해석 범위]
원문 사례라고 오인시키지 않도록 재구성 문구를 남겼다. 질문 문장의 길이가 곧 추론 깊이는 아니다. 과제마다 정답 형식과 채점이 다르므로 정확도 하나로 보편적 공간 이해 능력을 나타내지 않는다.
[전환]
이 질문을 위한 FOA 공간 토큰이 기존 의미 입력과 어디에서 결합하는지 본다.
-->


---
layout: seminar
variant: method
---

# Spatial-Omni: FOA 공간 토큰을 언어 입력에 더한다

::body::
<PaperFigure src="/research/spatialomni-core.png" alt="Spatial-Omni Fig. 1 오른쪽 경로. FOA 공간 encoder와 W 채널 audio encoder가 각각 projector를 거쳐 언어 입력에 결합" caption="Fig. 1 오른쪽 경로 크롭. 영상은 기존 backbone의 선택 경로이며 공간 QA의 추가 관측이 아니다." />

::aside::
<section><span class="seminar-label semantic-input">두 입력 경로</span><p>FOA → 공간 encoder<br/>W → 의미 encoder</p></section><section><span class="seminar-label semantic-geometry">학습 순서</span><p>projector 정렬<br/>→ LoRA 결합<br/>→ 공간 경로 적응</p></section>

::takeaway::
**공간 토큰을 결합하는 구조**와 일반 오디오 성능을 보존했다는 주장은 구분한다.

::source::
Spatial-Omni, arXiv:2606.10738v2, Fig. 1 오른쪽 패널·§5.

<!--
[S54]
[Sources]
- https://arxiv.org/html/2606.10738v2
[발표 노트]
FOA 공간 관측은 SO-Encoder에 들어가고 W 채널은 기존 Audio Encoder로 들어간다. 별도의 projector가 공간 표현을 언어 토큰 차원에 맞춰 기존 오디오 및 텍스트 토큰과 결합한다. 원문의 전체 그림 중 결합 경로를 크롭했으며 SO-Encoder 내부 블록은 생략했다. 원본의 visual branch는 기반 멀티모달 모델의 구조이고 여기의 공간 QA에서 영상 정보를 새 관측으로 사용한다는 뜻은 아니다.
[해석 범위]
기본 학습은 projector 정렬, LLM LoRA 결합, 공간 encoder의 학습 가능한 부분을 포함한 적응으로 구성된다. 기존 의미 경로를 구조적으로 보존하는 것과 실제 일반 오디오 성능의 보존은 다르다. Fig. 5에서 MIX는 일부 성능을 회복하지만 완전 보존으로 말하지 않는다.
[전환]
같은 SO-7B에서 공간 토큰을 없앤 조건과 실제 토큰을 제공한 조건을 비교한다.
-->


---
layout: seminar
variant: result
---

# Spatial-Omni: 공간 토큰이 없으면 무엇이 달라질까?

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">SO-Bench · 같은 7B 계열 · greedy decoding · 점수는 모두 % (높을수록 좋음)</p>
<PaperFigure src="/diagrams/result-55.svg" alt="EAzi (%) ↑
방위각 오차 ≤ 20°, IS-Loc (%) ↑
위치로 음원 식별, RLR (%) ↑
상대 좌우 원문 수치 비교 그래프. SO-7B-zs · 공간 토큰 0: 13.06, 40.69, 47.15; SO-7B · 실제 공간 토큰: 76.38, 66.81, 72.97" />
</div>

::takeaway::
실제 공간 토큰 조건에서 **위치 추정·음원 식별·관계 판단**의 점수가 높다.

::source::
Spatial-Omni, arXiv:2606.10738v2, Table 2의 SO-7B-zs/SO-7B. MIX와 구분.

<!--
[S55]
[Sources]
- https://arxiv.org/html/2606.10738v2
[발표 노트]
S53에서 구분한 세 질문으로 돌아간다. SO-7B-zs는 공간 토큰을 0으로 만든 조건이고 SO-7B는 실제 공간 토큰을 받는다. EAzi는 방위각 오차가 20도 안에 들어오는 비율, IS-Loc은 위치 기반 식별, RLR은 상대 좌우 판정이다. 선택한 세 점수가 실제 공간 토큰 조건에서 모두 높다. 같은 7B 계열의 내부 비교로 읽는다.
[해석 범위]
입력 ablation이 공간 정보의 유용성을 보이지만 특정 phase 기전을 입증하지 않는다. SO-7B와 MIX를 섞지 않는다. 복합 MH 점수는 22.52/39.93으로 여전히 어렵다. 일반 오디오 성능의 완전 보존이나 임의 배열 일반화는 이 실험으로 주장할 수 없다. SC의 WER는 낮을수록 좋은 별도 지표다.
[전환]
개별 관계 질문을 더 복합적인 장면 선택과 구별한 TWNM의 세 평가 층위를 본다.

[시각화 전 표의 수치·조건 보존]
SO-Bench · 같은 7B 계열 · greedy decoding · 점수는 모두 % (높을수록 좋음)

모델·공간 입력 | EAzi / 방위각 오차 ≤ 20° | IS-Loc / 위치로 음원 식별 | RLR / 상대 좌우 | 

SO-7B-zs · 토큰 0 | 13.06 | 40.69 | 47.15 | 

SO-7B · 실제 토큰 | 76.38 | 66.81 | 72.97 |
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->


---
layout: seminar
variant: figure
---

# TWNM: 지각·연결·복합 질의를 구분한다

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
[S56]
[Sources]
- https://arxiv.org/html/2601.02954v3
[발표 노트]
같은 청취자 기준의 장면에서 필요한 답의 종류를 차례로 바꾼다. L1은 사건 종류나 위치 같은 개별 관측을 읽고, L2는 어떤 속성이 어느 음원에 속하는지 연결한다. L3는 관찰자 회전, 음원 제거, 복합 조건 등의 질문을 적용한다. 화면의 그림은 Fig. 4에서 청취자 중심 장면을 선택한 도해이며 오른쪽은 과제 정의를 설명하는 한국어 질문이다.
[해석 범위]
원문 도해는 네 개의 기호를 보이는 개념 예시지만 실제 모델의 source slots와 주평가 합성 장면은 최대 세 음원이다. 예시 그림과 숨겨진 scene metadata는 모델의 추론 입력이 아니다. 정답 생성에 사용하는 metadata와 audio-only 질문 입력을 구분한다. 그래프 기호는 평가 목표의 정의이며 명시적 scene graph 출력이 아니다. L3 점수를 순수 공간 추론 능력 전체로 해석하지 않는다.
[전환]
이런 질문을 위해 공간 표현과 의미 표현을 결합하는 방법, 그리고 학습 순서를 확인한다.
-->


---
layout: seminar
variant: method
---

# TWNM: 음원 단위 지도와 언어 결합을 나눈다

::body::
<PaperFigure src="/research/p2-twnm-v3-fig2.png" alt="TWNM Fig. 2 원문 구조. FOA spatial encoder와 semantic encoder, hybrid projector와 단계별 언어 학습" caption="v3: 공간 encoder 학습·적응 → projector 정렬 → SFT → SAPO." />

::takeaway::
source slots로 공간 인코더를 지도하고, **dense 음향 토큰**을 의미 경로와 결합한다.

::source::
The World is Not Mono, arXiv:2601.02954v3, Fig. 2·§4.1–4.2. v3의 FOA·SAPO.

<!--
[S57]
[Sources]
- https://arxiv.org/html/2601.02954v3
[발표 노트]
원문의 왼쪽은 FOA 오디오를 공간 경로와 의미 경로로 나누고, 가운데 hybrid projector가 두 표현을 결합하는 구조다. 의미 경로는 W 채널의 고정 Whisper-small이고 공간 encoder는 최대 세 source slots와 방향·거리·사건·존재 여부를 지도 학습한다. 다만 pooled slot head만 LLM에 보내는 것은 아니다. §4.1은 dense encoder map을 의미 경로 길이에 맞춰 결합한다고 설명한다.
[해석 범위]
그림의 Stage 1은 공간 인코더 학습·적응, Stage 2는 projector 정렬, Stage 3은 SFT, Stage 4는 SAPO다. v3의 FOA와 SAPO를 초기 버전의 binaural·GRPO로 바꾸지 않는다. source slots에 의한 내부 지도와 명시적인 scene graph 출력도 다르다.
[전환]
최종 SAPO 단계가 모든 질문 수준에서 함께 좋아지는지 SFT와 비교한다.
-->


---
layout: seminar
variant: result
---

# TWNM: SAPO는 L3를 높이고 L1·L2를 낮췄다

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
[S58]
[Sources]
- https://arxiv.org/html/2601.02954v3
[발표 노트]
가장 큰 변화는 L3의 51.19에서 79.76% 상승이다. 그러나 앞의 두 열도 읽으면 L1은 65.19에서 63.64%, L2는 70.61에서 69.89%로 소폭 낮아졌다. 따라서 최종 정책 학습이 모든 능력을 동시에 개선했다고 요약하지 않는다. 같은 exact MCQA 프로토콜의 단일 실행 결과다.
[해석 범위]
평가의 렌더 장면, 공간 구성, 질문과 정답은 학습에서 분리했지만 dry-source clip identity는 중복될 수 있다. 새로운 음원 정체성에 대한 전이라고 부르지 않는다. STARSS23 QA는 encoder 적응 녹음과 분리되지 않아 recording-disjoint 전이도 아니다. strict pick-letter audit를 사용한 corrupted-input 통제는 본문의 full-FOA exact score와 동일한 채점 효과 크기로 합치지 않는다.
[전환]
시간 변화가 들어오면 사건 순서, 음원 이동, 질의 구간의 요구를 나눠야 한다.

[시각화 전 표의 수치·조건 보존]
ASA benchmark · 최대 3음원 합성 FOA · exact MCQA · 단일 실행 · 정확도 (%) ↑

학습 단계 | L1 / 지각 | L2 / 관계 연결 | L3 / 복합 질의 | 

TWNM-SFT | 65.19 | 70.61 | 51.19 | 

TWNM-SAPO | 63.64 | 69.89 | 79.76 |
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->


---
layout: seminar
variant: focus
---

# 시간 이해가 요구하는 정보는 세 가지로 나뉜다

::body::
<PaperFigure src="/diagrams/p2-s59-time-requirements.png" alt="사건의 시간 막대, 한 음원의 연속 위치 곡선, 질문 관련 시간 구간을 나란히 보여 주는 세 시간 관계." caption="설명용 시간축 · 실제 모델 예측 아님" />

::takeaway::
**순서·연속 이동·질의 구간**은 서로 다른 시간 정보의 요구다.

::source::
Motion 2025, arXiv:2509.14666v1, Table 1; Dynamic QA, arXiv:2602.16334v1, Table 2 기반 C59.

<!--
[S59]
[Sources]
- https://arxiv.org/html/2509.14666v1
- https://arxiv.org/html/2602.16334v1
[시각 자료]
직접 제작한 강의용 벡터 도식을 삽입했다. 원문 결과·예측을 재현한 그림이 아니며 기존 해석 범위와 평가 조건을 유지한다. SVG 원본과 2배 해상도 PNG는 public/diagrams에 보관한다.
[발표 노트]
알람이 말소리보다 먼저 울렸는지는 사건 순서다. 같은 알람의 위치가 왼쪽에서 오른쪽으로 바뀌었는지는 연속 이동이다. 알람이 울린 특정 구간에만 답해야 하는 경우는 질문 관련 시간 선택이다. 이 세 질문은 시간 이해라는 말 안에 함께 들어갈 수 있지만 서로 다른 관측과 평가가 필요하다.
[해석 범위]
화면은 논문의 질문 범주를 설명하기 위한 재구성이지 실제 오디오나 예측 궤적이 아니다. 두 사건이 순서대로 발생했다고 해서 한 음원이 이동한 것은 아니다. 세 축을 발전 단계나 성능 순위로 만들지 않는다. 이후 Motion과 Dynamic QA는 움직임·구간 선택, ST-AudioLM은 시간별 공간 상태, CoSTALA는 사건 순서의 검색을 읽는다.
[전환]
먼저 시간별 지각 예측을 구조화해 추론 LLM에 전달하는 Motion 2025를 본다.
-->


---
layout: seminar
variant: result
---

# Motion 2025: 예측 속성을 읽는 추론 경로

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
[S60]
[Sources]
- https://arxiv.org/html/2509.14666v1
[발표 노트]
언어 모델이 원 파형을 직접 듣는 경로가 아니라 지각 모델의 시간별 예측을 JSON으로 읽는 구조다. 동일한 DeepSeek-R1-distilled Qwen-7B와 greedy decoding을 사용한 두 행을 고른다. DSAST에 AGM을 결합하면 Overall은 20.7에서 31.1%로 높아진다. 그러나 DoA·trajectory는 35.8에서 26.4%로 낮아진다. 이를 모든 움직임 질문의 개선으로 요약하지 않는다.
[해석 범위]
지각 인코더와 AGM은 학습하며 training-free는 추가 추론 LLM 연결에 관한 표현이다. stereo STARSS23 기반 시간별 예측을 사용하고 QA는 STARSS23 test metadata에서 만든 Boolean·single-answer MCQ다. 정답 속성을 넣는 oracle 결과와 혼합하지 않는다. Table 2 미관측 클래스 encoder 평가는 이 QA 표와 별개다. 본문 문장의 일부 모델명보다 정확한 표 행을 따른다.
[전환]
질문과 관련된 구간을 더 잘 골라주면 답이 달라지는지 Dynamic QA의 두 조건 축을 읽는다.

[시각화 전 표의 수치·조건 보존]
학습한 지각 결과 → JSON → 같은 Qwen-7B 추론 모델 · QA 정확도 (%) ↑

지각 → 추론 경로 | DoA·trajectory | Overall | 

DSAST + Qwen7B | 35.8 | 20.7 | 

DSAST w/ AGM + Qwen7B | 26.4 | 31.1 |
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->


---
layout: seminar
variant: result
---

# Dynamic QA: 구간 선택과 thinking을 분리한다

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
[S61]
[Sources]
- https://arxiv.org/html/2602.16334v1
[발표 노트]
한 번에 한 조건만 바꿔 읽는다. Thinking 행에서는 NoMask 54.3, AGM 55.0, 정답 구간 GT 56.1%다. Non-Thinking 행에서는 54.1, 54.0, 54.1%로 거의 변하지 않는다. 같은 mask의 두 행을 비교하면 thinking의 효과도 볼 수 있다. Overall은 Yes/No, MCQ, open 질문을 포함한다.
[해석 범위]
AudioSet strong-labeled 원음에 움직임을 부여한 합성 stereo 평가다. 시간 정보를 확장한 BAT 계열 encoder, Q-Former, Qwen3-4B를 학습하고 AGM은 추론 전처리다. GT는 배포 가능한 관측이 아니라 정답 이벤트 구간을 제공한 참고 조건이다. 시간 mask는 구간 밖 파형을 0으로 하므로 같은 구간의 간섭 음원을 완전히 제거하지 못한다. 수치 차이를 통계적 유의성이나 rationale의 청각적 충실성 증명으로 바꾸지 않는다.
[전환]
구간 선택과 구별해 시간별 공간 표현 자체를 유지하는 ST-AudioLM을 살펴본다.

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
layout: seminar
variant: focus
---

# ST-AudioLM: 같은 음원의 시간을 따라가야 한다

::body::
<PaperFigure src="/diagrams/p2-s62-source-trajectories.png" alt="시간을 따라 교차하는 알람 A와 말소리 B의 좌우 위치 곡선. 나중 시점에서 A는 오른쪽, B는 왼쪽에 있다." caption="좌우 위치–시간 재구성 · 실제 예측 아님" />

::takeaway::
각 순간의 위치를 넘어 **음원 정체성과 시간별 공간 상태**를 함께 유지해야 한다.

::source::
ST-AudioLM, arXiv:2606.14141v1, ST-AudioQA Table 1 기반 설명용 재구성 C62. 실제 예측 아님.

<!--
[S62]
[Sources]
- https://arxiv.org/html/2606.14141v1
[시각 자료]
직접 제작한 강의용 벡터 도식을 삽입했다. 원문 결과·예측을 재현한 그림이 아니며 기존 해석 범위와 평가 조건을 유지한다. SVG 원본과 2배 해상도 PNG는 public/diagrams에 보관한다.
[발표 노트]
한 시점의 방향 추정이 맞아도 다음 시점에 음원 정체성이 바뀌면 관계 질문을 틀릴 수 있다. 화면에서 알람 A와 말소리 B는 계속 같은 이름을 유지한다. 질문은 특정 소리가 움직인 뒤의 관계를 요구하므로 음원 정체성, 참조 시점, 시간별 공간 상태를 함께 읽어야 한다. 그림의 방향은 이해를 위한 단순 예이며 실제 모델 궤적이나 생성 결과가 아니다.
[해석 범위]
ST-AudioQA는 통제된 한·두 음원 합성 장면으로 구성한다. 이런 성과를 밀집한 현실 동적 장면이나 연속 대화의 해결로 확대하지 않는다. 정적인 위치 설명과 움직임에 조건을 둔 관계 질문은 서로 다른 출력 요구다.
[전환]
시간별 공간 상태가 언어 입력까지 남도록 만든 표현 경로를 본다.
-->


---
layout: seminar
variant: method
---

# ST-AudioLM: 사건 의미와 시간별 궤적을 전달한다

::body::
<PaperFigure src="/research/p2-staudiolm-v1-fig1.png" alt="ST-AudioLM Fig. 1. 의미 token과 dynamic trajectory token을 만드는 encoder 및 frozen encoder에서 connector와 LoRA로 이어지는 QA 구조" caption="왼쪽: 궤적 지도 학습. 오른쪽: 고정 ST-Audio Encoder + 학습하는 connector·LoRA." />

::takeaway::
QA 학습에서는 **의미·동적 궤적 토큰을 유지한 인코더를 고정**하고 언어 연결을 조정한다.

::source::
ST-AudioLM, arXiv:2606.14141v1, Fig. 1. 원문 방법 그림.

<!--
[S63]
[Sources]
- https://arxiv.org/html/2606.14141v1
[발표 노트]
왼쪽의 encoder는 사건 의미 토큰과 정적 위치 토큰, 시간 구간별 동적 궤적 토큰을 만든다. 궤적 토큰은 activity, direction, distance의 지도 학습으로 시간 정보를 유지한다. 오른쪽 QA 경로에서는 고정 ST-Audio Encoder가 의미 토큰 하나와 dynamic trajectory 토큰을 내보내고, 학습 가능한 두 층 MLP connector와 LoRA가 이를 언어 입력에 연결한다.
[해석 범위]
이 구조도는 방법을 설명하며 실제 움직임 예측 성공의 근거를 대신하지 않는다. 정적 encoder를 시간 구간별로 반복 적용하는 것과 궤적 지도 학습을 같은 방법으로 그리지 않는다. encoder Table 3와 실제 녹음 적응 결과는 다음 조합 QA 평가와 별개다.
[전환]
같은 FOA·언어 모델·토큰 인터페이스 조건에서 조합 질문 결과를 읽는다.
-->


---
layout: seminar
variant: result
---

# ST-AudioLM: 평균을 펼치면 움직임 난도가 남는다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">ST-AudioQA Type C · FOA, OLMo2, 41-token 인터페이스 · controlled-answer accuracy (0–100) ↑</p>
<PaperFigure src="/diagrams/result-64.svg" alt="시간 관계
Temp. rel., 이동 조건
Move-spat., 궤적 관계
Traj. rel., 평균 원문 수치 비교 그래프. Spatial-AST-FOA + OLMo2: 80.4, 55.2, 54.3, 63.3; ST-AudioLM: 86.0, 55.8, 60.6, 67.5" />
</div>

::takeaway::
조합 QA 평균은 높아졌지만 **이동·궤적 관계는 시간 관계보다 어려운 상태**로 남는다.

::source::
ST-AudioLM, arXiv:2606.14141v1, Table 5. ↑ 높을수록 좋음.

<!--
[S64]
[Sources]
- https://arxiv.org/html/2606.14141v1
[발표 노트]
같은 FOA 계열 입력과 OLMo2, 41-token 인터페이스를 사용하는 QA 학습 비교다. baseline은 정적 FOA encoder, ST-AudioLM은 궤적 지도를 학습한 표현을 사용한다. 평균은 63.3에서 67.5로 높아진다. 그러나 ST-AudioLM의 시간 관계 86.0에 비해 이동 조건 관계는 55.8, 두 음원 궤적 관계는 60.6이다. 평균만 보면 남는 난도를 놓칠 수 있다.
[해석 범위]
값은 통제된 답 형식의 0–100 정확도다. 모든 encoder 지표 우세나 밀집한 현실 장면의 해결을 뜻하지 않는다. BAT는 같은 scene metadata를 바이노럴로 렌더링해 받으므로 동일 입력 ablation이 아니다. Table 4 기본·두 음원 QA와 Table 3 encoder 및 실제 녹음 적응은 각각 따로 읽는다.
[전환]
연속 이동과 다른 시간 축, 즉 위치가 고정된 사건들의 발생 순서를 검색하는 CoSTALA로 옮긴다.

[시각화 전 표의 수치·조건 보존]
ST-AudioQA Type C · FOA, OLMo2, 41-token 인터페이스 · controlled-answer accuracy (0–100) ↑

QA 학습 모델 | 시간 관계 / Temp. rel. | 이동 조건 / Move-spat. | 궤적 관계 / Traj. rel. | 평균 | 

Spatial-AST-FOA / + OLMo2 | 80.4 | 55.2 | 54.3 | 63.3 | 

ST-AudioLM | 86.0 | 55.8 | 60.6 | 67.5 |
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->


---
layout: seminar
variant: focus
---

# CoSTALA: 순서나 위치가 다르면 다른 후보다

::body::
<PaperFigure src="/diagrams/p2-s65-event-negatives.png" alt="시간의 먼저와 나중, 공간의 왼쪽과 오른쪽 격자에서 기준 사건열, 순서 반전, 위치 교환을 비교한다." caption="사건 배치 재구성 · 화살표는 시간" />

::takeaway::
같은 두 소리도 **발생 순서·각 사건의 방향**이 달라지면 설명문과의 대응이 바뀐다.

::source::
CoSTALA, arXiv:2608.24374v1, §2.1 기반 설명용 재구성 C65. 겹치지 않는 두 FOA 사건·8방향.

<!--
[S65]
[Sources]
- https://arxiv.org/html/2608.24374v1
[시각 자료]
직접 제작한 강의용 벡터 도식을 삽입했다. 원문 결과·예측을 재현한 그림이 아니며 기존 해석 범위와 평가 조건을 유지한다. SVG 원본과 2배 해상도 PNG는 public/diagrams에 보관한다.
[발표 노트]
설명문과 잘 맞는 오디오를 검색하는 문제로 읽는다. 기준 사건열은 알람이 왼쪽에서 먼저 울리고 말소리가 오른쪽에서 나중에 난다. Temporal negative는 소리와 위치는 그대로 두고 순서를 뒤집는다. Spatial negative는 사건 순서를 유지하며 각 소리의 위치를 바꾼다. 화살표는 발생 순서를 뜻하며 한 음원의 이동 경로를 나타내지 않는다.
[해석 범위]
CoSTALA의 범위는 겹치지 않는 두 합성 FOA 사건과 8방향이다. 화면은 §2.1의 negative 구성을 설명하는 예다. 자유형 QA, 연속 음원 추적, 겹친 음원 분리의 성공 사례가 아니다. Fig. 1과 Fig. 2는 contrastive·local·consistency 학습의 방법 그림이며 실제 검색 결과와 구분한다.
[전환]
사건별 정렬과 일관성을 포함하는 전체 loss가 이 검색 문제에서 어떤 변화를 만드는지 본다.
-->


---
layout: seminar
variant: result
---

# CoSTALA: 사건별 정렬을 더한 검색의 변화

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
[S66]
[Sources]
- https://arxiv.org/html/2608.24374v1
[발표 노트]
Table 2의 contrastive-only와 전체 loss 두 행에서 Global Text-to-Audio R@1만 선택한다. 사건별 local alignment와 consistency 등을 포함한 전체 조건에서 5.84에서 8.10%로 높아진다. §3.1은 E_global과 T_st의 cosine similarity로 검색한다고 명시한다. Fig. 2의 최종 E_st를 직접 평가한 표라고 설명하지 않는다.
[해석 범위]
여러 loss를 함께 바꿨으므로 단일 loss의 독립 인과효과는 분리되지 않는다. Soft slicing은 원 segment duration을 사용하며 자동 사건 경계 추정의 성공은 확인하지 않았다. 의미 전용 열을 모든 의미 지표의 보존으로 확대하지 않는다. 새로운 음원·방 분할 일반화와 연속 이동 추적, 겹친 음원 분리, 자유형 QA는 별도 검증이 필요하다.
[이해 확인과 전환]
“사건 순서를 잘 검색하면 움직이는 음원도 잘 추적할까요?”에 대해 평가 대상이 달라 별도 검증이 필요하다고 답을 회수한다. 다음 절에서는 답변 정답률이 실제 청각 근거에 얼마나 의존하는지 따져본다.

[시각화 전 표의 수치·조건 보존]
두 합성 FOA 사건 · Global Text-to-Audio 검색 · $E_{\mathrm{global}}\leftrightarrow T_{\mathrm{st}}$의 cosine similarity

CoSTALA 학습 loss | Global T2A R@1 (%) / 높을수록 좋음 | 

대조 학습만 · $L_{\mathrm{cl}}$ | 5.84 | 

전체 · $L_{\mathrm{cl}}+L_{\mathrm{st}}+L_{\mathrm{local}}+L_{\mathrm{consist}}$ | 8.10 |
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->


---
layout: seminar
variant: figure
---

# 서로 다른 시험이 확인하는 것

::body::
<PaperFigure src="/diagrams/p3-evidence-targets.svg" alt="답변 정확도, 고정 표현의 선형 판독, 표적 위상 변경에 대한 거리 반응을 독립적으로 비교하는 세 그림" caption="문헌의 평가 대상과 측정값을 재구성한 개념도." />

::takeaway::
<strong>시스템의 답, 표현의 판독, 자극 반응</strong>은 서로 다른 증거다.

::source::
STAR-Bench v2 · WearVox v1 · SARL v2 · Interference/BMLD v1. 문헌 종합.

<!--
[S67]
[Sources]
- https://arxiv.org/html/2510.24693v2
- https://arxiv.org/html/2601.02391v1
- https://arxiv.org/html/2606.05544v2
- https://arxiv.org/html/2606.14820v1
[청중 질문]
지금까지의 좋은 답변 점수만으로 공간 정보를 읽고 특정 청각 단서를 썼다고 말할 수 있는가?
[발표 노트]
S66의 검색 결과도 특정 출력 계약임을 회수한다. 그다음 ‘답을 맞혔는가 / 정보가 읽히는가 / 단서 변경에 반응하는가’를 읽는다. WearVox는 별도의 실제 응답 대상 판단 사례로 위치시킨다.
SARL의 GRAM-B/F와 BMLD의 GRAM-T는 같은 평가 객체가 아니다. Spatial-AST 표현과 BAT 전체 질문응답 시스템도 구별한다. 네 실험을 모든 모델이 통과해야 하는 단계적 보장 사다리로 읽지 않는다.
[해석 범위]
Spatial-AST 인코더와 BAT 전체 QA 시스템, SARL의 GRAM-B/F와 BMLD의 GRAM-T를 동일 평가 객체로 연결하지 않는다. 단계별 보장 사다리가 아니며 전체 시험 모델 목록은 근거 대장과 부록이다.
[시각화 전 상세 본문 — 발표 설명용 보존]
시험 대상 | 바꾼 조건 | 측정한 것 | 
STAR-Bench
Gemini 2.5 Pro | 공간 질문 유형 | 답변 정확도 AA | 
WearVox
SC / MC Wearllama | 채널·시스템 학습 | 실제 side-talk 정확도 | 
SARL
고정 오디오 표현 | 음원·방 요인 | 학습한 선형 판독 점수 | 
BMLD
선택한 고정 인코더 | 표적 위상·파형 단서 | 임베딩 거리비 반응 | 


[핵심 결론]
시스템의 답, 표현의 판독, 자극 반응은 서로 다른 증거다.
[전환]
먼저 답변 평가 자체가 어떤 청각 정보를 요구하도록 설계되었는지 살핀다.
-->


---
layout: seminar
variant: method
---

# 설명문에 청각 단서가 얼마나 남아 있는가?

::body::
<PaperFigure src="/research/star-caption-panel.png" alt="STAR-Bench의 청각 입력과 텍스트 캡션 기반 추론 비교" caption="STAR-Bench Fig. 1의 audio/caption 비교 패널." />

::aside::
<section><span class="seminar-label">문장에 남은 정보</span><p>소리 · 사건</p></section><section><span class="seminar-label">따로 확인할 정보</span><p>방향 · 미세한 시간 관계</p></section>

::takeaway::
평가하려는 단서가 <strong>설명문에 보존되는지</strong>부터 확인한다.

::source::
STAR-Bench, arXiv:2510.24693v2, Fig. 1 관련 패널 크롭.

<!--
[S68]
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
[전환]
이런 질문을 실제 모델에 물었을 때의 보고 점수는 어느 기준과 비교해야 하는가?
-->


---
layout: seminar
variant: result
---

# STAR-Bench: 공간 질문의 점수와 우연 기준

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
[S69]
[Sources]
- https://arxiv.org/html/2510.24693v2
[청중 질문]
벤치마크의 낮은 평균은 어떤 종류의 질문에서 나온 것인가?
[발표 노트]
평가 모델의 버전과 질문 형식을 먼저 밝힌다. 우연 기준선을 읽고 과제별 점수를 비교한다. AA는 반복 실행 평균이고 ACR는 매번 맞힌 문항 비율임을 한 문장으로 구별한다.
이 표는 audio/caption ablation 결과표가 아니다. ACR는 모든 반복 실행에서 맞힌 문항의 비율이며 AA와 구별한다. 통계적 유의성, 위상 처리 기전 또는 최신 모든 모델의 능력을 이 숫자만으로 결론내리지 않는다.
[해석 범위]
숫자는 효과의 통계적 유의성이나 phase 사용을 입증하지 않는다. BAT의 0점 등을 기전 붕괴의 증거로 크게 쓰지 않는다. 서로 다른 입력 지원·전처리·응답 형식 적합성이 개입할 수 있다. 전체 19모델 순위표와 ACR는 부록이다.
[전환]
통제된 질문과 별도로, 실제 착용자 환경에서 ‘응답할 발화’를 고르는 문제를 보자.

[시각화 전 표의 수치·조건 보존]
세 선택지 MCQA · Gemini 2.5 Pro, 2025년 6월 업데이트 · AA (%) ↑평가 조건 | Localization | Relation | Trajectory | 
무작위 선택 | 33.33 | 33.33 | 33.33 | 
Gemini 2.5 Pro | 40.87 | 48.97 | 45.28 | 
AA: 반복 prompt 변형 실행의 평균 정확도
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->


---
layout: seminar
variant: method
---

# WearVox: 이 말은 기기에게 하는 말인가?

::body::
<PaperFigure src="/research/wearvox-side-talk-panel.png" alt="착용자의 발화가 기기에게 향한 것인지 다른 사람에게 향한 것인지 구별하는 side-talk 사례" caption="WearVox Fig. 1의 side-talk rejection 문제 패널." />

::aside::
<section><span class="seminar-label">기기에게 한 말</span><p>응답</p></section><section><span class="seminar-label">주변 사람끼리의 말</span><p>비응답</p></section>

::takeaway::
실제 착용자 장면에서는 <strong>발화의 응답 대상</strong>을 구별해야 한다.

::source::
WearVox, arXiv:2601.02391v1, Fig. 1의 side-talk 패널 크롭.

<!--
[S70]
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
[전환]
이 사례에서 추가 채널을 실제로 어떻게 제공했고, 무엇이 개선되었는가?
-->


---
layout: seminar
variant: result
---

# WearVox: 추가 채널을 쓴 시스템의 결과

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">실제 WearVox 시험 · Side Talk Rejection 정확도 (%) ↑</p>
<PaperFigure src="/diagrams/result-71.svg" alt="Side Talk Rejection 정확도 (%) ↑ 원문 수치 비교 그래프. SC · beamformed: 85.4; MC · 채널 0 + beamformed: 93.9" />
<p class="seminar-chart-note">MC는 두 채널을 interleave · 원시 전체 배열의 동시 입력은 아님</p>
</div>

::takeaway::
이 <strong>추가 채널·시스템 학습 조건</strong>에서 실제 응답 대상 판단이 개선됐다.

::source::
WearVox, arXiv:2601.02391v1, Fig. 2·Table 4. 원표의 85.4를 채택.

<!--
[S71]
[Sources]
- https://arxiv.org/html/2601.02391v1
[청중 질문]
이 논문의 ‘다채널’은 어떤 신호를 더 받는다는 뜻인가?
[발표 노트]
Fig. 2를 근거로 입력 차이를 말로 설명한 다음 표를 읽는다. 합성 다채널 학습과 실제 WearVox 시험을 구별한다. 같은 종류의 질문에서 추가 채널·시스템 구성이 어떤 이득을 보고했는지 한정한다.
음성 인코더를 고정하고 projection과 언어 모델을 학습한다. 실측 RIR을 활용한 합성 다채널 학습과 실제 착용자 시험을 구분한다. 채널0의 SNR, beamforming, 학습 조건이 함께 바뀌므로 위상만의 효과로 분리한 통제가 아니다. 서론의 85.6 대신 Table 4의 85.4를 사용했다.
[해석 범위]
모든 원시 마이크 채널의 동시 입력으로 그리지 않는다. 채널0의 SNR·beamforming·학습 변경이 함께 있으므로 phase-only 통제가 아니다. 초록/서론의 85.6이 아니라 Table 4의 85.4를 사용한다. 다른 응용 과제는 부록 밖 참고로 남긴다.
[전환]
시스템 출력을 잠시 떠나, 고정된 표현 자체에서 어떤 공간 정보가 읽히는지 묻는다.

[시각화 전 표의 수치·조건 보존]
실제 WearVox 시험 · Side Talk Rejection 정확도 (%) ↑입력·시스템 | 정확도 | 
SC · beamformed 채널 | 85.4 | 
MC · 채널 0 + beamformed | 93.9 | 
MC는 두 채널을 interleave한다. 원시 전체 배열의 동시 입력은 아니다.
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->


---
layout: seminar
variant: figure
---

# 공간 정보는 고정 표현에서 읽히는가?

::body::
<PaperFigure src="/diagrams/p3-sarl-linear-readout.svg" alt="합성 공간 장면이 고정 오디오 인코더를 지나고 시간 평균 표현에서 사건, 방위, 고도, 거리, 잔향, 부피, 형상을 각각 선형 판독하는 구조" caption="SARL 프로토콜 재구성 · 모델별 입력 형식 · 판독 20 epochs · 무작위 0, 완전 1" />

::takeaway::
<strong>인코더는 고정하고, 공간 요인의 판독기만 학습한다.</strong>

::source::
SARL, arXiv:2606.05544v2, §3·Table 1 기반 프로토콜 재구성.

<!--
[S72]
[Sources]
- https://arxiv.org/html/2606.05544v2
[청중 질문]
같은 음원도 위치·방이 달라질 때 인코더에 어떤 정보가 남는가?
[발표 노트]
S17의 고정/학습 범위를 회수한다. 범주 과제의 macro-F1과 연속량을 구간화한 판독 점수를 설명한다. 마지막으로 무작위 기준 0, 완전 성능 1의 정규화가 raw accuracy가 아님을 밝힌다.
범주 과제는 macro-F1, 연속량은 구간화·soft label 후 1−MAE/R을 계산하며 무작위 기준 b에 대해 (x−b)/(1−b)로 정규화한다. raw accuracy가 아니다. source와 room 과제군의 생성 파이프라인도 다르며, 한 요인의 낮은 선형 점수는 pooling 전 정보나 비선형 판독 가능성까지 부정하지 않는다.
[해석 범위]
source와 room 과제군은 생성 파이프라인도 달라 순수 요인 난이도만 비교하는 것이 아니다. 하나의 낮은 점수로 pooling 전 정보나 비선형 판독 가능성까지 부정하지 않는다. 수식과 모델별 입력 목록은 부록이다.
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
[전환]
이 고정된 시험에서 접근성과 단순한 반응 민감도는 어떻게 달라지는가?
-->


---
layout: seminar
variant: figure
---

# 표현이 변하는 것과 정보가 읽히는 것은 다르다

::body::
<PaperFigure src="/research/sarl-summary.svg" alt="SARL에서 사건 의미, 위치, 방 특성의 정규화 접근성을 비교한 원문 막대그래프" ><template #caption>의미 · 위치 · 방의 정규화 판독 점수. 원문 축과 입력 범례 유지.</template></PaperFigure>

::takeaway::
<strong>입력 변화에 대한 민감도</strong>와 목표 요인의 판독 가능성은 같은 측정이 아니다.

::source::
SARL, arXiv:2606.05544v2, Fig. 2. 민감도의 정의는 Fig. 3과 구별.

<!--
[S73]
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
[전환]
특정 단서를 바꾸는 최소 자극 실험은 어떤 더 좁은 질문에 답할 수 있을까?
-->


---
layout: seminar
variant: figure
---

# 오른쪽 표적의 위상을 뒤집는다면?

::body::
<PaperFigure src="/diagrams/p3-bmld-stimulus-waveforms.svg" alt="동일한 잡음을 공유한 두 채널의 파형. 잡음만, 양쪽 n+s, 왼쪽 n+s와 오른쪽 n-s 조건을 비교하고 잡음 기준 표현 거리비를 측정한다" caption="설명용 합성 파형(시간·진폭 임의 단위) · 고정 인코더 · final-block 평균 pooling" />

::takeaway::
측정값은 <strong>잡음 기준 임베딩 거리비</strong>이며, 인간의 탐지 역치와 구별한다.

::source::
Interference/BMLD, arXiv:2606.14820v1, §2 자극 정의 재구성.

<!--
[S74]
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
[전환]
주파수와 SNR를 고정한 한 조건부터 실제 결과를 읽는다.
-->


---
layout: seminar
variant: result
---

# 500 Hz의 위상 변경과 표현 거리 반응

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">500 Hz · SNR −14 dB · 고정 인코더, 모델별 전처리 · 100 seeds/cell</p>
<PaperFigure src="/diagrams/result-75.svg" alt="표현 거리비 지표 (dB) 원문 수치 비교 그래프. Spatial-AST: 6.8*; DSpAST: 7.0*; GRAM-T: 2.1*; WavJEPA: 0.5*" />
<p class="seminar-chart-note">* 원표의 FDR 보정 표시(<MathInline tex="q=0.05" />) · 양수: 역위상 조건의 표현 거리가 더 큼</p>
</div>

::takeaway::
양의 거리비는 <strong>이 자극·표현에서의 반응</strong>이며 청취 역치나 QA 정확도가 아니다.

::source::
Interference/BMLD, arXiv:2606.14820v1, Table 1·§2.3. 원문 수치·별표 유지.

<!--
[S75]
[Sources]
- https://arxiv.org/html/2606.14820v1
[청중 질문]
모델별 양의 반응이 보이면 모두 사람처럼 잡음 속 소리를 더 잘 듣는가?
[발표 노트]
S74의 두 거리를 회수하고 양수/음수의 뜻을 설명한다. 선택 모델들의 반응을 같은 자극에서 읽되 내부 전처리는 다름을 표시한다. 왼쪽 채널만 쓰는 mono 대조군은 입력이 변하지 않아 구성상0이라는 점을 말한다.
Table 1의 네 값과 별표를 보존했다. 원문은 sign-flip permutation을 5,000회 이상 수행하고 Benjamini–Hochberg FDR 보정을 적용한다. 95% bootstrap CI는 2,000회 이상 resampling으로 구한다. 단일채널 대조는 왼쪽 입력이 동일하여 구성상 0이며, EC=15.7 dB는 인간 실측 역치가 아닌 분석적 참조다. 한 주파수·SNR를 모든 자극이나 자연 장면으로 확대하지 않는다.
[해석 범위]
EC=15.7을 인간 실측 역치나 모델의 목표 정답으로 제시하지 않는다. 한 조건의 값으로 주파수 전역 일반화를 하지 않는다. 전체 모델/주파수 곡선과 pooling 비교는 부록으로 보낸다.
[전환]
이 반응을 설명할 수 있는 다른 신호 단서를 바꾸면 무엇이 남는가?

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
layout: seminar
variant: result
---

# 파형 단서를 바꾸면 어떤 반응이 남는가?

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
[S76]
[Sources]
- https://arxiv.org/html/2606.14820v1
[청중 질문]
위상 조건 반응이 다른 간섭 단서에도 의존한다면 어디까지 주장할 수 있는가?
[발표 노트]
무엇을 변형했는지 먼저 설명한다. 예를 들어 vocoded 75%는 50% unmasking+25% reversal이며 정확도75%가 아님을 읽는다. 파형 변형의 부수 변화도 있으므로 ‘phase 사용 증명’과 ‘phase가 전혀 없음’ 양쪽 단정을 피한다.
Unmasking은 양의 유의 반응, reversal은 음의 유의 반응이다. 두 비율을 분리해야 total 75%를 성능 정확도로 잘못 읽지 않는다. 원문 그림의 GRAM-T 네 조건과 양·음 방향을 표로 재작성했다. 파형 조작은 하나의 내부 기전을 유일하게 복원하지 않으며, phase 사용의 완전한 증명이나 phase 정보 부재로 단정하지 않는다. 추가 채널별 대조, 같은 parser 조건, 다른 pooling·판독은 후속 통제 제안이며 이 슬라이드가 보고하는 실행 결과가 아니다.
[해석 범위]
이후 제안할 채널별 대조·동일 parser·추가 pooling/판독 실험은 미실행이다. 이 결과는 배열 일반화나 모든 질문 응답 모델의 인과 추론을 시험하지 않는다. 상세 유의성 검정은 부록이다.
[전환]
이제 각 논문이 처음의 질문에 어느 입력과 근거로 답했는지 회수한다.

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


---
layout: seminar
variant: figure
---

# 같은 알람 장면에서 출력은 달라진다

::body::
<PaperFigure src="/diagrams/p3-alarm-evidence-recap.svg" alt="공통 알람 장면에서 방향 응답과 목표 선택, 공간 문장과 음원별 장면 기술, 시간 움직임 판단으로 갈라지는 대표 연구의 출력 개념도" caption="문헌 종합 개념도 · 각 연구의 보고 조건과 수치는 앞 결과 장에 제시." />

::takeaway::
문헌은 <strong>서로 다른 질문과 출력, 검증 조건</strong>을 채운다.

::source::
AGG-RL · SelectTSL · ELSA · Sci-Phi · ST-AudioLM · STAR-Bench/WearVox/SARL/BMLD의 문헌 종합.

<!--
[S77]
[Sources]
- https://proceedings.iclr.cc/paper_files/paper/2026/file/ee860a9fa65a55a335754c557a5211de-Paper-Conference.pdf
- https://arxiv.org/html/2510.05542v1
- https://arxiv.org/html/2606.14141v1
- https://arxiv.org/html/2510.24693v2
- https://arxiv.org/html/2601.02391v1
- https://arxiv.org/html/2606.05544v2
- https://arxiv.org/html/2606.14820v1
[청중 질문]
처음의 알람 문제를 이 발표는 실제로 어디까지 설명했는가?
[발표 노트]
S02 질문을 회수한다. 청중에게 ‘알람의 방향 숫자’와 ‘알람 뒤에 난 소리’의 출력 차이를 말해 보도록 한다. 대표 결과가 검증한 조건과 아직 미보고인 조건을 각각 하나씩 확인한다.
처음의 알람 방향 질문을 회수하고, 방향 숫자와 알람 뒤의 사건을 묻는 질문은 출력이 다름을 청중에게 확인한다. 각 행의 보고 조건 밖은 미보고로 남으며 실패와 동일하지 않다. 새 배열, 중첩·이동 음원, 자유 질문, 현장 녹음의 모든 조합을 하나의 모델이 해결했다는 결론을 내리지 않는다.
[해석 범위]
‘검증됨(조건 명시) / 미보고 / 해당 없음’을 사용한다. 이기지 못한 모델로 단순 색칠하지 않는다. 서로 다른 배열·데이터·판독을 한 성능선으로 연결하지 않는다. 그림은 문헌 종합이며 새 실험 데이터가 아니다.
[시각화 전 상세 본문 — 발표 설명용 보존]
질문·대표 연구 | 출력 | 확인한 조건 | 
어디에 소리가 있나? · AGG-RL | 방향 후보별 응답 | 선택한 합성 배열·격자 | 
알람만 어디에 있나? · SelectTSL | 목표 DOA·활성 수 | 요청 목표의 합성 장면 | 
어느 문장과 맞나? · ELSA | 공간 문장 선택 | 합성·실녹음 차이 유지 | 
음원별 속성은? · Sci-Phi | 음원별 장면 기술 | 같은 RIR 조건의 TupleScore | 
시간에 따라 무엇이 바뀌나? · ST-AudioLM | 시간·움직임 QA | 정적·동적 과제별 점수 | 
답의 근거는? · 네 평가 연구 | 답·판독·자극 반응 | 각각 다른 모델·입력·측정 | 


[핵심 결론]
문헌은 서로 다른 질문과 출력, 검증 조건을 채운다.
[전환]
연구 설계에서 다음에 요구할 증거를 세 질문으로 정리하고 마친다.
-->


---
layout: seminar
variant: figure
---

# 관측·출력·근거를 함께 확인한다

::body::
<PaperFigure src="/diagrams/p3-observation-output-evidence.svg" alt="두 마이크로 관측한 공간 장면, 방위와 고도와 거리를 명시한 위치 출력, 같은 질문에서 방 조건을 바꾸는 근거 비교를 연결한 결론 그림" caption="세 관점을 연결한 발표자 재구성." />

::takeaway::
새 음원·방·배열·질문 조합·실측 조건은 <strong>각각 다른 전이 축</strong>이다.

::source::
이 발표의 문헌 종합. 토의에서는 원하는 출력과 평가 조건을 먼저 지정한다.

<!--
[S78]
[Sources]
- https://arxiv.org/html/2510.24693v2
- https://arxiv.org/html/2601.02391v1
- https://arxiv.org/html/2606.05544v2
- https://arxiv.org/html/2606.14820v1
[청중 질문]
다음 공간 오디오 논문을 읽거나 설계할 때 무엇부터 확인해야 하는가?
[발표 노트]
위치 판독, 목표 선택, 장면·시간 판단에서 확인한 성과를 인정한다. 이어 일반화와 청각 단서의 근거가 과제마다 다르게 남는다고 정리한다. 더 큰 모델이나 특정 새 구조가 반드시 정답이라는 결론으로 넘어가지 않는다.
위치 판독, 목표 선택, 장면과 시간 판단에서 보고한 성과를 각각 인정한다. 인간 같은 위상 처리를 모든 과제 성공의 필요조건으로 요구하지 않으며, 관측된 실패에서 정보 부재를 단정하지 않는다. 더 큰 모델이나 새 구조가 반드시 정답이라는 결론 대신, 어떤 비교가 다음 주장을 지지할지 토의한다.
[해석 범위]
인간 같은 위상 처리를 모든 과제 성공의 필요조건으로 요구하지 않는다. 관측된 실패에서 정보 부재를 단정하지 않는다. 기존 연구 가설과 네 실험 제안은 문헌 결과와 분리된 토의 부록으로 보존한다.
[시각화 전 상세 본문 — 발표 설명용 보존]
관측무엇을 입력받았는가?

출력정확히 어떤 질문에 답했는가?

근거어떤 비교가 그 주장을 지지하는가?


[핵심 결론]
새 음원·방·배열·질문 조합·실측 조건은 각각 다른 전이 축이다.
[전환]
Q&A에서 원하는 출력·평가 조건을 지정받아 해당 원문 결과나 부록으로 돌아간다. 새로운 논문 목록으로 발표를 다시 시작하지 않는다.
-->
