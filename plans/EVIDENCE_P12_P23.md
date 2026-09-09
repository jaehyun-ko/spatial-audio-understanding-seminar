# 본문 근거 대장 P12–P23

기준일: 2026-09-09. 본문 위치는 `BLUEPRINT_PART2.md`의 S38–S66을 따른다. P 번호는 문헌 식별자다. 발표에서는 P16 Dual-BEATs를 P15 PhaseCoder보다 먼저 다룬다. 이 문서는 제작용 근거 설계이며 그림 취득·크롭·슬라이드 렌더 검증 완료를 뜻하지 않는다.

공통 원칙: 한 장의 주근거는 하나로 제한한다. 아래 결과는 같은 논문의 선택 행끼리 읽으며 논문 간 통합 순위를 만들지 않는다. 입력 조건, 학습 변경, 평가 데이터와 채점 방법을 함께 표시한다. 그래프에서 확정하지 않은 수치는 원문 패널을 사용하고 눈대중으로 만들지 않는다.

### P12. BAT: Learning to Reason about Spatial Sounds with Large Language Models

- 채택 버전·원문 링크: [arXiv 2402.01591v4](https://arxiv.org/html/2402.01591v4). Table 1의 과제 정의와 Table 4의 결과를 같은 버전으로 사용한다.
- 본문 위치: S38–39, S49 비교.
- 고유 문제·그림 역할: S38은 Table 1의 C/D 질문을 바탕으로 소리 이름과 위치의 대응이 달라지는 장면을 재구성한다. 기존 SELD도 사건과 위치를 연결함을 먼저 설명한다. Fig. 1은 공간 인코더·projector·LLM의 방법 그림이며 본문 결과를 대신하지 않는다.
- 본문 결과: S39는 Table 4의 최종 BAT 두 입력 행과 Type E 평균 BA만 주근거로 쓴다.

  | 최종 BAT 입력 | Type E 평균 BA |
  | --- | ---: |
  | P, 질문만 | 54.48% |
  | B+P, 바이노럴과 질문 | 76.89% |

- 비교 조건: 같은 SpatialSoundQA에서 정해진 공간 관계 Yes/No 답변을 평가한다. Type E는 두 음원 관계 과제다. 입력 오디오는 AudioSet 원음을 SoundSpaces RIR로 공간화한 10초 바이노럴이다. 공간 인코더 사전학습과 perception-to-reasoning 언어 연결 학습을 구분한다. 표의 P는 prompt, B는 binaural이다.
- 허용 결론: 해당 모델·평가에서 바이노럴 관측을 제공한 조건은 질문만 제공한 조건보다 관계 QA 정확도가 높다.
- 금지 해석·미해결: 특정 위상 단서의 인과효과나 모든 자유형 공간 대화의 성공으로 확대하지 않는다. mono 행은 stage III만 학습했으므로 최종 three-stage BAT와 입력만 다른 통제가 아니다. C/D 제거 비교도 학습 유형·분량을 함께 바꾼다. 원문 Table 1의 일부 예시보다 실제 Type E 채점의 binary 정의를 우선한다.

### P13. DSpAST: Disentangled Representations for Spatial Audio Reasoning with Large Language Models

- 채택 버전·원문 링크: [arXiv 2509.13927v1](https://arxiv.org/html/2509.13927v1). Fig. 1–2와 Table 2–3 번호를 이 버전에 고정한다.
- 본문 위치: S40–41, S49 비교.
- 고유 문제·그림 역할: §3.2의 과제별 특징 중요도 차이를 문제 장면으로 재구성한다. Fig. 1은 추가 특징·feature attention·분기를 보여주는 방법 그림이다. Transformer와 patch embedding의 파라미터는 공유한다. Fig. 2의 평균 attention은 보조 관찰이며 단서 사용의 인과 실험이 아니다.
- 본문 결과: Table 3에서 동일 single-stage BAT의 인코더 두 행, Type D 방향 정확도·DER와 Type E 평균 BA를 선택한다.

  | 인코더 | Type D 방향 정확도 | Type D DER | Type E 평균 BA |
  | --- | ---: | ---: | ---: |
  | SpatialAST, single-stage BAT | 34.80% | 53.40% | 74.04% |
  | DSpAST, single-stage BAT | 37.35% | 48.51% | 76.56% |

- 비교 조건: SpatialSoundQA 합성 바이노럴, 질문과 오디오를 받아 답변 토큰을 생성한다. single-stage는 전체 질문 유형으로 5 epochs 학습하며 LoRA와 greedy decoding을 사용한다. 방향은 8개 조합 범주의 정확도, DER는 거리 오차 0.5 m 초과 비율이다. 인코더의 특징뿐 아니라 사전학습 curriculum·AdaCos loss도 달라진다.
- 허용 결론: 이 언어 학습 설정에서 DSpAST 인코더를 사용한 모델은 선택한 공간 질문의 점수가 더 좋다.
- 금지 해석·미해결: 전체 차이를 분기 하나에 귀속하지 않는다. 원 BAT와 checkpoint·의미 평가 embedding이 달라 논문 간 수치를 직접 연결하지 않는다. §4.2.1의 A/B/C 설명에 오기가 있으므로 음원 수와 질문 유형은 BAT 정의를 따른다. Table 2의 MAE는 각도이며 caption의 모든 수치가 백분율이라는 표현을 복사하지 않는다.

### P14. OWL: Geometry-Aware Spatial Reasoning for Audio Large Language Models

- 채택 버전·원문 링크: [arXiv 2509.26140v1](https://arxiv.org/html/2509.26140v1), 2025-09-30 공개. 이 버전의 SAGE loss ablation을 본문에 채택한다.
- 본문 위치: S42–44, S49 비교.
- 고유 문제·그림 역할: S42 Fig. 2는 BiDepth의 depth·음향 대응을 보여주는 학습 장면이다. S43 Fig. 4는 깊이·RIR 보조 학습과 바이노럴 추론 경로를 구분하는 방법 그림이다. Fig. 1의 활용 개념과 Fig. 4의 구조를 실제 성능 근거로 대체하지 않는다.
- 본문 결과: S44의 주근거는 Table 5의 binaural-only loss와 전체 geometric loss 두 행이다.

  | SAGE loss 조건 | MAE | DER |
  | --- | ---: | ---: |
  | L_binaural, η₂=0 | 26.32° | 17.11% |
  | 전체 조건, η₂=10⁻² | 21.67° | 14.32% |

- 비교 조건: BiDepth 합성 평가이며 추론에는 바이노럴 오디오만 제공한다. 기하 보조 학습에는 depth와 RIR 정답을 사용한다. MAE는 방향 오차, DER는 거리 오차가 0.5 m를 넘는 비율이다. 이후 OWL QA 학습에서는 SAGE 음향 인코더를 고정하고 projector와 LLM LoRA를 학습한다.
- 허용 결론: 이 BiDepth loss 비교에서 기하 항을 포함한 학습 조건은 방향·거리 오차가 더 낮다.
- 금지 해석·미해결: Table 4의 QA 시스템 차이를 geometry만의 효과로 부르지 않는다. 해당 QA와 CoT Table 6은 부록이다. Table 3의 4-bin/12-bin 방향 평가를 섞지 않는다. Table 2의 SSQA MAE는 geometry SAGE 18.47°가 Spatial-AST 17.94°보다 높으므로 모든 전이 지표 우세를 주장하지 않는다. BiDepth의 room/source 분할은 저자의 기술이며 합성 환경 밖 일반화와 구분한다.

### P15. PhaseCoder: Microphone Geometry-Agnostic Spatial Audio Understanding for Multimodal LLMs

- 채택 버전·원문 링크: [arXiv 2601.21124v2](https://arxiv.org/html/2601.21124v2). v2의 Table 1 실녹음 DOA와 Table 3 공간 QA를 별도 평가로 유지한다.
- 본문 위치: S47–48, S49 비교.
- 고유 문제·그림 역할: S47 Fig. 2의 채널 위상 관측으로 배열 신호를 설명한다. 마이크 좌표도 입력한다는 점을 명시한다. Fig. 1·3의 전체 구조는 부록이다. 기존 의미 오디오 경로와 PhaseCoder의 공간 경로를 구분한다.
- 본문 결과: S48은 Table 3의 Gemma Baseline과 Gemma SFT, Task 2 관계 Yes/No 정확도를 주근거로 쓴다.

  | 모델 | Synthetic Task 2 | RSL2019 Task 2 |
  | --- | ---: | ---: |
  | Gemma, Baseline | 48.44% | 53.91% |
  | Gemma SFT, Ours | 76.76% | 73.83% |

- 비교 조건: baseline은 mono 입력이고 SFT에는 다채널·마이크 좌표에서 만든 공간 토큰과 추가 학습이 함께 들어간다. QA의 두 발화는 비중첩 연결이다. Synthetic은 미사용 LibriSpeech·RIR·배열을 사용한다. RSL QA는 원 데이터의 train split 녹음에서 재구성하며, Gemma의 의미 입력은 채널 평균을 사용한다.
- 허용 결론: 공간 입력과 SFT를 결합한 시스템은 이 합성·재구성 QA의 관계 판단을 개선한다.
- 금지 해석·미해결: 토큰 하나의 순수 인과효과, 좌표 불필요, 겹친 음원의 분리 성공으로 해석하지 않는다. RSL Task 4 mean WER는 baseline 42.90에서 SFT 48.41로 악화한다. 원문은 WER>3.0 출력을 제외하므로 미필터 오류·실패율을 보장하지 않는다. 무지향·free-floating 배열 가정과 장치 산란을 구분하고 Table 1 encoder 성과는 부록에서 별도 읽는다.

### P16. Dual-BEATs: Unlocking Zero-Shot Stereo Audio Perception in Audio Large Language Models via Dithering

- 채택 버전·원문 링크: [arXiv 2607.08800v1](https://arxiv.org/html/2607.08800v1), 2026-07-09 공개. 본문 Table 1의 97.1을 사용하고 초록의 97.2와 혼합하지 않는다.
- 본문 위치: S45–46, S49 비교.
- 고유 문제·그림 역할: S45는 §3.2와 Appendix A.3의 amplitude panning을 설명용 장면으로 재구성한다. Fig. 1은 두 고정 BEATs 경로와 dither의 방법 그림이다. Fig. 2는 학습·평가 panning 조합의 일반화 결과이며 부록에 둔다.
- 본문 결과: Table 1의 OLMo-3-7B+Dual-BEATs, Direction-First 행만 사용한다. 각 PA 안에서 dither Off/On을 비교한다.

  | 평가 PA | Off 방향 정확도 | On 방향 정확도 |
  | --- | ---: | ---: |
  | 0.00 | 99.5% | 99.0% |
  | 0.50 | 37.9% | 97.1% |

- 비교 조건: 같은 backbone·출력 순서·PA의 Left/Center/Right 분류다. 원음 하나를 좌우 gain으로 공간화한다. On은 DA=0.05의 채널별 독립 dither, 학습·평가 random seed는 분리한다. BEATs는 고정하고 projector·언어 adaptation을 학습한다. PA=0.50은 약한 쪽 gain 0.5를 뜻하며 Center 자체가 아니다.
- 허용 결론: 이 단일 원음 panning 실험에서 dither는 PA=0.50 성능을 크게 높이며 모든 PA에서 일률적으로 이득을 주지는 않는다.
- 금지 해석·미해결: 미관측 panning 일반화를 새 배열·HRTF·잔향 전이로 부르지 않는다. 위상 활용, 사람의 청취 한계, 모든 정규화 계층의 원인 기전을 이 표만으로 입증하지 않는다. Table 1과 Fig. 2의 학습·평가 PA 조건을 섞지 않고 semantic F1 저하도 공간 성과에 묻어 없애지 않는다.

### P17. Sci-Phi: A Large Language Model Spatial Audio Descriptor

- 채택 버전·원문 링크: [arXiv 2510.05542v1](https://arxiv.org/html/2510.05542v1), 2025-10-07 공개. 이 버전의 Fig. 2·Table 2 평가 정의를 함께 사용한다.
- 본문 위치: S50–52.
- 고유 문제·그림 역할: S50은 §3.3의 음원·배경·방 출력 형식을 설명용 장면으로 재구성한다. S51 Fig. 1은 공간 인코더와 W 채널 의미 인코더의 방법이다. S52 전에 이름과 위치를 바꿔 붙인 작은 예로 음원별 공통 대응의 필요성을 설명한다.
- 본문 결과: S52는 Fig. 2의 TupleScore 패널 하나를 주근거로 쓴다. `SELDNet+Phi-4 (MC, FT)`와 `Sci-Phi`를 선택하고 synthetic-RIR/real-RIR 조건을 분리한다. 1–4음원 전체 평균의 diamond만 비교하며 한 음원·네 음원 기호를 평균으로 바꾸지 않는다. 미확정 정밀 수치는 새로 적지 않는다.
- 비교 조건: 두 시스템 모두 장면 기술에 미세조정한 비교다. baseline은 고정 SELDNet 표현을 사용하고 Sci-Phi는 공간 encoder도 적응한다. 입력은 FOA, 출력은 최대 네 방향성 음원과 배경·방 속성이다. TupleScore는 What·Where·When의 기하평균이며 음원 단위 대응을 결정한다. Synthetic은 미관측 방·음원, real-RIR는 실측 RIR로 합성한 음원과 실제 배경을 사용한다.
- 허용 결론: 선택한 두 RIR 평가 조건에서 공간 표현을 함께 적응한 Sci-Phi는 해당 미세조정 기준선보다 높은 TupleScore를 보인다.
- 금지 해석·미해결: Table 2의 Optimal-Metric/Optimal-Source는 채점 원칙 비교이며 모델 ablation이 아니다. TupleScore의 두 채점값 동일성은 정의에서 나온다. 실측 RIR 합성을 현장 혼합음 녹음으로 부르지 않는다. Real-RIR의 수평 방향 위주 범위와 누락된 방 크기·배경 라벨을 합성 평가의 전체 범위로 확대하지 않는다.

### P18. Spatial-Omni: Spatial Audio Understanding Integration in Multimodal LLMs via FOA Encoding

- 채택 버전·원문 링크: [arXiv 2606.10738v2](https://arxiv.org/html/2606.10738v2), 첫 공개 2026-06-09, v2 수정 2026-09-07. Fig. 2(a)·Fig. 1·Table 2를 v2로 통일한다.
- 본문 위치: S53–55.
- 고유 문제·그림 역할: S53 Fig. 2(a)는 위치 기반 음원 식별·상대 좌우 등의 과제 예시다. S54 Fig. 1은 FOA 공간 토큰과 기존 의미 오디오 입력의 결합 방법이다. 구조적 의미 경로 유지와 실제 일반 음향 성능을 구별한다.
- 본문 결과: S55는 Table 2의 SO-7B-zs와 SO-7B 행, 아래 세 열을 채택한다.

  | 모델 | EAzi | IS-Loc | RLR |
  | --- | ---: | ---: | ---: |
  | SO-7B-zs, 공간 토큰 0 | 13.06 | 40.69 | 47.15 |
  | SO-7B | 76.38 | 66.81 | 72.97 |

- 비교 조건: SO-Bench, 같은 7B 계열에서 공간 입력을 바꾼 내부 비교다. EAzi는 방위각 오차 20° 이내 비율, IS-Loc은 위치 조건에 맞는 음원 식별, RLR은 상대 좌우 판정이다. 값은 백분율 척도지만 서로 다른 과제다. Greedy decoding을 사용한다. 기본 학습은 projector 정렬, LLM LoRA 결합, 공간 인코더의 학습 가능한 부분을 포함한 적응으로 나뉜다.
- 허용 결론: 이 인터페이스에서 실제 공간 토큰은 zero-spatial 조건보다 선택한 공간 추정·식별·관계 판단에 유용하다.
- 금지 해석·미해결: input ablation을 특정 phase 기전의 증거로 바꾸지 않는다. SO-7B와 MIX를 섞지 않는다. MH는 22.52/39.93으로 여전히 어렵다. Fig. 5의 일반 오디오 결과는 완전 보존이 아니라 MIX의 부분 회복이다. SC의 WER는 낮을수록 좋으며 다른 지표와 단순 평균하지 않는다. 임의 배열 일반화는 평가하지 않았다.

### P19. The World is Not Mono: Enabling Spatial Understanding in Large Audio-Language Models

- 채택 버전·원문 링크: [arXiv 2601.02954v3](https://arxiv.org/html/2601.02954v3), 2026-05-10 수정. 초기 버전의 binaural·GRPO 대신 v3의 FOA·SAPO를 사용한다.
- 본문 위치: S56–58.
- 고유 문제·그림 역할: S56 Fig. 4는 L1 지각, L2 연결, L3 복합 질의의 문제 예시다. Fig. 1의 추상 과제 계층은 보조다. S57 Fig. 2는 source slots와 의미 경로·학습 단계의 방법이다. 예시 장면과 정답 생성 metadata는 추론 입력이 아니다.
- 본문 결과: Table 5의 TWNM-SFT/TWNM-SAPO와 L1/L2/L3 세 열을 채택한다.

  | 학습 단계 | L1 | L2 | L3 |
  | --- | ---: | ---: | ---: |
  | TWNM-SFT | 65.19% | 70.61% | 51.19% |
  | TWNM-SAPO | 63.64% | 69.89% | 79.76% |

- 비교 조건: 최대 세 음원 합성 FOA 장면의 ASA benchmark, 동일 exact MCQA 채점과 단일 실행 결과다. 음향 인코더 학습·적응 후 projector 정렬, SFT, SAPO를 구분한다. 최종 평가의 새 렌더 장면·질문·공간 구성은 학습과 분리하지만 dry-source clip identity는 중복될 수 있다.
- 허용 결론: 최종 SAPO 단계는 이 평가의 복합 질의 점수를 높였고, 기초 지각과 관계 연결에는 소폭 하락이 함께 나타났다.
- 금지 해석·미해결: 모든 능력의 동시 향상, explicit scene graph 출력, 새로운 음원 정체성 전이로 해석하지 않는다. Table 2 외부 모델은 입력·채점이 다른 진단 참고다. Table 11 통제는 strict pick-letter audit라 full-FOA exact score와 완전히 같은 채점이 아니다. STARSS23 QA는 encoder 적응 녹음과 분리되지 않아 recording-disjoint 전이로 부르지 않는다.

### P20. Spatial Audio Motion Understanding and Reasoning

- 채택 버전·원문 링크: [arXiv 2509.14666v1](https://arxiv.org/html/2509.14666v1), 2025-09-18 공개. Table 1의 질문과 Table 3의 QA 결과를 사용한다.
- 본문 위치: S59–60.
- 고유 문제·그림 역할: S59는 Table 1의 방향 궤적·거리 변화 질문을 시간축 장면으로 재구성한다. Fig. 1은 DSAST·AGM 예측을 JSON으로 정리해 추론 LLM에 전달하는 방법이며 부록에 둔다. 정답 metadata와 추론에 전달하는 예측 속성을 구별한다.
- 본문 결과: S60은 Table 3에서 같은 Qwen7B 추론 모델을 쓰는 AGM 유무 두 행의 DoA·Overall 열을 채택한다.

  | 모델 | DoA & trajectory | Overall |
  | --- | ---: | ---: |
  | DSAST+Qwen7B | 35.8% | 20.7% |
  | DSASTw/AGM+Qwen7B | 26.4% | 31.1% |

- 비교 조건: 추론 LLM은 DeepSeek-R1-distilled Qwen-7B와 greedy decoding으로 동일하다. stereo STARSS23 기반 지각 인코더의 시간별 예측을 언어 모델이 읽는다. QA는 STARSS23 test 장면 metadata에서 만든 Boolean·single-answer MCQ다. AGM과 지각 인코더는 학습하며 추가 추론 LLM 연결은 training-free다.
- 허용 결론: 같은 추론 모델에 AGM 결합 지각 결과를 전달한 경로는 전체 QA를 개선했지만 방향·궤적 질문 점수는 낮아졌다.
- 금지 해석·미해결: 모든 구성요소의 무학습, 모든 움직임 과제 개선, 원 파형을 추론 LLM이 직접 듣는 구조로 설명하지 않는다. BAT와는 LLM·입력 인터페이스가 다르다. Table 2의 미관측 음원 클래스 encoder 평가는 Table 3 QA와 별개다. 본문 결과 문장의 일부 모델명이 표와 달라 정확한 행 이름을 우선한다.

### P21. Spatial Audio Question Answering and Reasoning on Dynamic Source Movements

- 채택 버전·원문 링크: [arXiv 2602.16334v1](https://arxiv.org/html/2602.16334v1), 2026-02-18 공개. Table 3의 Overall 행을 본문에 고정한다.
- 본문 위치: S59, S61.
- 고유 문제·그림 역할: S59 Table 2의 질문으로 질의 관련 시간 구간을 설명한다. Fig. 1은 공간 인코더·Q-Former·thinking LLM과 AGM 전처리의 방법이다. masking은 검출 구간 밖 파형을 0으로 만드는 시간 선택이며 겹친 음원의 완전한 분리 파형을 뜻하지 않는다.
- 본문 결과: Table 3의 Overall 행에서 같은 모델의 masking×thinking 여섯 조건을 채택한다.

  | 출력 설정 | NoMask | AGM | GT mask |
  | --- | ---: | ---: | ---: |
  | Thinking | 54.3% | 55.0% | 56.1% |
  | Non-Thinking | 54.1% | 54.0% | 54.1% |

- 비교 조건: AudioSet strong-labeled 원음에 움직임을 부여한 합성 stereo 평가다. 시간 정보를 확장한 BAT 계열 인코더, Q-Former, Qwen3-4B를 학습한다. AGM은 추론 전처리이며 GT는 정답 이벤트 구간을 제공하는 참고 조건이다. 같은 thinking 열에서 masking을, 같은 mask에서 thinking을 비교한다. Overall은 Yes/No·MCQ·open 질문을 포함한다.
- 허용 결론: 이 평가에서 masking과 thinking의 결합 효과는 조건에 따라 다르며 Overall 개선 폭은 제한적이다.
- 금지 해석·미해결: GT mask를 배포 가능한 추론 입력으로 쓰지 않는다. 하위 과제의 큰 개선량을 Overall에 대입하지 않는다. 시간 mask는 같은 구간의 간섭 음원을 완전히 제거하지 못한다. 수치 차이를 통계적 유의성이나 생성한 rationale의 청각적 충실성 증명으로 바꾸지 않는다.

### P22. Spatio-Temporal Audio Language Modeling for Dynamic Sound Sources

- 채택 버전·원문 링크: [ST-AudioLM, arXiv 2606.14141v1](https://arxiv.org/html/2606.14141v1), 2026-06-12 공개. ST-AudioQA Table 1과 Table 5를 본문에 대응시킨다.
- 본문 위치: S62–64.
- 고유 문제·그림 역할: S62는 Table 1의 시간 조건 질문을 바탕으로 음원 정체성과 시간별 위치를 연결하는 장면을 재구성한다. S63 Fig. 1은 사건 의미·궤적 표현과 언어 모델의 방법이다. 이 구조도를 고유 문제 그림으로 표시하지 않는다.
- 본문 결과: Table 5의 QA-trained Spatial-AST-FOA+OLMo2와 ST-AudioLM 두 행을 채택한다.

  | 모델 | Temp. rel. | Move-spat. | Traj. rel. | Avg. |
  | --- | ---: | ---: | ---: | ---: |
  | Spatial-AST-FOA+OLMo2 | 80.4 | 55.2 | 54.3 | 63.3 |
  | ST-AudioLM | 86.0 | 55.8 | 60.6 | 67.5 |

- 비교 조건: ST-AudioQA의 Type C, controlled-answer accuracy, 0–100 척도다. 열은 시간 관계 변화·이동 조건 공간 관계·두 음원의 궤적 관계를 뜻한다. 두 행은 같은 FOA 계열 입력·OLMo2·41-token 인터페이스의 QA 학습 비교다. 선택한 baseline은 정적 FOA encoder를 사용하고 제안 모델은 궤적 지도 학습 표현을 사용한다.
- 허용 결론: 해당 통제 장면에서 궤적 표현을 사용하는 시스템은 조합 QA 평균이 더 높고, 이동·궤적 관계의 어려움은 남는다.
- 금지 해석·미해결: 모든 encoder 지표에서 우수하거나 밀집한 현실 동적 장면을 해결했다고 말하지 않는다. BAT는 같은 장면 metadata를 바이노럴로 렌더링해 입력하므로 동일 입력 ablation이 아니다. Table 3 encoder와 실제 녹음 적응, Table 4 기본·두 음원 QA는 별도 부록이다. 사건 순서의 검색 성과와 합산하지 않는다.

### P23. CoSTALA: Compositional Spatio-Temporal Audio-Language Alignment via Multi-Grain Hierarchical Contrastive Learning

- 채택 버전·원문 링크: [arXiv 2608.24374v1](https://arxiv.org/html/2608.24374v1), 2026-08-25 공개. Fig. 1–2와 Table 2의 역할을 구별한다.
- 본문 위치: S65–66.
- 고유 문제·그림 역할: S65는 §2.1의 기준 사건열·temporal negative·spatial negative를 재구성한다. 두 사건의 순서 또는 방향을 바꾸며 연속 이동 궤적은 그리지 않는다. Fig. 1은 학습 구조, Fig. 2는 isolated/composed 특징과 일관성 학습의 방법이며 부록으로 둔다.
- 본문 결과: S66은 Table 2에서 contrastive-only와 전체 loss 두 행의 Global Text-to-Audio R@1 열을 선택한다.

  | CoSTALA loss | Global T2A R@1 |
  | --- | ---: |
  | L_cl | 5.84% |
  | L_cl + L_st + L_local + L_consist | 8.10% |

- 비교 조건: 겹치지 않는 두 합성 FOA 사건, 8방향, 공간·시간 caption의 retrieval 평가다. §3.1은 E_global과 T_st의 cosine similarity로 검색한다고 명시한다. R@1은 정답이 첫 검색 후보에 들어오는 비율이다. 사건별 local alignment와 consistency를 포함한 전체 학습 조건을 contrastive-only와 비교한다.
- 허용 결론: 이 합성 사건열의 검색에서는 전체 loss 구성의 R@1이 더 높다.
- 금지 해석·미해결: Table 2를 Fig. 2의 최종 E_st 직접 평가로 설명하지 않는다. soft slicing은 원 segment duration을 사용하므로 자동 사건 경계 추정은 확인하지 않았다. 의미 전용 열을 모든 지표의 보존 증거로 쓰지 않는다. 순서 구별을 연속 음원 추적·겹친 음원 분리·자유형 QA로 확대하지 않는다. 단일 loss의 독립 인과효과와 새로운 음원·방 분할 일반화는 별도 검증이 필요하다.
