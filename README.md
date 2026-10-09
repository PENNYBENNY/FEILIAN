# FEILIAN — Submission Overview

**The overview page for FEILIAN**, the hash function submitted to the NGCC-CH programme of the
Institute of Commercial Cryptography Standards (ICCS), China, under the designation `hash-10`.

**Live site — <https://pennybenny.github.io/FEILIAN/>**

The page is organised as five chapters: an **introduction** to the design — a four-view figure, the
performance the specification reports for it, and the revision history of the submission — a **live
demonstration** that computes digests in the browser, the **downloads** (one checksummed release
package), the **independent third-party analyses**, each linked to its own document, and the
**erratum**, a pointer to the designers' record of every change from v1.0 to v1.0.1, published on
its own and linked directly. Detailed specification tables are deliberately kept out of the page and
left to the PDF. The palette is deliberately plain — one accent colour and neutral greys — and every
figure keeps its own proportions rather than being stretched to the width of the card.

The third-party material cited is the technical assessment by Mounir Idrassi (findings R1–R8),
the ngcc.dev report by Markku-Juhani O. Saarinen, and the component-level analysis in Cryptology
ePrint 2026/2236 — each linked to its own document. None of them establishes a full-round
cryptanalytic break, and the page states that boundary as plainly as they do.

It is one HTML file with **no build step, no framework and no external dependencies**. Every figure
is inline SVG or plain JavaScript, and the live demo's hash core is inlined into the same file, so
the page renders and the demo runs identically offline, from `file://`, and from any static host.

---

## Contents

| § | Section | What it covers |
|---|---|---|
| 1 | Introduction | The design in brief — 1024-bit state and block, the tweakable ARX permutation, Davies–Meyer — with a **four-view interactive figure** redrawn from the specification's own diagrams (compression function / one round / SubColumn / ARX S-box); the performance the specification reports (cycles per byte against BLAKE-64 / SHA-512 / SHA-3-512, software benchmarks on three platforms, and FPGA throughput); and the **revision history of the submission** |
| 2 | Live demonstration | A JavaScript port of the compression function running in the page: text / hex / bit-string input, 512 / 768 / 1024 output, a known-answer self-test against the Appendix B vectors, and the timings it measures itself |
| 3 | Downloads | One **version 1.0.1 release package** — specification, erratum and all implementations in a single archive — with its SHA-256, and a note on which revision is which |
| 4 | Third-party analysis | The three independent sources, listed one per row and each linked to its own document. Their findings are not reproduced on the page |
| 5 | Erratum | A pointer to the designers' erratum from v1.0 to v1.0.1: what the three pages cover — the specification typo corrections, the implementation corrections and the further text changes made in response to the community assessments — with the erratum linked directly as a PDF of its own |
| — | Sources | Documents referenced |

---

## Downloads

| Artifact | File | Contents | Size |
|---|---|---|---|
| Release package v1.0.1 | [`files/FEILIAN-v1.0.1.zip`](files/FEILIAN-v1.0.1.zip) | the whole of version 1.0.1 in one archive — specification (69 pp.), the three-page erratum from v1.0, the reference, optimized (AVX2/NEON) and RTL implementations, and the implementations README | 856 KB |
| Erratum | [`files/FEILIAN_Erratum.pdf`](files/FEILIAN_Erratum.pdf) | the three-page erratum on its own, byte-identical to the copy inside the package — linked from §5, which is why it is not repacked into the archive only | 125 KB |
| Checksums | [`files/SHA256SUMS.txt`](files/SHA256SUMS.txt) | `sha256sum -c` compatible | — |

```
23d3e6721563a27b15b39b14a3e3042b9c5da6925fb3d540464d85206de05d5c  FEILIAN-v1.0.1.zip
98e74ec289636cea9fafa56518240a55e1d2473ff6af5d07e0b311baec98e424  FEILIAN_Erratum.pdf
```

[`files/SHA256SUMS.txt`](files/SHA256SUMS.txt) is the canonical list of digests; the
copy above is for convenience and is regenerated together with the artifacts.

The package is published **byte-for-byte as distributed**, never repacked, so its digest is the
digest of the official artifact and can be checked against any other copy of it. The SHA-256 of the
specification PDF *inside* the package is
`2d14bcf877eb9fbdb79fe573be078923445aec373270a16676ebd494ffabf0db`; the erratum inside it is the
same file as [`files/FEILIAN_Erratum.pdf`](files/FEILIAN_Erratum.pdf) above.

---

## Verifying a release

```bash
python tools/verify_release.py
python tools/verify_release.py --url https://pennybenny.github.io/FEILIAN/
```

The first form checks every digest against the files on disk, that each artifact the page links to
exists — both those in the download manifest and the documents linked straight from the text — that
the navigation anchors resolve to real sections, that the tags balance, and that the release metadata
is present. The second additionally fetches the deployed page and every artifact
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
files/                        the published release package and its checksums
  FEILIAN-v1.0.1.zip
  FEILIAN_Erratum.pdf         published on its own so §5 can link it directly
  SHA256SUMS.txt
tools/
  make_downloads.py           copy a release package into files/ and rewrite the page's manifest
  verify_release.py           checksums, links, page structure, deployed bytes
README.md                     this file
DEPLOY.md                     publishing and maintenance
NOTICE.md                     provenance, authorship and rights
CHANGELOG.md                  release history
LICENSE                       CC BY 4.0 (compendium only)
```

The download section of the page is generated from a manifest embedded between
`/* DOWNLOADS:BEGIN */` and `/* DOWNLOADS:END */` in `index.html`.
`tools/make_downloads.py` copies a release package into `files/`, records its digest and rewrites
that block, so the page can never advertise a package that has not been published — an
unpublished entry renders as a disabled button rather than a dead link.

Documents that the text links directly rather than offering as a card — currently the erratum of §5 —
are published by the same script from its `ASSETS` table and covered by the same checksums; they are
in `files/` so that the link is same-origin and keeps working wherever the page is served from.

---

## Provenance, authorship and licensing

This page is **part of the submission**. It is the entry point published for the hash-10 submission:
the version 1.0.1 release package and the erratum published with it, and the third-party analyses the submission has received. Every parameter, test vector and measurement on the page is taken from the
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
| `files/FEILIAN-v1.0.1.zip` | the submission material, published as distributed; all rights remain with the designers; **no licence granted** |
| `files/FEILIAN_Erratum.pdf` | the same submission material, as a document of its own; **no licence granted** |
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

> *FEILIAN (hash-10) — Submission Overview* (v1.6.1), <https://pennybenny.github.io/FEILIAN/>

---

## Corrections

Errors in the presentation are the responsibility of this repository. Please open an issue for any
discrepancy — a wrong constant, a mistyped vector, a misattributed figure — and it will be fixed and
recorded in [`CHANGELOG.md`](CHANGELOG.md).

## Release history

See [`CHANGELOG.md`](CHANGELOG.md). Current release: **v1.6.1** (9 October 2026), tracking
specification **v1.0.1** (8 October 2026).
