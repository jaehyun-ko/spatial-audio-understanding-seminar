---
layout: seminar
variant: figure
---

# 연결 정렬과 언어 적응은 다른 학습 단계다

::body::
<PaperFigure src="/diagrams/causal-adapter-training.svg" alt="표현 사전학습, 인코더와 LLM을 고정한 연결 모듈 정렬, 연결 모듈과 LLM LoRA 적응을 구분한다. Spatial-Omni와 Sci-Phi는 공간 인코더를 학습하는 순서가 다르다." />

::takeaway::
흔한 순서는 **표현 학습 → 연결 정렬 → 언어 적응**이며, 동결 범위는 논문마다 다르다.

::source::
Spatial-Omni v2 학습 단계 · Sci-Phi v1 §3.1–3.3. 상단은 공통 설명용 단계.

<!--
[B-ADAPTER-TRAINING]
[Sources]
- https://arxiv.org/html/2606.10738v2
- https://arxiv.org/html/2510.05542v1
[그림]
public/diagrams/causal-adapter-training.svg. 파랑과 청록의 채워진 영역은 해당 단계에서 학습하는 모듈이다. 회색 기본 가중치와 학습하는 LoRA를 분리했다. 표현 학습의 사건·위치·시간 heads는 가능한 학습 목표의 분류이며 모든 모델이 세 목표를 동일하게 사용한다는 뜻은 아니다. 아래 두 줄은 논문의 QA 학습 차이를 나타낸다.
[발표 노트]
인코더 사전학습은 관측으로부터 의미·공간·시간 표현을 학습하는 문제이다. 연결 정렬은 기존 E와 LLM을 고정한 채 P가 적절한 연속 입력을 만들도록 학습하는 문제이다. 다음 단계에서는 P와 함께 LLM을 적응시키기도 한다. LoRA는 기본 가중치를 고정하면서 추가 저랭크 가중치를 학습하는 흔한 방법이다. 상단 세 단계는 설명을 위한 일반형이며 각 논문의 실제 일정과 구분해야 한다.
[실제 사례]
Spatial-Omni는 별도 E 사전학습 뒤 QA에서 P만 학습하고, 다음 P+LLM LoRA, 마지막에는 P+LoRA+SO-Encoder를 학습한다. 기존 Omni audio tower는 기본 설정에서 계속 고정이다. 따라서 E가 항상 고정된다고 그리면 틀린다. 단계별 점수 상승은 학습량과 질문 난도 및 동결 범위도 함께 바뀌므로 LoRA 하나의 효과로 귀속하지 않는다.
Sci-Phi는 기존 mono encoder/projector와 Audio LoRA를 고정하고, 공간 SELDNet encoder와 신규 공간 projector 및 Spatial LoRA를 함께 QA 학습한다. Spatial LoRA r320의 별도 공간 적응 경로를 기존 Audio LoRA와 혼동하지 않는다.
[해석 범위]
고정된 모듈의 구조와 기존 일반 오디오 성능의 유지 여부는 별개다. Spatial-Omni Table18에서 일반 audio 성능 감소와 MIX의 일부 회복을 함께 확인해야 한다. LoRA만 가능한 것도 아니다. connector-only, 다른 adapter, 전체 미세조정 등의 선택 가능성이 있으며 개별 논문의 실험 범위 안에서 판단한다.
[전환]
연결 모듈과 LoRA를 모두 어댑터라고 부르면 역할이 섞인다. 다음 그림은 두 모듈이 실제로 놓이는 위치를 구분한다.
-->
