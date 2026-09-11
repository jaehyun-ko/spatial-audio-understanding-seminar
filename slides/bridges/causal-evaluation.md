---
layout: seminar
variant: figure
---

# 읽히는 정보가 답에도 쓰이는가?

::body::
<PaperFigure src="/diagrams/causal-evaluation-map.svg" alt="입력 X, 인코더 E의 H, projector P의 Z, LLM과 답으로 이어지는 공통 관측 지도. SARL 판독은 H, BMLD 자극 반응은 X에서 H, Spatial-Omni zero 기준선은 공간 token 인터페이스, BAT 질문만 조건은 X 없이 Q에 배치한다. 주황 점선은 token 치환·복구와 오디오 짝 비교의 미실행 제안이다." caption="각 문헌의 관측 위치를 겹쳐 그린 지도. E: 인코더 · P: adapter · Q: 질문." />

::takeaway::
<strong>판독, 자극 반응, token 비교, 답변 변화</strong>는 서로 다른 증거다.

::source::
SARL v2 §3 · BMLD v1 §2 · Spatial-Omni v2 §5.3·App. E · BAT v4 Table 4.

<!--
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
[전환]
처음 알람 장면으로 돌아가 동일 모델의 표현·토큰·답을 함께 검사하는 다음 실험을 정한다.
-->
