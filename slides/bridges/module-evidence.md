---
layout: seminar
variant: result
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
[이번 장의 역할]
인코더·어댑터·언어 모델의 전체 구조를 이해한 뒤, 어댑터를 단순 차원 변환의 부품으로만 다루지 않는 근거를 보인다. TWNM의 Appendix G Table 15는 P0: Single MLP, P1: Dual Tower, P2: Dense Hybrid 연결 설계를 비교한다. Overall은 각각 39.20, 46.40, 52.10%다. ASA 평가에 대해 원문이 보고한 Overall이다. L1/L2/L3의 단순 평균으로 만들지 않는다.

이 표의 semantic-answer judge는 질문·선지·gold·생성 답변을 받는 Gemini 3 Flash이며 audio/RTSD를 직접 보지 않는다. 최종 SAPO 이전의 진단이다. 다음 장의 main Table 5에서 SFT/SAPO를 비교한 exact MCQA와 채점법이 다르므로 숫자의 높낮이를 두 표 사이에서 비교하지 않는다.

원문은 projector ablation이라고 명명하지만 각 행의 encoder checkpoint, LLM checkpoint, 학습 예산과 seed가 완전히 같은지 별도 명시하지 않는다. 따라서 연결 설계별 보고 결과로 해석한다. P만 바꾸고 나머지를 완벽히 고정한 인과 실험이라고 강화하지 않는다. 앞서 살펴본 DSpAST는 같은 QA 인터페이스의 인코더 비교, OWL은 인코더 사전학습 loss 비교였다. 다음 장에서는 SFT와 SAPO의 답변 학습 목표를 비교한다.

[원문 산술의 한계]
본문의 수준별 문항 수 385/279/336으로 Table 15의 수준별 점수를 가중해도 이 Overall과 일치하지 않는다. P0/P1/P2 재계산은 약 39.45/46.78/52.41이며 보고값 39.20/46.40/52.10과 다르다. 평가 집계 또는 분모의 차이는 원문만으로 해결하지 못했다. 슬라이드는 보고 Overall 세 개를 그대로 인용하며 정확한 성공 문항 수로 역산하지 않는다.

[Sources]
- https://arxiv.org/html/2601.02954v3
-->
