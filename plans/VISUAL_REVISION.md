# 그림 중심 개정 — 2026-09-11

최종 덱은 78장, 고정 원문 27편, 발표 노트 78개를 유지한다. 새 개념도 30개와 결과 그래프 23개를 넣었다. 나머지 장은 원문 그림·그래프·Manim을 중심으로 구성하고 필요한 직접 설명만 남겼다. 원문 그림의 축·범례는 그대로 유지했다.

## 3차원 연구 목표

S02는 두 마이크를 x축 위에 두고 중점을 원점 O로 정의한다. 알람을 향한 거리 r, +x에서 +y 방향의 방위각 α, xy 평면에서 +z 방향의 고도각 β를 그렸다. 원점에서 음원까지의 벡터, 수평 투영, 각도 호를 함께 보여준다. S78도 같은 좌표 관례로 마무리한다.

좌표 정의는 [MathWorks Spherical Coordinates](https://www.mathworks.com/help/phased/ug/spherical-coordinates.html)를 따랐다. 그림은 연구의 출력 목표를 설명한다. 두 마이크의 단일 TDoA가 임의의 3차원 음원 위치를 유일하게 결정한다는 뜻은 아니다.

## 그림으로 바꾼 설명

| 범위 | 새 그림 | 표현 방식 |
| --- | ---: | --- |
| S02 | 1 | x축 마이크 쌍과 3차원 알람 좌표 |
| Part 1 | 16 | 도착 시간·레벨·위상 파형, 전달 경로, 배열, 방향 응답, 사건 타임라인, 마스킹, 고정/학습 경로, 공간 문장 |
| Part 2 | 8 | 음원 위치 교환, 특징 가중치, gain 파형, 학습/추론 조건, 음원별 속성, 시간 구간, 교차 궤적, 사건 순서 |
| Part 3 | 5 | 평가 대상, 선형 판독, 같은 잡음의 표적 위상 반전, 알람의 다양한 출력, 관측·출력·근거 |
| 정량 결과 | 23 | 0 기준 막대, 지표별 두 점 비교, 명시적 범위의 선, 의미를 구분한 누적 막대 |

MIT 감각계 강의·Auditory Lab, DCASE 과제 설명, Dive into Deep Learning 교재, Csound 공간화 교재의 설명 순서를 참고했다. Manim은 기존 3Blue1Brown 공식 코드의 추적값·대응 변환 방식으로 구성한 라이트 영상을 유지한다. 교육 자료의 그림이나 영상을 그대로 복제하지 않았다. 실제 연구 결과는 기존에 고정한 각 논문 버전에만 근거한다.

- [Part 1 출처·변경·검수](VISUAL_PART1.md)
- [Part 2 출처·변경·검수](VISUAL_PART2.md)
- [Part 3 출처·변경·검수](VISUAL_PART3.md)
- [Manim 구성과 코드 참고](../manim/scenes.md)

긴 본문과 원표는 각 장의 발표 노트에 보존했다. 중요한 평가 조건, 방법 대응, 결과가 나빠진 반례, 단위와 유의성 별표는 화면에서도 읽을 수 있다. 글자 수는 그림 안 라벨을 제외하면 실제 감소를 과장하므로 전체 감소율을 주장하지 않는다.

## 정량 근거 보존

`RESULTS_VISUAL_DATA.json`은 원표 행과 그래프에 배치한 값을 함께 담는다. 23장의 결과 수치 99개와 S46의 PA 조건 두 개를 이전 표와 대조했다. 그림에 없던 성능 수치를 새로 만들거나 서로 다른 논문 점수를 정규화하지 않았다.

- S46: PA 조건을 두 패널로 바꾸고 Dither Off/On을 비교한다.
- S61: 50–60% y축을 명시한 선 그래프다. 구간 masking 결과를 음원 분리로 해석하지 않는다.
- S75: 유의성 별표와 q 조건을 유지한다.
- S76: 50% unmasking과 25% reversal의 합 75%는 유의한 반응 비율이며 정확도가 아니다.

## 편집과 재생성

프로젝트 Python 환경에는 NumPy·Matplotlib·Manim이 있고, 생성 그림은 Pretendard를 사용한다. Part 1·2 PNG 렌더는 프로젝트 Playwright Chromium과 `public/fonts`의 글꼴을 사용한다.

```bash
.venv/bin/python scripts/visuals/spatial-goal.py
python3 scripts/visuals/part1-diagrams.py
node scripts/visuals/render-part1-diagrams.mjs
python3 scripts/visuals/part2-diagrams.py
node scripts/visuals/render-part2-diagrams.mjs
.venv/bin/python scripts/visuals/part3-diagrams.py
.venv/bin/python scripts/visuals/result-charts.py
npm run assemble
npm run validate
npm run lint:slop
```

SVG는 Slidev와 PDF용이다. PPTX는 대응 PNG를 포함한다. 개념도 PNG는 2배 해상도, 결과 그래프 PNG는 1.8배 해상도다. 본문 수식은 KaTeX, 그래프·개념도의 수식은 mathtext 또는 벡터 표기, Manim은 MathTex로 조판한다. PPTX의 독립 본문 수식 6개는 2배 해상도 렌더 이미지다. 제목·캡션·출처 등 624개 텍스트 개체는 PPTX에서 편집 가능하다. 현재 PPTX 안에 native 표는 없으며, 그래프 수치는 JSON과 생성 스크립트에서 수정한다.

내보내기와 최종화는 [README](../README.md)의 명령을 따른다. 현재 확정본은 `output/pptx/spatial-audio-understanding-visual.pptx`와 `output/pdf/spatial-audio-understanding-visual.pdf`다. 일반 파일명과 루트 PDF도 같은 최신 내용이며 이전 `-light` 파일은 보존했다.

## 최종 검수

- 78장 구조, 27편 출처, 81개 자산 참조, 발표 노트 검사 및 anti-slop 검사 통과.
- 프로덕션 빌드 통과. 브라우저 전체 78장 자동 조판 검사에서 잘림·겹침·수식 오류 0건. Wake Lock 권한 경고 2건은 브라우저의 절전 방지 기능과 관련되며 렌더 오류가 아니다.
- PPTX 무결성·글꼴·조판·Artifact Tool 재가져오기 검사 통과.
- PDF와 LibreOffice에서 렌더한 PPTX 78장 모두 실제 이미지로 검토. 좌표·파형·수식·그래프 핵심 장은 원본 크기로 확대 확인.
- 전체 PPTX와 PDF 78장 배경 `#f6f8fa` 유지, PPTX 텍스트 624개 및 독립 수식 이미지 6개 보존 확인.
- 원표 99개 결과 숫자 및 PA 조건 두 개, 발표 노트 78개 보존 확인.
- 검수 JSON은 `output/qa/visual/`, 파일 해시·구성은 `output/manifest.json`에 보관한다. Microsoft PowerPoint 앱에서는 직접 검수하지 않았다.
