# Part 1 asset and evidence record

Created 2026-09-11. Applies to slides/part1.md S01–S37. Existing assets remain documented in ASSET_SOURCES.md. Native result tables are editable HTML. Diagram labels and captions are native text. PDF-derived SVG labels may be outlines, not editable text.

| Asset | Figure/version | Original source | Treatment | SHA-256 |
|---|---|---|---|---|
| `public/research/p1-agg-path.svg` | AGG-RL, ICLR 2026, Fig. 1(a) | https://proceedings.iclr.cc/paper_files/paper/2026/file/ee860a9fa65a55a335754c557a5211de-Paper-Conference.pdf | Existing native PDF extraction agg-rl-fig1.svg; viewBox 0 0 183 125. Original paths/glyph outlines retained. Authors retain copyright; scholarly attribution. | `f26a8d8fea0a23d09cade37096e4f1a473457f781373bf1089cb6838c48d2917` |
| `public/research/p1-sfd-results.svg` | SFD arXiv:2508.20914v1, Fig. 2 | https://arxiv.org/html/2508.20914v1/doa_performance_vary_hours.svg | Original SVG downloaded unchanged. arXiv non-exclusive license / IEEE publication. | `8b0528002898924dfd7ce5fcad7462505ddde110e4687dbae18eaf420e70d3d4` |
| `public/research/p1-sfd-1h.svg` | SFD Fig. 2, 1h panel | https://arxiv.org/html/2508.20914v1/doa_performance_vary_hours.svg | Original 1h panel viewBox 158 0 111 178; original full legend viewBox 0 177 426 50. Paths/glyphs reused in a 426×280 SVG. No curve values inferred. y-axis unit supplied by editable slide caption. Other panel curves excluded. | `27149bdaaf3dfc2c8831bc22ae8d47396aa7944f0d871a8629455d27ea683015` |
| `public/research/p1-lam-method.png` | LAM arXiv:2507.07066v1, Fig. 2 | https://arxiv.org/html/2507.07066v1/LAM_architecture_v3.png | Original PNG downloaded unchanged; no screenshot. | `274315acf0eaec7dd9d7ee3eb41b26e2a53521a32aa76fe327f08c4715b1cfa1` |
| `public/research/p1-lam-threshold.svg` | LAM arXiv:2507.07066v1, Fig. 3 | https://arxiv.org/html/2507.07066v1/fix.svg | Original SVG unchanged. Evaluation solid lines are the selected evidence. Dashed validation, green threshold and original legend retained. | `97e2fb2a92497f0475eff141437d95739715e4c6e2f01c45162845f543d0d7a2` |
| `public/research/p1-gram-results.svg` | GRAM arXiv:2506.00934v5, Fig. 3 | https://arxiv.org/html/2506.00934v5/figure3.svg | Original SVG downloaded unchanged. CC BY-NC-SA 4.0. | `29c6d175ed3a1598ce1368e235cb0b59cf7310b2bb13e7ef5928588a1b33ddce` |
| `public/research/p1-gram-doa.svg` | GRAM Fig. 3(A), DOA | https://arxiv.org/html/2506.00934v5/figure3.svg | Original DOA panel viewBox 0 0 142 96 plus original full legend viewBox 301 0 79 46. Paths/glyphs reused in 226×96 SVG. Median/IQR/whiskers preserved; no inferred values or mean bars. CC BY-NC-SA 4.0; crop/rearrangement disclosed. | `25f1ff0aed0bb2188f905daba5bcbcf75b6b3de0161169443827880ba83a1763` |
| `public/research/p1-selecttsl-problem.png` | SelectTSL arXiv:2607.02343v1, Fig. 1 | https://arxiv.org/html/2607.02343v1/TSEDOAnet-intro-v2.png | Original PNG downloaded unchanged. CC BY 4.0. | `75b1b1b260310f02f7d803b9d8dcef870f2d7bbe71f1a283f061c3eb7702c120` |

## Source checks

- Neural-SRP v1 Table I: Recorded4 SRP 1.19 m and NeuralSRP+ 0.77 m checked.
- MC-SimCLR v1 Table 1: LP Random 23.6% / 83.1°, w/o DA 33.0% / 13.2° checked.
- CCSR v2 Table III: 8-room scratch 0.40 samples versus fine-tune 0.28; C50 counterexample 1.14→1.21 dB checked. §IV-A masking: same-frame mask to spatial branch and complementary masks to spectral branch checked.
- SFD v1 Fig. 2: selected 1h panel and entire legend retained. Table2 1h/10h caption/text conflict remains, so not used.
- LAM v1 Fig. 3: same model threshold tradeoff; solid test and dashed validation distinguished.
- GRAM v5 Fig. 3: DOA boxplots retain median/IQR and original input-model legend.
- AT2SELD v1 Table12: Stage3 no-stitch0.708 / late-only0.624 checked with strong-dropout context.
- ELSA arXivv1 vs NeurIPS2024 published PDF Table2 p7: Direction4-class92.0%,92.8%,35.8% identical. Version gate resolved for selected result.
- SALM v2 Table1: sClotho selected same-model rows9.1/9.6/1.8 and10.5/10.4/1.6 checked.
- SelectTSL v1 TableVI Full and A1:0.98°/0.96 and2.10°/0.83 checked; F1 uses0–1. TableIII inconsistent P/R/MOTA* rows remain unused.

## Scientific boundaries

Concept slides show requested outputs, not empirical successes. The phase animation is an explanatory reconstruction. Full fine-tuning, frozen-encoder probing, and prompt classification remain distinct. No cross-paper metric leaderboard or chart-estimated numerical values was created.

## PPTX 호환성

`p1-gram-doa.svg`의 중첩 clip/use 구조가 LibreOffice에서 다른 패널과 검은 배경으로 표시되어, PPTX에 한해 Chromium으로 원본 SVG를 그대로 2260×960 렌더한 `p1-gram-doa-compat.png`를 사용한다. 재작성이나 데이터 변경은 없으며 Slidev·PDF는 SVG를 유지한다.
