# 도입부 Manim 원본과 현재 덱의 사용 범위

2026-09-11 인코더·어댑터·LLM 구성 개정본에서는 이 시퀀스의 **S02–S06 다섯 장면**을 사용한다. 현재 덱 S07은 새 질문 로드맵이며, 아래의 6장 독립 미리보기와 원본 S07 영상은 이전 도입 설계의 기록이다. `apply.mjs`는 이전 2–7장 교체용이므로 현재 재구성 덱에는 실행하지 않는다. 현재 순서는 `plans/CAUSAL_DECK_ORDER.json`을 따른다.

기존 78장 덱의 2–7번만 대체하는 연속 장면이다. 일반 음원과 x축의 두 마이크를 유지하면서 공간 좌표, 관측 신호, 시간차, 반사와 혼합, 배열 기하, 연구 범위를 전개한다.

- 최종 영상: `output/intro-sequence/intro-02-07.mp4` (1920×1080, 60 fps, 59.25초)
- 6장 PDF: `output/intro-sequence/intro-02-07.pdf`
- 발표 미리보기: `http://localhost:3037/animations/intro-sequence/review.html`
- 현재 Slidev 사용 구간: `slides/part1.md`와 `slides.md`의 2–6번
- 6장 독립 Slidev 입력: `intro-review.md`
- 구간별 영상과 포스터: `public/animations/intro-sequence/`

미리보기는 각 구간 끝에서 멈춘다. 방향키로 이동하고 Space로 재생·정지한다. 전체 재생은 한 영상에서 장면을 이어 보여준다. PDF에는 각 구간의 마지막 도해를 사용한다.

## 재현

프로젝트 루트의 기존 `.venv`와 설치된 LaTeX, ffmpeg를 사용한다. 전역 설정과 다른 파트의 생성 코드는 변경하지 않는다.

```sh
.venv/bin/manim --media_dir tmp/intro-sequence/media-final --save_sections --progress_bar none -v WARNING manim/intro-sequence/intro.py SpatialAudioIntro -o intro-sequence.mp4
python3 manim/intro-sequence/publish.py
python3 manim/intro-sequence/export_webm.py
python3 manim/intro-sequence/export_video.py
```

`apply.mjs`는 보존된 이전 원고에만 적용하는 마이그레이션이다. 현재 덱은 `scripts/restructure-causal-deck.mjs`와 `npm run assemble`로 재구성한다.

서버 3037이 실행 중일 때 아래 검수를 실행할 수 있다. PDF도 이 과정에서 생성한다.

```sh
node manim/intro-sequence/verify.mjs
.venv/bin/python manim/intro-sequence/verify_physics.py
node scripts/visual-qa.mjs --url http://localhost:3037 --slides 2-6 --out tmp/intro-sequence/deck-qa --fail-on-warnings
```

좌표 관례, 신호 모델, 논문 그림과의 대응 범위는 `scenes.md`에, 발표 문구와 출처는 `slides.json`에 기록했다. 애니메이션은 독립 작성한 ManimCE 코드다. 3B1B의 객체 연속성과 동기화 구성을 참고했으며 코드나 미디어를 복사하지 않았다.
