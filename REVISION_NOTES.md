# Revision Notes — MC Audio-LM의 연구사

## 2026-09-11 · 공간 QA의 출발과 연구 질문의 분화

현재 덱은85장(본문49, 부록36)이다. 앞부분의 배열기하→GCC-PHAT→SRP→Neural-SRP와 다섯 라이트 Manim을 유지했다. BAT가 초기 공간 Audio-LM으로 도입한 E→P→LM 연결과 공간 QA를 본문에 복원했다. 이후 DSpAST/OWL의 encoder 개선, Motion의 JSON 대안, 기존 Audio-LM의 공간 확장, Dynamic QA/ST-AudioLM의 시간 구조로 연결한다.

6개 새 도식은 연구사 지도, 두 LM 입력 인터페이스, BAT의 전환, DSpAST/OWL 인코더 변화, 기존 의미·공간 경로, 동적 장면 처리다. 마지막 종합은 편집 가능한 native table이다. 이전의 중복된 adapter-training/synthesis 두 장을 제외해80→85장으로 바뀌었다. 원문 근거 페이지는 모두 유지했다.

최초 공개일과 채택 버전을 분리한다. BAT는2024년 시작이며, TWNM의 FOA·SAPO는2026-05-10 v3로 표시한다. Motion은2025년9월 OWL과 동시기의 대안이다. CoT/JSON/LoRA를 동일 분류 축에 놓지 않는다. 연속 오디오 입력을 LM hidden width·어휘 확대와 구분하며 Pengi의 frozen-LM 연결을 배경 사례로 소개한다.

기존99개 보고값과 별도 TWNM3개 보고값,27편 문헌과 각 수치의 비교 조건을 보존한다. OWL의 geometry-loss ablation은 위치 판독 결과이며 QA/LoRA 효과로 읽지 않는다. 기존 Audio-LM 확장은 관련 설계 문제로 묶되 직접적인 구현 계승을 과장하지 않는다. 실제 명시적 계승은 연구사 검증 대장에 근거를 남긴다.

산출물: `output/pptx/spatial-audio-understanding-mc-history-complete.pptx`, `output/pdf/spatial-audio-understanding-mc-history.pdf`. 최종 검수·개체 수·해시는 `output/manifest.json`과 `output/qa/mc-history/`를 따른다.

이전80장 개정 문서와 원고는 [보관 폴더](plans/archive/pre-mc-history)에 남겼으며 이전 배포본도 보존한다.
