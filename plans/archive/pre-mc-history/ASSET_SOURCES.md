# Research figure sources

The deck uses paper- and dataset-native figures at their original aspect ratio unless noted. Each slide also carries a visible attribution line and a `[Sources]` block in its speaker notes. Earlier revision sections preserve historical construction records and object counts; the localization-revision section and current mappings record the active assets. Earlier QA/object counts are historical.

| Local asset | Source figure | Official source | Reuse status in this deck |
|---|---|---|---|
| `iiplab-logo.png` | IIP Lab official wordmark | https://iip.sogang.ac.kr/layouts/iiplab/top-logo.png | Official identity asset; scaled only |
| `soundspaces2-concept.png` | SoundSpaces 2.0 concept | https://vision.cs.utexas.edu/projects/soundspaces2/concept.png | CC BY 4.0; retained from an earlier cover, not used in the current typographic cover |
| `princeton-hrtf-setup.png` | 3D3A HRTF measurement setup | https://3d3a.princeton.edu/3d3a-lab/3d3a-hrtf-database | CC BY 4.0; scaled only |
| `owl-bidepth.png` | OWL / BiDepth Fig. 2 | https://arxiv.org/html/2509.26140v1/figure/simulation_setup_2.png | CC BY 4.0; scaled only |
| `neural-srp-output.png` | Neural-SRP Fig. 1 | https://arxiv.org/html/2403.09455v1/outputs.png | CC BY 4.0; scaled only |
| `neural-srp-architecture.svg` | Neural-SRP Fig. 3 | https://arxiv.org/html/2403.09455v1/neural-srp-architecture.svg | CC BY 4.0; scaled only |
| `locata-dicit.svg` | LOCATA Fig. 1(b), DICIT array geometry | https://doi.org/10.1109/TASLP.2020.2990485 | Paper-native vector crop used in the design specimen; scaled only, scholarly attribution retained |
| `agg-rl-overall.png` | AGG-RL Fig. 2 / project overview | https://github.com/BaekMS/Audio-Geometry-Grid_Representation-Learning | No explicit repository figure license; scholarly attribution and rights warning retained |
| `agg-rl-fig1.svg` | AGG-RL Fig. 1(a–b), published PDF p. 2 | https://proceedings.iclr.cc/paper_files/paper/2026/file/ee860a9fa65a55a335754c557a5211de-Paper-Conference.pdf | Native vector extraction for the design specimen. Authors retain copyright; no blanket reuse permission inferred. Crop retains both panels, axes, units, and panel captions. Main figure caption is outside the crop; the specimen provides a Korean explanation and attribution. |
| `animations/tdoa-ipd-wrap.mp4`, `.webm`, `-start.png`, `-poster.png` | Manim explanatory reconstruction of path difference, TDoA and wrapped IPD | `manim/scenes.md`, `manim/tdoa_ipd_wrap.py`; concept checked against AGG-RL Fig. 1(a–b) | Original code-generated visual for the design specimen, not a paper figure. MP4 and WebM carry the same silent animation for browser compatibility. It uses the paper's physical example as scholarly context and is labeled as an explanatory reconstruction. The start and final-frame posters are extracted from the rendered video. |
| `agg-rl-spectrum.png` | AGG-RL 4-channel / 2-speaker example | https://raw.githubusercontent.com/BaekMS/Audio-Geometry-Grid_Representation-Learning/main/spectrum_plots/4ch_0.png | No explicit repository figure license; scholarly attribution and rights warning retained |
| `mc-simclr-overview.png` | MC-SimCLR Fig. 1 | https://arxiv.org/html/2309.15938v1/mc-simclr-wider.png | CC BY 4.0; scaled only |
| `ccsr-task.png` | CCSR Fig. 1 | https://arxiv.org/html/2312.00476v2/meth_task.png | arXiv non-exclusive license; scholarly attribution retained |
| `sfd-framework.svg` | SFD Fig. 1 | https://arxiv.org/html/2508.20914v1/neural_fe_and_finetune.drawio.svg | arXiv non-exclusive / IEEE publication; scholarly attribution retained |
| `gram-overview.png` | GRAM Fig. 1 | https://arxiv.org/html/2506.00934v5/figure1.png | CC BY-NC-SA 4.0; scaled only |
| `bat-architecture.png` | BAT Fig. 1 | https://arxiv.org/html/2402.01591v4/architecture.png | CC BY 4.0; scaled only |
| `dspast-architecture.png` | DSpAST repository architecture | https://github.com/wilkinghoff/DSpAST/blob/main/dspast_illustration.png | CC BY-NC 4.0; scaled only |
| `owl-architecture.png` | OWL Fig. 4 | https://arxiv.org/html/2509.26140v1/owl_main_arch.png | CC BY 4.0; scaled only |
| `phasecoder-architecture.png` | PhaseCoder Fig. 3 | https://arxiv.org/html/2601.21124v2/model_architecture_v2.png | CC BY 4.0; scaled only |
| `sarl-summary.svg` | SARL Fig. 2 | https://arxiv.org/html/2606.05544v2/fig2.svg | CC BY 4.0; scaled only |
| `sarl-sensitivity.svg` | SARL Fig. 3 | https://arxiv.org/html/2606.05544v2/fig3.svg | CC BY 4.0; scaled only |
| `bmld-deficit.svg` | BMLD Fig. 1 | https://arxiv.org/html/2606.14820v1/fig1_absolute_deficit.svg | CC BY 4.0; scaled only |
| `bmld-ablation.png` | BMLD Fig. 3 | https://arxiv.org/html/2606.14820v1/fig4_ablation.png | CC BY 4.0; scaled only |

The UDL Book assets were reviewed but not inserted: its CC BY-NC-ND 4.0 figures must remain unmodified, and the available generic Transformer diagrams do not describe these spatial-audio systems as precisely as their paper-native figures.

## Native PDF extraction

Use original figure files when available. For PDF-native vectors, preserve paths with `pdftocairo -svg`. For embedded pixel images, prefer `pdfimages -all` rather than a screenshot. Browser screenshots are visual QA artifacts, not final figure sources.

`agg-rl-fig1.svg` contains 150 paths and 173 glyph references, with no embedded raster image. Text is outlined, so enlargement is sharp but the original labels are not directly editable text. Presentation captions and result tables remain editable in Slidev. Extraction provenance, input/output SHA-256, page, and crop bounds are recorded in `public/research/agg-rl-fig1.source.json`.

To reproduce (Poppler required; supply the official PDF at the specified local path):

```bash
node scripts/extract-pdf-figure.mjs \
  --pdf tmp/agg-design-source.pdf --page 2 --box 106,465,398,125 \
  --out public/research/agg-rl-fig1.svg \
  --source https://proceedings.iclr.cc/paper_files/paper/2026/file/ee860a9fa65a55a335754c557a5211de-Paper-Conference.pdf
```

The helper protects existing outputs unless `--force` is explicitly supplied. The source PDF is read only. Crop coordinates use PDF points from the page's top-left corner.

## Typeface

`public/fonts/Pretendard-{Regular,Medium,SemiBold,Bold}.woff2` are unmodified static Pretendard v1.3.9 faces from [the official release](https://github.com/orioncactus/pretendard/tree/v1.3.9/packages/pretendard/dist/web/static/woff2). Copyright Kil Hyung-jin. SIL Open Font License 1.1 is included as `public/fonts/OFL-Pretendard.txt`. No external font service is needed for slide text. Static faces preserve the selected typeface while avoiding variable-font Type 3 glyph warnings in the PDF exporter.

## Final 78-slide figure refinements (2026-09-11)

Original paper panels were cropped or repositioned for readable projection. No numerical result, curve or source color was changed. Native slide captions and tables remain editable in PPTX.

| Asset | Source and exact change |
| --- | --- |
| `neural-srp-response-pair.svg` | Original `neural-srp-output.png` (600×600). Top panel `(0,0,570,276)` and lower panel `(0,277,570,587)` placed side by side; shared original x-axis `(65,535,505,583)` duplicated below the left panel. Colorbars and values preserved. |
| `sfd-1h-plot.svg` | Original vector `p1-sfd-results.svg`, viewport `(148,19,129,159)`, only the 1h panel. All curves retained. Seven original legend labels/colors separately typeset in the slide. |
| `gram-scene.png` | Original `gram-overview.png`, crop `(0,0,300,275)`: Fig. 1(A) scene only. |
| `sciphi-core.png` | Original `p2-sciphi-v1-fig1.png`, crop `(0,83,570,243)`: encoder/projector/LLM path. |
| `spatialomni-core.png` | Original `p2-spatialomni-v2-path.png`, crop `(60,218,770,780)`: core encoder/projector/LLM path, with optional visual branch identified in caption. |

Coordinates for raster crops are `(left,top,right,bottom)` in source pixels. SVG viewport uses `(x,y,width,height)`. Additional source and extraction records: [Part 1](plans/ASSETS_PART1.md), [Part 2](plans/ASSETS_PART2.md), [Part 3](plans/ASSETS_PART3.md).

The final STAR and WearVox slides use the original-PNG panel crops `star-caption-panel.png` and `wearvox-side-talk-panel.png` to avoid neighboring panel fragments and SVG mask incompatibility. Their source versions, exact crop bounds and hashes are recorded in [Part 3](plans/ASSETS_PART3.md). The extracted SVGs remain as provenance artifacts.

For PPTX only, `p1-gram-doa-compat.png` is a 2260×960 Chromium rendering of the exact `p1-gram-doa.svg` paper-panel composition on white. LibreOffice misinterprets the nested SVG clipping/use structure. The PNG preserves the chart and legend without changing data; Slidev and PDF retain the vector SVG. `scripts/export-editable-pptx.mjs` selects this compatibility asset explicitly.

## Light theme and equation revision (2026-09-11)

- `public/iiplab-mark.png`: unchanged symbol from the existing official `iiplab-logo.png` (307×56), cropped to pixel box `(0,0,49,56)`. The white wordmark is replaced by editable dark lab-name text for the light cover. Official source: https://iip.sogang.ac.kr/layouts/iiplab/top-logo.png.
- `public/cover-wave-light.svg`: presenter-authored decorative vector, adapted from `cover-wave.svg` with transparent background and the shared blue/teal palette. It contains no paper data.
- `public/animations/tdoa-ipd-wrap.{mp4,webm}` and both posters: regenerated from `manim/tdoa_ipd_wrap.py`, light `#f6f8fa` background, MathTex equations, original frame count and timing.
- `components/MathInline.vue`: KaTeX 0.18.4, HTML+MathML in Slidev/PDF. The PPTX export includes 29 transparent equation PNGs captured at 2× canvas resolution; native text and all 31 tables remain editable. These equations typeset the existing slide notation rather than adding experimental content.


## 2026-09-11 teaching diagrams and exact-data charts

The visual revision adds 30 original concept diagrams and 23 exact-data charts under `public/diagrams/`. These are presenter-authored reconstructions, not copied lecture artwork or new experimental measurements. The source-paper figures that remain in the deck keep their original axes, legends and citations. Long explanations and original table rows are preserved in speaker notes.

- Goal geometry: `spatial-goal-3d.svg/png`, generated by `scripts/visuals/spatial-goal.py`. Coordinates follow [MathWorks: Spherical Coordinates](https://www.mathworks.com/help/phased/ug/spherical-coordinates.html): origin at microphone-pair midpoint, microphones on x, azimuth from +x toward +y, elevation from xy toward +z, radial distance from origin. The two-channel picture defines a target coordinate system and does not imply that one TDoA uniquely identifies a 3D point.
- Part 1: 16 original diagrams; see [teaching references, sources and reconstruction record](plans/VISUAL_PART1.md).
- Part 2: 8 original diagrams; see [source mapping and reconstruction record](plans/VISUAL_PART2.md).
- Part 3: 5 original diagrams; see [SARL/BMLD and MIT auditory demonstration references](plans/VISUAL_PART3.md).
- Quantitative charts: `result-11.svg/png` through selected slides ending at `result-76.svg/png`, 23 pairs in total. Generated by `scripts/visuals/result-charts.py` from [exact table data](plans/RESULTS_VISUAL_DATA.json); all 99 numeric entries including significance stars are unchanged. Method names, units and protocol restrictions belong to the same cited slide as before. Original O46 (current S66) transposes the PA rows into comparison panels; original O76 (current S80) retains 50% unmasking plus 25% reversal and does not label this as accuracy. These asset suffixes are original slide IDs, not current page numbers.

[Visual revision overview and reproduction commands](plans/VISUAL_REVISION.md) records delivery formats and validation.

## Retained causal assets in the localization revision (2026-09-11)

The current deck has **47 main slides and 33 evidence-appendix slides**. Current page numbers below come from [CAUSAL_DECK_ORDER.json](plans/CAUSAL_DECK_ORDER.json). `Oxx` means the original pre-restructure slide in [the preserved deck](slides/archive/visual-before-causal.md); `Sxx` means the current displayed page. Existing filenames such as `result-46` and `p2-s40-*` retain **original O-numbers**, not current page numbers. The full mapping is in [EVIDENCE_LEDGER.md](plans/EVIDENCE_LEDGER.md).

Twelve of the previous thirteen causal assets remain active: **11 educational diagrams and one chart of three reported values**. `causal-roadmap` is preserved but inactive. The four new GCC/SRP calculated diagrams are listed separately below. They were drawn with scientific plotting/vector primitives; no paper artwork is represented as newly measured evidence. Each basename below has both `.svg` and `.png` under `public/diagrams/`. The design canvas is 1136×404 and the PNG is 2272×808. Math and text are outlined in SVG; the surrounding slide title, takeaway and attribution remain separate slide content. Background `#f6f8fa`, ink `#142233`, blue `#1f5fae`, teal `#008b9a`, and caution orange `#a95018` follow the light design system.

| Current page / asset basename | Primary conceptual or numerical source | What was reconstructed; scope | Durable generator |
| --- | --- | --- | --- |
| S11 · `causal-srp-neural` | [Neural-SRP v1](https://arxiv.org/html/2403.09455v1), [AGG-RL published paper](https://proceedings.iclr.cc/paper_files/paper/2026/file/ee860a9fa65a55a335754c557a5211de-Paper-Conference.pdf), [IPDnet](https://arxiv.org/html/2405.07021v1) | Analytic steering/aggregation versus a learned pair response. Curves are illustrative. Neural-SRP's original 2D location output is distinguished from AGG-RL's DOA reimplementation. | `scripts/visuals/causal-signal.py` |
| S14 · `causal-readout-to-encoder` | [MC-SimCLR v1](https://arxiv.org/html/2309.15938v1), [CCSR v2](https://arxiv.org/html/2312.00476v2), [GRAM v5](https://arxiv.org/html/2506.00934v5), [SFD v1](https://arxiv.org/html/2508.20914v1) | A task output versus reusable latent information. Synthetic grids and readouts are explanatory; no representation accessibility is inferred from the drawing itself. | `scripts/visuals/causal-signal.py` |
| S16 · `causal-encoder-criteria` | [SALM v2](https://arxiv.org/html/2507.16724v2), [SARL v2](https://arxiv.org/html/2606.05544v2), [probing-method review](https://aclanthology.org/2022.cl-1.7/) | Same event under location/time/environment changes and the attributes to inspect. Proposed criteria, not measured predictions or proof of complete factorization. | `scripts/visuals/causal-evaluation.py` |
| S17 · `causal-encoder-objectives` | [MC-SimCLR v1](https://arxiv.org/html/2309.15938v1), [CCSR v2](https://arxiv.org/html/2312.00476v2), [LAM v1](https://arxiv.org/html/2507.07066v1), [SFD v1](https://arxiv.org/html/2508.20914v1) | Crop consistency, complementary masked STFT recovery, physical covariance reconstruction, and clean spatial-feature prediction. Generated covariance/waveforms are illustrative. LAM uses the physical decoder; SFD clean features are computed targets. | `scripts/visuals/causal-signal.py` |
| S15 · `causal-audio-llm-contract` | [Spatial-Omni v2 §3](https://arxiv.org/html/2606.10738v2), [PhaseCoder v2 §3.3](https://arxiv.org/html/2601.21124v2) | X→E→H→P→Z plus question embeddings→LLM. Continuous audio embeddings augment the input sequence; vocabulary growth and hidden-width growth are separate concepts. | `scripts/visuals/causal-llm.py` |
| S25 · `causal-token-bottleneck` | [ST-AudioLM v1 §4.1–4.2](https://arxiv.org/html/2606.14141v1), [TWNM v3 §4.1](https://arxiv.org/html/2601.02954v3) | Authored counterexample: reversed source trajectories have identical plain time means. ±60°/0° are teaching values, not paper data. The limitation applies to order-free averaging; learned global tokens may encode order. Actual tokens are continuous, not the displayed attribute table. TWNM's dense LLM input is distinguished from source-slot supervision. | `scripts/visuals/causal-llm.py` |
| S30 · `causal-adapter-training` | [Spatial-Omni v2 training stages](https://arxiv.org/html/2606.10738v2), [Sci-Phi v1 §3](https://arxiv.org/html/2510.05542v1) | Encoder pretraining, connector alignment, and decoder adaptation. SO and Sci-Phi are separate examples with different freeze/train schedules; LoRA is a common choice, not a universal requirement. | `scripts/visuals/causal-llm.py` |
| S33 · `causal-lora-reading` | [LoRA v2 §4.1](https://arxiv.org/abs/2106.09685v2), [BAT v4](https://arxiv.org/html/2402.01591v4), [BAT official implementation](https://github.com/X-LANCE/SLAM-LLM/tree/main/examples/seld_spatialsoundqa), [BLIP-2](https://arxiv.org/abs/2301.12597) | Frozen W0 plus low-rank BA, with α/r scaling, inside the LLM. Vocabulary bars are illustrative. BAT paper's LLaMA-Adapter V2 and released Q-Former+LoRA implementation are explicitly distinguished in notes. | `scripts/visuals/causal-llm.py` |
| S35 · `causal-module-evidence` | [TWNM v3 Appendix G.1 Table15](https://arxiv.org/html/2601.02954v3) | **Reported-data chart**, not a concept diagram: P0 Single MLP 39.20, P1 Dual Tower 46.40, P2 Dense Hybrid 52.10, all reported Overall(%). Audit and consistency limits below apply. | `scripts/visuals/causal-spine.py` |
| S41 · `causal-evaluation-map` | [SARL v2](https://arxiv.org/html/2606.05544v2), [BMLD v1](https://arxiv.org/html/2606.14820v1), [BAT v4](https://arxiv.org/html/2402.01591v4), [Spatial-Omni v2](https://arxiv.org/html/2606.10738v2), [causal analysis of representations](https://aclanthology.org/2021.tacl-1.10/) | Distinguishes fixed-representation readouts, token interventions, and answer dependence on audio. Tests drawn across boundaries are proposed analyses, not jointly demonstrated sufficient conditions in one system. | `scripts/visuals/causal-evaluation.py` |
| S46 · `causal-synthesis` | [GRAM v5](https://arxiv.org/html/2506.00934v5), [Sci-Phi v1](https://arxiv.org/html/2510.05542v1), [SARL v2](https://arxiv.org/html/2606.05544v2), [BMLD v1](https://arxiv.org/html/2606.14820v1), [Spatial-Omni v2](https://arxiv.org/html/2606.10738v2), [ST-AudioLM v1](https://arxiv.org/html/2606.14141v1), [BAT v4](https://arxiv.org/html/2402.01591v4) | Synthesizes preservation in E, transmission by P, and use by LLM. Evidence from one module is not treated as proof about another. | `scripts/visuals/causal-spine.py` |
| S47 · `causal-closing-tests` | [SARL v2](https://arxiv.org/html/2606.05544v2), [BMLD v1](https://arxiv.org/html/2606.14820v1), [Spatial-Omni v2](https://arxiv.org/html/2606.10738v2), [BAT v4](https://arxiv.org/html/2402.01591v4), [causal analysis of representations](https://aclanthology.org/2021.tacl-1.10/) | Unexecuted proposed test: move the same alarm while preserving another source, compare H/Z readouts and answers. Two microphones lie on x with midpoint origin, azimuth/elevation/radius defined geometrically. One TDoA is not claimed to uniquely identify all 3D coordinates. | `scripts/visuals/causal-evaluation.py` |

The corresponding files in `slides/bridges/` retain the complete source lists, narrated definitions and interpretation limits. S48 is a new appendix-index slide with no additional causal image. The scope of the nine audio–LLM papers, including BAT paper/code differences and unresolved implementation details, is recorded in [CAUSAL_LLM_MODULES.md](plans/CAUSAL_LLM_MODULES.md).

Reproduction uses the project's existing Python environment with numpy/matplotlib and the local Pretendard faces. `causal-signal.py` embeds the repository's bundled WOFF2 faces via fontTools; the other generators use `~/Library/Fonts/Pretendard-{Regular,SemiBold}.otf`. These commands regenerate only their named assets:

```bash
.venv/bin/python scripts/visuals/causal-signal.py
.venv/bin/python scripts/visuals/causal-llm.py
.venv/bin/python scripts/visuals/causal-evaluation.py
.venv/bin/python scripts/visuals/causal-spine.py
```

### Existing99 values and the three newly added TWNM values

The existing 23 result charts retain **all 99 original values** (including the existing significance notation). Their canonical input is [RESULTS_VISUAL_DATA.json](plans/RESULTS_VISUAL_DATA.json); their renderer remains `scripts/visuals/result-charts.py`. The new `causal-module-evidence` chart adds exactly these **three reported values**, independently of that 99-value set:

| Source row, verbatim identifier | Reported Overall (%) | Current page |
| --- | ---: | --- |
| P0: Single MLP | 39.20 | S35 |
| P1: Dual Tower | 46.40 | S35 |
| P2: Dense Hybrid | 52.10 | S35 |

[Source: TWNM v3 Appendix G.1, Table15](https://arxiv.org/html/2601.02954v3). This is a **pre-SAPO semantic-answer-judge audit**, distinct from the exact-MCQA SFT/SAPO comparison in Table5/current S34. The judge protocol in §F.6 uses Gemini 3 Flash with question, options, gold-option text and generated answer; it does not provide audio or RTSD to the judge. The paper calls Table15 a projector ablation but does not explicitly establish identical encoder/LLM checkpoints, training budgets and seeds across P0/P1/P2. The figure therefore compares reported connector-design results without claiming a fully matched single-module causal intervention.

The caption describes Overall as counting the 1,000 ASA items. However, weighting its level-wise percentages by the 385/279/336 level counts reported in App.D.3 yields 39.4523/46.7759/52.4109, which differ from the reported 39.20/46.40/52.10. The figure retains the **reported Overall column**, does not reconstruct correct-item counts or silently repair the paper, and does not call the column an unweighted mean of the three levels. Full details are in [CAUSAL_LLM_MODULES.md §7](plans/CAUSAL_LLM_MODULES.md). No summary score pools these three values with the original 99.


## Localization foundation: four calculated teaching diagrams

Current S07–S10 make the coordinate-finding calculation explicit before Neural-SRP or LLM integration. The assets below are presenter-authored **synthetic calculation examples**, not paper results, field recordings or neural-model predictions. Source metadata and arrays preserve generation conditions. All four use the shared light palette and separately typeset equations.

| Current page / asset | Computation and interpretation | Generator / source data |
| --- | --- | --- |
| S07 · `gcc-phat.svg/png` | Known delayed synthetic channel signals → cross spectrum → PHAT normalization → actual inverse-transform lag curve. The peak is a time delay, not a coordinate. Channel order fixes the delay sign. | `scripts/visuals/gcc-phat.py`; `public/diagrams/gcc-phat.source.json`; shared `localization-simulation.npz` |
| S08 · `localization-tdoa-locus.svg/png` | The shared planar microphone geometry maps one delay to multiple positions. The displayed locus is a distance-difference constraint, not a unique 3D solution. | `scripts/visuals/localization-geometry.py`; matching `.source.json` |
| S09 · `localization-srp-candidate.svg/png` | Candidate-to-microphone distances give an expected delay; the actual synthetic GCC curve is queried at that delay to score the candidate. The full curve, not only its peak, is used. | Same generator; matching `.source.json`; `public/diagrams/localization-simulation.npz` |
| S10 · `localization-srp-sum.svg/png` | Three microphone pairs' candidate maps are computed from the same scene and summed; argmax selects a candidate within the stated planar grid. | Same generator; matching `.source.json`; shared `.npz` |

All asset basenames reside in `public/diagrams/`. S07–S10 all share one geometry and synthetic scene from `localization-simulation.npz`; the GCC generator reads that shared source. The diagrams do not claim to show a field recording. Intro τ=t₂−t₁ and subsequent τᵢⱼ=tᵢ−tⱼ are explicitly related in the notes so channel ordering, geometric distance differences and curve lookup remain consistent.

```bash
.venv/bin/python scripts/visuals/gcc-phat.py
.venv/bin/python scripts/visuals/localization-geometry.py
```

The Neural-SRP comparison at S11 preserves the original learned pair-response versus fixed sum/argmax distinction. AGG-RL appears at appendix S49–S51. The active intro Manim remains S02–S06 with five light-theme clips; S07 is now the GCC-PHAT diagram, not the retired causal roadmap or preserved intro s07 clip. Current package/render verification belongs to `output/qa/localization/` and `output/manifest.json`; old render counts above are not verification of the 80-slide revision.
