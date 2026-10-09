# Changelog

All notable changes to this page are recorded here. The revision history of the
submission itself — specification releases and the reports it has received — is
the update log in §3 of the page.

This project uses [semantic versioning](https://semver.org/); the major version
tracks the specification revision it was built against.

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
