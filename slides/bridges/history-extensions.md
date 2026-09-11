---
layout: seminar
variant: figure
---

# 기존 Audio-LM을 살리고 공간 경로를 붙이는 문제

::body::
<PaperFigure src="/diagrams/history-extensions.svg" alt="Sci-Phi부터 기존 의미·음성 경로와 공간 경로의 병렬 결합이 중요한 설계 질문이 된다. PhaseCoder·Spatial-Omni·TWNM은 같은 모델의 순차 개선이 아니라 배열 기하·이식 절차·음원 결속에 대한 서로 다른 선택이다." />

::takeaway::
새 공간 경로를 붙인 뒤에는 **공간 정보의 기여와 기존 의미 능력**을 함께 확인해야 한다.

::source::
Sci-Phi v1 §3 · PhaseCoder v2 §3.3 · TWNM v3 §3 · Spatial-Omni v2 §3·5.

<!--
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
