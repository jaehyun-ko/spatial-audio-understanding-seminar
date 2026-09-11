---
layout: seminar
variant: figure
---

# 오디오 표현은 어떻게 LLM의 입력이 되는가

::body::
<PaperFigure src="/diagrams/causal-audio-llm-contract.svg" alt="다채널 파형 X가 인코더 E를 거쳐 T×de 표현 H가 되고 어댑터 P에서 K×dLLM 연속 오디오 토큰 Z가 된다. 질문 임베딩과 함께 고정하거나 적응한 LLM에 입력되어 답변을 생성한다." />

::takeaway::
**연속 오디오 입력의 연결**과 **LM 가중치의 적응**은 별개다. LoRA는 후자의 한 방법이다.

::source::
Spatial-Omni v2 §3 · PhaseCoder v2 §3.3 기반 교육용 재구성. 모델별 연결 순서는 다름.

<!--
[B-AUDIO-LLM-CONTRACT]
[Sources]
- https://arxiv.org/html/2606.10738v2
- https://arxiv.org/html/2601.21124v2
[그림]
public/diagrams/causal-audio-llm-contract.svg. scripts/visuals/causal-llm.py로 제작한 설명용 그림이다. 파형·격자·토큰 값은 실제 모델 출력이 아니다. 수식은 matplotlib mathtext 경로로 렌더했다.
[발표 노트]
X는 관측한 공간 오디오이다. E가 만드는 H는 인코더의 잠재 표현이다. T는 잠재 표현의 길이로, 모델에 따라 패치나 집계 토큰을 포함하므로 언제나 순수 시간 길이라는 뜻은 아니다. P는 이 표현을 LLM 입력 폭 d_LLM에 맞추고 필요하면 길이 K를 줄이거나 여러 스트림을 합친다. Q-Former, MLP, temporal shuffle와 융합 모듈이 모두 이 자리에 올 수 있다. 이후 Z는 질문 텍스트의 임베딩과 함께 디코더에 입력된다. 그림은 공통 분석 관점이며 실제 prepend/interleave와 경계 표지는 모델별로 다르다.
[정의]
LoRA는 연속 오디오 입력을 처리하는 LLM 선형층을 저랭크로 적응하는 방법이다. 이 발표의 구조도는 인코더·어댑터·LLM 적응을 구별하기 위한 공통 틀이며, 모든 Audio-LLM이 LoRA를 필수로 사용한다는 뜻은 아니다. 상세 수식과 학습 범위는 후반에서 확대한다.
연속 오디오 토큰이 기존 임베딩 차원의 입력 시퀀스에 추가된다. 새로운 어휘 항목을 추가하거나 LLM hidden width를 확대하는 것과 구분한다. PhaseCoder는 공간 soft token과 경계 표지를 구분하고, 경계 표지에 기존 미사용 token ID를 사용한다. “어댑터로 확장된 토큰 공간”이라는 모호한 표현 대신 “연속 오디오 임베딩으로 증강한 입력 시퀀스”라고 설명한다.
[해석 범위]
E가 관측에서 소실한 정보를 P나 LLM이 보장하여 복원한다는 의미가 아니다. LLM의 사전확률 추론과 오디오 정보의 보존을 구분한다. 이 구조는 연속 오디오 표현을 언어 디코더에 직접 연결하는 계열의 분석 틀이며 좌표 head, retrieval, 속성 JSON을 텍스트로 전달하는 시스템까지 필수 구조로 일반화하지 않는다.
[전환]
연결 구조를 정했으니 먼저 H에 사건·위치·시간이 읽을 수 있는 형태로 남아 있는지 확인한다. 이후 P가 무엇을 토큰에 남기는지, LoRA 등의 적응으로 LLM이 그것을 사용하는지를 차례로 본다.
-->
