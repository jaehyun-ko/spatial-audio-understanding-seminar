# 공간 소리를 듣고 판단하는 모델

배열 기하에서 GCC-PHAT·SRP·Neural-SRP의 좌표 계산을 설명한 뒤, 공간 Audio-LM의 연구 질문이 어떻게 달라졌는지 연결하는 한국어 과학 세미나다.

## 현재 개정 — 2026-09-11

**85장: 본문 49장 + 근거 부록 36장, 핵심 문헌 27편.** MC Audio-LM을 모듈별로 흩어놓은 구성에서 BAT의 출발, 2025년의 분화, 기존 Audio-LM의 공간 확장, 시간·궤적 표현으로 다시 엮었다. 6개 설명 도식과 편집 가능한 종합표 1장을 추가하고 중복된 설명 두 장은 제외했다.

| 장 | 설명 흐름 |
| --- | --- |
| S01–S13 | 3D 목표 → 배열·시간차 → GCC-PHAT → SRP → Neural-SRP |
| S14–S21 | 좌표 이후 필요한 정보 → 연구사 지도 → JSON/연속 표현 → E·P·LM 적응 → 인코더 관찰 기준 |
| S22–S27 | BAT 2024의 공간 QA → DSpAST·OWL의 표현 개선 → Motion 2025의 JSON 대안 |
| S28–S36 | Sci-Phi·PhaseCoder·Spatial-Omni·TWNM: 기존 의미 경로와 공간 경로의 결합 |
| S37–S41 | Motion·Dynamic QA·ST-AudioLM: 정적 위치에서 시간별 음원 상태로 |
| S42–S49 | 표현 판독·정보 전달·답변 사용을 구별한 검증과 다음 실험 |
| S50–S85 | 원문 방법·결과·조건을 보존한 근거 부록 |

논문의 최초 공개일과 채택 버전을 구분한다. BAT의 시작은2024년이며 v4 결과를 사용한다. TWNM의 FOA·SAPO는2026년5월 v3의 방법이다. Sci-Phi·PhaseCoder·Spatial-Omni를 하나의 모델을 순차 개선한 계보로 연결하지 않는다. OWL의 CoT는 답변 학습, Motion의 JSON은 입력 전달, LoRA는 가중치 적응이다. 연속 임베딩의 입력 추가는 LM hidden width나 어휘 수 확대를 요구하지 않는다.

## 산출물

- [PowerPoint 최종본](output/pptx/spatial-audio-understanding-mc-history-complete.pptx)
- [PDF 최종본](output/pdf/spatial-audio-understanding-mc-history.pdf)
- [연구사·원문 검증](plans/MC_AUDIO_LM_HISTORY.md)
- [순서와 역할](plans/CAUSAL_DECK_ORDER.json), [검수·해시](output/manifest.json)

85장 PPTX/PDF의 라이트 배경, 수식14개, 발표 노트85개, native table1개와 텍스트728개를 확인했다. 최종 브라우저 검사와 PPTX 구조 검사에서 미해결 오류는0건이다. 검수 기록은 `output/qa/mc-history/`에 있다. 일반 파일명 별칭도 이번 최종본과 동일하다. 이전 `-localization` 배포본은 별도로 보존한다.

PPTX 제목·본문·캡션·출처와 S48 종합표는 편집 가능한 개체다. 수식·그림·그래프는 렌더 이미지이며 SVG·Python·JSON·NPZ 원본을 보존한다. 상세 해설과 비교 조건은 발표 노트에 있다. Pretendard 글꼴을 사용한다. PowerPoint 앱 대신 LibreOffice로 PPTX를 다시 렌더해 확인한다.

S02–S06의 다섯 Manim은 같은 라이트 테마를 유지한다. Slidev에서는 영상이 재생되고 PPTX/PDF에는 마지막 설명 포스터가 들어간다. GCC/SRP의 계산 장면은 교육용 합성이며 논문 성능 결과가 아니다. 기존23개 그래프의99개 보고값과 TWNM projector 비교의3개 보고값은 원문 조건과 함께 보존한다.

## 재생성과 내보내기

현재 순서의 기준은 `plans/CAUSAL_DECK_ORDER.json`, 설명 원고는 `slides/bridges/`, 원문 자료 보존본은 `slides/archive/visual-before-causal.md`다. part 파일은21/28/36장으로 나누며 관리상의 구분이다. 재생성은 part 파일을 덮어쓰므로 수정은 원천 자료에 반영한다.

```bash
node scripts/restructure-causal-deck.mjs
npm run assemble
npm run validate
npm run lint:slop
npm run dev:final
```

발표 화면은 `http://localhost:3037`, 노트는 `http://localhost:3037/#/presenter/`다. 내보내기를 실행하는 동안 원고·그림을 변경하거나 별도 build를 병행하지 않는다.

```bash
npm run build
npx slidev export slides.md --format pdf --per-slide --wait 500 --wait-until networkidle --output output/pdf/spatial-audio-understanding-mc-history.pdf
node scripts/export-editable-pptx.mjs --url http://localhost:3037 --out tmp/finalization/candidate-mc-history.pptx
python3 scripts/refine-pptx-typography.py tmp/finalization/candidate-mc-history.pptx
node scripts/finalize-pptx.mjs --candidate tmp/finalization/candidate-mc-history.pptx --out output/pptx/spatial-audio-understanding-mc-history-complete.pptx
node scripts/render-pptx-preview.mjs output/pptx/spatial-audio-understanding-mc-history-complete.pptx tmp/mc-history-pptx-qa
```

PPTX 생성에는 Codex 번들 Artifact Tool 런타임을 사용한다. `output/`과 `tmp/`는 생성물 폴더다.

## 근거와 편집 자료

[발표 설계](NARRATIVE_PLAN.md) · [학술 구조](ACADEMIC_STRUCTURE.md) · [27편 근거](plans/EVIDENCE_LEDGER.md) · [E/P/LM](plans/CAUSAL_LLM_MODULES.md) · [디자인](DESIGN_SYSTEM.md) · [자산 출처](ASSET_SOURCES.md) · [변경 기록](REVISION_NOTES.md)

## Tailnet 접속

현재 Slidev 주소는 [Tailnet 발표 화면](http://jaehyun-macmini.tail852ccc.ts.net:3037/)이다. Tailscale Serve가 Tailnet의3037을 로컬 IPv4 loopback3037로 연결한다. `vite.config.ts`에서 이 기기의 정확한 Tailnet 호스트를 허용한다.

```bash
npm run dev:tailnet
# 별도 터미널에서 Tailnet 전달 설정을 복원할 때
tailscale serve --bg --tcp=3037 tcp://127.0.0.1:3037
```

현재 백그라운드 서버의 PID와 로그 경로는 `tmp/tailnet/server.json`에 기록했다.
