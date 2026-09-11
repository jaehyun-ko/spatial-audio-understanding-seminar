---
layout: seminar
variant: figure
---

# 보존·전달·사용은 각각 확인해야 한다

::body::
<PaperFigure src="/diagrams/causal-synthesis.svg" alt="인코더에서 정보가 남는지, 어댑터가 의미·공간·시간 구조를 전달하는지, LLM이 질문에 따라 오디오를 사용하는지의 세 경계와 해당 증거를 연결" />

::takeaway::
좋은 Audio-LLM은 **정보를 남기고, 구조를 전달하고, 답에 사용하는 조건**을 만족해야 한다.

::source::
27편의 설계·평가 근거 종합. 문헌별 관찰 범위와 실제 모듈 구성은 발표 노트·근거 부록 참조.

<!--
[이번 장의 역할]
논문명을 외우는 대신 세 개의 확인 가능한 질문으로 회수한다. 인코더의 채널·주파수·시간 처리는 공간 단서를 남기는가. adapter가 차원·길이를 맞추면서 사건과 위치, 시간의 결속을 전달하는가. 언어 모델 적응은 새로 연결한 연속 audio token을 질문에 맞게 이용하게 하는가. 이 역할 구분으로 각 논문의 의미가 생긴다.

MC-SimCLR·CCSR·SFD·LAM·GRAM은 서로 다른 학습 목표와 판독 프로토콜의 인코더 증거다. AT2SELD는 의미와 공간의 결합 위치를 고정 클래스 SELD에서 본다. ELSA·SALM·CoSTALA는 언어 정렬과 결속의 요구를 다루며 생성형 LLM이나 LoRA 효과의 증거는 아니다. SelectTSL은 prompt로 목표를 지정해 물리 단서를 판독하는 별도 설계다.

BAT·DSpAST·OWL·Dual-BEATs·PhaseCoder는 관측 입력과 인코더, 학습 조건을 구분해 읽는다. Sci-Phi·Spatial-Omni·TWNM·ST-AudioLM은 의미/공간 분기와 source/time 구조의 전달을 비교한다. Motion 2025·Dynamic QA는 예측 속성이나 선택한 시간 구간이 LLM에 주는 정보의 범위를 드러내는 별도 경로다. STAR-Bench·WearVox는 시스템 답변의 평가이고 SARL·BMLD는 표현 수준의 검사다. 한 단계의 관찰만으로 다른 단계를 이미 증명했다고 말하지 않는다.

[Sources]
- https://arxiv.org/html/2506.00934v5
- https://arxiv.org/html/2606.05544v2
- https://arxiv.org/html/2606.14820v1
- https://arxiv.org/html/2510.05542v1
- https://arxiv.org/html/2606.10738v2
- https://arxiv.org/html/2606.14141v1
- https://arxiv.org/html/2402.01591v4
-->
