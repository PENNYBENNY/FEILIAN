# Changelog

All notable changes to this compendium are recorded here.
This project uses [semantic versioning](https://semver.org/); the major version
tracks the specification revision it was built against.

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
