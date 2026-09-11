# MC Audio-LM의 연구사: 입력 인터페이스와 학습 대상

검증일: 2026-09-11. 현재 덱의 P12–P22 지정 버전, arXiv 제출 이력, 원문 Methods/Related work를 확인했다. 논문의 최초 공개일과 덱에서 사용하는 수정 버전의 날짜를 분리한다. 아래 화살표는 성능 순위가 아니라 저자가 명시한 설계 계승 또는 문제의 분화다. web 도구의 인증 만료 뒤 arXiv HTML/abs를 직접 취득해 확인했으며, 새로 취득한 파일은 이 디렉터리에 보관했다.

## 1. 먼저 고정해야 할 역사적 순서

| 최초 공개일 | 논문 | 덱의 채택 버전 | 날짜 근거 |
|---|---|---|---|
| 2024-02-02 | BAT | v4, 2026-08-13 | [제출 이력](https://arxiv.org/abs/2402.01591) |
| 2025-09-17 | DSpAST | v1; 이후 v2는 2025-11-01 | [제출 이력](https://arxiv.org/abs/2509.13927) |
| 2025-09-18 | Spatial Audio Motion Understanding and Reasoning | v1 | [제출 이력](https://arxiv.org/abs/2509.14666) |
| 2025-09-30 | OWL | v1 | [제출 이력](https://arxiv.org/abs/2509.26140) |
| 2025-10-07 | Sci-Phi | v1 | [제출 이력](https://arxiv.org/abs/2510.05542) |
| 2026-01-06 | The World is Not Mono (TWNM) | v3, 2026-05-10 | [제출 이력](https://arxiv.org/abs/2601.02954) |
| 2026-01-28 | PhaseCoder | v2, 2026-08-05 | [제출 이력](https://arxiv.org/abs/2601.21124) |
| 2026-02-18 | Dynamic Source Movements QA | v1 | [제출 이력](https://arxiv.org/abs/2602.16334) |
| 2026-06-09 | Spatial-Omni | v2, 2026-09-07 | [제출 이력](https://arxiv.org/abs/2606.10738) |
| 2026-06-12 | ST-AudioLM | v1 | [제출 이력](https://arxiv.org/abs/2606.14141) |
| 2026-07-09 | Dual-BEATs | v1 | [제출 이력](https://arxiv.org/abs/2607.08800) |

**Motion은 OWL 이후에 등장한 해결책이 아니다.** 둘은 2025년 9월의 서로 다른 접근이고 Motion이 12일 먼저 공개됐다. BAT의 2026년 v4 날짜로 BAT를 후반에 배치해서도 안 된다. BAT v1 원문에도 이미 Spatial-AST → projection → LLaMA-2와 LLaMA-Adapter V2, perception-to-reasoning curriculum이 명시돼 있다. [BAT v1 §4.2·§5.1](https://arxiv.org/html/2402.01591v1)

## 2. 실제 계승과 연구 질문

| 논문 | 저자가 명시한 선행 작업과 바꾼 지점 | 연구사에서의 역할 |
|---|---|---|
| BAT | AudioMAE에서 초기화한 Spatial-AST를 사건·방향·거리 목표로 학습하고, 출력 토큰을 LLaMA-2의 입력 임베딩으로 투영. 지각→여러 음원→관계 QA curriculum. | **위치를 예측하는 음향 모델의 표현을 언어 질문에 재사용하는 초기 공간 Audio-LM.** 좌표를 추정한 뒤 수치만 넘기는 구조가 아님. 저자는 최초 spatial audio-based LLM으로 소개하므로 발표에서는 “초기 대표 모델” 또는 “저자가 최초로 제시한”으로 한정. [v1 §1·4.1·4.2](https://arxiv.org/html/2402.01591v1) |
| DSpAST | §2가 BAT/Spatial-AST를 직접 검토하고 §3가 명시적으로 확장이라고 설명. ILD/GCC 추가, 과제별 feature attention/분기, 공유 backbone, 크기를 맞춘 표현. | **같은 LM 연결에서 E가 사건·방향·거리를 함께 담는 방식을 개선.** 파라미터를 크게 키우는 발전사보다 “과제별로 필요한 물리 단서가 다르다”는 질문. [§2–3·4.2](https://arxiv.org/html/2509.13927v1) |
| Motion 2025 | §1에서 BAT의 학습 비용·정적 음원 범위를 동기로 제시. DSAST는 BAT 전처리를 따르고 AGM을 결합하나, 추론은 예측 속성을 JSON으로 만들어 별도 LLM에 전달. | **동적 음원 정보를 명시적인 사건별 시계열로 내보내는 대안.** LM이 오디오 임베딩을 직접 해석하도록 학습하는 경로와 분기. [§1·2.1–2.2](https://arxiv.org/html/2509.14666v1) |
| OWL | §4에서 BAT의 mel/IPD 입력을 따름. §5에서 BAT와 같은 LLaMA-2를 사용한다고 명시. SAGE에 depth/RIR 보조 감독, Q-Former와 CoT curriculum. | **직접 오디오 토큰 통합을 유지하면서 E의 기하 감독과 답변 학습을 개선.** CoT가 있어도 외부 좌표 JSON 경유형으로 분류하지 않음. [§4–5·Fig.4](https://arxiv.org/html/2509.26140v1) |
| Sci-Phi | Phi-4-Multimodal을 바탕으로 기존 mono 의미 경로를 유지. SELDNet 구조/checkpoint를 공간 경로로 가져와 적응. BAT는 관련 연구/비교 범위이고 BAT backbone을 계승한 모델은 아님. | **공간 전용 Audio-LM에서 기존 Audio-LM의 공간 확장으로 질문이 이동.** 전체 장면의 What/Where/When, 배경·방 특성을 함께 기술. [§1·3.1–3.3·Fig.1](https://arxiv.org/html/2510.05542v1) |
| TWNM v3 | 기존 공간 QA/SELD를 토대로 FOA 공간 표현과 Whisper 의미 표현을 결합. Audio-Flamingo-3 계열 Qwen2.5-7B decoder. | **의미·공간 정보를 음원에 결속시켜 복합 질문까지 학습하는 문제.** dense hybrid projector, SFT, SAPO를 서로 다른 변경으로 읽음. v3의 FOA/SAPO를 1월 v1의 방법으로 소급하지 않음. [§2–3·App.E](https://arxiv.org/html/2601.02954v3) |
| PhaseCoder v2 | §2는 BAT를 가장 가까운 soft spatial embedding 방식으로 지목. mono USM 경로가 있는 Gemma 3n에 임의 배열의 마이크 좌표·위상 표현을 더함. | **같은 공간 표현이 특정 하드웨어에 묶이지 않게 하기.** 기존 speech/mono 경로와 공간 경로의 보완 관계. [§2·3.3·4.2](https://arxiv.org/html/2601.21124v2) |
| Dynamic QA 2026 | §3.2가 BAT 공간 encoder의 penultimate layer를 시간 인식에 맞게 수정했다고 명시. Q-Former→Qwen3-4B thinking과 결합. | **정적 공간 QA를 동적 장면과 질문 관련 구간 선택으로 확장.** Motion 2025와 저자 세 명이 같지만 본문에서 Motion 파이프라인의 직접 계승은 확인되지 않았으므로 실선 계승 화살표는 BAT에서 연결. [§3.2·4·5](https://arxiv.org/html/2602.16334v1) |
| Spatial-Omni v2 | 원래 Omni audio tower와 별도 SO-Encoder를 병렬로 두고 여러 backbone에 적용. §5.1은 BAT의 class-first→spatial 학습 경험을 따른다고 명시. 관련 연구는 Sci-Phi, PhaseCoder, TWNM의 공간 경로를 구별. | **기존 모델의 의미 능력을 유지하면서 공간 입력을 이식하는 절차와 범용성.** 단일 새 모델보다 여러 Audio/Omni LM에 적용하는 인터페이스를 비교. [§2.2·3·5.1·App.C](https://arxiv.org/html/2606.10738v2) |
| ST-AudioLM | §5.1에서 BAT의 Spatial-AST backbone을 FOA에 적응했다고 명시. §2에서 Dynamic QA를 동시기 연구로 인용하면서 dedicated trajectory tokens를 차이로 제시. | **시간에 따라 바뀌는 음원의 상태를 어떤 토큰 구조에 남길 것인가.** 같은 41-token baseline으로 단순 토큰 개수와 학습한 시간 표현을 구별. [§2·4·5.1·Table5](https://arxiv.org/html/2606.14141v1) |
| Dual-BEATs | BAT·PhaseCoder·TWNM의 전용 공간 경로를 관련 연구로 설명하고, frozen BEATs를 좌우에 독립 적용하는 대안을 제시. | **전용 공간 E 없이도 어떤 단서까지 보존할 수 있는가.** amplitude-panned single-source stereo와 dither 효과의 제한된 진단. 자연 HRTF/임의 배열/겹친 음원의 해결로 확대하지 않음. [§2·3·5](https://arxiv.org/html/2607.08800v1) |

## 3. LM이 무엇을 받는가와 무엇을 학습하는가

E=오디오 인코더, P=연결 모듈, LM=언어 모델. `LM+LoRA`는 기반 가중치 전체를 갱신한다는 뜻이 아니다. encoder 사전학습과 QA 적응을 분리한다.

| 방법 | 추론 때 LM에 들어오는 공간 정보 | QA/연결 학습에서 실제로 바꾸는 것 | 확인할 섹션 |
|---|---|---|---|
| BAT v1/v4 | Spatial-AST의 연속 출력 토큰을 text embedding 차원으로 projection | P 및 LLaMA-Adapter V2의 zero-init attention/norm/bias/scale 등. QA E의 동결 상태는 본문만으로 확정하지 않음. 저자 공개 Q-Former+LoRA 구현과 논문 실험을 혼합하지 않음. | §4.2·5.1 |
| DSpAST | 과제별 분기 표현→Q-Former→LLaMA-2 | 공간 사전학습 후 E 고정; P 및 LM LoRA QA 학습 | §2·4.2 |
| Motion 2025 | 예측 Event/DoA/Distance/Time frames를 담은 **JSON의 텍스트 토큰** | DSAST E는 학습, AGM은 고정. 추가 reasoning LM 연결은 training-free. P/LM LoRA를 필수 블록으로 그리지 않음. | §2.1–2.2·3.2 |
| OWL | SAGE 연속 특징→Q-Former의 query tokens→LLaMA-2 | 기하 감독으로 E 사전학습 후 E 고정; P+LM LoRA, perceptual→relation→CoT curriculum | §4–5, App.B–C |
| Sci-Phi | 별도 spatial/audio embeddings를 텍스트와 함께 입력 | 기존 mono E/P/audio LoRA 고정. 공간 E/P/new spatial LoRA 학습 | §3.1·3.3 |
| TWNM v3 | FOA 공간 map+W Whisper 특징→dense hybrid projector→연속 audio tokens | 공간 E 학습/적응→E/LM 고정 P 정렬→P+LoRA SFT→SAPO LoRA. source slots 자체가 3개 LLM object token이라는 해석은 잘못. | §3, App.E |
| PhaseCoder v2 | 공간 soft tokens를 기존 mono audio tokens 앞에 추가 | 새 P와 Gemma LoRA. 원래 USM 경로 유지. 공간 E의 QA 동결 여부는 본문/공개 encoder 코드에서 미확정. | §3.3 |
| Dynamic QA 2026 | 시간 인식 encoder→Q-Former→Qwen3-4B | 첫 단계 E 고정 및 P 정렬; 두 번째 E/P/LM LoRA 학습. 첫 단계 LM 동결은 정확한 문구가 충분하지 않아 별도 확정 금지. | §3.2·5.2 |
| Spatial-Omni v2 | 기존 audio tokens+별도 spatial tokens | ①P ②P+LM LoRA ③P+LoRA+공간 E의 학습 가능한 부분. 원래 audio tower는 기본 설정에서 고정. | §5.1, App.C.3 |
| ST-AudioLM | 의미 1+시간 40의 연속 토큰→2층 MLP→OLMo2 | 공간/시간 E 사전학습 후 E와 base LM 고정, P+LoRA | §4.1–4.2·5.1 |
| Dual-BEATs | 좌우 BEATs의 시간 정렬 feature concat→P | 두 E 고정, P+QLoRA. Table5는 embedding/lm_head도 modules_to_save에 포함하므로 “LoRA만 학습” 금지. | §3, App.B |

**PhaseCoder의 같은 논문 안에 두 경로가 함께 있다.** §4.2와 Appendix K의 Zero-Shot Gemma baseline은 PhaseCoder가 추정한 azimuth/elevation/distance 배열을 160ms 간격으로 텍스트화해 해석 지침과 함께 전달한다. 제안 방법은 예측 좌표 대신 연속 공간 표현을 주고 P/LoRA를 학습한다. 따라서 “구조화된 관측을 말로 전달 / 비언어 표현을 직접 연결”의 예시가 된다. 학습량이 맞춰진 순수 인터페이스 비교라는 주장은 피한다. 이 baseline은 채택한 v2의 설명이다. [PhaseCoder §4.2·App.K](https://arxiv.org/html/2601.21124v2)

## 4. 발표에서 사용할 짧은 역사 서사

1. **BAT에서 출발:** 위치를 추정하는 encoder의 특징을 projector로 LM에 연결하면 “몇 도인가”를 넘어 “어느 소리가 다른 소리의 왼쪽인가”를 물을 수 있다. 여기서 공간 Audio-LM의 직접 연결 틀이 등장한다.
2. **2025년에는 두 질문이 갈라진다:** DSpAST/OWL은 LM에 넘길 E가 무엇을 배워야 하는지 묻는다. 전자는 과제별 신호 특징, 후자는 기하 감독을 개선한다. 같은 시기의 Motion은 E가 추정한 사건별 좌표 시계열을 먼저 JSON으로 명시하고 LM의 기존 언어 추론을 사용한다. OWL의 CoT는 이 JSON 경로가 아니다.
3. **Sci-Phi 이후 기존 Audio-LM에 공간 경로를 더한다:** 풍부한 mono 의미/음성 능력이 이미 있으므로 그것을 유지한 채 공간 E/P/적응 경로를 병렬로 붙인다. PhaseCoder는 하드웨어 기하, Spatial-Omni는 여러 backbone 이식과 능력 보존, TWNM은 음원별 결속과 복합 QA의 학습을 각기 묻는다. 이들은 동일한 단일 계보라기보다 관련된 설계 질문이다.
4. **정적 장면에서 동적 상태로:** 2025 Motion은 명시적 시계열, 2026 Dynamic QA는 시간 인식 encoder+Q-Former+thinking, ST-AudioLM은 trajectory supervision+시간 토큰을 택한다. “어떤 소리인가/어디인가”에서 “어느 소리가 언제 어디로 이동했는가”로 필요한 표현이 바뀐다.
5. **마지막 평가는 세 경계를 나눠 묻는다:** E에 위치·사건·시간이 함께 남는가 → P/JSON이 필요한 관계를 전달하는가 → LM의 답이 실제 오디오 변화에 맞게 바뀌는가. 단순 QA 점수의 연대별 상승 그래프로 대체하지 않는다.

## 5. 화살표와 표현의 경계

- 실선으로 표시해도 되는 명시 계승: **BAT/Spatial-AST→DSpAST**, **BAT 입력/LM 틀→OWL**, **BAT encoder→Dynamic QA**, **BAT backbone→ST-AudioLM**. PhaseCoder는 BAT를 가장 가까운 soft-embedding 전례로 인용하지만 E 자체는 별도로 설계한다.
- **Phi-4-MM→Sci-Phi**, **Gemma3n→PhaseCoder 통합**, **Qwen/여러 Omni backbone→Spatial-Omni**, **AF3 계열 decoder→TWNM v3**는 실제 기반 모델의 결합 관계다.
- Sci-Phi→PhaseCoder→Spatial-Omni를 하나의 모델을 순차 개량한 실선 계보로 그리지 않는다. 공통 문제인 “기존 의미 경로+새 공간 경로”로 묶되 저자/구현 계승은 구별한다.
- **LM 표현공간 확장**을 사용할 경우 “비언어 오디오 입력 표현의 종류를 넓힌다”로 정의한다. 이 모델들은 대개 같은 LM 차원의 연속 임베딩을 입력하며 hidden width나 vocabulary 증가가 필수는 아니다. PhaseCoder의 경계 표지는 기존 미사용 token ID를 재사용한다.
- **CoT는 추론/출력 학습 방식, JSON은 입력 인터페이스, LoRA는 가중치 적응 방식**이다. 세 이름을 서로 배타적인 방법 분류로 나열하지 않는다.
- Q-Former 내부 cross-attention, Motion 지각부의 audio↔class-text cross-attention, LM decoder에 추가하는 cross-attention은 서로 다른 위치다. Motion/OWL을 이유 없이 “cross-attention형 LM”으로 묶지 않는다.
- 일부 후속 논문은 BAT를 “single-source only/coarse localization”로 지나치게 단순화한다. BAT에는 multi-source Type C/D/E와 encoder의 1° 분류 목표가 있다. 발표자는 후속 저자의 비판을 그대로 사실화하지 말고 **정적 합성 QA 범위, 질문의 범주화, 환경/동적 일반화**로 구체화한다.
- ELSA/SALM/CoSTALA의 audio–text alignment/retrieval은 이 생성 LM 통합 계보의 비교 축이지 projector+LoRA 모델이라고 그릴 대상이 아니다.

## 확인한 로컬 근거

- 기존 원문 텍스트: `tmp/causal-llm-module-research/2402.01591v4.txt`, `2509.13927v1.txt`, `2509.26140v1.txt`, `2510.05542v1.txt`, `2601.02954v3.txt`, `2601.21124v2.txt`, `2606.10738v2.txt`, `2606.14141v1.txt`, `2607.08800v1.txt`.
- 이번 추가 원문: `tmp/mc-history/2402.01591v1.html/.txt`, `2509.14666v1.html/.txt`, `2602.16334v1.html/.txt`.
- 이번 최초 공개일 검증: 각 arXiv ID의 `tmp/mc-history/*.abs.html` 제출 이력.
- 기존 근거 대장과 대조: `plans/EVIDENCE_P12_P23.md`, `plans/CAUSAL_LLM_MODULES.md`.
