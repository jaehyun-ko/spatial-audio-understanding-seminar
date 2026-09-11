---
layout: seminar
variant: figure
---

# 학습 과제는 어떤 관계를 남기게 하는가?

::body::
<PaperFigure src="/diagrams/causal-encoder-objectives.svg" alt="같은 녹음의 두 구간을 가깝게 하는 MC-SimCLR, 두 분기의 마스크로 STFT를 복원하는 CCSR, 음향지도와 물리식을 통해 CSM을 복원하는 LAM, 오염 신호에서 clean 공간 특징을 예측하는 SFD의 네 학습 관계" caption="관측 관계와 학습 목표의 도해 · 각 목표의 효과는 후속 판독 실험으로 검증" />

::takeaway::
**위치·사건·방 정보가 남도록 과제를 설계**하고, **무엇을 읽을 수 있는지 따로 검사**한다.

::source::
MC-SimCLR §3 · CCSR Fig. 1 · LAM Eq. 4 · SFD Fig. 1 · 발표자 재구성 도해

<!--
[BRIDGE: encoder-objectives 발표 노트]
[핵심 질문]
정답 위치를 직접 주지 않는 학습이 공간 표현에 어떤 성질을 유도하는가? 네 방법은 각각 다른 관측 관계를 이용하며 한 과제가 다른 과제를 차례로 대체한 순서가 아니다.

[구간 간 일관성]
MC-SimCLR는 같은 다채널 녹음에서 뽑은 두 시간 구간의 표현을 가깝게 학습한다. 정지·비중첩 음원 조건에서 사건과 위치가 일관적이라는 가정이다. 채널 변환은 양쪽 positive crop에 일관되게 적용한다. 모든 채널 순열·회전에 무조건 불변이 되는 것이 목표라고 해석하지 않는다. 효과는 고정 인코더 사건·방향 LP 등 각 프로토콜에서 읽는다.

[채널 간 관계]
CCSR의 위쪽 마스크는 spatial encoder 입력에서 두 채널의 같은 시간 프레임을 함께 가린 것이다. 아래쪽은 spectral encoder의 상보 마스크로, 해당 시간에 한 채널이 보인다. 두 분기를 결합하여 dual-channel 복소 STFT를 출력하되 손실은 한 채널의 가려진 프레임에 적용한다. 검은 구멍이나 완전히 미관측인 새 채널을 생성하는 그림이 아니다. 관측 프레임의 내용과 다른 프레임에서의 전달 관계를 같이 이용한다. CCSR도 잡음·잔향을 다룬다. 복원 성과와 TDOA/T60/C50 판독 성과를 동일시하지 않는다.

[물리적 공간 구조]
LAM의 잠재 비음수 음향지도 x와 알려진 steering matrix A를 이용하여 C_hat=A diag(x) A^H로 CSM을 복원한다. 그림의 행렬은 Hermitian PSD covariance의 크기를 단순 도해한 것이며 측정 수치가 아니다. 실제 학습은 복원 MSE와 희소·평활 제약을 사용한다. 물리적 decoder가 해석 가능성을 유도하지만 역문제의 유일성이나 범용 의미 표현을 보장하지 않는다. 후속 DOA의 LE와 LR를 함께 읽는다. UpLAM의 특정 4→32채널 구성은 임의 배열 무학습 적용의 증거가 아니다.

[오염에 강한 단서]
SFD는 오염된 바이노럴 STFT를 인코더에 넣고, 대응하는 clean 비잔향 신호에서 고정 계산한 GCC·GCC-PHAT·CPSPhase 또는 ILD+IPD를 목표로 학습한다. 이들은 별도 모델 변형이다. 오른쪽의 clean 경로는 학습된 teacher network가 아니라 특징 계산이다. 아래 곡선은 공간 특징의 개념을 나타내며 모든 특징이 직선 위상 곡선이라는 뜻은 아니다. 이 예측 head는 사전학습 후 제거하고 인코더·DOA head를 FT한다. clean 목표 신호가 필요하다.

[다음 연결과 검증]
그림 제목의 '남기게 하는가'는 설계 의도에 관한 질문이다. 표현에 정보가 남았다는 결론은 실제 판독으로 확인해야 한다. frozen LP는 이미 접근 가능한 정보를 검사하고 전체 FT는 유용한 초기화인지를 검사한다. GRAM의 여러 소비자 판독, AT2SELD의 의미 결합 깊이 실험은 여기서 남은 질문을 각각 다른 방식으로 검사한다. 단일 과제 점수가 일반적인 언어 판단 능력을 보장하지 않는다.

[Sources]
- https://arxiv.org/html/2309.15938v1
- https://arxiv.org/html/2312.00476v2
- https://arxiv.org/html/2507.07066v1
- https://arxiv.org/html/2508.20914v1
- https://arxiv.org/html/2506.00934v5
- https://arxiv.org/html/2606.27751v1
-->
