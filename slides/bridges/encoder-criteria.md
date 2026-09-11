---
layout: seminar
variant: figure
---

# LLM 전에 무엇이 읽혀야 하는가?

::body::
<PaperFigure src="/diagrams/causal-encoder-criteria.svg" alt="같은 알람의 위치 이동, 같은 좌표의 소리 교체, 같은 두 사건의 순서 교환을 각각 인코더 표현 H의 판독으로 연결한다. 기대하는 종류·위치·순서의 변화와 불변을 구분한다." caption="후속 실험 제안. = 는 유지, ↔ 는 조건에 맞는 변화. H는 인코더 표현." />

::takeaway::
같은 소리의 <strong>종류는 유지</strong>하고, 바뀐 <strong>위치와 순서는 읽혀야 한다.</strong>

::source::
SARL v2 · SALM v2 · SelectTSL v1 · CoSTALA v1의 관측 문제를 종합한 제안.

<!--
[Bridge: encoder-criteria]
[Sources]
- https://arxiv.org/html/2606.05544v2
- https://arxiv.org/html/2507.16724v2
- https://arxiv.org/html/2607.02343v1
- https://arxiv.org/html/2608.24374v1
- https://aclanthology.org/2022.cl-1.7/
[청중 질문]
오디오를 LLM에 넘기기 전에 encoder에서 확인해야 할 정보는 무엇인가?
[발표 노트]
모든 도형과 latent cell은 설명용이며 실험 결과가 아니다. 왼쪽은 같은 dry 알람의 위치만 바꾼다. 알람이라는 의미는 같고 정답 위치는 달라야 한다. 가운데는 위치를 고정하고 알람을 말소리로 교체한다. 좌표는 같고 종류는 달라야 한다. 오른쪽은 사건과 구간을 유지한 채 AB와 BA의 순서를 교환한다. 판독은 명시적인 학습 head/probe이며 LLM의 답변이 아니다.
H_frame, H_mean, adapter 뒤 Z를 구별해 같은 조건의 판독기를 학습한다. 선형 probe에서 못 읽는 것은 모든 정보가 사라졌다는 뜻이 아니다. 위치 민감성 또는 좌표 변환에 대한 equivariance와 의미 label의 invariance를 혼동하지 않는다. 수치나 성공률은 아직 측정하지 않았다.
[확장 통제]
두 소리의 의미–위치 결속은 종류 집합과 위치 집합을 유지하고 대응만 교환하여 측정한다. 종류와 위치를 개별적으로 맞히는 것만으로 공동 대응은 보장되지 않는다. 시간 순서 판독과 동일 종류 두 음원의 지속 identity 추적도 별개다. SelectTSL의 MOTA*는 ID switch를 제외하므로 후자를 증명하지 않는다. CoSTALA의 known segment duration을 자동 사건 경계 검출로 바꾸어 말하지 않는다.
[해석 범위]
그림의 2-mic 배치는 도입 장면의 관찰 좌표계를 회수한다. 두 채널의 단일 지연만으로 3차원 좌표를 유일하게 복원할 수 있다고 주장하지 않는다. 실제 실험에는 과제·배열·방에 맞는 식별 가능성과 train/test source·RIR 분리가 필요하다.
[전환]
표현에서 정보를 읽을 수 있다면, adapter와 LLM은 그 정보를 얼마나 보존하고 사용하는가?
-->
