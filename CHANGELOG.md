# Changelog

All notable changes to this compendium are recorded here.
This project uses [semantic versioning](https://semver.org/); the major version
tracks the specification revision it was built against.

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
