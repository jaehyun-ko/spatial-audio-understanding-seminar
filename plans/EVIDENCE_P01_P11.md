# 본문 근거 대장 P01–P11

기준일: 2026-09-09. 슬라이드 번호는 확장 발표의 새 순서다. P 번호는 문헌 식별자이므로 발표 순서와 다르다. 이 문서는 제작용 근거 설계이며 그림 취득·크롭·슬라이드 렌더 검증 완료를 뜻하지 않는다.

공통 원칙: 한 논문의 결과를 다른 논문의 숫자와 통합 순위로 만들지 않는다. 입력, 사전학습 목표, downstream에서 갱신한 부분, 평가 데이터와 지표를 함께 표시한다. 그림의 정성적 예시와 정량 성능을 구별한다. 아래에 정밀 수치를 적지 않은 그래프는 원문 패널·곡선을 그대로 사용하고 눈대중 수치를 만들지 않는다.

### P01. The Neural-SRP method for positional sound source localization

- 채택 버전·원문 링크: [arXiv 2403.09455v1](https://arxiv.org/html/2403.09455v1). 이 버전의 Fig. 1·3 및 Table I를 한 묶음으로 사용한다.
- 본문 위치: S10–11.
- 고유 문제·그림 역할: S10의 Fig. 1은 잔향 관측에서 SRP와 NeuralSRP+가 만든 위치 응답의 정성적 비교다. 쌍별 격자 예측과 합산 방법은 S10–11의 구두 설명에 최소한으로 남긴다. Fig. 3 전체 구조와 Fig. 4의 쌍별 쌍곡선 목표는 부록이다.
- 본문 결과: S11은 Table I의 Recorded4 한 조건에서 SRP 1.19 m와 NeuralSRP+ 0.77 m를 주비교로 사용한다. Recorded6는 부록이다. 아래 표는 부록 수치까지 보존한 근거 요약이며 전체를 본문에 넣지 않는다.

  | 평가 | SRP | NeuralSRP+ |
  | --- | ---: | ---: |
  | Recorded4 | 1.19 m | 0.77 m |
  | Recorded6 | 0.75 m | 0.56 m |

- 비교 조건: 단일 정지 음성, 0.5초 입력. 입력은 쌍별 STFT 위상·마이크 절대좌표·방 크기다. 후보 좌표는 학습 목표 구성에 쓰며 추론 입력이 아니다. Recorded는 잔향시간 800 ms인 한 방의 녹음으로 학습 250개·시험 2,500개다. `+`는 합성 학습 뒤 Recorded로 추가 학습한 모델이다.
- 허용 결론: 해당 실녹음 적응 조건에서 쌍별 학습·합산 모델이 SRP보다 평균 위치 오차가 작다.
- 금지 해석·미해결: 실녹음 zero-shot 전이, 다중 음원 검증, 각도 오차로 해석하지 않는다. 본문 상대개선율은 표 원수치의 통상적 감소율과 달라 사용하지 않는다. CRNN 비교는 입력·학습 목표도 달라 단일 설계 요소의 ablation이 아니다.

### P02. Physics-Informed Audio-Geometry-Grid Representation Learning for Universal Sound Source Localization

- 채택 버전·원문 링크: [ICLR 2026 출판본](https://proceedings.iclr.cc/paper_files/paper/2026/file/ee860a9fa65a55a335754c557a5211de-Paper-Conference.pdf). 표 번호는 이 출판본 기준이다.
- 본문 위치: S4–5, S7, S12–14.
- 고유 문제·그림 역할: Fig. 1(a)(b)는 경로 차이·위상 감김의 물리적 문제를 설명한다. S7의 배열 변경은 §2.2 기반 설명 장면이다. S12에서 배열 기하와 후보 DOA 목록을 구별하고, S13 Fig. 2에서 오디오·기하 표현과 후보 격자 표현의 정합을 설명한다.
- 본문 결과: S14는 Table 2의 조건을 붙인 Table 3의 Dynamic-U만 사용한다. Neural-SRP와 Neural-SRP `with AGG-RL` 두 행에서 MAE 21.18°·19.05° 및 ACC10 45.51%·54.13%를 비교한다. Dynamic-S의 비개선은 본문 한계 주석에 남기되 그 수치, Proposed 전체 시스템, Table 4 격자 수 결과는 부록으로 보낸다. 아래 표는 부록 수치까지 보존한 근거 요약이다.

  | 모델 | Dynamic-S MAE / ACC10 | Dynamic-U MAE / ACC10 |
  | --- | --- | --- |
  | Neural-SRP | 19.60° / 52.32% | 21.18° / 45.51% |
  | Neural-SRP with AGG-RL | 19.79° / 50.56% | 19.05° / 54.13% |
  | Proposed | 10.32° / 77.34% | 14.12° / 63.17% |

- 비교 조건: Dynamic-S는 학습에 노출된 채널 수 4–12, Dynamic-U는 미노출 13–16의 합성 배열 조건이다. `Dynamic`을 움직이는 음원으로 풀지 않는다. 평가 음성 TIMIT·잡음 ESC-50, 최대 두 정지 화자다. DNN의 학습 프로토콜을 맞췄지만 입력 특징·구조는 다르다. MAE는 각도 오차, ACC10는 10° 이내 비율이다. 원표 ±는 MAE의 95% CI다.
- 허용 결론: 후보 격자 정합을 붙인 Neural-SRP는 이 미노출 채널 수 조건에서 MAE와 ACC10가 개선되었다. 학습에 노출된 채널 수 조건에서는 같은 개선이 나타나지 않았다는 한계를 함께 말한다. 전체 제안 시스템의 성과는 부록의 별도 비교에 한정한다.
- 금지 해석·미해결: Dynamic-S에서는 결합만으로 개선되지 않는다. 전체 Proposed와 기준선 차이를 AGG-RL 하나의 인과 효과로 귀속하지 않는다. 모든 배열·환경의 보장이나 범용 frozen 표현 재사용의 증거로 쓰지 않는다. 격자 수 변화는 Table 4의 별도 질문으로 부록에 둔다.

### P03. Exploring Self-Supervised Contrastive Learning of Spatial Sound Event Representation

- 채택 버전·원문 링크: [MC-SimCLR, arXiv 2309.15938v1](https://arxiv.org/html/2309.15938v1).
- 본문 위치: S18–19.
- 고유 문제·그림 역할: Fig. 1의 같은 다채널 녹음에서 뽑은 시간 구간을 양성 쌍으로 쓰는 과제를 먼저 보여준다. 정지 음원 가정 아래 사건·공간 정보의 일관성을 학습한다. S19는 DOA만이 아니라 사건 분류와 방향 판독을 회수한다.
- 본문 결과: S19는 Table 1의 LP에서 Random(no-pretrain)과 MC-SimCLR w/o DA 두 행, 사건 정확도와 방위각 오차 두 열만 사용한다. 각각 23.6%·83.1°와 33.0%·13.2°다. FT와 전체 augmentation 조합은 부록으로 보낸다. 아래 표는 부록 수치까지 보존한 근거 요약이며 전체를 본문에 넣지 않는다.

  | 학습 | LP 정확도 / 방위각 오차 | FT 정확도 / 방위각 오차 |
  | --- | --- | --- |
  | Random | 23.6% / 83.1° | 43.7% / 11.8° |
  | MC-SimCLR w/o DA | 33.0% / 13.2° | 45.6% / 11.4° |
  | +CS+MU+RRC+CD | 51.5% / 10.1° | 53.4% / 8.7° |

- 비교 조건: FSDnoisy18k 기반 합성, 지름 10 cm의 4마이크 원형 배열, 정지·비중첩 사건. 38.8시간 noisy split으로 사전학습하고 clean split의 라벨로 평가 모델을 학습한다. LP는 인코더 고정 후 두 선형 판독기를 각각 학습한다. FT는 인코더와 두 판독기를 갱신한다.
- 허용 결론: 이 데이터의 고정 인코더 선형 판독에서는 추가 augmentation이 없는 대조 사전학습 뒤 사건 정확도가 높아지고 방향 오차가 낮아졌다. FT에 관한 결론은 부록의 별도 비교에서만 말한다.
- 금지 해석·미해결: 모든 augmentation이 모든 지표를 단조 개선한다고 말하지 않는다. MU를 뺀 조합은 방향 오차가 LP 9.4°·FT 8.6°로 더 낮다. 이동·중첩 음원 또는 새 배열 재사용으로 확장하지 않는다.

### P04. Self-Supervised Learning of Spatial Acoustic Representation with Cross-Channel Signal Reconstruction and Multi-Channel Conformer

- 채택 버전·원문 링크: [CCSR, arXiv 2312.00476v2](https://arxiv.org/html/2312.00476v2).
- 본문 위치: S20–21.
- 고유 문제·그림 역할: Fig. 1에서 한 채널의 가린 STFT 프레임을 복원하려면 다른 프레임에서의 채널 관계와 보이는 채널의 내용이 필요함을 설명한다. 전체 미관측 채널을 생성하는 과제로 그리지 않는다. 구조의 세부 층은 부록으로 둔다.
- 본문 결과: S21은 Table III의 학습 방 8개 조건에서 Supervised scratch와 Pre-train + fine-tune 두 행의 TDOA MAE만 주표로 비교한다. 0.40 samples와 0.28 samples다. C50 MAE가 1.14 dB에서 1.21 dB로 증가한 반례는 본문 각주에 남긴다. frozen·Non-informative 행과 T60 결과는 부록이다. 아래 표는 부록 수치까지 보존한 근거 요약이다.

  | 학습 설정 | TDOA MAE, samples | T60 MAE, s | C50 MAE, dB |
  | --- | ---: | ---: | ---: |
  | Non-informative | 2.98 | 0.287 | 4.90 |
  | Supervised scratch | 0.40 | 0.069 | 1.14 |
  | Pre-train + linear evaluation | 1.49 | 0.083 | 1.57 |
  | Pre-train + fine-tune | 0.28 | 0.050 | 1.21 |

- 비교 조건: 두 마이크의 복소 STFT, 단일 정지 음성, 합성 잔향과 SNR 15–30 dB. downstream 학습 8개 방, 검증·시험 각각 20개 방을 분리하며 8개 방 설정은 4회 평균이다. LP는 인코더 고정, FT는 전체 downstream 모델 갱신이다.
- 허용 결론: 이 조건에서 복원 사전학습 후 전체 미세조정은 처음부터 학습한 모델보다 TDOA 오차를 줄였지만 C50는 개선하지 못했다. 고정 표현의 정보 접근성과 방 특성 판독은 부록의 별도 결과로 한정한다.
- 금지 해석·미해결: 복원 오차를 downstream 성능으로 대신하지 않는다. 고정 표현이 완전 지도학습보다 우수하거나 모든 과제가 개선된다고 말하지 않는다. CCSR도 잡음·잔향을 다루므로 다음 SFD를 소개할 때 이를 없는 조건으로 만들지 않는다.

### P05. Learning Robust Spatial Representations from Binaural Audio through Feature Distillation

- 채택 버전·원문 링크: [SFD, arXiv 2508.20914v1](https://arxiv.org/html/2508.20914v1), 2025-08-28 공개. [WASPAA 2025 출판 확인](https://vbn.aau.dk/en/publications/learning-robust-spatial-representations-from-binaural-audio-throu-2/). 아래 그래프는 v1 기준이다.
- 본문 위치: S24–25.
- 고유 문제·그림 역할: Fig. 1에서 noisy/reverberant STFT 입력과 깨끗한 비잔향 바이노럴 신호에서 계산한 특징 목표를 대비한다. GCC, GCC-PHAT, CPSPhase, ILD+IPD는 별도 모델 변형이다. 별도 학습된 teacher network로 그리지 않는다.
- 본문 결과: S25는 Fig. 2의 `1h` 패널만 사용한다. STFT-DNN과 SFD-CPSPhase를 주비교로 읽는다. x축 SNR, y축 DOA MAE(°), 1h는 라벨을 사용하는 미세조정 데이터 양이다. `10min` 패널과 SFD-GCC-PHAT 변형은 부록이다. 원패널의 나머지 곡선은 범례를 유지하며 비강조 처리하고 정밀 수치를 추정해 쓰지 않는다.
- 비교 조건: 본문 두 모델은 STFT 입력·545k 파라미터와 1시간의 라벨 학습량을 공유한다. SFD는 960시간 LibriSpeech 원음 기반 사전학습 후 인코더와 DOA head를 미세조정한다. 단일 정지 음성·합성 바이노럴이고 HRTF 피험자를 분리한다. 평가 잡음은 학습과 같은 종류의 다른 클립이다.
- 허용 결론: 해당 저라벨·잡음 조건에서 특징 증류 사전학습은 DOA 미세조정에 도움이 된다.
- 금지 해석·미해결: 10분만으로 전체 모델을 학습했다거나 frozen 범용 표현을 검증했다고 말하지 않는다. clean 신호가 필요하다. Fig. 2 패널의 y축 범위가 다르다. Table 2 caption은 1h, §5.1은 10h로 PDF에서도 충돌하므로 시간 조건이 붙은 Table 2 수치 사용은 출판본 대조 전 보류한다. 결론과 본문 개선율도 그대로 복사하지 않는다.

### P06. GRAM: Spatial general-purpose audio representations for real-world environments

- 채택 버전·원문 링크: [arXiv 2506.00934v5](https://arxiv.org/html/2506.00934v5). 철회된 중복 ID 2602.03307을 출처로 쓰지 않는다.
- 본문 위치: S28–30.
- 고유 문제·그림 역할: S28은 Fig. 1의 자연스러운 복합 장면·과제 부분으로 기존 clean audio 학습과 실제 장면의 차이를 설명한다. S29는 같은 Fig. 1의 마스킹 학습·판독 경로만 사용한다. 그림을 전체 복제하기보다 역할별 크롭을 사용한다.
- 본문 결과: S30은 Fig. 3(A)의 DOA error boxplot만 사용한다. GRAM-Ambisonics와 Spatial-AST의 해당 분포를 주비교로 읽고 원범례의 모델·데이터 조건을 유지한다. 중앙선은 median, 상자는 사분위 범위이므로 평균 막대로 바꾸지 않는다. Fig. 3(B) T60, Fig. 5 STARSS23 validation 곡선, Table 1 NatHEAR 일반 과제는 모두 부록이다.
- 비교 조건: Fig. 3은 SC-5 음성과 ESC-50 환경음을 공간화한 합성 자연 장면의 판독이다. HEAR 방식 평가는 고정 인코더와 라벨로 학습한 판독기를 사용한다. 모델별 원래 입력 형식과 전처리 차이를 표시하며 동일 입력 ablation으로 부르지 않는다. 부록 Fig. 5에서는 pretrained fine-tuning·scratch·direct transfer를 따로 표시한다.
- 허용 결론: 합성 자연 장면에서 고정된 공간 표현으로 방향을 판독한 성과를 확인할 수 있다. 방 음향 판독과 실제 녹음 미세조정에 관한 결론은 각 부록 결과를 제시할 때만 말한다.
- 금지 해석·미해결: direct transfer를 라벨 없는 zero-shot으로 부르지 않는다. Table 2 전체를 실녹음으로 묶지 않는다. TAU-2019는 [측정 RIR 기반 합성 사건과 현장 잡음](https://dcase.community/challenge2019/task-sound-event-localization-and-detection)이다. 입력·학습 데이터가 다른 비교를 마스킹 목표 하나의 효과로 해석하지 않는다.

### P07. Latent Acoustic Mapping for Direction of Arrival Estimation: A Self-Supervised Approach

- 채택 버전·원문 링크: [LAM, arXiv 2507.07066v1](https://arxiv.org/html/2507.07066v1), 2025-07-08 공개.
- 본문 위치: S22–23.
- 고유 문제·그림 역할: Fig. 1의 음향지도 예시로 공간 정보를 어떤 중간 결과에 담는지 보여준다. Fig. 2는 관측 covariance를 잠재 음향지도와 알려진 steering matrix로 복원하는 학습 경로다. `정답 없이`는 위치 라벨 없는 복원 사전학습을 뜻한다.
- 본문 결과: S23은 Fig. 3에서 UpLAM+GRU-MHSA의 STARSS dev-test-sony 평가 곡선을 사용한다. x축은 Multi-ACCDOA detection threshold, 읽을 곡선은 같은 모델의 LE와 LR다. 기본 threshold 0.5의 녹색 세로선을 남긴다. threshold를 낮출 때 LR와 LE가 함께 높아지는 관계를 읽는다. validation 곡선을 시험 결과와 혼동하지 않는다. Table 2의 아래 모델 비교와 K-means 결과는 부록이다.

  | 모델 | LE | LR |
  | --- | ---: | ---: |
  | UpLAM + GRU-MHSA | 18.65° | 57.6% |
  | SELDnet, 4ch | 23.3° | 82.3% |

- 비교 조건: Eigenscape 실녹음 10시간과 SpatialScaper 합성 10시간으로 라벨 없는 CSM 복원을 학습한다. STARSS dev-test-sony 평가에서는 dev-train-tau/sony와 companion synthetic data로 지도 DOA 모델을 학습하고 dev-test-tau로 검증한다. UpLAM은 4채널 CSM을 32채널 CSM으로 올리는 학습된 변형이다. 지도학습 GRU-MHSA 판독과 K-means 판독을 혼용하지 않는다.
- 허용 결론: 같은 음향지도 판독 모델에서도 검출 threshold에 따라 위치 오차와 검출 범위의 상충이 나타난다.
- 금지 해석·미해결: Fig. 3을 두 모델 비교로 읽지 않는다. 새 임의 배열에 대한 무학습 적용, 범용 의미 표현, 모든 지표 우월성을 주장하지 않는다. validation에 LOCATA·RSoANU를 추가한 dagger 행은 다른 조건이므로 부록의 기본 조건 두 행과 섞지 않는다. 오차 감소만으로 성능 승리를 선언하지 않는다.

### P08. From General-Purpose Audio Tagging to Spatially Grounded Sound Event Localization and Detection

- 채택 버전·원문 링크: [arXiv 2606.27751v1 연구 보고서](https://arxiv.org/html/2606.27751v1), 2026-06-26 공개. 보고서 내부 명칭 AT2SELD를 사용한다.
- 본문 위치: S26–27.
- 고유 문제·그림 역할: Fig. 25에서 일반 오디오 태깅의 의미 표현을 어느 깊이에서 공간 경로와 결합할지 설명한다. 공간 단서를 처리하기 전의 결합과 높은 수준의 결합을 구별한다.
- 본문 결과: S27은 Table 12에서 no-stitch(cs00)와 late-only(cs01) 두 행의 Test SELD 0.708·0.624만 주비교로 사용한다. Table 11의 강한 dropout 조건을 표 위에 붙인다. 아래 네 설정·세 지표 표와 Fig. 40은 부록이다. Fig. 40의 metric delta를 별도 성능 근거로 중복 계산하지 않는다.

  | 결합 위치 | Test SELD | LE_CD | LR_CD |
  | --- | ---: | ---: | ---: |
  | 없음, cs00 | 0.708 | 14.55° | 0.050 |
  | late only, cs01 | 0.624 | 12.49° | 0.142 |
  | early only, cs10 | 0.715 | 13.15° | 0.050 |
  | early + late, cs11 | 0.705 | 13.18° | 0.058 |

- 비교 조건: STARSS23, FOA 공간 경로와 pretrained audio-tagging 의미 경로의 supervised SELD 적응. Stage 3의 강한 dropout을 공유한 설정끼리 비교한다. test는 best validation SELD checkpoint로 평가한다. 이 표를 frozen representation probe로 부르지 않는다.
- 허용 결론: 이 강한 정규화 설정 안에서는 late-only 결합의 Test SELD가 무결합보다 낮다. early 결합까지 포함한 일반화된 비교는 부록의 해당 행을 제시할 때만 말한다.
- 금지 해석·미해결: Stage 3 무결합 기준은 unregularized Stage 2보다 저하되어 있다. 따라서 이 비교만으로 pretrained semantic branch가 가장 좋은 공간 전용 시스템을 이겼다고 말하지 않는다. open-vocabulary SELD나 자유형 QA 모델로 분류하지 않는다.

### P09. Learning Spatially-Aware Language and Audio Embeddings

- 채택 버전·원문 링크: [ELSA, arXiv 2409.11369v1](https://arxiv.org/html/2409.11369v1), 2024-09-17 공개. [NeurIPS 2024 출판본](https://papers.neurips.cc/paper_files/paper/2024/file/3acc054949b6948d4444b35d412cab56-Paper-Conference.pdf)과 최종 자산·표 번호를 대조하는 제작 gate를 유지한다.
- 본문 위치: S32–33.
- 고유 문제·그림 역할: S32는 소리 의미와 공간 표현이 함께 맞아야 하는 검색 문제를 설명한다. Fig. 1(a)(b)는 FOA 공간화·공간 caption 생성, (c)는 오디오와 문장 표현 정렬이다. 구조도를 고유 문제 그림으로 대신하지 않는다.
- 본문 결과: S33은 Table 2의 ELSA `Direction (4-class)` 한 행만 사용한다. 합성 S-Clotho 92.0%·S-AC 92.8%와 실녹음 S-RWD 35.8%를 비교한다. Appendix Table A.T.7의 LAION-CLAP 비교는 부록이다. 아래 표의 CLAP 행은 부록 근거 보존용이며 본문 주표에 넣지 않는다.

  | 모델 | S-Clotho | S-AC | S-RWD |
  | --- | ---: | ---: | ---: |
  | ELSA | 92.0% | 92.8% | 35.8% |
  | LAION-CLAP | 28.2% | 29.3% | 27.3% |

- 비교 조건: 동일 모델의 방향 prompt 분류 정확도다. 학습된 audio/text embedding의 cosine similarity로 template 후보를 비교한다. S-Clotho/S-AC는 합성, S-RWD는 5개 방에서 녹음한 70개 sample의 작은 실녹음 세트다. ELSA 정렬 학습은 전체 구성요소를 갱신하며 spatial branch는 지도 공간 사전학습 초기화를 쓴다. 부록 비교에서 ELSA는 FOA·공간 특징, CLAP은 omni 채널만 받으므로 입력을 맞춘 ablation이 아니다.
- 허용 결론: 공간 언어 정렬의 방향 분류는 합성 데이터에서 작동하고, 이 작은 실녹음 세트에서는 큰 전이 차이가 남는다.
- 금지 해석·미해결: Table 2 자체에 baseline이 있다고 쓰지 않는다. 자유형 QA·언어 추론이나 연속 각도 회귀의 성과로 바꾸지 않는다. Table 1의 MLP DOA 회귀는 별도의 학습 프로토콜이다. 결과 자산 제작 전 v1과 출판본을 대조한다.

### P10. SALM: Spatial Audio Language Model with Structured Embeddings for Understanding and Editing

- 채택 버전·원문 링크: [arXiv 2507.16724v2](https://arxiv.org/html/2507.16724v2), 첫 공개 2025-07-22, v2 2025-09-18.
- 본문 위치: S34–35.
- 고유 문제·그림 역할: Fig. 1의 semantic/spatial branch와 원래 caption·공간 caption 대응을 사용한다. 의미와 공간 정보의 분리된 감독을 결합 표현과 함께 사용하는 이유를 질문한다.
- 본문 결과: Table 1의 동일 SALM 두 행, `L_sCL + L_DOA`와 `L_sCL + L_CL + L_DOA`를 비교한다. 본문은 sClotho의 T2A R@1·A2T R@1·Localization Error 세 열로 고정한다.

  | 손실 조건 | T2A R@1 | A2T R@1 | Localization Error |
  | --- | ---: | ---: | ---: |
  | L_sCL + L_DOA | 9.1% | 9.6% | 1.8° |
  | L_sCL + L_CL + L_DOA | 10.5% | 10.4% | 1.6° |

- 비교 조건: 합성 FOA sClotho 평가. semantic branch는 omni, spatial branch는 FOA 전체를 사용한다. CLAP semantic/text 및 PSELDNet DOA branch로 초기화하고 정렬·지도 DOA 목표로 학습한다. L_CL은 원래 caption과 semantic embedding의 대조 목표다. 위치 열은 지도 DOA loss로 학습한 MLP의 오차이며 zero-shot prompt 방향 분류와 다르다.
- 허용 결론: 같은 모델에서 의미 정렬 항을 함께 사용한 설정은 선택한 합성 평가의 검색과 위치 오차에서 더 좋다.
- 금지 해석·미해결: 분기가 통계적으로 완전히 독립되었다는 증명으로 쓰지 않는다. SALM-s와의 차이를 손실 하나의 효과로 섞지 않는다. Table 2의 측정 SRIR 합성을 현장 혼합음 녹음으로 부르지 않는다. editing은 임베딩 조작만 언급하고 파형 생성·편집 성과로 확장하지 않는다.

### P11. SelectTSL: Prompt-Guided Selective Target Sound Localization in Complex Scenarios

- 채택 버전·원문 링크: [arXiv 2607.02343v1](https://arxiv.org/html/2607.02343v1), 2026-07-02 프리프린트.
- 본문 위치: S36–37.
- 고유 문제·그림 역할: Fig. 1은 모든 활성 음원 위치와 요청한 목표만의 위치를 대비하는 문제 그림이다. Fig. 2는 prompt-conditioned selection과 IPD 기반 DOA·활성 수 판독 경로다. 내부 selection 학습은 설명하되 분리 파형 성능은 본문의 독립 주제로 삼지 않는다.
- 본문 결과: S37은 Table VI의 Full과 A1(w/o IPD Enhancer) 두 행, MAE·F1 두 열만 사용한다. 각각 0.98°·0.96과 2.10°·0.83이다. A4와 OSPA-T는 부록으로 보낸다. 아래 표는 부록 수치까지 보존한 근거 요약이며 전체를 본문에 넣지 않는다. MOTA*의 외부 순위 비교를 중심 근거로 삼지 않는다.

  | 설정 | MAE | F1 | OSPA-T |
  | --- | ---: | ---: | ---: |
  | Full | 0.98° | 0.96 | 2.08° |
  | A1: w/o IPD Enhancer | 2.10° | 0.83 | 5.02° |
  | A4: direct IPD input | 2.71° | 0.73 | 6.50° |

- 비교 조건: 두 채널 혼합음과 text 및/또는 1초 audio cue로 목표를 지정한다. Full은 text+audio 조건을 유지한다. 주 실험은 합성 4×4×2 m 방, T60 0.2 s, 20 cm 마이크 간격, 5초 clip, SNR -5–5 dB다. 프레임별 목표 활성 수는 0/1/2, 방위각은 [0,180)이다. selection·DOA·cardinality를 함께 학습한다.
- 허용 결론: 해당 목표 선택 설정에서 IPD Enhancer를 제거하면 위치 오차와 검출 F1가 모두 나빠진다. 직접 IPD로 바꾼 조건의 결론은 부록 A4 비교에서만 말한다.
- 금지 해석·미해결: MAE는 원표 caption 기준 true positive의 오차이므로 검출 실패를 함께 설명한다. Table III의 일부 P/R·MOTA* 행은 정의식과 일치하지 않아 미해결로 남긴다. MOTA*는 ID-switch 벌점이 없어 음원 정체성 추적의 증거로 삼지 않는다. TAU-SRIR 결과는 측정 RIR 합성이며 현장 이동 혼합음 녹음이 아니다. 360°·임의 다중 목표·미학습 의미 범주로 확장하지 않는다.
