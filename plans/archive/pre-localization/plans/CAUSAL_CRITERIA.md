# 공간 표현의 성질을 관측하는 기준

2026-09-11. 문헌의 보고 범위와 **아직 수행하지 않은 후속 실험 제안**을 구분한다. 기존 논문의 숫자는 근거 대장에 유지하며, 이 문서와 세 bridge 슬라이드는 새로운 성능 수치를 만들지 않는다.

## 구조 진단과 발표의 중심 질문

논문마다 입력–구조–결과를 반복하면 ‘무엇을 해결하려고 다음 논문을 읽는가’가 늦게 드러난다. 마지막에 QA·probe·자극 반응을 모아도 서로 다른 모델의 결과가 하나의 모델을 단계별로 검증한 것처럼 보일 수 있다. 그림의 수를 늘리는 것과 설명의 논리를 바꾸는 것은 별개다.

발표의 중심 질문은 **“LLM에 넘기는 표현에 어떤 공간 정보가 있어야 하며, 그 정보가 답에 쓰였다는 것을 어떻게 확인하는가?”**다. 도입의 같은 알람–말소리 장면을 계속 사용한다. 논문은 이 질문의 개별 관측 창으로 배치한다. 한 논문의 좋은 결과가 다음 단계의 통과를 보장하지 않는다.

표기는 입력 X → encoder E의 표현 H → projector/adapter P의 토큰 Z → LLM L(Z,Q)의 답 Y로 통일한다. 전처리는 E 앞 별도 과정이며 P와 혼동하지 않는다. 목표 좌표는 마이크 쌍의 중점 O를 기준으로 한 방위각 α, 고도각 β, 거리 r이다. 마이크는 x축의 (−d/2,0,0), (d/2,0,0)에 놓는다. α는 +x에서 +y 방향, β는 xy 평면에서 +z 방향이다. 이 좌표 정의는 두 마이크의 한 TDOA만으로 3개 좌표를 유일하게 식별한다는 주장이 아니다.

원하는 출력이 음원 종류·위치·시간·정체성을 요구한다면 이 속성들을 관찰한다. 모든 과제에 원시 위상이나 모든 방 속성의 재구성이 필요한 것은 아니다. 위치 질의에서는 위치 변화에 맞는 출력 변화가 필요하고, 동일 소리를 이동했을 때 소리의 종류는 유지돼야 한다. **의미 불변성과 위치 민감성은 같은 표현에서 함께 요구할 수 있다.**

## 일곱 성질: 관측량과 통제 실험

아래 실험은 해당 문헌의 실험을 그대로 했다는 서술이 아니라 후속 설계다. probe의 학습 용량·학습 예산·데이터 분할을 고정하고, H의 frame 표현·평균 표현·Z를 따로 측정한다. 선형 판독 실패는 해당 판독 조건의 한계이며 정보의 완전한 부재를 뜻하지 않는다. Probe의 해석 범위는 [Belinkov 2022](https://aclanthology.org/2022.cl-1.7/), 무작위 라벨 대조의 동기는 [Hewitt & Liang 2019](https://aclanthology.org/D19-1275/)에 근거한다. 후자의 언어 probe 방법을 오디오에 적용하는 것은 이 발표의 제안이다.

| 필요한 성질 | 관측량 | 바꾸는 것 / 고정하는 것 | 실패를 구분하는 대조 |
| --- | --- | --- | --- |
| 공간 정보의 판독 가능성 | 방위·고도 각오차(°), 구면 방향오차(°), 거리 절대·상대 오차; H·Z에서 동일 용량 판독 | 같은 dry sound·방·잡음에서 위치만 이동. 방·음원 identity를 분리한 평가 | 채널 순서·지연·gain·전처리 후 실제 입력을 먼저 검사. 비공간 질문은 유지. 단일 평균 점수보다 각 좌표별 보고 |
| 의미–위치 결속 | 음원 종류와 좌표의 **공동 대응** 정확도, prompt 표적의 방향오차와 누락·오검출 | 두 소리의 종류 집합과 위치 집합을 그대로 두고 배치만 맞교환 | 각 종류·각 위치를 따로 맞히는 점수와 비교. 모든 종류×위치 조합을 균형화해 위치별 class prior 차단 |
| 시간과 음원 정체성 | AB/BA 순서 판독; 지속 추적이면 ID switch·연속성·누락까지 | 같은 사건과 위치의 시간 순서 교환; 별도로 같은 종류 두 음원의 교차·재등장 | 알려진 구간 경계와 예측 경계 분리. frame별 정답 대응과 지속 identity를 별도 평가 |
| 기하·도메인 전이 | 좌표 변환 후 방향·거리 오차, 새 방·배열·장치별 성능 | 배열/장면 회전, 미관측 방·mic geometry·실녹음으로 이동 | 좌표계를 회전하면 예측 좌표도 그 변환을 따라야 한다. 좌표 정합 후 비교하며, 기존 좌표를 무조건 유지하는 ‘불변성’으로 평가하지 않음 |
| 언어와의 정렬 | 동일 후보 집합의 retrieval Recall@K, 위치·관계 hard-negative 구별, 질의 바꿔쓰기 일관성 | 같은 오디오에서 방향 단어·관계·사건 순서만 달리한 문장 | 의미만 다른 음성/문장과 공간만 다른 문장을 구분. 검색 성공과 생성형 LLM의 사용을 별도 측정 |
| 답변의 정보 의존성 | label이 바뀐 짝을 **둘 다** 맞힌 비율; token 개입 후 목표 오류 변화 및 복구 | 고정 checkpoint에서 위치가 다른 오디오·H·Z를 대응 치환. 제거/복구 조건 포함 | 질문만, 무관하지만 길이·분포가 맞는 오디오, 동일 예산의 무작위 token 제거, 정상 token 복구. 단순 답변 변화는 성공이 아님 |
| 기존 의미 정보의 보존 | 원래 비공간 task의 macro-F1·retrieval·해당 speech task의 WER 등 | 공간 적응 전후의 동일 비공간 평가; 위치만 바꾼 같은 음원의 의미 판독 | 일반 의미 caption/label 사용. 공간을 포함한 caption 검색을 일반 의미 보존의 대용으로 삼지 않음. 공간·의미 성능의 절충을 함께 표시 |

### 성질과 문헌의 연결

- **ELSA**는 공간 표현과 문장 정렬, 합성→실녹음 분포 이동의 관측 창이다. 동일 계열 평가에서도 실제 소규모 S-RWD 결과를 합성 결과와 분리해야 한다. [v1 §3–4, Table 2](https://arxiv.org/html/2409.11369v1). 이를 일반적인 LLM 답변의 정보 사용 증거로 확대하지 않는다.
- **SALM**의 semantic/spatial branch와 공간 문장·DOA 학습은 의미 정렬과 방향 판독을 따로 관측할 동기를 준다. 구조적으로 branch를 나눈 것만으로 통계적 독립이나 일반화가 증명되지는 않는다. 실측 SRIR로 만든 오디오는 현장 혼합음 녹음과 구별한다. [v2 §2–3, Tables 1–3](https://arxiv.org/html/2507.16724v2).
- **SelectTSL**은 질의로 선택한 소리와 위치의 결속을 본다. MAE는 맞게 대응된 검출만의 오차이므로 F1을 함께 읽는다. MOTA*는 ID switch를 생략하고 frame별 대응을 사용하므로 지속 정체성의 증거가 아니다. [v1 §V, Table VI](https://arxiv.org/html/2607.02343v1).
- **CoSTALA**의 시간·공간 hard negative는 사건/위치 집합을 유지하고 대응만 바꾸는 대조의 예다. 평가 retrieval은 E_global과 복합 T_st의 정렬이며, 구간 분할에는 원래 사건 길이가 쓰인다. ‘semantic-only’ 열도 E_sem↔T_st이므로 원래 비공간 의미 보존 검증으로 읽지 않는다. [v1 §2–3, Table 2](https://arxiv.org/html/2608.24374v1).

## 기존 증거는 pipeline 어디에 놓이는가?

| 문헌·현재 근거 | 관측 위치 | 말할 수 있는 것 | 말하면 안 되는 것 / 후속 제안 |
| --- | --- | --- | --- |
| SARL v2, Fig. 2 선형 probe | frozen E의 pooling된 H | 지정된 판독기로 요인 라벨을 읽는 성능 | Fig. 3의 통제 변화에 대한 표현 민감도와도 별개. Z나 LLM 사용을 검사하지 않음 |
| SARL v2, Fig. 3 변화 민감도 | 통제한 X → H 거리 | 특정 source/room 변화에 표현이 얼마나 달라지는지 | 정답 좌표를 읽는 정확도, 특정 음향 단서의 독점 사용으로 읽지 않음 |
| Interference/BMLD v1 | 위상 조건을 바꾼 X → frozen E의 H | S₀N₀·SπN₀의 기준 N₀ 대비 임베딩 거리비 | 사람의 탐지 역치, 선형 위치 판독, LLM 답변 정확도가 아님 |
| ELSA·SALM·CoSTALA | E 및 별도 audio–text readout | 지정된 template·caption 후보에서 정렬 | 생성 LLM의 실제 소비나 모든 원래 의미 보존을 보장하지 않음 |
| SelectTSL | audio encoder + prompt-conditioned head | 선택한 음원의 검출·위치 대응 | LLM token 사용이나 장기 identity tracking의 검증 아님 |
| Spatial-Omni v2, zero-spatial 변형 | P→Z→LLM의 공간 token 인터페이스 | 선택된 공간 task에서 실제 공간 token 조건의 유용성 | 본문은 zero-spatial ‘변형’으로 기술. 동일 checkpoint의 추론 시 제거만 바꿨다고 단정하지 않음. 특정 phase 기전의 증명 아님 |
| BAT v4, Table 4 P / B+P | LLM 질문만 vs 오디오+질문 | Type E 평가에서 질문만 기준을 넘는 청각 입력의 기여 | 특정 phase 단서나 token 축의 기여로 해석하지 않음. 다른 학습 variant를 pure inference ablation으로 합치지 않음 |
| STAR-Bench v2 | 입력 인터페이스를 포함한 전체 QA | 공간 질문의 정답·재실행 일관성, native preprocessing 제약 | 선택 Table 2 기준은 Random Guess. caption 비교도 question-only가 아님. 질문만/오디오 치환은 후속 제안 |
| WearVox v1 | 실제 wearable 입력 + projection + LLM | 실제 side-talk 조건의 전체 SLLM 성능 | frozen encoder만의 향상이나 phase만의 효과가 아님. 입력은 beamformed와 선택 채널이며 raw 5ch 전체 입력이 아님 |

직접 근거: [SARL v2 §3](https://arxiv.org/html/2606.05544v2), [Interference/BMLD v1 §2](https://arxiv.org/html/2606.14820v1), [Spatial-Omni v2 §5–6](https://arxiv.org/html/2606.10738v2), [BAT v4 Table 4](https://arxiv.org/html/2402.01591v4), [STAR-Bench v2 §3–4 및 Appendix C/D](https://arxiv.org/html/2510.24693v2), [WearVox v1 §4.3 및 Table 4](https://arxiv.org/html/2601.02391v1). 고정한 27개 논문의 source version은 기존 근거 대장을 따른다.

BMLD 자극은 같은 잡음 n으로 N₀=(n,n), S₀N₀=(n+s,n+s), SπN₀=(n+s,n−s)를 만든다. 오른쪽 **표적**의 반전이지 오른쪽 혼합음 전체의 반전이 아니다. 위상 변경은 혼합음 간섭·특징을 함께 바꾸므로, 반응 하나로 내부 단일 기전을 식별하지 못한다.

## 최소 실험 설계 — 모두 제안, 미실행

1. **입력부터 확인한다.** 원 오디오와 모델 전처리 후 channel 수·동기·gain·downmix 여부를 기록한다. 위치를 바꾼 한 쌍, 소리 종류를 바꾼 한 쌍, 시간 순서를 바꾼 한 쌍을 렌더하고, 원본 음원·방·잡음 seed를 공유한다. 위치 변화 자체에 따른 RIR·ILD 변화는 신호 생성의 일부다. 이 전체 변화와 특정 phase 단서의 독립 개입을 구분한다.
2. **같은 checkpoint의 E와 P 경계를 읽는다.** H_frame, H_mean, Z에 동일한 판독 문제와 학습 예산을 적용한다. source clip·room·RIR identity가 train/test에 새지 않도록 분리하고, label permutation·단순 기준선·별도 용량의 readout을 보고한다. H에서 높고 Z에서 낮으면 adapter 경계에서의 접근 가능성 저하를 의심하되 정보 소멸로 확정하지 않는다.
3. **답의 올바른 변화를 검사한다.** 질문을 고정하고 알람 위치만 바뀐 장면 쌍에 대해 두 정답을 모두 맞히는지 측정한다. 같은 장면 쌍의 ‘어떤 소리인가’ 답은 유지돼야 한다. 그 다음 H 또는 Z를 다른 짝의 것으로 바꾸고, 공간 token 제거와 정상 token 복구를 실시한다. token 수·norm·분포 변화 및 다른 의미 정보 손실을 대조한다.
4. **질문 prior와 개입 손상을 검사한다.** 질문만, 내용은 같고 위치만 다른 오디오, 길이·수준을 맞춘 무관 오디오, 같은 수의 무작위 token 제거를 비교한다. 원 checkpoint를 고정한 추론 개입과 재학습 variant의 성능 차이를 다른 그림/표에 둔다.
5. **일반화와 의미 비용을 마지막에 함께 본다.** 새 room·array geometry·device·실녹음 조건을 각각 분리하고 좌표계를 보정한다. 기존 의미 task를 같은 평가셋에서 다시 수행한다. 실환경 성공은 유용한 외적 검증이며 내부 단서 사용의 독립적인 증명은 아니다.

정답이 바뀌는 counterfactual 쌍의 권장 관측량은 `mean[1(pred(X,Q)=Y AND pred(X′,Q)=Y′)]`이다. 정답이 유지돼야 하는 nuisance 변환에는 오류 증가/출력 일관성을 사용한다. **정답이 바뀌어야 하는 조작과 유지돼야 하는 조작을 같은 consistency 점수로 합치지 않는다.**

개입 후 성능 하락만으로 목표 정보의 역할을 확정하지 않는다. 비표적 의미 task의 손상, 무작위 동일 예산 제거, 원 토큰 복구를 함께 봐야 한다. 이것은 언어 모델의 [Amnesic Probing](https://aclanthology.org/2021.tacl-1.10/)에서 제기한 encoded–used 구분과 후속 [개입 선택성 연구](https://aclanthology.org/2025.findings-acl.674/)를 공간 오디오에 적용하는 제안이다. Attention 그림은 이 개입을 대체하지 않는다.

## 새 bridge 슬라이드와 자산

- `slides/bridges/encoder-criteria.md`: 위치만/종류만/순서만 바꾼 3개 입력 쌍과 H 판독. 유지할 성질과 변해야 할 성질을 같은 그림에서 표시.
- `slides/bridges/causal-evaluation.md`: X→E(H)→P(Z)→LLM(답)에 판독·token 개입·질문만/오디오 개입을 서로 다른 위치로 배치. 기존 근거와 미실행 제안을 구분.
- `slides/bridges/closing-tests.md`: 같은 3D mic 장면에서 좌표→token→답의 3단계 후속 실험을 회수.
- 생성 코드: `scripts/visuals/causal-evaluation.py`. 산출물: `public/diagrams/causal-{encoder-criteria,evaluation-map,closing-tests}.{svg,png}`.
- 화면은 light paper #f6f8fa, ink #142233, blue #1f5fae, teal #008b9a, orange #a95018. 기본 크기 1136×404; PNG 2272×808. 수식은 Matplotlib mathtext/STIX path로 출력.
- QA 기록은 자산 및 조립 preview 확인 후 아래에 추가한다.

### Spatial-Omni zero 조건의 원문 확인

v2 §5.3은 SO-7B-zs의 zero token 사용, Appendix E.2 *Spatial Audio LLM Baselines*는 null spatial token의 LLM 입력을 기술한다. §5.1과 Appendix C.3의 일반 3단계 학습 설명에서는 SO-7B-zs의 적용 시점과 SO-7B checkpoint 공유를 특정하지 않는다. 그러므로 **학습부터 zero**와 **같은 checkpoint에서 추론 때만 zero** 중 어느 쪽인지 현재 원문만으로 결정하지 않는다. 화면은 ‘zero 기준선’, notes는 ‘적용 시점·checkpoint 공유 미명시’로 고정했다. [원문 §5.3·Appendix E.2](https://arxiv.org/html/2606.10738v2).

### 자산 QA — 2026-09-11

- 새 SVG 3개와 2272×808 PNG 3개를 생성하고 실제 PNG 전체를 열어 확인했다. 순서 조작·두 마이크 위치·α/β/r·H/Z 분기·보고/제안 표시를 확인했다.
- 그림 내부 텍스트 경계 검사를 통과했다. 숫자 성능값을 사용하지 않았으며 latent cell·probe scatter·파형은 설명용임을 notes에 명시했다.
- 마지막 수정에서 좌표 α와 M₂가 가까운 간격을 분리하고, 알람 원위치 A/이동위치 B를 종료 그림의 정답 쌍에 연결했다. BAT 질문만 조건에는 X 제외를 표시했다.
- 원래 parts, shared CSS, 기존 PNG/SVG에는 변경을 가하지 않았다. 최종 조립 슬라이드 검수는 아래에 별도 기록한다.

### 3장 직접 렌더 QA 완료

- 3개 chunk를 `tmp/causal-bridge-preview/slides.md`에 모으고 동일 layout/components/style를 읽는 별도 Slidev 3041 서버에서 1280×720으로 렌더했다.
- `node scripts/visual-qa.mjs --url http://localhost:3041 --slides 3 --out tmp/causal-bridge-qa/slides --fail-on-warnings`: 세 장 모두 0 review candidates.
- 실제 `slide-01.png`~`slide-03.png`를 모두 full-size로 열어 제목·라이트 배경·한글·수식·파형·공간 좌표·takeaway·source의 잘림과 겹침이 없음을 확인했다. 시험 제안과 보고된 관측의 색/점선 구분, position 변화와 의미 유지 구분도 확인했다.
- 위 검수는 bridge 자체의 브라우저 렌더다. 최종 본문 위치에 조립된 덱의 PDF/PPTX 검수는 export 후 별도다.
