---
theme: default
title: '공간 오디오 이해: 학술 발표 디자인 시편'
description: 학술 발표 디자인 시스템의 10개 대표 화면
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

# 공간 오디오 이해

::identity::
<img src="/iiplab-logo.png" alt="서강대학교 IIP Lab" />

::subtitle::
공간 표현 학습과 추론 모델의 연구 동향

::source::
공간 단서의 기초, 음원 위치 추정 및 표현 평가

<!--
[Sources]
- Logo: https://iip.sogang.ac.kr/layouts/iiplab/top-logo.png
[시편]
표지 기본형. 실제 78장 개정본이 아닌 디자인 시스템의 대표 화면이다.
-->

---
layout: seminar
variant: focus
---

# 마이크 위치가 바뀌면 소리는 어떻게 달라질까?

::body::
<PaperFigure src="/research/locata-dicit.svg" alt="LOCATA DICIT 배열의 마이크 위치와 로컬 좌표계" caption="DICIT 배열은 서로 다른 간격의 선형 부분 배열을 포함한다." />

::aside::
<div class="seminar-definition"><span class="seminar-label semantic-input">소리에서 바뀌는 것</span><p>마이크의 위치와 간격에 따라 채널 사이의 시간차가 달라진다.</p></div>
<div class="seminar-definition"><span class="seminar-label semantic-geometry">함께 알려줘야 하는 것</span><p>마이크가 놓인 위치와 배열의 기준 좌표다.</p></div>

::takeaway::
같은 방향의 소리도 **마이크 배치**가 바뀌면 채널 사이의 시간차가 달라진다.

::source::
Evers et al., The LOCATA Challenge, IEEE/ACM TASLP 28, 2020, Fig. 1(b).

<!--
[Sources]
- https://doi.org/10.1109/TASLP.2020.2990485
[발표 노트]
DICIT 배열의 로컬 좌표축과 서로 다른 마이크 간격을 먼저 읽는다. 이 그림은 배열 기하의 한 예이며, 모든 배열을 대표하지 않는다.
-->

---
layout: seminar
variant: focus
---

# 시간차는 위상차 그래프에서 어떻게 보일까?

::body::
<ManimScene
  src="/animations/tdoa-ipd-wrap.mp4"
  webm="/animations/tdoa-ipd-wrap.webm"
  poster="/animations/tdoa-ipd-wrap-start.png"
  print-poster="/animations/tdoa-ipd-wrap-poster.png"
  description="두 마이크의 경로 차이가 시간차가 되고, 같은 추적값이 위상 원과 주파수별 위상차 그래프를 함께 움직이는 설명용 애니메이션"
/>

::takeaway::
위상차는 **+π에 닿으면 −π에서 다시 이어진다.**

::source::
Baek et al., AGG-RL, ICLR 2026, Fig. 1(a–b) 기반 설명용 재구성.

<!--
[Sources]
- https://proceedings.iclr.cc/paper_files/paper/2026/file/ee860a9fa65a55a335754c557a5211de-Paper-Conference.pdf
[발표 노트]
애니메이션은 단일 직접음과 한 마이크 쌍을 가정한 설명용 재구성이다. 경로 차이에서 시간차를 얻고, τ=0.5 ms를 고정한 채 주파수를 올린다. 하나의 추적값이 위상 원의 벡터와 그래프의 점을 함께 움직이므로 +π에서 −π로 넘어가는 순간을 대응해 읽는다. 단일 주파수의 모호성은 다음 원문 그림에서 설명한다.
-->

---
layout: seminar
variant: figure
---

# 왜 한 주파수의 위상차만으로는 부족할까?

::body::
<PaperFigure src="/research/agg-rl-fig1.svg" alt="AGG Fig. 1. 두 마이크의 도달 시간차와 지연 0.5 ms에서 발생하는 채널 간 위상차 래핑" caption="왼쪽: 도달 시간차(TDoA). 오른쪽: τ = 0.5 ms에서 주파수에 따른 채널 간 위상차(IPD)." />

::takeaway::
**한 주파수에서 잰 위상차**만으로는 시간차를 하나로 정할 수 없다.

::source::
Baek et al., AGG-RL, ICLR 2026, Fig. 1(a–b).

<!--
[Sources]
- https://proceedings.iclr.cc/paper_files/paper/2026/file/ee860a9fa65a55a335754c557a5211de-Paper-Conference.pdf
[발표 노트]
왼쪽 음원과 마이크, 경로 차이, 시간차를 먼저 읽고 오른쪽 IPD 그래프로 이동한다. τ=0.5 ms와 ±π 경계를 짚는다. 위상 래핑은 위상값을 한 주기 안에 표현하면서 생기는 불연속이다. 단일 주파수의 모호성을 광대역 입력 전체의 정보 부재로 확대하지 않는다. 단일 쌍만으로 3D 방향이 유일하다고 주장하지 않는다. 출판본 2쪽에서 추출한 원본 벡터다. Fig. 1의 물리적 문제와 Fig. 2 구조도를 구별한다.
-->

---
layout: seminar
variant: method
---

# Neural-SRP는 마이크 쌍을 어떻게 합칠까?

::body::
<PaperFigure src="/research/neural-srp-architecture.svg" alt="Neural-SRP Fig. 3. 위상 특징과 마이크 좌표 및 방 크기를 결합해 고정 격자 응답을 예측하는 구조" />

::aside::
<section><span class="seminar-label semantic-input">모델이 받는 값</span><p>마이크 쌍의 STFT 위상<br/>마이크 좌표와 방 크기</p></section>
<section><span class="seminar-label semantic-result">위치를 찾는 과정</span><p>각 마이크 쌍이 만든 위치 응답을 더해 음원 위치를 고른다.</p></section>
<section><span class="seminar-label semantic-geometry">학습할 때만 쓰는 값</span><p>후보 위치 좌표로 정답 응답을 만든다.</p></section>

::takeaway::
마이크 좌표는 모델이 직접 보고, **후보 위치 좌표는 학습용 정답**을 만드는 데 쓴다.

::source::
Grinstein et al., Neural-SRP, arXiv:2403.09455v1, Fig. 3. CC BY 4.0.

<!--
[Sources]
- https://arxiv.org/html/2403.09455v1#S4
- https://arxiv.org/html/2403.09455v1/neural-srp-architecture.svg
[발표 노트]
그림의 위쪽 위상 입력부터 따라간다. 원본 비율을 보존하고 오른쪽 설명과 분리한다.
-->

---
layout: seminar
variant: result
---

# 처음 보는 채널 수에서도 AGG가 도움이 될까?

::body::
<table class="seminar-results">
<caption>Dynamic-U: 학습 4–12채널, 평가 13–16채널</caption>
<colgroup><col style="width:48%"/><col style="width:26%"/><col style="width:26%"/></colgroup>
<thead><tr><th scope="col">Neural-SRP</th><th scope="col">MAE (°)<br/>낮을수록 좋음</th><th scope="col">ACC₁₀ (%)<br/>높을수록 좋음</th></tr></thead>
<tbody>
<tr><td>기본 모델</td><td>21.18</td><td>45.51</td></tr>
<tr class="is-emphasis"><td>AGG 적용</td><td>19.05</td><td>54.13</td></tr>
</tbody>
</table>

::aside::
<section><span class="seminar-label semantic-input">무엇을 비교했나</span><p>Neural-SRP 기본 모델과 AGG 표현을 넣은 모델을 비교했다.</p></section>
<section><span class="seminar-label semantic-geometry">어떤 장면에서 시험했나</span><p>정지한 음성 음원이 최대 2개인 합성 장면이다.</p></section>
<section><span class="seminar-label semantic-negative">주의할 점</span><p>Dynamic-S에서는 AGG를 넣어도 성능이 좋아지지 않았다.</p></section>

::takeaway::
**학습 때보다 채널이 많은 Dynamic-U**에서는 AGG를 넣은 모델의 오차가 줄었다.

::source::
Baek et al., AGG-RL, ICLR 2026, Table 3, Neural-SRP without/with AGG. 원문 수치 재구성.

<!--
[Sources]
- https://proceedings.iclr.cc/paper_files/paper/2026/file/ee860a9fa65a55a335754c557a5211de-Paper-Conference.pdf
- Repository evidence: plans/EVIDENCE_P01_P11.md, P02, Table 3
[발표 노트]
수정 가능한 HTML 표다. 원문 전체 테이블의 단일 비교만 옮겼다. Dynamic은 음원 이동이 아니라 배열 조건을 뜻한다. 전체 제안 모델의 점수나 Dynamic-S 점수와 섞지 않는다.
-->

---
layout: seminar
variant: compare
---

# 인코더를 고정하면 무엇을 학습하는가?

::body::
<table class="seminar-comparison">
<colgroup><col style="width:20%"/><col style="width:18%"/><col style="width:27%"/><col style="width:35%"/></colgroup>
<thead><tr><th scope="col">평가 방식</th><th scope="col">인코더</th><th scope="col">추가 학습</th><th scope="col">평가 대상</th></tr></thead>
<tbody>
<tr><td>선형 판독</td><td>고정</td><td>선형층</td><td>선형 판독 성능</td></tr>
<tr><td>MLP 판독</td><td>고정</td><td>비선형 판독기</td><td>비선형 판독 성능</td></tr>
<tr><td>전체 미세조정</td><td>업데이트</td><td>인코더와 과제 헤드</td><td>적응 후의 과제 성능</td></tr>
<tr><td>LLM 연결</td><td>방법별 상이</td><td>프로젝터, LoRA 등</td><td>명시한 조건의 시스템 성능</td></tr>
</tbody>
</table>

::takeaway::
인코더를 그대로 두어도 **판독기는 과제의 정답으로 새로 학습**한다.

::source::
인코더 업데이트 범위와 판독기 학습에 따른 평가 구분.

<!--
[발표 노트]
같은 입력과 레이블 조건을 전제로 판독기와 업데이트 범위의 차이를 설명한다. frozen encoder와 zero-shot을 동일시하지 않는다. 이 표는 평가 프로토콜을 구분하며 논문 간 성능 순위를 제시하지 않는다.
-->

---
layout: seminar-section
---

# 표현에 정보가 있다는 걸<br/>어떻게 확인할까?

::context::
공간 표현의 진단 평가

::bridge::
표현에서 정보를 꺼내는 실험과<br/>소리 단서를 바꿨을 때의 반응을 따로 살펴본다.

<!--
[발표 노트]
방법 목록을 반복하는 목차 대신 다음에 검증할 질문으로 전환한다.
-->

---
layout: seminar
variant: figure
---

# SARL은 표현에서 어떤 정보를 꺼내 보는가?

::body::
<PaperFigure src="/research/sarl-summary.svg" alt="SARL Fig. 2. 각 모델의 음원 의미, 위치, 방 특성에 대한 선형 판독 성능을 무작위 기준으로 정규화한 그래프" caption="단일 음원 합성 장면. 고정 인코더, 시간 평균 풀링, 과제 레이블로 지도학습한 선형 판독기." />

::takeaway::
선형 판독 점수가 낮아도 **그 정보가 표현에 전혀 없다고 단정할 수는 없다.**

::source::
Chen et al., SARL, arXiv:2606.05544v2, Fig. 2. CC BY 4.0.

<!--
[Sources]
- https://arxiv.org/html/2606.05544v2
- https://arxiv.org/html/2606.05544v2/fig2.svg
[발표 노트]
정규화 축과 세 마커를 먼저 읽는다. Semantic, Localization, Room을 서로 구별한다. 낮은 선형 접근성이 정보가 완전히 없다는 뜻은 아니다. BMLD의 GRAM-T와 동일 체크포인트라고 가정하지 않는다.
-->

---
layout: seminar
variant: closing
---

# 모델의 결과를 어디까지 믿을 수 있을까?

::body::
<dl class="seminar-claims">
<div><dt>모델이 본 것</dt><dd>실제로 넣어 준 값과 학습할 때만 쓴 정보를 구분한다.</dd></div>
<div><dt>모델이 맞힌 것</dt><dd>방향, 사건, 공간 관계와 움직임 가운데 무엇을 출력했는지 확인한다.</dd></div>
<div><dt>시험한 조건</dt><dd>어떤 데이터와 소리 단서에서 얻은 결과인지 확인한다.</dd></div>
</dl>

::takeaway::
점수만 보지 말고 **모델이 본 것과 시험한 조건**을 함께 확인해야 한다.

::source::
선택 문헌에 적용한 공통 평가 기준.

<!--
[시편]
종합 화면 기본형. 27편의 전체 문헌 흐름은 NARRATIVE_PLAN.md와 BLUEPRINT_PART1–3.md에 따로 보존한다. 전체 공간 오디오 연구에 대한 완전한 분류를 주장하지 않는다.
-->
