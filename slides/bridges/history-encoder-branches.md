---
layout: seminar
variant: figure
---

# 같은 연결 틀에서, 인코더가 배워야 할 것을 바꾼다

::body::
<PaperFigure src="/diagrams/history-encoder-branches.svg" alt="2025년 DSpAST와 OWL은 BAT의 공간 표현 문제를 각각 과제별 단서 선택과 방 기하 감독으로 확장한다. 둘의 공통 기반과 다른 학습 개입을 먼저 보여 준 뒤 각 내부 비교를 읽는다." />

::takeaway::
같은 공간 QA 틀에서도 **어떤 신호 단서를 넣고 어떤 목표로 E를 학습하는지**가 다르다.

::source::
DSpAST v1 §2–4 · OWL v1 §4–5 · BAT 기반의 명시적 확장/참조.

<!--
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
