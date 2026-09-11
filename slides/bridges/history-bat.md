---
layout: seminar
variant: figure
---

# BAT: 공간 지각의 표현을 질문의 입력으로 바꾼다

::body::
<PaperFigure src="/diagrams/history-bat.svg" alt="일반 Audio-LM의 encoder→projection→LM 연결을 공간 지각에 적용한 초기 대표 모델이다. 공간 좌표를 텍스트로만 직렬화하는 모델이 아니며 기하 인코더 사전학습과 공간 QA 적응을 구별한다." />

::takeaway::
BAT의 전환은 **공간 속성을 배우던 인코더의 표현을 언어 질문에 재사용**한 데 있다.

::source::
Pengi 2023 §3 · BAT 최초 공개 v1 §4–5; 결과 장은 지정 v4 사용.

<!--
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
