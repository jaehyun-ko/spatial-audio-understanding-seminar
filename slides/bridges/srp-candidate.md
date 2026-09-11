---
layout: seminar
variant: figure
---

# 후보 좌표가 예측한 지연에서 상관값을 읽는다

::body::
<PaperFigure src="/diagrams/localization-srp-candidate.svg" alt="두 후보 위치에서 마이크까지의 거리를 계산하고, 거리 차이를 음속으로 나눈 예상 지연을 같은 GCC-PHAT 곡선에 대입한다. 실제 생성 위치 A의 점수는 약1이고 다른 후보 B의 점수는 약-0.01이다.">
<template #caption>
<div>좌표 <MathInline tex="p" /> → 거리 차이 → 기대 지연 <MathInline tex="\tau_{21}(p)" /> → 쌍 응답 <MathInline tex="R_{21}(p)" /></div>
</template>
</PaperFigure>

::takeaway::
SRP는 **후보 위치의 예상 지연**이 **관측 상관과 얼마나 맞는지** 평가한다.

::source::
Neural-SRP, 2024, §III-A, Eq. 3–6 · 동일 무반향 합성 신호의 GCC-PHAT · 높이 고정

<!--
[BRIDGE: srp-candidate 발표 노트]
[핵심 질문]
지연 축의 곡선을 어떻게 공간 좌표의 점수로 바꾸는가? SRP의 핵심 한 연산을 후보 A와 B 두 개로 설명한다.

[설명 순서]
왼쪽에서 후보 pA=(0.6,1.6)를 선택한다. 알려진 두 마이크 좌표로 계산한 거리는 d1=2.030394m, d2=1.600781m다. 거리 차이를 음속으로 나누면 tau21(pA)=-1.252516ms다. 오른쪽의 GCC-PHAT 곡선에서 이 지연의 값을 읽으면 R21(pA)=0.999622...로 약 1이다.

두 번째 후보 pB=(-0.4,1.3)는 d1=1.323820m, d2=1.671077m를 예측한다. tau21(pB)=+1.012412ms로 A와 다른 지연이다. 동일한 GCC 곡선에서 읽은 값은 약 -0.01이다. A는 설명용 합성 신호를 생성한 위치여서 이 이상적인 예시에서 높은 점수가 나온다. B의 결과는 다른 관측을 사용한 비교가 아니라 같은 관측과 같은 곡선에서 읽는 위치만 바꾼 것이다.

[수식]
R21(p)=C21^PHAT(tau21(p)),
tau21(p)=(||p-M2||-||p-M1||)/c.
C21^PHAT(tau)=IFFT[X2(f) X1*(f)/|X2(f) X1*(f)|]의 tau 지연 값으로 정의하여 tau21=t2-t1 부호와 맞춘다. PHAT 값은 확률이 아니므로 음의 측엽도 가능하다. 이 설명에서는 대역에 포함된 주파수 빈 수로 IFFT를 정규화하여 완전히 맞는 이상적 지연의 응답이 1이 되도록 했다.

[계산 조건]
앞 GCC 그림과 뒤 SRP 지도는 같은 배열, 같은 음원, 같은 합성 신호를 재사용한다. fs=16kHz, N=8192(512ms), seed=20260911. 80ms 중심, 표준편차 6ms인 Gaussian envelope의 광대역 잡음을 만들고 100–4000Hz 대역을 남겼다. 각 채널은 Xi=S exp(-j2πf di/c)의 분수 지연으로 계산했다. 이는 512ms 주기의 spectral shift이며 신호 burst는 경계에서 충분히 떨어져 있다. 반사, 다중 음원, 마이크 오차, 센서 잡음은 추가하지 않은 이상적인 직접 경로 예시다.

각 쌍의 교차 스펙트럼을 실제로 계산하고 대역 안에서 PHAT 정규화한 뒤 16배 보간 IFFT를 수행했다. 기대 지연의 점수는 그 곡선을 선형 보간해서 읽었다. 16배 보간은 시간 축을 촘촘히 평가하는 계산이며 원 신호에 새 정보를 추가하는 조작이 아니다. 정확한 숫자와 배열은 source.json 및 localization-simulation.npz에 있다. 본문 숫자는 이해를 돕는 반올림값이며 보고된 논문 점수가 아니다.

[다음 연결]
후보 A만 높은 것은 아니다. 이전 쌍곡선 위의 모든 후보도 같은 tau21을 예측하므로 같은 높은 점수를 갖는다. 이제 전체 좌표 격자에서 이 계산을 반복하여 쌍별 응답 지도를 만들고, 다른 위치의 마이크를 추가했을 때 지도를 어떻게 합치는지 본다.

[출처]
- https://arxiv.org/html/2403.09455v1, §III-A, Eqs. 3–6
- https://www.mathworks.com/help/phased/ref/gccphat.html
- public/diagrams/localization-srp-candidate.source.json
- public/diagrams/localization-simulation.npz
-->
