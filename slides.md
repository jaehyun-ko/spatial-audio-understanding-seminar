---
theme: default
title: 공간 오디오 연구 계보
description: 배열 변화에 대한 공간 표현의 일반화와 검증을 다루는 문헌 세미나
presenter: IIP Lab
aspectRatio: 16/9
canvasWidth: 1280
colorSchema: light
transition: none
mdc: true
routerMode: hash
class: cover-slide ref-cover academic-slide
drawings:
  persist: false
---

<img src="/iiplab-logo.png" class="cover-logo" />

<div class="reference-cover-copy">
  <div class="cover-eyebrow">IIP LAB · SOGANG UNIVERSITY</div>
  <h1>공간 오디오<br/>연구 계보</h1>
  <h2>배열이 바뀌어도<br/>공간 단서를 읽을 수 있는가</h2>
  <p>2023–2026 대표 문헌 세미나</p>
</div>



<!--
[Sources]
- Logo: https://iip.sogang.ac.kr/layouts/iiplab/top-logo.png — IIP Lab identity asset, scaled only.

[발표 노트]
이 발표는 공간 오디오 연구의 대표 방법을 비교하는 문헌 세미나다. 중심 질문은 새로운 마이크 배열에서도 공간 단서를 일관되게 해석할 수 있는지이다. 마지막의 구조와 실험은 검증 전 연구 제안임을 먼저 밝힌다.
-->

---
layout: default
class: tone-overview academic-slide opening-question
---

## 배열이 바뀌어도<br/>방향을 읽을 수 있을까?

<div class="scenario-columns">
<div><small>달라지는 관측</small><h3>채널 사이의 지연</h3><p>마이크 배치가 바뀌면<br/>위상차도 달라진다.</p></div>
<div><small>유지할 공간 의미</small><h3>같은 음원의 방향</h3><p>같은 좌표계에서는<br/>같은 방향을 가리켜야 한다.</p></div>
</div>
<div class="note">사고실험: 음원과 배열 중심을 고정한 원거리 단일 음원</div>

<!--
[발표 노트]
사고실험에서 음원 위치와 배열 중심, 세계 좌표계는 고정한다. 마이크 배치만 바뀌므로 파형의 채널 관계는 변하지만 기대하는 세계 좌표계 방향은 같다. 서로 다른 관측을 같은 공간 의미로 읽는 문제를 제기한다.

[상세 설명]
## 배열을 바꾼 뒤에도 같은 음원의 방향을 읽을 수 있을까

 같은 방, 같은 음원 위치를 두고 마이크의 배치만 바꾸는 상황을 생각해 보자. 
 
 조건 관측 신호 기대하는 출력 
 
 학습에 사용한 배열 기준 마이크 배치의 다채널 파형 정해 둔 좌표계의 음원 방향 
 처음 보는 배열 채널 간 지연과 위상차가 달라짐 같은 좌표계에서 같은 음원 방향 
 
 관측 단서가 달라져도, 배열 기하에 맞춰 방향을 해석하는 표현 을 배웠는가? 
 설명을 위한 사고실험이다. 음원과 배열 중심을 고정하고, 원거리 단일 음원을 가정한다.
-->

---
layout: default
class: tone-overview academic-slide 
---

## 오늘의 질문

<div class="academic-questions">
<div><b>방향 계산</b><span>위상차를 어떻게 방향으로 바꾸는가?</span></div>
<div><b>표현 재사용</b><span>다른 과제에서도 공간 정보를 읽을 수 있는가?</span></div>
<div><b>표현 검증</b><span>성능이 좋아졌다면, 무엇을 배운 것인가?</span></div>
</div>
<div class="academic-takeaway">논문 비교 기준: <b>입력 · 학습 · 출력 · 적응 · 평가</b></div>
<div class="note">2023–2026년 대표 문헌과 후속 연구 제안</div>

<!--
[발표 노트]
먼저 지연과 방향의 관계를 설명하고, 위치 추정·표현 학습·언어 모델을 살펴본다. 발표의 설명 순서는 기술이 차례로 대체되었다는 역사적 주장이 아니다. 비교축은 입력, 학습, 출력, 적응, 평가의 다섯 가지다.

[상세 설명]
## 발표의 질문과 비교 범위

 
 1. 방향 계산 마이크 사이의 위상차를 어떻게 방향으로 바꾸는가? 
 2. 표현의 재사용 위치 추정 외의 과제와 언어 모델에서도 공간 정보를 읽을 수 있는가? 
 3. 검증의 범위 관측한 성능이 표현 자체에 대해 무엇을 입증하는가? 
 
 논문마다 입력, 학습, 출력, 적응, 평가 를 같은 기준으로 읽는다. 
 대표 문헌을 선택한 세미나다. 직접적인 인용 계보나 전 분야의 체계적 문헌고찰을 주장하지 않는다. 마지막에는 검증할 연구 가설과 실험 계획을 제안한다.
-->

---
layout: default
class: tone-signal academic-slide 
---

## 위상차가 방향이 되기까지

<div class="signal-chain">
<div class="signal-stage"><small>입력</small><b>파형</b><span>x₁(t), x₂(t), …</span></div><div class="chain-arrow">→</div>
<div class="signal-stage"><small>채널 비교</small><b>교차 스펙트럼</b><span>Xᵢ(f)Xⱼ*(f)</span></div><div class="chain-arrow">→</div>
<div class="signal-stage"><small>상대 지연</small><b>IPD / TDoA</b><span>위상차 / 도달 시간차</span></div><div class="chain-arrow">→</div>
<div class="signal-stage"><small>기하 해석</small><b>DOA</b><span>음원의 도래 방향</span></div>
</div>
<div class="signal-summary">지연을 방향으로 바꾸려면 <b>마이크 좌표</b>가 필요하다.</div>
<div class="note">원거리 직접음 근사. 반사음과 잡음은 별도로 고려한다.</div>

<!--
[발표 노트]
다채널 신호를 주파수 영역에서 비교하면 상대 위상차를 얻는다. 직접음과 원거리 근사에서 지연을 배열 좌표와 연결해 DOA를 구한다. PHAT의 수식은 부록 B에 있다.

[상세 설명]
## 채널 간 지연과 배열 기하로 음원의 방향을 구한다

 
 01 · 수집 파형 x₁(t), x₂(t), … 
 → 
 02 · 비교 교차 스펙트럼 Xᵢ(f)Xⱼ*(f) 
 → 
 03 · 정렬 IPD / TDoA 채널 사이 상대 지연 
 → 
 04 · 방향 계산 DOA + 마이크 좌표 
 

 IPD 는 채널 간 위상차, TDoA 는 도달 시간차, DOA 는 음원의 도래 방향이다. 
 원거리 직접음 근사에서 지연과 마이크 좌표를 연결한다. 반사음과 잡음은 이 단서를 흐릴 수 있다.
-->

---
layout: default
class: tone-signal academic-slide 
---

## 두 채널의 방향 모호성

<div class="visual-split wide-copy">
<div class="visual-copy">
<div class="route-list">
<div class="route-item"><div class="route-no">배열</div><div><b>여러 쌍의 시간차</b><span>마이크 좌표와 여러 지연 제약을 함께 푼다.</span></div></div>
<div class="route-item"><div class="route-no">사람</div><div><b>방향별 스펙트럼</b><span>머리·귓바퀴의 여과 특성이 앞뒤와 고도 모호성을 줄인다.</span></div></div>
</div>
<div class="callout"><b>HRTF</b><br/>청자마다 다른 머리 관련 전달함수</div>
</div>
<div><div class="visual-media paper-figure"><img src="/research/princeton-hrtf-setup.png" /></div><div class="figure-caption">여러 방향에서 전달함수를 측정하는 3D3A 실험 장치</div></div>
</div>
<div class="source">Princeton 3D3A Lab · HRTF Database · CC BY 4.0</div>

<!--
[Sources]
- Figure/data: https://3d3a.princeton.edu/3d3a-lab/3d3a-hrtf-database — Princeton 3D3A HRTF Database, CC BY 4.0.

[발표 노트]
마이크 쌍 하나의 시간차는 하나의 공간 제약이다. 3차원 방향을 정하려면 추가 마이크 쌍이나 HRTF의 스펙트럼 단서 같은 정보가 필요하다. HRTF 차이와 배열 기하 차이는 각각 다른 일반화 조건이다.

[상세 설명]
## 두 채널에서 얻는 방향 정보와 모호성

 
 
 
 배열 여러 마이크 쌍과 좌표 여러 마이크 쌍에서 얻은 τᵢⱼ ≈ (mⱼ−mᵢ)ᵀu / c를 함께 풀어 방향 u를 찾는다. 
 사람 ITD · ILD와 HRTF 머리와 귓바퀴가 만드는 방향별 스펙트럼 단서가 앞뒤·고도 모호성을 줄인다. 
 
 HRTF 는 머리 관련 전달함수다. 방향별 여과 특성은 청자마다 다르다. 
 
 
 
 Princeton 3D3A Lab은 실제 머리 주변의 여러 방향에서 전달함수를 측정해 HRTF를 구축한다. 
 
 

 Princeton 3D3A Lab, 3D3A HRTF Database measurement setup, CC BY 4.0.
-->

---
layout: default
class: tone-local academic-slide section-break
---

## 위치 추정

<div class="section-index">01</div><div class="bridge-question">모델은 배열 기하를<br/>어떻게 반영할까?</div><div class="bridge-summary">마이크 배치가 달라지면 같은 방향의 위상차도 달라진다.</div>

<!--
[발표 노트]
앞 절에서 위상 단서를 방향으로 바꾸는 데 기하가 필요함을 보았다. 이제 모델 안에서 기하를 어디에 반영하는지 살핀다. 먼저 학습 목표가 서로 다른 위치 추정 방법을 비교한다.

[상세 설명]
## 새 배열에 맞는 방향 계산

 01 · 위치 추정 
 위상차는 마이크 사이의 상대 지연을 반영한다. 마이크 간격과 배치가 달라지면 같은 방향에서도 관측 단서가 달라진다. 
 모델은 마이크 좌표와 후보 방향 을 계산에 어떻게 반영하는가?
-->

---
layout: default
class: tone-local academic-slide 
---

## 학습하는 대상이 다르다

<div class="claim-list">
<div><b>GCC / SRP / MUSIC</b><span>상관과 공간 응답을 계산한다</span></div>
<div><b>IPDnet</b><span>직접음의 위상차를 추정한다</span></div>
<div><b>Neural-SRP</b><span>위치별 응답을 학습한다</span></div>
</div>
<div class="academic-takeaway">최종 방향이 같아도 <b>중간 표현</b>은 다르다.</div>
<div class="source">Knapp & Carter, 1976 · Wang et al., IPDnet, 2024 · Grinstein et al., Neural-SRP, 2024</div>

<!--
[Sources]
- Figure: https://arxiv.org/html/2403.09455v1/outputs.png — Grinstein et al., Neural-SRP, Fig. 1, CC BY 4.0.
- Claim: https://arxiv.org/abs/2405.07021 — Wang et al., IPDnet.

[발표 노트]
GCC는 시간차, SRP는 후보 위치별 합산 응답, MUSIC은 신호·잡음 부분공간 구조를 이용한다. IPDnet과 Neural-SRP도 학습 목표가 다르므로 최종 위치 오차만으로 내부 표현이 같다고 볼 수 없다.

[상세 설명]
## 위치 추정 방법마다 학습하는 대상이 다르다

 
 
 
 계열 계산·학습 대상 출력 
 
 GCC / SRP / MUSIC 상관·합산·부분공간 지연 / 공간 스펙트럼 
 IPDnet 직접음 IPD 음원별 DP-IPD 
 Neural-SRP SRP 보정 음원 위치 
 
 
 IPDnet은 직접음 위상차를 추정하고, Neural-SRP는 위치별 응답을 학습한다. 
 
 
 
 실제 녹음에서 NeuralSRP+(위)와 기존 SRP(아래)가 만든 공간 응답을 비교한다. 
 
 

 Grinstein et al., Neural-SRP, Fig. 1, arXiv:2403.09455v1, CC BY 4.0; IPDnet, arXiv:2405.07021.
-->

---
layout: default
class: tone-local academic-slide evidence-slide
---

## Neural-SRP · 쌍별 응답의 합산

<div class="evidence-layout">
<div class="evidence-figure"><img src="/research/neural-srp-architecture.svg" /></div>
<div class="evidence-comment"><h3>마이크 쌍마다</h3><p>위상 특징<br/>마이크 좌표<br/>방 크기</p><h3>고정 격자 예측</h3><p>쌍별 응답을 합산해<br/>음원의 위치를 찾는다.</p></div>
</div>
<div class="figure-caption">후보 좌표는 학습 목표를 만드는 데 사용한다. 추론 입력에는 넣지 않는다.</div>
<div class="source">Grinstein et al., Neural-SRP, Fig. 3, arXiv:2403.09455v1.</div>

<!--
[Sources]
- Figure: https://arxiv.org/html/2403.09455v1/neural-srp-architecture.svg — Grinstein et al., Neural-SRP, Fig. 3, CC BY 4.0.

[발표 노트]
Neural-SRP의 입력은 마이크 쌍의 STFT 위상과 쌍의 좌표, 방 크기다. 후보 위치는 학습 목표를 만들 때 사용하며 추론 입력이 아니다. 고정 격자를 예측하고 쌍별 출력을 합산한다. 다음 AGG-RL과 후보 격자의 취급을 비교한다.
- Primary: https://arxiv.org/html/2403.09455v1#S4

[상세 설명]
## Neural-SRP는 마이크 쌍별 공간장을 학습하고 합산한다

 
 
 
 설계 원칙 
 쌍별 위상 + 좌표 + 방 크기 
 마이크 쌍의 위상 특징과 메타데이터로 고정 위치 격자의 응답을 예측하고, 쌍별 결과를 합산한다. 
 
 
 Neural-SRP가 보존하는 구조 
 TDoA로 만든 쌍곡선 학습 목표와 마이크 쌍 합산 구조가 SRP의 물리적 가정을 반영한다. 후보 좌표는 추론 입력으로 넣지 않는다. 
 
 
 
 
 위상 특징을 추출한 뒤 좌표·방 크기와 결합한다. 쌍별 위치 격자를 합산해 음원을 찾는다. 
 
 

 Grinstein et al., Neural-SRP, Fig. 3, arXiv:2403.09455v1, CC BY 4.0.
-->

---
layout: default
class: tone-local academic-slide evidence-slide
---

## AGG-RL · 후보 방향도 입력한다

<div class="evidence-layout">
<div class="evidence-figure"><img src="/research/agg-rl-overall.png" /></div>
<div class="evidence-comment"><h3>세 가지 입력</h3><p>다채널 오디오<br/>마이크 좌표<br/>후보 DOA 격자</p><h3>공간 스펙트럼</h3><p>각 후보 방향에 대한<br/>응답을 계산한다.</p></div>
</div>

<div class="source">Baek et al., AGG-RL, ICLR 2026, Fig. 2.</div>

<!--
[Sources]
- Figure: https://github.com/BaekMS/Audio-Geometry-Grid_Representation-Learning — Baek et al., official AGG-RL project, Fig. 2.
- Rights note: https://iclr.cc/FAQ/Copyright — ICLR authors retain copyright; repository has no explicit figure license.

[발표 노트]
AGG-RL은 오디오, 배열 기하, 후보 DOA 격자를 모델에 함께 제공한다. LNuDFT와 상대 위치 인코딩은 구조 요소다. 새 배열·채널 수·격자에 관한 평가와 다른 후속 과제로의 재사용은 구별한다.
- Primary: https://proceedings.iclr.cc/paper_files/paper/2026/file/ee860a9fa65a55a335754c557a5211de-Paper-Conference.pdf

[상세 설명]
## AGG-RL은 배열과 후보 방향을 함께 조건으로 쓴다

 
 
 
 입력 다채널 파형 마이크 좌표 + 후보 DOA 격자 
 구조 학습 가능한 비균일 푸리에 변환(LNuDFT)과 상대 위치 인코딩 
 출력 후보 방향별 공간 스펙트럼 
 평가 새 기하 · 채널 수 · 격자 
 
 위치 추정을 위한 표현이다. 다른 과제에서의 재사용은 따로 평가한다. 
 
 
 
 AGG-RL은 오디오, 마이크 좌표, 후보 방향 격자를 하나의 모델에서 결합한다. 
 
 

 Baek et al., AGG-RL, ICLR 2026, Fig. 2 / official project. Repository has no explicit figure reuse license.
-->

---
layout: default
class: tone-local academic-slide 
---

## 배열 일반화의 세 축

<div class="claim-list">
<div><b>채널 수</b><span>마이크 2개에서 N개로</span></div>
<div><b>배열 배치</b><span>학습에 사용한 배치에서 새로운 배치로</span></div>
<div><b>후보 격자</b><span>고정된 방향 목록에서 새로운 방향 질의로</span></div>
</div>
<div class="academic-takeaway">세 조건을 <b>독립적으로</b> 바꿔 평가한다.</div>
<div class="source">Baek et al. · AGG-RL · ICLR 2026</div>

<!--
[Sources]
- Figure: https://raw.githubusercontent.com/BaekMS/Audio-Geometry-Grid_Representation-Learning/main/spectrum_plots/4ch_0.png — official AGG-RL project.

[발표 노트]
채널 수가 바뀌는 것, 같은 채널 수에서 배치가 바뀌는 것, 후보 방향의 샘플링이 바뀌는 것은 다른 실험이다. 이 절은 기하 조건부 위치 추정을 설명했다. 다음 절에서는 방향 출력 이외의 정보도 후속 과제에 쓰는 사전학습을 본다.

[상세 설명]
## 배열 일반화에는 채널 수, 배치, 후보 격자의 구분이 필요하다

 
 
 
 채널 수 마이크 2개 → N개 
 배열 기하 고정 배열 → 처음 보는 배열 
 후보 격자 고정 격자 → 자유로운 방향 질의 
 
 새 배열에서 위치 추정이 가능해도, 다른 과제에 쓸 공간 정보 가 표현에 남는지는 별도 질문이다. 
 
 
 
 4채널·2음원 장면에서 후보 방향마다 계산한 공간 스펙트럼. 
 
 

 Baek et al., AGG-RL official project, 4-channel / 2-speaker spectrum example; no explicit figure reuse license.
-->

---
layout: default
class: tone-repr academic-slide section-break
---

## 표현 학습

<div class="section-index">02</div><div class="bridge-question">위치 추정 외의 과제에도<br/>공간 정보를 쓸 수 있을까?</div><div class="bridge-summary">사전학습의 목표가 표현에 남는 정보를 결정한다.</div>

<!--
[발표 노트]
위치 추정과 표현 학습은 함께 존재하는 연구 목표다. 한 계열이 다른 계열을 대체했다고 설명하지 않는다. 대조 학습과 복원, 특징 증류, 마스킹의 목표를 비교한다.

[상세 설명]
## 여러 과제에서 재사용할 공간 표현

 02 · 표현 학습 
 위치 추정은 방향을 출력하도록 모델을 학습한다. 표현 학습은 사전학습한 인코더를 여러 후속 과제에서 사용하는 것을 목표로 한다. 
 어떤 사전학습 목표 가 어떤 공간 정보를 남기는가?
-->

---
layout: default
class: tone-repr academic-slide concept-compare
---

## 표현 학습의 두 목표

<div class="paper-compare concept-compare">
<div class="paper-side"><div class="paper-figure"><img src="/research/mc-simclr-overview.png" /></div><div class="concept-text"><h3>MC-SimCLR</h3><p><strong>같은 녹음의 시간 구간을 가깝게</strong><br/>정지 음원을 가정한 대조 학습</p></div></div>
<div class="paper-side"><div class="paper-figure"><img src="/research/ccsr-task.png" /></div><div class="concept-text"><h3>CCSR</h3><p><strong>관측하지 않은 채널을 복원</strong><br/>채널 간 관계를 배우는 복원 학습</p></div></div>
</div>
<div class="source">Jiang et al., MC-SimCLR, 2023, Fig. 1 · Yang & Li, CCSR, 2023, Fig. 1</div>

<!--
[Sources]
- Figure: https://arxiv.org/html/2309.15938v1/mc-simclr-wider.png — Jiang et al., MC-SimCLR, Fig. 1, CC BY 4.0.
- Figure: https://arxiv.org/html/2312.00476v2/meth_task.png — Yang & Li, CCSR, Fig. 1; arXiv non-exclusive license.

[발표 노트]
MC-SimCLR의 양성 쌍은 같은 녹음의 서로 다른 다채널 시간 구간이며 정지 음원을 가정한다. 임의의 단일 채널끼리 묶는 방식으로 설명하지 않는다. CCSR은 다른 채널의 신호를 복원한다.
- Primary: https://arxiv.org/html/2309.15938v1
- Primary: https://arxiv.org/html/2312.00476v2

[상세 설명]
## MC-SimCLR과 CCSR은 ‘무엇을 같게 볼지’를 다르게 정한다

 
 
 
 MC-SimCLR · 대조 학습 정지 음원을 가정한다. 같은 녹음의 두 다채널 시간 구간을 양성 쌍으로 사용한다. 소리 사건과 방위각 과제로 표현을 평가한다. 
 
 
 
 CCSR · 채널 복원 다른 채널을 복원하며 직접음·반사음·잔향을 설명하는 채널 간 관계를 배운다. 
 
 

 Jiang et al., MC-SimCLR, Fig. 1, arXiv:2309.15938v1, CC BY 4.0; Yang & Li, CCSR, Fig. 1, arXiv:2312.00476v2.
-->

---
layout: default
class: tone-repr academic-slide 
---

## SFD · 깨끗한 특징을 학습 목표로

<div class="visual-split wide-copy">
<div class="visual-copy">
<div class="paper-sheet">
<div class="paper-row"><b>목표</b><span>깨끗한 바이노럴 신호의<br/>공간 특징</span></div>
<div class="paper-row"><b>입력</b><span>잡음·잔향이 섞인 파형</span></div>
<div class="paper-row"><b>전이</b><span>DOA 과제에서<br/>전체 미세조정</span></div>
</div>
<div class="callout">성능 향상은 <b>사전학습의 유용성</b>을 보여준다.</div>
</div>
<div><div class="visual-media paper-figure"><img src="/research/sfd-framework.svg" /></div><div class="figure-caption">특징 증류 후 위치 추정에 적응하는 과정</div></div>
</div>
<div class="source">Bovbjerg et al. · SFD · arXiv:2508.20914 · Fig. 1</div>

<!--
[Sources]
- Figure: https://arxiv.org/html/2508.20914v1/neural_fe_and_finetune.drawio.svg — Bovbjerg et al., SFD, Fig. 1; arXiv non-exclusive / IEEE publication.

[발표 노트]
SFD의 네 목표는 각각 학습한 변형으로 비교한다. 깨끗한 특징을 목표로 잡음·잔향 입력을 사전학습한 뒤 DOA에서 전체 미세조정한다. 이 결과와 고정 인코더의 선형 위상 접근성은 다른 주장이다.
- Primary: https://arxiv.org/html/2508.20914v1

[상세 설명]
## SFD는 깨끗한 공간 특징을 사전학습 목표로 쓴다

 
 
 
 교사 깨끗한 바이노럴 신호의 GCC, GCC-PHAT, CPS 위상, ILD+IPD 중 한 목표 사용 
 학생 잡음과 잔향이 섞인 파형에서 같은 목표값 예측 
 전이 사전학습 뒤 DOA 헤드와 함께 전체 미세조정 
 
 전체 미세조정의 성능은 사전학습의 유용성 을 보여준다. 고정 표현의 접근성은 따로 측정한다. 
 
 
 
 Spatial Feature Distillation의 사전학습과 미세조정 흐름. 
 
 

 Bovbjerg et al., SFD, Fig. 1, arXiv:2508.20914v1. arXiv non-exclusive / IEEE rights; attribution shown.
-->

---
layout: default
class: tone-repr ref-gram academic-slide full-figure
---

## GRAM · 여러 과제에서 같은 표현 읽기

<div class="hero-figure"><img src="/research/gram-overview.png" /></div>
<div class="academic-takeaway"><b>공간 과제와 일반 오디오 과제</b>를 고정 인코더로 함께 평가한다.</div>
<div class="source">Yuksel et al. · GRAM · arXiv:2506.00934v5 · Fig. 1</div>

<!--
[Sources]
- Figure: https://arxiv.org/html/2506.00934v5/figure1.png — Yuksel et al., GRAM, Fig. 1, CC BY-NC-SA 4.0.
- Correct record: https://arxiv.org/abs/2506.00934 — current GRAM paper; 2602.03307 was withdrawn as an erroneous duplicate.

[발표 노트]
그림은 장면 생성, 사전학습, 공통 평가의 세 부분으로 읽는다. GRAM은 고정 특징의 여러 과제 평가가 중심이며 일부 전체 미세조정 비교도 있다. 표현 재사용을 확인해도 물리 개입의 일관성까지 자동으로 입증되는 것은 아니다.
- Primary: https://arxiv.org/html/2506.00934v5

[상세 설명]
## GRAM은 공간 과제와 일반 오디오 과제를 함께 평가한다

 
 여러 음원과 실내 음향으로 장면을 생성하고 다채널 마스킹 오토인코더를 학습한다. 고정 인코더의 특징으로 여러 후속 과제를 평가한다. 

 Yuksel et al., GRAM, Fig. 1, arXiv:2506.00934v5, CC BY-NC-SA 4.0.
-->

---
layout: default
class: tone-language academic-slide section-break
---

## 공간 언어 모델

<div class="section-index">03</div><div class="bridge-question">“오른쪽 뒤의 소리는<br/>무엇인가?”</div><div class="bridge-summary">언어로 답하려면 소리의 종류와 방향을 함께 읽어야 한다.</div>

<!--
[발표 노트]
질문 예시는 실제 모델 출력이나 성능 수치가 아닌 설명용 문장이다. 소리 종류와 방향을 동시에 읽는 판독기로 LLM을 도입한다. 판독기는 인코더의 특징에서 출력 정보를 추출하는 모듈이며, 전체 시스템 성능과 인코더 자체의 증거를 구분한다.

[상세 설명]
## 공간 표현을 언어로 읽는 방법

 03 · 공간 언어 모델 
 예를 들어 ‘오른쪽 뒤에서 들리는 소리는 무엇인가?’라는 질문에는 음원 종류와 방향을 함께 읽어야 한다. 
 인코더의 표현을 프로젝터와 LLM 에 연결하면, 어떤 공간 질문에 답할 수 있는가?
-->

---
layout: default
class: tone-language ref-bat academic-slide full-figure
---

## BAT · 바이노럴 표현을 LLM에 연결

<div class="hero-figure"><img src="/research/bat-architecture.png" /></div>
<div class="academic-takeaway">Spatial-AST의 표현을 <b>프로젝터</b>로 LLM 토큰에 연결한다.</div>
<div class="source">Zheng et al. · BAT · arXiv:2402.01591v4 · Fig. 1</div>

<!--
[Sources]
- Figure: https://arxiv.org/html/2402.01591v4/architecture.png — Zheng et al., BAT, Fig. 1, CC BY 4.0.

[발표 노트]
왼쪽의 바이노럴 인코더, 중간의 프로젝터, 오른쪽의 LLM 순서로 설명한다. 답변 성능에는 데이터 생성과 프로젝터, LLM 적응도 기여한다. 다음에는 위치 추정 인코더를 공간 토큰으로 재사용하는 PhaseCoder를 비교한다.

[상세 설명]
## BAT은 바이노럴 표현을 LLM의 입력 토큰에 연결한다

 
 Spatial-AST는 바이노럴 오디오를 인코딩하고, 프로젝터는 이를 LLaMA 토큰 공간에 잇는다. 오른쪽은 SoundSpaces로 바이노럴 오디오를 만드는 과정이다. 

 Zheng et al., BAT, Fig. 1, arXiv:2402.01591v4, CC BY 4.0.
-->

---
layout: default
class: tone-language ref-phasecoder academic-slide full-figure
---

## PhaseCoder · 위치 표현을 공간 토큰으로

<div class="hero-figure"><img src="/research/phasecoder-architecture.png" /></div>
<div class="academic-takeaway"><b>공간 토큰과 모노 오디오 토큰</b>을 함께 LLM에 입력한다.</div>
<div class="source">Dementyev et al. · PhaseCoder · arXiv:2601.21124v2 · Fig. 3</div>

<!--
[Sources]
- Figure: https://arxiv.org/html/2601.21124v2/model_architecture_v2.png — Dementyev et al., PhaseCoder, Fig. 3, CC BY 4.0.

[발표 노트]
왼쪽은 기하를 조건으로 한 PhaseCoder 학습, 오른쪽은 공간 토큰과 모노 오디오 토큰을 LLM에 결합하는 과정이다. 공간 토큰이 무엇을 추가하는지와 새 배열에서의 평가 조건을 중심으로 읽는다.

[상세 설명]
## PhaseCoder는 위치 추정 인코더를 공간 토큰 생성기로 쓴다

 
 왼쪽은 마이크 배열 기하를 조건으로 PhaseCoder를 학습하는 과정이다. 오른쪽은 공간 토큰과 기존 모노 오디오 토큰을 Gemma 3n에 함께 넣는 과정이다. 

 Dementyev et al., PhaseCoder, Fig. 3, arXiv:2601.21124v2, CC BY 4.0.
-->

---
layout: default
class: tone-language academic-slide 
---

## 질문에 따라 입력과 출력이 달라진다

<table class="academic-table">
<thead><tr><th>과제</th><th>대표 모델</th><th>읽어내는 정보</th></tr></thead><tbody>
<tr><td>정적 장면</td><td>BAT · DSpAST</td><td>음원 종류 · 방향 · 거리</td></tr>
<tr><td>움직임</td><td>ST-AudioLM</td><td>소리 사건과 시간별 궤적</td></tr>
<tr><td>여러 공간 과제</td><td>OWL · Spatial-Omni</td><td>위치와 공간 관계에 대한 응답</td></tr>
</tbody></table>
<div class="academic-takeaway">바이노럴과 FOA, 서로 다른 평가셋의 점수는 <b>같은 순위로 비교할 수 없다.</b></div>
<div class="source">ST-AudioLM, arXiv:2606.14141 · Spatial-Omni, arXiv:2606.10738 · OWL, ICLR 2026</div>

<!--
[Sources]
- Claim: https://arxiv.org/abs/2606.14141 — Oh et al., ST-AudioLM.
- Claim: https://arxiv.org/abs/2606.10738 — Zhu et al., Spatial-Omni.
- Claim: https://arxiv.org/abs/2509.26140 — Biswas et al., OWL.

[발표 노트]
이 표의 열은 시계열 발전 단계가 아니라 과제의 차이다. FOA는 바이노럴과 다른 공간 표현 형식이다. DSpAST는 사건·방향·거리, OWL은 학습 시 기하 지도 정보를 사용한다. 서로 다른 평가셋의 점수를 단순 순위로 만들지 않는다.

[상세 설명]
## 공간 언어 모델의 입력과 출력 과제

 
 정적 질의 BAT · DSpAST 바이노럴 장면에서 음원 종류·방향·거리를 묻는다. 
 움직임 ST-AudioLM 1차 앰비소닉스(FOA) 장면에서 소리 사건과 시간별 궤적 토큰을 함께 예측한다. 
 통합 과제 OWL · Spatial-Omni OWL은 바이노럴 입력과 학습 시 기하 지도를 사용한다. Spatial-Omni는 FOA 인코더를 쓴다. 
 

 과제와 입력이 다르므로 서로 다른 평가셋의 정답률을 같은 순위로 비교할 수 없다. 

 ST-AudioLM, arXiv:2606.14141; Spatial-Omni, arXiv:2606.10738; OWL, ICLR 2026.
-->

---
layout: default
class: tone-eval academic-slide section-break
---

## 표현의 검증

<div class="section-index">04</div><div class="bridge-question">성능이 좋아졌다면,<br/>무엇을 배운 것일까?</div><div class="bridge-summary">인코더, 판독기, 추가 학습의 기여를 구분해야 한다.</div>

<!--
[발표 노트]
방법의 출력이 좋아졌을 때 무엇이 좋아졌는지 분리하는 평가로 전환한다. 인코더를 고정한 탐침과 통제된 입력 개입은 서로 다른 가설을 검증한다.

[상세 설명]
## 성능이 좋아진 이유를 구분하는 평가

 04 · 표현의 검증 
 후속 과제의 점수에는 인코더, 판독기, 추가 학습 데이터가 함께 영향을 준다. 
 인코더를 고정하고 입력 단서를 통제 하면, 표현에 대해 무엇을 확인할 수 있는가?
-->

---
layout: default
class: tone-eval academic-slide 
---

## 인코더 적응과 판독기 용량

<table class="academic-table">
<thead><tr><th>평가 방식</th><th>인코더</th><th>확인하는 것</th></tr></thead><tbody>
<tr><td>선형 탐침</td><td>고정</td><td>선형으로 읽히는 정보</td></tr>
<tr><td>소형 MLP</td><td>고정</td><td>비선형으로 읽히는 정보</td></tr>
<tr><td>전체 미세조정</td><td>업데이트</td><td>과제 적응 후의 성능</td></tr>
<tr><td>LLM 연결</td><td>방법별 상이</td><td>해당 학습 조건의 시스템 성능</td></tr>
</tbody></table>
<div class="academic-takeaway"><b>무엇을 고정하고 무엇을 학습했는가?</b></div>
<div class="source">인코더 고정의 사례: OWL, arXiv:2509.26140v1, §5</div>

<!--
[Sources]
- https://arxiv.org/html/2509.26140v1

[발표 노트]
선형 탐침과 작은 MLP는 고정 인코더의 정보 접근성을 서로 다른 용량에서 측정한다. 전체 미세조정은 인코더를 바꾼다. LLM 연결은 인코더 고정 여부가 방법마다 다르므로 일렬의 적응량 사다리로 놓지 않는다.

[상세 설명]
## 인코더 적응과 판독기 용량은 별도로 비교한다

 
 평가 방식 인코더 판독기·추가 학습 해석할 수 있는 범위 
 
 선형 탐침 고정 선형층 학습 기존 특징의 선형 접근성 
 소형 MLP 고정 비선형 판독기 학습 정해 둔 용량에서의 접근성 
 전체 미세조정 업데이트 헤드와 인코더 학습 과제에 적응한 전체 모델 성능 
 LLM 연결 방법별 상이 프로젝터·LoRA 등 명시한 적응 조건의 시스템 성능 
 
 LLM을 연결해도 인코더를 고정할 수 있다. 학습한 모듈과 데이터량 을 함께 기록한다. 
 사례: OWL, arXiv:2509.26140v1, §5 (SAGE 고정, 프로젝터·LoRA 적응).
-->

---
layout: default
class: tone-eval academic-slide 
---

## 학습에서 무엇을 제외했는가

<div class="visual-split wide-copy">
<div class="visual-copy"><div class="route-list">
<div class="route-item"><div class="route-no">01</div><div><b>콘텐츠</b><span>화자 · 클립 · 소리 종류</span></div></div>
<div class="route-item"><div class="route-no">02</div><div><b>음향 환경</b><span>HRTF 청자 · 방 · 충격응답</span></div></div>
<div class="route-item"><div class="route-no">03</div><div><b>센서</b><span>배열 배치 · 채널 수 · 장치</span></div></div>
<div class="route-item"><div class="route-no">04</div><div><b>녹음 조건</b><span>시뮬레이션 · 실제 녹음</span></div></div>
</div></div>
<div><div class="visual-media paper-figure"><img src="/research/owl-bidepth.png" /></div><div class="figure-caption">BiDepth의 기하 정보와 바이노럴 장면 생성</div></div>
</div>
<div class="source">Biswas et al. · OWL / BiDepth · arXiv:2509.26140v1 · Fig. 2</div>

<!--
[Sources]
- Figure: https://arxiv.org/html/2509.26140v1/figure/simulation_setup_2.png — Biswas et al., OWL, Fig. 2, CC BY 4.0.

[발표 노트]
무엇을 학습에서 배제했는지 구체적으로 말해야 일반화 주장에 범위가 생긴다. 화자만 새롭고 HRTF·방·배열이 같다면 이들 조건의 일반화를 입증하지 못한다. 그림은 BiDepth의 데이터 생성 사례이며 모든 평가셋의 구조를 대표하지 않는다.

[상세 설명]
## 학습에 쓰지 않은 조건을 명시해야 일반화를 해석할 수 있다

 
 
 
 01 콘텐츠 화자 · 클립 · 소리 종류 
 02 음향 환경 HRTF 청자 · 방 · RIR/BRIR 
 03 센서 배열 기하 · 장치 · 채널 수 
 04 현실 조건 시뮬레이션 → 실제 녹음 · 이동 
 
 
 
 
 BiDepth는 깊이 파노라마와 바이노럴 시뮬레이션을 결합해, 기하 정보를 지도 신호로 쓰는 장면을 만든다. 
 
 

 Biswas et al., OWL / BiDepth, Fig. 2, arXiv:2509.26140v1, CC BY 4.0.
-->

---
layout: default
class: tone-eval ref-sarl academic-slide evidence-slide
---

## SARL · 음원과 방 정보의 접근성

<div class="evidence-layout">
<div class="evidence-figure"><img src="/research/sarl-summary.svg" /></div>
<div class="evidence-comment"><h3>음원 요인의<br/>점수가 더 높다</h3><p>고정 인코더<br/>선형 탐침<br/>단일 음원 합성 장면</p><p>방 정보의 완전한 부재를 뜻하지는 않는다.</p></div>
</div>
<div class="figure-caption">무작위 기준으로 정규화한 점수. 음원 종류·위치와 방 요인을 비교한다.</div>
<div class="source">Chen et al. · SARL · arXiv:2606.05544v2 · Fig. 2</div>

<!--
[Sources]
- Figure: https://arxiv.org/html/2606.05544v2/fig2.svg — Chen et al., SARL, Fig. 2, CC BY 4.0.
- Figure: https://arxiv.org/html/2606.05544v2/fig3.svg — Chen et al., SARL, Fig. 3, CC BY 4.0.

[발표 노트]
SARL의 핵심 결과는 평가한 인코더에서 음원 요인이 방 요인보다 선형으로 잘 읽힌다는 것이다. 단일 음원 합성 분포, 시간 평균 풀링, 선형 탐침과 무작위 기준 정규화 조건을 명시한다. 큰 표현 민감도가 높은 판독 점수를 항상 뜻하지는 않는다.
- Primary: https://arxiv.org/html/2606.05544v2

[상세 설명]
## SARL의 고정 표현에서는 음원 요인이 방 요인보다 잘 읽힌다

 
 
 
 고정 인코더와 선형 탐침. 음원 종류·위치와 방 요인의 무작위 기준 정규화 점수를 비교한다. 
 
 
 
 요인을 통제해 바꾼 뒤 표현 거리의 변화를 측정한다. 큰 변화가 높은 판독 성능을 보장하지는 않는다. 
 
 

 단일 음원 합성 장면과 선형 판독기 에서의 결과다. 낮은 방 요인 점수는 방 정보의 완전한 부재를 뜻하지 않는다. 

 Chen et al., SARL, Figs. 2–3, arXiv:2606.05544v2, CC BY 4.0.
-->

---
layout: default
class: tone-eval academic-slide evidence-slide 
---

## SARL · 민감도와 접근성

<div class="evidence-layout"><div class="evidence-figure"><img src="/research/sarl-sensitivity.svg" /></div><div class="evidence-comment"><h3>많이 변한다고<br/>잘 읽히지는 않는다</h3><p>음원·방 요인을<br/>통제해 바꾼 뒤<br/>표현 거리를 측정한다.</p></div></div>
<div class="figure-caption">앞 장의 판독 점수와 함께 해석한다. 큰 표현 변화가 높은 판독 성능을 보장하지는 않는다.</div>
<div class="source">Chen et al. · SARL · arXiv:2606.05544v2 · Fig. 3</div>

<!--
[발표 노트]
앞 장에서는 고정 인코더의 선형 접근성을 보았다. 이 그림은 입력 요인을 바꿨을 때 표현이 얼마나 변하는지 측정한다. 접근성과 민감도는 서로 다른 측정이다.
[Sources]
https://arxiv.org/html/2606.05544v2/fig3.svg — CC BY 4.0
-->

---
layout: default
class: tone-eval academic-slide 
---

## BMLD · 표적음의 위상만 바꾼다

<p class="academic-lead">양쪽 귀에 같은 잡음. 표적음만 한쪽에서 반전.</p>
<table class="academic-table">
<thead><tr><th>조건</th><th>왼쪽 귀</th><th>오른쪽 귀</th></tr></thead><tbody>
<tr><td>N₀</td><td>잡음 n</td><td>같은 잡음 n</td></tr>
<tr><td>S₀N₀</td><td>s + n</td><td>s + n</td></tr>
<tr><td>SπN₀</td><td>s + n</td><td><b>−s</b> + n</td></tr>
</tbody></table>
<div class="academic-takeaway">두 혼합음의 표현이 <b>잡음 기준에서 떨어진 거리</b>를 비교한다.</div>
<div class="note">BMLD: 양이 마스킹 레벨 차이. 여기서는 임베딩 거리 비율을 dB로 측정한다.</div>
<div class="source">Chen, Yu &amp; He · arXiv:2606.14820v1 · Eq. (1)</div>

<!--
[Sources]
- https://arxiv.org/html/2606.14820v1

[발표 노트]
양쪽 귀에 같은 잡음을 놓는다. 표적음만 한쪽에서 부호를 반전하면 표적의 귀 사이 위상이 180도 변한다. 두 혼합음의 임베딩이 잡음만 있을 때의 임베딩에서 얼마나 떨어지는지 거리 비율을 측정한다. 사람의 BMLD 검출 역치를 그대로 측정하는 실험은 아니다.

[상세 설명]
## BMLD 평가: 잡음은 고정하고 표적음의 양이 위상을 바꾼다

 BMLD는 양이 마스킹 레벨 차이다. 이 평가는 위상 조건에 따른 변화를 고정 임베딩의 거리로 측정한다. 
 
 조건 왼쪽 귀 오른쪽 귀 비교 목적 
 
 N₀ 잡음 n 같은 잡음 n 잡음만 있는 기준 표현 
 S₀N₀ 표적 s + 잡음 n 표적 s + 잡음 n 양쪽 표적이 같은 위상 
 SπN₀ 표적 s + 잡음 n −s + 잡음 n 표적만 180° 반전 
 
 두 혼합음이 잡음 기준 표현에서 떨어진 거리의 비율 을 dB로 비교한다. 
 Δ = 20 log₁₀(‖z(SπN₀) − z(N₀)‖ / ‖z(S₀N₀) − z(N₀)‖). 같은 시행에서는 잡음 파형을 동일하게 유지한다. 
 Chen, Yu &amp; He, arXiv:2606.14820v1, Eq. (1). 청취 검출 역치와 구별되는 임베딩 지표.
-->

---
layout: default
class: tone-eval academic-slide full-figure
---

## BMLD · 모델마다 다른 위상 반응

<div class="hero-figure"><img src="/research/bmld-deficit.svg" /></div>
<div class="academic-takeaway">500 Hz, SNR −14 dB: <b>GRAM-T +2.1 dB</b>, Spatial-AST +6.8 dB, EC 기준 +15.7 dB</div>
<div class="note">임베딩 거리 비율이다. 사람의 청취 역치와 같은 지표가 아니다.</div>
<div class="source">Chen, Yu &amp; He · BMLD · arXiv:2606.14820v1 · Fig. 1 / Table 1</div>

<!--
[Sources]
- Figure: https://arxiv.org/html/2606.14820v1/fig1_absolute_deficit.svg — BMLD, Fig. 1, CC BY 4.0.
- Figure: https://arxiv.org/html/2606.14820v1/fig4_ablation.png — BMLD, Fig. 3, CC BY 4.0.

[발표 노트]
왼쪽 수치는 500 Hz와 −14 dB SNR의 특정 조건이다. EC는 equalization-cancellation 기준이다. dB 값을 나누어 배수 결손으로 해석하지 않는다. 오른쪽은 단서 제거 뒤 유의한 변화가 나타난 조건 비율이며 정답률이 아니다. 위상 반전에 대한 반응에는 스펙트럼·시간 단서가 기여할 수 있다.
- Primary: https://arxiv.org/html/2606.14820v1

[상세 설명]
## BMLD 반응은 위상 이외의 단서에도 영향을 받는다

 
 
 
 500 Hz, SNR −14 dB의 임베딩 거리 지표: GRAM-T +2.1 dB, Spatial-AST +6.8 dB, EC 기준 +15.7 dB. 
 
 
 
 단서 제거 후 유의한 표현 변화의 비율. 역방향 반응도 포함하므로 정확도로 읽지 않는다. 
 
 

 스펙트럼·시간 단서의 기여 를 분리해야 위상 인코딩을 해석할 수 있다. 이 지표는 청취 역치나 기하 등변성을 직접 측정하지 않는다. 

 Chen, Yu & He, BMLD, Figs. 1 & 3, arXiv:2606.14820v1, CC BY 4.0.
-->

---
layout: default
class: tone-eval academic-slide evidence-slide 
---

## BMLD · 다른 단서의 기여

<div class="evidence-layout"><div class="evidence-figure"><img src="/research/bmld-ablation.png" /></div><div class="evidence-comment"><h3>위상 반응에는<br/>다른 단서도 섞인다</h3><p>스펙트럼 단서 제거<br/>시간 단서 제거</p><p>각 조작 뒤의<br/>표현 변화를 비교한다.</p></div></div>
<div class="figure-caption">유의한 변화가 나타난 조건의 비율. 역방향 반응도 포함하므로 정확도로 읽지 않는다.</div>
<div class="source">Chen, Yu & He · BMLD · arXiv:2606.14820v1 · Fig. 3</div>

<!--
[발표 노트]
스펙트럼·시간 단서의 기여를 분리해야 위상 인코딩을 해석할 수 있다. 이 지표는 청취 역치나 기하 등변성을 직접 측정하지 않는다. 원문의 막대는 유의한 변화 조건의 비율이며 반응 부호를 구분해 해석한다.
[Sources]
https://arxiv.org/html/2606.14820v1/fig4_ablation.png — CC BY 4.0
-->

---
layout: default
class: tone-current academic-slide summary-slide
---

## 처음 질문으로 돌아오면

<p class="academic-lead">배열이 바뀌어도 공간 단서를 읽을 수 있는가?</p>
<div class="claim-list">
<div><b>기하 조건부 위치 추정</b><span>새 배열에서도 방향을 구하는가</span></div>
<div><b>사전학습 표현</b><span>다른 과제에서도 정보를 읽는가</span></div>
<div><b>공간 언어 시스템</b><span>음향 단서를 바꾸면 답도 맞게 변하는가</span></div>
</div>
<div class="academic-takeaway">표현은 <b>위상 변화와 배열 기하의 관계</b>를 보존하는가?</div>

<!--
[발표 노트]
도입의 배열 변경 사례를 다시 제시한다. 기하 조건부 위치 추정, 과제 전이, 언어 답변은 각각 유용한 증거다. 이 발표에서는 표현이 위상 변화와 기하 관계를 얼마나 보존하는지라는 후속 질문을 선택한다. 모든 기존 연구가 이 문제를 빠뜨렸다는 선행연구 부재 주장은 하지 않는다.

[상세 설명]
## 처음 질문으로 돌아가면, 서로 다른 증거가 필요하다

 배열을 바꾼 뒤에도 같은 음원의 방향을 읽을 수 있을까? 
 
 문헌에서 살펴본 접근 확인하는 것 추가로 확인할 것 
 
 Neural-SRP · AGG-RL 기하를 조건으로 한 위치 추정 과제를 바꾼 뒤의 표현 재사용 
 MC-SimCLR · SFD · GRAM 사전학습과 후속 과제 성능 동일 조건의 위상·기하 관계 진단 
 BAT · PhaseCoder 공간 단서를 이용하는 언어 시스템 음향 단서 개입과 답변 변화의 일치 
 
 여기서 제안하는 질문은 표현이 위상 변화와 배열 기하의 관계를 얼마나 보존하는가 이다. 
 이 표는 발표의 비교 관점이다. 모든 선행연구가 해당 검증을 누락했다고 주장하는 것은 아니다.
-->

---
layout: default
class: tone-current academic-slide 
---

## 연구 가설 · 지연과 기하의 관계

<p class="proposal-status">검증 전 연구 제안</p>
<div class="current-pipeline">
<div class="current-node"><small>위상 확보</small><b>다채널 인코더</b><p>상대 위상 단서를 남긴다</p></div>
<div class="current-arrow">→</div>
<div class="current-node"><small>관계 판독</small><b>마이크 쌍 표현</b><p>쌍 사이의 지연을 읽는다</p></div>
<div class="current-arrow">→</div>
<div class="current-node"><small>기하 해석</small><b>기하 연산 Q</b><p>지연을 방향과 연결한다</p></div>
</div>
<div class="academic-takeaway"><b>인코더를 고정한 채</b> 새로운 배열에서도 이 관계를 유지할 수 있는가?</div>

<!--
[발표 노트]
여기부터는 문헌의 확정된 결과가 아니라 검증할 연구 가설이다. 위상 단서를 확보하는 인코더와 마이크 쌍 관계의 판독, 기하를 이용하는 연산을 나눈다. 학습되지 않은 배열에서도 지연 판독과 기하 관계가 유지되는지 실험으로 확인해야 한다.

[상세 설명]
## 연구 가설: 마이크 쌍 표현에 지연과 기하의 관계가 남는가

 연구 제안 · 아래 구조와 가설은 실험으로 검증해야 한다. 
 
 01 · 위상 확보 위상을 담는 인코더 다채널 파형의 상대 위상 단서를 보존한다. 
 → 
 02 · 관계 추출 마이크 쌍 관계 콘텐츠와 이득에 덜 흔들리는 마이크 쌍 표현을 만든다. 
 → 
 03 · 기하 작용 기하 법칙 Q 마이크 변위와 후보 방향으로 관계 변화를 학습한다. 
 

 검증할 가설 : 고정한 마이크 쌍 표현에서 지연을 읽고, 새로운 배열에서도 기하 관계를 유지할 수 있다.
-->

---
layout: default
class: tone-current academic-slide 
---

## 네 실험으로 가설을 검증한다

<div class="experiment-grid">
<div class="experiment"><small>01</small><b>고정 표현</b><p>선형 탐침과 소형 MLP로<br/>TDoA·DOA를 읽을 수 있는가?</p></div>
<div class="experiment"><small>02</small><b>새 배열</b><p>채널 수·배치·격자가 바뀌어도<br/>오차가 유지되는가?</p></div>
<div class="experiment"><small>03</small><b>지연 개입</b><p>알려진 Δτ에 맞춰<br/>예측이 변하는가?</p></div>
<div class="experiment"><small>04</small><b>파형과 잠재 개입</b><p>같은 개입에 대응하는<br/>출력 변화가 나타나는가?</p></div>
</div>
<div class="note">검증 계획. 기준선: GCC-PHAT/SRP, 학습 전 인코더. 동일한 학습량과 조건별 불확실성을 보고한다.</div>

<!--
[발표 노트]
각 실험은 비교 기준과 주장을 지지하지 못하는 조건을 함께 정한다. 채널별 시간 지연은 마이크 쌍 사이에 일관되게 적용한다. 임의로 각 쌍의 지연을 따로 바꾸면 하나의 물리 장면과 맞지 않을 수 있다. 전체 장면을 지연시키는 개입과 단일 직접음의 이동도 구별한다. 잠재 개입은 대응 관계를 정의한 뒤 별도 실험으로 평가한다.

[상세 설명]
## 검증 계획과 가설을 지지하지 못하는 조건

 
 실험 통제·비교 관측값과 반증 조건 
 
 고정 인코더 판독 선형 탐침 / small MLP 동일 데이터와 학습량 TDoA·DOA 오차 물리 특징 기준선보다 나쁘면 접근성 주장 제한 
 처음 보는 배열 채널 수·배치·격자를 분리 음원·방 중복 차단 조건별 오차 증가 학습 배열에서만 맞으면 전이 가설 미지지 
 통제된 지연 개입 채널 지연을 일관되게 적용 단일 음원·대역·레벨 통제 알려진 Δτ와 예측 변화의 잔차 다른 단서만으로 설명되면 위상 해석 제한 
 파형·잠재 개입 비교 대응 관계를 별도로 정의 헤드와 질문을 고정 방향·응답 변화의 일치율 개입 간 불일치 시 재사용 범위 제한 
 
 실험 계획이다. 기준선: GCC-PHAT/SRP 및 학습 전 인코더. 효과 크기와 여러 시드·장면의 불확실성을 함께 보고한다.
-->

---
layout: default
class: tone-current academic-slide summary-slide conclusion-slide
---

## 공간 단서를 읽었다는 근거

<div class="claim-list">
<div><b>신호와 기하</b><span>지연을 배열 좌표에 맞춰 해석한다</span></div>
<div><b>표현과 판독</b><span>고정한 모듈과 학습한 모듈을 구분한다</span></div>
<div><b>개입과 일관성</b><span>바꾼 단서에 맞게 표현과 출력이 변한다</span></div>
</div>
<div class="closing-question">정답률에 더해,<br/><b>단서 변화에 대한 반응</b>을 확인한다.</div>

<!--
[발표 노트]
처음 질문에 대한 답은 조건을 명시한 위치 추정 성능과 표현 진단을 함께 보아야 한다는 것이다. 기하 일반화와 단서 개입의 일관성은 제안한 후속 검증이다. 성능 지표를 대체한다는 주장을 하지 않고 토의를 연다.

[상세 설명]
## 배열 일반화와 단서 개입을 함께 검증하는 공간 표현

 배열이 바뀌어도 공간 단서를 읽을 수 있는가? 
 
 신호와 기하 채널 간 지연을 방향으로 해석하려면 배열 좌표가 필요하다. 
 표현과 판독 후속 과제 성능은 인코더 고정 여부와 판독기 용량을 함께 보아야 한다. 
 다음 연구 질문 새 배열과 통제된 지연 개입에서, 표현과 출력의 변화가 일치하는가? 
 
 정답률에 더해, 변화시킨 단서에 맞게 반응하는지 확인한다. 
 문헌 검토의 결론과 후속 실험 제안 · 토의
-->

---
layout: default
class: tone-overview academic-slide academic-appendix
---

## 주요 용어

<div class="appendix-label">부록 A · 용어</div>
<table class="academic-table glossary-table">
<thead><tr><th>용어</th><th>의미</th><th>발표에서의 역할</th></tr></thead>
<tbody>
<tr><td>IPD / ILD</td><td>채널 간 위상차 / 레벨차</td><td>위치와 관련된 관측 단서</td></tr>
<tr><td>TDoA / DOA</td><td>도달 시간차 / 음원의 도래 방향</td><td>상대 지연과 최종 방향을 구별</td></tr>
<tr><td>GCC-PHAT</td><td>위상 변환으로 가중한 일반화 상호상관</td><td>채널 간 지연 추정 기준선</td></tr>
<tr><td>SRP / MUSIC</td><td>조향 응답 전력 / 다중 신호 분류법</td><td>응답 합산 / 부분공간 기반 위치 추정</td></tr>
<tr><td>CPS / HRTF</td><td>교차 전력 스펙트럼 / 머리 관련 전달함수</td><td>채널 간 관계 / 청자별 여과 특성</td></tr>
<tr><td>RIR / BRIR</td><td>방 충격응답 / 바이노럴 방 충격응답</td><td>반사음·잔향을 포함한 전달 특성</td></tr>
<tr><td>바이노럴 / FOA</td><td>두 귀 신호 / 1차 앰비소닉스</td><td>서로 다른 공간 오디오 표현 형식</td></tr>
<tr><td>탐침 / LoRA</td><td>고정 특징의 판독기 / 저랭크 적응</td><td>평가 시 어디를 학습했는지 구별</td></tr>
</tbody></table>

<!--
[발표 노트]
본문에서 처음 등장한 약어를 다시 확인하는 부록이다. 바이노럴과 FOA를 마이크 개수만 다른 동일 신호로 다루지 않는다.
-->

---
layout: default
class: tone-signal academic-slide academic-appendix
---

## PHAT와 지연 추정

<div class="appendix-label">부록 B · 지연 추정</div>

<div class="equation-logic">
  <div>
    <div class="kicker">교차 스펙트럼</div>
    <div class="equation">X₁X₂* = A₁A₂ · exp[j(φ₁−φ₂)]</div>
    <div class="equation small mt-4">∠(X₁X₂*) = φ₁−φ₂ = IPD</div>
  </div>
  <div class="logic-arrow">→</div>
  <div>
    <div class="kicker">PHAT + 역푸리에 변환</div>
    <div class="equation">Φ₁₂(f) = X₁X₂* / |X₁X₂*|</div>
    <div class="equation small mt-4"><span>τ̂ = arg max<sub>τ</sub> 𝓕⁻¹{Φ₁₂}(τ)</span></div>
  </div>
</div>

<div class="equation-result">크기가 아니라 <b>주파수별 위상 변화</b>가 같은 지연값을 가리키는 지점을 찾는다.</div>

<!--
[Sources]
- Claim: Knapp & Carter, “The Generalized Correlation Method for Estimation of Time Delay,” IEEE TASSP, 1976.

[발표 노트]
PHAT는 교차 스펙트럼의 크기를 정규화한다. 실제 구현에는 분모가 0에 가까운 경우의 수치 안정화가 필요하다. 역변환의 지연 부호는 사용한 푸리에 변환과 상관 정의를 일관되게 따라야 한다.
-->

---
layout: default
class: tone-language academic-slide academic-appendix
---

## 공간 표현의 판독기

<div class="appendix-label">부록 C · 표현의 판독</div>

<div class="consumer-map">
  <div class="consumer-origin">공간 표현<br/><span class="muted large">z(x, 배열 기하)</span></div>
  <div class="consumer-branches">
    <div class="consumer-branch"><span>→</span><div><b>위치 추정기</b><small>후보 방향 분류 · 좌표 회귀</small></div></div>
    <div class="consumer-branch"><span>→</span><div><b>탐침 · 디코더</b><small>요인 접근성 · 물리 법칙</small></div></div>
    <div class="consumer-branch"><span>→</span><div><b>언어 모델</b><small>질의응답 · 그라운딩 · 궤적 추론</small></div></div>
  </div>
</div>

<div class="question-hero">임베딩의 공간성을 말하려면, <b>누가 얼마나 적응해 무엇을 읽었는지</b> 밝혀야 한다.</div>

<!--
[발표 노트]
표현을 읽는 모듈과 적응 조건을 구별하는 개념도다. 이 도식이 모든 소개 모델이 명시적 기하 입력을 갖는다는 뜻은 아니다.
-->

---
layout: default
class: tone-eval academic-slide academic-appendix
---

## 판독기마다 다른 검증 가설

<div class="appendix-label">부록 D · 판독기 수식</div>

<div class="readout-grid">
  <div class="readout"><small>LINEAR PROBE</small><h3>선형 탐침</h3><div class="equation small">ŷ = Wz + b</div><p>공간 요인을<br/>선형 변환만으로 읽을 수 있는가?</p></div>
  <div class="readout"><small>SMALL MLP</small><h3>소형 MLP</h3><div class="equation small">ŷ = W₂σ(W₁z)</div><p>약한 비선형 변환만으로<br/>읽을 수 있는가?</p></div>
  <div class="readout"><small>PHYSICS-AWARE DECODER · 연구 제안</small><h3>물리 디코더</h3><div class="equation small">Q(zᵢ,zⱼ; mᵢ,mⱼ) → τᵢⱼ</div><p>마이크 쌍의 관계가<br/>기하 법칙에 맞는가?</p></div>
</div>

<div class="question-hero">판독기의 용량을 밝혀야 <b>‘읽을 수 있다’</b>와 <b>‘물리 법칙에 맞게 정리돼 있다’</b>를 구분할 수 있다.</div>

<!--
[발표 노트]
Linear probe는 선형 접근성, small MLP는 제한된 비선형 접근성을 측정한다. physics-aware decoder는 이 발표가 제안하는 판독 방식이며 기하 조건을 명시해야 한다. 세 방법이 같은 가설을 검증하지는 않는다.
-->

---
layout: default
class: tone-language academic-slide academic-appendix
---

## DSpAST와 OWL

<div class="appendix-label">부록 E · 언어 모델 상세</div>

<div class="paper-compare">
  <div class="paper-side">
    <div class="paper-figure"><img src="/research/dspast-architecture.png" /></div>
    <div><h3>DSpAST · 요인 분리</h3><p>사건 · 방향 · 거리별로 표현을 나눈다.</p></div>
  </div>
  <div class="paper-side">
    <div class="paper-figure"><img src="/research/owl-architecture.png" /></div>
    <div><h3>OWL · 기하 정렬</h3><p>깊이·RIR은 학습 지도 정보다. 추론 입력은 바이노럴 오디오다.</p></div>
  </div>
</div>

<div class="source">Wilkinghoff & Tan, DSpAST official repo illustration; Biswas et al., OWL, Fig. 4.</div>

<!--
[Sources]
- Figure: https://github.com/wilkinghoff/DSpAST/blob/main/dspast_illustration.png — DSpAST official repository, CC BY-NC 4.0.
- Figure: https://arxiv.org/html/2509.26140v1/owl_main_arch.png — Biswas et al., OWL, Fig. 4, CC BY 4.0.

[발표 노트]
DSpAST는 사건·방향·거리 분기와 입력 특징 어텐션을 쓴다. OWL의 깊이·방 충격응답은 학습용 지도 정보이며 추론 시 입력은 바이노럴 오디오다.
- Primary: https://arxiv.org/html/2509.13927v1
- Primary: https://arxiv.org/html/2509.26140v1
-->

---
layout: default
class: tone-overview academic-slide academic-appendix
---

## 공간 오디오 문헌 지도

<div class="appendix-label">부록 F · 문헌 지도</div>

<div class="research-map">
  <div class="map-lane local">
    <div class="lane-name">위치 추정</div><div class="lane-job">방향을 직접 구한다</div><div class="lane-papers">GCC/SRP/MUSIC · IPDnet · Neural-SRP · AGG-RL</div>
  </div>
  <div class="map-lane repr">
    <div class="lane-name">공간 표현</div><div class="lane-job">공간 정보를 다시 쓴다</div><div class="lane-papers">MC-SimCLR · CCSR · SFD · GRAM</div>
  </div>
  <div class="map-lane language">
    <div class="lane-name">언어 모델</div><div class="lane-job">공간을 묻고 설명한다</div><div class="lane-papers">BAT · DSpAST · PhaseCoder · OWL · ST-AudioLM · Spatial-Omni</div>
  </div>
</div>

<div class="map-band"><b>검증</b><span>SARL은 고정 표현의 요인 접근성을, BMLD는 양이 위상 조건에 대한 표현 반응을 비교한다.</span></div>

<div class="note mt-6">공통 문제에 따른 분류다. 직접적인 후속 관계나 모든 평가가 모든 입력 형식에 그대로 적용된다는 뜻은 아니다.</div>

<!--
[발표 노트]
이 지도는 공통 문제를 기준으로 분류한다. 화살표로 직접적인 논문 계승 관계를 주장하지 않는다. SARL과 BMLD는 각각의 입력·분포·지표가 있는 진단이며 모든 모델에 수정 없이 적용된다는 뜻이 아니다.
-->

---
layout: default
class: tone-overview academic-slide academic-appendix
---

## 위치 추정과 표현 학습

<div class="appendix-label">부록 G · 방법 비교</div>
<table class="literature-table academic-literature"><thead><tr><th>연구</th><th>목표</th><th>입력</th><th>학습</th><th>출력</th><th>적응</th><th>핵심 평가</th></tr></thead><tbody>
<tr><td>IPDnet</td><td>위치 추정</td><td>다채널</td><td>DP-IPD</td><td>음원 IPD</td><td>과제 학습</td><td>이동 · 새 배열</td></tr>
<tr><td>Neural-SRP</td><td>위치 추정</td><td>쌍별 위상+좌표+방 크기</td><td>신경 SRP</td><td>위치</td><td>과제 학습</td><td>시뮬 → 실녹음</td></tr>
<tr><td>AGG-RL</td><td>위치 추정</td><td>오디오+기하+격자</td><td>격자 정합</td><td>스펙트럼</td><td>과제 학습</td><td>기하 · 채널 · 격자</td></tr>
<tr><td>MC-SimCLR</td><td>표현 학습</td><td>다채널</td><td>대조 학습</td><td>임베딩</td><td>탐침 / 미세조정</td><td>사건 종류 · 방위각</td></tr>
<tr><td>CCSR</td><td>표현 학습</td><td>다채널</td><td>채널 복원</td><td>임베딩</td><td>선형 / 미세조정</td><td>모의 · 실제 과제</td></tr>
<tr><td>SFD</td><td>강건한 DOA</td><td>바이노럴</td><td>특징 증류</td><td>초기 인코더</td><td>전체 미세조정</td><td>HRTF · 잡음 · 잔향</td></tr>
<tr><td>GRAM</td><td>범용 표현</td><td>다채널</td><td>마스킹 AE</td><td>임베딩</td><td>고정 탐침 / 미세조정 비교</td><td>일반 · 공간 · 실제</td></tr>
</tbody></table>


<!--
[발표 노트]
목표를 먼저 분류한 뒤 입력·학습·출력·적응·평가의 다섯 축으로 읽는다. Neural-SRP의 방 크기와 좌표 입력, GRAM의 고정 탐침과 미세조정 비교를 구분한다.
-->

---
layout: default
class: tone-overview academic-slide academic-appendix
---

## 언어 시스템과 진단 프로토콜

<div class="appendix-label">부록 H · 시스템과 평가</div>
<table class="literature-table academic-literature"><thead><tr><th>연구</th><th>목표</th><th>입력</th><th>학습</th><th>출력</th><th>적응</th><th>핵심 평가</th></tr></thead><tbody>
<tr><td>BAT</td><td>공간 QA</td><td>바이노럴</td><td>지시 학습</td><td>텍스트</td><td>프로젝터+LoRA</td><td>추론 QA</td></tr>
<tr><td>DSpAST</td><td>공간 QA</td><td>바이노럴</td><td>사건·방향·거리 분리</td><td>텍스트</td><td>LLM 연결</td><td>요인 QA</td></tr>
<tr><td>PhaseCoder</td><td>DOA + QA</td><td>다채널+기하</td><td>위상 토큰</td><td>좌표 / 텍스트</td><td>LLM 연결</td><td>새 배열 기하</td></tr>
<tr><td>OWL</td><td>3D QA</td><td>바이노럴</td><td>깊이·RIR 지도</td><td>텍스트</td><td>LLM 연결</td><td>BiDepth + 전이</td></tr>
<tr><td>ST-AudioLM</td><td>궤적 QA</td><td>FOA 시퀀스</td><td>사건+움직임</td><td>토큰</td><td>시스템 학습</td><td>동적 QA</td></tr>
<tr><td>Spatial-Omni</td><td>통합 QA</td><td>FOA</td><td>SO-Encoder</td><td>텍스트</td><td>시스템 학습</td><td>16개 하위 과제</td></tr>
<tr><td>SARL</td><td>표현 진단</td><td>통제 합성 장면</td><td>선형 탐침</td><td>요인별 점수</td><td>인코더 고정</td><td>접근성 · 민감도</td></tr>
<tr><td>BMLD</td><td>단서 진단</td><td>양이 위상 조건</td><td>추가 학습 없음</td><td>거리 비율</td><td>인코더 고정</td><td>위상 반전 · 단서 제거</td></tr>
</tbody></table>
<div class="note">OWL의 깊이·RIR은 학습용 지도 정보다. 추론에는 바이노럴 오디오를 사용한다.</div>

<!--
[발표 노트]
언어 시스템은 인코더, 프로젝터, LLM의 학습 조건이 다르다. SARL과 BMLD는 방법과 평가의 혼동을 피하도록 별도 행으로 표시했다.
-->

---
layout: default
class: tone-eval academic-slide evidence-slide academic-appendix
---

## Neural-SRP · 실제 녹음의 응답

<div class="evidence-layout"><div class="evidence-figure"><img src="/research/neural-srp-output.png" /></div><div class="evidence-comment"><h3>같은 녹음,<br/>다른 공간 응답</h3><p>위: NeuralSRP+<br/>아래: SRP</p><p>주황색 ×는 음원,<br/>파란 점은 마이크다.</p></div></div>
<div class="figure-caption">원문의 실제 녹음 예시. 하나의 예시 그림으로 모든 조건의 성능을 대표하지 않는다.</div>
<div class="source">Grinstein et al. · Neural-SRP · arXiv:2403.09455v1 · Fig. 1</div>

<!--
[발표 노트]
본문에서 비교한 SRP와 Neural-SRP의 응답 예시를 보여준다. 그림의 위쪽과 아래쪽 방법을 바꾸어 읽지 않는다.
[Sources]
https://arxiv.org/html/2403.09455v1/outputs.png — CC BY 4.0
-->

---
layout: default
class: tone-eval academic-slide evidence-slide academic-appendix
---

## AGG-RL · 후보 방향별 응답

<div class="evidence-layout"><div class="evidence-figure"><img src="/research/agg-rl-spectrum.png" /></div><div class="evidence-comment"><h3>4채널,<br/>2음원 장면</h3><p>후보 방향별<br/>공간 스펙트럼을<br/>비교하는 예시</p></div></div>
<div class="figure-caption">공식 프로젝트의 예시 그림. 일반화 범위는 논문의 실험 조건으로 판단한다.</div>
<div class="source">Baek et al. · AGG-RL · Official project</div>

<!--
[발표 노트]
원문의 스펙트럼 예시를 확대해 확인하는 부록이다. 단일 그림을 새 배열·채널·격자 모두에 대한 일반화의 증거로 해석하지 않는다.
[Sources]
https://raw.githubusercontent.com/BaekMS/Audio-Geometry-Grid_Representation-Learning/main/spectrum_plots/4ch_0.png
원저작자 귀속. 저장소에 명시적인 그림 재사용 라이선스가 없다.
-->

---
layout: default
class: tone-overview academic-slide academic-appendix
---

<div class="appendix-label">참고문헌 · 1/2</div>
<h2>위치 추정 · 표현 학습 · 데이터</h2>

<div class="references-grid">
<ol>
  <li>Knapp & Carter. <b>The Generalized Correlation Method for Estimation of Time Delay.</b> IEEE TASSP, 1976.</li>
  <li>Grinstein et al. <b>The Neural-SRP Method for Positional Sound Source Localization.</b> arXiv:2403.09455, 2024.</li>
  <li>Wang et al. <b>IPDnet: A Universal Direct-Path IPD Estimation Network for Sound Source Localization.</b> arXiv:2405.07021, 2024.</li>
  <li>Baek et al. <b>Physics-Informed Audio-Geometry-Grid Representation Learning for Universal Sound Source Localization.</b> ICLR 2026.</li>
  <li>Jiang et al. <b>Exploring Self-Supervised Contrastive Learning of Spatial Sound Event Representation.</b> arXiv:2309.15938, 2023.</li>
  <li>Yang & Li. <b>Self-Supervised Learning of Spatial Acoustic Representation with Cross-Channel Signal Reconstruction and Multi-Channel Conformer.</b> arXiv:2312.00476, 2023.</li>
</ol>
<ol start="7">
  <li>Bovbjerg et al. <b>Learning Robust Spatial Representations from Binaural Audio through Feature Distillation.</b> arXiv:2508.20914, 2025.</li>
  <li>Yuksel et al. <b>GRAM: Spatial General-Purpose Audio Representations for Real-World Environments.</b> arXiv:2506.00934v5, 2025–2026.</li>
  <li>Chen et al. <b>SoundSpaces 2.0: A Simulation Platform for Visual-Acoustic Learning.</b> NeurIPS, 2022.</li>
  <li>Evers et al. <b>The LOCATA Challenge.</b> IEEE/ACM TASLP, 2020.</li>
  <li>Princeton 3D3A Lab. <b>3D3A HRTF Database.</b> CC BY 4.0.</li>
  <li>Biswas et al. <b>BiDepth dataset</b> in OWL, arXiv:2509.26140, 2025.</li>
</ol>
</div>

<!--
[발표 노트]
위치 추정, 공간 표현, 데이터의 주요 참고문헌이다. 본문 결과의 세부 조건은 각 슬라이드의 원문 링크와 함께 확인한다.
-->

---
layout: default
class: tone-overview ref-references-end academic-slide academic-appendix
---

<div class="appendix-label">참고문헌 · 2/2</div>
<h2>언어 모델 · 평가</h2>

<div class="references-grid">
<ol start="13">
  <li>Zheng et al. <b>BAT: Learning to Reason about Spatial Sounds with Large Language Models.</b> arXiv:2402.01591, 2024.</li>
  <li>Wilkinghoff & Tan. <b>DSpAST: Disentangled Representations for Spatial Audio Reasoning with Large Language Models.</b> arXiv:2509.13927, 2025.</li>
  <li>Dementyev et al. <b>PhaseCoder: Microphone Geometry-Agnostic Spatial Audio Understanding for Multimodal LLMs.</b> arXiv:2601.21124, 2026.</li>
  <li>Biswas et al. <b>OWL: Geometry-Aware Spatial Reasoning for Audio Large Language Models.</b> ICLR 2026.</li>
  <li>Oh et al. <b>Spatio-Temporal Audio Language Modeling for Dynamic Sound Sources.</b> arXiv:2606.14141, 2026.</li>
</ol>
<ol start="18">
  <li>Zhu et al. <b>Spatial-Omni: Spatial Audio Understanding Integration in Multimodal LLMs via FOA Encoding.</b> arXiv:2606.10738, 2026.</li>
  <li>Chen et al. <b>Probing Spatial Structure in Pretrained Audio Representations.</b> arXiv:2606.05544, 2026.</li>
  <li>Chen, Yu & He. <b>Spectro-Temporal Interference Confounds Phase Encoding in Spatial Audio Foundation Models.</b> arXiv:2606.14820, 2026.</li>
  <li>Grumiaux et al. <b>A Survey of Sound Source Localization with Deep Learning Methods.</b> JASA, 2022.</li>
  <li>Grinstein et al. <b>Steered Response Power for Sound Source Localization: A Tutorial Review.</b> EURASIP, 2024.</li>
</ol>
</div>

<div class="note mt-6">대표 논문을 중심으로 그린 지도다. 모든 위치 추정·SELD·공간 LLM 연구를 망라하지는 않는다.</div>

<!--
[발표 노트]
공간 언어 모델과 진단 프로토콜의 주요 참고문헌이다. 2026년 논문 중 arXiv 원고와 학회 발표를 구별해 표기했다.
-->
