# Part 2 visual revision — S38–S66

2026-09-11. Scope: S38, S40, S45, S49, S50, S59, S62, S65. The part still contains 29 slides. These eight slides now use authored teaching diagrams with direct labels. Original paper figures and all eleven quantitative result tables were unchanged by this authoring subtask. Original scientific notes, evaluation conditions, source versions and limitations were retained verbatim; a separate visual-provenance paragraph was added.

## Design and interpretation

All diagrams use the deck's light canvas `#f6f8fa`, navy `#142233`, blue `#1f5fae`, teal `#008b9a`, secondary text `#586879`, rule `#d4dde7` and caution `#a95018`. Their viewport is 1136×360, fitting the 1136×404 body with a short figure caption. Direct labels are 24–30 px. Bell and speaking-person shapes consistently denote the same two example sources. Listener orientation is forward/up, making left and right unambiguous.

These are original reconstructions of the stated task or method, not traced paper figures and not actual model predictions. No result data were invented. The SVG originals preserve geometry and labels; PNG delivery versions are rasterized at 2272×720 for PowerPoint compatibility.

| Slide | Original explanation replaced by | Scientific basis | Asset stem |
| --- | --- | --- | --- |
| S38 | Two listener-centered source scenes, the same sources exchanging left/right, direct answer labels | [BAT v4, Table 1](https://arxiv.org/html/2402.01591v4) | `p2-s38-position-swap` |
| S40 | Binaural waveforms, feature planes, visibly different feature-weight bars, three parameter-sharing branches, event/direction/distance pictograms | [DSpAST v1, §3.2–3.3 and Fig. 1](https://arxiv.org/html/2509.13927v1) | `p2-s40-feature-selection` |
| S45 | Three aligned L/R waveform pairs with identical timing and different amplitude | [Dual-BEATs v1, §3.2 and App. A.3](https://arxiv.org/html/2607.08800v1); [Csound FLOSS Manual, Panning and Spatialization](https://www.csound-tutorial.net/floss_manual/Release04/Cs_FM_04_ScrapBook/b-panning-and-spatialization.html) | `p2-s45-gain-waveforms` |
| S49 | Training/inference boundary map with depth planes, binaural heads, gain waveforms and microphone-coordinate geometry | BAT/DSpAST above; [OWL v1](https://arxiv.org/html/2509.26140v1); [PhaseCoder v2](https://arxiv.org/html/2601.21124v2); Dual-BEATs above | `p2-s49-learning-inference` |
| S50 | A room, two named sources, direction/distance rays, source-linked activity bars, room/background properties | [Sci-Phi v1, §3.3](https://arxiv.org/html/2510.05542v1) | `p2-s50-scene-attributes` |
| S59 | Separate event bars, one continuous location–time curve, and a query interval with time mask | [Motion v1, Table 1](https://arxiv.org/html/2509.14666v1); [Dynamic QA v1, Table 2](https://arxiv.org/html/2602.16334v1) | `p2-s59-time-requirements` |
| S62 | Two crossing location–time curves with persistent A/B identity, ending in an explicit time-conditioned left/right relation | [ST-AudioLM v1, ST-AudioQA Table 1](https://arxiv.org/html/2606.14141v1) | `p2-s62-source-trajectories` |
| S65 | Three time-by-position event grids distinguishing a reference, time reversal and position swap | [CoSTALA v1, §2.1](https://arxiv.org/html/2608.24374v1) | `p2-s65-event-negatives` |

S40 feature-plane intensities and weight-bar heights are deliberately illustrative, and its caption says so. The shared patch-embedding and Transformer parameters are explicitly labeled; the image does not claim three independent large encoders. S45 does not impose a numerical pan law or reproduce the paper's gain range. Its equations remain properly typeset `MathInline` in the caption. Its labels compare gains, avoiding the incorrect pointwise statement that an oscillating waveform L is always greater than R. S49 explicitly states that OWL's encoder is frozen during QA, and its depth supervision terminates before inference. S59 and S65 differentiate event chronology from continuous movement. S62 highlights the final time region without suggesting an actual prediction.

## Reproduction and checks

- `python3 scripts/visuals/part2-diagrams.py`: create the eight editable SVG sources in `public/diagrams`.
- `node scripts/visuals/render-part2-diagrams.mjs`: render eight 2× PNGs using the deck's bundled Pretendard fonts.
- Historical text/notes comparison: `tmp/visual-part2/report_changes.py` and `tmp/visual-part2/changes.json`. These are audit records, not part of asset generation.
- Both durable generators resolve fonts/assets relative to the repository. `part2-diagrams.py --output-dir DIR` and `render-part2-diagrams.mjs --input-dir DIR --output-dir DIR` support staged reproduction. The current Python generator was executed with its file writes captured in memory and reproduced all eight final SVGs byte-for-byte; no public assets were rewritten during this check. The PNG renderer retains the exact original viewport, 2× device scale, embedded Pretendard font CSS and Chromium screenshot settings.
- Contact sheet: `tmp/visual-part2/contact.jpg`; diagrams also individually inspected at full resolution. During inspection, corrected an overlapping depth icon in S49, waveform/label spacing in S45, and an unnecessary marker at the crossing in S62.
- Quantitative result-table preservation: all eleven table strings matched byte-for-byte immediately after the subtask rewrite. Root's later chart conversions, if any, are separate changes.
- Integration QA: `node scripts/visual-qa.mjs --url http://localhost:3037 --slides 38,40,45,49,50,59,62,65 --out tmp/visual-part2/slide-qa --fail-on-warnings` passed all eight slides with **0 review candidates**. Inspected the eight-slide browser contact sheet and S45 at full resolution, including both KaTeX equations. Root performs final full-deck PPTX/PDF QA.

## Text reduction

The eight original explanatory bodies contained 825 non-whitespace characters (HTML excluded). The replacement direct diagram labels contain 526 characters, a 36% reduction. Including the new brief captions gives 659 characters, a 20% reduction. TeX expressions, titles, takeaways, sources and presenter notes are excluded equally from this local measure. Most of the remaining text is short direct labels; the explanatory relations themselves are expressed as source positions, waveforms, feature weighting, a training boundary, event bars and trajectories.

최종 통합 PPTX LibreOffice 검수: 2026-09-11, 해당 Part 전체 장을 접촉 시트로 검토하고 핵심 수식·기하·그래프 장을 원본 크기로 확대했다. 추가 수정이 필요한 오류는 발견하지 못했다. `tmp/visual-pptx-qa`에 최종 렌더를 보관한다.
