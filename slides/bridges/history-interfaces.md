---
layout: seminar
variant: figure
---

# 언어로 기술해 넘길까, 오디오 표현을 직접 연결할까?

::body::
<PaperFigure src="/diagrams/history-interfaces.svg" alt="Motion은 예측 속성을 JSON으로, OWL은 SAGE의 연속 표현을 Q-Former로 전달한다. 입력 인터페이스와 LoRA 가중치 적응을 별도 축으로 구분한다." />

::takeaway::
**LM에 들어가는 정보의 형식**과 **LM 가중치를 학습하는 방식**은 서로 다른 선택이다.

::source::
Motion 2025 v1 §2.2 · OWL v1 §5, App. B.3 · PhaseCoder v2 §4.2, App. K.

<!--
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
