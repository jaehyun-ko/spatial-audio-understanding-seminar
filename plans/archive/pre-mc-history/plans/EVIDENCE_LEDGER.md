# 27편 근거 인덱스

검토일: 2026-09-09 · 제작 검토: 2026-09-11 · 상위 설계: [NARRATIVE_PLAN.md](../NARRATIVE_PLAN.md)

이 인덱스의 27편을 현재 80장 원고의 근거로 유지한다. 산출물의 생성·검수 상태는 이번 개정의 명세와 검사 기록을 따른다. 실제 채택한 버전·크롭·수치 범위는 장별 발표 노트와 ASSETS_PART1–3에 기록했다. 출판본 대조가 완료되지 않은 자료는 명시한 arXiv 버전의 결과로 유지한다.

근거 카드: [P01–P11](EVIDENCE_P01_P11.md) · [P12–P23](EVIDENCE_P12_P23.md) · [P24–P27](EVIDENCE_P24_P27.md)

P-ID는 문헌의 고정 식별자이며 슬라이드 순서·성능 순위·출판 순서가 아니다. 원문의 결과를 재현한 것이 아니라 발표에 사용할 보고 근거를 선정했다. 명세와 카드가 충돌하면 아래 우선순위로 제작 전에 해결한다.

1. 정확한 버전의 원문 조건·표/그림.
2. 근거 카드의 비교 대상·단위·허용 결론.
3. 장별 명세의 좁은 주화면 선택.
4. 상위 스토리보드의 짧은 요약.

카드는 참고할 전체 비교를 보존할 수 있지만 주화면은 한 비교로 좁힌다. 부록 수치를 본문에 전부 넣지 않는다. 미해결 원고 오류를 임의 수정하지 않는다.

## 현재 페이지와 원본 번호의 구별

현재 덱은 **본문 S01–S47 + 근거 부록 S48–S80**이다. 이 표의 현재 페이지는 [조립 순서 명세](CAUSAL_DECK_ORDER.json)의 `number`, `origin`, `appendix`를 기준으로 갱신했다(2026-09-11).

- **P01–P27**: 문헌의 고정 ID.
- **O01–O78**: 재구성 전 [보존 원고](../slides/archive/visual-before-causal.md)의 원본 슬라이드 번호. 과거 근거 카드의 `[Sxx]`와 `result-xx`·`p2-sxx` 파일명은 이 원본 번호를 뜻한다.
- **현재 S01–S80**: 최종 덱에서 화면에 표시하는 페이지. 원본 O와 일치한다고 가정하지 않는다.
- 아래 문헌 표는 원본 근거 슬라이드를 유지한 현재 위치다. 여러 문헌을 종합한 신규 교육용 bridge의 위치는 별도 표에 기록했다. 삭제된 도입·전환 개념장은 보존 원고에 남는다. 새 정량 근거인 S35는 TWNM 행에도 표시했다.

| ID | 문헌 | 원본 슬라이드 O | 현재 본문 S | 현재 근거 부록 S | 고유 역할·주 결과 |
| --- | --- | --- | --- | --- | --- |
| P01 | Neural-SRP | O10–O11 | S12–S13 | — | 쌍별 학습 위치 응답; Table I Recorded4 |
| P02 | AGG-RL | O04–O05·O07·O12–O14 | S04–S05 | S49–S51 | 물리 문제/배열·격자 정합; Table 3 Dynamic-U, 같은 모델 AGG 유무 |
| P03 | MC-SimCLR | O18–O19 | S19 | — | 반복 관측 대조; Table 1 LP 사건/방향 |
| P04 | CCSR | O20–O21 | — | S56 | 가린 STFT 프레임 복원; Table III 8개 방 |
| P05 | SFD | O24–O25 | S20 | S55 | clean 특징 목표; Fig. 2 1h, 전체 미세조정 조건 |
| P06 | GRAM | O28–O30 | S18 | S57 | 복합 장면 표현; Fig. 3(A) DOA 판독 |
| P07 | LAM | O22–O23 | — | S54 | covariance를 설명하는 지도; LE/LR trade-off |
| P08 | AT2SELD | O26–O27 | — | S58–S59 | 의미·공간 결합 위치; Table 12 |
| P09 | ELSA | O32–O33 | S22 | S60 | 공간 문장 정렬; Table 2/A.T.7 Direction |
| P10 | SALM | O34–O35 | S23–S24 | — | 구조화 정렬 목표; Table 1 loss ablation |
| P11 | SelectTSL | O36–O37 | — | S61–S62 | 요청 목표 DOA/활성 수; Table VI |
| P12 | BAT | O38–O39 | — | S76 | 질문별 공간 답변; Table 4 audio/prompt |
| P13 | DSpAST | O40–O41 | S36–S37 | — | 과제별 특징 읽기; Table 3 matched interface |
| P14 | OWL | O42–O44 | S38–S39 | S68 | 학습 때 기하 지도; Table 5 |
| P15 | PhaseCoder | O47–O48 | S40 | S67 | 배열+좌표의 언어 연결; v2 Table3 공간 QA·목표 화자 전사 |
| P16 | Dual-BEATs | O45–O46 | — | S65–S66 | 전처리와 레벨 단서; Table 1 dither |
| P17 | Sci-Phi | O50–O52 | S26 | S69–S70 | 음원별 속성 묶음; Fig. 2 TupleScore |
| P18 | Spatial-Omni | O53–O55 | S31–S32 | — | 과제별 공간 토큰; v2 Table 2 zero-spatial |
| P19 | The World is Not Mono | O56–O58 | S29·S34·S35(신규) | S71 | source-slot 지도와 dense 입력·복합 질의; v3 Table5 SAPO + 신규 Table15 보고 Overall |
| P20 | Spatial Audio Motion Understanding and Reasoning | O59–O60 | — | S72·S74 | 시간 속성→JSON→LLM; Table 3 |
| P21 | Spatial Audio Question Answering and Reasoning on Dynamic Source Movements | O59·O61 | — | S72·S75 | 질문 관련 구간; Table 3 mask 비교 |
| P22 | ST-AudioLM | O62–O64 | S27–S28 | S73 | 시간별 의미·궤적; Table 5 조합 QA |
| P23 | CoSTALA | O65–O66 | — | S63–S64 | 사건 순서/위치 정렬; Table 2 retrieval |
| P24 | STAR-Bench | O67–O69 | S42 | S77 | 질문·모델 답변의 시험; Table 2 AA |
| P25 | WearVox | O67·O70–O71 | S45 | S78 | 실제 응답 대상 판단; Table 4 side-talk |
| P26 | SARL | O67·O72–O73 | S21 | S79 | 고정 표현 접근성; Fig. 2/3 정의 구별 |
| P27 | BMLD/간섭 단서 연구 | O67·O74–O76 | S43–S44 | S80 | 통제 자극·거리 반응; Table 1/Fig. 3 |

## 결과 해석에 공통으로 붙일 조건

- 입력: 원시 배열 / binaural / FOA / amplitude-panned stereo / beamformed signal을 구별한다. 좌표와 depth가 각각 추론 입력인지 학습 지도인지 표시한다.
- 갱신 범위: frozen encoder는 판독기까지 무학습이라는 뜻이 아니다. 전체 미세조정과 모듈 적응을 따로 쓴다.
- 데이터: 완전 합성 / 측정 RIR 기반 합성 / 현장 혼합음 녹음을 구별한다. ‘새 방’과 ‘새 음원 정체성’과 ‘새 배열’은 다른 split이다.
- 지표: 각도·위치 오차, 검출률, QA 정확도, Recall@K, 정규화 접근성, 임베딩 거리비를 합산하거나 공통 점수처럼 그리지 않는다.
- 결론: 시스템 비교와 단일 요소 ablation을 구별한다. 미보고는 실패가 아니며, 한 조건의 성공은 보편적 해결이 아니다.

## 제작·검증 기록의 확인 위치

선택한 그림의 취득·크롭·출처는 ASSETS_PART1–3과 [자산 출처](../ASSET_SOURCES.md), 모듈 검증과 신규 bridge의 범위는 [LLM 모듈 근거](CAUSAL_LLM_MODULES.md)에 기록했다. 최종 PDF/PPTX의 렌더 검수 상태는 해당 산출 검수 기록과 함께 확인한다. SFD Table 2, SelectTSL Table III 등 원문 충돌의 처리 상태는 [레드팀 보고](REDTEAM_REVIEW.md)에 모았다. 이 인덱스는 원문 버전 변경을 자동 추적하지 않는다.

IPDnet과 GCC/SRP는 설명용 기준이며 이 27편에 중복 계수하지 않는다. 선택적 시청각·생성·과제 확장은 본문 범위 밖에 유지한다.

## 연결 설명의 현재 위치

| 현재 페이지 | Bridge 원고 | 역할 |
| --- | --- | --- |
| S07 (본문) | [gcc-phat](../slides/bridges/gcc-phat.md) | GCC-PHAT: 두 신호에서 시간차를 찾는다 |
| S08 (본문) | [tdoa-locus](../slides/bridges/tdoa-locus.md) | 지연 하나에 대응하는 좌표는 여러 개다 |
| S09 (본문) | [srp-candidate](../slides/bridges/srp-candidate.md) | 후보 좌표가 예측한 지연에서 상관값을 읽는다 |
| S10 (본문) | [srp-sum](../slides/bridges/srp-sum.md) | 쌍별 응답을 합하고 가장 높은 좌표를 고른다 |
| S11 (본문) | [srp-neural](../slides/bridges/srp-neural.md) | Neural-SRP: 쌍별 공간 응답을 학습한다 |
| S14 (본문) | [readout-to-encoder](../slides/bridges/readout-to-encoder.md) | 좌표 다음에 무엇을 전달해야 하는가? |
| S15 (본문) | [audio-llm-contract](../slides/bridges/audio-llm-contract.md) | 오디오 표현은 어떻게 LLM의 입력이 되는가 |
| S16 (본문) | [encoder-criteria](../slides/bridges/encoder-criteria.md) | LLM 전에 무엇이 읽혀야 하는가? |
| S17 (본문) | [encoder-objectives](../slides/bridges/encoder-objectives.md) | 학습 과제는 어떤 관계를 남기게 하는가? |
| S25 (본문) | [token-bottleneck](../slides/bridges/token-bottleneck.md) | 시간 평균은 서로 다른 이동을 같게 만들 수 있다 |
| S30 (본문) | [adapter-training](../slides/bridges/adapter-training.md) | 연결 정렬과 언어 적응은 다른 학습 단계다 |
| S33 (본문) | [lora-reading](../slides/bridges/lora-reading.md) | LoRA는 LLM의 입력 처리 방식을 조정한다 |
| S35 (본문) | [module-evidence](../slides/bridges/module-evidence.md) | 토큰을 결합하는 설계에 따라 결과가 달라졌다 |
| S41 (본문) | [causal-evaluation](../slides/bridges/causal-evaluation.md) | 읽히는 정보가 답에도 쓰이는가? |
| S46 (본문) | [synthesis](../slides/bridges/synthesis.md) | 보존·전달·사용은 각각 확인해야 한다 |
| S47 (본문) | [closing-tests](../slides/bridges/closing-tests.md) | 같은 장면에서 표현·토큰·답을 함께 검사한다 |
| S48 (부록) | [appendix-index](../slides/bridges/appendix-index.md) | 근거 부록 |

현재 bridge 원고는 17장이다. 이전 `roadmap`은 비활성이고 GCC-PHAT·같은 지연의 위치·후보 점수·쌍 합산 네 장이 기초 설명을 맡는다. 활성 causal 자산 12개와 새 GCC/SRP 계산 자산 4개를 구분한다. 부록 목차는 별도 설명 이미지를 추가하지 않는다.

## 전체 페이지의 원본 대응

| 현재 페이지 | 구분 | 원본 또는 bridge |
| --- | --- | --- |
| S01 | 본문 | O01 |
| S02 | 본문 | O02 |
| S03 | 본문 | O03 |
| S04 | 본문 | O04 |
| S05 | 본문 | O05 |
| S06 | 본문 | O06 |
| S07 | 본문 | 연결 설명 `gcc-phat` |
| S08 | 본문 | 연결 설명 `tdoa-locus` |
| S09 | 본문 | 연결 설명 `srp-candidate` |
| S10 | 본문 | 연결 설명 `srp-sum` |
| S11 | 본문 | 연결 설명 `srp-neural` |
| S12 | 본문 | O10 |
| S13 | 본문 | O11 |
| S14 | 본문 | 연결 설명 `readout-to-encoder` |
| S15 | 본문 | 연결 설명 `audio-llm-contract` |
| S16 | 본문 | 연결 설명 `encoder-criteria` |
| S17 | 본문 | 연결 설명 `encoder-objectives` |
| S18 | 본문 | O29 |
| S19 | 본문 | O19 |
| S20 | 본문 | O25 |
| S21 | 본문 | O73 |
| S22 | 본문 | O32 |
| S23 | 본문 | O34 |
| S24 | 본문 | O35 |
| S25 | 본문 | 연결 설명 `token-bottleneck` |
| S26 | 본문 | O51 |
| S27 | 본문 | O63 |
| S28 | 본문 | O64 |
| S29 | 본문 | O57 |
| S30 | 본문 | 연결 설명 `adapter-training` |
| S31 | 본문 | O54 |
| S32 | 본문 | O55 |
| S33 | 본문 | 연결 설명 `lora-reading` |
| S34 | 본문 | O58 |
| S35 | 본문 | 연결 설명 `module-evidence` |
| S36 | 본문 | O40 |
| S37 | 본문 | O41 |
| S38 | 본문 | O43 |
| S39 | 본문 | O44 |
| S40 | 본문 | O48 |
| S41 | 본문 | 연결 설명 `causal-evaluation` |
| S42 | 본문 | O68 |
| S43 | 본문 | O74 |
| S44 | 본문 | O75 |
| S45 | 본문 | O71 |
| S46 | 본문 | 연결 설명 `synthesis` |
| S47 | 본문 | 연결 설명 `closing-tests` |
| S48 | 부록 | 연결 설명 `appendix-index` |
| S49 | 부록 | O12 |
| S50 | 부록 | O13 |
| S51 | 부록 | O14 |
| S52 | 부록 | O16 |
| S53 | 부록 | O15 |
| S54 | 부록 | O23 |
| S55 | 부록 | O24 |
| S56 | 부록 | O21 |
| S57 | 부록 | O30 |
| S58 | 부록 | O26 |
| S59 | 부록 | O27 |
| S60 | 부록 | O33 |
| S61 | 부록 | O36 |
| S62 | 부록 | O37 |
| S63 | 부록 | O65 |
| S64 | 부록 | O66 |
| S65 | 부록 | O45 |
| S66 | 부록 | O46 |
| S67 | 부록 | O47 |
| S68 | 부록 | O42 |
| S69 | 부록 | O50 |
| S70 | 부록 | O52 |
| S71 | 부록 | O56 |
| S72 | 부록 | O59 |
| S73 | 부록 | O62 |
| S74 | 부록 | O60 |
| S75 | 부록 | O61 |
| S76 | 부록 | O39 |
| S77 | 부록 | O69 |
| S78 | 부록 | O70 |
| S79 | 부록 | O72 |
| S80 | 부록 | O76 |

현재 원본 그대로 대응하지 않는 개념장: O07·O08·O09·O17·O18·O20·O22·O28·O31·O38·O49·O53·O67·O77·O78. 내용·이전 근거는 보존 원고에 남는다. 원본 O09의 SRP 설명은 현재 S09–S10에서 계산 단계로 풀어 쓴다.

## 수치 출처: 기존99개와 신규3개

기존23개 result 그래프의 **99개 값**은 [원래 표 데이터](RESULTS_VISUAL_DATA.json)와 지정 버전의 표를 그대로 유지했다. 파일명 `result-NN`의 NN은 현재 페이지가 아니라 원본 O번호다. 예를 들어 원본 O46의 dither 그래프는 현재 S66, 원본 O76의 단서 제거 그래프는 현재 S80이다.

현재 **S35**의 TWNM projector 비교는 새로 추가한 **3개 보고값**이다. [TWNM v3 Appendix G.1 Table15](https://arxiv.org/html/2601.02954v3)의 `P0: Single MLP` 39.20%, `P1: Dual Tower` 46.40%, `P2: Dense Hybrid` 52.10%를 Overall 열에서 전사했다. 기존99개를 수정하거나 이 세 값과 합산한 종합 점수를 만들지 않았다.

Table15는 최종 SAPO 이전 **semantic-answer judge** 진단이다. 현재 S34의 Table5 **exact MCQA**와 다른 채점이다. 원문 §F.6의 Gemini 3 Flash judge는 질문·선지·gold option text·생성 답변만 보고, 오디오·RTSD를 받지 않는다. 저자는 projector ablation이라고 명명하지만 P0/P1/P2의 encoder/LLM checkpoint, 학습 예산 및 seed가 완전히 동일하다는 별도 명시는 없다. 따라서 연결 설계별 보고 결과로 한정한다.

Table15 caption은 Overall이 ASA1,000항목을 센다고 설명하지만, App.D.3의 수준별 수385/279/336으로 수준별 백분율을 가중하면39.4523/46.7759/52.4109로 보고 Overall과 일치하지 않는다. 이 산술 불일치를 임의 수정하지 않았고, **분모별 정답 수를 재구성하지 않은 원문 보고 Overall**로 사용한다. 세 수준의 단순평균도 아니다. 상세 확인은 [LLM 모듈 근거 §7](CAUSAL_LLM_MODULES.md)을 참조한다.

## GCC/SRP 교육용 계산의 출처

S07–S10은 같은 합성 장면과 기하를 사용한다. S07의 실제 GCC-PHAT 곡선을 후보 좌표의 기대 지연으로 조회해 S08–S10의 쌍 응답과 합산 지도로 연결한다. 원자료는 `public/diagrams/gcc-phat.source.json`, `localization-*.source.json` 및 `localization-simulation.npz`에 보존한다. 이 계산 예는 기존99개·TWNM3개의 논문 보고값 집합에 포함하지 않는다. 계산·그림의 생성 조건은 [자산 출처](../ASSET_SOURCES.md)를 따른다.
