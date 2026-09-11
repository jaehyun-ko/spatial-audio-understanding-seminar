# S67–S78 원문 그림·수치 근거

제작·검토일: 2026-09-11. 발표는 고정된 아래 버전을 사용한다. STAR와 WearVox의 별도 OpenReview 출판본 대조는 접근 오류(403)로 완료하지 못했으며 출판본과 동일하다고 주장하지 않는다.

| 장·자산 | 공식 원문 | 범위·변경 |
| --- | --- | --- |
| S68 `star-caption-comparison.svg` | https://arxiv.org/pdf/2510.24693v2 | PDF 2쪽, `(x=121,y=83,w=214,h=126)` pt. Caption 비교 원문 패널. 원본 벡터/래스터 보존. SHA-256·추출 명령은 `public/research/star-caption-comparison.source.json`. |
| S69 결과표 | https://arxiv.org/html/2510.24693v2 | Table 2, AA, Gemini 2.5 Pro (June 2025)의 40.87/48.97/45.28. 각 3지선다의 우연 기준 33.33과 구분. |
| S70 `wearvox-side-talk.svg` | https://arxiv.org/pdf/2601.02391v1 | PDF 2쪽, `(x=70,y=240,w=245,h=58)` pt. Side Talk Rejection 패널. SHA-256·추출 명령은 `public/research/wearvox-side-talk.source.json`. |
| S71 결과표 | https://arxiv.org/html/2601.02391v1 | Table 4: SC beamformed 85.4, MC channel 0 + beamformed interleave 93.9. 서론의 85.6 대신 표를 채택. |
| S72–73 `sarl-summary.svg` | https://arxiv.org/html/2606.05544v2/fig2.svg | 원본 그림. 의미·위치(방위/고도/거리)·방(RT60/부피/형상) 그룹과 정규화 축 보존. Fig. 3 민감도와 구별. |
| S74–75 자극·결과표 | https://arxiv.org/html/2606.14820v1 | §2와 Table 1: 500 Hz, −14 dB에서 Spatial-AST 6.8*, DSpAST 7.0*, GRAM-T 2.1*, WavJEPA 0.5*. 별표는 원문의 FDR q=.05. 사람의 탐지 역치나 QA 정확도가 아니다. |
| S76 결과표 | https://arxiv.org/html/2606.14820v1/fig4_ablation.png | 본문의 Fig. 3 원본 GRAM-T 막대를 확인해 네 조건의 수치를 재작성. 원신호·고역통과·Mel ILD 제거는 unmasking/reversal 100/0, vocoding은 50/25. Total 75는 정확도가 아니다. |

S67·S77·S78은 근거의 종류와 연구 질문을 비교한 발표자의 종합이다. 새 실험 결과를 생성하지 않았다. 결과표는 HTML 표와 PPTX의 native table로 작성했으며 원문 수치가 직접 편집 가능한 셀에 들어 있다. 원문 그림에는 생성형 재작성, 데이터 제거, 곡선 보정이나 눈대중 수치 추가를 하지 않았다.

## 최종 호환성 수정

68·70장의 PDF 벡터 추출 시편은 보존했다. STAR 시편에 인접 패널 조각이 남고 WearVox의 SVG mask가 LibreOffice에서 검게 렌더되어, 최종 슬라이드에는 같은 공식 원문 그림의 원본 PNG를 크롭했다. 원문 수치·곡선·범례·발화 내용은 바꾸지 않았다.

- `star-caption-panel.png`: `star-caption-original.png`(1576×545)의 `(0,0,905,107)`, `(0,107,870,490)`, `(0,490,916,545)` 세 직사각형을 원래 위치 그대로 백색 916×545 캔버스에 유지했다. 인접 패널 조각만 제외하고 원문 그래프·주석·전체 범례를 보존한다.
- `wearvox-side-talk-panel.png`: `wearvox-tasks-original.png`(1134×563)의 `(0,420,598,563)` 크롭. Fig. 1의 Side Talk Rejection 패널이다.

원본 PNG의 출처는 위 표와 같은 고정 원문의 Fig. 1이며, SVG 추출본을 다시 그리거나 생성형 도구로 재작성하지 않았다. 파일 해시:

- `star-caption-original.png`: `85a5f0b65d77b063d6937e0204a5f12c46649cd248b619d43b691b9c7653feaa`
- `star-caption-panel.png`: `e5cb2ef51e83f04f7f89ca0ce631d5d3addbd26dc100581da079ec0ce413b6a4`
- `wearvox-tasks-original.png`: `f33916ec5cd926f575fd4ef29cf154985d43c50d9bd44cd43e8d26d26b962e5d`
- `wearvox-side-talk-panel.png`: `569ca0bf7da1078142b99fbf329fc5e93004dac95e783fefce41d86d209e89c7`
