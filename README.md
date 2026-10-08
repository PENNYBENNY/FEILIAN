# FEILIAN — Specification Compendium

**A structured, self-contained presentation of the FEILIAN hash function**, submitted to the
NGCC-CH programme of the Institute of Commercial Cryptography Standards (ICCS), China, under the
designation `hash-10`.

**Live site — <https://pennybenny.github.io/FEILIAN/>**

The compendium transcribes the submitted specification (revision 29 September 2026, 70 pp.) into a
single browsable page: design parameters, the compression pipeline, IV and round constants, the
canonical Appendix B test vectors for all three digest sizes, the security argument of Chapter 4,
the performance reported in Chapter 5, and the applications of Chapter 6 — together with a summary
of the independent component-level analysis in Cryptology ePrint 2026/2236.

It is one HTML file with **no build step, no framework and no external dependencies**. Every figure
is inline SVG or plain JavaScript, so it renders identically offline, from `file://`, and from any
static host.

---

## Contents

| § | Section | What it covers |
|---|---|---|
| 1 | Overview | Architecture diagram and the design in brief |
| 2 | Specification | Official parameters: 1024-bit state, 512-bit blocks, 20 rounds in 5 phases, Davies–Meyer with HAIFA-style domain extension |
| 3 | Pipeline | Interactive walkthrough of the five phases across four rounds |
| 4 | IV & Constants | The sixteen π-derived IV words and the four round constants |
| 5 | Test Vectors | Appendix B digests and intermediate states, 512 / 768 / 1024 |
| 6 | Security | Chapter 4 claims, the NIST SP 800-22 sampling, and the structural arguments |
| 7 | Performance | Chapter 5 operation counts, software timings and FPGA synthesis results |
| 8 | Applications | MAC, KDF and XOF constructions from Chapter 6 |
| 9 | Components | Whole-output linear structures in FEILIAN-type components (ePrint 2026/2236) |
| 10 | Downloads | The specification, the implementations and the full archive |
| 11 | References | Sources |

---

## Downloads

| Artifact | File | Contents | Size |
|---|---|---|---|
| Specification | [`files/specification.pdf`](files/specification.pdf) | the submission, as filed — 70 pp. | 649 KB |
| Reference code | [`files/feilian-code.zip`](files/feilian-code.zip) | C (reference + AVX2/SIMD) and SystemVerilog cores | 107 KB |
| Full archive | [`files/feilian-archive.zip`](files/feilian-archive.zip) | implementations, KAT vectors, Appendix B material, analysis notes, tooling | 9.94 MB |
| Checksums | [`files/SHA256SUMS.txt`](files/SHA256SUMS.txt) | `sha256sum -c` compatible | — |

```
7f498f6c4830f78d5f40c1c21b9ad41e0c33dc4d20a91c7277c3add8c4144255  specification.pdf
fcb148478f5e06b13b8837fac549a905d5c50b69fe6ac2f8f69a37d5b57693f5  feilian-code.zip
60a587d284415c79db027fe2424b51d979ef19f9e993684744824c6a73bc9b42  feilian-archive.zip
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

The compendium is **unofficial**. It is a presentation of published material, it is not part of the
submission, and it is not endorsed by the designers. Every parameter, test vector and measurement
on the page is transcribed from the sources listed above; where the compendium and an authoritative
document disagree, the specification and the original papers prevail.

**The specification is by** Lei Wang, Ling Song, Yaobin Shen, Kaixuan Wang, Zicheng Shi and Xin Yi
(Shanghai Jiao Tong University; Jinan University; Xiamen University).

**The component analysis summarised in §9 is by** Mounir Idrassi (AM Crypto, Japan), Cryptology
ePrint Archive, Report 2026/2236, distributed under CC BY 4.0.

Licensing is split, because the repository contains two kinds of material:

| Material | Terms |
|---|---|
| The compendium — `index.html`, the documentation, `tools/` | **CC BY 4.0** — see [`LICENSE`](LICENSE) |
| `files/specification.pdf`, `files/feilian-code.zip`, `files/feilian-archive.zip` | redistributed as filed; all rights remain with the authors; **no licence granted** |
| `files/SHA256SUMS.txt` | checksums — copy freely |

See [`NOTICE.md`](NOTICE.md) for the full statement. If you are a rights holder and want any file
withdrawn, open an issue and it will be removed promptly.

---

## How to cite

The specification:

> Lei Wang, Ling Song, Yaobin Shen, Kaixuan Wang, Zicheng Shi and Xin Yi.
> *FEILIAN: A Hash Function Proposal.* Submitted to the Next-generation Cryptographic Algorithms
> Program (NGCC-CH), Institute of Commercial Cryptography Standards, China. Revision 29 September
> 2026, 70 pp.

The component analysis:

> Mounir Idrassi. *A Complete Classification of Whole-Output Linear Structures in FEILIAN-Type
> Components.* Cryptology ePrint Archive, Report 2026/2236, 2026.
> <https://eprint.iacr.org/2026/2236>

This compendium, if you need to point at it:

> *FEILIAN Specification Compendium* (v1.0.0), <https://pennybenny.github.io/FEILIAN/>

---

## Corrections

Errors in the transcription or presentation are the responsibility of this repository, not of the
FEILIAN designers. Please open an issue for any discrepancy — a wrong constant, a mistyped vector,
a misattributed figure — and it will be fixed and recorded in [`CHANGELOG.md`](CHANGELOG.md).

## Release history

See [`CHANGELOG.md`](CHANGELOG.md). Current release: **v1.0.0** (8 October 2026), tracking
specification revision 2026-09-29.
