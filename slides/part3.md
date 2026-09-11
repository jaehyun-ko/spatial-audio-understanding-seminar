---
layout: "seminar-section"
chapter: "근거 부록"
causalStage: "appendix"
---

# 근거 부록

::context::
본문의 질문을 더 자세히 확인할 때

::bridge::
A 관측과 인코더 · B 의미와 공간의 정렬<br/>
C 공간 Audio-LM의 세부 설계 · D 시간 정보의 전달 · E 답변의 근거

::source::
27편의 지정 원문 버전 · 실험 조건·수치·반례를 보존한 선택 자료

<!--
[현재 S50 · 근거 부록]
근거 부록

[설명의 중심]
본문은 49장에서 마쳤으며 이후는 질문에 따라 선택해 보는 상세 근거다.

[연결]
이 장은 본문의 근거 부록 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[근거 부록의 사용]
본문은 앞의 49장에서 마쳤다. 이 부록은 논문을 순서대로 추가 발표하기 위한 두 번째 본문이 아니다. 질문이 나오면 해당 설계 경계나 검증 조건으로 이동해 필요한 그림·표를 확인한다. 다섯 구역은 관측과 인코더, 의미와 공간 결속, 토큰으로 보내는 관측, 시간 정보 전달, 답변의 근거다. 장 번호와 논문별 연결은 CAUSAL_DECK_ORDER와 본문 근거 대장에 기록한다. 모든 수치는 기존 지정 원문의 조건에 한정한다. 설명용 범위·발표자 정리.
-->

---
layout: "seminar"
variant: "figure"
chapter: "근거 부록 A · 관측과 인코더"
causalStage: "appendix"
originSlide: 29
---

# 사전학습 목표와 표현의 재사용 시험을 분리한다

::body::
<PaperFigure src="/diagrams/p1-pretrain-probe.svg" alt="마스킹 복원 사전학습 인코더를 고정한 뒤 새 과제 정답으로 판독기를 학습하는 두 단계 프로토콜" caption="고정 판독 프로토콜 · 실녹음 전체 미세조정은 별도 평가" />

::takeaway::
**마스킹은 학습 목표**, 고정 인코더의 여러 과제 판독은 **재사용을 확인하는 시험**이다.

::source::
GRAM, arXiv:2506.00934v5, Fig. 1·HEAR 평가 프로토콜 기반 재구성.

<!--
[현재 S51 · 근거 부록]
근거 부록 A · 관측과 인코더

[설명의 중심]
GRAM은 마스킹 목표를 수행한 뒤 고정 표현으로 여러 출력을 판독한다. 학습 손실을 정보 보존의 직접 지표로 대신하지 않는다.

[연결]
이 장은 본문의 A · 관측과 인코더 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S51 발표 노트]
[설명 순서]
“사전학습에서 모델이 받는 과제와 후속 평가에서 판독기가 받는 정답은 다릅니다. 고정 특징 평가를 중심으로 읽되, 원문에 있는 전체 미세조정 비교는 별도 조건으로 구분하겠습니다.”

[경계·원문의 추가 자료]
모든 보고 결과가 고정 인코더라고 단정하지 않는다. 판독기의 용량과 학습 데이터량을 함께 기록하고 마스킹 세부 구현은 원문의 추가 자료으로 보낸다.


사전학습은 마스킹 autoencoding을 사용한다. Ambisonics는 4채널 mel 및 intensity vector, binaural은 두 귀의 mel을 다룬다. HEAR 방식에서 고정 인코더와 지도 판독기를 사용한다.
[Sources]
- https://arxiv.org/html/2506.00934v5

[시각화 전 본문 설명]
마스킹 사전학습
가린 관측을 예측하며 인코더 학습
고정 표현 추출
후속 과제에서 인코더 가중치 고정
라벨을 쓰는 판독
과제별 판독기 학습 → 방향 등 출력
입력 변형
Binaural / Ambisonics / Clean
따로 읽을 결과
실녹음 전체 미세조정은 별도의 평가

[설명 그림의 범위]
발표자 제작 SVG. 개념의 관계를 읽기 위한 도식이며 원문의 실험 관측이나 모델 추정값을 그린 결과가 아니다.
교육 참고: Dive into Deep Learning §14.2 Fine-Tuning, pretrained features와 새 출력층의 구별 및 고정 특징 평가. 각 논문의 프로토콜은 기존 출처와 노트가 기준이다.
- https://d2l.ai/chapter_computer-vision/fine-tuning.html
-->

---
layout: "seminar"
variant: "method"
chapter: "근거 부록 A · 관측과 인코더"
causalStage: "appendix"
originSlide: 25
---

# 공간 단서를 목표로 배운 초기화는 잡음에서 시험한다

::body::
<PaperFigure src="/research/sfd-1h-plot.svg" alt="SFD Fig. 2의 1시간 라벨 조건. x축 SNR dB, y축 DOA MAE 도. 원본 곡선과 축을 보존한 패널" />

::aside::
<section>
<span class="seminar-label">1시간 라벨 · 전체 미세조정</span>
<div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;font-size:20px"><span style="width:26px;border-top:3px solid #0072b2;flex:none"></span><span>GCC-PHAT-DNN</span></div><div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;font-size:20px"><span style="width:26px;border-top:3px solid #d55e00;flex:none"></span><span>GCC-DNN</span></div><div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;font-size:20px"><span style="width:26px;border-top:3px solid #009e73;flex:none"></span><span>STFT-DNN</span></div><div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;font-size:20px"><span style="width:26px;border-top:3px solid #f0e442;flex:none"></span><span>SFD-CPSPhase</span></div><div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;font-size:20px"><span style="width:26px;border-top:3px solid #cc79a7;flex:none"></span><span>SFD-GCC</span></div><div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;font-size:20px"><span style="width:26px;border-top:3px solid #999999;flex:none"></span><span>SFD-GCC-PHAT</span></div><div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;font-size:20px"><span style="width:26px;border-top:3px solid #56b4e9;flex:none"></span><span>SFD-ILD+IPD</span></div><p style="font-size:20px;margin-top:16px">x: SNR (dB)<br/>y: DOA MAE (°), 낮을수록 좋음</p>
</section>

::takeaway::
이 결과는 **공간 특징 사전학습 후 전체 미세조정**의 근거다. 고정 표현 판독과는 다르다.

::source::
SFD, arXiv:2508.20914v1, Fig. 2의 1h 패널. 원본 벡터 크롭·범례 재배치.

<!--
[현재 S52 · 근거 부록]
근거 부록 A · 관측과 인코더

[설명의 중심]
SFD는 clean 공간 특징 목표를 쓰지만 이 그림의 성과는 저라벨 전체 미세조정 조건이다. 앞의 frozen probe와 구별한다.

[연결]
이 장은 본문의 A · 관측과 인코더 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S52 발표 노트]
[설명 순서]
“여기서는 라벨 시간과 백본을 맞추고 초기화만 비교하겠습니다. 사전학습 이후 인코더도 DOA에 맞춰 바뀌므로, 이 결과는 적응에 유용한 초기 표현의 증거로 읽어야 합니다.”

[경계·원문의 추가 자료]
Table 2의 1시간·10시간 표기 충돌 때문에 그 표는 사용하지 않는다. 10분 패널과 다른 변형은 원문의 추가 자료이며 서로 다른 데이터 조건의 수치를 섞지 않는다.


주비교는 STFT-DNN(녹색)과 SFD-CPSPhase(노랑). 두 모델은 STFT 입력, 545k 파라미터와 1시간 라벨 학습량을 공유한다. SFD는 LibriSpeech 원음 960시간 기반 사전학습을 추가로 사용하고 인코더와 DOA head를 함께 미세조정한다. 단일 정지 음성·합성 바이노럴, HRTF 피험자 분리. 평가 잡음은 학습과 같은 종류의 다른 클립. 원래 나머지 곡선과 범례를 보존했다. 곡선으로 정밀 수치를 만들지 않는다. Table 2의 caption 1h/본문10h 충돌 때문에 해당 표는 본문에서 쓰지 않는다.
[Sources]
- https://arxiv.org/html/2508.20914v1
-->

---
layout: "seminar"
variant: "figure"
chapter: "근거 부록 A · 관측과 인코더"
causalStage: "appendix"
originSlide: 12
---

# 배열 좌표와 후보 격자는 서로 다른 변경이다

::body::
<PaperFigure src="/diagrams/p1-query-grid.svg" alt="같은 녹음과 마이크 배열을 유지하며 후보 방향 목록을 성긴 격자에서 촘촘한 격자로 바꾼 기하" caption="마이크 배열은 고정 · 질의할 후보 방향의 간격과 개수만 변경" />

::takeaway::
**배열 기하**와 **후보 방향 격자**는 독립적으로 달라질 수 있다.

::source::
AGG-RL, ICLR 2026. 설명용 재구성.

<!--
[현재 S53 · 근거 부록]
근거 부록 A · 관측과 인코더

[설명의 중심]
새 채널 기하와 새 후보 방향 목록은 서로 다른 일반화 요구다.

[연결]
이 장은 본문의 A · 관측과 인코더 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S53 발표 노트]
[설명 순서]
“앞에서는 녹음하는 마이크 배치를 바꿨지만, 여기서는 같은 녹음에 물어볼 방향 목록을 바꿉니다. 출력 칸이 고정된 모델과 후보 방향을 조건으로 받는 모델은 이 요구를 다르게 다룹니다.”

[경계·원문의 추가 자료]
후보 수 증가를 각도 정확도의 자동 향상으로 표현하지 않는다. 임의 격자와 임의 실제 배열 모두에 대한 보장도 주장하지 않는다.


AGG-RL §2.2 기반 설명용 재구성. 앞의 배열 변경과 이번 후보 목록 변경을 분리한다. 후보 수를 늘린다고 각도 정확도가 자동 향상되지는 않는다. 고정 출력 칸과 후보 조건 입력이라는 설계의 차이를 설명하되 임의 배열 전체에 대한 보장으로 확대하지 않는다.
[Sources]
- https://proceedings.iclr.cc/paper_files/paper/2026/file/ee860a9fa65a55a335754c557a5211de-Paper-Conference.pdf

[시각화 전 본문 설명]
관측 조건마이크 배열
어디에서 소리를 받는가
질의 조건후보 격자
어떤 방향들을 물어보는가
이번 변화같은 녹음
후보 방향의 간격·개수만 변경

[설명 그림의 범위]
발표자 제작 SVG. 개념의 관계를 읽기 위한 도식이며 원문의 실험 관측이나 모델 추정값을 그린 결과가 아니다.
-->

---
layout: "seminar"
variant: "method"
chapter: "근거 부록 A · 관측과 인코더"
causalStage: "appendix"
originSlide: 13
---

# AGG-RL: 기하와 후보 방향의 정합

::body::
<PaperFigure src="/research/agg-rl-overall.png" alt="AGG-RL Fig. 2 오디오와 마이크 기하의 표현을 후보 방향 표현과 비교하는 구조" />

::aside::
<section><span class="seminar-label semantic-input">관측 경로</span><p>다채널 오디오 + 마이크 좌표</p></section>
<section><span class="seminar-label semantic-geometry">후보 경로</span><p>판정할 방향 격자</p></section>
<section><span class="seminar-label semantic-result">표현의 비교</span><p>두 표현의 정합으로 공간 응답 계산</p></section>

::takeaway::
후보 방향도 입력으로 받아 **후보별 공간 응답**을 계산한다.

::source::
Baek et al., AGG-RL, ICLR 2026, Fig. 2 / 공식 프로젝트 그림.

<!--
[현재 S54 · 근거 부록]
근거 부록 A · 관측과 인코더

[설명의 중심]
AGG-RL은 오디오·기하·후보 격자 정합이라는 다른 설계 질문을 다룬다. 원형 Neural-SRP와 재구현 차이를 구별한다.

[연결]
이 장은 본문의 A · 관측과 인코더 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S54 발표 노트]
[설명 순서]
“그림에서 먼저 오디오와 마이크 좌표가 들어오는 경로, 후보 방향이 들어오는 경로를 나눠 보겠습니다. 이들이 만드는 표현을 비교해 각 후보의 응답을 계산하는 것이 이번 설계의 핵심입니다.”

[경계·원문의 추가 자료]
LNuDFT·rMPE를 학습 목표라고 부르지 않는다. 모든 내부 층과 손실 유도는 원문의 추가 자료이며 구조만으로 일반화 성능을 결론내리지 않는다.


LNuDFT는 주파수 단서 처리, rMPE는 마이크 상대 기하 표현과 연결한다. 둘은 학습 목표 이름이 아니다. 그림의 전체 층을 모두 읽기보다 입력 경로와 두 표현의 정합을 짚는다. 성능은 다음 실험 조건에서 따로 확인한다.
[Sources]
- https://proceedings.iclr.cc/paper_files/paper/2026/file/ee860a9fa65a55a335754c557a5211de-Paper-Conference.pdf

[원형과 재구현의 구별]
Neural-SRP 2024 원형은 STFT 위상·쌍 좌표·방 크기로 25×25 2D 위치 응답을 예측한다. AGG-RL 2026 §4.1의 Neural-SRP는 time-domain GCC-PHAT 입력·Fibonacci DOA 격자·다중 spatial spectra로 수정된 재구현이다. 앞의 Recorded 4 위치 오차와 여기 Dynamic-U DOA 결과는 한 checkpoint의 단계적 향상이나 동일 과제의 연속 성능 비교가 아니다.
-->

---
layout: "seminar"
variant: "result"
chapter: "근거 부록 A · 관측과 인코더"
causalStage: "appendix"
originSlide: 14
---

# 기하 정합의 효과는 미노출 채널 수로 시험한다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">Dynamic-U · 학습 4–12채널 / 시험 13–16채널</p>
<PaperFigure src="/diagrams/result-14.svg" alt="방향 MAE (°) ↓, $\mathrm{ACC}_{10}$ (%) ↑ 원문 수치 비교 그래프. 기본 Neural-SRP: 21.18, 45.51; AGG 적용: 19.05, 54.13" />
<p class="seminar-chart-note">합성 · 최대 두 정지 화자 · Dynamic-S에서는 두 지표가 개선되지 않음</p>
</div>

::takeaway::
AGG-RL의 **DOA 재구현 안에서** 정합의 효과를 비교한다. 원형의 2D 위치 실험과는 구별한다.

::source::
AGG-RL, ICLR 2026, Table 3, Neural-SRP without/with AGG-RL. 원문 수치의 그래프 재구성.

<!--
[현재 S55 · 근거 부록]
근거 부록 A · 관측과 인코더

[설명의 중심]
동일 재구현 안에서 AGG 유무를 비교한다. 앞의 2D 위치 실험과 이 DOA 실험을 연속 성능 향상처럼 읽지 않는다.

[연결]
이 장은 본문의 A · 관측과 인코더 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S55 발표 노트]
[설명 순서]
“여기서 Dynamic은 음원 이동이 아니라 배열 조건입니다. 같은 기준 모델의 정합 유무를 비교하면 미관측 채널 수에서 이득이 있지만, 학습 채널 수 범위인 Dynamic-S에서는 개선되지 않습니다.”

[경계·원문의 추가 자료]
모든 배열 일반화의 보장으로 읽지 않는다. Proposed 전체 시스템, Dynamic-S 상세, Table 4 격자 수와 Table 5 비용은 별도 원문의 추가 자료이다.


Dynamic은 음원 이동이 아니라 배열 조건을 뜻한다. ACC10은 10° 이내의 비율. 원표의 MAE ±는 95% 신뢰구간이며 여기서는 점추정만 표시했다. 전체 Proposed 모델의 성과를 AGG 하나의 효과로 대체하지 않는다.
[Sources]
- https://proceedings.iclr.cc/paper_files/paper/2026/file/ee860a9fa65a55a335754c557a5211de-Paper-Conference.pdf

[시각화 전 표의 수치·조건 보존]
Dynamic-U · 학습 4–12채널 / 시험 13–16채널Neural-SRP | MAE (°) ↓ | $\mathrm{ACC}_{10}$ (%) ↑ | 
기본 모델 | 21.18 | 45.51 | 
AGG 적용 | 19.05 | 54.13 | 

[조건]
합성 평가최대 두 정지 화자 / TIMIT 음성·ESC-50 잡음

조건의 경계Dynamic-S에서는 두 지표가 개선되지 않았다.
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.

[원형과 재구현의 구별]
Neural-SRP 2024 원형은 STFT 위상·쌍 좌표·방 크기로 25×25 2D 위치 응답을 예측한다. AGG-RL 2026 §4.1의 Neural-SRP는 time-domain GCC-PHAT 입력·Fibonacci DOA 격자·다중 spatial spectra로 수정된 재구현이다. 앞의 Recorded 4 위치 오차와 여기 Dynamic-U DOA 결과는 한 checkpoint의 단계적 향상이나 동일 과제의 연속 성능 비교가 아니다.

[시험 축]
후보 재질의 기능과 구별하여, 이번 정량 비교는 미노출 채널 수를 검사한다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "근거 부록 A · 관측과 인코더"
causalStage: "appendix"
originSlide: 16
---

# 입력 형식이 다르면 보존된 단서도 다르다

::body::
<PaperFigure src="/diagrams/p1-input-representations.svg" alt="물리적 위치의 마이크 배열과 두 귀 관측 및 구면조화 FOA 기저 성분을 구별한 그림" caption="FOA는 구면조화 기저 성분 표현 · 기저의 형태는 설명용 단면" />

::takeaway::
**추론 때 주는 정보**와 **학습 정답을 만드는 정보**를 나눠 읽는다.

::source::
AGG-RL, ICLR 2026; SFD, arXiv:2508.20914v1; GRAM, arXiv:2506.00934v5. 설명용 재구성.

<!--
[현재 S56 · 근거 부록]
근거 부록 A · 관측과 인코더

[설명의 중심]
배열·binaural·FOA는 다른 관측 계약이다.

[연결]
이 장은 본문의 A · 관측과 인코더 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S56 발표 노트]
[설명 순서]
“마이크 배열의 채널, 두 귀의 관측, FOA의 공간 성분은 같은 종류의 채널 목록이 아닙니다. 또한 오디오를 해석할 때 주는 정보와 학습 정답을 만드는 정보도 나눠 보아야 합니다.”

[경계·원문의 추가 자료]
FOA를 마이크 네 개라고 설명하지 않는다. 모든 모델에 좌표나 깊이가 추론 입력으로 들어간다는 보편 도식도 피한다.


배열에서 절대/상대 좌표는 방법에 따라 입력이 된다. 바이노럴의 HRTF가 언제나 별도 추론 텐서로 제공된다는 의미는 아니다. FOA는 구면조화 기저 성분 표현이다. 깊이 정보도 어떤 방법에서는 학습 지도에만 사용되므로 보편적인 추론 입력으로 그리지 않는다.
[Sources]
- https://proceedings.iclr.cc/paper_files/paper/2026/file/ee860a9fa65a55a335754c557a5211de-Paper-Conference.pdf
- https://arxiv.org/html/2508.20914v1
- https://arxiv.org/html/2506.00934v5

[시각화 전 본문 설명]
오디오 관측과 기하·지도 정보는 별개의 조건
입력 형식 | 채널이 뜻하는 것 | 추가 정보의 역할
마이크 배열 | 서로 다른 위치의 관측 | 좌표: 방법에 따라 추론 입력
바이노럴 | 두 귀의 관측 | HRTF: 청자별 전달 특성
FOA | 구면조화의 1차 성분 | 네 개의 점 마이크와 다름

[설명 그림의 범위]
발표자 제작 SVG. 개념의 관계를 읽기 위한 도식이며 원문의 실험 관측이나 모델 추정값을 그린 결과가 아니다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "근거 부록 A · 관측과 인코더"
causalStage: "appendix"
originSlide: 15
---

# 좌표에 사건 이름까지 붙이면 SELD가 된다

::body::
<PaperFigure src="/diagrams/p1-seld-timeline.svg" alt="말소리와 알람의 활성 시간 구간을 방향 화살표와 연결한 SELD 출력 형식" caption="고정 클래스 SELD · 정적 두 음원의 설명용 예시" />

::takeaway::
방향에 **사건 종류와 활성 시점**을 연결한 출력이 SELD다.

::source::
SELD 출력 형식의 설명용 예시. 실제 추정 결과가 아님.

<!--
[현재 S57 · 근거 부록]
근거 부록 A · 관측과 인코더

[설명의 중심]
고정 클래스 SELD도 사건과 위치를 연결한다. LLM 이전 설계의 범위를 확인한다.

[연결]
이 장은 본문의 A · 관측과 인코더 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S57 발표 노트]
[설명 순서]
“지금 요구하는 것은 방향 목록에 사건 종류와 활성 시점을 연결한 출력입니다. 이 결합은 SELD도 다루므로, 본문에서 논의한 언어 모델이 처음 가능하게 만든 능력으로 설명하지 않겠습니다.”

[경계·원문의 추가 자료]
고정 클래스 SELD를 자유 어휘 질의나 자유형 답변과 동일시하지 않는다. 평가 지표의 세부 정의는 실제 결과를 읽을 때 소개한다.


고정 클래스 sound event localization and detection을 설명한다. 의미와 위치의 결합이 LLM 등장 후 처음 가능해진 것은 아니다. 자유 어휘 질의 또는 자유형 답변 생성과는 출력 계약이 다르다.
[Sources]
- https://arxiv.org/html/2606.27751v1

[시각화 전 본문 설명]
같은 설명용 두 음원 장면
음원 | 사건 종류 | 활성 시점 | 방향
음원 A | 말소리 | 말하는 동안 | 왼쪽
음원 B | 알람 | 울리는 동안 | 오른쪽

[설명 그림의 범위]
발표자 제작 SVG. 개념의 관계를 읽기 위한 도식이며 원문의 실험 관측이나 모델 추정값을 그린 결과가 아니다.
교육 참고: DCASE 2019 공식 SELD 과제 정의의 사건 클래스·onset/offset·DOA 대응. 타임라인은 임의 시각과 활동 구간의 설명용 장면이다.
- https://dcase.community/challenge2019/task-sound-event-localization-and-detection
-->

---
layout: "seminar"
variant: "figure"
chapter: "근거 부록 A · 관측과 인코더"
causalStage: "appendix"
originSlide: 23
---

# 위치 오차는 검출 범위와 함께 읽어야 한다

::body::
<PaperFigure src="/research/p1-lam-threshold.svg" alt="LAM Fig. 3 같은 UpLAM GRU-MHSA의 검출 threshold에 따른 LE와 LR" caption="STARSS dev-test-sony: 실선이 평가 곡선. 점선은 검증, 녹색선은 기본 임계값 0.5." />

::takeaway::
임계값을 낮추면 **재현율과 위치 오차가 함께 높아질 수 있다.**

::source::
LAM, arXiv:2507.07066v1, Fig. 3. 원문 벡터; LE (°) ↓, LR (%) ↑.

<!--
[현재 S58 · 근거 부록]
근거 부록 A · 관측과 인코더

[설명의 중심]
LAM은 잠재 지도를 읽는 threshold에 따라 LE/LR이 달라진다.

[연결]
이 장은 본문의 A · 관측과 인코더 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S58 발표 노트]
[설명 순서]
“여기서는 두 모델의 우열이 아니라 같은 모델의 검출 기준을 바꿉니다. 놓치는 음원과 위치 오차가 어떻게 함께 달라지는지 보면서, 기본 임계값에서 얻은 결과의 의미를 확인하겠습니다.”

[경계·원문의 추가 자료]
곡선의 여러 점을 서로 다른 모델로 설명하지 않는다. Table 2의 모델 비교는 원문의 추가 자료이며, 이 결과를 음원 종류나 자연어 이해로 확대하지 않는다.


두 패널은 두 모델이 아니라 같은 UpLAM + GRU-MHSA의 LE와 LR이다. 실선 evaluation만 주근거로 읽고 점선 validation을 시험 성과로 혼동하지 않는다. LE는 낮을수록, LR은 높을수록 좋다. Eigenscape 10시간+SpatialScaper 합성 10시간으로 CSM 복원을 학습했다. 후속 DOA 판독기는 STARSS dev-train-tau/sony와 companion synthetic data로 지도학습하고 dev-test-tau로 검증했다. 기본 임계값0.5의 평가 표값은 LE18.65°, LR57.6%; 곡선에서 새 수치를 추정하지 않았다.
[Sources]
- https://arxiv.org/html/2507.07066v1
-->

---
layout: "seminar"
variant: "method"
chapter: "근거 부록 A · 관측과 인코더"
causalStage: "appendix"
originSlide: 24
---

# 공간 단서를 목표로 정해 인코더를 학습한다

::body::
<PaperFigure src="/research/sfd-framework.svg" alt="SFD Fig. 1 오염된 바이노럴 입력에서 깨끗한 공간 특징을 예측한 뒤 DOA 미세조정" />

::aside::
<section><span class="seminar-label semantic-input">모델 입력</span><p>잡음·잔향이 섞인 바이노럴 STFT</p></section>
<section><span class="seminar-label semantic-geometry">사전학습 목표</span><p>clean 신호에서 계산한 공간 특징</p></section>
<section><span class="seminar-label semantic-result">후속 과제</span><p>특징 예측기를 버리고 DOA에 미세조정</p></section>

::takeaway::
오염된 입력으로 **깨끗한 비잔향 신호의 공간 특징**을 예측한다.

::source::
SFD, arXiv:2508.20914v1, Fig. 1. 원문 벡터.

<!--
[현재 S59 · 근거 부록]
근거 부록 A · 관측과 인코더

[설명의 중심]
SFD의 학습 목표는 별도 teacher network가 아니라 clean audio의 공간 특징이다.

[연결]
이 장은 본문의 A · 관측과 인코더 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S59 발표 노트]
[설명 순서]
“이 방법은 모델이 복원할 대상을 원래 파형 전체 대신 공간 특징으로 정합니다. 깨끗한 신호에서 얻은 목표를 오염된 입력으로 예측하게 한 뒤 DOA 과제에 적응합니다.”

[경계·원문의 추가 자료]
GCC·GCC-PHAT·CPS 위상·ILD/IPD를 모두 한 손실로 합쳐 학습했다고 설명하지 않는다. 세부 목표 수식은 해당 결과 해석에 필요한 것만 남긴다.


GCC, GCC-PHAT, CPSPhase, ILD+IPD는 각각 별도의 특징 목표 변형이다. 여러 목표를 한 손실로 모두 결합한 모델로 설명하지 않는다. 별도 학습된 teacher network가 아니라 clean 비잔향 바이노럴 신호의 분석적 특징 추출이다. DOA 라벨이 없어도 clean target은 필요하다.
[Sources]
- https://arxiv.org/html/2508.20914v1
-->

---
layout: "seminar"
variant: "result"
chapter: "근거 부록 A · 관측과 인코더"
causalStage: "appendix"
originSlide: 21
---

# 복원이 모든 물리량의 보존을 보장하지는 않는다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">학습 방 8개 · 검증/시험 각 20개 방 · 4회 평균</p>
<PaperFigure src="/diagrams/result-21.svg" alt="TDoA MAE (samples) ↓ 원문 수치 비교 그래프. 처음부터 지도학습: 0.40; 사전학습 + 전체 미세조정: 0.28" />
<p class="seminar-chart-note"><MathInline tex="C_{50}" /> MAE는 1.14 → 1.21 dB로 증가 · 두 마이크·단일 정지 음성</p>
</div>

::takeaway::
TDoA 오차는 줄었지만 **모든 공간 지표가 개선된 것은 아니다.**

::source::
CCSR, arXiv:2312.00476v2, Table III, 8-room condition. 원문 수치의 그래프 재구성.

<!--
[현재 S60 · 근거 부록]
근거 부록 A · 관측과 인코더

[설명의 중심]
CCSR은 전체 미세조정에서 TDoA는 개선하지만 C50는 악화한다.

[연결]
이 장은 본문의 A · 관측과 인코더 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S60 발표 노트]
[설명 순서]
“여기서는 후속 조건에서 처음부터 학습한 경우와 전체 미세조정한 경우를 비교합니다. TDoA는 개선됐지만 C50 오차는 1.14 dB에서 1.21 dB로 증가해, 모든 지표가 함께 좋아지지는 않았습니다.”

[경계·원문의 추가 자료]
C50 반례를 짧은 주석으로 남긴다. frozen의 TDoA 1.49와 T60 상세는 원문의 추가 자료이며, 전체 적응 결과를 고정 표현의 선형 접근성으로 표현하지 않는다.


전체 downstream 모델을 업데이트한 fine-tuning 비교다. 고정 인코더의 TDoA 1.49 samples와 섞어 사전학습 이득을 계산하지 않는다. C50는 초기 50 ms와 후기 에너지 비율의 명료도 지표이며 여기서는 dB MAE를 비교한다. CCSR도 잡음과 잔향을 포함한다.
[Sources]
- https://arxiv.org/html/2312.00476v2

[시각화 전 표의 수치·조건 보존]
학습 방 8개 · 검증/시험 각 20개 방 · 4회 평균학습 설정 | TDoA MAE (samples) ↓ | 
처음부터 지도학습 | 0.40 | 
사전학습 + 전체 미세조정 | 0.28 | 

[조건]
평가 입력두 마이크, 단일 정지 음성 / 합성 잔향·SNR 15–30 dB

함께 읽을 반례$C_{50}$ MAE: 1.14 → 1.21 dB / 오히려 증가
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "근거 부록 A · 관측과 인코더"
causalStage: "appendix"
originSlide: 30
---

# 고정 표현의 위치 판독으로 재사용을 확인한다

::body::
<PaperFigure src="/research/p1-gram-doa.svg" alt="GRAM Fig. 3(A) SC-5와 ESC-50의 고정 표현 DOA 오차 boxplot과 원본 범례" caption="합성 자연 장면 · 고정 인코더 + 지도 판독기. 중앙선: 중앙값, 상자: 사분위 범위." />

::takeaway::
**중앙값과 퍼짐**, 그리고 모델마다 다른 입력 조건을 함께 읽는다.

::source::
GRAM, arXiv:2506.00934v5, Fig. 3(A). 원본 벡터 크롭·범례 재배치.

<!--
[현재 S61 · 근거 부록]
근거 부록 A · 관측과 인코더

[설명의 중심]
GRAM의 median·IQR과 native input 조건을 보존해 판독 범위를 읽는다.

[연결]
이 장은 본문의 A · 관측과 인코더 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S61 발표 노트]
[설명 순서]
“먼저 각 분포가 어떤 입력에서 나온 고정 특징인지 확인하겠습니다. 중앙값과 퍼짐을 함께 읽되, 입력까지 통제한 동일 조건의 사전학습 제거 실험으로 해석하지는 않겠습니다.”

[경계·원문의 추가 자료]
T60과 STARSS23 전체 미세조정은 원문의 추가 자료이다. TAU2019 측정 RIR 합성을 전체 실제 녹음이라 부르거나 실녹음 적응 결과를 고정 판독과 합치지 않는다.


GRAM-Ambisonics와 SpatialAST(supervised)를 중심으로 읽되 원래 입력과 학습 데이터가 다르다는 것을 명시한다. GRAM-Bin.Patch/Time은 바이노럴, GRAM-Ambisonics는 FOA, GRAM-Clean은 clean 음원 학습 조건이다. SC-5 음성과 ESC-50 환경음을 공간화한 합성 자연 장면에서 고정 특징으로 판독했다. 원본 box는 first/third quartile, center line median, whiskers1.5IQR다. 평균 막대로 바꾸거나 수치를 눈대중으로 읽지 않았다. 입력까지 통제한 masking ablation이 아니다.
[Sources]
- https://arxiv.org/html/2506.00934v5
-->

---
layout: "seminar"
variant: "figure"
chapter: "근거 부록 B · 의미와 공간의 정렬"
causalStage: "appendix"
originSlide: 32
---

# “뒤쪽의 알람”은 종류와 위치가 함께 맞아야 한다

::body::
<PaperFigure src="/diagrams/p1-spatial-language.svg" alt="청자 뒤 알람 관측과 동일한 소리 이름에 앞쪽 또는 뒤쪽 공간 표현을 붙인 두 문장 후보" caption="설명용 문장 후보 · 실제 모델의 정합 점수나 성공 예시가 아님" />

::takeaway::
ELSA의 검색용 문장 정렬은 **사건과 위치를 함께 맞추는 요구**를 보여 준다.

::source::
ELSA의 공간 오디오–언어 정렬 문제에 기반한 설명용 후보. 실제 모델 점수가 아님.

<!--
[현재 S62 · 근거 부록]
근거 부록 B · 의미와 공간의 정렬

[설명의 중심]
ELSA의 검색은 어떤 의미 결속을 토큰에 남겨야 할지 보여 준다. 생성형 LLM의 성과는 아니다.

[연결]
이 장은 본문의 B · 의미와 공간의 정렬 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S62 발표 노트]
[설명 순서]
“여기서는 자유롭게 답을 생성하는 대신 후보 문장과 녹음이 얼마나 맞는지 비교합니다. 소리 이름이 같은 문장도 위치가 다르면 다른 대응으로 구별해야 합니다.”

[경계·원문의 추가 자료]
설명용 후보의 성공을 ELSA의 실험 결과로 표시하지 않는다. 프롬프트 분류·검색과 생성형 QA는 출력 방식부터 다르다.


C32. 요구 출력은 후보 문장의 선택 또는 정합 점수다. 임의의 점수를 넣지 않았다. ELSA의 prompt 분류와 검색은 자유롭게 답변을 생성하는 QA와 다르다. 근거 부록의 ELSA 결과 장에서 동일 모델의 합성/실녹음 방향 분류를 확인한다.
[Sources]
- https://papers.neurips.cc/paper_files/paper/2024/file/3acc054949b6948d4444b35d412cab56-Paper-Conference.pdf

[시각화 전 본문 설명]
관측공간 오디오
알람 소리 + 위치 단서
문장 후보 A앞쪽의 알람
같은 종류, 다른 방향
문장 후보 B뒤쪽의 알람
위치 표현까지 맞는가

[설명 그림의 범위]
발표자 제작 SVG. 개념의 관계를 읽기 위한 도식이며 원문의 실험 관측이나 모델 추정값을 그린 결과가 아니다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "근거 부록 B · 의미와 공간의 정렬"
causalStage: "appendix"
originSlide: 34
---

# 의미와 공간을 따로 배우고 같은 음원에 연결한다

::body::
<PaperFigure src="/diagrams/p1-salm-factorization.svg" alt="같은 알람의 위치 변화와 omni 의미 분기 및 FOA 공간 분기의 서로 다른 caption 정렬 목표" caption="원래 caption과 공간 caption을 구별하는 분기 역할의 개념도" />

::takeaway::
SALM은 **의미·공간을 각각 감독하고 결합**한다. LLM의 답변 생성과는 다른 정렬 문제다.

::source::
SALM, arXiv:2507.16724v2, Fig. 1 기반 분기 역할 재구성.

<!--
[현재 S63 · 근거 부록]
근거 부록 B · 의미와 공간의 정렬

[설명의 중심]
SALM의 구조화 정렬은 사건 의미와 위치를 어떤 감독으로 결합할지 보여 준다.

[연결]
이 장은 본문의 B · 의미와 공간의 정렬 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S63 발표 노트]
[설명 순서]
“같은 알람을 다른 위치로 옮기면 소리의 종류는 유지되지만 공간 속성은 바뀝니다. SALM은 이 차이를 표현의 분리와 언어 정렬이라는 설계 선택으로 다룹니다.”

[경계·원문의 추가 자료]
두 분기를 만들었다는 사실만으로 완전한 요인 분리를 입증했다고 말하지 않는다. 임베딩 편집은 본문의 파형 생성 성과로 쓰지 않는다.


그림은 같은 알람의 위치를 바꾼 설명용 사고실험이다. SALM은 semantic/text를 CLAP으로, 공간 DOA 분기를 PSELDNet으로 초기화한다. omni semantic branch와 FOA spatial branch를 결합하며 원래 caption과 spatial caption을 구별한다. 분기 구조 자체가 통계적 독립성이나 완전한 요인 분리를 입증하지 않는다. 임베딩 조작을 파형 편집 성과로 확대하지 않는다.
[Sources]
- https://arxiv.org/html/2507.16724v2

[시각화 전 본문 설명]
공통 소리알람
장소가 달라도 종류는 유지
의미 분기omni 채널
원래 caption과 정렬
공간 분기FOA 전체
공간 caption·방향과 연결

[설명 그림의 범위]
발표자 제작 SVG. 개념의 관계를 읽기 위한 도식이며 원문의 실험 관측이나 모델 추정값을 그린 결과가 아니다.
-->

---
layout: "seminar"
variant: "result"
chapter: "근거 부록 B · 의미와 공간의 정렬"
causalStage: "appendix"
originSlide: 35
---

# 의미 정렬을 더하면 검색과 위치 판독이 어떻게 바뀌나

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">동일 SALM · 합성 FOA sClotho 평가</p>
<PaperFigure src="/diagrams/result-35.svg" alt="T2A R@1 (%) ↑, A2T R@1 (%) ↑, 위치 오차 (°) ↓ 원문 수치 비교 그래프. $L_{\mathrm{sCL}}+L_{\mathrm{DOA}}$: 9.1, 9.6, 1.8; 위 조건 + $L_{\mathrm{CL}}$: 10.5, 10.4, 1.6" />
</div>

::takeaway::
**의미 정렬 loss의 기여**를 본 결과다. LLM·LoRA의 효과를 측정한 표가 아니다.

::source::
SALM, arXiv:2507.16724v2, Table 1, sClotho. 원문 수치의 그래프 재구성.

<!--
[현재 S64 · 근거 부록]
근거 부록 B · 의미와 공간의 정렬

[설명의 중심]
SALM의 동일 모델 loss 비교로 의미 목표의 기여를 본다. adapter/LoRA ablation과 구별한다.

[연결]
이 장은 본문의 B · 의미와 공간의 정렬 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S64 발표 노트]
[설명 순서]
“다른 모델의 순위가 아니라 같은 SALM의 학습 목표 한 가지를 비교합니다. 검색 점수는 높아지고 위치 오차는 낮아졌지만, 이는 같은 원문 조건에서 관측한 변화입니다.”

[경계·원문의 추가 자료]
두 검색 방향을 정의하고 지표의 좋은 방향을 표시한다. 실측 SRIR·표현 편집·다른 모델 순위는 원문의 추가 자료이며, 자연어 복합 추론의 증거로 확대하지 않는다.


T2A는 텍스트→오디오, A2T는 오디오→텍스트 검색이다. R@1은 정답이 최상위 후보에 있는 비율. LCL은 원래 caption과 semantic embedding의 대조 목표다. LsCL은 공간 caption을 사용한 대조 목표, LDOA는 지도 방향 목표다. 위치 오차는 지도 DOA loss로 학습한 MLP의 오차로, ELSA의 zero-shot prompt 방향 분류와 다른 프로토콜이다. 두 행은 SALM-s 같은 다른 모델을 섞지 않았다.
[Sources]
- https://arxiv.org/html/2507.16724v2

[시각화 전 표의 수치·조건 보존]
동일 SALM · 합성 FOA sClotho 평가SALM의 학습 목표 | T2A R@1 (%) ↑ | A2T R@1 (%) ↑ | 위치 오차 (°) ↓ | 
$L_{\mathrm{sCL}}+L_{\mathrm{DOA}}$ | 9.1 | 9.6 | 1.8 | 
위 조건 + $L_{\mathrm{CL}}$ | 10.5 | 10.4 | 1.6 |
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "근거 부록 B · 의미와 공간의 정렬"
causalStage: "appendix"
originSlide: 26
---

# 의미 특징은 공간 경로의 어느 깊이에서 합칠까?

::body::
<PaperFigure src="/diagrams/p1-fusion-depth.svg" alt="같은 공간 처리 경로에서 태깅 의미 특징을 낮은 수준과 높은 수준에 연결하는 두 대안" caption="일반 오디오 태깅 사전학습 특징의 결합 위치 비교" />

::takeaway::
AT2SELD는 **의미·공간 특징의 결합 위치**를 비교한다.

::source::
AT2SELD, arXiv:2606.27751v1, Fig. 25 기반 결합 위치 재구성.

<!--
[현재 S65 · 근거 부록]
근거 부록 B · 의미와 공간의 정렬

[설명의 중심]
AT2SELD는 고정 클래스 SELD에서 semantic–spatial 결합 위치를 시험한다.

[연결]
이 장은 본문의 B · 의미와 공간의 정렬 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S65 발표 노트]
[설명 순서]
“앞의 SELD는 소리 종류와 위치를 함께 출력했습니다. 이 연구는 일반 오디오 태깅에서 얻은 의미 정보를 그 예측 과정의 어디에 연결하는 것이 유용한지 묻습니다.”

[경계·원문의 추가 자료]
의미 분류기가 정확하면 음원과 방향의 대응도 자동으로 해결된다고 주장하지 않는다. 고정 클래스 SELD 적응을 자유 어휘 질의응답과 구별한다.


이 연구 보고서에서 쓰는 AT2SELD 명칭을 따른다. 공간 경로의 초반에 결합할지 후반에 결합할지가 이번 설계 질문이다. 의미 분류가 가능하다고 사건-방향 대응이 자동으로 보장되지 않는다. 자유 어휘나 자유형 QA 모델이 아니다.
[Sources]
- https://arxiv.org/html/2606.27751v1

[시각화 전 본문 설명]
공간 경로
FOA 입력 → 공간 단서 처리 → SELD 출력
early 결합
낮은 수준의 특징에서 의미 경로 연결
late 결합
높은 수준의 특징에서 의미 경로 연결
의미 경로의 출발점
일반 오디오 태깅 사전학습
최종 출력
고정 클래스 사건·활성·위치

[설명 그림의 범위]
발표자 제작 SVG. 개념의 관계를 읽기 위한 도식이며 원문의 실험 관측이나 모델 추정값을 그린 결과가 아니다.
-->

---
layout: "seminar"
variant: "result"
chapter: "근거 부록 B · 의미와 공간의 정렬"
causalStage: "appendix"
originSlide: 27
---

# 결합 위치의 효과도 학습 조건에 달려 있다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">STARSS23 · Stage 3의 강한 dropout을 공유</p>
<PaperFigure src="/diagrams/result-27.svg" alt="Test SELD ↓ 원문 수치 비교 그래프. no-stitch · cs00: 0.708; late-only · cs01: 0.624" />
<p class="seminar-chart-note">최적 validation 체크포인트로 test · 무결합 기준도 Stage 2보다 저하된 조건</p>
</div>

::takeaway::
이 Stage 3 조건에서 **late-only의 SELD 점수가 낮았다.**

::source::
AT2SELD, arXiv:2606.27751v1, Table 11–12. 원문 수치의 그래프 재구성.

<!--
[현재 S66 · 근거 부록]
근거 부록 B · 의미와 공간의 정렬

[설명의 중심]
AT2SELD late 결합의 이득은 강한 dropout이라는 같은 조건 안의 결과다.

[연결]
이 장은 본문의 B · 의미와 공간의 정렬 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S66 발표 노트]
[설명 순서]
“이 차이는 원문의 특정 학습 단계와 dropout 조건에서 읽어야 합니다. 그 안에서 late-only 결합이 점수를 낮췄다고 말할 수 있지만, 의미 결합이 모든 학습 조건에서 우월하다는 결론은 아닙니다.”

[경계·원문의 추가 자료]
전체 설정 탐색과 다른 학습 단계는 원문의 추가 자료이다. 다른 조건의 최상위 행을 이번 기준선과 짝짓거나 범용 표현의 성과로 확대하지 않는다.


FOA 공간 경로와 pretrained audio-tagging 의미 경로를 사용한다. 이 표는 frozen probe가 아니다. Stage3 no-stitch는 unregularized Stage2보다 악화됐으므로, 강한 정규화 안에서의 성능 회복을 모든 공간 전용 모델에 대한 우위로 확대하지 않는다. early-only와 early+late는 원문의 추가 자료의 별도 비교다.
[Sources]
- https://arxiv.org/html/2606.27751v1

[시각화 전 표의 수치·조건 보존]
STARSS23 · Stage 3의 강한 dropout을 공유결합 설정 | Test SELD ↓ | 
no-stitch · cs00 | 0.708 | 
late-only · cs01 | 0.624 | 

[조건]
학습·선택지도 SELD 적응 / 최적 validation 체크포인트로 test

비교의 범위무결합 기준 자체가 Stage 2보다 저하된 조건
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->

---
layout: "seminar"
variant: "result"
chapter: "근거 부록 B · 의미와 공간의 정렬"
causalStage: "appendix"
originSlide: 33
---

# 언어 정렬도 실제 녹음에서 따로 검사한다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">동일 ELSA · 문장 template와 audio embedding의 cosine similarity</p>
<PaperFigure src="/diagrams/result-33.svg" alt="4방향 정확도 (%) ↑ 원문 수치 비교 그래프. S-Clotho · 합성: 92.0; S-AC · 합성: 92.8; S-RWD · 실녹음: 35.8" />
<p class="seminar-chart-note">S-RWD: 실제 5개 방, 70개 샘플</p>
</div>

::takeaway::
이 작은 실녹음 평가에서 **합성보다 방향 분류 정확도가 낮았다.**

::source::
ELSA, NeurIPS 2024, Table 2. arXiv v1과 출판본 수치 일치 확인.

<!--
[현재 S67 · 근거 부록]
근거 부록 B · 의미와 공간의 정렬

[설명의 중심]
ELSA의 공간 문장 정렬은 합성→실녹음 전이 격차가 남는다.

[연결]
이 장은 본문의 B · 의미와 공간의 정렬 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S67 발표 노트]
[설명 순서]
“ELSA는 공간 정보를 담은 오디오와 텍스트를 함께 정렬합니다. 같은 방향 후보를 사용해도 합성과 실제 녹음에서 정확도가 달라지므로, 이 차이를 포함해 재사용 범위를 읽겠습니다.”

[경계·원문의 추가 자료]
Table 2에 없는 기준선을 만들지 않는다. CLAP의 Appendix A Table 7은 입력 조건을 표시해 원문의 추가 자료에 두며, 합성·실제 차이를 단일 원인의 효과로 단정하지 않는다.


방향 후보 네 클래스를 cosine similarity로 비교한 동일 모델의 prompt 분류다. 연속 각도 회귀나 자유형 QA 점수가 아니다. ELSA는 전체 구성요소를 갱신하며 spatial branch는 지도 공간 사전학습으로 초기화한다. 원문 Table2에는 baseline이 없다. NeurIPS 출판본 PDF p7 Table2에서92.0%,92.8%,35.8%를 대조해 확인했다. 작은 S-RWD와 합성의 차이를 하나의 원인으로 설명하지 않는다.
[Sources]
- https://papers.neurips.cc/paper_files/paper/2024/file/3acc054949b6948d4444b35d412cab56-Paper-Conference.pdf

[시각화 전 표의 수치·조건 보존]
동일 ELSA · 문장 template와 audio embedding의 cosine similarity평가 데이터 | 관측 조건 | 4방향 정확도 (%) ↑ | 
S-Clotho | 합성 | 92.0 | 
S-AC | 합성 | 92.8 | 
S-RWD | 실녹음 | 35.8 | 

[조건]
학습 방식공간화한 오디오·문장의 대조 정렬

실녹음 크기S-RWD: 5개 방, 70개 샘플
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->

---
layout: "seminar"
variant: "method"
chapter: "근거 부록 B · 의미와 공간의 정렬"
causalStage: "appendix"
originSlide: 36
---

# 문장으로 고른 음원의 위치만 읽을 수 있나?

::body::
<PaperFigure src="/research/p1-selecttsl-problem.png" alt="SelectTSL Fig. 1 모든 음원 위치와 prompt로 지정한 speech 위치를 찾는 과제 비교" />

::aside::
<section><span class="seminar-label semantic-input">목표를 지정하는 입력</span><p>텍스트 및/또는 1초 예시 오디오</p></section>
<section><span class="seminar-label semantic-result">찾아야 할 출력</span><p>프레임별 목표 수 0 / 1 / 2와 DOA</p></section>

::takeaway::
SelectTSL의 출력은 **지정한 목표의 활성 수와 방향**이다.

::source::
SelectTSL, arXiv:2607.02343v1, Fig. 1. CC BY 4.0.

<!--
[현재 S68 · 근거 부록]
근거 부록 B · 의미와 공간의 정렬

[설명의 중심]
SelectTSL은 생성 LLM 없이 prompt 조건으로 목표 음원을 골라 위치를 읽는다.

[연결]
이 장은 본문의 B · 의미와 공간의 정렬 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S68 발표 노트]
[설명 순서]
“앞의 정렬에서는 오디오와 문장의 대응을 평가했지만, 여기서는 요청한 소리의 위치를 직접 출력합니다. 목표가 없거나 여러 개일 수도 있으므로, 선택과 활성 수 판단도 과제의 일부가 됩니다.”

[경계·원문의 추가 자료]
파형을 분리해 생성하는 과제로 소개하지 않는다. full model의 텍스트·예시 오디오 조건을 텍스트만 쓰는 시스템으로 축약하지 않는다.


다음 결과에서 Full은 text+audio cue를 함께 받는다. 원문 문제 그림의 prompt는 speech이며 앞서 사용한 알람 사고실험과 별개다. 내부 extraction 모듈의 selection 학습은 설명하되 출력 파형의 생성 성능이 본문의 주제는 아니다. 원문 MOTA*에는 ID-switch 벌점이 없어 음원 정체성 추적의 근거로 삼지 않는다.
[Sources]
- https://arxiv.org/html/2607.02343v1
-->

---
layout: "seminar"
variant: "result"
chapter: "근거 부록 B · 의미와 공간의 정렬"
causalStage: "appendix"
originSlide: 37
---

# 목표 선택 뒤에도 IPD 경로의 기여가 남았다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">text + 1초 audio cue 유지 · 같은 목표 입력 조건</p>
<PaperFigure src="/diagrams/result-37.svg" alt="MAE (°) ↓, F1 ↑ 원문 수치 비교 그래프. Full: 0.98, 0.96; IPD Enhancer 제거 · A1: 2.10, 0.83" />
<p class="seminar-chart-note">MAE는 true positive만 계산 · F1과 함께 해석</p>
</div>

::takeaway::
목표 입력을 유지한 비교에서 **위상 정보 강화 경로의 기여**가 나타났다.

::source::
SelectTSL, arXiv:2607.02343v1, Table VI. F1은 0–1 척도. 원문 수치의 그래프 재구성.

<!--
[현재 S69 · 근거 부록]
근거 부록 B · 의미와 공간의 정렬

[설명의 중심]
SelectTSL의 IPD enhancer 제거 결과는 prompt와 물리 단서의 역할을 구별한다.

[연결]
이 장은 본문의 B · 의미와 공간의 정렬 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S69 발표 노트]
[설명 순서]
“같은 목표 입력을 둔 채 IPD Enhancer를 제거한 조건을 비교하겠습니다. 오차와 F1의 변화는 해당 경로의 기여를 보여주지만, 다른 입력 단서의 도움까지 없앴다는 뜻은 아닙니다.”

[경계·원문의 추가 자료]
A4 직접 입력과 OSPAT는 원문의 추가 자료이다. MAE는 true positive 조건이며, Table III의 MOTA*·Recall 불일치와 실측 RIR 정적 합성이라는 범위를 유지한다.


주 실험은 5초 clip, SNR−5~5dB, 방위각[0,180), 프레임별 목표 수0/1/2 조건이다. Selection, DOA, cardinality를 함께 학습한다. MAE는 검출된 true positive 오차로 미검출을 직접 벌하지 않는다. TableVI Full/A1의 F1은0.96/0.83이며 퍼센트로 옮기지 않았다. A4, OSPA-T는 별도 원문의 추가 자료이다. TableIII의 일부 P/R·MOTA* 불일치가 있어 이를 새로운 정량 근거로 사용하지 않는다. TAU-SRIR는 측정 RIR 합성이므로 현장 이동 혼합 녹음으로 설명하지 않는다.
[Sources]
- https://arxiv.org/html/2607.02343v1

[시각화 전 표의 수치·조건 보존]
text + 1초 audio cue 유지 · 같은 목표 입력 조건SelectTSL 설정 | MAE (°) ↓ | F1 ↑ | 
Full | 0.98 | 0.96 | 
IPD Enhancer 제거 · A1 | 2.10 | 0.83 | 

[조건]
합성 주 실험4×4×2 m 방 · $T_{60}=0.2\,\mathrm{s}$ / 마이크 간격 20 cm

오차의 분모MAE는 true positive만 계산 / F1을 함께 읽어야 한다.
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->

---
layout: "seminar"
variant: "focus"
chapter: "근거 부록 B · 의미와 공간의 정렬"
causalStage: "appendix"
originSlide: 65
---

# 시간과 위치를 바꾼 문장은 다른 정답이다

::body::
<PaperFigure src="/diagrams/p2-s65-event-negatives.png" alt="시간의 먼저와 나중, 공간의 왼쪽과 오른쪽 격자에서 기준 사건열, 순서 반전, 위치 교환을 비교한다." caption="사건 배치 재구성 · 화살표는 시간" />

::takeaway::
같은 두 소리도 **발생 순서·각 사건의 방향**이 달라지면 설명문과의 대응이 바뀐다.

::source::
CoSTALA, arXiv:2608.24374v1, §2.1 기반 설명용 재구성 C65. 겹치지 않는 두 FOA 사건·8방향.

<!--
[현재 S70 · 근거 부록]
근거 부록 B · 의미와 공간의 정렬

[설명의 중심]
CoSTALA는 시간 순서·위치 결속을 hard negative로 정렬한다.

[연결]
이 장은 본문의 B · 의미와 공간의 정렬 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S70]
[Sources]
- https://arxiv.org/html/2608.24374v1
[시각 자료]
직접 제작한 강의용 벡터 도식을 삽입했다. 원문 결과·예측을 재현한 그림이 아니며 기존 해석 범위와 평가 조건을 유지한다. SVG 원본과 2배 해상도 PNG는 public/diagrams에 보관한다.
[발표 노트]
설명문과 잘 맞는 오디오를 검색하는 문제로 읽는다. 기준 사건열은 알람이 왼쪽에서 먼저 울리고 말소리가 오른쪽에서 나중에 난다. Temporal negative는 소리와 위치는 그대로 두고 순서를 뒤집는다. Spatial negative는 사건 순서를 유지하며 각 소리의 위치를 바꾼다. 화살표는 발생 순서를 뜻하며 한 음원의 이동 경로를 나타내지 않는다.
[해석 범위]
CoSTALA의 범위는 겹치지 않는 두 합성 FOA 사건과 8방향이다. 화면은 §2.1의 negative 구성을 설명하는 예다. 자유형 QA, 연속 음원 추적, 겹친 음원 분리의 성공 사례가 아니다. Fig. 1과 Fig. 2는 contrastive·local·consistency 학습의 방법 그림이며 실제 검색 결과와 구분한다.
-->

---
layout: "seminar"
variant: "result"
chapter: "근거 부록 B · 의미와 공간의 정렬"
causalStage: "appendix"
originSlide: 66
---

# 순서·위치 정렬은 검색으로도 시험할 수 있다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">두 합성 FOA 사건 · Global Text-to-Audio 검색 · <MathInline tex="E_{\mathrm{global}}\leftrightarrow T_{\mathrm{st}}" />의 cosine similarity</p>
<PaperFigure src="/diagrams/result-66.svg" alt="Global T2A R@1 (%) ↑ 원문 수치 비교 그래프. 대조 학습만 · $L_{\mathrm{cl}}$: 5.84; 전체 · $L_{\mathrm{cl}}+L_{\mathrm{st}}+L_{\mathrm{local}}+L_{\mathrm{consist}}$: 8.10" />
</div>

::takeaway::
전체 loss는 **이 사건열 검색을 개선**했으며, 연속 이동 추적은 별도 검증이 필요하다.

::source::
CoSTALA, arXiv:2608.24374v1, Table 2·§3.1. R@1: 정답을 첫 후보로 검색한 비율.

<!--
[현재 S71 · 근거 부록]
근거 부록 B · 의미와 공간의 정렬

[설명의 중심]
CoSTALA retrieval은 생성형 LLM의 LoRA/QA 성과가 아니다.

[연결]
이 장은 본문의 B · 의미와 공간의 정렬 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S71]
[Sources]
- https://arxiv.org/html/2608.24374v1
[발표 노트]
Table 2의 contrastive-only와 전체 loss 두 행에서 Global Text-to-Audio R@1만 선택한다. 사건별 local alignment와 consistency 등을 포함한 전체 조건에서 5.84에서 8.10%로 높아진다. §3.1은 E_global과 T_st의 cosine similarity로 검색한다고 명시한다. Fig. 2의 최종 E_st를 직접 평가한 표라고 설명하지 않는다.
[해석 범위]
여러 loss를 함께 바꿨으므로 단일 loss의 독립 인과효과는 분리되지 않는다. Soft slicing은 원 segment duration을 사용하며 자동 사건 경계 추정의 성공은 확인하지 않았다. 의미 전용 열을 모든 의미 지표의 보존으로 확대하지 않는다. 새로운 음원·방 분할 일반화와 연속 이동 추적, 겹친 음원 분리, 자유형 QA는 별도 검증이 필요하다.
[이해 확인과 전환]
“사건 순서를 잘 검색하면 움직이는 음원도 잘 추적할까요?”에 대해 평가 대상이 달라 별도 검증이 필요하다고 답을 회수한다.

[시각화 전 표의 수치·조건 보존]
두 합성 FOA 사건 · Global Text-to-Audio 검색 · $E_{\mathrm{global}}\leftrightarrow T_{\mathrm{st}}$의 cosine similarity

CoSTALA 학습 loss | Global T2A R@1 (%) / 높을수록 좋음 | 

대조 학습만 · $L_{\mathrm{cl}}$ | 5.84 | 

전체 · $L_{\mathrm{cl}}+L_{\mathrm{st}}+L_{\mathrm{local}}+L_{\mathrm{consist}}$ | 8.10 |
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->

---
layout: "seminar"
variant: "focus"
chapter: "근거 부록 C · 공간 Audio-LM의 세부 설계"
causalStage: "appendix"
originSlide: 40
---

# 인코더가 같은 관측에서 과제별 특징을 고르게 한다

::body::
<PaperFigure src="/diagrams/p2-s40-feature-selection.png" alt="바이노럴 파형의 여러 특징을 과제별로 가중하고 공유 파라미터의 세 경로로 사건, 방향, 거리를 읽는 구조." caption="설계 재구성 · 가중 막대는 설명용" />

::takeaway::
DSpAST는 **과제별 특징 선택**을 위해 사건·방향·거리의 정보 경로를 나눈다.

::source::
DSpAST, arXiv:2509.13927v1, §3.2·Fig. 1 기반 설명용 재구성 C40.

<!--
[현재 S72 · 근거 부록]
근거 부록 C · 공간 Audio-LM의 세부 설계

[설명의 중심]
DSpAST는 audio feature를 어떻게 선택할지 encoder 단계의 설계다.

[연결]
이 장은 본문의 C · 공간 Audio-LM의 세부 설계 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S72]
[Sources]
- https://arxiv.org/html/2509.13927v1
[시각 자료]
직접 제작한 강의용 벡터 도식을 삽입했다. 원문 결과·예측을 재현한 그림이 아니며 기존 해석 범위와 평가 조건을 유지한다. SVG 원본과 2배 해상도 PNG는 public/diagrams에 보관한다.
[발표 노트]
하나의 바이노럴 관측에 세 종류의 질문을 붙인다. 사건 이름을 구분하는 정보와 방향·거리를 구분하는 정보가 동일한 중요도를 가져야 할 이유는 없다. DSpAST는 여러 입력 특징의 가중과 과제별 분기를 통해 이 차이를 설계에 반영한다. 그림의 공유 backbone은 Transformer와 patch embedding이 파라미터를 공유한다는 뜻이다. 독립된 대형 인코더 세 개로 설명하지 않는다.
[해석 범위]
화면은 §3.2의 설계 의도를 재구성한 개념도다. Fig. 1은 방법 그림이며 Fig. 2의 평균 attention도 단서 사용의 인과 검증은 아니다. 실제 개선에는 추가 특징, 사전학습 curriculum, AdaCos loss 변경이 함께 포함된다.
-->

---
layout: "seminar"
variant: "method"
chapter: "근거 부록 C · 공간 Audio-LM의 세부 설계"
causalStage: "appendix"
originSlide: 43
---

# 기하 지도는 인코더에 배우고, QA에서는 오디오만 읽는다

::body::
<PaperFigure src="/research/p2-owl-v1-fig4.png" alt="OWL Fig. 4 원문 구조. 왼쪽 SAGE의 깊이와 RIR 보조 학습, 오른쪽 바이노럴 오디오를 받는 OWL 추론" caption="왼쪽: depth·RIR로 SAGE 학습. 오른쪽: 고정 음향 인코더 → projector → LLM." />

::takeaway::
**기하 지도는 인코더 학습에**, projector·LoRA는 그 표현을 사용하는 QA 학습에 쓴다.

::source::
OWL, arXiv:2509.26140v1, Fig. 4. 원문 구조도.

<!--
[현재 S73 · 근거 부록]
근거 부록 C · 공간 Audio-LM의 세부 설계

[설명의 중심]
OWL은 SAGE 표현 학습과 frozen encoder→projector→LLM LoRA QA 학습을 분리한다.

[연결]
이 장은 본문의 C · 공간 Audio-LM의 세부 설계 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S73]
[Sources]
- https://arxiv.org/html/2509.26140v1
[발표 노트]
원문 왼쪽 SAGE와 오른쪽 OWL을 구분한다. SAGE에서는 깊이와 음향 표현으로 RIR을 복원하는 보조 학습이 음향 표현에 영향을 준다. OWL의 추론 경로에는 바이노럴 음향 인코더가 만든 표현이 남고, 이를 projector로 언어 모델에 연결한다. OWL QA 학습에서는 SAGE 음향 인코더를 고정하고 projector와 LLM LoRA를 학습한다.
[해석 범위]
학습 그림의 depth와 RIR을 추론 입력 목록에 넣지 않는다. 구조도는 어떤 경로를 설계했는지 보여 주며 그 자체가 기하 이해 성공의 근거는 아니다. Q-Former 상세와 CoT curriculum의 효과는 본문의 loss 비교와 구분한다.
-->

---
layout: "seminar"
variant: "focus"
chapter: "근거 부록 C · 공간 Audio-LM의 세부 설계"
causalStage: "appendix"
originSlide: 45
---

# 좌우 음량만 주는 입력으로 무엇을 시험하나?

::body::
<PaperFigure src="/diagrams/p2-s45-gain-waveforms.png" alt="동일한 파형에서 좌우 gain만 바꾼 Left, Center, Right의 세 예. 파형의 시간 구조는 유지되고 진폭만 변한다.">
  <template #caption><MathInline tex="L=g_L\,x" /> · <MathInline tex="R=g_R\,x" /> · 같은 모노 원음, gain만 변경 · 두 BEATs 경로 고정</template>
</PaperFigure>

::takeaway::
Dual-BEATs는 **제한된 좌우 레벨 차이**를 읽는 stereo 분류를 다룬다.

::source::
Dual-BEATs, arXiv:2607.08800v1, §3.2·Appendix A.3 기반 설명용 재구성 C45.

<!--
[현재 S74 · 근거 부록]
근거 부록 C · 공간 Audio-LM의 세부 설계

[설명의 중심]
Dual-BEATs의 amplitude panning은 실제 배열의 위상·기하 입력과 다른 제한된 관측이다.

[연결]
이 장은 본문의 C · 공간 Audio-LM의 세부 설계 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S74]
[Sources]
- https://arxiv.org/html/2607.08800v1
[시각 자료]
직접 제작한 강의용 벡터 도식을 삽입했다. 원문 결과·예측을 재현한 그림이 아니며 기존 해석 범위와 평가 조건을 유지한다. SVG 원본과 2배 해상도 PNG는 public/diagrams에 보관한다.
Csound FLOSS Manual의 Panning and Spatialization 장에서 같은 신호를 채널별 이득으로 나누는 설명 방식을 참고했다: https://www.csound-tutorial.net/floss_manual/Release04/Cs_FM_04_ScrapBook/b-panning-and-spatialization.html . 그림의 진폭 비는 설명용이며 논문의 gain 범위나 pan law를 수치로 재현하지 않았다.
[발표 노트]
이번에는 방이나 실제 마이크 배열을 추정하는 문제를 잠시 내려놓고 입력 생성 조건을 제한한다. 하나의 모노 원음에 좌우 gain을 적용한다. 소리 내용은 같지만 채널 크기가 달라지고, 모델은 Left/Center/Right를 분류한다. 고정된 두 BEATs 경로가 각각 좌우 채널을 읽으며 projector와 언어 adaptation은 학습한다. 화면은 입력을 만드는 방법의 설명이고 실제 공간 신호나 모델 출력 그래프가 아니다.
[해석 범위]
amplitude panning을 HRTF가 반영된 물리적 방향 변화, 위상 활용, 방 잔향 또는 새로운 배열 전이와 동일시하지 않는다. 정규화가 어떤 단서를 지웠는지의 기전은 결과표 하나로 입증되지 않는다.
-->

---
layout: "seminar"
variant: "result"
chapter: "근거 부록 C · 공간 Audio-LM의 세부 설계"
causalStage: "appendix"
originSlide: 46
---

# 전처리가 단서를 바꾸면 점수도 달라진다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">OLMo-3-7B + Dual-BEATs · Direction-First · 방향 정확도 (%) ↑</p>
<PaperFigure src="/diagrams/result-46.svg" alt="PA = 0.00, PA = 0.50 원문 수치 비교 그래프. Dither Off: 99.5, 37.9; Dither On · DA = 0.05: 99.0, 97.1" />
</div>

::takeaway::
PA = 0.50에서는 크게 개선됐고, **PA = 0.00에서는 소폭 낮아졌다.**

::source::
Dual-BEATs, arXiv:2607.08800v1, Table 1. ↑ 높을수록 좋음. On: 채널별 독립 dither.

<!--
[현재 S75 · 근거 부록]
근거 부록 C · 공간 Audio-LM의 세부 설계

[설명의 중심]
Dual-BEATs의 dither 효과는 panning 조건에 의존한다.

[연결]
이 장은 본문의 C · 공간 Audio-LM의 세부 설계 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S75]
[Sources]
- https://arxiv.org/html/2607.08800v1
[발표 노트]
같은 backbone과 출력 순서를 고정하고 각 PA 안에서 dither Off와 On을 읽는다. PA=0.50은 약한 채널의 gain이 0.5인 조건이며 Center를 뜻하지 않는다. 독립 dither의 진폭 DA는 0.05다. 이 조건의 방향 정확도는 37.9에서 97.1%로 높아진다. 반면 PA=0.00에서는 99.5에서 99.0%로 소폭 낮아진다. 따라서 모든 PA에서 일률적 이득이라고 말하지 않는다.
[해석 범위]
표의 97.1을 사용하며 초록의 97.2와 혼합하지 않는다. 학습·평가 random seed는 분리되지만 미관측 panning의 일반화가 새 HRTF·배열·잔향 전이는 아니다. semantic F1 저하 역시 공간 성과에 묻어 없애지 않는다. Table 1과 Fig. 2의 학습·평가 PA 조건은 구분해야 한다.

[시각화 전 표의 수치·조건 보존]
OLMo-3-7B + Dual-BEATs · Direction-First · 방향 정확도 (%) ↑

평가 PA | Dither Off | Dither On / DA = 0.05 | 

0.00 | 99.5 | 99.0 | 

0.50 | 37.9 | 97.1 |
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "근거 부록 C · 공간 Audio-LM의 세부 설계"
causalStage: "appendix"
originSlide: 42
---

# 방 기하 지도는 학습 때만 사용할 수 있다

::body::
<PaperFigure src="/research/p2-owl-v1-fig2.png" alt="BiDepth 원문 Fig. 2. 청취자 관점 깊이 영상과 같은 장면의 바이노럴 음향 시뮬레이션" caption="왼쪽: 깊이 지도. 오른쪽: 청취자·음원 배치와 바이노럴 합성 장면." />

::aside::
<section><span class="seminar-label semantic-geometry">학습할 때</span><p>깊이와 RIR 정답으로<br/>기하적 제약을 제공</p></section><section><span class="seminar-label semantic-input">추론할 때</span><p>바이노럴 오디오와<br/>언어 질문을 제공</p></section>

::takeaway::
**깊이·RIR은 학습 지도**, 질문에 답할 때의 관측은 바이노럴 오디오다.

::source::
OWL, arXiv:2509.26140v1, Fig. 2. 원문 그림.

<!--
[현재 S76 · 근거 부록]
근거 부록 C · 공간 Audio-LM의 세부 설계

[설명의 중심]
OWL의 depth/RIR은 표현 학습용이고 QA 추론의 추가 시각 입력이 아니다.

[연결]
이 장은 본문의 C · 공간 Audio-LM의 세부 설계 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S76]
[Sources]
- https://arxiv.org/html/2509.26140v1
[발표 노트]
소리는 음원뿐 아니라 방과 전파 경로에 의해 달라진다. BiDepth는 같은 청취 위치에서 기하와 음향을 연결하는 합성 데이터다. 왼쪽의 depth는 청취자 관점의 공간 기하를, 오른쪽은 청취자와 음원 배치에 따른 바이노럴 관측을 나타낸다. SAGE는 이런 학습 장면의 depth와 RIR 정보를 보조 지도에 사용한다.
[해석 범위]
깊이 영상을 추론 시에도 제공하는 시청각 QA로 소개하지 않는다. 합성 장면의 기하 지도를 이용한 학습과 실제 방에서의 일반화는 별개다. 저자가 기술한 room/source 분할이 곧 현실 환경 전반의 일반화 보장은 아니다.
-->

---
layout: "seminar"
variant: "focus"
chapter: "근거 부록 C · 공간 Audio-LM의 세부 설계"
causalStage: "appendix"
originSlide: 50
---

# 사건 이름과 속성을 같은 음원에 묶는다

::body::
<PaperFigure src="/diagrams/p2-s50-scene-attributes.png" alt="방 안의 알람과 말소리에서 청취자로 이어지는 방향과 거리, 음원별 발생 구간, 방과 배경 속성의 연결." caption="출력 형식 재구성 · 실제 생성 응답 아님" />

::takeaway::
각 소리의 내용·시간·공간 속성이 **같은 음원에 붙어 있어야** 설명이 일관된다.

::source::
Sci-Phi, arXiv:2510.05542v1, §3.3 출력 형식 기반 설명용 재구성 C50.

<!--
[현재 S77 · 근거 부록]
근거 부록 C · 공간 Audio-LM의 세부 설계

[설명의 중심]
Sci-Phi는 종류·방향·거리를 같은 source record에 묶는 요구를 다룬다.

[연결]
이 장은 본문의 C · 공간 Audio-LM의 세부 설계 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S77]
[Sources]
- https://arxiv.org/html/2510.05542v1
[시각 자료]
직접 제작한 강의용 벡터 도식을 삽입했다. 원문 결과·예측을 재현한 그림이 아니며 기존 해석 범위와 평가 조건을 유지한다. SVG 원본과 2배 해상도 PNG는 public/diagrams에 보관한다.
[발표 노트]
Sci-Phi는 질문 하나의 짧은 답 대신 장면 전체의 속성을 한 번에 생성한다. 방향성 음원마다 설명, 발생 구간, 방향, 거리, 음압, 명료도를 연결하고 비방향성 배경과 방 특성은 장면 단위로 기술한다. 화면의 항목은 출력 형식을 설명하며 모델이 실제로 생성한 응답은 아니다. 데이터의 방향성 음원 수는 최대 네 개다.
[해석 범위]
방과 배경 속성은 모델이 추정하는 값이다. 이를 직접 관측된 사실처럼 읽거나 모든 자유형 장면에 검증된 출력으로 확대하지 않는다. 각 필드를 따로 맞히는 것과 같은 음원에 올바로 대응시키는 것은 다르다. 예를 들어 알람의 왼쪽 위치를 말소리에 붙이면 소리 목록과 방향 목록은 맞아도 장면 기술이 틀리다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "근거 부록 C · 공간 Audio-LM의 세부 설계"
causalStage: "appendix"
originSlide: 52
---

# 속성이 맞아도 음원을 잘못 연결하면 틀린 답이다

::body::
<PaperFigure src="/research/p2-sciphi-v1-tuplescore.png" alt="Sci-Phi Fig. 2 TupleScore 원본 패널. SELDNet+Phi-4 MC FT와 Sci-Phi의 합성 RIR 및 실측 RIR 조건, diamond는 1–4음원 평균" caption="원본 점·축 보존. 오른쪽 두 모델의 ◆·◇(1–4음원 평균)를 비교한다." />

::aside::
<section><span class="seminar-label ">TupleScore · 0–1, 높을수록 좋음</span><p>What × Where × When의<br/>기하평균</p></section><section><span class="seminar-label semantic-geometry">RIR 조건을 분리</span><p>◆ 합성 RIR<br/>◇ 실측 RIR로 합성</p></section><section><span class="seminar-label ">이번에 읽는 비교</span><p>SELDNet+Phi-4 (MC, FT)<br/>↔ Sci-Phi</p></section>

::takeaway::
같은 RIR 조건에서 **Sci-Phi의 평균 TupleScore가 미세조정 기준선보다 높다.**

::source::
Sci-Phi, arXiv:2510.05542v1, Fig. 2 TupleScore 패널 크롭·§4. 정밀값을 추정해 재작성하지 않음.

<!--
[현재 S78 · 근거 부록]
근거 부록 C · 공간 Audio-LM의 세부 설계

[설명의 중심]
Sci-Phi TupleScore는 What×Where×When의 결속을 보며 단순히 속성 정답 수만 세지 않는다.

[연결]
이 장은 본문의 C · 공간 Audio-LM의 세부 설계 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S78]
[Sources]
- https://arxiv.org/html/2510.05542v1
[발표 노트]
먼저 이름과 방향을 바꿔 붙인 예를 떠올린다. 알람은 왼쪽이고 말소리는 오른쪽인데 출력이 이 연결을 뒤집었다면 이름 목록과 방향 목록이 각각 맞아도 장면 설명은 틀리다. TupleScore는 What·Where·When의 기하평균으로 음원 단위 공통 대응을 정한다. 원문 패널의 오른쪽 두 모델, SELDNet+Phi-4 (MC, FT)와 Sci-Phi를 선택한다. ◆는 synthetic-RIR, ◇는 real-RIR의 1–4음원 전체 평균이다. 두 조건 모두 Sci-Phi의 평균이 더 높다.
[해석 범위]
원본 축과 점을 보존하기 위해 mono 및 ○·□도 남겼지만 이 장의 비교는 두 모델의 diamond에 한정한다. ○는 한 음원, □는 네 음원이며 평균으로 읽지 않는다. 두 모델 모두 장면 기술에 미세조정했고 baseline은 공간 encoder 고정, Sci-Phi는 적응한다. 실측 RIR은 실제 배경을 더해 합성한 장면이지 현장 혼합음 녹음이 아니다. real-RIR는 수평 방향 위주이며 방 크기와 배경 라벨이 없다. Table 2의 OM/OS는 채점 원칙이고 모델 ablation이 아니다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "근거 부록 C · 공간 Audio-LM의 세부 설계"
causalStage: "appendix"
originSlide: 56
---

# 지각·음원 결속·복합 질의를 나눠 측정한다

::body::
<div style="display:grid;grid-template-columns:480px 1fr;gap:38px;height:100%">
<PaperFigure src="/research/p2-twnm-v3-scene.png" alt="TWNM Fig. 4의 청취자 중심 장면 부분. 음원과 방향의 관계를 나타내는 설명 도해" caption="원문 Fig. 4 장면 크롭 · 모델 입력이나 생성 결과가 아닌 개념 예시" />
<div style="display:flex;flex-direction:column;justify-content:center;gap:23px">
<section><span class="seminar-label">L1 · 지각</span><p>어떤 소리가 들리는가?</p></section>
<section><span class="seminar-label">L2 · 음원과 속성 연결</span><p>어떤 소리가 그 위치에 있는가?</p></section>
<section><span class="seminar-label">L3 · 질문 조건을 적용</span><p>청취자 방향이 바뀌면 답도 바뀌는가?</p></section>
<p class="seminar-figure-note">질문은 평가 정의를 설명하는 재구성이다.</p>
</div></div>

::takeaway::
세 층위는 **무엇을 평가하는지의 구분**이며, 모델이 출력하는 명시적 그래프가 아니다.

::source::
The World is Not Mono, arXiv:2601.02954v3, Fig. 4 장면 부분·§3.

<!--
[현재 S79 · 근거 부록]
근거 부록 C · 공간 Audio-LM의 세부 설계

[설명의 중심]
TWNM의 질문 수준은 LLM 학습 후의 trade-off를 펼쳐 보는 기준이다.

[연결]
이 장은 본문의 C · 공간 Audio-LM의 세부 설계 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S79]
[Sources]
- https://arxiv.org/html/2601.02954v3
[발표 노트]
같은 청취자 기준의 장면에서 필요한 답의 종류를 차례로 바꾼다. L1은 사건 종류나 위치 같은 개별 관측을 읽고, L2는 어떤 속성이 어느 음원에 속하는지 연결한다. L3는 관찰자 회전, 음원 제거, 복합 조건 등의 질문을 적용한다. 화면의 그림은 Fig. 4에서 청취자 중심 장면을 선택한 도해이며 오른쪽은 과제 정의를 설명하는 한국어 질문이다.
[해석 범위]
원문 도해는 네 개의 기호를 보이는 개념 예시지만 실제 모델의 source slots와 주평가 합성 장면은 최대 세 음원이다. 예시 그림과 숨겨진 scene metadata는 모델의 추론 입력이 아니다. 정답 생성에 사용하는 metadata와 audio-only 질문 입력을 구분한다. 그래프 기호는 평가 목표의 정의이며 명시적 scene graph 출력이 아니다. L3 점수를 순수 공간 추론 능력 전체로 해석하지 않는다.
-->

---
layout: "seminar"
variant: "focus"
chapter: "근거 부록 D · 시간 정보의 전달"
causalStage: "appendix"
originSlide: 59
---

# 시간을 줄이기 전에 질문이 요구하는 정보를 정한다

::body::
<PaperFigure src="/diagrams/p2-s59-time-requirements.png" alt="사건의 시간 막대, 한 음원의 연속 위치 곡선, 질문 관련 시간 구간을 나란히 보여 주는 세 시간 관계." caption="설명용 시간축 · 실제 모델 예측 아님" />

::takeaway::
**순서·연속 이동·질의 구간**은 서로 다른 시간 정보의 요구다.

::source::
Motion 2025, arXiv:2509.14666v1, Table 1; Dynamic QA, arXiv:2602.16334v1, Table 2 기반 C59.

<!--
[현재 S80 · 근거 부록]
근거 부록 D · 시간 정보의 전달

[설명의 중심]
사건 순서·연속 궤적·질문 관련 구간을 구분한다.

[연결]
이 장은 본문의 D · 시간 정보의 전달 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S80]
[Sources]
- https://arxiv.org/html/2509.14666v1
- https://arxiv.org/html/2602.16334v1
[시각 자료]
직접 제작한 강의용 벡터 도식을 삽입했다. 원문 결과·예측을 재현한 그림이 아니며 기존 해석 범위와 평가 조건을 유지한다. SVG 원본과 2배 해상도 PNG는 public/diagrams에 보관한다.
[발표 노트]
알람이 말소리보다 먼저 울렸는지는 사건 순서다. 같은 알람의 위치가 왼쪽에서 오른쪽으로 바뀌었는지는 연속 이동이다. 알람이 울린 특정 구간에만 답해야 하는 경우는 질문 관련 시간 선택이다. 이 세 질문은 시간 이해라는 말 안에 함께 들어갈 수 있지만 서로 다른 관측과 평가가 필요하다.
[해석 범위]
화면은 논문의 질문 범주를 설명하기 위한 재구성이지 실제 오디오나 예측 궤적이 아니다. 두 사건이 순서대로 발생했다고 해서 한 음원이 이동한 것은 아니다. 세 축을 발전 단계나 성능 순위로 만들지 않는다. 본문에서 Motion과 Dynamic QA는 움직임·구간 선택, ST-AudioLM은 시간별 공간 상태를 다뤘다. 근거 부록의 CoSTALA는 사건 순서의 검색을 다룬다.
-->

---
layout: "seminar"
variant: "focus"
chapter: "근거 부록 D · 시간 정보의 전달"
causalStage: "appendix"
originSlide: 62
---

# 교차하는 궤적에도 음원 정체성이 남아야 한다

::body::
<PaperFigure src="/diagrams/p2-s62-source-trajectories.png" alt="시간을 따라 교차하는 알람 A와 말소리 B의 좌우 위치 곡선. 나중 시점에서 A는 오른쪽, B는 왼쪽에 있다." caption="좌우 위치–시간 재구성 · 실제 예측 아님" />

::takeaway::
각 순간의 위치를 넘어 **음원 정체성과 시간별 공간 상태**를 함께 유지해야 한다.

::source::
ST-AudioLM, arXiv:2606.14141v1, ST-AudioQA Table 1 기반 설명용 재구성 C62. 실제 예측 아님.

<!--
[현재 S81 · 근거 부록]
근거 부록 D · 시간 정보의 전달

[설명의 중심]
ST-AudioLM이 시간별 source 상태를 전달해야 하는 이유다.

[연결]
이 장은 본문의 D · 시간 정보의 전달 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S81]
[Sources]
- https://arxiv.org/html/2606.14141v1
[시각 자료]
직접 제작한 강의용 벡터 도식을 삽입했다. 원문 결과·예측을 재현한 그림이 아니며 기존 해석 범위와 평가 조건을 유지한다. SVG 원본과 2배 해상도 PNG는 public/diagrams에 보관한다.
[발표 노트]
한 시점의 방향 추정이 맞아도 다음 시점에 음원 정체성이 바뀌면 관계 질문을 틀릴 수 있다. 화면에서 알람 A와 말소리 B는 계속 같은 이름을 유지한다. 질문은 특정 소리가 움직인 뒤의 관계를 요구하므로 음원 정체성, 참조 시점, 시간별 공간 상태를 함께 읽어야 한다. 그림의 방향은 이해를 위한 단순 예이며 실제 모델 궤적이나 생성 결과가 아니다.
[해석 범위]
ST-AudioQA는 통제된 한·두 음원 합성 장면으로 구성한다. 이런 성과를 밀집한 현실 동적 장면이나 연속 대화의 해결로 확대하지 않는다. 정적인 위치 설명과 움직임에 조건을 둔 관계 질문은 서로 다른 출력 요구다.
-->

---
layout: "seminar"
variant: "result"
chapter: "근거 부록 E · 답변의 근거"
causalStage: "appendix"
originSlide: 69
---

# 선택형 점수는 우연 기준부터 확인한다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">세 선택지 MCQA · Gemini 2.5 Pro, 2025년 6월 업데이트 · AA (%) ↑</p>
<PaperFigure src="/diagrams/result-69.svg" alt="Localization, Relation, Trajectory 원문 수치 비교 그래프. 무작위 선택: 33.33, 33.33, 33.33; Gemini 2.5 Pro: 40.87, 48.97, 45.28" />
<p class="seminar-chart-note">AA: 반복 prompt 변형 실행의 평균 정확도</p>
</div>

::takeaway::
보고된 버전은 우연 기준보다 높았으며, <strong>공간 과제마다 점수가 달랐다.</strong>

::source::
STAR-Bench, arXiv:2510.24693v2, Table 2 선택 열. ↑ 높을수록 좋음.

<!--
[현재 S82 · 근거 부록]
근거 부록 E · 답변의 근거

[설명의 중심]
STAR의 random guess는 question-only model과 다른 기준이다.

[연결]
이 장은 본문의 E · 답변의 근거 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S82]
[Sources]
- https://arxiv.org/html/2510.24693v2
[청중 질문]
벤치마크의 낮은 평균은 어떤 종류의 질문에서 나온 것인가?
[발표 노트]
평가 모델의 버전과 질문 형식을 먼저 밝힌다. 우연 기준선을 읽고 과제별 점수를 비교한다. AA는 반복 실행 평균이고 ACR는 매번 맞힌 문항 비율임을 한 문장으로 구별한다.
이 표는 audio/caption ablation 결과표가 아니다. ACR는 모든 반복 실행에서 맞힌 문항의 비율이며 AA와 구별한다. 통계적 유의성, 위상 처리 기전 또는 최신 모든 모델의 능력을 이 숫자만으로 결론내리지 않는다.
[해석 범위]
숫자는 효과의 통계적 유의성이나 phase 사용을 입증하지 않는다. BAT의 0점 등을 기전 붕괴의 증거로 크게 쓰지 않는다. 서로 다른 입력 지원·전처리·응답 형식 적합성이 개입할 수 있다. 전체 19모델 순위표와 ACR는 원문의 추가 자료이다.

[시각화 전 표의 수치·조건 보존]
세 선택지 MCQA · Gemini 2.5 Pro, 2025년 6월 업데이트 · AA (%) ↑평가 조건 | Localization | Relation | Trajectory | 
무작위 선택 | 33.33 | 33.33 | 33.33 | 
Gemini 2.5 Pro | 40.87 | 48.97 | 45.28 | 
AA: 반복 prompt 변형 실행의 평균 정확도
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->

---
layout: "seminar"
variant: "method"
chapter: "근거 부록 E · 답변의 근거"
causalStage: "appendix"
originSlide: 70
---

# 현장에서는 말의 내용과 응답 대상이 갈린다

::body::
<PaperFigure src="/research/wearvox-side-talk-panel.png" alt="착용자의 발화가 기기에게 향한 것인지 다른 사람에게 향한 것인지 구별하는 side-talk 사례" caption="WearVox Fig. 1의 side-talk rejection 문제 패널." />

::aside::
<section><span class="seminar-label">기기에게 한 말</span><p>응답</p></section><section><span class="seminar-label">주변 사람끼리의 말</span><p>비응답</p></section>

::takeaway::
실제 착용자 장면에서는 <strong>발화의 응답 대상</strong>을 구별해야 한다.

::source::
WearVox, arXiv:2601.02391v1, Fig. 1의 side-talk 패널 크롭.

<!--
[현재 S83 · 근거 부록]
근거 부록 E · 답변의 근거

[설명의 중심]
WearVox는 내용 전사만으로 해결되지 않는 기기 응답 대상의 문제를 보여 준다.

[연결]
이 장은 본문의 E · 답변의 근거 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S83]
[Sources]
- https://arxiv.org/html/2601.02391v1
[청중 질문]
인식 가능한 말이 들렸다는 이유만으로 음성 기기가 응답해야 하는가?
[발표 노트]
기기를 향한 발화와 주변 사람끼리의 대화를 대비한다. 내용 인식은 두 경우 모두 가능해도 요구 출력은 응답/비응답으로 다름을 설명한다. 웨어러블 실제 녹음과 앞 합성 공간 QA의 평가 조건 차이를 짚는다.
사용자 발화의 의미와 방향·채널 관측이 어떤 정보를 제공할 수 있는지 문제를 설명한다. 문제 그림 자체를 정확도나 특정 모델의 성공 사례로 해석하지 않는다.
[해석 범위]
WearVox를 앞 공간 LLM들의 실환경 전이 시험이라고 소개하지 않는다. 실제 사용 조건이라는 별도 검증 축이다. 주변 대화의 의도를 음향만으로 언제나 유일하게 알 수 있다고도 하지 않는다.
[시각화 전 상세 본문 — 발표 설명용 보존]
WearVox Fig. 1의 side-talk rejection 문제 패널.


[보조 설명]
내용만으로는 부족한 질문발화를 전사해도
누구에게 한 말인지는 남는다.

요구하는 출력응답할 발화인지
주변 대화인지 판단한다.


[핵심 결론]
실제 착용자 장면에서는 발화의 응답 대상을 구별해야 한다.
-->

---
layout: "seminar"
variant: "figure"
chapter: "근거 부록 E · 답변의 근거"
causalStage: "appendix"
originSlide: 72
---

# 고정 인코더 위에 선형 판독기만 학습한다

::body::
<PaperFigure src="/diagrams/p3-sarl-linear-readout.svg" alt="합성 공간 장면이 고정 오디오 인코더를 지나고 시간 평균 표현에서 사건, 방위, 고도, 거리, 잔향, 부피, 형상을 각각 선형 판독하는 구조" caption="SARL 프로토콜 재구성 · 모델별 입력 형식 · 판독 20 epochs · 무작위 0, 완전 1" />

::takeaway::
<strong>인코더는 고정하고, 공간 요인의 판독기만 학습한다.</strong>

::source::
SARL, arXiv:2606.05544v2, §3·Table 1 기반 프로토콜 재구성.

<!--
[현재 S84 · 근거 부록]
근거 부록 E · 답변의 근거

[설명의 중심]
SARL의 linear accessibility는 인코더를 고정하고 라벨로 판독기를 학습한 증거다.

[연결]
이 장은 본문의 E · 답변의 근거 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S84]
[Sources]
- https://arxiv.org/html/2606.05544v2
[청중 질문]
같은 음원도 위치·방이 달라질 때 인코더에 어떤 정보가 남는가?
[발표 노트]
S18의 고정/학습 범위를 회수한다. 범주 과제의 macro-F1과 연속량을 구간화한 판독 점수를 설명한다. 마지막으로 무작위 기준 0, 완전 성능 1의 정규화가 raw accuracy가 아님을 밝힌다.
범주 과제는 macro-F1, 연속량은 구간화·soft label 후 1−MAE/R을 계산하며 무작위 기준 b에 대해 (x−b)/(1−b)로 정규화한다. raw accuracy가 아니다. source와 room 과제군의 생성 파이프라인도 다르며, 한 요인의 낮은 선형 점수는 pooling 전 정보나 비선형 판독 가능성까지 부정하지 않는다.
[해석 범위]
source와 room 과제군은 생성 파이프라인도 달라 순수 요인 난이도만 비교하는 것이 아니다. 하나의 낮은 점수로 pooling 전 정보나 비선형 판독 가능성까지 부정하지 않는다. 수식과 모델별 입력 목록은 원문의 추가 자료이다.
[시각화 전 상세 본문 — 발표 설명용 보존]
관측단일 음원 10초 합성 오디오 · 모델별 전처리

고정하는 부분오디오 인코더 · 시간 평균 pooling

학습하는 부분요인별 선형 판독기 · 20 epochs


[보조 설명]
읽는 요인사건, 방향, 거리
\mathrm{RT}_{60} , 방 부피, 형상

점수의 기준무작위 = 0
완전 성능 = 1


[핵심 결론]
선형 판독은 특정 pooling 뒤에서 정보가 얼마나 쉽게 읽히는지 시험한다.
-->

---
layout: "seminar"
variant: "result"
chapter: "근거 부록 E · 답변의 근거"
causalStage: "appendix"
originSlide: 76
---

# 단서를 제거하며 남은 반응의 원인을 좁힌다

::body::
<div class="seminar-result-visual">
<p class="seminar-chart-context">GRAM-T · 20개 주파수 × SNR cell 중 유의한 반응 비율 (%)</p>
<PaperFigure src="/diagrams/result-76.svg" alt="유의한 반응 비율 (%) 원문 수치 비교 그래프. 원신호: 100, 0; 고역통과 > 2 kHz: 100, 0; Mel 대역 ILD 제거: 100, 0; 50 Hz 포락선 vocoding: 50, 25" />
<p class="seminar-chart-note">Vocoded 75% = 50% + 25% · 정확도가 아닌 유의 반응 비율</p>
</div>

::takeaway::
파형 변형의 부수 변화까지 고려해 <strong>가능한 설명의 범위</strong>를 좁힌다.

::source::
Interference/BMLD, arXiv:2606.14820v1, Fig. 3의 GRAM-T 원문 값 재작성.

<!--
[현재 S85 · 근거 부록]
근거 부록 E · 답변의 근거

[설명의 중심]
BMLD 단서 제거는 표현의 반응을 설명하며 accuracy를 재는 실험이 아니다.

[연결]
이 장은 본문의 E · 답변의 근거 질문을 보완하는 선택 자료다.

[상세 근거와 해석 범위]
[S85]
[Sources]
- https://arxiv.org/html/2606.14820v1
[청중 질문]
위상 조건 반응이 다른 간섭 단서에도 의존한다면 어디까지 주장할 수 있는가?
[발표 노트]
무엇을 변형했는지 먼저 설명한다. 예를 들어 vocoded 75%는 50% unmasking+25% reversal이며 정확도75%가 아님을 읽는다. 파형 변형의 부수 변화도 있으므로 ‘phase 사용 증명’과 ‘phase가 전혀 없음’ 양쪽 단정을 피한다.
Unmasking은 양의 유의 반응, reversal은 음의 유의 반응이다. 두 비율을 분리해야 total 75%를 성능 정확도로 잘못 읽지 않는다. 원문 그림의 GRAM-T 네 조건과 양·음 방향을 표로 재작성했다. 파형 조작은 하나의 내부 기전을 유일하게 복원하지 않으며, phase 사용의 완전한 증명이나 phase 정보 부재로 단정하지 않는다. 추가 채널별 대조, 같은 parser 조건, 다른 pooling·판독은 후속 통제 제안이며 이 슬라이드가 보고하는 실행 결과가 아니다.
[해석 범위]
후속 제안으로 제시한 채널별 대조·동일 parser·추가 pooling/판독 실험은 미실행이다. 이 결과는 배열 일반화나 모든 질문 응답 모델의 인과 추론을 시험하지 않는다. 상세 유의성 검정은 원문의 추가 자료이다.

[시각화 전 표의 수치·조건 보존]
GRAM-T · 20개 주파수 × SNR cell 중 유의한 반응 비율 (%)파형 조건 | Unmasking | Reversal | 
원신호 | 100 | 0 | 
고역통과 > 2 kHz | 100 | 0 | 
Mel 대역 ILD 제거 | 100 | 0 | 
50 Hz 포락선 vocoding | 50 | 25 | 
Vocoded 75% = 50% + 25% · 75% 정확도를 뜻하지 않는다.
[그래프]
원문 값 그대로 재구성. 각 패널은 자체 단위와 축을 사용하며 서로 다른 지표의 길이를 종합 점수로 읽지 않는다.
-->
