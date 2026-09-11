# 공간 단서 계산에서 재사용할 표현으로 넘어가는 설명 구조

2026-09-11 개정. 현재 순서는 배열 기하 → GCC-PHAT → SRP → Neural-SRP → 인코더·LLM 통합이다. 이전 설명 구조와 자산 검수는 `archive/pre-localization/plans/CAUSAL_SIGNAL_BRIDGE.md`에 보존했다. P 식별자는 `EVIDENCE_P01_P11.md`와 같다. 아래 순서는 연구의 역사적 계승이나 논문 간 성능 순위가 아니라, **하나의 계산을 어디까지 유지하고 어느 부분을 학습해야 하는가**라는 설명의 순서다.

## 1. 지연 곡선에서 후보 좌표의 점수로 넘어간다

S07에서는 알려진 지연을 가진 두 합성 신호의 교차스펙트럼을 PHAT로 정규화하고 역변환한다. 결과 Cᵢⱼ(τ)의 가로축은 위치가 아니라 지연이다. 곡선의 최대점은 시간차의 예시 추정값이다. S08에서는 같은 시간차를 만드는 위치가 하나가 아님을 보여준다.

S09의 SRP는 후보 위치마다 거리차/c를 계산하고 **전체 GCC 곡선에서 해당 지연의 값을 조회**한다. 쌍마다 최대점 하나를 미리 고르는 단계는 필요하지 않다. S10은 같은 기하에서 세 마이크의 세 쌍 점수를 더해 후보 공간 응답의 최대점을 선택한다. S07–S10의 파형·GCC·쌍 응답·합산은 공유 합성 신호와 기하에서 계산하며 그림 편의상 독립 곡선을 만들어 합치지 않는다.

### 지연 부호와 공간 계산

알려진 마이크 위치를 \(p_i,p_j\), 후보 음원 위치를 \(p\), 음속을 \(c\)라 하자. 이 문서의 지연 부호는 Neural-SRP 원문 Eq. 5를 따른다.

\[
\tau_{ij}(p)=\frac{\lVert p_i-p\rVert-\lVert p_j-p\rVert}{c},\quad
R_{ij}(p)=C_{ij}^{\rm PHAT}\!\left(\tau_{ij}(p)\right),\quad
\hat p=\arg\max_{p\in\mathcal G}\sum_{i<j}R_{ij}(p).
\]

기하가 후보의 지연을 예측하고, 그 지연에서 관측 상관값을 읽으며, 쌍들의 지지를 합쳐 최대점을 고른다. **SRP도 알려진 새 배열 기하와 후보 격자를 계산에 넣을 수 있다.** 배열 변화 자체가 신경망을 요구하는 이유는 아니다. 학습을 도입하는 직접적인 동기는 잡음·잔향으로 불분명해진 관측에서 유용한 관계나 응답을 추정하는 데 있다. [Neural-SRP §III-A, Eq. 4–6](https://arxiv.org/html/2403.09455v1)

두 마이크의 지연 하나는 위치 한 점을 정하지 못한다. 같은 지연을 만드는 위치들은 2D 단면에서 쌍곡선, 3D에서 회전쌍곡면을 이룬다. 제시한 수식의 영 지연은 예외적으로 이등분 평면이다. 먼 거리에서는 방향에 대한 원뿔 모호성과 거리 정보의 약화도 남는다. S02의 3D \((\alpha,\beta,r)\)는 최종 문제의 좌표 정의이며, 그 그림의 두 마이크만으로 세 값을 유일하게 추정했다는 뜻이 아니다. 아래 Neural-SRP 설명 그림의 지도는 원문과 같은 **높이를 고정한 2D 위치 격자**다.

## 2. 비슷한 이름의 방법들이 실제로 학습하는 것

| 계산 위치 | 관측 입력과 학습 대상 | 남아 있는 기하·집계 | 출력·일반화 범위 |
| --- | --- | --- | --- |
| SRP-PHAT | STFT 교차스펙트럼을 정규화하여 상관을 계산. 학습 없음 | 후보별 기대 지연 → 쌍 응답 → 모든 쌍 합 → argmax | 알려진 기하와 원하는 후보 격자를 분석적으로 적용 |
| IPDnet 가변 배열 모델 | 기준 채널과 각 채널의 복소 STFT 실수·허수 → 음원 트랙별 **직접 경로 IPD 벡터**. PIT-MSE 지도 | 기준쌍 \(M-1\)개. 공유망의 중간 특징을 평균·방송하여 쌍끼리 통신. 출력 DP-IPD와 **기하 템플릿의 내적을 쌍 평균** | 활성 트랙마다 후보 점수와 방향. 최대 트랙 수 K는 고정. 배열 좌표는 후단 템플릿 계산에 필요 |
| Neural-SRP 원문 2024 | 쌍별 **STFT 위상 + 두 마이크 좌표 + 방 크기** → 한 쌍의 25×25 위치 응답. 같은 TDoA 능선 목표를 L1로 학습 | 모든 \(i<j\) 쌍에 공유망 적용 → 응답 합 → argmax | 알려진 높이의 2D 위치. 후보 좌표는 타깃 구성에 사용하며 추론 입력이 아님. 쌍 공유·합산으로 마이크 수 변화 처리 |
| AGG-RL 출판본 2026 | 관측+상대 마이크 기하의 표현 A와 **후보 방향 자체의 표현 G**를 학습. 정답 DOA로 만든 soft spatial spectrum에 weighted BCE | 기준 마이크와 나머지의 PHAT 교차스펙트럼, 채널 attention. 후보 임베딩과 관측 임베딩 내적 → sigmoid → peak 탐색 | 후보 개수·좌표를 바꾸어도 고정 분류 head를 교체하지 않음. 배열 변화와 후보 격자 변화는 별도 축 |

IPDnet의 한 트랙 점수는 \(s_k(q)=(M-1)^{-1}\sum_{m=2}^{M}\hat{\mathbf q}_{1m,k}^{\top}\mathbf q_{1m}(q)\)이다. 즉 **IPD 벡터를 학습한 뒤 물리적 방향 템플릿과 비교**한다. 이를 Neural-SRP의 격자 응답 직접 학습과 같은 모듈로 그리지 않는다. [IPDnet §IV-C–E, Eq. 14–20](https://arxiv.org/html/2405.07021v1)

Neural-SRP의 학습 목표는
\[
Y_{ij}(p)=\exp\!\left[-\left(\frac{|\tau_{ij}(p)-\tau_{ij}(p_s)|}{\sigma_\tau}\right)^2\right]
\]
이다. \(\sigma_\tau\)는 여기서 지연 단위를 분명히 하기 위해 이름을 붙인 폭이다. **단일 음원 점 주변의 원형 Gaussian이 아니라 같은 TDoA를 공유하는 능선**이다. 마지막 층에 활성화가 없는 응답값을 확률로 부르지 않는다. 현재 S11에서 쌍 응답 학습을 먼저 설명하고 S12의 실제 응답·S13의 결과를 읽는다. [Neural-SRP §IV, Eq. 7–10, §V-C](https://arxiv.org/html/2403.09455v1)

AGG-RL은 주파수 샘플 위치를 학습하는 LNuDFT, 상대 마이크 위치 인코딩, 후보 격자 인코딩을 구분한다. LNuDFT는 시간 샘플링이나 임의의 푸리에 기저 전체를 학습하는 주장이 아니다. 기준쌍 PHAT를 사용하므로 “쌍 관계가 전혀 없다”도 틀리다. 분리된 후보 인코더의 내적 정합은 \(\hat S(q)=\mathrm{sigmoid}(G(q)^TA/\sqrt{H})\)로 요약할 수 있다. 상대좌표 사용은 평행이동에 대한 일관성을 주지만 자동으로 회전 불변성을 뜻하지 않는다. 원문의 구면각 \(\phi\in[0,\pi]\)는 극각이므로 발표의 elevation \(\beta\)와는 \(\beta=\pi/2-\phi\)로 변환한다. [AGG-RL §3.1–3.3, Eq. 7–16](https://proceedings.iclr.cc/paper_files/paper/2026/file/ee860a9fa65a55a335754c557a5211de-Paper-Conference.pdf)

### 반드시 분리할 재구현과 결과 조건

- **AGG-RL 표의 Neural-SRP는 원문 2024 모델 그대로가 아니다.** §4.1에서 입력을 time-domain GCC-PHAT로 바꾸고, 복수 spatial spectra와 2,048점 Fibonacci DOA 격자를 출력하도록 수정한 재구현이다. 원문 25×25 위치 응답, STFT 위상 입력과 일치하지 않는다.
- 따라서 원문 Recorded4의 **1.19→0.77 m**는 그 녹음 추가 학습 조건의 위치 추정 비교이고, AGG-RL Dynamic-U의 **21.18→19.05°**, **45.51→54.13%**는 같은 논문 안의 수정 모델에 AGG-RL을 붙인 비교다. 서로 이어진 동일 모델의 개선 곡선으로 합치지 않는다. Dynamic-S에서는 개선이 일관되지 않는다.
- AGG-RL의 IPDnet 직접 정량 비교는 생략되었다. AGG-RL이 IPDnet보다 우월하다는 결과로 읽지 않는다. “Dynamic”은 이 실험에서 이동 음원을 뜻하지 않는다. [AGG-RL §4.1, Table 2–3](https://proceedings.iclr.cc/paper_files/paper/2026/file/ee860a9fa65a55a335754c557a5211de-Paper-Conference.pdf)

## 3. 위치 추정기에서 인코더로 넘어갈 때 남는 질문

마지막 argmax는 목적에 맞는 위치 출력을 만들지만, 그 좌표만 다음 단계에 전달하면 사건 종류, 시간 구조, 방의 전달 특성을 충분히 전달하지 못한다. 그렇다고 기존 localizer 내부가 그런 정보를 모두 지웠다고 단정할 수는 없다. **새 질문은 중간 표현 h에 무엇이 남아 있고 어떤 판독기가 읽을 수 있느냐**다.

특히 IPDnet과 SFD를 연결하면 전환이 선명하다. IPDnet은 예측한 물리 특징을 최종 기하 계산에 사용한다. SFD는 clean 신호에서 고정 계산한 공간 특징을 예측하도록 인코더를 학습한 뒤 **특징 예측기를 버리고 인코더를 DOA 모델의 초기값으로 사용**한다. SFD에는 별도로 학습한 teacher network가 없다. 이 전환은 “특징이 최종 제품”에서 “특징 예측이 표현을 학습시키는 과제”로 목적을 바꾼다. 실제 증거는 저라벨 DOA **미세조정**이며 frozen 범용 표현을 입증하지 않는다. [SFD §3, Fig. 1–2](https://arxiv.org/html/2508.20914v1)

범용성의 요구도 분해해야 한다: (a) 방향이 바뀌면 구별하는가, (b) 같은 장면의 다른 시간 구간이나 잡음에는 적절히 일관적인가, (c) 사건과 그 사건의 위치를 결속하는가, (d) 필요하면 방 특성도 판독 가능한가, (e) 새 기하·입력 형식·환경으로 옮겨도 작동하는가. **잔향은 DOA에는 방해일 수 있지만 T60 판독에서는 목표 정보**이므로 “공간 표현은 잔향을 지워야 한다”는 하나의 불변성 규칙을 적용하지 않는다. 이 질문들은 다음 절의 원문 설계·평가를 바탕으로 한 발표자의 종합이다.

## 4. 논문을 공간 표현의 성질과 검증 기준에 배치한다

| 표현에 요구하는 성질 | 그 성질을 유도하려는 관측 관계 | 허용되는 검증과 한계 |
| --- | --- | --- |
| 시간 구간이 달라도 사건·공간 일관성 유지 | **MC-SimCLR:** 같은 다채널 녹음의 두 crop을 양성 쌍으로 가깝게. 정지 음원 가정. 방향을 바꾸는 채널 변환은 양쪽에 일관되게 적용 | 고정 인코더의 사건·방향 **두 LP**가 증거. 모든 채널 순열·회전에 불변이라는 뜻 아님. 정지·비중첩·고정 배열 조건 |
| 채널 간 전달 관계 보존 | **CCSR:** 공간 분기의 동시 프레임 마스크와 스펙트럼 분기의 상보 마스크; 관측 관계를 이용해 가린 복소 STFT 복원 | TDOA·T60·C50로 따로 판독. 8개 방 FT에서 TDOA .40→.28 samples지만 C50 1.14→1.21 dB. 복원 성공·모든 과제 개선·frozen 우수성을 동일시하지 않음 |
| 잠재 공간 구조의 물리적 해석 가능성 | **LAM:** 잠재 비음수 음향지도 x와 알려진 steering A로 \(\hat C=A\operatorname{diag}(x)A^H\)를 만들어 관측 CSM 복원. 희소·평활 제약 | CSM을 설명하는 구조와 downstream DOA를 구별. 검출 threshold에 따른 LE/LR를 함께 검사. 특정 4→32채널 UpLAM을 임의 배열 zero-shot으로 일반화하지 않음 |
| 오염된 관측에서 방향 관련 특징 회수 | **SFD:** noisy/reverberant STFT에서 clean 비잔향 신호의 고정 공간 특징을 예측 | clean 쌍 필요. 특징 head를 제거한 후 저라벨 DOA FT에서 확인. 직접 특징 추정 성능만으로 범용성을 주장하지 않음 |
| 의미와 공간을 같은 대상에 연결 | **AT2SELD:** 태깅 의미 분기와 FOA 공간 분기의 결합 깊이 변경 | supervised SELD 적응의 동일 강한 dropout 조건에서 late-only .624 vs no-stitch .708. 초기 결합이 자동으로 유리하지 않음. 모든 조건의 공간 전용 최고 모델을 이긴 증거 아님 |
| 서로 다른 소비자가 의미·공간 정보를 읽음 | **GRAM:** 자연 장면의 다채널 mel/공간 단서 패치를 마스킹 복원. Ambisonics는 mel 4채널+IV 3채널 | 고정 인코더+얕은 판독기로 HEAR/NatHEAR/RealSELD를 평가. 합성 자연 장면과 실녹음·별도 FT를 구별. DOA boxplot 하나보다 여러 소비자의 판독이 범용성 질문에 맞음 |

원문 근거: [MC-SimCLR §3–4, Table 1](https://arxiv.org/html/2309.15938v1), [CCSR §II–III, Table III](https://arxiv.org/html/2312.00476v2), [LAM §2, Eq. 4, Fig. 3](https://arxiv.org/html/2507.07066v1), [SFD §3–5](https://arxiv.org/html/2508.20914v1), [AT2SELD Stage 3, Table 11–12](https://arxiv.org/html/2606.27751v1), [GRAM §3–4.1](https://arxiv.org/html/2506.00934v5).

각 방법은 위 성질을 **유도하려는 설계**다. 학습 목표가 그 성질을 보장한다는 정리는 아니다. 사건·DOA·방 특성의 여러 head가 성공해도 사건별 결속이나 LLM의 언어 추론까지 자동으로 입증되지 않는다. 인코더 고정 판독, 전체 미세조정, 기하 템플릿 탐색, 언어 후보 유사도, 자유형 언어 응답을 구별하여 결과를 해석한다.

## 5. 현재 슬라이드와 재현 자료

| 장 | 설명 | 자산·생성 원본 |
| --- | --- | --- |
| S07 | 두 신호 → PHAT 가중 → 지연 곡선 | `gcc-phat.svg/png/source.json`; `scripts/visuals/gcc-phat.py` |
| S08 | 같은 시간차의 위치 궤적, 한 쌍의 모호성 | `localization-tdoa-locus.svg/png/source.json` |
| S09 | 후보 좌표 → 예상 지연 → 곡선 조회 → 후보 점수 | `localization-srp-candidate.svg/png/source.json` |
| S10 | 세 쌍의 후보 응답 → 합산 → 최대 후보 | `localization-srp-sum.svg/png/source.json` |
| S11 | 쌍별 응답 계산을 학습으로 바꾸고 합산 유지 | `causal-srp-neural.svg/png`; `scripts/visuals/causal-signal.py` |
| S12–S13 | 원문의 실제 응답과 실녹음 적응 결과 | 기존 Neural-SRP 그림·보고값 유지 |
| S14–S15 | 좌표 다음에 필요한 정보 → E/P/LLM·LoRA | `causal-readout-to-encoder`, `causal-audio-llm-contract` |
| S16–S21 | 관찰 기준, 학습 과제, 판독 프로토콜과 근거 | 인코더 bridge와 기존 원문 자료 |
| S49–S51 | 선택적 배열·후보 격자 확장 | AGG-RL 기존 설명·원문 결과 |

경로가 짧게 적힌 자산은 `public/diagrams/`에 있다. S08–S10 생성기는 `scripts/visuals/localization-geometry.py`, 공통 수치 원자료는 `public/diagrams/localization-simulation.npz`다. S07–S10 전체가 하나의 공유 기하·합성 신호를 사용한다. GCC 생성기 역시 이 수치 원자료를 읽으며 독립적으로 임의 지연 곡선을 그리지 않는다. 현장 녹음이라는 뜻은 아니다.

```bash
.venv/bin/python scripts/visuals/gcc-phat.py
.venv/bin/python scripts/visuals/localization-geometry.py
.venv/bin/python scripts/visuals/causal-signal.py
```

합성 신호의 GCC와 후보 지도의 계산 결과는 교육용이며 논문 실험값이 아니다. 밝은 공통 팔레트, Pretendard, 수식 경로 조판을 사용한다. 기하·지연 부호·곡선 조회·최대점의 일치와 실제 이미지의 축·라벨·수식을 함께 확인한다. 현재 통합·배포 검수 상태는 `output/qa/localization/`와 `output/manifest.json`을 따른다.
