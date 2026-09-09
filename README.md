# Spatial Audio Understanding Seminar

**모델은 소리를 듣고, 무엇이 어디에서 어떻게 일어나는지 판단할 수 있는가?**

공간 단서의 기초부터 위치 추정, 표현 학습, 언어 정렬, 목표 선택, 장면·관계·움직임 판단과 평가까지 연결하는 한국어 학술 세미나 자료다. 소리 생성·렌더링·로봇 행동 전반으로 범위를 넓히지 않는다. 논문을 설명하는 순서는 기술의 직접적인 대체 계보나 성능 순위가 아니다.

## 현재 상태 — 2026-09-09

| 구분 | 상태 | 시작 문서 |
| --- | --- | --- |
| 실행 가능한 현재 덱 | 본문 30장 + 부록·참고문헌 12장, 총 42장 | [slides.md](slides.md), [PDF](spatial-audio-lineage.pdf) |
| 다음 개정 설계 | 27편·78장, 레드팀 반영. 아직 덱에 적용하지 않음 | [NARRATIVE_PLAN.md](NARRATIVE_PLAN.md) |
| 장별 상세 명세 | 78장 모두 질문·핵심 문장·화면 근거·설명 순서·한계·전환 작성 | [S01–37](plans/BLUEPRINT_PART1.md), [S38–66](plans/BLUEPRINT_PART2.md), [S67–78](plans/BLUEPRINT_PART3.md) |
| 문헌 근거와 감사 | 버전, 결과 비교, 평가 조건, 반례와 원문 불일치 기록 | [27편 근거 인덱스](plans/EVIDENCE_LEDGER.md), [레드팀 보고](plans/REDTEAM_REVIEW.md) |

지금까지 정리한 내용:

- 현재 덱의 학술 발표 구조, 스타일, 원문 그림과 출처를 정리했다.
- 개정안은 기초 문제의식을 먼저 설명하고, 같은 장면에서 달라지는 질문과 출력을 연결하도록 설계했다.
- 각 결과의 입력·학습·출력·적응·평가 조건을 구분하고 본문에 표시할 비교를 선정했다.
- 시스템 답변 성능, 고정 표현의 판독, 통제 자극의 반응을 서로 다른 증거로 분리했다.
- [32장 초안](plans/narrative-32-slide-draft.md)과 [레드팀 이전 78장안](plans/narrative-78-slide-pre-redteam.md)을 보존했다.

다음 단계는 개정안의 그림 확보·출판본 대조, 실제 슬라이드 적용, 렌더 검증과 리허설이다. 78장안의 운영 예산은 설명 105분 + 그림 읽기·개념 회수 21분이며, 두 회차 56/70분을 가정한다. Q&A와 휴식은 별도이고 실측 발표 시간이 아니다. 현재 PDF에는 이 개정안이 반영되어 있지 않다.

## 실행

Node.js 버전은 [.nvmrc](.nvmrc)의 24를 기준으로 한다. nvm을 쓰는 경우 먼저 `nvm install`과 `nvm use`를 실행한다.

```bash
npm ci
npm run validate
npm run lint:slop
npm run dev
```

## 정적 빌드 / PDF

```bash
npm run build
npm run export
```

## 파일

- `slides.md`: 16:9 Slidev 원고
- `style.css`: 전역 스타일
- `global-bottom.vue`: 페이지 번호 등 공통 하단 요소
- `package-lock.json`: 재현 가능한 Node.js 의존성 설치
- `public/*.svg`: 로컬 벡터 자산
- `public/research/*`: 논문 그림과 데이터 설명 이미지
- `ACADEMIC_STRUCTURE.md`: 학술 발표의 질문, 본문·부록 구성, 구조 변경 이유
- `NARRATIVE_PLAN.md`, `plans/`: 다음 개정의 상세 설계와 문헌 근거
- `ASSET_SOURCES.md`: 현재 덱의 이미지 출처와 이용 조건 기록
- `prompts/anti_ai_slop_review.md`: AI slop 제거용 편집 프롬프트
- `REVISION_NOTES.md`: 삭제·수정한 주장 기록
- `scripts/validate.mjs`: 구조·asset·필수 논문 검증
- `scripts/anti_slop_lint.mjs`: 금지 문구와 과밀 슬라이드 점검

## 현재 42장 덱의 흐름

기존 덱은 ‘배열이 바뀌어도 공간 단서를 읽을 수 있는가’를 중심으로 한다. 상세 구성은 [ACADEMIC_STRUCTURE.md](ACADEMIC_STRUCTURE.md)에, 다음 78장 개정의 흐름은 [NARRATIVE_PLAN.md](NARRATIVE_PLAN.md)에 있다. [참고 SlideShare](https://www.slideshare.net/slideshow/ss-79607172/79607172)의 문제 제기→필요 개념→해결 방법→처음 질문 재방문 방식을 참고했다.

1. 1–3장: 배열 변경 사고실험과 발표의 질문·비교 범위
2. 4–5장: 교차 스펙트럼, IPD, TDoA, DOA와 배열 기하·HRTF
3. 6–10장: IPDnet, Neural-SRP, AGG-RL의 위치 추정과 배열 일반화
4. 11–14장: MC-SimCLR, CCSR, SFD, GRAM의 사전학습과 표현 재사용
5. 15–18장: BAT, PhaseCoder와 공간 언어 모델의 입력·과제 비교
6. 19–26장: 인코더 적응과 평가 조건, SARL의 접근성·민감도(22–23장), BMLD의 자극·반응·단서 기여(24–26장)
7. 27–30장: 처음 질문 재방문, 연구 가설, 네 가지 검증 실험과 결론·토의

31–42장은 용어, PHAT와 판독기 수식, DSpAST·OWL 상세, 문헌 지도, 목표와 다섯 비교축을 정리한 표, Neural-SRP·AGG-RL의 원문 응답 예시(39–40장), 참고문헌(41–42장)이다. 본문에서는 30장에서 발표를 마치고 필요할 때 부록을 참조한다.

## 검증 범위

`npm run validate`와 `npm run lint:slop`은 Node.js만으로 실행된다. 실제 Slidev build/export에는 `@slidev/cli`와 Playwright 설치가 필요하다.

이 두 검사는 현재 42장 덱용이다. 78장 설계의 내용·시간·시각 품질을 검증하는 도구는 아니며, 실제 개정 때 장수 제한과 검증 기준을 함께 갱신해야 한다. `scripts/render_preview.py`는 `mistune`을 사용하는 보조 HTML 미리보기이며 실제 Slidev 렌더를 대체하지 않는다.

## 저장소 관리와 출처

저장소 이름은 구현 도구나 임시 버전보다 주제를 드러내는 `spatial-audio-understanding-seminar`를 사용한다. 기존 PDF 파일명과 로컬 폴더명은 호환성을 위해 유지한다.

소스·설계 문서·발표용 자산과 현재 PDF를 버전 관리한다. `node_modules/`, `dist/`, `preview/`, `output/`, `tmp/`, `.codex-*` 작업 자료와 비밀 설정 파일은 제외하며 로컬 파일을 삭제하지 않는다.

논문 그림과 기관 로고의 권리는 각 원저작자에게 있다. 출처 기록은 [ASSET_SOURCES.md](ASSET_SOURCES.md)를 확인한다. 저장소 전체에 제3자 자산의 재배포 권한을 부여하는 라이선스를 임의로 붙이지 않는다. 연구 가설과 후속 실험은 검증 전 제안으로 구분한다.
