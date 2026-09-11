# S38–S66 원문 그림·제작 근거

취득일: 2026-09-11. 모든 원본은 아래 명시한 arXiv HTML의 고정 버전 자산에서 직접 취득했다. 도표 값은 plans/EVIDENCE_P12_P23.md의 선택 행·열을 유지해 수정 가능한 HTML 표로 작성했다. 원문 실험 그래픽을 생성형 도구로 재작성하거나 읽지 못한 숫자를 추정하지 않았다.

## 원본 자산

| 파일 | 원본 URL | SHA-256 |
| --- | --- | --- |
| `p2-sciphi-v1-fig1.png` | https://arxiv.org/html/2510.05542v1/model.png | `9ac37ba0ac23877058ecd517b52d862ff7eceaf1fddea11f76e0475a81963a3b` |
| `p2-sciphi-v1-fig2.jpg` | https://arxiv.org/html/2510.05542v1/figures/combined.jpg | `5cef0f24a01e56179e9c0583d5eab93c77d5a1650d71f86a14d3e2db9b85c2f5` |
| `p2-spatialomni-v2-fig1.png` | https://arxiv.org/html/2606.10738v2/model.png | `3a3c56103313786cdfc62516a561e0dd26b5be89f0c9c0e5cb115777bf1a76c8` |
| `p2-spatialomni-v2-fig2.png` | https://arxiv.org/html/2606.10738v2/data.png | `40931ca4e527e036b8528817a0df23ca4c212d374bc315a0a79c3ba266ec73e4` |
| `p2-twnm-v3-fig2.png` | https://arxiv.org/html/2601.02954v3/figures/twnm_framework.png | `294ec9137dc04d4c591250ae923102a6a8ca4f02b831a9f7e10c8ca2fa1c7967` |
| `p2-staudiolm-v1-fig1.png` | https://arxiv.org/html/2606.14141v1/pipeline.png | `7599da1a6582d49f88f85da2b3dc955aad399e11e6f954408072998173e379b6` |
| `p2-owl-v1-fig2.png` | https://arxiv.org/html/2509.26140v1/figure/simulation_setup_2.png | `287ac9bc170105d80181ab25059cee5a98af5cd757dd1aa4b7d58a42f37c07a0` |
| `p2-owl-v1-fig4.png` | https://arxiv.org/html/2509.26140v1/owl_main_arch.png | `5e25958e88e4e2ada0dfd620ff7626caccae4ae0bb7693773187ca37cd8ee8a7` |
| `p2-phasecoder-v2-fig2.png` | https://arxiv.org/html/2601.21124v2/visualizing_embeddings_v2.png | `112760256a4d02a7d3a19f22175a09f83c3e507bc77ec7380109839bd83c65c1` |
| `p2-twnm-v3-fig4.png` | https://arxiv.org/html/2601.02954v3/figures/asa_benchmark_examples.png | `1ee44a929acec39f87da7f36efcf3890369f1adcc0d56b9acfbce93ad340420e` |

## 원문 패널 추출

좌표는 원본 픽셀 `(left, top, right, bottom)`. 패널을 자르는 작업 외에 선·점·색·텍스트를 고치지 않았다.

| 추출 파일 | 원본 | 크롭 | 판독 범위 |
| --- | --- | --- | --- |
| `p2-sciphi-v1-tuplescore.png` | `p2-sciphi-v1-fig2.jpg` | `(0, 510, 880, 990)` | TupleScore 전체 패널. 축·모델 라벨·모든 원본 점을 보존. 해석은 SELDNet+Phi-4(MC, FT)와 Sci-Phi의 diamond 평균으로 제한. |
| `p2-spatialomni-v2-fig2a.png` | `p2-spatialomni-v2-fig2.png` | `(10, 38, 447, 564)` | Fig. 2(a) 과제 분류 원형도. 원문 질문 사례가 아니며 오른쪽 한국어 질의는 설명용 C53. |
| `p2-phasecoder-v2-input.png` | `p2-phasecoder-v2-fig2.png` | `(0, 0, 1728, 790)` | Fig. 2 상단 파형 관측. 시간(ms)·amplitude 축과 채널 범례 보존. 하단 분류 예측 분리. |
| `p2-twnm-v3-scene.png` | `p2-twnm-v3-fig4.png` | `(980, 69, 1515, 495)` | Fig. 4의 청취자 중심 장면. 평가 단계 정의를 위한 원문 도해이며 모델 입력·생성 장면 아님. 도해 4음원 기호와 최대 3음원 평가 조건 구분. |
| `p2-spatialomni-v2-path.png` | `p2-spatialomni-v2-fig1.png` | `(757, 0, 1600, 900)` | Fig. 1 오른쪽 공간·의미 토큰 결합 경로. 원문 visual branch는 backbone의 선택 경로로 구분. |

## 제작 검토에서 바로잡은 귀속

- S52: 계획의 “diamond만 남기기”는 원본 점의 삭제를 초래한다. 원본 패널을 그대로 추출하고 오른쪽 두 모델의 ◆/◇ 전체 평균만 읽도록 본문·노트에서 선택했다. 정밀값은 새로 쓰지 않았다.
- S53: Spatial-Omni Fig. 2(a)는 질의 사례 그림이 아닌 과제 분류도다. 원문 도해와 발표자 질의 예시를 구별했다.
- S56: TWNM Fig. 4 장면의 네 기호는 개념 도해다. 실제 모델·평가의 최대 세 source slots와 구분했다.
- S57: TWNM v3 §4.1은 source slots로 지도한 dense encoder map을 LLM에 전달한다고 명시한다. pooled source slot head만 LLM 입력이라고 오해하지 않도록 결론을 교정했다.

## 과학·구조 QA

- S38–S66 정확히 29장, 각 장 explicit seminar frontmatter와 발표 노트·원문 URL 포함.
- S39, 41, 44, 46, 48, 55, 58, 60, 61, 64, 66은 원문 선택 수치·단위·좋은 방향을 유지한 HTML 결과표.
- S44의 비개선 전이, S46 PA=0 비개선, S48 WER 악화, S58 L1/L2 하락, S60 DoA 하락, S61 Overall의 제한적 차이, S64 남는 난도를 보존했다.
- S49는 BAT/DSpAST를 공통 입력 계열 한 행으로 묶어 4행으로 구성. 같은 시스템으로 취급하지 않는다는 설명을 노트에 기록.
- 새 공통 CSS 클래스 없음. 기존 seminar-* 및 semantic-* 클래스와 인라인 구조·간격만 사용.
- 최종 렌더 검증·PPTX/PDF 내보내기는 전체 덱 통합 이후 root의 공통 QA를 따른다.
