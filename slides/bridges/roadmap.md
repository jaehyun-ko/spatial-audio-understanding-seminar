---
layout: seminar
variant: figure
---

# 좌표를 찾던 신호로, 질문에도 답하려면?

::body::
<PaperFigure src="/diagrams/causal-roadmap.svg" alt="같은 다채널 관측에서 위쪽은 SRP 또는 학습 응답과 좌표 출력, 아래쪽은 인코더 표현과 어댑터를 거쳐 LLM의 종류·위치·시간 답변으로 이어지는 두 요구" />

::takeaway::
**계산할 응답 → 남겨 둘 정보 → LLM이 읽을 토큰**의 순서로 설계를 살핀다.

::source::
설명용 설계 비교. Neural-SRP §IV; Spatial-Omni §3; ST-AudioLM §3. 기술의 대체 역사가 아님.

<!--
[이번 장의 역할]
발표의 질문을 연산과 정보의 흐름으로 정의한다. 앞의 두 채널 관측에는 경로 차이·잔향·배열 기하가 함께 반영된다. 먼저 이 관측에서 후보 위치의 응답을 계산하고 정해진 좌표를 고르는 일을 다룬다. 다음은 왜 그 응답을 학습하는지다. 위치 출력만 얻고 끝내는 대신 사건 종류·위치·시간을 보존한 중간 표현을 만들면, 여러 질문에 사용할 가능성이 생긴다. 여기부터 encoder의 성질, adapter의 전달 형식, LLM의 입력 활용을 나눠 관찰해야 한다.

기존 SRP·Neural-SRP가 Audio-LLM으로 순차 대체되었다는 역사적 주장을 하지 않는다. 같은 목표를 확장할 때 달라지는 설계 질문을 설명한다. Neural-SRP 원형의 2D 위치 출력과 도입의 3D 연구 목표도 동일시하지 않는다. 새로운 3D 도해와 파형은 교육용이며 모든 후속 논문의 실제 입력 채널 구성이 같다는 뜻이 아니다.

[Sources]
- https://arxiv.org/html/2403.09455v1
- https://arxiv.org/html/2606.10738v2
- https://arxiv.org/html/2606.14141v1
-->
