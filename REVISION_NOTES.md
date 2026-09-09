# Revision Notes — Anti-Slop Pass

## 2026-09-09 · 시각 구성 재정리

38장 구조 개정 뒤, 긴 제목과 축소된 논문 그림을 다시 검토했다. 제목과 화면 문구를 줄이고 상세 설명·해석 조건은 발표 노트에 보존했다. SARL의 접근성·민감도와 BMLD의 결과·단서 제거 그림을 분리해 본문을 30장으로 구성했다. Neural-SRP·AGG-RL의 응답 예시 두 장을 부록에 두어 현재 총 42장(본문 30장, 부록·참고문헌 12장)이다. 아래 38장 기록은 이전 단계의 이력이다. 이 변경 기록 자체가 최종 렌더링 품질의 검증을 대신하지는 않는다.

## 2026-09-09 · 학술 세미나 구조 개정

개정 직전 원고의 실제 35장(본문 32장, 부록·참고문헌 3장)을 38장(본문 28장, 부록·참고문헌 10장)으로 재구성했다. 아래에 남긴 ‘36개 slide chunk’는 이전 anti-slop 편집 당시의 기록이며 이번 개정 직전 장수를 뜻하지 않는다.

- [지정된 SlideShare 참고자료](https://www.slideshare.net/slideshow/ss-79607172/79607172)의 문제 제기, 필요한 개념, 한계와 해결 방법, 목표 재방문 흐름을 반영했다.
- 도입의 분류표를 배열 변경 사고실험과 발표 질문으로 바꾸었다. 25장에서 같은 상황을 다시 제시해 문헌의 증거와 후속 질문을 연결한다.
- 위치 추정, 표현 학습, 언어 모델, 검증의 전환 페이지에 앞 절의 내용과 다음 질문을 함께 제시했다. 방법 계열을 단선적인 기술 발전 단계로 설명하지 않는다.
- 데이터 분할은 평가 절로, PHAT와 판독기 수식·DSpAST와 OWL의 상세 구조·전체 문헌 지도는 부록으로 옮겼다. 전체 비교표를 두 장으로 나누고 용어표를 추가했다.
- 연구 목표를 먼저 분류하고 입력·학습·출력·적응·평가의 다섯 축을 비교하도록 용어를 통일했다.
- 인코더 적응량의 사다리를 인코더 고정 여부와 판독기 용량의 비교표로 바꾸었다. LLM 연결에서 인코더를 고정하는 경우를 명시했다.
- Neural-SRP의 추론 입력, MC-SimCLR의 양성 쌍, SFD의 대체 학습 목표, DSpAST의 요인 분기, OWL의 학습용 지도 정보와 추론 입력을 구체화했다.
- SARL의 합성 장면·선형 판독 조건을 명시했다. BMLD는 자극 조건과 지표를 먼저 설명하고, 임베딩 거리 비율을 청취 역치나 기하 등변성으로 해석하지 않도록 정리했다.
- 마지막 구조와 실험을 검증 전 연구 제안으로 표시하고 가설을 지지하지 못하는 조건을 추가했다. 결론은 ‘정답률에 더해 단서 변화에 맞게 반응하는지 확인한다’로 한정했다.

발표 시간이 지정되지 않아 대학원 세미나 30–40분을 가정했다. 현재 장별 역할과 본문·부록 구분은 [ACADEMIC_STRUCTURE.md](ACADEMIC_STRUCTURE.md)에 정리했다. 아래의 이전 편집 기준과 변경 기록은 이력으로 보존한다.

## 적용한 편집 기준

`prompts/anti_ai_slop_review.md`를 기준으로 전체 슬라이드를 다시 작성했다.

## 주요 변경

- 41장 원고를 36개 slide chunk로 재구성했다.
- “계보상의 의미”, “전환점”, “아직 아무도 해결하지 못했다”, “강한 방법 논문” 같은 추상적 문구를 삭제했다.
- 논문별 설명을 `입력 → 학습 목표 → 출력/interface → adaptation → 평가` 중심으로 바꿨다.
- AGG-RL·BAT·BMLD를 한 종류의 연구처럼 놓던 구성을 수정했다.
  - AGG-RL: task-native localization method
  - BAT: spatial-language system
  - BMLD: controlled-intervention evaluation
- “분야가 A에서 B로 진화했다”는 단선형 서술을 세 개의 병렬 계열과 가로지르는 평가층으로 바꿨다.
- 억지로 만든 통합 공백 슬라이드를 삭제하고, SFD·PhaseCoder·SARL·BMLD·BAT에서 직접 이어지는 비교 질문만 남겼다.
- 데이터 설명에 source corpus, HRTF/RIR/BRIR/ATF, microphone geometry, scene labels, split 단위를 포함했다.
- Frozen linear, small MLP, full fine-tuning, projector/LoRA의 증거 범위를 분리했다.
- current research는 “모든 문제를 통합한다”가 아니라 `phase information → relative intervention variable`이라는 구체적 질문으로 한정했다.
- 그라디언트·배지·카드 중심 스타일을 줄이고, 표와 입력–출력 흐름도를 중심으로 바꿨다.

## 삭제하거나 낮춘 주장

- “공간 오디오 연구는 어디서를 맞히는 모델에서 공간 변수를 재사용하는 모델로 이동했다.”
- “AGG-RL은 새로운 전환점이다.”
- “아직 general-purpose + geometry-aware + physically faithful + QA를 동시에 해결한 연구가 없다.”
- “BMLD는 물리 기전을 규명하는 방법 family다.”
- “SFD가 phase representation을 직접 검증했다.”
- “BAT과 AGG-RL은 같은 task 계열이다.”

## 남은 사실 검증 주의점

- 본문은 대표 논문 중심이며 전 분야를 망라한 survey가 아니다.
- GI-DOAEnet은 세부 방법 슬라이드 대신 AGG-RL의 geometry-conditioned baseline 계열로만 언급한다.
- LLM QA 수치는 encoder뿐 아니라 projector, LoRA, curriculum, 데이터 생성의 영향을 함께 받는다.
- BMLD는 특정 모델의 성능표가 아니라 frozen cue-sensitivity benchmark로 해석한다.
