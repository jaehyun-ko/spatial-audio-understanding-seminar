---
layout: seminar
variant: figure
---

# 공간 QA에서 기존 Audio-LM 확장과 동적 장면으로

::body::
<PaperFigure src="/diagrams/history-map.svg" alt="최초 공개 연대와 개정판을 구분한 지도로, 초기 BAT에서 표현 개선·구조화 언어 전달·기존 Audio-LM 확장·시간 표현으로 연구 문제가 갈라지는 과정을 먼저 제시한다." />

::takeaway::
**공간 QA 연결 → 표현·전달 방식의 분화 → 기존 Audio-LM 확장 → 시간 구조**

::source::
BAT v1 §4 · DSpAST·Motion·OWL·Sci-Phi의 최초 공개본 · 2026 채택 버전은 노트 참조.

<!--
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
