# 27편 근거 인덱스

검토일: 2026-09-09 · 상위 설계: [NARRATIVE_PLAN.md](../NARRATIVE_PLAN.md)

근거 카드: [P01–P11](EVIDENCE_P01_P11.md) · [P12–P23](EVIDENCE_P12_P23.md) · [P24–P27](EVIDENCE_P24_P27.md)

P-ID는 문헌의 고정 식별자이며 슬라이드 순서·성능 순위·출판 순서가 아니다. 원문의 결과를 재현한 것이 아니라 발표에 사용할 보고 근거를 선정했다. 명세와 카드가 충돌하면 아래 우선순위로 제작 전에 해결한다.

1. 정확한 버전의 원문 조건·표/그림.
2. 근거 카드의 비교 대상·단위·허용 결론.
3. 장별 명세의 좁은 주화면 선택.
4. 상위 스토리보드의 짧은 요약.

카드는 참고할 전체 비교를 보존할 수 있지만 주화면은 한 비교로 좁힌다. 부록 수치를 본문에 전부 넣지 않는다. 미해결 원고 오류를 임의 수정하지 않는다.

| ID | 문헌 | 본문 위치 | 고유 역할·주 결과 |
| --- | --- | --- | --- |
| P01 | Neural-SRP | S10–11 | 쌍별 학습 위치 응답; Table I Recorded4 |
| P02 | AGG-RL | S04–05·S07·S12–14 | 물리 문제/배열·격자 정합; Table 3 Dynamic-U, 같은 모델 AGG 유무 |
| P03 | MC-SimCLR | S18–19 | 반복 관측 대조; Table 1 LP 사건/방향 |
| P04 | CCSR | S20–21 | 가린 STFT 프레임 복원; Table III 8개 방 |
| P05 | SFD | S24–25 | clean 특징 목표; Fig. 2 1h, 10min은 부록 |
| P06 | GRAM | S28–30 | 복합 장면 표현; Fig. 3(A) DOA 판독 |
| P07 | LAM | S22–23 | covariance를 설명하는 지도; LE/LR trade-off |
| P08 | AT2SELD | S26–27 | 의미·공간 결합 위치; Table 12 |
| P09 | ELSA | S32–33 | 공간 문장 정렬; Table 2/A.T.7 Direction |
| P10 | SALM | S34–35 | 구조화 정렬 목표; Table 1 loss ablation |
| P11 | SelectTSL | S36–37 | 요청 목표 DOA/활성 수; Table VI |
| P12 | BAT | S38–39 | 질문별 공간 답변; Table 4 audio/prompt |
| P13 | DSpAST | S40–41 | 과제별 특징 읽기; Table 3 matched interface |
| P14 | OWL | S42–44 | 학습 때 기하 지도; Table 5 |
| P15 | PhaseCoder | S47–48 | 배열+좌표의 언어 연결; v2 Table 3 |
| P16 | Dual-BEATs | S45–46 | 전처리와 레벨 단서; Table 1 dither |
| P17 | Sci-Phi | S50–52 | 음원별 속성 묶음; Fig. 2 TupleScore |
| P18 | Spatial-Omni | S53–55 | 과제별 공간 토큰; v2 Table 2 zero-spatial |
| P19 | The World is Not Mono | S56–58 | source slots·복합 질의; v3 Table 5 SAPO |
| P20 | Spatial Audio Motion Understanding and Reasoning | S59–60 | 시간 속성→JSON→LLM; Table 3 |
| P21 | Spatial Audio Question Answering and Reasoning on Dynamic Source Movements | S59·S61 | 질문 관련 구간; Table 3 mask 비교 |
| P22 | ST-AudioLM | S62–64 | 시간별 의미·궤적; Table 5 조합 QA |
| P23 | CoSTALA | S65–66 | 사건 순서/위치 정렬; Table 2 retrieval |
| P24 | STAR-Bench | S67–69 | 질문·모델 답변의 시험; Table 2 AA |
| P25 | WearVox | S67·S70–71 | 실제 응답 대상 판단; Table 4 side-talk |
| P26 | SARL | S67·S72–73 | 고정 표현 접근성; Fig. 2/3 정의 구별 |
| P27 | BMLD/간섭 단서 연구 | S67·S74–76 | 통제 자극·거리 반응; Table 1/Fig. 3 |

## 결과 해석에 공통으로 붙일 조건

- 입력: 원시 배열 / binaural / FOA / amplitude-panned stereo / beamformed signal을 구별한다. 좌표와 depth가 각각 추론 입력인지 학습 지도인지 표시한다.
- 갱신 범위: frozen encoder는 판독기까지 무학습이라는 뜻이 아니다. 전체 미세조정과 모듈 적응을 따로 쓴다.
- 데이터: 완전 합성 / 측정 RIR 기반 합성 / 현장 혼합음 녹음을 구별한다. ‘새 방’과 ‘새 음원 정체성’과 ‘새 배열’은 다른 split이다.
- 지표: 각도·위치 오차, 검출률, QA 정확도, Recall@K, 정규화 접근성, 임베딩 거리비를 합산하거나 공통 점수처럼 그리지 않는다.
- 결론: 시스템 비교와 단일 요소 ablation을 구별한다. 미보고는 실패가 아니며, 한 조건의 성공은 보편적 해결이 아니다.

## 제작 단계에 남은 gate

선택한 그림의 파일 취득·출판본 대조·표 셀/범례 재확인·출처 및 재구성 표기·읽을 수 있는 크롭·렌더·리허설은 아직 남았다. SFD Table 2, SelectTSL Table III 등 원문 충돌의 처리 상태는 [레드팀 보고](REDTEAM_REVIEW.md)에 모았다. 이 인덱스는 원문 버전 변경을 자동 추적하지 않는다.

IPDnet과 GCC/SRP는 설명용 기준이며 이 27편에 중복 계수하지 않는다. 선택적 시청각·생성·과제 확장은 본문 범위 밖에 유지한다.
