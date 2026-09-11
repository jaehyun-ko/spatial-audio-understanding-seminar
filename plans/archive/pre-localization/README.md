# 공간 소리를 듣고 판단하는 모델

**마이크의 관측을 LLM의 답변으로 연결하려면 어떤 정보가 남고, 전달되고, 사용되어야 하는가?** 이 질문을 중심으로 신호처리, 공간 인코더, adapter와 LLM 적응, 평가를 연결하는 한국어 학술 세미나다. 27편의 지정 원문을 다루며, 서로 다른 논문의 점수를 통합 순위나 한 모델의 단계별 검증으로 해석하지 않는다.

## 현재 개정 — 2026-09-11

전체 78장을 **본문 48장 + 질문별 근거 부록 30장**으로 재구성했다. 새 연결 페이지 14장과 설명 그림 13개를 추가해 논문별 반복 소개를 관측·설계·검증의 질문으로 연결한다. 기존 비교 그래프의 수치 99개와 TWNM 원문에 보고된 adapter 비교값 3개를 대조 범위로 관리한다. 후자의 채점 방식·비교 범위는 [별도 원자료](plans/CAUSAL_ADAPTER_DATA.json)에 기록했다.

현재 장 번호와 본문·부록 구분의 기준은 [CAUSAL_DECK_ORDER.json](plans/CAUSAL_DECK_ORDER.json)이다. 편집 원본은 `slides/part1.md`·`part2.md`·`part3.md`이며 파일 분할 37/29/12는 발표의 절 구분이 아니다. 새 연결 페이지는 [slides/bridges](slides/bridges)에 있고, 개정 전 원고는 [보존본](slides/archive/visual-before-causal.md)에 남아 있다.

## 산출물과 편집 범위

- [PowerPoint](output/pptx/spatial-audio-understanding-causal-final.pptx): 검수한 78장 최종본. 제목·본문·캡션·출처는 편집 가능한 native 텍스트 run 669개이며 발표 노트 78개를 보존한다. 본문 수식 8개는 전체 글리프 높이를 포함한 2배 해상도 이미지다. 개념도·그래프는 이미지이고 편집 원본은 SVG·Python·JSON으로 보존한다.
- [PDF](output/pdf/spatial-audio-understanding-causal.pdf): 검수한 78장 배포본. 새 SVG 도식·그래프는 벡터를 유지하며 원문 래스터 그림과 Manim 포스터는 이미지다.
- [Slidev 원고](slides.md): 활성 애니메이션과 발표 노트를 포함한다. 상세 해설·평가 조건·원표는 각 장의 노트에 남겼다.

도입의 활성 Manim은 **S02–S06의 다섯 장**이다. 같은 3차원 장면에서 목표 좌표 → 두 채널 관측 → 경로와 시간차 → 잔향·혼합 → 배열 기하를 보여준다. [개별 재생 파일](public/animations/intro-sequence)과 [제작 원본](manim/intro-sequence)을 보존한다. **S07은 새 정적 로드맵**이다. 이전 약 12초 `tdoa-ipd-wrap.mp4`는 보존된 파일럿이며 현재 S05의 영상이 아니다. PPTX/PDF에는 마지막 설명 포스터를 사용한다.

PPTX 글꼴은 Pretendard다. 다른 컴퓨터에서도 같은 글꼴을 설치해야 조판을 유지하기 쉽다. 검수 절차는 브라우저 화면, PDF 렌더, LibreOffice의 PPTX 렌더를 각각 읽는 방식이며 Microsoft PowerPoint 앱의 직접 검수와 구별한다.

PDF와 LibreOffice의 PPTX 렌더를 각각 78장 모두 개별 검수했고, 원고와 발표 노트 78개의 일치를 확인했다. 본문 수식 8개의 전체 높이를 보존하도록 캡처 범위를 수정한 뒤 수식이 있는 6장을 다시 읽었다. 활성 Manim 5개 MP4의 3,084프레임은 모서리 RGB 검사에서 밝은 배경을 유지했다. 전체 78장 브라우저 검사는 geometry 발견사항 0건, runtime error 0건이다. 페이지별 새 로드의 wake-lock 환경 경고 78건과 표지·부록의 의도된 배경 장식 경고 2건은 별도 기록했다. 패키지·글꼴·재가져오기 검사와 파일 동일성 기록은 [검수 자료](output/qa/causal)와 [산출물 명세](output/manifest.json)에 있다.

## 발표 흐름

| 장 | 중심 질문 |
| --- | --- |
| 1–14 | 기하로 계산한 공간 응답을 무엇까지 학습으로 바꿀 수 있는가? |
| 15–21 | 인코더에 어떤 정보가 남아야 하고 어떻게 읽는가? |
| 22–30 | 의미·위치·시간을 어떤 토큰 구조로 전달하는가? |
| 31–35 | adapter 정렬과 LLM 적응은 각각 무엇을 바꾸는가? |
| 36–41 | 모듈·학습 조건의 차이를 어느 성능에 귀속할 수 있는가? |
| 42–48 | 답이 실제 소리에 근거하는지 어떤 관측과 개입으로 확인하는가? |
| 49–78 | 필요할 때 선택하는 근거 부록: A 관측·인코더, B 결속, C 전달할 관측, D 시간, E 답변 근거 |

S48에서 본문을 마친다. 부록은 두 번째 연속 발표가 아니라 질문에 따라 선택하는 자료다. 이전 두 회차 구성이나 126분 설계 예산은 현재 48장 본문의 실측 발표 시간으로 사용하지 않는다.

## 실행과 내보내기

Node.js 24와 프로젝트 의존성을 사용한다.

```bash
npm ci
npm run assemble
npm run validate
npm run lint:slop
npm run dev:final
```

발표 화면은 `http://localhost:3037`, 노트는 `http://localhost:3037/#/presenter/`다. part 원고 편집 뒤 `npm run assemble`로 `slides.md`를 갱신한다. 구조를 다시 생성할 때에는 `scripts/restructure-causal-deck.mjs`가 보존 원고·bridge·순서 JSON으로 part 파일을 덮어쓴다는 점을 확인하고 실행한다. 독립적으로 수정한 part 내용을 먼저 반영해야 한다.

```bash
npm run qa
npm run build
npx slidev export slides.md --format pdf --per-slide --wait 300 --wait-until networkidle --output output/pdf/spatial-audio-understanding-causal.pdf
```

PPTX 내보내기는 Codex 번들 Artifact Tool 런타임을 사용한다. `RUNTIME_NODE_MODULES`로 모듈 경로를 지정할 수 있다. 실행 중인 3037 서버와 `slides.md`가 같은 원고여야 한다.

```bash
node scripts/export-editable-pptx.mjs --url http://localhost:3037 --out tmp/causal-finalization/candidate.pptx
python3 scripts/refine-pptx-typography.py tmp/causal-finalization/candidate.pptx
node scripts/finalize-pptx.mjs --candidate tmp/causal-finalization/candidate.pptx --out output/pptx/spatial-audio-understanding-causal-final.pptx
node scripts/render-pptx-preview.mjs output/pptx/spatial-audio-understanding-causal-final.pptx tmp/causal-pptx-final-qa
```

이번 개정의 구분 파일명은 PPTX의 `-causal-final`과 PDF의 `-causal`이다. `output/pptx/spatial-audio-understanding-causal.pptx`와 일반 파일명 `output/pptx/spatial-audio-understanding.pptx`는 최종 PPTX와 바이트가 같은 별칭이다. `output/pdf/spatial-audio-understanding.pdf`와 루트 `spatial-audio-lineage.pdf`도 causal PDF와 바이트가 같다. 이전 `-visual`·`-light` 파일은 이력이다. `output/`과 `tmp/`는 생성물 폴더로 Git에서 제외한다.

## 근거와 재현 자료

- [현재 순서](plans/CAUSAL_DECK_ORDER.json), [발표 흐름](NARRATIVE_PLAN.md), [학술 구조](ACADEMIC_STRUCTURE.md), [인코더와 신호처리 연결](plans/CAUSAL_SIGNAL_BRIDGE.md), [adapter·LLM 연결](plans/CAUSAL_LLM_MODULES.md), [성질과 통제 실험](plans/CAUSAL_CRITERIA.md)
- [27편 근거 인덱스](plans/EVIDENCE_LEDGER.md), [기존 비교값](plans/RESULTS_VISUAL_DATA.json), [TWNM adapter 보고값](plans/CAUSAL_ADAPTER_DATA.json)
- [그림 생성 코드](scripts/visuals), [원문 그림 출처](ASSET_SOURCES.md), [이전 시각화 개정](plans/VISUAL_REVISION.md)
- [디자인 규칙](DESIGN_SYSTEM.md), [디자인 시편](design-system.md), [변경 기록](REVISION_NOTES.md)

학습 목표·frozen probe·표현의 자극 반응·전체 QA 점수는 서로 다른 증거다. SARL 판독은 LLM 사용을 보장하지 않고, BMLD 표현 반응은 사람의 탐지 역치가 아니다. STAR의 random guess와 BAT의 질문만 조건도 구분한다. 새 통제 실험은 제안으로 표시한다. 논문 그림과 기관 로고의 권리는 각 원저작자에게 있다.
