# FEILIAN — Submission Overview

**The overview page for FEILIAN**, the hash function submitted to the NGCC-CH programme of the
Institute of Commercial Cryptography Standards (ICCS), China, under the designation `hash-10`.

**Live site — <https://pennybenny.github.io/FEILIAN/>**

The page is organised as five chapters: an **introduction** to the design, a **live demonstration**
that computes digests in the browser, the **artifacts** — downloadable and checksummed, with the
revision history of the submission — the **independent third-party analyses**, each finding listed
with its current status, and the **erratum** in which the designers record every change from v1.0 to
v1.0.1. Detailed specification tables are deliberately kept out of the page and left to the PDF; the
page carries a one-screen summary and a single interactive figure.

The third-party material presented is the technical assessment by Mounir Idrassi (findings R1–R8),
the ngcc.dev report by Markku-Juhani O. Saarinen, and the component-level analysis in Cryptology
ePrint 2026/2236. None of them establishes a full-round cryptanalytic break, and the page states
that boundary as plainly as they do.

It is one HTML file with **no build step, no framework and no external dependencies**. Every figure
is inline SVG or plain JavaScript, and the live demo's hash core is inlined into the same file, so
the page renders and the demo runs identically offline, from `file://`, and from any static host.

---

## Contents

| § | Section | What it covers |
|---|---|---|
| 1 | Introduction | The design in brief — 1024-bit state and block, the tweakable ARX permutation, Davies–Meyer, the public tweak — with an interactive five-phase figure and a one-table parameter summary. Detail beyond that is in the PDF |
| 2 | Live demonstration | A JavaScript port of the compression function running in the page: text / hex / bit-string input, 512 / 768 / 1024 output, a known-answer self-test against the Appendix B vectors, and the timings it measures itself |
| 3 | Downloads | The specification, the erratum, the implementations and the full archive, each with its SHA-256, plus the revision history of the submission and a note on which revision is which |
| 4 | Third-party analysis | The three independent sources, the R1–R8 findings table with the status of each against the material released here, and the ePrint 2026/2236 component result |
| 5 | Erratum | The designers' erratum from v1.0 to v1.0.1 reproduced in full — the specification typo corrections, the software and hardware implementation corrections, the further text changes made in response to the assessment, and how each maps onto R1–R8 |
| — | Sources | Documents referenced |

---

## Downloads

| Artifact | File | Contents | Size |
|---|---|---|---|
| Specification | [`files/specification.pdf`](files/specification.pdf) | the submission, as filed — version 1.0.1, 69 pp. | 650 KB |
| Erratum | [`files/FEILIAN_Erratum.pdf`](files/FEILIAN_Erratum.pdf) | corrections from v1.0 to v1.0.1, October 2026, 2 pp. | 124 KB |
| Reference code | [`files/feilian-code.zip`](files/feilian-code.zip) | C (reference + AVX2/SIMD) and SystemVerilog cores, v1.0.1 | 108 KB |
| Full archive | [`files/feilian-archive.zip`](files/feilian-archive.zip) | implementations, KAT vectors, Appendix B material, analysis notes, tooling | 9.94 MB |
| Checksums | [`files/SHA256SUMS.txt`](files/SHA256SUMS.txt) | `sha256sum -c` compatible | — |

```
2d14bcf877eb9fbdb79fe573be078923445aec373270a16676ebd494ffabf0db  specification.pdf
04969502772e3d2f380549f80f3edf68a1bf6e1479d03094a2f251bbc4bd235e  FEILIAN_Erratum.pdf
c9962a89df794f453bbd1a688eecd71bb9e7bd4649b9ab15a64e8b8c3912d034  feilian-code.zip
c76e8fa4f3cc09703f25464fe02accd9f47b3e8abfaf3fa2fa3d8b2af8f081a4  feilian-archive.zip
```

[`files/SHA256SUMS.txt`](files/SHA256SUMS.txt) is the canonical list of digests; the
copies above are for convenience and are regenerated together with the artifacts.

The archives are built deterministically — sorted entries, fixed timestamps, fixed permissions —
so rebuilding them from the same inputs reproduces the same digests.

---

## Verifying a release

```bash
python tools/verify_release.py
python tools/verify_release.py --url https://pennybenny.github.io/FEILIAN/
```

The first form checks every digest against the files on disk, that each artifact the page links to
exists, that the navigation anchors resolve to real sections, that the tags balance, and that the
release metadata is present. The second additionally fetches the deployed page and every artifact
and compares the served bytes against the local copies. Exit status is non-zero if anything fails.

To verify a download by hand:

```bash
sha256sum -c SHA256SUMS.txt
```

---

## Running it locally

Open `index.html` in any browser — no server required. If you prefer one:

```bash
python -m http.server 8000     # then visit http://localhost:8000/
```

---

## Repository layout

```
index.html                    the entire site — single file, no dependencies
files/                        published artifacts and their checksums
  specification.pdf
  FEILIAN_Erratum.pdf
  feilian-code.zip
  feilian-archive.zip
  SHA256SUMS.txt
tools/
  make_downloads.py           rebuild files/ and rewrite the page's manifest
  verify_release.py           checksums, links, page structure, deployed bytes
README.md                     this file
DEPLOY.md                     publishing and maintenance
NOTICE.md                     provenance, authorship and rights
CHANGELOG.md                  release history
LICENSE                       CC BY 4.0 (compendium only)
```

The download section of the page is generated from a manifest embedded between
`/* DOWNLOADS:BEGIN */` and `/* DOWNLOADS:END */` in `index.html`.
`tools/make_downloads.py` rewrites that block with the real sizes and checksums, so the page can
never advertise an artifact that has not been published — an unpublished entry renders as a
disabled button rather than a dead link.

---

## Provenance, authorship and licensing

This page is **part of the submission**. It is the entry point published for the hash-10 submission:
the specification and the erratum as released, the implementations, and the third-party analyses the
submission has received. Every parameter, test vector and measurement on the page is taken from the
sources listed above; where the page and the specification disagree, the specification prevails.

**The specification is by** Lei Wang, Ling Song, Yaobin Shen, Kaixuan Wang, Zicheng Shi and Xin Yi
(Shanghai Jiao Tong University; Jinan University; Xiamen University).

**The component analysis of §4 is by** Mounir Idrassi (AM Crypto, Japan), Cryptology ePrint Archive,
Report 2026/2236, distributed under CC BY 4.0. **The technical assessment of §4 is by** the same
author, version 1.0.2, 27 September 2026, also CC BY 4.0. **The ngcc.dev report** is by
Markku-Juhani O. Saarinen; ngcc.dev is his personal site and states that it is unaffiliated with
NICCS — its identifiers and editorial labels belong to that site and are not official competition
assessments.

Licensing is split, because the repository contains two kinds of material:

| Material | Terms |
|---|---|
| This page — `index.html`, the documentation, `tools/` | **CC BY 4.0** — see [`LICENSE`](LICENSE) |
| `files/specification.pdf`, `files/FEILIAN_Erratum.pdf`, `files/feilian-code.zip`, `files/feilian-archive.zip` | the submission material, released here as filed; all rights remain with the designers; **no licence granted** |
| `files/SHA256SUMS.txt` | checksums — copy freely |

See [`NOTICE.md`](NOTICE.md) for the full statement. If you are a rights holder and want any file
withdrawn, open an issue and it will be removed promptly.

---

## How to cite

The specification:

> Lei Wang, Ling Song, Yaobin Shen, Kaixuan Wang, Zicheng Shi and Xin Yi.
> *FEILIAN: A Hash Function Proposal.* Submitted to the Next-generation Cryptographic Algorithms
> Program (NGCC-CH), Institute of Commercial Cryptography Standards, China. Version 1.0.1, 8 October
> 2026, 69 pp. (Erratum from v1.0 released with it.)

The component analysis:

> Mounir Idrassi. *A Complete Classification of Whole-Output Linear Structures in FEILIAN-Type
> Components.* Cryptology ePrint Archive, Report 2026/2236, 2026.
> <https://eprint.iacr.org/2026/2236>

The submission's overview page, if you need to point at it:

> *FEILIAN (hash-10) — Submission Overview* (v1.3.0), <https://pennybenny.github.io/FEILIAN/>

---

## Corrections

Errors in the presentation are the responsibility of this repository. Please open an issue for any
discrepancy — a wrong constant, a mistyped vector, a misattributed figure — and it will be fixed and
recorded in [`CHANGELOG.md`](CHANGELOG.md).

## Release history

See [`CHANGELOG.md`](CHANGELOG.md). Current release: **v1.3.0** (9 October 2026), tracking
specification **v1.0.1** (8 October 2026).
