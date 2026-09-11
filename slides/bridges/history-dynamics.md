---
layout: seminar
variant: figure
---

# 움직임을 묻기 시작하면 시간 구조가 필요하다

::body::
<PaperFigure src="/diagrams/history-dynamics.svg" alt="Motion의 명시적 시계열과 BAT 계열 Dynamic QA·ST-AudioLM의 연속 토큰 경로를 나란히 비교한다. BAT에서 후자의 backbone 계승은 원문 명시이며 세 논문 사이의 직선적인 성능 발전으로 그리지 않는다." />

::takeaway::
정적 위치 다음에는 **어느 음원이 언제 움직였는지**를 전달하는 방식이 쟁점이 된다.

::source::
Motion v1 §2.2 · Dynamic Source Movements v1 §3.2 · ST-AudioLM v1 §2·4·5.1.

<!--
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
