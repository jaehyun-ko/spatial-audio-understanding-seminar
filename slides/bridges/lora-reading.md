---
layout: seminar
variant: figure
---

# LoRA는 LLM의 입력 처리 방식을 조정한다

::body::
<PaperFigure src="/diagrams/causal-lora-reading.svg" alt="오디오와 질문의 임베딩 입력이 LLM 내부의 고정 선형층 W0 경로와 저랭크 A,B 학습 경로를 지난다. W=W0+(alpha/r)BA로 두 경로를 합하고 후속 층과 출력 헤드를 통해 기존 어휘에서 답변을 생성한다." />

::takeaway::
**P는 연속 오디오 토큰을 만들고, LoRA는 이를 처리하는 LLM 가중치를 적응한다.**

::source::
LoRA v2 §4.1 · BAT v4 §4.2와 저자 공개 구현은 적응 방식이 다름. 교육용 재구성.

<!--
[B-LORA-READING]
[Sources]
- https://arxiv.org/abs/2106.09685v2
- https://arxiv.org/html/2402.01591v4
- https://github.com/X-LANCE/SLAM-LLM/tree/main/examples/seld_spatialsoundqa
- https://github.com/X-LANCE/SLAM-LLM/blob/main/examples/seld_spatialsoundqa/scripts/finetune_spatial-ast_qformer_llama_2_7b.sh
- https://arxiv.org/abs/2305.11834
[그림]
public/diagrams/causal-lora-reading.svg. LLM 내부 선형층 하나를 확대한 설명용 도식이다. 실제 모델의 activations나 어휘 확률을 측정한 그림이 아니다. 아래 학습 경로에는 alpha/r scaling을 표시했으며 후속 Transformer 층과 출력 헤드는 축약했다.
[발표 노트]
P가 만든 Z와 질문 임베딩은 이미 LLM과 같은 입력 폭을 가진 연속 벡터이다. LoRA는 이 입력의 어휘를 늘리는 모듈이 아니다. W0가 기존 선형층이고 W=W0+(alpha/r)BA로 업데이트를 제한한다. W0의 크기가 d_out×d_in이면 A는 r×d_in, B는 d_out×r이다. r은 학습 업데이트의 랭크로 토큰 개수나 어휘 수와 구분한다. h는 그림에서 선택한 선형층의 입력 hidden state이며 최초 입력 임베딩과 모든 내부층에서 그대로 같다는 뜻은 아니다.
모델에 따라 attention의 Q/K/V/O 또는 FFN 선형층 등에 LoRA를 적용하므로 “읽기 적응”은 조건을 처리하는 방식의 변화라는 뜻이다. 출력 헤드만 학습한다는 설명은 부정확하다. 생성은 후속 층과 출력 헤드를 통해 기존 어휘에 대한 확률을 얻는다. 별도의 special token 추가나 embedding/head 학습은 독립적인 구현 선택이다.
[논문별 예외]
BAT v4 본문은 LLaMA-Adapter V2의 zero-initialized attention, projection, norm/bias/scale 적응을 설명한다. 반면 저자 BAT 공개 SLAM-LLM 실행 설정은 frozen Spatial-AST+Q-Former+LLM LoRA를 사용한다. 논문 실험과 공개 구현을 같은 세부 구조로 합치지 않는다. LoRA가 필요하다는 일반 명제의 근거로 BAT를 사용하지 않는다.
Pengi 2023은 audio encoder와 mapping network를 학습하고 GPT2 언어 모델을 고정한다. 연속 오디오 입력을 추가하기 위해 LoRA가 반드시 필요한 것은 아니다. 이 일반 오디오 배경 사례가 공간 QA에서 같은 성능을 보장하는 것은 아니다.
[해석 범위]
P와 LoRA를 적응시켜도 E가 관측에서 잃어버린 정보가 보장 복원되는 것은 아니다. 학습 가능한 구조가 있다는 사실, 실제 해당 모듈의 성능 기여, 다른 조건으로 일반화하는 능력은 각각 별도로 검증한다.
-->
