# 공간 오디오–LLM: 모듈, 학습 상태, 검증 범위

검증일: 2026-09-11. 대상은 원고 `EVIDENCE_P12_P23.md`의 지정 버전과 저자 원문이다. 아래 구성은 덱을 읽는 **분석 관점**이며 모든 공간 오디오 시스템의 필수 구조가 아니다. 발표 그림은 원문 구조를 설명하는 재구성이고, 수치 실험과 교육용 반례를 구분한다.

현재 구조는 **본문 49장+부록 36장=85장**이다. 위치 명세는 [CAUSAL_DECK_ORDER](CAUSAL_DECK_ORDER.json), 최초 공개 연대·명시 계승은 [MC_AUDIO_LM_HISTORY](MC_AUDIO_LM_HISTORY.md)를 따른다. 직전 문서는 [보관본](archive/pre-mc-history/plans/CAUSAL_LLM_MODULES.md)에 보존했다.

## 1. 먼저 고정할 정의

S16은 **기존 언어 표현을 통해 전달하는 경로**와 **오디오 연속 표현을 직접 연결하는 경로**를 나눈다. Motion 2025는 지각부가 예측한 사건·DoA·거리·시간을 JSON 텍스트로 만들어 LM에 전달한다. OWL은 SAGE의 연속 특징을 Q-Former로 전달하므로 직접 연결형이다. OWL의 CoT는 출력 학습 방식이며 JSON 입력을 뜻하지 않는다. “표현공간 확장”을 쓸 때에는 비언어 입력 표현의 종류를 넓힌다는 범위로 정의하고, hidden width·vocabulary 증가와 구별한다. [Motion §2.2](https://arxiv.org/html/2509.14666v1), [OWL §5](https://arxiv.org/html/2509.26140v1)

다음 E/P/LM 표기는 직접 연속 표현을 연결하는 계열의 공통 분석 틀이다.

입력 $X$에서 인코더가 $H=E_\theta(X)\in\mathbb R^{T\times d_e}$를 만들고, 연결 모듈이 $Z=P_\phi(H)\in\mathbb R^{K\times d_{\rm LLM}}$를 만든다. $Z$는 질문의 텍스트 임베딩과 함께 디코더에 입력된다. 여기서 $T$는 인코더 표현의 길이이며 모든 모델에서 순수한 시간 축이라는 뜻은 아니다. $K$는 연결 모듈이 선택·재표본화·압축한 입력 길이이다. 여러 인코더가 있으면 $P$가 스트림을 융합하기도 한다. 구체적인 연결 순서는 모델마다 다르다. [Spatial-Omni §3](https://arxiv.org/html/2606.10738v2), [PhaseCoder §3.3](https://arxiv.org/html/2601.21124v2)

- **E의 질문:** 의미·위치·시간 정보를 어떤 표현에 남겼는가?
- **P의 질문:** 어떤 길이·순서·분기·차원으로 LLM에 전달하는가?
- **LLM 적응의 질문:** 전달된 조건을 답변 생성에 사용하도록 무엇을 학습했는가?

권장 문장: **“연결 모듈은 기존 LLM 임베딩 차원의 연속 오디오 토큰을 입력 시퀀스에 추가하고, LoRA 등의 적응은 LLM이 그 조건을 사용하는 방식을 학습한다.”** “어댑터로 확장된 토큰 공간을 LoRA가 사용한다”는 문장은 어휘 집합이나 임베딩 폭의 증가로 오해되므로 사용하지 않는다. PhaseCoder의 공간 토큰은 soft token이며, 경계 표지는 기존 어휘의 미사용 토큰 ID를 재사용한다. 경계 표지의 구현과 연속 오디오 표현은 별개다. [PhaseCoder §3.3](https://arxiv.org/html/2601.21124v2)

LoRA는 선형층을 $W=W_0+(\alpha/r)BA$로 적응한다. $W_0\in\mathbb R^{d_{out}\times d_{in}}$는 고정하고, $A\in\mathbb R^{r\times d_{in}}$, $B\in\mathbb R^{d_{out}\times r}$를 학습한다. 낮은 랭크 $r$는 업데이트의 제약이며 토큰 개수나 어휘 수가 아니다. 적용 층에 따라 attention/FFN의 처리도 바꾸므로 “출력 헤드만 학습한다”로 축약하지 않는다. 일반적인 생성은 기존 어휘에 대한 확률 분포를 사용한다. 일부 구현이 embedding/lm_head도 학습한다는 사실 자체가 vocabulary 확장을 뜻하지는 않는다. [LoRA §4.1](https://arxiv.org/abs/2106.09685v2)

P와 LLM은 E에서 실제로 소실된 정보를 **보장하여 복원하지 못한다**. 문맥·사전확률로 추론할 수 있다는 것과 관측 정보의 보존은 구분한다. 교육 그림의 반례는 순서 정보가 없는 단순 시간 평균에만 해당한다. 학습한 전역 토큰도 순서를 인코딩할 수 있으므로 모든 전역 표현의 불가능성 증명으로 확장하지 않는다.

## 2. 실제 모듈과 학습 상태

`고정`은 해당 단계에서 기존 가중치를 학습하지 않는다는 뜻이다. `LLM 고정+LoRA`는 기존 LLM 가중치는 고정하고 추가 저랭크 가중치는 학습한다는 뜻이다. QA 학습과 인코더 사전학습을 별도로 읽는다.

| 논문·입력과 E | 실제 P 및 LLM 입력 | LLM 적응·freeze/train 단계 | 1차 출처 |
|---|---|---|---|
| **BAT v4**: 10초 바이노럴, L/R log-mel+IPD sin/cos. AudioMAE 초기화 Spatial-AST. 사건·방향·거리 CLS와 패치 표현. | 학습 가능한 query projection. CLS+audio patches를 LLaMA 2 입력 임베딩으로 연결. 32/64 queries 비교. | 인코더 사건 학습→사건·방향·거리 학습. 논문은 **LLaMA-Adapter V2**: projection, zero-init attention, norm/bias/scale 등을 적응. QA는 perception→relation curriculum. 논문 본문만으로 QA E freeze를 단정하지 않는다. | [§4.1–4.2, §5.1, App. H, Tables 11–12](https://arxiv.org/html/2402.01591v4) |
| **BAT 저자 공개 구현**: Spatial-AST. 논문 v4 실험과 구현 세부를 섞지 않는다. | Q-Former 8층, 기본64 queries, 768→4096; LLaMA2-7B. | 실행 스크립트: E 고정, LLM 기본 가중치 고정, P+LoRA 학습. 설정의 LoRA r8/α32, Q/V, dropout.05. | [저자 프로젝트의 공개 저장소](https://github.com/X-LANCE/SLAM-LLM/tree/main/examples/seld_spatialsoundqa), [실행 설정](https://github.com/X-LANCE/SLAM-LLM/blob/main/examples/seld_spatialsoundqa/scripts/finetune_spatial-ast_qformer_llama_2_7b.sh), [모델 설정](https://github.com/X-LANCE/SLAM-LLM/blob/main/examples/seld_spatialsoundqa/seld_config.py) |
| **DSpAST**: 바이노럴 mel/IPD+ILD/GCC. 사건·방향·거리별 feature attention, 공유 Transformer/patch embedding, 분기별 축소 후 결합. | Spatial-AST 호환 CLS/patch 표현→Q-Former→LLaMA2-7B. | 사건·공간 인코더의 3단계 학습 후 E 고정. BAT 기반 P+LoRA QA; single-stage와 단계별 질문 curriculum 비교. | [§2, §3, §4.2.1](https://arxiv.org/html/2509.13927v1) |
| **OWL**: SAGE(AudioMAE 초기화 오디오 Transformer), 바이노럴 spectral/IPD. 깊이 ResNet과 RIR 재구성 보조 지도는 **학습 때만** 사용. | Q-Former 8층/64 queries→LLaMA2-7B. query 표현이지 명시적인 사건별 토큰이라고 증명한 것은 아니다. | E 사건 학습→기하 보조 공동 학습. QA E 고정, Q-Former+LoRA 학습; perception/relation/CoT 순. r8/α32는 확인되나 target 층/비율은 부록 상충. | [§4–5, App. B–C](https://arxiv.org/html/2509.26140v1) |
| **Dual-BEATs**: 같은 고정 BEATs를 L/R에 각각 적용. 시점이 정렬된 768차원 둘을 특징축에서1536차원으로 결합. | 시간 pooling 없이50 tokens/s. Gemma3-1B-it(1152) 또는 OLMo3-7B(4096)용 학습 projector. 좌우 결합은 토큰 길이2배가 아니다. | E 고정, NF4 LLM에 QLoRA+P를 한 QA 단계에서 학습. Table5는 embed_tokens/lm_head도 modules_to_save에 포함. LoRA rank는 원문에서 확인되지 않음. | [§3.2–3.3, Table5](https://arxiv.org/html/2607.08800v1) |
| **PhaseCoder**: 마이크 좌표+다채널 STFT 크기/위상. 250ms 창, 5 Transformer blocks, 256차원 공간 벡터. | 새 2층 MLP 256→2048→2048. 160ms hop=6.25 공간 tokens/s. Gemma3n-e4b-it의 USM 오디오 표현 앞에 공간188개+경계표지, 이어 오디오188개(30초 패딩). | E를 clean→noise localization 지도. QA P 학습, Gemma LoRA r8/α16/dropout.1, 5단계 curriculum. native USM 구조를 유지. **QA E freeze 상태는 본문·공개 encoder 추론 코드에서 명확히 확인되지 않아 도식에 동결 표지를 붙이지 않음.** | [§3, §4.2](https://arxiv.org/html/2601.21124v2), [저자 공개 encoder 코드 범위](https://github.com/google-deepmind/phasecoder) |
| **Sci-Phi**: FOA4 mel+3 intensity vector→SELDNet(3CNN/2GRU/2attention). W→Phi4-MM 원래 mono encoder 별도. | 공간·mono 각각2층 linear projector→3072. 공간 projector는 신규, mono projector는 기존 고정. 가변길이 spatial/audio embedding 구간. 일정 token rate는 확인되지 않음. | mono E/P와 Audio LoRA 고정. **공간 E+공간 P+새 Spatial LoRA를 함께 QA 학습**(5 epochs). Phi4Mini3.8B, Spatial LoRA r320. 공간 branch의 후속 적응이 핵심 차이. | [§3.1–3.3](https://arxiv.org/html/2510.05542v1) |
| **Spatial-Omni v2**: FOA mel/IV. SO-Encoder: BEATs 의미 경로에 공간 residual, 시간 의미 경로, CNN/Transformer 공간 경로, local cross-fusion. 기존 Omni의 W audio tower 별도 유지. | SO 표현10Hz→TemporalPixelShuffle→LN+2층 MLP. Table12 공간 토큰2.5Hz. 의미/공간 스트림을 LLM 기존 차원으로 연결. 주 모델 Qwen2.5-Omni7B, 여러 base에 이식. | E 사전학습 후 QA①P만 ②P+LLM LoRA ③P+LoRA+SO-E. 기존 audio tower는 기본 설정에서 고정. LoRA r16/α32/dropout.05/QKVO. 따라서 “E는 늘 고정”은 오류. | [§3, App. 학습 설정, Tables12–14](https://arxiv.org/html/2606.10738v2) |
| **TWNM v3**: FOA complex STFT real/imag 8채널 공간 encoder+LSTM attractor(최대3 source slots), room 전역 heads. W→고정 Whisper-small. | **LLM에는 dense 시계열**을 전달. 의미 expert+4 공간 experts+결합 expert를 concat/LN/bottleneck MLP로 연결. `<AcousticTokens>` 자리에 연속 임베딩. AF3 계열 Qwen2.5-7B; 새 decoder cross-attention 없음. source slots를3개 명시 객체 토큰으로 그리지 않는다. | ①공간 E 지도/실제 적응 ②E와 decoder 고정/P 정렬 ③P+LoRA SFT(r8/α32) ④SAPO LoRA 최적화. ④의 P 업데이트는 명시 근거 없이 추가하지 않음. | [§3, App. D/G](https://arxiv.org/html/2601.02954v3) |
| **ST-AudioLM**: FOA mel/IV→AST. 사건/DoA/거리 global tokens. 패치의 주파수 평균→40 시간 bins/10초→시간 attention, 동적 activity/3D방향/log거리 heads. | **의미1+시간40=41 tokens**→2층 MLP→OLMo2-7B-Instruct. 전역 DoA/거리 토큰은 LLM 입력에서 제외. 250ms 시간 해상도. | E 사건→정적 공간→동적+정적 replay+의미 distillation. QA에서는 heads 제거/E 고정, P+LoRA(r16/α32)3단계 학습. | [§4.1–4.2, §5.1](https://arxiv.org/html/2606.14141v1) |

| **Motion 2025**: stereo→DSAST; AGM의 class-text 특징과 frame별 confidence를 결합하여 사건·DoA·거리를 예측. | **JSON 텍스트**: Event/DoA/Source distance/Time frames. system prompt+예측 속성+질문→DeepSeek-R1-distilled Qwen-7B. | DSAST를 학습하고 AGM은 고정. 추가 reasoning LM 연결은 training-free. decoder cross-attention이나 연속 audio P/LoRA를 그리지 않는다. | [§2.1–2.2·3.2](https://arxiv.org/html/2509.14666v1) |
| **Dynamic QA 2026**: BAT encoder의 penultimate layer를 시간 인식에 맞게 수정. stereo, 질문 관련 시간 mask는 추론 전처리. | 연속 오디오 특징→Q-Former→Qwen3-4B thinking. Motion과 달리 직접 표현 연결이다. | 첫 단계 E 고정/P 정렬, 두 번째 E+P+LM LoRA 적응(r8/α16). 첫 단계의 LM 동결 상태는 문구만으로 확정하지 않는다. | [§3.2·4·5.2](https://arxiv.org/html/2602.16334v1) |

## 3. 어떤 실험이 무엇을 말하는가

숫자는 기존 근거 대장의 지정 프로토콜과 원문 표를 다시 확인했다. 같은 행의 지표끼리만 비교하며 여러 데이터셋·채점법의 숫자를 합치지 않는다.

| 논문 | 실제 관찰/통제와 지지하는 해석 | 이 비교만으로 입증하지 못하는 주장 |
|---|---|---|
| BAT | Table4 같은 최종 모델의 질문만54.48→바이노럴+질문76.89, Type E 평균BA. Table11 CLS/patch 결합, Table12 query 길이 비교는 입력 표현·connector 설계에 근거를 준다. [원문](https://arxiv.org/html/2402.01591v4) | 특정 IPD의 인과효과, LoRA의 필수성, 관계 질문의 보편적 해결. mono 행은 학습 단계가 달라 단순 채널 제거 통제로 취급하지 않음. |
| DSpAST | Table3 같은 single-stage QA에서 Spatial-AST→DSpAST: direction accuracy34.80→37.35, DER53.40→48.51, BA74.04→76.56. Table2는 feature/attention ablation. [원문](https://arxiv.org/html/2509.13927v1) | 전체 개선을 attention 하나에 귀속하거나 heatmap을 인과적 feature 사용의 증거로 해석. 인코더의 특징·학습 목표·curriculum 변화가 함께 있음. |
| OWL | Table5 기하 보조 가중치0→full: MAE26.32→21.67, DER17.11→14.32. 지정 인코더 조건에서 학습 시 기하 지도의 효과. [원문](https://arxiv.org/html/2509.26140v1) | 전체 QA 향상을 기하만으로 귀속, 모든 기하/방의 일반화, CoT가 실제 청각 근거를 충실히 따름, Q-Former가 항상 MLP보다 우수함. |
| Dual-BEATs | Table1 dither Off→On: PA.5에서37.9→97.1; PA0에서는99.5→99.0. pan으로 만든 좌/중/우 조건의 robustness. [원문](https://arxiv.org/html/2607.08800v1) | 모든 조건에서 개선, 자연 HRTF/위상/배열 일반화. frozen LLM 실패는 §3.3 서술이며 LoRA-on/off matched 수치표가 아니므로 보편적 필요성 근거로 사용하지 않음. |
| PhaseCoder | Table1 외부 localization 평가와 Table3 LLM QA는 별도. RSL Task2 mono+SFT53.91→PhaseCoder73.83; WER42.90→48.41로 모든 태스크 개선 아님. [원문](https://arxiv.org/html/2601.21124v2) | Q/P/LoRA 각각의 기여 분리, spatial token만의 보편적 효과, 이미 없어진 신호의 복원. 마이크 좌표 입력이 모든 배치 조건의 완전 불변성을 보장한다는 주장. |
| Sci-Phi | Fig2는 SELDNet/Phi4 기반 비교에서 공간 경로의 end-to-end 적응을 평가. Table2 OptimalMetric/OptimalSource는 평가 매칭 방식. [원문](https://arxiv.org/html/2510.05542v1) | Fig2를 LoRA만의 효과로 읽기; Table2 행을 학습 ablation으로 읽기; 발생 사건/시간·공간 속성 묘사를 완전한 개체 추적 증명으로 확대. |
| Spatial-Omni | Table2 zero spatial tokens→real: E-Azi13.06→76.38, I-SLoc40.69→66.81, R-LR47.15→72.97. 해당 입력의 기여. -so/-uat/-iv/-neuiv는 설계 통제. [원문](https://arxiv.org/html/2606.10738v2) | stage별 향상을 LoRA만에 귀속(학습량/질문 난도/동결도 변화). 원래 audio tower를 고정했다는 구조로 일반 audio 능력 보존을 단정(Table18 감소, MIX 일부 회복). |
| TWNM | App.G Table15 **semantic judge**: P0 MLP overall39.20, P1 dual46.40, dense52.10; connector 선택에 직접 근거. main Table5 **exact MCQA** SFT→SAPO L1 65.19→63.64/L2 70.61→69.89/L3 51.19→79.76: reasoning 수준별 학습 목적 효과. [원문](https://arxiv.org/html/2601.02954v3) | main exact와 appendix semantic-judge 혼용, SAPO가 모든 수준을 개선, dense expert가 명시 객체 그래프를 만든다는 주장. pretraining/QA의 원음·recording 중복 범위는 기존 근거대장 경고 유지. |
| ST-AudioLM | 같은 FOA·41 tokens·OLMo2 비교: Table5 Spatial-AST 평균63.3→ST-AudioLM67.5; temporal80.4→86.0, moving55.2→55.8, trajectory54.3→60.6. 동적 표현 패키지의 효과. [원문](https://arxiv.org/html/2606.14141v1) | 단순 토큰 수 증가 효과(둘 다41), LoRA만의 효과, 모든 이동 문제 해결. 시간 attention/동적 지도/보존 학습이 함께 바뀌므로 단일 요인 인과로 말하지 않음. |

## 4. 필수 구조와 선택을 분리

이 덱에서 E→P→LLM은 **연속 오디오 표현을 언어 디코더에 직접 입력하는 모델군**을 비교하는 좋은 공통 좌표다. P는 단순 선형, MLP, Q-Former, 시계열 재표본화, 융합 모듈일 수 있다. 차원과 입력 형식이 이미 호환되면 별도 학습 P가 반드시 필요한 것도 아니다.

LoRA는 자주 사용되는 효율적 LLM 적응법이며 수학적 필수 조건이 아니다. frozen LLM에 학습 connector만 연결하는 설계도 실제로 존재한다. BLIP-2는 동결된 image encoder와 LLM 사이의 query bridge를 학습하는 대표적인 별도 모달리티 사례이다. 이는 공간 오디오에서 동일 성능을 보장하는 주장이 아니라 universal necessity의 반례다. [BLIP-2](https://arxiv.org/abs/2301.12597)

BAT v4가 선택한 LLaMA-Adapter V2와 BAT 공개 코드의 LoRA도 구분해야 한다. “BAT는 LoRA를 쓰지 않는다”나 “BAT가 LoRA 필수성을 증명한다” 모두 부정확하다. [BAT v4](https://arxiv.org/html/2402.01591v4), [BAT 공개 코드](https://github.com/X-LANCE/SLAM-LLM/tree/main/examples/seld_spatialsoundqa)

예측한 속성을 텍스트/JSON으로 전달하는 Motion은 본문 S16·S27의 주요 대안이다. E→P→LM의 직접 연속 토큰 경로와 구별하며, 좌표 head만 필요한 위치 추정과 text–audio retrieval도 이 공통 구조 밖에 존재한다. 이들의 표준 파이프라인에 연속 audio token projector나 LLM LoRA가 반드시 포함되는 것으로 그리지 않는다. 기존 `EVIDENCE_P12_P23.md`의 입력·데이터·평가 한계를 유지한다.

## 5. 모호점과 슬라이드 작성 규칙

| 항목 | 확인된 사실 / 최종 처리 |
|---|---|
| BAT paper/code | v4 본문 LLaMA-Adapter V2 vs 저자 공개 Q-Former+LoRA. 출처를 한 라벨에 혼합하지 않음. 공개 실행 설정의 freeze만 code 조건에 표기. |
| OWL v1 LoRA | App.B의 Q/V,4.1M,0.062%와 App.C의 Q/K/V,약0.8%가 상충. r8/α32만 공통 확정. 슬라이드에는 타깃층/비율 생략. |
| PhaseCoder QA encoder | 원문이 connector/LLM LoRA를 명시하나 encoder freeze는 불명확. 공식 저장소는 encoder inference/checkpoint 위주이며 QA 학습 구현을 제공하지 않음. “고정 E” 단정 금지. |
| Dual-BEATs rank | 원문 Table5에 rank 미표기. 값을 추정하지 않음. modules_to_save를 무시해 “LoRA만 학습”이라고 단정하지 않음. |
| 시계열 tokens | ST-AudioLM1+40, PhaseCoder6.25Hz, Dual-BEATs50Hz, SO2.5Hz는 해당 구현. 다른 모델 token rate를 도식 편의상 꾸며내지 않음. |
| TWNM dense/slots | encoder source-slot 지도와 LLM dense 입력을 분리. 3개 객체 토큰/scene graph를 LLM 입력으로 그리지 않음. |
| pooling 교육 예 | 장면1 A:-60→0→60/B:60→0→-60과 장면2 역순은 단순 평균에서 각 사건의 평균0으로 같아진다. 반례는 순서 없는 시간 평균에 한정. 숫자는 실험값이 아닌 교육용이다. |

## 6. 활성 bridge와 그림의 범위

| 현재 위치 | 원고 | 역할 |
|---|---|---|
| S15 | history-map | 최초 공개 연대와 연구 문제의 분화 |
| S16 | history-interfaces | Motion JSON과 OWL 연속 표현의 두 경로 |
| S17 | audio-llm-contract | E/P/LM과 연속 임베딩 입력 |
| S18 | lora-reading | P와 LoRA의 위치·역할·수학적 구별 |
| S22 | history-bat | 초기 공간 QA 연결의 출발점 |
| S24 | history-encoder-branches | DSpAST 단서 선택과 OWL 기하 감독 |
| S28 | history-extensions | 기존 Audio-LM 의미 경로와 새 공간 경로 |
| S35 | module-evidence | TWNM projector 보고값 3개 |
| S37 | history-dynamics | 명시 시계열과 연속 시간 토큰의 선택 |
| S38 | token-bottleneck | 순서 없는 시간 평균의 손실 반례 |
| S48 | history-synthesis | 연구 질문을 보존·전달·사용의 검사로 회수 |

새 history 계열 설명 7장은 **도식 6장과 네이티브 HTML 종합표 1장(S48)**이다. 원고는 `slides/bridges/history-*.md`, 출처는 [MC_AUDIO_LM_HISTORY](MC_AUDIO_LM_HISTORY.md)에 있다. 이 도식과 표는 새로운 수치 실험이 아니다. 기존 `adapter-training`과 `synthesis` 원고/이미지는 보존하되 현재 순서에서 비활성이다.

기존 audio-llm-contract/token-bottleneck/lora-reading 그림은 `scripts/visuals/causal-llm.py`로 재현한다. 라이트 디자인 시스템·Pretendard·렌더된 수식을 유지하고 글자 bounds와 실제 그림을 검수한다. 최종 활성 자산과 생성 경로는 [ASSET_SOURCES](../ASSET_SOURCES.md)를 따른다.

## 7. 추가 수치: TWNM v3 projector 진단 3개

기존 덱의 99개 원문 수치와 별도로 새로 추가하는 값이다. [원문 App. G.1, Table15](https://arxiv.org/html/2601.02954v3)에서 직접 확인했다.

| 원문 행명 | Overall (%) |
|---|---:|
| P0: Single MLP | 39.20 |
| P1: Dual Tower | 46.40 |
| P2: Dense Hybrid | 52.10 |

- 분모는 ASA benchmark **전체1,000항목**. 수준별 점수의 단순평균이 아니다.
- 최종 SAPO 이전의 semantic-answer audit. 원문 §F.6의 judge는 Gemini 3 Flash이며 질문/선지/gold option text/모델 답만 받는다. 오디오·RTSD를 보지 않는다. main Table5의 exact MCQA와 다른 프로토콜이다.
- 저자가 projector ablation으로 제시한 비교이다. 다만 G.1/Table15에는 P0/P1/P2의 encoder checkpoint, LLM checkpoint, 학습 예산, seed가 완전히 동일하다는 별도 명시가 없다. “연결 설계에 따른 결과”로 해석하고 “P만 바꾼 엄밀한 matched 인과 실험”으로 강화하지 않는다. 특히 G.2의 reduced-budget 동일 조건 문장은 Table16 reward 비교에 대한 것이므로 Table15에 옮겨 쓰지 않는다.
- 권장 화면 표제: `TWNM · 연결 설계별 결과`; 조건: `ASA 1,000개 · SAPO 이전 · semantic judge · Overall (%) ↑`. main exact-MCQA와 같은 축·평균으로 합산하지 않는다.

### Table15 원문 내부 산술 불일치

App.D.3에 보고한 수준별 항목 수385/279/336으로 Table15의 수준별 백분율을 가중하면 P0=39.4523, P1=46.7759, P2=52.4109가 된다. Table15 Overall39.20/46.40/52.10과 일치하지 않는다. 따라서 위 세 값은 **원문 보고 Overall**로만 전사하고, 분모별 정답 수를 우리가 복원하거나 수준별 분모를 확정한 것으로 표현하지 않는다. Table15 caption의 “1,000항목”은 저자의 보고 설명이다.

### 추가 해석 주의

- Spatial-Omni zero/null-spatial 변형의 적용 시점(학습부터/추론 시)과 full 모델과의 checkpoint 공유는 원문에 명확하지 않다. Table2를 고정 checkpoint의 추론 시 제거 실험으로 단정하지 않는다.
- PhaseCoder Task4의 WER는 공간 조건으로 목표 화자를 골라 전사하는 **targeted transcription**이다. 일반 mono ASR/기존 의미 능력의 독립적인 보존 시험은 아니다. 선택·결속과 전사 오류가 섞이므로 관계 QA 향상과 다른 과제의 상반된 결과로 읽는다. 일반 의미 능력 보존에는 별도의 일반 audio benchmark가 필요하다.

## 8. 현재 연구사 설명 위치와 검수

S15의 전체 지도와 S16의 두 입력 경로를 본 뒤 S17–S18의 E/P/LM·LoRA 틀을 익힌다. S22–S27의 2024–2025년 분화, S28–S36의 기존 Audio-LM 공간 확장, S37–S41의 동적 상태 표현을 그 관점에서 읽는다. S42–S49는 표현·전달·답변의 서로 다른 검증 범위를 회수한다. BAT의 출발은 2024년이며 채택한 v4의 2026년 개정일과 구별한다. Motion은 OWL 이후가 아니라 2025년 9월의 동시기 대안이다.

PhaseCoder v2 §4.2·App.K의 zero-shot baseline은 추정 좌표 시계열을 text arrays로 전달하고, 제안 모델은 spatial soft tokens와 P/LoRA 적응을 사용한다. 같은 논문에서 두 인터페이스를 관찰할 수 있지만 학습량과 모델 상태가 같은 순수 인터페이스 ablation은 아니다. [원문](https://arxiv.org/html/2601.21124v2)

Q-Former 내부 cross-attention, Motion의 지각부 audio↔class-text 결합, LM decoder에 추가하는 cross-attention을 구별한다. 여러 후속 논문의 BAT 관련 서술을 그대로 옮겨 “BAT는 단일 음원만 다룬다” 또는 “encoder가 coarse bins만 쓴다”고 단정하지 않는다. BAT의 multi-source QA와 1° 공간 encoder 분류 목표는 존재하며, 한계는 실제 정적 합성 QA·질문 범위로 특정한다.

직전 80장 검수 기록은 `output/qa/localization/`에 보존된다. 이번 85장 내보내기·렌더 검수 상태와 최종 산출물 경로는 `output/manifest.json` 및 해당 산출물 검수 기록을 따른다. 이 문서 갱신 자체가 최종 파일의 검수 완료를 뜻하지 않는다.
