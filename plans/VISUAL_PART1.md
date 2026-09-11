# Part 1: 설명을 읽는 화면에서 관계를 보는 화면으로

S03–37 중 텍스트 개념·방법·정성 비교 16장을 새 설명 그림으로 바꿨다. S01/S02와 모든 기존 원문 그림 및 정량 결과표는 수정하지 않았다. 전체 37장 수와 기존 발표 노트를 유지했으며, 교체한 본문·aside의 설명은 각 장의 `[시각화 전 본문 설명]`에 보존했다.

## 적용 기준

- 캔버스 `#f6f8fa`, 주 텍스트 `#142233`, 관측/초점 파랑 `#1f5fae`, 두 번째 관측/기하 청록 `#007b80`, 공통 라벨 `#008b9a`, 보조 문구 `#586879`.
- 각 그림은 1136 × 400 SVG이며 같은 이름의 2272 × 800 PNG도 제공한다. SVG의 도형, 경로, 파형 및 문구는 모두 새로 작성했다. 원문 도형을 트레이싱하거나 스크린샷을 변형하지 않았다.
- 그래프와 마스킹은 관계를 설명하는 합성 도식이다. 논문의 관측값, 모델 점수, 실제 복원 결과로 제시하지 않는다. 축에 실측 단위를 붙이거나 임의의 성능 수치를 넣지 않았다.
- 기하 그림은 마이크, 음원, 경로, 후보 방향 자체를 보여 준다. 프로토콜 그림은 짧은 모듈 이름과 실제 연결/업데이트 경로를 보여 준다. 긴 해설을 상자에 옮겨 담는 방식은 사용하지 않았다.
- 원문의 실험 범위와 핵심 가정은 캡션과 노트에 남겼다. 고정 인코더와 zero-shot, SELD와 자유형 QA, 위치 판독과 파형 분리를 혼동하지 않는다.

## 자산과 과학적 근거

| 장 | 자산 (`public/diagrams/`, SVG + PNG) | 표현한 관계 | 근거 및 범위 |
| --- | --- | --- | --- |
| S03 | `p1-channel-cues` | 두 관측 파형의 시간·레벨·주파수별 위상 차이 | SFD의 관측 단서, MIT OCW의 ITD/ILD 교육 설명. 파형은 설명용 합성 함수이며 각 비교를 독립적으로 단순화했다. |
| S06 | `p1-room-observation` | 음원 레벨·직접음 거리·반사 경로가 관측에 합쳐짐 | CCSR의 신호 모델. 작은 신호의 크기 하나로 거리를 유일하게 정한다는 의미가 아니다. |
| S07 | `p1-array-baseline` | 평면파의 입사 방향과 배열 중심을 고정한 두 간격 | AGG-RL 기반 원거리 단일 음원 사고실험. 파면은 입사 방향에 수직이다. |
| S08 | `p1-direction-then-event` | 활성 방향 응답의 두 후보와 사건 이름의 연결 | 발표용 과제 구분. 응답은 임의 함수이며 실제 모델 출력이 아니다. 모든 시스템의 필수 두 단계 구현을 뜻하지 않는다. |
| S09 | `p1-candidate-delay-match` | 후보 기하 → 쌍별 기대 지연 → 관측 대조 → 합산 응답 | Neural-SRP·AGG-RL 및 기존 노트의 GCC/SRP 직관. 상관 곡선은 실제 측정값이 아니다. |
| S12 | `p1-query-grid` | 동일 녹음·배열과 성긴/촘촘한 질의 격자 | AGG-RL §2.2. 질의 격자 증가는 정확도의 자동 향상을 뜻하지 않는다. |
| S15 | `p1-seld-timeline` | 사건별 활성 구간과 해당 방향 | DCASE 공식 SELD 출력 정의. 정적 두 음원 설명용 예시이며 고정 클래스·활성·DOA의 결합을 보인다. |
| S16 | `p1-input-representations` | 물리 마이크 위치, 두 귀 관측, FOA 기저 성분 | AGG-RL·SFD·GRAM. FOA 기저는 형태를 구별하는 단면 도식이며 네 개 점 마이크로 표현하지 않았다. |
| S17 | `p1-frozen-finetune` | 판독기만 업데이트하는 경로와 전체 업데이트 경로 | MC-SimCLR·CCSR·GRAM 평가 조건, D2L의 특징층/출력층 구분. 두 경우 모두 후속 지도 판독을 포함한다. |
| S18 | `p1-contrastive-crops` | 같은 다채널 녹음의 시간 crop과 표현 공간의 당김 | MC-SimCLR Fig. 1. 정지·비중첩 음원 가정. 단일 채널 둘을 임의로 양성 쌍으로 고르는 그림이 아니다. |
| S20 | `p1-ccsr-masking` | 공동 마스킹과 상보 마스킹, 결합 후 STFT 복원 | CCSR Fig. 1·§IV-A. 마스크의 구체적 인덱스는 설명용이며 전체 구현도를 대체하지 않는다. |
| S26 | `p1-fusion-depth` | 낮은/높은 공간 특징에 연결되는 의미 특징 | AT2SELD Fig. 25 기반 결합 위치의 두 대안. 자유 어휘 QA 구조를 뜻하지 않는다. |
| S29 | `p1-pretrain-probe` | 마스킹 사전학습에서 고정 표현의 지도 판독으로 전달 | GRAM Fig. 1·HEAR 평가, D2L의 특징 추출/출력층 구분. 전체 미세조정 실험은 별도 범위다. |
| S31 | `p1-protocol-map` | 6개 연구의 목표 → 평가 모듈 → 출력 | 기존 표의 각 연구 대응을 개별 경로로 풀었다. CCSR/SFD의 밑줄은 인코더와 판독기 모두의 업데이트. LAM/AT2SELD의 지도 판독·적응을 구별한다. 통합 순위가 아니다. |
| S32 | `p1-spatial-language` | 뒤쪽 알람 관측과 위치 단어만 다른 후보 문장 | ELSA의 정렬 문제. 임의 정합 점수·실제 정답 판정을 넣지 않았다. |
| S34 | `p1-salm-factorization` | 동일 소리 이동, omni 의미 분기와 FOA 공간 분기 | SALM Fig. 1. 분기 역할을 보이며 통계적 독립성이나 완전 분리를 입증하는 그림이 아니다. |

## 교육 참고 자료

논문 목록 27편의 정체성·버전을 추가하거나 바꾸지 않았다. 아래 자료는 설명 순서와 시각적 대응을 위한 교육 참고이며, 실험 주장의 출처는 원래 논문이다.

1. [MIT OCW 9.04 Sensory Systems, Fall 2013: introductory lecture transcript, pp. 25–26](https://ocw.mit.edu/courses/9-04-sensory-systems-fall-2013/974a38b4102523393a53a4464fe66045_g1ka1MXpo3s.pdf). 두 귀의 도착 시간과 레벨을 각각 비교하는 설명을 S03의 두 파형 비교 순서에 참고했다. 영상이나 슬라이드 이미지를 가져오지 않았다.
2. [DCASE 2019: Sound Event Localization and Detection](https://dcase.community/challenge2019/task-sound-event-localization-and-detection). 사건 클래스, onset/offset, DOA의 대응을 S15의 타임라인과 공간 화살표로 연결했다.
3. [Dive into Deep Learning §14.2: Fine-Tuning](https://d2l.ai/chapter_computer-vision/fine-tuning.html). 사전학습 특징층과 새 출력층의 구별, 특징층을 고정하는 변형을 S17/S29의 업데이트 경로에 참고했다. 원 그림은 복사하지 않았다.

## 재생성 및 검증

- SVG 생성: `python3 scripts/visuals/part1-diagrams.py`
- PNG 렌더: `node scripts/visuals/render-part1-diagrams.mjs`
- 두 스크립트는 스크립트 위치를 기준으로 저장소의 `public/diagrams`를 찾는다. PNG 렌더는 `public/fonts`에 포함된 Pretendard Regular/SemiBold/Bold WOFF2를 사용하므로 개인 홈 경로나 시스템 폰트 설치에 의존하지 않는다. Node 의존성은 저장소의 `playwright-chromium`을 사용한다.
- 기존 자산을 바꾸지 않고 재생성하려면 SVG 생성에 `--output-dir tmp/part1-rebuild`를, PNG 렌더에 `--input-dir tmp/part1-rebuild --output-dir tmp/part1-rebuild`를 붙인다. 명시한 상대 경로는 실행한 디렉터리를 기준으로 해석한다.
- 소스 적용: `tmp/visual-part1/apply_slides.py` (이미 적용됨; 재실행은 노트 중복을 만들므로 하지 않는다.)
- 교체 전 최신 Part 1: `tmp/visual-part1/part1-before-visual.md`.
- 그림 접촉 시트: `tmp/visual-part1/contact-1.png`–`contact-4.png` (첫 검토용; 최종 수정 SVG/PNG가 기준).
- 적용 스크립트는 총 37개 발표 노트와 수정 대상 밖 21개 장의 바이트 단위 불변성을 확인했다.
- 최초 접촉 시트 검토에서 마스킹 격자의 작은 셀, S17/S26의 하단 문구, S07의 파면 방향, FOA 쌍엽의 접점을 수정했다. 최종 PPT/PDF는 루트 작업에서 전체 덱을 조립한 뒤 별도 검증한다.
- 최종 SVG 16개의 텍스트 bounding box 점검: 캔버스 이탈 0건, 텍스트 사이 겹침 0건.
- 조립된 실제 Slidev 16장 QA: `tmp/visual-part1/deck-qa-final/report.json`, 모두 review candidate 0건. 접촉 시트 4개로 전체 16장의 밝은 배경·도형·레이블·캡션·takeaway 배치를 눈으로 확인했다. 최초 서버 504(Outdated Optimize Dep)가 해소된 뒤 새로 실행한 최종 결과다.
- 영구 경로 스크립트를 저장소 밖의 임시 작업 디렉터리에서 실행해 검증했다. 재생성 SVG 16개는 기존 `public/diagrams/p1-*.svg`와 SHA-256이 모두 일치했다. PNG 16개도 임시 경로에 2272 × 800으로 정상 렌더했다. 검증 전후 기존 SVG/PNG 32개와 `slides/part1.md`의 해시는 변하지 않았다.

최종 통합 PPTX LibreOffice 검수: 2026-09-11, 해당 Part 전체 장을 접촉 시트로 검토하고 핵심 수식·기하·그래프 장을 원본 크기로 확대했다. 추가 수정이 필요한 오류는 발견하지 못했다. `tmp/visual-pptx-qa`에 최종 렌더를 보관한다.
