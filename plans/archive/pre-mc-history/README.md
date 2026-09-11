# 공간 소리를 듣고 판단하는 모델

**배열 기하로 좌표를 어떻게 찾는지 먼저 설명하고, 그 계산을 학습으로 바꾼 뒤 LLM 통합으로 넘어가는 한국어 학술 세미나**다. 핵심 문헌 27편은 각 질문에 필요한 구조·실험의 근거로 읽는다.

## 현재 개정 — 2026-09-11

현재 구성은 **80장: 본문 47장 + 근거 부록 33장**이다. 배열 기하 다음에 GCC-PHAT의 지연 곡선, 같은 시간차를 만드는 위치들, SRP의 후보별 점수, 여러 마이크 쌍의 합산을 차례로 배치했다. 그 계산을 이해한 뒤 Neural-SRP의 학습 대상을 설명한다. AGG-RL의 배열·후보 격자 확장은 부록으로 옮겼다.

현재 순서는 [CAUSAL_DECK_ORDER.json](plans/CAUSAL_DECK_ORDER.json)을 따른다. 연결 원고는 `slides/bridges/`, 원문 근거 보존본은 `slides/archive/visual-before-causal.md`에 있다. `slides/part1.md`·`part2.md`·`part3.md`의 37/29/14 분할은 파일 관리 단위이며 발표의 절 경계가 아니다. 이전 causal 개정 문서는 [보관 폴더](plans/archive/pre-localization)에 남겼다.

## 발표 흐름

| 장 | 설명 순서 |
| --- | --- |
| S01–S06 | 3D 목표 좌표 → 관측 → 경로차·시간차 → 잔향·혼합 → 배열 기하 |
| S07–S10 | GCC-PHAT 지연 곡선 → 같은 지연의 위치 궤적 → 후보 좌표의 점수 → 쌍 합산·최대점 |
| S11–S13 | Neural-SRP의 쌍 응답 학습 → 실제 응답 예시 → 실녹음 적응 결과 |
| S14–S21 | 좌표만으로 부족한 질문 → 인코더·어댑터·LLM/LoRA → 표현의 관찰 기준과 근거 |
| S22–S29 | 의미·위치·시간 관계를 어떤 토큰 구조로 전달할 것인가 |
| S30–S34 | 어댑터 정렬과 LLM 적응을 어떻게 학습할 것인가 |
| S35–S40 | 모듈·학습 조건의 차이가 무엇을 뒷받침하는가 |
| S41–S47 | 표현에서 읽힌 정보가 실제 답에도 쓰이는지 어떻게 확인할 것인가 |
| S48–S80 | 질문별 근거 부록. S49–S51은 AGG-RL의 배열·후보 확장 |

GCC-PHAT은 지연축 점수 곡선을 만든다. SRP는 후보 좌표에서 기대 지연을 계산해 **그 지연의 곡선 값을 조회하고**, 쌍별 점수를 합쳐 최대 좌표를 고른다. 쌍마다 피크 하나를 먼저 선택해야 하는 알고리즘으로 설명하지 않는다. Neural-SRP는 쌍별 공간 응답을 학습하며 합산·argmax는 유지한다. 한 쌍의 TDoA로 3D 좌표가 유일하게 결정되지는 않는다.

## 산출물과 검수

이번 개정의 배포 경로는 [PowerPoint](output/pptx/spatial-audio-understanding-localization-final.pptx)와 [PDF](output/pdf/spatial-audio-understanding-localization.pdf)다. 생성·검수 상태와 해시는 [산출물 명세](output/manifest.json), 검사 기록은 `output/qa/localization/`에서 확인한다. PPTX/PDF 80장 내보내기와 검수를 마쳤다. 일반 파일명 별칭은 이번 최종본과 동일하다. 이전 `-causal` 파일은 이전 개정으로 보존한다.

PPTX 제목·본문·캡션·출처는 편집 가능한 텍스트, 수식·그림·그래프는 렌더 이미지다. SVG·Python·JSON 편집 원본을 보존한다. 발표 노트에는 상세 해설·조건·원표를 남긴다. PPTX는 native 텍스트 run 694개, 발표 노트 80개, 전체 글리프를 포함한 2배 해상도 수식 이미지 14개를 포함한다. Pretendard를 사용하며, 다른 컴퓨터에도 같은 글꼴 설치가 필요하다. 브라우저 80장 검사에서 잘림·겹침·수식 오류 0건을 확인했다. PDF 70장은 이전 검수본과 본문 픽셀이 같고, 새 4장과 변경 6장을 개별 검수했다. LibreOffice PPTX 렌더도 변경 영역과 이전 검수본을 대조했다. Microsoft PowerPoint 앱 직접 검수와는 구별한다.

S02–S06의 활성 Manim 다섯 장은 유지한다. 목표 좌표 → 관측 → 시간차 → 잔향·혼합 → 배열 기하를 같은 라이트 장면에서 보여준다. S07부터는 GCC-PHAT/SRP 설명 도해다. Slidev는 영상을 재생하고 PPTX/PDF는 마지막 설명 포스터를 쓴다. 이전 intro s07과 `tdoa-ipd-wrap`은 보존 미디어이며 현재 위치의 영상이 아니다.

기존 23개 결과 그래프의 **99개 보고값**과 TWNM adapter 비교의 **3개 보고값**을 구분해 보존한다. 새 GCC/SRP 그림의 값은 알려진 합성 신호·기하에 대한 교육용 계산이며 논문 성능에 추가하지 않는다. 모든 자체 도해·영상은 라이트 테마, 수식은 수식 조판을 유지한다.

## 실행과 내보내기

```bash
npm ci
npm run assemble
npm run validate
npm run lint:slop
npm run dev:final
```

발표 화면은 `http://localhost:3037`, 노트는 `http://localhost:3037/#/presenter/`다. `scripts/restructure-causal-deck.mjs`는 보존 원고·bridge·순서 JSON으로 part 파일을 덮어쓰므로, part에 직접 한 수정을 원천에 반영한 뒤 재생성한다.

```bash
npm run qa
npm run build
npx slidev export slides.md --format pdf --per-slide --wait 500 --wait-until networkidle --output output/pdf/spatial-audio-understanding-localization.pdf
node scripts/export-editable-pptx.mjs --url http://localhost:3037 --out tmp/localization-finalization/candidate.pptx
python3 scripts/refine-pptx-typography.py tmp/localization-finalization/candidate.pptx
node scripts/finalize-pptx.mjs --candidate tmp/localization-finalization/candidate.pptx --out output/pptx/spatial-audio-understanding-localization-final.pptx
node scripts/render-pptx-preview.mjs output/pptx/spatial-audio-understanding-localization-final.pptx tmp/localization-pptx-final-qa
```

PPTX 내보내기는 Codex 번들 Artifact Tool 런타임을 사용한다. `RUNTIME_NODE_MODULES`로 모듈 경로를 지정할 수 있다. `output/`과 `tmp/`는 생성물 폴더로 Git에서 제외한다.

## 근거와 재현 자료

- [발표 설계](NARRATIVE_PLAN.md), [학술 구조](ACADEMIC_STRUCTURE.md), [좌표 계산에서 인코더로](plans/CAUSAL_SIGNAL_BRIDGE.md), [어댑터·LLM](plans/CAUSAL_LLM_MODULES.md), [관찰 기준](plans/CAUSAL_CRITERIA.md)
- [27편 근거와 현재 번호](plans/EVIDENCE_LEDGER.md), [기존 결과 데이터](plans/RESULTS_VISUAL_DATA.json), [TWNM adapter 보고값](plans/CAUSAL_ADAPTER_DATA.json)
- [자산 출처](ASSET_SOURCES.md), [디자인 규칙](DESIGN_SYSTEM.md), [변경 기록](REVISION_NOTES.md)
