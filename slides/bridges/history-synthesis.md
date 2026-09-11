---
layout: seminar
variant: figure
---

# 연구사의 공통 질문은 공간 정보가 어디서 사라지는가다

::body::
<table class="seminar-compact" style="font-size:24px;line-height:1.3">
<colgroup><col style="width:36%"/><col style="width:38%"/><col style="width:26%"/></colgroup>
<thead><tr><th>연구에서 바뀐 질문</th><th>정보가 넘어가는 경계</th><th>필요한 확인</th></tr></thead>
<tbody>
<tr><th scope="row">BAT: 위치에서 관계 질문으로</th><td>E → P → LM</td><td>질문만 / 오디오 추가</td></tr>
<tr><th scope="row">DSpAST · OWL: 무엇을 배울까</th><td>물리 단서·기하 지도 → E</td><td>E 판독과 QA 구분</td></tr>
<tr><th scope="row">Motion: 예측을 언어로 넘길까</th><td>속성 시계열 → JSON → LM</td><td>예측 오류·정보 누락</td></tr>
<tr><th scope="row">기존 Audio-LM: 공간을 더할까</th><td>의미 + 공간 → P → LM</td><td>공간 기여·의미 능력</td></tr>
<tr><th scope="row">Dynamic · ST: 이동을 묻는다면</th><td>사건·시간·음원 → 토큰</td><td>시간·정체성 결속</td></tr>
</tbody>
</table>

::takeaway::
각 논문을 **무엇을 남기고, 무엇을 넘기며, 답에 무엇을 쓰게 했는가**로 연결해 읽는다.

::source::
27편의 설계·평가 종합 · 연구사와 명시적 계승 근거는 발표 노트 및 근거 부록.

<!--
[Sources]
- https://arxiv.org/html/2402.01591v1
- https://arxiv.org/html/2509.13927v1
- https://arxiv.org/html/2509.26140v1
- https://arxiv.org/html/2509.14666v1
- https://arxiv.org/html/2510.05542v1
- https://arxiv.org/html/2606.14141v1

[그림]
이 표는 원문 Methods에 근거한 연구 질문과 평가 기준의 정리다. PPT에서도 native table로 내보낸다. 최초 공개 연대와 채택 버전은 plans/MC_AUDIO_LM_HISTORY.md에 구분하여 기록했다. 화살표는 그림 내부의 데이터 흐름이며 논문 간 성능 상승을 뜻하지 않는다.

[연구사와 발표 노트]
공간 신호처리에서는 지연 관계를 후보 좌표의 응답으로 바꾸고 합산했다. Neural-SRP는 그 쌍별 응답 생성기를 학습하되 합산과 좌표 선택을 유지했다. 다음 단계는 이 출력 좌표만으로 사건·시간·관계 질문에 충분한가이다.
BAT는 공간 속성을 학습한 encoder의 표현을 언어 질문에 연결했다. DSpAST와 OWL은 같은 틀의 표현 사전학습과 입력 단서를 다시 설계했다. Motion은 명시적인 예측 속성 언어화를 통해 별도 추론 LM과 연결하는 다른 선택이다. Sci-Phi·PhaseCoder·Spatial-Omni·TWNM은 이미 풍부한 의미·음성 경로가 있는 모델에 공간 경로를 더하면서 결속, 배열 조건, 이식과 학습을 묻는다. Dynamic QA·ST-AudioLM에서는 표현의 시간 구조가 새로운 요구가 된다.
이러한 문제의 확대가 인코더·연결부·LM의 평가 기준을 정한다. E의 고정 판독에 공간 정보가 읽힌다는 사실만으로 LM이 그것을 쓴다고 보장하지 않는다. JSON과 연속 token의 전달 범위, 질문만 기준선과 오디오 입력의 차이, 단서 개입에 따른 답의 변화, 기존 능력 보존을 구분한다. 마지막 장은 동일 장면의 H→Z/JSON→답을 함께 검사하는 앞으로의 실험 제안이며 이번 작업에서 수행한 모델 실험이 아니다.
-->
