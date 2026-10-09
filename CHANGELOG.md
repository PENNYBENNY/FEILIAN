# Changelog

All notable changes to this page are recorded here. The revision history of the
submission itself — specification releases and the reports it has received — is
the update log in §3 of the page.

This project uses [semantic versioning](https://semver.org/); the major version
tracks the specification revision it was built against.

## [1.6.1] — 2026-10-09

Two of the figure's four views are redrawn against the specification's own diagrams, and the
live demonstration is cut back to the hash tool alone.

### Changed

- **§1 · the figure, view "One round".** The six 4×4 matrices sat in one long row
  stretched across the card, which read as a flat strip inside a stray rectangle. They are drawn
  now as the two-row serpentine of specification Figure 2.6 — *v → SC → SR* on the
  first row, the state carried round the right-hand return into the second row,
  *→ SR → AC → v′* — with the next-round loop closing on the input. Matrix
  cells go 12 px → 16 px, and each operand caption moves beside its matrix, clear of the wires.
- **§1 · the figure, view "SubColumn".** Redrawn on the four-wire layout of specification
  Figure 2.4: `a₁ b₁ a₀ b₀` as four parallel lines, one addition node each on
  `a₁` and `a₀`, the ⊕ / rotation / Σ chains on `b₁` and `b₀`, and the
  two cross-feeds that make SubColumn more than four independent S-boxes —
  `s₀ = a₁ + b₁` dropping from the `a₁` addition to the `b₀` XOR,
  `s₁ = a₀′` rising from the `a₀` addition to the `b₁` XOR. Both were
  staircases routed across the block borders before.
- **§1 · operand matrices.** All sixteen cells of an operand matrix are now visible in a
  resting colour. The rows an operand is *not* added to were near-white before, so the matrix read
  as two floating strips of four squares. The figure caption now says which rows the message
  halves, the round constants and the tweak land in.
- **§1 · step highlighting.** The active step's arrow, arrowhead and addition node light
  up together with its label, and the operand link lights with them, so the step being shown is
  unambiguous.

### Removed

- **§2 Live demonstration.** The **What this accepts** table, the **Known-answer self-test**
  table and the `core: … / engine: …` footer line are gone. The self-test itself still
  runs at load and still reports through the `self-test` pill in the demo header — the page
  shows *9/9 pass* there — so the claim is still checked on the page, only without the table
  printed under it.
- With them go their styles: `#demo .tagline`, `.t-ok` / `.t-ui` / `.t-sp` / `.t-po`,
  `#demo .kats*`, `#demo .card*`, `#demo table*`, `#demo td.m` and `#demo .demo-src`.

### Notes

- No digest, figure value, link or release package changed; `tools/verify_release.py` still
  reports 25 / 25.

## [1.6.0] — 2026-10-09

A quieter, plainer presentation: one accent colour instead of a gradient palette, the
specification tables thinned out of §1, and the page's blocks rearranged.

### Changed

- **Colour.** The palette is reduced to a single deep navy accent (`#1e3a5f`) on neutral
  greys, in place of the indigo→cyan gradient. Concretely:
  - the header band is now one flat navy (`#17293f`) — the two radial colour washes, the
    faint background grid, the animated pulse dot and the gradient-filled wordmark are gone;
  - `--grad`, which drove the gradient on the stat numerals, the progress bar, the bar
    charts and the Play button, is a flat colour, so all four are now plain;
  - the four matrix columns in the figure become a muted four-colour ramp (navy / steel /
    slate-green / ochre) instead of the bright indigo / sky / green / amber;
  - the status badges, callouts, verdict boxes, tables and the two charts are re-tinted to
    the same restrained set.
- **§1 Introduction.** Two cards are removed: **Design highlights** and **Public tweak**.
  What they covered is in the specification and, for the tweak, already labelled in the
  compression-function view of the figure (`tw = (ver, flag, t₀, t₁)`).
- **Figure proportions.** The four views no longer stretch to the full width of the card.
  Each view now has its own tight `viewBox` and a width cap — 740 / 820 / 680 / 660 px
  against a ~1022 px card interior — and is centred, so it is drawn at roughly its design
  size. One round and SubColumn, which were the flattest, gain the most from this.
- **§2 Live demonstration.** Only the hash tool is left: the section lead, the strapline in
  the demo header, the **Convention frozen in this core** card and the **Cost of one digest**
  card are all removed. What remains is the controls, the input pane, the digest pane, the
  accept/reject table and the known-answer self-test.
- **§1 ⇄ §3.** The **revision history of the submission** moves from §3 to the end of §1.
  §3's heading becomes **Artifacts** and it keeps the "which revision is which" note; the
  lead paragraph now points to §1 for the history.
- **§4 Third-party analysis.** The three review cards are laid out as **three rows in one
  column** rather than three columns: title and byline on the left, the source link aligned
  right on the same row. They collapse to a single block under 720 px.

### Notes

- No content was added or removed beyond the two §1 cards and the §2 prose. Every figure,
  value, digest and link on the page is unchanged, as is the release package.
- Still one self-contained HTML file: no new file, no new dependency, no build step.

## [1.5.2] — 2026-10-09

§1's design figure becomes four interactive views drawn from the specification's own
diagrams, and §5's performance heading is shortened.

### Changed

- **"The design in one picture" is renamed "The design in four views"** and rebuilt as a
  four-view interactive figure instead of a single static five-phase drawing. The four views —
  the compression function FEILIAN-*f*, one round of the state matrix, SubColumn, and the ARX
  S-box — are procedurally drawn from the specification's own figures: the 4×4 matrix, the
  column/round colouring and the message and tweak wires are all generated in the page,
  so nothing is a bitmap. The old title claimed a single picture the figure no longer is.
  - A row of tabs switches between the views, and each view carries its own step control
    (**previous / play / next**) with a caption that names the step it is showing: the
    compression function walks the block through the five phases and the Davies–Meyer
    feed-forward, one round walks SubColumn → ShiftRow → SubColumn → ShiftRow →
    AddConstant, SubColumn lights the two stacked ARX S-boxes and the tweaks they
    exchange, and the ARX S-box traces the add–rotate–XOR network.
  - The figure auto-starts when it scrolls into view, honours
    `prefers-reduced-motion` by holding the first step instead of animating, and the
    **Play** button runs a tour that cycles all four views.
  - The **step cadence is slowed** to a readable pace — roughly 1.7× the original interval
    per view (1050 / 1550 / 3000 ms per step for the four views) — and the cross-fade, wire
    and matrix-shift transitions are lengthened to match. The Play tour dwells 15 s on each
    view instead of 9 s.
- **§1 heading** "Performance reported in the specification (§5)" → **"Performance"**.
  The measurements it presents are unchanged; only the heading was shortened.

### Notes

- The four views are redrawn from the specification, not copied: the specification's
  figures are vector art with no embedded bitmaps, so each view is rebuilt as inline SVG
  and driven by the same JavaScript. No new external dependency, no new file — the page
  is still one self-contained HTML file.

## [1.5.1] — 2026-10-09

§5 links the erratum as a document of its own instead of pointing into the archive.

### Added

- **§5 Erratum** now opens `files/FEILIAN_Erratum.pdf` directly. The erratum is
  published on its own — byte-identical to the copy inside the release package,
  not a re-export — so the section links the PDF, prints its SHA-256 prefix and
  still offers the release package as the secondary option. Previously it told
  the reader the document existed only inside the archive.
- `tools/make_downloads.py` gains an **`ASSETS` table**: artifacts published and
  checksummed exactly like a package but deliberately given no download card, for
  documents the page links from the text. `files/` is reconciled to `PACKAGES`
  plus `ASSETS`; files are still copied verbatim and nothing is repacked.
- `tools/verify_release.py` now checks in-text document links as well —
  existence, that each one is checksummed, and that the digest printed on the
  page matches `files/SHA256SUMS.txt` — and fetches them in `--url` mode. A
  document linked outside the manifest was previously invisible to the gate.

### Fixed

- `make_downloads.py` reported "manifest markers not found" whenever the manifest
  was in fact already up to date: it could not tell that case from a genuinely
  missing marker. The two are now distinguished, and the closing line reports
  which one happened.
- The footer and NOTICE state the erratum's digest alongside the package's, since
  the erratum is now downloadable on its own.

## [1.5.0] — 2026-10-09

The submission is now distributed the way the designers issue it — one release
package per revision — and the page follows: a single download, and an erratum
chapter that points at the document instead of reprinting it.

### Changed

- **§3 Downloads.** The four separate artifacts (specification PDF, erratum PDF,
  code bundle, full archive) are retired and replaced by the **version 1.0.1
  release package**, `files/FEILIAN-v1.0.1.zip` (856 KB): specification, erratum
  and all implementations in one archive. The package is the designers' own
  artifact, published byte-for-byte as distributed and never repacked, so its
  SHA-256 is the digest of the official file. `files/` now holds only the package
  and `SHA256SUMS.txt`; `tools/make_downloads.py` no longer assembles archives.
- **§5 Erratum** is now a **pointer**, not a transcription. The erratum's own
  Table 1, Table 2 and §3 are no longer reproduced, and neither is the page's
  R1–R8 mapping table; the section states what the three pages contain, quotes
  the opening sentence, and points at the document inside the release package.
- The `citation_pdf_url` metadata is dropped, since no specification PDF is
  served as a standalone file any more.
- Cross-references updated: the downloads lead and revision caption, the
  "Read this first" note, sources [1], the footer, and README and NOTICE.

## [1.4.0] — 2026-10-09

The page is re-aimed at the submission's own material: the introduction gains the
performance the specification reports, the third-party section stops restating the
reviewers' content and links to it instead, and the parameter summary table is
dropped.

### Changed

- **Introduction.** The one-table parameter summary (*At a glance*) is removed —
  the full tables are in the specification PDF. In its place the introduction now
  carries **Chapter 5 performance**: the cycles-per-byte curve of FEILIAN-1024
  against BLAKE-64, SHA-512 and SHA-3-512 (specification Table 5.3), the software
  benchmark table (Table 5.2) and the FPGA throughput chart (Table 5.5). These are
  the specification's own reported values; nothing on the page is measured locally.
- **Third-party analysis** now only lists the three sources and links to each
  document. The reviewer quotations, the descriptive paragraphs, the R1–R8
  findings table and the ePrint component-analysis card are removed, and the page
  no longer restates the reviewers' findings.
- **§5** maps the designers' corrections onto the assessment's own R-numbers by
  reference to the assessment **[2]**, since the findings table it used to point
  at is gone.
- Cross-references updated throughout — the downloads revision table, the footer
  and the meta descriptions — and README and NOTICE brought in line.

## [1.3.2] — 2026-10-09

The designers' erratum was reissued in a revised three-page edition. The page's
transcription is brought onto that edition, and two findings whose disposition
was understated are corrected.

### Changed

- **`files/FEILIAN_Erratum.pdf` replaced.** The revised edition is 3 pp.,
  128,118 B, SHA-256 `98e74ec289636cea…`; it supersedes the two-page edition
  (126,901 B, `04969502…`) published with v1.0.1 on 8 October. The revised
  edition adds a second reference (the ngcc.dev report, accessed 2026-10-08),
  adds one further text change to its section 3, corrects the bibliography page
  it cites, and fixes typographical errors of its own. The erratum keeps the
  version number v1.0.1; it was not reissued under a new number.
- **§5 corrections.** The opening note is re-quoted in the revised edition's
  word order (`… illustrates FEILIAN fully and correctly`). The sentence
  *"the software implementation (both reference and optimized codes) are
  correct"* is **deleted by the revised edition**, so the page no longer quotes
  it as erratum text; the erratum's own section 2 wording is quoted instead. The
  bibliography location is corrected from *p. 61* to *p. 40*, which is what the
  specification itself prints on the page carrying that entry. Section 3's list
  of further text changes is now **five** items, the first being the explicit
  counter convention (t₀ the high word, t₁ the low word) — the change that
  answers the counter-word finding.
- **R7 is now recorded as partly addressed, not open.** The assessment's R7
  covers both the mode-level claims and keyed-use implementation requirements.
  v1.0.1 fixes the implementation half: the digest output and the top-level MMIO
  read path are restricted to completed hashes. The mode-level specifications
  and bounds remain open, and the page now says so on both sides.
- **R8's disposition is recorded.** The designers' stated position — that the
  shared DRNG/KAT tooling defect belongs to infrastructure used by all
  submissions and should be raised with the NGCC organising committee — is now
  stated in the findings table instead of being left implicit.
- Section 5's third change list is attributed to references **[2, 3]** rather
  than [2], following the erratum's own `[1, 2]`; Sources [3] notes that the
  erratum cites the ngcc.dev report as its own reference [2].
- README and NOTICE updated for the new erratum edition, page count and digest;
  footer release string.

## [1.3.1] — 2026-10-09

Every source the page cites is now reachable from the page, and the two
numbering schemes in the findings table are kept side by side instead of one
being folded into the other.

### Added

- **External links** — the three reviewer cards each carry a source line, and
  references [2]–[10] in **Sources** link to their documents: the technical
  assessment's repository, the ngcc.dev report, ePrint 2026/2236, HAIFA, the PGV
  and composition papers, Kelsey–Schneier, NIST SP 800-22 and RFC 5869.
  External links go from 2 to 14. The "no external dependencies" claim is
  unaffected — it concerns what the page loads at runtime, not hyperlinks.
- **A second numbering scheme** — where the ngcc.dev report covers a defect the
  assessment numbers R1–R8, its own identifier (`hash-10-1 … hash-10-5`) is
  shown beneath the row number and deep-links to that entry. The two schemes are
  kept separate; neither renumbers the other.

### Changed

- **R1 severity** — recorded as **Critical**, ngcc.dev's rating of the three
  affected RTL cores, instead of *High*; the badge gets its own solid style
  (`--crit`). The table caption now states that each severity is quoted from the
  source that raised the finding.
- `README.md` describes the dual numbering in its §4 entry.

### Removed

- The note recording a residual wording issue in the specification's description
  of the IV ("the first decimal digits of π", §2.1) is removed from the page.

## [1.3.0] — 2026-10-09

The page is presented as the submission's own overview, the update log becomes a
revision history of the submission rather than of the site, and a live
demonstration is added as a chapter of its own.

### Added

- **§2 Live demonstration** — the browser demo developed alongside the
  verification work is now part of the page. A JavaScript port of the reference
  compression function is inlined into `index.html`, wrapped in an IIFE so it
  shares no names with the page's own script; in text, hex or bit-string mode at
  512 / 768 / 1024 bits it renders digests live, and it self-tests against the
  canonical Appendix B vectors, including the two bit-level cases, before any
  user input is hashed. Its stylesheet is scoped under `#demo`, so it cannot
  reach the rest of the page.
- A **Live demo** entry in the navigation and in the hero call to action.

### Changed

- **Voice** — the page is no longer described as an *unofficial compendium*
  ("not part of the submission, not endorsed by the designers"). It now presents
  itself as the submission's overview published for the NGCC-CH hash-10 entry,
  and the findings table's status column is attributed to the submission rather
  than to a third-party transcription. `README.md` and `NOTICE.md` follow.
- **§3 Downloads** — the *Update log* card becomes the **revision history of the
  submission**: it lists the specification releases and the reports the
  submission has received (v1.0.1 + erratum on 08-10, the assessment and ePrint
  2026/2236 on 27-09, the ngcc.dev report on 23/26-09, the original v1.0 on
  30-06). The previous site-release entries (v1.0.0 / v1.1.0 / v1.2.0) and the
  intermediate 2026-09-29 posting are dropped; the section is retitled
  *Artifacts and revision history*.
- **Hero** — the animated "live · initial vector" panel is removed; the hero is
  single-column.
- **Chapter numbering** — Downloads 02→03, Third-party analysis 03→04, Erratum
  04→05, with the in-page cross-references updated to match.
- Page metadata (`<title>`, `og:` and `twitter:` titles and descriptions) mention
  the live demo.

### Fixed

- The demo's timing readout shows `n/a` instead of an infinite rate if the
  browser's clock is too coarse to measure a single compression.

## [1.2.0] — 2026-10-09

Moves the distributed artifacts to specification **v1.0.1** (8 October 2026) and
adds a section reproducing the designers' erratum.

### Changed

- `files/specification.pdf` is now **version 1.0.1**, 69 pp., SHA-256
  `2d14bcf877eb9fbd…`, replacing the 2026-09-29 revision.
- `files/FEILIAN_Erratum.pdf` is **new**: the designers' erratum recording every
  change from v1.0 to v1.0.1.
- `files/feilian-code.zip` and `files/feilian-archive.zip` are rebuilt from the
  **v1.0.1 implementations** — reference 512/768/1024, optimized SIMD
  512/768/1024, and the 1SC/2SC/4SC/8SC RTL.
- The page is now five sections — **Introduction**, **Downloads**,
  **Third-party analysis**, **Erratum**, **Sources**.

### Added

- **§4 Erratum** — the erratum reproduced in full: the four specification typo
  corrections (IV₇, the AddConstant row order, a bibliography label, and the
  Appendix B.2/B.3 vectors), the software and hardware corrections of its
  Table 2, the four further text changes made in response to the assessment, and
  a table mapping each correction onto the R1–R8 findings.
- `tools/make_downloads.py` gains `--impl` (the implementations tree to package)
  and `--erratum`, and publishes the erratum as a fourth artifact.

### Status of the findings

| Finding | Status |
|---|---|
| R1 hardware message-length binding | **Addressed in v1.0.1** — the current block length enters the compression input; block, final flag and cumulative length are transaction-consistent |
| R2 inconsistent algorithm definitions | Addressed — the v1.0.1 typo fixes remove the printed discrepancies |
| R3 Appendix B counter conventions | Addressed — B.2/B.3 reprinted under true message-length counts |
| R4 C bit-input and length contracts | Addressed in v1.0.1 — unused low bits masked, both additions guarded, the length cast checked |
| R5 silent allocation failure | Addressed in v1.0.1 — failure propagated through the return code; a mismatched digest length now returns an error |
| R6 mode proof and margins | Open — partly clarified (notation unified, §4.3.1) |
| R7 MAC/KDF/XOF scope | Open — partly clarified (encoding and XOF footnotes, §6.2–6.3) |
| R8 shared DRNG and KAT driver | Reported, not applied — the erratum does not touch the shared tooling |

The erratum's own summary is that **the design does not change**: v1.0.1 corrects
typography and refines the implementations, and the compression function, IV,
round constants and counter conventions are untouched.

## [1.1.0] — 2026-10-09

Restructured around the three things a reader needs: an introduction to the
design, the artifacts, and the independent third-party analyses. Tracks the same
specification revision, **2026-09-29 (70 pp.)**.

### Changed

- The page is now four sections — **Introduction**, **Downloads**,
  **Third-party analysis**, **Sources** — replacing the previous eleven.
- The detailed specification material (parameter tables, per-round definitions,
  IV and round constants, Appendix B vectors, Chapter 5 performance, Chapter 6
  applications and the Chapter 4 claims) has been **removed from the page** and
  left to the specification PDF. The introduction keeps a one-table parameter
  summary and a single interactive figure.
- **Downloads** gains a revision history: what was published and when, and an
  explicit table separating the revision the third-party assessment examined
  (2026-06-30, 68 pp.) from the revision distributed here (2026-09-29, 70 pp.).
- **Third-party analysis** is new. It presents the technical assessment
  (findings R1–R8) with a status column for each finding against the material
  distributed here, the ngcc.dev report, and the component result of
  ePrint 2026/2236.
- `tools/verify_release.py` scopes its navigation check to the `<nav>` block —
  in-text cross-references were being counted as navigation items — and adds a
  check that every in-page anchor resolves.

### Status of the findings

| Finding | Status |
|---|---|
| R1 hardware message-length binding | Open — the RTL cores are unmodified, published as filed |
| R2 inconsistent algorithm definitions | Addressed in the 2026-09-29 revision |
| R3 Appendix B counter conventions | Addressed — reprinted under true message-length counts |
| R4 C bit-input and length contracts | Addressed — six C variants, 12 files |
| R5 silent allocation failure | Addressed — failure propagated through the return code |
| R6 mode proof and margins | Open — text-level |
| R7 MAC/KDF/XOF scope | Open — text-level |
| R8 shared DRNG and KAT driver | Reported, not applied — unmodified submission infrastructure |

No full-round cryptanalytic break is claimed by any of the three sources, or here.

## [1.0.0] — 2026-10-08

First public release. Tracks the submitted specification, **revision
2026-09-29 (70 pp.)**.

### Contents

- **Sections 1–11** — overview; specification parameters; the five-phase
  compression pipeline (interactive); IV and round constants; canonical
  Appendix B test vectors for 512/768/1024; the security argument of Chapter 4;
  the reported performance of Chapter 5; the applications of Chapter 6;
  the component-level linear-structure analysis of ePrint 2026/2236; downloads;
  references.
- **Downloadable artifacts** — `files/specification.pdf`,
  `files/feilian-code.zip` (reference and optimized implementations, C and
  SystemVerilog), `files/feilian-archive.zip` (implementations, KAT vectors,
  Appendix B material, analysis notes, tooling) and `files/SHA256SUMS.txt`.
- **Repository tooling** — `tools/make_downloads.py` rebuilds the artifacts and
  rewrites the page's manifest; `tools/verify_release.py` checks the checksums,
  the page's links and structure, and optionally the deployed bytes.

### Notes on the transcription

- Values are transcribed from the specification as printed. All sixteen IV words
  and the four round constants were independently recomputed — from π by exact
  integer arithmetic, and from √2, √3, √5 and √7 to 64 fractional bits — and
  agree word for word with the printed values, including
  `IV₇ = 0x3F84D5B5B5470917`.
- The six digests in the test-vector table were string-compared against
  Appendix B of the specification and match exactly.
- Performance figures are the specification's own reported values (Chapter 5).
  Nothing in this repository was benchmarked, synthesised or otherwise measured
  locally; no machine-specific numbers appear anywhere on the page.

### Licensing

- Compendium text and figures: CC BY 4.0 — see `LICENSE`.
- Submission material under `files/`: redistributed as filed, all rights with
  the authors — see `NOTICE.md`.
