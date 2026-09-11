---
layout: "seminar"
variant: "figure"
chapter: "03 · 2024–2025: 공간 QA의 출발과 분화"
causalStage: "main"
---

# BAT: 공간 지각의 표현을 질문의 입력으로 바꾼다

::body::
<PaperFigure src="/diagrams/history-bat.svg" alt="일반 Audio-LM의 encoder→projection→LM 연결을 공간 지각에 적용한 초기 대표 모델이다. 공간 좌표를 텍스트로만 직렬화하는 모델이 아니며 기하 인코더 사전학습과 공간 QA 적응을 구별한다." />

::takeaway::
BAT의 전환은 **공간 속성을 배우던 인코더의 표현을 언어 질문에 재사용**한 데 있다.

::source::
Pengi 2023 §3 · BAT 최초 공개 v1 §4–5; 결과 장은 지정 v4 사용.

<!--
[현재 S22 · 본문]
03 · 2024–2025: 공간 QA의 출발과 분화

[설명의 중심]
일반 Audio-LM의 encoder→projection→LM 연결을 공간 지각에 적용한 초기 대표 모델이다. 공간 좌표를 텍스트로만 직렬화하는 모델이 아니며 기하 인코더 사전학습과 공간 QA 적응을 구별한다.

[연결]
다음에 확인할 질문: BAT 2024: 공간 입력은 관계 질문에 기여했는가?

[상세 근거와 해석 범위]
[Sources]
- https://arxiv.org/abs/2305.11834
- https://arxiv.org/html/2402.01591v1
- https://arxiv.org/html/2402.01591v4

[그림]
이 그림은 원문 Methods에 근거한 교육용 재구성으로 실제 activation이나 성능 측정 그림이 아니다. 최초 공개 연대와 채택 버전은 plans/MC_AUDIO_LM_HISTORY.md에 구분하여 기록했다. 화살표는 그림 내부의 데이터 흐름이며 논문 간 성능 상승을 뜻하지 않는다.

[연구사와 발표 노트]
Audio encoder의 특징을 연속 입력으로 바꾸어 언어 모델과 연결하는 틀은 일반 Audio-LM에도 있다. Pengi 2023은 학습 가능한 audio encoder와 mapping network로 frozen GPT2에 prefix를 연결한다. 이 배경 사례는 연속 오디오 입력 추가가 LM LoRA를 필수로 요구하지 않음을 보여주며 27개 핵심 공간 문헌의 추가 성능 비교로 세지 않는다.
BAT는 AudioMAE 기반 Spatial-AST에 binaural mel/IPD를 주고 사건·방향·거리의 지각 목표로 공간 표현을 학습한다. projection으로 text embedding 차원에 맞춘 출력 특징을 질문과 LLaMA2에 제공한다. 지각에서 다중 음원·관계 질문으로 확장하는 perception-to-reasoning 학습을 사용한다. BAT에도 다중 음원 C/D/E 질문이 있으므로 후속 논문의 정적 장면 한계를 단일 음원 전용이었다는 뜻으로 바꾸지 않는다.
BAT v1/v4 본문은 LLaMA-Adapter V2의 projection 및 zero-init attention, norm/bias/scale 등 적응을 설명한다. 공개 SLAM-LLM 실행 구성의 Q-Former+LoRA와 논문 결과를 동일한 세부 구현으로 합치지 않는다. 그림의 LM 적응은 이 공통 역할만 뜻한다. BAT의 연구사적 의미는 기존 음향 모델의 좌표 출력만 읽는 것을 넘어 공간 표현을 직접 질문 조건부 생성에 재사용하는 초기 공간 Audio-LM의 대표 틀이라는 점이다.
-->

---
layout: "seminar"
variant: "result"
chapter: "03 · 2024–2025: 공간 QA의 출발과 분화"
causalStage: "main"
originSlide: 39
---

# BAT 2024: 공간 입력은 관계 질문에 기여했는가?

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">SpatialSoundQA · 두 음원의 관계 Yes/No · 같은 최종 BAT</p>
<PaperFigure src="/diagrams/result-39.svg" alt="관계 질문 · 평균 BA (%) ↑ 원문 수치 비교 그래프. P · 질문만: 54.48; B + P · 바이노럴 + 질문: 76.89" />
</div>

::takeaway::
이 평가에서 **바이노럴 입력을 제공한 조건**의 관계 QA 점수가 더 높다.

::source::
BAT, arXiv:2402.01591v4, Table 4의 최종 BAT 두 입력 행. 원문 수치의 그래프 재구성.

<!--
[현재 S23 · 본문]
03 · 2024–2025: 공간 QA의 출발과 분화

[설명의 중심]
BAT Table 4는 question-only 대비 binaural input의 실제 추가 기여를 관찰한 근거다.

[연결]
다음에 확인할 질문: 같은 연결 틀에서, 인코더가 배워야 할 것을 바꾼다

[상세 근거와 해석 범위]
[S23]
[Sources]
- https://arxiv.org/html/2402.01591v4
[발표 노트]
표의 P는 prompt, B는 binaural을 뜻한다. 같은 최종 BAT에 질문만 주는 경우와 질문·오디오를 함께 주는 경우를 읽는다. Type E는 두 음원 관계의 Yes/No 질문이며 평균 balanced accuracy로 평가한다. 질문만으로도 54.48%가 남고 바이노럴을 제공하면 76.89%로 높아진다. 공간 인코더의 사전학습과 perception-to-reasoning 언어 연결 학습을 구분해야 한다.
[해석 범위]
AudioSet 원음을 SoundSpaces RIR로 공간화한 10초 합성 바이노럴 조건이다. mono 행은 stage III만 학습한 모델이므로 여기의 최종 three-stage 모델과 입력만 다른 통제가 아니다. 이 결과는 청각 관측의 유용성을 보이지만 특정 위상 단서의 인과효과는 분리하지 않는다.

[시각화 전 표의 수치·조건 보존]
SpatialSoundQA · 두 음원의 관계 Yes/No · 같은 최종 BAT

모델에 제공한 입력 | Type E 평균 BA (%) / 높을수록 좋음 | 

P · 질문만 | 54.48 | 

B + P · 바이노럴 + 질문 | 76.89 |
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "03 · 2024–2025: 공간 QA의 출발과 분화"
causalStage: "main"
---

# 같은 연결 틀에서, 인코더가 배워야 할 것을 바꾼다

::body::
<PaperFigure src="/diagrams/history-encoder-branches.svg" alt="2025년 DSpAST와 OWL은 BAT의 공간 표현 문제를 각각 과제별 단서 선택과 방 기하 감독으로 확장한다. 둘의 공통 기반과 다른 학습 개입을 먼저 보여 준 뒤 각 내부 비교를 읽는다." />

::takeaway::
같은 공간 QA 틀에서도 **어떤 신호 단서를 넣고 어떤 목표로 E를 학습하는지**가 다르다.

::source::
DSpAST v1 §2–4 · OWL v1 §4–5 · BAT 기반의 명시적 확장/참조.

<!--
[현재 S24 · 본문]
03 · 2024–2025: 공간 QA의 출발과 분화

[설명의 중심]
2025년 DSpAST와 OWL은 BAT의 공간 표현 문제를 각각 과제별 단서 선택과 방 기하 감독으로 확장한다. 둘의 공통 기반과 다른 학습 개입을 먼저 보여 준 뒤 각 내부 비교를 읽는다.

[연결]
다음에 확인할 질문: DSpAST 2025: 같은 LM 연결에서 인코더를 비교한다

[상세 근거와 해석 범위]
[Sources]
- https://arxiv.org/html/2509.13927v1
- https://arxiv.org/html/2509.26140v1

[그림]
이 그림은 원문 Methods에 근거한 교육용 재구성으로 실제 activation이나 성능 측정 그림이 아니다. 최초 공개 연대와 채택 버전은 plans/MC_AUDIO_LM_HISTORY.md에 구분하여 기록했다. 화살표는 그림 내부의 데이터 흐름이며 논문 간 성능 상승을 뜻하지 않는다.

[연구사와 발표 노트]
DSpAST는 BAT Spatial-AST를 확장하여 ILD/GCC 등의 특징, feature attention, 의미·방향·거리별 표현을 설계한다. patch embedding과 Transformer backbone 공유를 유지하며 사전학습 curriculum과 AdaCos loss도 달라진다. 따라서 이후 QA 비교를 attention 블록 하나의 인과 효과로 읽지 않는다. QA에서는 E를 고정하고 P와 LM LoRA를 학습한다.
OWL은 BAT의 mel/IPD 입력과 LLaMA2 연결을 참조하면서 SAGE의 사전학습에 depth와 RIR 재구성 감독을 도입한다. 이 정보는 사전학습에만 사용하며 QA 추론에서는 binaural audio만 받는다. E를 고정한 후 Q-Former와 LoRA를 학습하며 perceptual→relation→CoT curriculum을 쓴다. 두 논문이 LM 인터페이스의 큰 틀을 유지하면서 encoder가 남기는 공간 정보를 바꾼다는 질문으로 읽는다.
이후 DSpAST 장의 Table3는 같은 single-stage BAT 연결에서 encoder 설계/사전학습을 비교한 QA 결과이다. OWL 장의 Table5는 SAGE의 geometry loss에 따른 위치 판독 결과이며 QA 또는 LoRA 효과를 직접 비교한 표가 아니다. 두 평가의 결과 수준을 혼동하지 않는다.
-->

---
layout: "seminar"
variant: "result"
chapter: "03 · 2024–2025: 공간 QA의 출발과 분화"
causalStage: "main"
originSlide: 41
---

# DSpAST 2025: 같은 LM 연결에서 인코더를 비교한다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">합성 바이노럴 · single-stage BAT · 전체 질문 5 epochs, LoRA, greedy decoding</p>
<PaperFigure src="/diagrams/result-41.svg" alt="방향 정확도 (%) ↑
Type D · 8범주, DER (%) ↓
거리 오차 > 0.5 m, 관계 평균 BA (%) ↑
Type E 원문 수치 비교 그래프. SpatialAST: 34.80, 53.40, 74.04; DSpAST: 37.35, 48.51, 76.56" />
</div>

::takeaway::
LLM 인터페이스를 맞춘 비교에서 **인코더 설계·사전학습의 기여**를 읽는다.

::source::
DSpAST, arXiv:2509.13927v1, Table 3의 single-stage 두 행. ↑ 높을수록, ↓ 낮을수록 좋음.

<!--
[현재 S25 · 본문]
03 · 2024–2025: 공간 QA의 출발과 분화

[설명의 중심]
DSpAST의 matched QA interface 결과는 새 feature encoder의 기여에 해당한다. 특정 물리 단서 하나만 분리한 실험은 아니다.

[연결]
다음에 확인할 질문: OWL 2025: 기하 감독은 위치 추정에 기여했는가?

[상세 근거와 해석 범위]
[S25]
[Sources]
- https://arxiv.org/html/2509.13927v1
[발표 노트]
앞 장의 설계가 최종 언어 질문에도 유용한지 읽는다. 먼저 Type D의 목표 음원 방향 정확도는 34.80에서 37.35%로 높아지고, 거리 오차가 0.5m를 넘는 비율 DER는 53.40에서 48.51%로 낮아진다. 두 음원 관계 Type E의 평균 BA도 74.04에서 76.56%로 높아진다. 방향 정확도, 거리 실패 비율, 관계 판단은 서로 다른 지표라 단순 합산하지 않는다.
[해석 범위]
이 비교에서는 인코더 특징뿐 아니라 사전학습 curriculum과 AdaCos loss도 다르다. 차이 전체를 세 분기에 귀속할 수 없다. 원 BAT와 checkpoint 및 의미 평가 embedding이 달라 S23 수치와 직접 연결하지 않는다. 원문의 질문 유형 설명 일부 오기는 BAT의 유형 정의를 따른다.

[시각화 전 표의 수치·조건 보존]
합성 바이노럴 · single-stage BAT · 전체 질문 5 epochs, LoRA, greedy decoding

인코더 | 방향 정확도 (%) ↑ / Type D · 8범주 | DER (%) ↓ / 오차 > 0.5 m 비율 | 관계 평균 BA (%) ↑ / Type E | 

SpatialAST | 34.80 | 53.40 | 74.04 | 

DSpAST | 37.35 | 48.51 | 76.56 |
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->

---
layout: "seminar"
variant: "result"
chapter: "03 · 2024–2025: 공간 QA의 출발과 분화"
causalStage: "main"
originSlide: 44
---

# OWL 2025: 기하 감독은 위치 추정에 기여했는가?

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">BiDepth 합성 평가 · 추론 입력은 바이노럴 · 기하 지도 loss 비교</p>
<PaperFigure src="/diagrams/result-44.svg" alt="방향 MAE (°) ↓, 거리 DER (%) ↓ 원문 수치 비교 그래프. 바이노럴 loss · $\eta_2=0$: 26.32, 17.11; 전체 loss · $\eta_2=10^{-2}$: 21.67, 14.32" />
<p class="seminar-chart-note">DER: 거리 오차가 0.5 m를 넘는 비율</p>
</div>

::takeaway::
이 표의 개입은 **인코더의 geometry loss**다. 어댑터·LoRA·CoT 효과를 뜻하지 않는다.

::source::
OWL, arXiv:2509.26140v1, Table 5. DER: 거리 오차가 0.5 m를 넘는 비율.

<!--
[현재 S26 · 본문]
03 · 2024–2025: 공간 QA의 출발과 분화

[설명의 중심]
OWL Table 5는 SAGE의 geometry loss에 대한 공간 예측 ablation이다. projector나 CoT·LoRA의 효과로 섞지 않는다.

[연결]
다음에 확인할 질문: Motion 2025: 지각 결과를 JSON으로 넘기는 대안

[상세 근거와 해석 범위]
[S26]
[Sources]
- https://arxiv.org/html/2509.26140v1
[발표 노트]
여기서는 전체 QA 시스템의 성능 차이보다 좁게 SAGE loss를 비교한다. 바이노럴 항만 사용한 η₂=0과 기하 항을 포함한 η₂=10⁻² 조건이다. 방향 MAE는 26.32도에서 21.67도로, 거리 오차가 0.5m를 넘는 DER는 17.11%에서 14.32%로 줄었다. 낮은 값이 좋은 두 오차 지표를 함께 읽는다.
[해석 범위]
이 수치를 CoT나 projector의 효과로 섞지 않는다. 또한 모든 전이 지표가 좋아지는 것은 아니다. Table 2의 SSQA MAE는 geometry SAGE 18.47도가 Spatial-AST 17.94도보다 높다. Table 4 QA 전체 시스템 비교와 Table 6 CoT 비교는 별도의 실험이다.

[시각화 전 표의 수치·조건 보존]
BiDepth 합성 평가 · 추론 입력은 바이노럴 · 기하 지도 loss 비교

SAGE의 학습 조건 | 방향 MAE (°) / 낮을수록 좋음 | 거리 DER (%) / 낮을수록 좋음 | 

바이노럴 loss · $\eta_2=0$ | 26.32 | 17.11 | 

전체 loss · $\eta_2=10^{-2}$ | 21.67 | 14.32 |
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->

---
layout: "seminar"
variant: "result"
chapter: "03 · 2024–2025: 공간 QA의 출발과 분화"
causalStage: "main"
originSlide: 60
---

# Motion 2025: 지각 결과를 JSON으로 넘기는 대안

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">학습한 지각 결과 → JSON → 같은 Qwen-7B 추론 모델 · QA 정확도 (%) ↑</p>
<PaperFigure src="/diagrams/result-60.svg" alt="DoA·trajectory, Overall 원문 수치 비교 그래프. DSAST + Qwen7B: 35.8, 20.7; DSAST w/ AGM + Qwen7B: 26.4, 31.1" />
</div>

::takeaway::
AGM 결합 경로의 **전체 QA는 개선됐지만 방향·궤적 질문은 낮아졌다.**

::source::
Spatial Audio Motion Understanding and Reasoning, arXiv:2509.14666v1, Table 3. ↑ 높을수록 좋음.

<!--
[현재 S27 · 본문]
03 · 2024–2025: 공간 QA의 출발과 분화

[설명의 중심]
Motion 2025는 속성 추정과 LLM 추론을 잇는 경로로, 연속 audio token 결합과 구분한다.

[연결]
다음에 확인할 질문: 기존 Audio-LM을 살리고 공간 경로를 붙이는 문제

[상세 근거와 해석 범위]
[S27]
[Sources]
- https://arxiv.org/html/2509.14666v1
[발표 노트]
언어 모델이 원 파형을 직접 듣는 경로가 아니라 지각 모델의 시간별 예측을 JSON으로 읽는 구조다. 동일한 DeepSeek-R1-distilled Qwen-7B와 greedy decoding을 사용한 두 행을 고른다. DSAST에 AGM을 결합하면 Overall은 20.7에서 31.1%로 높아진다. 그러나 DoA·trajectory는 35.8에서 26.4%로 낮아진다. 이를 모든 움직임 질문의 개선으로 요약하지 않는다.
[해석 범위]
지각 인코더와 AGM은 학습하며 training-free는 추가 추론 LLM 연결에 관한 표현이다. stereo STARSS23 기반 시간별 예측을 사용하고 QA는 STARSS23 test metadata에서 만든 Boolean·single-answer MCQ다. 정답 속성을 넣는 oracle 결과와 혼합하지 않는다. Table 2 미관측 클래스 encoder 평가는 이 QA 표와 별개다. 본문 문장의 일부 모델명보다 정확한 표 행을 따른다.

[시각화 전 표의 수치·조건 보존]
학습한 지각 결과 → JSON → 같은 Qwen-7B 추론 모델 · QA 정확도 (%) ↑

지각 → 추론 경로 | DoA·trajectory | Overall | 

DSAST + Qwen7B | 35.8 | 20.7 | 

DSAST w/ AGM + Qwen7B | 26.4 | 31.1 |
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "04 · 2025–2026: 기존 Audio-LM에 공간 경로를 더한다"
causalStage: "main"
---

# 기존 Audio-LM을 살리고 공간 경로를 붙이는 문제

::body::
<PaperFigure src="/diagrams/history-extensions.svg" alt="Sci-Phi부터 기존 의미·음성 경로와 공간 경로의 병렬 결합이 중요한 설계 질문이 된다. PhaseCoder·Spatial-Omni·TWNM은 같은 모델의 순차 개선이 아니라 배열 기하·이식 절차·음원 결속에 대한 서로 다른 선택이다." />

::takeaway::
새 공간 경로를 붙인 뒤에는 **공간 정보의 기여와 기존 의미 능력**을 함께 확인해야 한다.

::source::
Sci-Phi v1 §3 · PhaseCoder v2 §3.3 · TWNM v3 §3 · Spatial-Omni v2 §3·5.

<!--
[현재 S28 · 본문]
04 · 2025–2026: 기존 Audio-LM에 공간 경로를 더한다

[설명의 중심]
Sci-Phi부터 기존 의미·음성 경로와 공간 경로의 병렬 결합이 중요한 설계 질문이 된다. PhaseCoder·Spatial-Omni·TWNM은 같은 모델의 순차 개선이 아니라 배열 기하·이식 절차·음원 결속에 대한 서로 다른 선택이다.

[연결]
다음에 확인할 질문: Sci-Phi 2025: 기존 의미 경로 옆에 공간 경로를 학습한다

[상세 근거와 해석 범위]
[Sources]
- https://arxiv.org/html/2510.05542v1
- https://arxiv.org/html/2601.21124v2
- https://arxiv.org/html/2601.02954v3
- https://arxiv.org/html/2606.10738v2

[그림]
이 그림은 원문 Methods에 근거한 교육용 재구성으로 실제 activation이나 성능 측정 그림이 아니다. 최초 공개 연대와 채택 버전은 plans/MC_AUDIO_LM_HISTORY.md에 구분하여 기록했다. 화살표는 그림 내부의 데이터 흐름이며 논문 간 성능 상승을 뜻하지 않는다.

[연구사와 발표 노트]
이 그림은 공통 설계 질문을 추상화한다. 구체적인 토큰 순서, 경로 고정 여부, projector의 융합 위치는 논문마다 다르다. 동일한 하나의 모델 계보로 읽지 않는다.
Sci-Phi는 Phi4-Multimodal의 기존 mono 의미 encoder/projector/audio LoRA를 고정하고 공간 encoder/projector/spatial LoRA를 학습한다. What/Where/When을 같은 음원에 결속하는 기술을 목표로 한다. PhaseCoder는 위상과 마이크 좌표를 공간 encoder에 입력하고 Gemma3n의 기존 USM audio tokens 앞에 spatial soft tokens를 추가한다. P와 Gemma LoRA를 학습하지만 공간 encoder의 QA 동결 여부는 확정하지 않는다.
TWNM 채택 v3는 FOA 공간 map과 Whisper 의미 feature를 dense hybrid projector로 결합한다. source-slot 감독용 출력과 실제 LM 입력인 dense features를 구분한다. Spatial-Omni는 여러 기존 Audio/Omni backbone의 의미 경로를 유지하면서 SO-Encoder와 공간 projector를 붙이고 P→P+LoRA→P+LoRA+공간 E의 학습 단계를 비교한다.
이후 상세 장은 이 질문별로 묶었으므로 날짜순의 성능 사다리가 아니다. 첫 공개 연대는 앞의 지도에, 세부 구현은 채택 버전에 귀속한다. PhaseCoder의 공간 지정 목표 전사 WER는 일반 의미 능력 보존 평가와 다르며 Spatial-Omni의 별도 일반 오디오 평가와도 구별한다.
-->

---
layout: "seminar"
variant: "method"
chapter: "04 · 2025–2026: 기존 Audio-LM에 공간 경로를 더한다"
causalStage: "main"
originSlide: 51
---

# Sci-Phi 2025: 기존 의미 경로 옆에 공간 경로를 학습한다

::body::
<PaperFigure src="/research/sciphi-core.png" alt="Sci-Phi Fig. 1. FOA의 공간 특징과 W 채널 spectral 특징을 두 인코더·projector로 Phi-4에 결합한 원문 구조" caption="공간 경로는 적응하고, 기존 mono 의미 인코더·projector·audio LoRA는 고정한다." />

::takeaway::
**기존 의미 경로는 고정**하고 공간 encoder·projector·LoRA를 적응한다.

::source::
Sci-Phi, arXiv:2510.05542v1, Fig. 1의 인코더·projector·LLM 경로 크롭.

<!--
[현재 S29 · 본문]
04 · 2025–2026: 기존 Audio-LM에 공간 경로를 더한다

[설명의 중심]
Sci-Phi는 고정된 의미 인코더·projector·audio LoRA를 유지하며 공간 인코더·projector·spatial LoRA를 적응하는 분기 설계다.

[연결]
다음에 확인할 질문: PhaseCoder: 특정 마이크 배열에 묶이지 않는 공간 입력

[상세 근거와 해석 범위]
[S29]
[Sources]
- https://arxiv.org/html/2510.05542v1
[발표 노트]
FOA 네 채널의 mel 특징과 W를 기준으로 계산한 intensity vector를 공간 인코더가 읽는다. 기존 mono 의미 인코더는 W 채널의 mel 특징만 읽는다. 두 경로의 projector가 언어 모델에 결합한다. 원문의 불 표식은 학습, 눈송이는 고정을 뜻한다. 공간 인코더와 공간 projector, spatial LoRA는 적응하고 기존 의미 인코더, 의미 projector, audio LoRA는 고정한다.
[해석 범위]
의미 경로를 구조적으로 유지한다는 사실만으로 모든 기존 언어·오디오 능력의 보존이 입증되지는 않는다. 비교 기준선은 고정 SELDNet 표현을 쓰며 Sci-Phi는 공간 encoder도 적응한다. 두 시스템 모두 장면 기술에 미세조정했다는 점이 근거 부록의 TupleScore 결과 해석의 전제다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "04 · 2025–2026: 기존 Audio-LM에 공간 경로를 더한다"
causalStage: "main"
originSlide: 47
---

# PhaseCoder: 특정 마이크 배열에 묶이지 않는 공간 입력

::body::
<PaperFigure src="/research/p2-phasecoder-v2-input.png" alt="PhaseCoder Fig. 2 상단. 약 13 ms 구간에서 네 마이크 채널의 파형과 채널 간 위상 차이를 보여 주는 원문 패널" caption="원문 Fig. 2 상단: 네 채널 파형. x축 시간(ms), y축 amplitude." />

::aside::
<section><span class="seminar-label semantic-input">공간 경로</span><p>다채널 오디오<br/>+ 마이크 좌표</p></section><section><span class="seminar-label ">의미 경로</span><p>기존 mono 오디오<br/>+ 텍스트 질문</p></section><section><span class="seminar-label semantic-geometry">명칭의 범위</span><p>배열 변화에 대응<br/>좌표는 계속 필요</p></section>

::takeaway::
PhaseCoder의 추론 입력에는 **다채널 오디오와 마이크 좌표**가 함께 필요하다.

::source::
PhaseCoder, arXiv:2601.21124v2, Fig. 2 상단 패널 크롭.

<!--
[현재 S30 · 본문]
04 · 2025–2026: 기존 Audio-LM에 공간 경로를 더한다

[설명의 중심]
PhaseCoder는 geometry-aware spatial tokens로 mono 경로를 확장한다.

[연결]
다음에 확인할 질문: PhaseCoder: 공간 QA와 목표 발화 전사의 절충

[상세 근거와 해석 범위]
[S30]
[Sources]
- https://arxiv.org/html/2601.21124v2
[발표 노트]
상단의 짧은 파형 구간에서 같은 음향 사건이 채널마다 서로 다른 관계로 관측되는 것을 본다. 같은 방향이라도 마이크의 수와 배치가 바뀌면 이런 관계가 달라진다. PhaseCoder는 다채널 오디오와 마이크 좌표를 받아 공간 토큰을 만들고, 기존 의미 오디오 경로와 함께 언어 모델에 제공한다. 그림의 아래 분류 head 결과는 이번 문제 관측과 분리하기 위해 크롭했다.
[해석 범위]
geometry-agnostic을 좌표가 필요 없다는 뜻으로 번역하지 않는다. 무지향·free-floating 마이크 배열 가정과 장치에 의한 산란 효과를 구분한다. 원문 Table 1의 실제 녹음 DOA는 인코더 평가이며 다음 QA 실험과 동일한 시험이 아니다.
-->

---
layout: "seminar"
variant: "result"
chapter: "04 · 2025–2026: 기존 Audio-LM에 공간 경로를 더한다"
causalStage: "main"
originSlide: 48
---

# PhaseCoder: 공간 QA와 목표 발화 전사의 절충

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">Gemma · Task 2 관계 Yes/No 정확도 (%) ↑ · 두 발화를 비중첩 연결</p>
<PaperFigure src="/diagrams/result-48.svg" alt="Synthetic 정확도 (%) ↑, RSL2019 정확도 (%) ↑ 원문 수치 비교 그래프. Baseline · mono: 48.44, 53.91; SFT · 공간 입력 + 학습: 76.76, 73.83" />
<p class="seminar-chart-note">반례 · RSL Task 4 mean WER: 42.90 → 48.41 (낮을수록 좋음)</p>
</div>

::takeaway::
**관계 QA와 공간 지정 목표 발화 전사**는 별도 과제로 확인해야 한다.

::source::
PhaseCoder, arXiv:2601.21124v2, Table 3. RSL QA는 train split 녹음에서 재구성.

<!--
[현재 S31 · 본문]
04 · 2025–2026: 기존 Audio-LM에 공간 경로를 더한다

[설명의 중심]
PhaseCoder Task 4는 공간으로 목표 화자를 골라 전사하는 과제다. WER는 선택·결속·전사의 오류를 함께 반영하며 일반 ASR 보존의 직접 지표가 아니다.

[연결]
다음에 확인할 질문: Spatial-Omni: 여러 기반 모델에 공간 경로를 이식한다

[상세 근거와 해석 범위]
[S31]
[Sources]
- https://arxiv.org/html/2601.21124v2
[발표 노트]
관계 Yes/No를 묻는 Task 2에서 Gemma baseline과 제안 SFT 시스템을 비교한다. 합성 평가의 정확도는 48.44에서 76.76%, RSL2019 재구성 QA는 53.91에서 73.83%로 높아진다. 그러나 목표 발화를 전사하는 RSL Task 4의 mean WER는 42.90에서 48.41로 악화한다. 서로 다른 과제를 합친 평균으로 이 상반된 결과를 가리지 않는다.
[해석 범위]
Baseline은 mono 입력이고 SFT에는 공간 입력과 추가 학습이 함께 들어가므로 공간 토큰만의 독립 인과효과가 아니다. Synthetic은 미사용 LibriSpeech·RIR·배열을 사용한다. RSL QA는 원 데이터 train split 녹음으로 재구성했으며 두 발화는 비중첩 연결이다. Gemma 의미 입력은 채널 평균이다. 원문은 WER>3.0 출력을 제외하므로 미필터 오류율을 보장하지 않는다.

[시각화 전 표의 수치·조건 보존]
Gemma · Task 2 관계 Yes/No 정확도 (%) ↑ · 두 발화를 비중첩 연결

시스템 조건 | Synthetic | RSL2019 | 

Baseline · mono | 48.44 | 53.91 | 

SFT · 공간 입력 + 학습 | 76.76 | 73.83 | 

반례　RSL Task 4 mean WER: 42.90 → 48.41 (낮을수록 좋음)
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
[과제 귀속 보완]
Task 4는 공간으로 지정한 목표 화자를 골라 전사하는 targeted transcription이다. WER는 선택·결속·전사 오류를 함께 반영하며 일반 ASR 또는 기존 의미 능력 보존을 직접 측정한 지표가 아니다.
-->

---
layout: "seminar"
variant: "method"
chapter: "04 · 2025–2026: 기존 Audio-LM에 공간 경로를 더한다"
causalStage: "main"
originSlide: 54
---

# Spatial-Omni: 여러 기반 모델에 공간 경로를 이식한다

::body::
<PaperFigure src="/research/spatialomni-core.png" alt="Spatial-Omni Fig. 1 오른쪽 경로. FOA 공간 encoder와 W 채널 audio encoder가 각각 projector를 거쳐 언어 입력에 결합" caption="Fig. 1 오른쪽 경로 크롭. 영상은 기존 backbone의 선택 경로이며 공간 QA의 추가 관측이 아니다." />

::aside::
<section><span class="seminar-label semantic-input">두 입력 경로</span><p>FOA → 공간 encoder<br/>W → 의미 encoder</p></section><section><span class="seminar-label semantic-geometry">학습 순서</span><p>projector 정렬<br/>→ LoRA 결합<br/>→ 공간 경로 적응</p></section>

::takeaway::
**projector 정렬 → LLM LoRA → 공간 경로 적응**으로 학습 문제를 나눈다.

::source::
Spatial-Omni, arXiv:2606.10738v2, Fig. 1 오른쪽 패널·§5.

<!--
[현재 S32 · 본문]
04 · 2025–2026: 기존 Audio-LM에 공간 경로를 더한다

[설명의 중심]
Spatial-Omni는 projector 정렬, LoRA, 공간 경로 적응을 나눠 학습하는 구체적인 사례다.

[연결]
다음에 확인할 질문: Spatial-Omni: 추가한 공간 입력의 기여를 확인한다

[상세 근거와 해석 범위]
[S32]
[Sources]
- https://arxiv.org/html/2606.10738v2
[발표 노트]
FOA 공간 관측은 SO-Encoder에 들어가고 W 채널은 기존 Audio Encoder로 들어간다. 별도의 projector가 공간 표현을 언어 토큰 차원에 맞춰 기존 오디오 및 텍스트 토큰과 결합한다. 원문의 전체 그림 중 결합 경로를 크롭했으며 SO-Encoder 내부 블록은 생략했다. 원본의 visual branch는 기반 멀티모달 모델의 구조이고 여기의 공간 QA에서 영상 정보를 새 관측으로 사용한다는 뜻은 아니다.
[해석 범위]
기본 학습은 projector 정렬, LLM LoRA 결합, 공간 encoder의 학습 가능한 부분을 포함한 적응으로 구성된다. 기존 의미 경로를 구조적으로 보존하는 것과 실제 일반 오디오 성능의 보존은 다르다. Fig. 5에서 MIX는 일부 성능을 회복하지만 완전 보존으로 말하지 않는다.

[기존 의미 능력]
기존 audio tower를 고정한 구조만으로 의미 능력의 보존을 보장하지 않는다. Spatial-Omni v2 Table 18과 MIX 비교가 별도의 일반 오디오 평가 근거다. PhaseCoder의 targeted transcription WER와 구별한다.
-->

---
layout: "seminar"
variant: "result"
chapter: "04 · 2025–2026: 기존 Audio-LM에 공간 경로를 더한다"
causalStage: "main"
originSlide: 55
---

# Spatial-Omni: 추가한 공간 입력의 기여를 확인한다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">SO-Bench · 같은 7B 계열 · greedy decoding · 점수는 모두 % (높을수록 좋음)</p>
<PaperFigure src="/diagrams/result-55.svg" alt="EAzi (%) ↑
방위각 오차 ≤ 20°, IS-Loc (%) ↑
위치로 음원 식별, RLR (%) ↑
상대 좌우 원문 수치 비교 그래프. SO-7B-zs · 공간 토큰 0: 13.06, 40.69, 47.15; SO-7B · 실제 공간 토큰: 76.38, 66.81, 72.97" />
</div>

::takeaway::
이 zero-spatial 비교는 **공간 입력 기여의 근거**이며 제거 시점·checkpoint 공유는 미명시다.

::source::
Spatial-Omni, arXiv:2606.10738v2, Table 2의 SO-7B-zs/SO-7B. MIX와 구분.

<!--
[현재 S33 · 본문]
04 · 2025–2026: 기존 Audio-LM에 공간 경로를 더한다

[설명의 중심]
Spatial-Omni의 zero-spatial 변형과 full 모델을 비교한다. 고정 checkpoint에서의 추론 시 제거 실험이라고 단정하지 않는다.

[연결]
다음에 확인할 질문: TWNM v3: 의미와 공간을 같은 음원에 묶는다

[상세 근거와 해석 범위]
[S33]
[Sources]
- https://arxiv.org/html/2606.10738v2
[발표 노트]
S33에서 구분한 세 질문으로 돌아간다. SO-7B-zs는 공간 토큰을 0으로 만든 조건이고 SO-7B는 실제 공간 토큰을 받는다. EAzi는 방위각 오차가 20도 안에 들어오는 비율, IS-Loc은 위치 기반 식별, RLR은 상대 좌우 판정이다. 선택한 세 점수가 실제 공간 토큰 조건에서 모두 높다. 같은 7B 계열의 내부 비교로 읽는다.
[해석 범위]
입력 ablation이 공간 정보의 유용성을 보이지만 특정 phase 기전을 입증하지 않는다. SO-7B와 MIX를 섞지 않는다. 복합 MH 점수는 22.52/39.93으로 여전히 어렵다. 일반 오디오 성능의 완전 보존이나 임의 배열 일반화는 이 실험으로 주장할 수 없다. SC의 WER는 낮을수록 좋은 별도 지표다.

[시각화 전 표의 수치·조건 보존]
SO-Bench · 같은 7B 계열 · greedy decoding · 점수는 모두 % (높을수록 좋음)

모델·공간 입력 | EAzi / 방위각 오차 ≤ 20° | IS-Loc / 위치로 음원 식별 | RLR / 상대 좌우 | 

SO-7B-zs · 토큰 0 | 13.06 | 40.69 | 47.15 | 

SO-7B · 실제 토큰 | 76.38 | 66.81 | 72.97 |
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.

[원문 확인 보완]
Spatial-Omni v2 §5.3과 Appendix E.2는 zero/null spatial token을 사용한 변형을 명시하지만, 적용 시점이 학습부터인지 추론만인지와 checkpoint 공유 여부는 명시하지 않는다. 고정 checkpoint의 추론 시 제거 ablation으로 단정하지 않는다.
-->

---
layout: "seminar"
variant: "method"
chapter: "04 · 2025–2026: 기존 Audio-LM에 공간 경로를 더한다"
causalStage: "main"
originSlide: 57
---

# TWNM v3: 의미와 공간을 같은 음원에 묶는다

::body::
<PaperFigure src="/research/p2-twnm-v3-fig2.png" alt="TWNM Fig. 2 원문 구조. FOA spatial encoder와 semantic encoder, hybrid projector와 단계별 언어 학습" caption="v3: 공간 encoder 학습·적응 → projector 정렬 → SFT → SAPO." />

::takeaway::
**source slots로 감독**하지만, LLM에는 의미 경로와 결합한 **dense 특징**을 보낸다.

::source::
The World is Not Mono, arXiv:2601.02954v3, Fig. 2·§4.1–4.2. v3의 FOA·SAPO.

<!--
[현재 S34 · 본문]
04 · 2025–2026: 기존 Audio-LM에 공간 경로를 더한다

[설명의 중심]
TWNM의 source slots는 학습 감독이고 실제 hybrid projector에는 dense encoder map이 전달된다.

[연결]
다음에 확인할 질문: TWNM의 connector 설계 비교는 adapter가 단순 차원 변환 이상의 선택임을 보여 준다. semantic-judge 점수이며 checkpoint·학습 예산을 완전히 맞췄다는 조건은 미명시다.

[상세 근거와 해석 범위]
[S34]
[Sources]
- https://arxiv.org/html/2601.02954v3
[발표 노트]
원문의 왼쪽은 FOA 오디오를 공간 경로와 의미 경로로 나누고, 가운데 hybrid projector가 두 표현을 결합하는 구조다. 의미 경로는 W 채널의 고정 Whisper-small이고 공간 encoder는 최대 세 source slots와 방향·거리·사건·존재 여부를 지도 학습한다. 다만 pooled slot head만 LLM에 보내는 것은 아니다. §4.1은 dense encoder map을 의미 경로 길이에 맞춰 결합한다고 설명한다.
[해석 범위]
그림의 Stage 1은 공간 인코더 학습·적응, Stage 2는 projector 정렬, Stage 3은 SFT, Stage 4는 SAPO다. v3의 FOA와 SAPO를 초기 버전의 binaural·GRPO로 바꾸지 않는다. source slots에 의한 내부 지도와 명시적인 scene graph 출력도 다르다.
-->

---
layout: "seminar"
variant: "result"
chapter: "04 · 2025–2026: 기존 Audio-LM에 공간 경로를 더한다"
causalStage: "main"
---

# 토큰을 결합하는 설계에 따라 결과가 달라졌다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">TWNM · ASA 평가 · semantic-judge · 원문 보고 Overall · 최종 SAPO 이전</p>
<PaperFigure src="/diagrams/causal-module-evidence.svg" alt="TWNM v3 Appendix G Table 15 connector 비교. Overall: P0 Single MLP 39.20, P1 Dual Tower 46.40, P2 Dense Hybrid 52.10 퍼센트" />
<p class="seminar-chart-note">동일 checkpoint·학습 예산의 완전 통제는 미명시 · 별도 exact-MCQA 점수와 채점법이 다름</p>
</div>

::takeaway::
어댑터에서는 **어떤 특징을 나누고 결합하는가**도 학습 설계의 일부다.

::source::
The World is Not Mono, arXiv:2601.02954v3, Appendix G, Table 15. 보고 수치 그대로 재구성.

<!--
[현재 S35 · 본문]
04 · 2025–2026: 기존 Audio-LM에 공간 경로를 더한다

[설명의 중심]
TWNM의 connector 설계 비교는 adapter가 단순 차원 변환 이상의 선택임을 보여 준다. semantic-judge 점수이며 checkpoint·학습 예산을 완전히 맞췄다는 조건은 미명시다.

[연결]
다음에 확인할 질문: TWNM v3: 연결 이후에는 답변 학습 목표도 달라진다

[상세 근거와 해석 범위]
[이번 장의 역할]
인코더·어댑터·언어 모델의 전체 구조를 이해한 뒤, 어댑터를 단순 차원 변환의 부품으로만 다루지 않는 근거를 보인다. TWNM의 Appendix G Table 15는 P0: Single MLP, P1: Dual Tower, P2: Dense Hybrid 연결 설계를 비교한다. Overall은 각각 39.20, 46.40, 52.10%다. ASA 평가에 대해 원문이 보고한 Overall이다. L1/L2/L3의 단순 평균으로 만들지 않는다.

이 표의 semantic-answer judge는 질문·선지·gold·생성 답변을 받는 Gemini 3 Flash이며 audio/RTSD를 직접 보지 않는다. 최종 SAPO 이전의 진단이다. 다음 장의 main Table 5에서 SFT/SAPO를 비교한 exact MCQA와 채점법이 다르므로 숫자의 높낮이를 두 표 사이에서 비교하지 않는다.

원문은 projector ablation이라고 명명하지만 각 행의 encoder checkpoint, LLM checkpoint, 학습 예산과 seed가 완전히 같은지 별도 명시하지 않는다. 따라서 연결 설계별 보고 결과로 해석한다. P만 바꾸고 나머지를 완벽히 고정한 인과 실험이라고 강화하지 않는다. 앞서 살펴본 DSpAST는 같은 QA 인터페이스의 인코더 비교, OWL은 인코더 사전학습 loss 비교였다. 다음 장에서는 SFT와 SAPO의 답변 학습 목표를 비교한다.

[원문 산술의 한계]
본문의 수준별 문항 수 385/279/336으로 Table 15의 수준별 점수를 가중해도 이 Overall과 일치하지 않는다. P0/P1/P2 재계산은 약 39.45/46.78/52.41이며 보고값 39.20/46.40/52.10과 다르다. 평가 집계 또는 분모의 차이는 원문만으로 해결하지 못했다. 슬라이드는 보고 Overall 세 개를 그대로 인용하며 정확한 성공 문항 수로 역산하지 않는다.

[Sources]
- https://arxiv.org/html/2601.02954v3
-->

---
layout: "seminar"
variant: "result"
chapter: "04 · 2025–2026: 기존 Audio-LM에 공간 경로를 더한다"
causalStage: "main"
originSlide: 58
---

# TWNM v3: 연결 이후에는 답변 학습 목표도 달라진다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">ASA benchmark · 최대 3음원 합성 FOA · exact MCQA · 단일 실행 · 정확도 (%) ↑</p>
<PaperFigure src="/diagrams/result-58.svg" alt="L1 · 지각, L2 · 관계 연결, L3 · 복합 질의 원문 수치 비교 그래프. TWNM-SFT: 65.19, 70.61, 51.19; TWNM-SAPO: 63.64, 69.89, 79.76" />
</div>

::takeaway::
**복합 질의의 개선**과 기초 지각·관계 연결의 소폭 하락이 함께 나타난다.

::source::
The World is Not Mono, arXiv:2601.02954v3, Table 5. ↑ 높을수록 좋음.

<!--
[현재 S36 · 본문]
04 · 2025–2026: 기존 Audio-LM에 공간 경로를 더한다

[설명의 중심]
TWNM SFT→SAPO는 복합 질의가 좋아져도 기본 지각·관계 연결이 낮아지는 trade-off를 드러낸다.

[연결]
다음에 확인할 질문: 움직임을 묻기 시작하면 시간 구조가 필요하다

[상세 근거와 해석 범위]
[S36]
[Sources]
- https://arxiv.org/html/2601.02954v3
[발표 노트]
가장 큰 변화는 L3의 51.19에서 79.76% 상승이다. 그러나 앞의 두 열도 읽으면 L1은 65.19에서 63.64%, L2는 70.61에서 69.89%로 소폭 낮아졌다. 따라서 최종 정책 학습이 모든 능력을 동시에 개선했다고 요약하지 않는다. 같은 exact MCQA 프로토콜의 단일 실행 결과다.
[해석 범위]
평가의 렌더 장면, 공간 구성, 질문과 정답은 학습에서 분리했지만 dry-source clip identity는 중복될 수 있다. 새로운 음원 정체성에 대한 전이라고 부르지 않는다. STARSS23 QA는 encoder 적응 녹음과 분리되지 않아 recording-disjoint 전이도 아니다. strict pick-letter audit를 사용한 corrupted-input 통제는 본문의 full-FOA exact score와 동일한 채점 효과 크기로 합치지 않는다.

[시각화 전 표의 수치·조건 보존]
ASA benchmark · 최대 3음원 합성 FOA · exact MCQA · 단일 실행 · 정확도 (%) ↑

학습 단계 | L1 / 지각 | L2 / 관계 연결 | L3 / 복합 질의 | 

TWNM-SFT | 65.19 | 70.61 | 51.19 | 

TWNM-SAPO | 63.64 | 69.89 | 79.76 |
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "05 · 2025–2026: 정적 위치에서 이동과 시간 관계로"
causalStage: "main"
---

# 움직임을 묻기 시작하면 시간 구조가 필요하다

::body::
<PaperFigure src="/diagrams/history-dynamics.svg" alt="Motion의 명시적 시계열과 BAT 계열 Dynamic QA·ST-AudioLM의 연속 토큰 경로를 나란히 비교한다. BAT에서 후자의 backbone 계승은 원문 명시이며 세 논문 사이의 직선적인 성능 발전으로 그리지 않는다." />

::takeaway::
정적 위치 다음에는 **어느 음원이 언제 움직였는지**를 전달하는 방식이 쟁점이 된다.

::source::
Motion v1 §2.2 · Dynamic Source Movements v1 §3.2 · ST-AudioLM v1 §2·4·5.1.

<!--
[현재 S37 · 본문]
05 · 2025–2026: 정적 위치에서 이동과 시간 관계로

[설명의 중심]
Motion의 명시적 시계열과 BAT 계열 Dynamic QA·ST-AudioLM의 연속 토큰 경로를 나란히 비교한다. BAT에서 후자의 backbone 계승은 원문 명시이며 세 논문 사이의 직선적인 성능 발전으로 그리지 않는다.

[연결]
다음에 확인할 질문: 차원을 맞추는 것만으로 충분하지 않다. 압축과 pooling이 source·time 관계를 잃게 할 수 있으므로 전달 구조를 정한다.

[상세 근거와 해석 범위]
[Sources]
- https://arxiv.org/html/2509.14666v1
- https://arxiv.org/html/2602.16334v1
- https://arxiv.org/html/2606.14141v1

[그림]
이 그림은 원문 Methods에 근거한 교육용 재구성으로 실제 activation이나 성능 측정 그림이 아니다. 최초 공개 연대와 채택 버전은 plans/MC_AUDIO_LM_HISTORY.md에 구분하여 기록했다. 화살표는 그림 내부의 데이터 흐름이며 논문 간 성능 상승을 뜻하지 않는다.

[연구사와 발표 노트]
상단의 작은 궤적은 같은 질문을 설명하기 위한 합성 도형으로 모델의 실제 출력이 아니다. Motion 2025는 학습 지각 모델이 추정한 시간별 사건·방향·거리 정보를 JSON으로 추론 모델에 전달한다. Dynamic QA 2026은 BAT encoder의 penultimate layer를 시간 인식으로 바꾸고 Q-Former와 Qwen3-4B를 연결한다. AGM mask는 질문 관련 시간 구간을 고르는 추론 전처리이며 원래 파형에서 다른 시간 구간을 0으로 만든다.
ST-AudioLM은 BAT의 Spatial-AST backbone을 FOA에 맞추고 semantic/static/dynamic token을 지도 학습한다. QA에서 고정 encoder의 semantic1+dynamic40을 MLP connector와 LoRA에 연결한다. 단순 pooling의 교육용 반례와 원문의 실제41-token 비교를 이어서 본다.
Dynamic QA와 ST-AudioLM의 BAT 기반 확장은 원문이 명시하지만 Motion→Dynamic→ST의 단일 계보를 뜻하지 않는다. ST-AudioLM은 Dynamic QA를 concurrent work로 구분한다. 다음 수치들은 각각의 원문 평가 내부 비교이며 서로 다른 데이터셋과 질문을 한 성능 그래프로 합치지 않는다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "05 · 2025–2026: 정적 위치에서 이동과 시간 관계로"
causalStage: "main"
---

# 시간 평균은 서로 다른 이동을 같게 만들 수 있다

::body::
<PaperFigure src="/diagrams/causal-token-bottleneck.svg" alt="두 음원 A와 B의 이동 방향이 반대인 두 장면은 각 음원의 단순 평균 방향이 모두 0으로 같아진다. 사건별 시간 속성을 남기면 장면1의 A는 -60,0,60도이고 B는60,0,-60도로 구분된다." />

::takeaway::
이동 질문에 답하려면 **사건·위치·시간의 대응을 전달하는 표현**이 필요하다.

::source::
교육용 평균 반례 · ST-AudioLM v1 §4.1–4.2 · TWNM v3 §4.1. 실제 토큰은 연속 임베딩.

<!--
[현재 S38 · 본문]
05 · 2025–2026: 정적 위치에서 이동과 시간 관계로

[설명의 중심]
차원을 맞추는 것만으로 충분하지 않다. 압축과 pooling이 source·time 관계를 잃게 할 수 있으므로 전달 구조를 정한다.

[연결]
다음에 확인할 질문: Dynamic QA 2026: 질문에 필요한 시간 구간을 고른다

[상세 근거와 해석 범위]
[B-TOKEN-BOTTLENECK]
[Sources]
- https://arxiv.org/html/2606.14141v1
- https://arxiv.org/html/2601.02954v3
[그림]
public/diagrams/causal-token-bottleneck.svg. 실험 결과가 아닌 교육용 반례이다. 청색 실선 A, 청록 점선 B를 두 장면에서 같은 사건으로 유지했다. 장면1은 A:-60→0→60도, B:60→0→-60도이며 장면2는 각각 역순이다. 이 범위는 각도 wrap 문제가 없고, 방향의 단순 시간 평균은 각 음원 모두0도이다. 서로 다른 운동을 같은 평균으로 매핑하는 구체적인 예이다.
[발표 노트]
파란 소리가 어느 쪽으로 움직였는지 물으면 두 장면의 정답이 다르다. 단순 평균만 전달하면 두 장면을 구분할 근거가 없다. 오른쪽은 장면1의 사건과 시간을 명시적으로 대응시킨 설명용 속성 표이다. 실제 모델이 이 숫자 표나 두 개의 명시적인 source token을 LLM에 넣는다는 뜻이 아니다. 시간 해상도와 사건 정보를 유지하는 연속 표현이 이 대응을 학습할 수 있게 해야 한다.
[논문 연결]
ST-AudioLM은 10초에서 의미1+시간40=41개의 토큰을 MLP로 LLM에 전달한다. 전역 DoA/거리 토큰은 encoder 지도에 쓰지만 LLM 입력에서는 제외한다. 정적 Spatial-AST 비교도 같은41개 토큰이므로 결과 차이를 토큰 개수 증가로 설명하지 않는다. 동적 지도, temporal attention, semantic distillation/replay가 함께 바뀐다.
TWNM은 encoder에 source-slot 지도를 사용하지만 LLM 입력은 의미·공간 밀집 시계열을 융합한 연속 토큰이다. LLM이 source slot3개 또는 명시 scene graph를 직접 입력받는 그림으로 대체하지 않는다.
[해석 범위]
이 그림은 순서 정보가 없는 단순 평균의 반례이다. 학습한 전역 토큰은 시간 순서 자체를 인코딩할 수 있으므로 모든 전역 표현이 이동을 표현할 수 없다는 증명이 아니다. 토큰 길이가 길다는 사실만으로 올바른 사건 결속을 보장하지도 않는다. 실제 성능은 같은 프로토콜의 통제로 확인한다.
-->

---
layout: "seminar"
variant: "result"
chapter: "05 · 2025–2026: 정적 위치에서 이동과 시간 관계로"
causalStage: "main"
originSlide: 61
---

# Dynamic QA 2026: 질문에 필요한 시간 구간을 고른다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">합성 이동 stereo · Qwen3-4B · Overall 정확도 (%) ↑ · GT는 정답 구간 참고 조건</p>
<PaperFigure src="/diagrams/result-61.svg" alt="NoMask, AGM mask, GT mask 원문 수치 비교 그래프. Thinking: 54.3, 55.0, 56.1; Non-Thinking: 54.1, 54.0, 54.1" />
<p class="seminar-chart-note">구간 밖을 0으로 masking · 같은 구간의 간섭 음원을 분리하는 것은 아님</p>
</div>

::takeaway::
masking과 thinking의 **결합 효과는 조건에 따라 다르며 전체 개선 폭은 제한적**이다.

::source::
Spatial Audio Question Answering and Reasoning on Dynamic Source Movements, arXiv:2602.16334v1, Table 3.

<!--
[현재 S39 · 본문]
05 · 2025–2026: 정적 위치에서 이동과 시간 관계로

[설명의 중심]
Dynamic QA는 mask 조건과 reasoning mode를 분리해 비교한다.

[연결]
다음에 확인할 질문: ST-AudioLM 2026: 시간별 음원 상태를 토큰으로 남긴다

[상세 근거와 해석 범위]
[S39]
[Sources]
- https://arxiv.org/html/2602.16334v1
[발표 노트]
한 번에 한 조건만 바꿔 읽는다. Thinking 행에서는 NoMask 54.3, AGM 55.0, 정답 구간 GT 56.1%다. Non-Thinking 행에서는 54.1, 54.0, 54.1%로 거의 변하지 않는다. 같은 mask의 두 행을 비교하면 thinking의 효과도 볼 수 있다. Overall은 Yes/No, MCQ, open 질문을 포함한다.
[해석 범위]
AudioSet strong-labeled 원음에 움직임을 부여한 합성 stereo 평가다. 시간 정보를 확장한 BAT 계열 encoder, Q-Former, Qwen3-4B를 학습하고 AGM은 추론 전처리다. GT는 배포 가능한 관측이 아니라 정답 이벤트 구간을 제공한 참고 조건이다. 시간 mask는 구간 밖 파형을 0으로 하므로 같은 구간의 간섭 음원을 완전히 제거하지 못한다. 수치 차이를 통계적 유의성이나 rationale의 청각적 충실성 증명으로 바꾸지 않는다.

[시각화 전 표의 수치·조건 보존]
합성 이동 stereo · Qwen3-4B · Overall 정확도 (%) ↑ · GT는 정답 구간 참고 조건

출력 설정 | NoMask | AGM mask | GT mask | 

Thinking | 54.3 | 55.0 | 56.1 | 

Non-Thinking | 54.1 | 54.0 | 54.1 | 

시간 mask는 구간 밖을 0으로 만든다. 같은 구간의 간섭 음원까지 분리하지는 않는다.
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->

---
layout: "seminar"
variant: "method"
chapter: "05 · 2025–2026: 정적 위치에서 이동과 시간 관계로"
causalStage: "main"
originSlide: 63
---

# ST-AudioLM 2026: 시간별 음원 상태를 토큰으로 남긴다

::body::
<PaperFigure src="/research/p2-staudiolm-v1-fig1.png" alt="ST-AudioLM Fig. 1. 의미 token과 dynamic trajectory token을 만드는 encoder 및 frozen encoder에서 connector와 LoRA로 이어지는 QA 구조" caption="왼쪽: 궤적 지도 학습. 오른쪽: 고정 ST-Audio Encoder + 학습하는 connector·LoRA." />

::takeaway::
고정 인코더의 **의미·궤적 토큰**을 학습하는 connector와 LoRA로 연결한다.

::source::
ST-AudioLM, arXiv:2606.14141v1, Fig. 1. 원문 방법 그림.

<!--
[현재 S40 · 본문]
05 · 2025–2026: 정적 위치에서 이동과 시간 관계로

[설명의 중심]
ST-AudioLM은 의미 토큰과 동적 궤적 토큰을 고정 encoder에서 꺼내 connector·LoRA로 연결한다.

[연결]
다음에 확인할 질문: ST-AudioLM: 같은 41개 토큰에서도 시간 표현이 다르다

[상세 근거와 해석 범위]
[S40]
[Sources]
- https://arxiv.org/html/2606.14141v1
[발표 노트]
왼쪽의 encoder는 사건 의미 토큰과 정적 위치 토큰, 시간 구간별 동적 궤적 토큰을 만든다. 궤적 토큰은 activity, direction, distance의 지도 학습으로 시간 정보를 유지한다. 오른쪽 QA 경로에서는 고정 ST-Audio Encoder가 의미 토큰 하나와 dynamic trajectory 토큰을 내보내고, 학습 가능한 두 층 MLP connector와 LoRA가 이를 언어 입력에 연결한다.
[해석 범위]
이 구조도는 방법을 설명하며 실제 움직임 예측 성공의 근거를 대신하지 않는다. 정적 encoder를 시간 구간별로 반복 적용하는 것과 궤적 지도 학습을 같은 방법으로 그리지 않는다. encoder Table 3와 실제 녹음 적응 결과는 다음 조합 QA 평가와 별개다.
-->

---
layout: "seminar"
variant: "result"
chapter: "05 · 2025–2026: 정적 위치에서 이동과 시간 관계로"
causalStage: "main"
originSlide: 64
---

# ST-AudioLM: 같은 41개 토큰에서도 시간 표현이 다르다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">ST-AudioQA Type C · FOA, OLMo2, 41-token 인터페이스 · controlled-answer accuracy (0–100) ↑</p>
<PaperFigure src="/diagrams/result-64.svg" alt="시간 관계
Temp. rel., 이동 조건
Move-spat., 궤적 관계
Traj. rel., 평균 원문 수치 비교 그래프. Spatial-AST-FOA + OLMo2: 80.4, 55.2, 54.3, 63.3; ST-AudioLM: 86.0, 55.8, 60.6, 67.5" />
</div>

::takeaway::
같은 41-token 인터페이스에서도 **시간 구조를 배운 표현**의 평균 성과가 달랐다.

::source::
ST-AudioLM, arXiv:2606.14141v1, Table 5. ↑ 높을수록 좋음.

<!--
[현재 S41 · 본문]
05 · 2025–2026: 정적 위치에서 이동과 시간 관계로

[설명의 중심]
같은 FOA·OLMo2·41-token 인터페이스 비교에서 encoder의 시간 구조 차이를 본다. connector 하나의 효과로 귀속하지 않는다.

[연결]
다음에 확인할 질문: H의 정보 접근성, Z의 전달, 답변의 오디오 의존을 서로 다른 관측·개입으로 시험한다.

[상세 근거와 해석 범위]
[S41]
[Sources]
- https://arxiv.org/html/2606.14141v1
[발표 노트]
같은 FOA 계열 입력과 OLMo2, 41-token 인터페이스를 사용하는 QA 학습 비교다. baseline은 정적 FOA encoder, ST-AudioLM은 궤적 지도를 학습한 표현을 사용한다. 평균은 63.3에서 67.5로 높아진다. 그러나 ST-AudioLM의 시간 관계 86.0에 비해 이동 조건 관계는 55.8, 두 음원 궤적 관계는 60.6이다. 평균만 보면 남는 난도를 놓칠 수 있다.
[해석 범위]
값은 통제된 답 형식의 0–100 정확도다. 모든 encoder 지표 우세나 밀집한 현실 장면의 해결을 뜻하지 않는다. BAT는 같은 scene metadata를 바이노럴로 렌더링해 받으므로 동일 입력 ablation이 아니다. Table 4 기본·두 음원 QA와 Table 3 encoder 및 실제 녹음 적응은 각각 따로 읽는다.

[시각화 전 표의 수치·조건 보존]
ST-AudioQA Type C · FOA, OLMo2, 41-token 인터페이스 · controlled-answer accuracy (0–100) ↑

QA 학습 모델 | 시간 관계 / Temp. rel. | 이동 조건 / Move-spat. | 궤적 관계 / Traj. rel. | 평균 | 

Spatial-AST-FOA / + OLMo2 | 80.4 | 55.2 | 54.3 | 63.3 | 

ST-AudioLM | 86.0 | 55.8 | 60.6 | 67.5 |
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "06 · 표현에서 답변까지 무엇을 확인해야 하나"
causalStage: "main"
---

# 읽히는 정보가 답에도 쓰이는가?

::body::
<PaperFigure src="/diagrams/causal-evaluation-map.svg" alt="입력 X, 인코더 E의 H, projector P의 Z, LLM과 답으로 이어지는 공통 관측 지도. SARL 판독은 H, BMLD 자극 반응은 X에서 H, Spatial-Omni zero 기준선은 공간 token 인터페이스, BAT 질문만 조건은 X 없이 Q에 배치한다. 주황 점선은 token 치환·복구와 오디오 짝 비교의 미실행 제안이다." caption="각 문헌의 관측 위치를 겹쳐 그린 지도. E: 인코더 · P: adapter · Q: 질문." />

::takeaway::
<strong>판독, 자극 반응, token 비교, 답변 변화</strong>는 서로 다른 증거다.

::source::
SARL v2 §3 · BMLD v1 §2 · Spatial-Omni v2 §5.3·App. E · BAT v4 Table 4.

<!--
[현재 S42 · 본문]
06 · 표현에서 답변까지 무엇을 확인해야 하나

[설명의 중심]
H의 정보 접근성, Z의 전달, 답변의 오디오 의존을 서로 다른 관측·개입으로 시험한다.

[연결]
다음에 확인할 질문: 문장으로만 넘기면 공간 단서가 얼마나 남는가?

[상세 근거와 해석 범위]
[Bridge: causal-evaluation]
[Sources]
- https://arxiv.org/html/2606.05544v2
- https://arxiv.org/html/2606.14820v1
- https://arxiv.org/html/2606.10738v2
- https://arxiv.org/html/2402.01591v4
- https://arxiv.org/html/2510.24693v2
- https://arxiv.org/html/2601.02391v1
- https://aclanthology.org/2021.tacl-1.10/
- https://aclanthology.org/2025.findings-acl.674/
[청중 질문]
표현의 정보를 읽는 것과 모델이 실제 답변에 사용하는 것을 어떻게 구분하는가?
[발표 노트]
이 그림은 한 모델의 구조도가 아니다. 서로 다른 모델·실험을 공통 X→E(H)→P(Z)→L(Z,Q)→답 좌표에 놓은 관측 지도다. 파랑은 보고된 관측 위치이고 주황 점선은 후속 제안이다. latent cell과 선형 판독 산점은 모식도이며 측정 결과가 아니다.
SARL Fig. 2는 고정 H의 선형 판독이고 Fig. 3의 source/room 변화 민감도와 구분한다. 둘 다 LLM이 해당 정보를 소비했는지는 검사하지 않는다. BMLD는 X의 표적 위상을 바꾼 뒤 H의 거리비 반응을 읽는다. 그림의 두 sinusoid는 표적 위상의 설명용 표시이고, 실제 자극은 같은 잡음 n으로 N0=(n,n), S0N0=(n+s,n+s), SπN0=(n+s,n−s)를 구성한다. 오른쪽 혼합음 전체가 뒤집히는 것이 아니다. 이는 인간 탐지 역치나 QA 점수가 아니다.
Spatial-Omni v2 §5.3은 SO-7B-zs가 zero spatial tokens를 사용한다고, Appendix E의 baseline 설명은 null spatial token을 LLM에 공급한다고 쓴다. 학습부터 zero인지 추론 시만 zero인지, SO-7B와 동일 checkpoint인지 명시하지 않는다. 따라서 ‘zero 기준선’으로만 표현하며 고정 checkpoint token 제거 실험으로 단정하지 않는다.
BAT Table 4 P는 실제 질문만 조건이다. 그림의 X→LLM 경로는 일반 오디오+질문 흐름이며 BAT P 조건에서는 X가 제외된다. STAR-Bench Table 2의 기준은 Random Guess이므로 STAR를 question-only 실험이라 부르지 않는다. STAR의 caption 대조 역시 질문만 조건이 아니다. WearVox는 전체 SLLM의 실녹음 검증으로, E만의 향상이나 특정 phase 사용을 직접 보여주지 않는다.
[주황 점선: 미실행 제안]
동일 checkpoint에서 Z를 위치가 다른 짝의 토큰으로 치환하고 정상 token으로 복구한다. 공간 관련 token 제거, 같은 수의 무작위 token 제거, 길이·norm·분포 대조를 함께 설계한다. 다른 의미 task까지 무너지는 일반 손상과 구분한다. H와 Z를 동일 probe로 판독하면 경계를 지나는 정보의 접근 가능성도 비교할 수 있다.
오디오 짝 비교는 같은 질문에서 위치 A·B의 정답이 각각 달라지는 쌍을 둘 다 맞히는지 확인한다. 단순히 답이 달라지는 것은 성공이 아니다. 새 수치를 만들지 않았고 어떠한 제안 실험도 수행했다고 주장하지 않는다.
[해석 범위]
probe 성능, cue sensitivity, LLM의 정보 사용을 같은 지표로 합치지 않는다. 다른 논문의 결과를 한 시스템이 통과한 보장 사다리로 그리지 않는다. 언어 분야의 amnesic probing은 실험 설계의 방법론적 참고이며 공간 오디오에서 검증된 결과가 아니다.
-->

---
layout: "seminar"
variant: "method"
chapter: "06 · 표현에서 답변까지 무엇을 확인해야 하나"
causalStage: "main"
originSlide: 68
---

# 문장으로만 넘기면 공간 단서가 얼마나 남는가?

::body::
<PaperFigure src="/research/star-caption-panel.png" alt="STAR-Bench의 청각 입력과 텍스트 캡션 기반 추론 비교" caption="STAR-Bench Fig. 1의 audio/caption 비교 패널." />

::aside::
<section><span class="seminar-label">문장에 남은 정보</span><p>소리 · 사건</p></section><section><span class="seminar-label">따로 확인할 정보</span><p>방향 · 미세한 시간 관계</p></section>

::takeaway::
평가하려는 단서가 <strong>설명문에 보존되는지</strong>부터 확인한다.

::source::
STAR-Bench, arXiv:2510.24693v2, Fig. 1 관련 패널 크롭.

<!--
[현재 S43 · 본문]
06 · 표현에서 답변까지 무엇을 확인해야 하나

[설명의 중심]
STAR의 caption 분석은 audio→text 중간 경로가 무엇을 놓칠 수 있는지 보여 준다. 모든 adapter의 token bottleneck 측정으로 일반화하지 않는다.

[연결]
다음에 확인할 질문: 같은 표현에서도 속성마다 읽히는 정도가 다르다

[상세 근거와 해석 범위]
[S43]
[Sources]
- https://arxiv.org/html/2510.24693v2
[청중 질문]
‘말소리와 알람이 있다’는 문장만 받았을 때도 방향·미세한 시간 질문에 답할 수 있는가?
[발표 노트]
원음을 듣는 조건과 문장으로 전달받는 조건을 읽는다. 문장에 남은 내용, 사라진 공간·시간 정보를 가른다. 설명의 충분성과 모델 능력을 동시에 바꾸면 원인을 하나로 정할 수 없음을 설명한다.
캡션 비교는 특정 채널이나 위상 단서만 제거하는 통제가 아니다. 설명의 정보량과 모델의 능력이 함께 바뀌므로 점수 차이를 한 음향 기전의 효과로 해석하지 않는다.
[해석 범위]
캡션은 무음·채널 위상 제거와 같은 통제가 아니다. 모든 문장은 공간 정보를 잃는다는 주장도 하지 않는다. 도입 알람 장면을 쓸 경우 ‘발표자 설명용’으로 표시한다.
[시각화 전 상세 본문 — 발표 설명용 보존]
STAR-Bench Fig. 1의 audio/caption 비교 패널.


[보조 설명]
설명문에 남은 것어떤 소리가 있었는지
어떤 사건을 기술했는지

따로 확인할 것방향과 미세한 시간 관계가
문장에도 보존됐는가?


[핵심 결론]
평가하려는 단서가 설명문에 보존되는지부터 확인한다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "06 · 표현에서 답변까지 무엇을 확인해야 하나"
causalStage: "main"
originSlide: 73
---

# 같은 표현에서도 속성마다 읽히는 정도가 다르다

::body::
<PaperFigure src="/research/sarl-summary.svg" alt="SARL에서 사건 의미, 위치, 방 특성의 정규화 접근성을 비교한 원문 막대그래프" ><template #caption>의미 · 위치 · 방의 정규화 판독 점수. 원문 축과 요인 범례 유지.</template></PaperFigure>

::takeaway::
고정 인코더의 **같은 판독 규칙**으로 의미·위치·방 정보의 접근성을 비교한다.

::source::
SARL, arXiv:2606.05544v2, Fig. 2. 민감도의 정의는 Fig. 3과 구별.

<!--
[현재 S44 · 본문]
06 · 표현에서 답변까지 무엇을 확인해야 하나

[설명의 중심]
SARL Fig. 2는 고정 표현에서 사건·위치·방 요인이 얼마나 읽히는지 비교한다. 입력 변화 민감도와의 구별은 별도 정의이며 이 한 그림이 두 지표를 직접 비교하는 것은 아니다.

[연결]
다음에 확인할 질문: 같은 잡음에서 표적 위상을 바꾸고 표현을 읽는다

[상세 근거와 해석 범위]
[S44]
[Sources]
- https://arxiv.org/html/2606.05544v2
[청중 질문]
입력 변화에 표현이 크게 움직이면 그 속성을 정확히 읽을 수 있는가?
[발표 노트]
우연 기준과 요인 그룹을 먼저 읽고, 같은 표현도 무엇을 읽느냐에 따라 결과가 달라짐을 설명한다. 이어 perturbation distance는 목표 라벨을 판독한 점수가 아니라는 차이를 묻는다.
먼저 정규화의 무작위 기준과 세 그룹을 읽는다. source의 전체 평균을 순수 위치 점수라고 부르지 않는다. 입력과 학습 데이터가 다른 모델들을 학습 목표 하나의 ablation처럼 비교하지 않는다. Fig. 3의 perturbation distance는 라벨을 판독한 점수와 다르며, 이 연구에서 시험하지 않은 공간 LLM의 실패를 주장하지 않는다.
[해석 범위]
서로 다른 mono/binaural/FOA 모델 비교는 학습 목표 하나의 통제가 아니다. 전체 source 평균을 순수 위치 성능이라 부르지 않는다. 이 연구가 시험하지 않은 공간 LLM을 실패 칸에 넣지 않는다.
[시각화 전 상세 본문 — 발표 설명용 보존]
의미 / 위치(방위·고도·거리) / 방( \mathrm{RT}_{60} ·부피·형상). 원문 정규화 축과 입력 범례 유지.

[핵심 결론]
입력 변화에 대한 민감도와 목표 요인의 판독 가능성은 같은 측정이 아니다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "06 · 표현에서 답변까지 무엇을 확인해야 하나"
causalStage: "main"
originSlide: 74
---

# 같은 잡음에서 표적 위상을 바꾸고 표현을 읽는다

::body::
<PaperFigure src="/diagrams/p3-bmld-stimulus-waveforms.svg" alt="동일한 잡음을 공유한 두 채널의 파형. 잡음만, 양쪽 n+s, 왼쪽 n+s와 오른쪽 n-s 조건을 비교하고 잡음 기준 표현 거리비를 측정한다" caption="설명용 합성 파형(시간·진폭 임의 단위) · 고정 인코더 · final-block 평균 pooling" />

::takeaway::
측정값은 <strong>잡음 기준 임베딩 거리비</strong>이며, 인간의 탐지 역치와 구별한다.

::source::
Interference/BMLD, arXiv:2606.14820v1, §2 자극 정의 재구성.

<!--
[현재 S45 · 본문]
06 · 표현에서 답변까지 무엇을 확인해야 하나

[설명의 중심]
BMLD는 같은 noise를 유지하며 오른쪽 target 위상만 반전한다. 입력 개입의 해석 가능한 사례다.

[연결]
다음에 확인할 질문: 표현의 단서 반응은 LLM의 답변 사용과 다르다

[상세 근거와 해석 범위]
[S45]
[Sources]
- https://arxiv.org/html/2606.14820v1
[청중 질문]
잡음 속 순음의 양이 위상 관계가 달라지면 고정 표현도 다르게 반응하는가?
[발표 노트]
noise-only 기준을 제시하고 동위상/역위상 표적을 더한다. 고정 인코더와 pooling을 통과한 후 두 표적 조건이 noise 표현에서 얼마나 떨어지는지 비교한다. 거리 비에 로그를 취한 값이 연구의 BMLD 유사 지표임을 설명한다.
n은 두 귀와 조건들에서 공유하는 동일 잡음, s는 표적 순음이다. 지표는 20 log10[d(antiphase,noise)/d(diotic,noise)]다. 양의 값은 역위상 표적 조건이 이 표현에서 기준 잡음과 더 멀어졌음을 뜻한다. phase flip은 오른쪽 혼합의 파형·간섭 무늬도 함께 바꾸므로 인코더 내부의 위상 비교만 조작한 실험은 아니다.
[해석 범위]
표적의 위상을 바꾸면 오른쪽 혼합 파형과 간섭 무늬도 달라진다. 단일 조작이 내부 위상 비교만 바꾸는 것은 아니다. 사람의 dB threshold 및 EC 모델 기준과 임베딩 거리비를 같은 성능 척도로 등치하지 않는다.
[시각화 전 상세 본문 — 발표 설명용 보존]
자극 | 왼쪽 채널 | 오른쪽 채널 | 
N_0  · 기준 |  n  |  n  | 
S_0N_0  · 동위상 |  s + n  |  s + n  | 
S_{\pi}N_0  · 역위상 |  s + n  |  -s + n  | 
같은 noise seed · 고정 인코더 · final-block 평균 pooling


[핵심 결론]
측정값은 noise 기준 임베딩 거리의 비이며, 인간의 탐지 역치와 구별한다.
-->

---
layout: "seminar"
variant: "result"
chapter: "06 · 표현에서 답변까지 무엇을 확인해야 하나"
causalStage: "main"
originSlide: 75
---

# 표현의 단서 반응은 LLM의 답변 사용과 다르다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">500 Hz · SNR −14 dB · 고정 인코더, 모델별 전처리 · 100 seeds/cell</p>
<PaperFigure src="/diagrams/result-75.svg" alt="표현 거리비 지표 (dB) 원문 수치 비교 그래프. Spatial-AST: 6.8*; DSpAST: 7.0*; GRAM-T: 2.1*; WavJEPA: 0.5*" />
<p class="seminar-chart-note">* 원표의 FDR 보정 표시(<MathInline tex="q=0.05" />) · 양수: 역위상 조건의 표현 거리가 더 큼</p>
</div>

::takeaway::
이 표현 거리 반응만으로 **LLM이 같은 단서를 사용한다**고 말할 수는 없다.

::source::
Interference/BMLD, arXiv:2606.14820v1, Table 1·§2.3. 원문 수치·별표 유지.

<!--
[현재 S46 · 본문]
06 · 표현에서 답변까지 무엇을 확인해야 하나

[설명의 중심]
임베딩 거리비 반응을 확인해도 인간 역치나 최종 LLM의 공간 추론이 증명되지는 않는다.

[연결]
다음에 확인할 질문: 현장 응답 대상은 전체 시스템으로 검증한다

[상세 근거와 해석 범위]
[S46]
[Sources]
- https://arxiv.org/html/2606.14820v1
[청중 질문]
모델별 양의 반응이 보이면 모두 사람처럼 잡음 속 소리를 더 잘 듣는가?
[발표 노트]
S45의 두 거리를 회수하고 양수/음수의 뜻을 설명한다. 선택 모델들의 반응을 같은 자극에서 읽되 내부 전처리는 다름을 표시한다. 왼쪽 채널만 쓰는 mono 대조군은 입력이 변하지 않아 구성상0이라는 점을 말한다.
Table 1의 네 값과 별표를 보존했다. 원문은 sign-flip permutation을 5,000회 이상 수행하고 Benjamini–Hochberg FDR 보정을 적용한다. 95% bootstrap CI는 2,000회 이상 resampling으로 구한다. 단일채널 대조는 왼쪽 입력이 동일하여 구성상 0이며, EC=15.7 dB는 인간 실측 역치가 아닌 분석적 참조다. 한 주파수·SNR를 모든 자극이나 자연 장면으로 확대하지 않는다.
[해석 범위]
EC=15.7을 인간 실측 역치나 모델의 목표 정답으로 제시하지 않는다. 한 조건의 값으로 주파수 전역 일반화를 하지 않는다. 전체 모델/주파수 곡선과 pooling 비교는 원문의 추가 자료으로 보낸다.

[시각화 전 표의 수치·조건 보존]
500 Hz · SNR −14 dB · 고정 인코더, 모델별 전처리 · 100 seeds/cell인코더 | 표현 거리비 지표 (dB) | 
Spatial-AST | 6.8* | 
DSpAST | 7.0* | 
GRAM-T | 2.1* | 
WavJEPA | 0.5* | 
* 원표의 FDR 보정 유의성 표시($q=0.05$). 양수는 역위상 조건의 거리가 더 큼.
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->

---
layout: "seminar"
variant: "result"
chapter: "06 · 표현에서 답변까지 무엇을 확인해야 하나"
causalStage: "main"
originSlide: 71
---

# 현장 응답 대상은 전체 시스템으로 검증한다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">기기에게 건넨 말인가? · WearVox · Side Talk Rejection 정확도 (%) ↑</p>
<PaperFigure src="/diagrams/result-71.svg" alt="Side Talk Rejection 정확도 (%) ↑ 원문 수치 비교 그래프. SC · beamformed: 85.4; MC · 채널 0 + beamformed: 93.9" />
<p class="seminar-chart-note">MC는 두 채널을 interleave · 원시 전체 배열의 동시 입력은 아님</p>
</div>

::takeaway::
이 <strong>추가 채널·시스템 학습 조건</strong>에서 실제 응답 대상 판단이 개선됐다.

::source::
WearVox, arXiv:2601.02391v1, Fig. 2·Table 4. 원표의 85.4를 채택.

<!--
[현재 S47 · 본문]
06 · 표현에서 답변까지 무엇을 확인해야 하나

[설명의 중심]
WearVox의 SC/MC 비교는 실환경 시스템의 응답 대상 판단이다. 채널 구성 외 설정과 실제 자료 조건도 함께 읽는다.

[연결]
다음에 확인할 질문: 연구사의 공통 질문은 공간 정보가 어디서 사라지는가다

[상세 근거와 해석 범위]
[S47]
[Sources]
- https://arxiv.org/html/2601.02391v1
[청중 질문]
이 논문의 ‘다채널’은 어떤 신호를 더 받는다는 뜻인가?
[발표 노트]
Fig. 2를 근거로 입력 차이를 말로 설명한 다음 표를 읽는다. 합성 다채널 학습과 실제 WearVox 시험을 구별한다. 같은 종류의 질문에서 추가 채널·시스템 구성이 어떤 이득을 보고했는지 한정한다.
음성 인코더를 고정하고 projection과 언어 모델을 학습한다. 실측 RIR을 활용한 합성 다채널 학습과 실제 착용자 시험을 구분한다. 채널0의 SNR, beamforming, 학습 조건이 함께 바뀌므로 위상만의 효과로 분리한 통제가 아니다. 서론의 85.6 대신 Table 4의 85.4를 사용했다.
[해석 범위]
모든 원시 마이크 채널의 동시 입력으로 그리지 않는다. 채널0의 SNR·beamforming·학습 변경이 함께 있으므로 phase-only 통제가 아니다. 초록/서론의 85.6이 아니라 Table 4의 85.4를 사용한다. 다른 응용 과제는 원문의 추가 자료 밖 참고로 남긴다.

[시각화 전 표의 수치·조건 보존]
실제 WearVox 시험 · Side Talk Rejection 정확도 (%) ↑입력·시스템 | 정확도 | 
SC · beamformed 채널 | 85.4 | 
MC · 채널 0 + beamformed | 93.9 | 
MC는 두 채널을 interleave한다. 원시 전체 배열의 동시 입력은 아니다.
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "06 · 표현에서 답변까지 무엇을 확인해야 하나"
causalStage: "main"
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
[현재 S48 · 본문]
06 · 표현에서 답변까지 무엇을 확인해야 하나

[설명의 중심]
BAT의 QA 연결, DSpAST·OWL의 공간 인코더, Motion의 구조화 언어 전달, 기존 Audio-LM의 공간 확장, 동적 장면 토큰이라는 문제 변화를 인코더·연결·언어 사용의 평가 기준으로 회수한다.

[연결]
다음에 확인할 질문: 같은 공간 장면을 유지한 통제 실험으로 H→Z→답의 연결을 확인하는 다음 연구 질문을 제안한다.

[상세 근거와 해석 범위]
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

---
layout: "seminar"
variant: "figure"
chapter: "06 · 표현에서 답변까지 무엇을 확인해야 하나"
causalStage: "main"
---

# 같은 장면에서 표현·토큰·답을 함께 검사한다

::body::
<PaperFigure src="/diagrams/causal-closing-tests.svg" alt="x축 위 두 마이크 M1과 M2의 중점 O를 원점으로 알람 A의 방위각 alpha, 고도각 beta, 거리 r를 정의한다. 같은 알람의 위치를 B로 옮긴 후 H와 Z에서 같은 판독기로 좌표를 읽고 LLM의 두 답을 정답 A와 B에 각각 대조하는 미실행 제안이다." caption="후속 실험 제안. 같은 모델·질문에서 알람만 이동하고 말소리는 유지한다." />

::takeaway::
<strong>좌표가 남고, token에 전달되고, 그 변화가 올바른 답으로 이어지는지</strong> 확인한다.

::source::
문헌 종합 기반 실험 제안 · SARL/BMLD/Spatial-Omni/BAT의 관측 범위를 구분.

<!--
[현재 S49 · 본문]
06 · 표현에서 답변까지 무엇을 확인해야 하나

[설명의 중심]
같은 공간 장면을 유지한 통제 실험으로 H→Z→답의 연결을 확인하는 다음 연구 질문을 제안한다.

[연결]
본문은 여기서 마친다. 다음 장부터는 질문별 근거 부록이며 필요한 비교를 선택해 열어 본다.

[상세 근거와 해석 범위]
[Bridge: closing-tests]
[Sources]
- https://arxiv.org/html/2606.05544v2
- https://arxiv.org/html/2606.14820v1
- https://arxiv.org/html/2606.10738v2
- https://arxiv.org/html/2402.01591v4
- https://aclanthology.org/2021.tacl-1.10/
[청중 질문]
다음에 하나의 시스템에서 어떤 세 가지 시험을 연결해야 하는가?
[발표 노트]
후속 실험 제안이며 결과는 없다. 왼쪽은 발표 도입의 동일한 알람·말소리 장면이다. 두 마이크는 x축 위 −d/2와 +d/2에 놓이며 중점 O가 원점이다. 방위각 α는 +x에서 +y 방향의 수평 회전, 고도각 β는 xy면에서 +z 방향, r은 O에서 알람까지의 거리다. 파란 A와 주황 B는 같은 알람의 서로 다른 위치이며 실제 예측 결과나 수치가 아니다.
1) 같은 encoder checkpoint의 H에서 각 좌표와 의미를 읽는다. 2) 같은 판독 조건을 adapter 뒤 Z에도 적용한다. 3) 질문을 고정하고 오디오 위치만 바꾼 쌍의 두 답을 모두 정답과 대조한다. ‘무슨 소리인가’라는 의미 질의는 그대로 유지돼야 한다. H·Z의 블록 색은 설명용이며 실측 임베딩이 아니다.
이후 Z 치환·제거와 정상 token 복구, 동일 예산의 무작위 제거, 질문만 및 오디오 치환 대조를 추가하면 단순 정보 존재와 실제 사용을 더 구분할 수 있다. probe가 높지만 답이 틀리면 과제 정렬·정보 사용을 의심할 수 있으나 원인을 확정하지 않는다. 새 방·배열·실녹음 전이와 원래 의미 성능을 별도로 검증한다.
[해석 범위]
두 마이크의 한 TDOA만으로 α·β·r가 유일하게 결정된다고 주장하지 않는다. 필요한 정보는 배열/입력/학습 조건에서 식별 가능한지 먼저 정해야 한다. 타 논문의 세 결과를 이어 한 모델의 충분조건이 증명됐다는 결론으로 만들지 않는다. 단서 반응은 사람 역치가 아니며, 선형 probe 성공은 LLM의 사용을 보장하지 않는다.
[마지막 말]
목표는 좋은 답 하나가 아니라, 어떤 공간 정보가 어디까지 남고 어떤 답에 쓰이는지 관찰 가능한 공간 표현이다.
-->
