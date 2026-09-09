# 근거 대장 — P24–P27

[전체 인덱스](EVIDENCE_LEDGER.md) · [S67–S78 명세](BLUEPRINT_PART3.md)

### P24. STAR-Bench: Probing Deep Spatio-Temporal Reasoning as Audio 4D Intelligence

- 채택 버전·원문 링크: [arXiv v2](https://arxiv.org/html/2510.24693v2), [ICLR 2026 학회본](https://openreview.net/pdf?id=Ts6j3GoZDE). 아래 선택은 v2 표 번호이며 자산은 학회본과 대조한다.
- 본문 위치: S67–S69.
- 고유 문제·그림 역할: Fig. 1은 audio/caption의 문제, Fig. 2는 과제 예시. 캡션 정보 보존의 문제와 공간 지각 점수를 구별한다.
- 본문 결과: Table 2 Gemini 2.5 Pro / Random Guess의 Localization·Relation·Trajectory 열. 모델 AA=40.87/48.97/45.28%, 우연 기준은 각 33.33%. 본 표는 audio/caption ablation 표가 아니다.
- 비교 조건: 19모델의 MCQA 보고 중 한 모델을 택한다. Gemini는 2025년 6월 업데이트 조건이다. AA는 반복 prompt 변형 실행 평균, ACR는 모든 실행 정답 비율. MA/OA는 집계 방식으로 AA/ACR와 다른 축이다.
- 허용 결론: 시험한 버전은 이 벤치마크의 공간 질문에서 제한된 점수를 보였다. 같은 과제의 우연 기준을 함께 읽어야 한다.
- 금지 해석·미해결: 최신 2026 모델 모두의 실패나 위상 처리 기전을 입증하지 않는다. 모델별 채널 처리·질문 형식 적합성의 차이가 있다. BAT의 0점에서 지각 정보 부재를 단정하지 않는다. 캡션 비교는 특정 음향 단서를 고립한 통제가 아니다.

### P25. WearVox: An Egocentric Multichannel Voice Assistant Benchmark for Wearables

- 채택 버전·원문 링크: [arXiv v1](https://arxiv.org/html/2601.02391v1), [ICLR 2026 학회본](https://openreview.net/pdf?id=QpaNErg7ug).
- 본문 위치: S67, S70–S71.
- 고유 문제·그림 역할: Fig. 1의 side-talk rejection 문제만 채택한다. Fig. 2는 실제 SC/MC 입력 경로다.
- 본문 결과: Table 4 SC Wearllama 대 MC Wearllama, Side Talk Rejection 정확도 85.4%→93.9%. 다른 과제의 성과는 이 발표의 주장이 아니다.
- 비교 조건: SC는 beamformed channel만, MC는 channel 0과 beamformed channel을 interleave한다. frozen speech encoder와 학습 projection/LLM 구성을 사용한다. 실측 RIR을 활용한 합성 다채널 학습과 실제 착용자 WearVox 시험을 구별한다.
- 허용 결론: 이 추가 채널·시스템 학습 조건은 실제 side-talk 판단에서 이득을 보고했다.
- 금지 해석·미해결: 모든 원시 마이크 채널 입력이나 순수 위상 효과로 그리지 않는다. SNR·beamforming·학습 조건이 함께 바뀐다. 서론 85.6과 Table 4 85.4의 불일치는 표 기준으로 처리한다. 앞 공간 LLM 전체의 실녹음 전이 검증도 아니다.

### P26. Probing Spatial Structure in Pretrained Audio Representations — SARL

- 채택 버전·원문 링크: [arXiv 2606.05544v2](https://arxiv.org/html/2606.05544v2).
- 본문 위치: S67, S72–S73.
- 고유 문제·그림 역할: §3 실험 프로토콜과 Table 1 시험 인코더 목록을 바탕으로 고정 표현 판독을 설명한다. Fig. 2는 접근성 결과, Fig. 3은 perturbation 민감도 결과다.
- 본문 결과: Fig. 2의 사건 의미 / 위치(방위·고도·거리 평균) / 방 특성(RT60·부피·형상 평균) 세 그룹을 주근거로 선정한다. source 전체를 위치로 묶지 않는다. Fig. 3은 민감도 정의를 대비하는 부록이다. 정규화 축을 유지하고 비슷한 막대를 정밀 순위 수치로 다시 쓰지 않는다.
- 비교 조건: 단일 음원 10초 합성, 모델별 native 전처리→frozen encoder→mean pooling→20epoch linear classifier. source·RIR/room을 구성한 분할 내에서 분리한다. source/room 과제군의 생성 파이프라인이 다르다. 연속량은 구간화·soft label 후 1−MAE/R, 범주는 macro-F1; 무작위 기준 b 대비 (x−b)/(1−b)로 정규화한다.
- 허용 결론: 해당 pooling·판독 조건에서 정보 접근성이 요인과 모델에 따라 다르며 단순한 입력 민감도와 같지 않다.
- 금지 해석·미해결: 낮은 선형 점수는 원표현 정보 부재가 아니다. 입력·학습 데이터가 달라 목표 하나의 인과 비교가 아니다. Table 1에는 A-MAE; SELD-S/EnCodec/SR-VAE; BANC/GRAM-B/S-AST/SFD/W-JEPA; AVSA/EINv2/SELD-F/GRAM-F가 있으며 앞 모든 LLM을 시험한 것이 아니다.

### P27. Spectro-Temporal Interference Confounds Phase Encoding in Spatial Audio Foundation Models

- 채택 버전·원문 링크: [arXiv 2606.14820v1](https://arxiv.org/html/2606.14820v1).
- 본문 위치: S67, S74–S76.
- 고유 문제·그림 역할: §2의 N0/S0N0/SπN0 자극을 재구성한다. 인간 역치와 고정 임베딩 거리비를 먼저 구별한다. Fig. 1은 조건별 반응, Fig. 3은 파형 ablation이다.
- 본문 결과: Table 1의 500Hz·−14dB, Spatial-AST 6.8 / DSpAST 7.0 / GRAM-T 2.1 / WavJEPA 0.5 dB. 이어 Fig. 3의 원신호·고역통과·대역에너지 조정·vocoder 조건, GRAM-T 대표 행. Vocoded 75%는 unmasking50%+reversal25%로 읽는다.
- 비교 조건: 동일 noise seed, 고정 인코더 final-block mean pooling과 모델별 전처리. 지표는 20log10[d(antiphase,noise)/d(diotic,noise)]. 선택한 네 값의 유의성 별표와 검정 각주를 보존한다. Table 1의 반복 자극 검정과 Fig. 3의 20 frequency×SNR cell 중 유의 비율은 다른 집계다. 왼쪽만 사용하는 mono 대조군은 입력 동일성 때문에 0이다.
- 허용 결론: 이 표현·자극 조건에서 위상 변경과 연관된 거리 반응이 있고, 파형 변형 실험은 간섭 단서 등 대안 설명을 고려하게 한다.
- 금지 해석·미해결: 인간 청취 역치, QA 정확도, 모델 내부 위상 기전의 단독 증거가 아니다. 표적 phase flip은 오른쪽 혼합의 파형·간섭 구조도 바꾼다. ‘전혀 phase가 없다’는 반대 단정도 피한다. EC 기준은 인간 실측치가 아니며 더 많은 채널/현실 장면/LLM 일반화는 미검증이다.
