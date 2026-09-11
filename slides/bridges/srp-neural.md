---
layout: seminar
variant: figure
---

# 쌍별 응답 계산을 학습으로 바꾼다

::body::
<PaperFigure src="/diagrams/causal-srp-neural.svg" alt="같은 채널쌍 관측에서 SRP는 기대 지연의 상관값으로 위치 응답을 계산하고 Neural-SRP는 같은 TDoA 능선을 목표로 쌍 응답을 학습한다. 두 방법 모두 모든 쌍의 응답을 합산하고 최대 위치를 선택한다.">
<template #caption>
<div>고정 계산 <MathInline tex="R_{ij}(p)=C_{ij}^{\rm PHAT}(\tau_{ij}(p))" /> · 학습 목표 <MathInline tex="Y_{ij}(p)=\exp\!\left[-\left(\frac{|\tau_{ij}(p)-\tau_{ij}(p_s)|}{\sigma_\tau}\right)^2\right]" /></div>
</template>
</PaperFigure>

::takeaway::
**쌍의 공간 응답을 학습**하고, **쌍 합산과 최대점 선택**은 유지한다.

::source::
Neural-SRP, 2024, §III–IV, Eq. 4–10 · 높이를 고정한 2D 위치 격자 · 지도는 설명용 계산

<!--
[BRIDGE: srp-neural 발표 노트]
[핵심 질문]
고정 수식의 어느 연산을 학습으로 바꾸었는가? 앞의 SRP 설명과 같은 입력 관측·쌍 응답·합산·최대점이라는 자리를 유지해 차이를 읽는다.

[설명 순서]
SRP-PHAT에서는 알려진 배열과 후보 위치로 기대 TDoA를 계산하고, 그 지연의 PHAT 상관값을 읽는다. Neural-SRP는 채널쌍의 STFT 위상과 두 마이크의 절대좌표, 방 크기를 입력으로 받아 그 쌍의 전체 공간 응답을 예측한다. 원문 CNN-GRU 뒤의 late fusion에 메타데이터가 들어가며 출력은 25×25 위치 격자다. 후보 좌표는 타깃을 만드는 데 쓰이고 추론 입력은 아니다. 각 쌍에서 같은 가중치의 네트워크를 사용하고 모든 i<j 응답을 합하여 최대 위치를 선택한다.

[수식과 기하]
여기서 tau_ij(p)=(||p_i-p||-||p_j-p||)/c. 관측 상관의 부호와 일관되게 사용한다. 도입의 tau=t2−t1는 여기 표기의 tau_21에 해당한다. 여기서는 원문 C_ij와 대응하는 tau_ij=t_i−t_j를 사용하므로 같은 물리 관계에 첨자 순서가 반대임을 먼저 짚는다. 정답 위치 p_s와 지연이 같은 위치는 모두 큰 타깃 응답을 갖는다. 그래서 한 쌍의 목표는 점 중심 Gaussian이 아니라 같은 TDoA의 쌍곡선 능선이다. sigma_tau는 지연 단위의 폭을 명시하려고 발표에서 붙인 이름이다. 원문의 손실은 L1이며 마지막 응답 층에는 활성화가 없으므로 확률 지도로 부르지 않는다. 단일 쌍의 지연으로 3D azimuth/elevation/distance를 유일하게 구할 수 없다. 본 그림은 높이를 고정한 2D 단면이다.

[그림 조건]
지도는 설명을 위해 거리 차이로 생성한 25×25 격자다. 첫 쌍 마이크 (-0.65,0),(0.65,0), 추가 마이크 (-0.5,2.8), 설명용 음원 (0.6,1.6), 거리 차이 폭 0.11 m를 사용했다. 정량 실험이나 실제 학습망 출력을 재현하지 않았다. 위·아래에 같은 설명용 지도를 사용하여 학습 뒤의 성능 개선을 그림 자체로 주장하지 않는다. 아래의 변화는 쌍 응답 계산 방법이다.

[다른 학습 위치와 구별]
IPDnet은 복소 STFT에서 음원 트랙별 직접 경로 IPD를 학습하고, 알려진 기하의 IPD 템플릿과 내적하여 방향을 판독한다. 가변 배열 모델은 기준쌍 M−1개 사이의 중간 특징 평균·방송과 후단 템플릿 점수 평균을 사용한다. Neural-SRP의 모든 쌍 지도 직접 학습과 다른 위치에 학습을 넣는다.

[다음 연결]
기하에 맞춰 후보를 평가하는 구조는 유지할 가치가 있다. 다음 질문은 후보의 위치와 개수도 입력으로 바꾸어 물을 수 있는가다. AGG-RL 비교표의 Neural-SRP는 time-domain GCC-PHAT 입력과 다중 Fibonacci DOA 격자 출력으로 수정한 재구현이다. 원문 2024의 STFT 위상→25×25 위치 모델과 동일 모델의 연속 개선으로 그리지 않는다.

[Sources]
- https://arxiv.org/html/2403.09455v1
- https://arxiv.org/html/2405.07021v1
- https://proceedings.iclr.cc/paper_files/paper/2026/file/ee860a9fa65a55a335754c557a5211de-Paper-Conference.pdf
-->
