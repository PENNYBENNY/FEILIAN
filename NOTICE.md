# NOTICE

Provenance, authorship and rights for everything in this repository.

## What this repository is

An **unofficial compendium** of the FEILIAN hash function, submitted to the
NGCC-CH programme of the Institute of Commercial Cryptography Standards (ICCS),
China, under the designation `hash-10`.

The compendium is a *presentation* of published material. It is not part of the
submission, it is not endorsed by the designers, and it makes no claim of its
own about the algorithm. Where the compendium and an authoritative document
disagree, the specification and the original papers prevail.

## The specification

> **FEILIAN: A Hash Function Proposal** — submitted to the Next-generation
> Cryptographic Algorithms Program (NGCC), China. Designation `hash-10`.
> Version 1.0.1, 8 October 2026, 69 pp.

The designers released a two-page **erratum** together with version 1.0.1,
recording every change from the June 2026 text. It is redistributed in `files/`
and reproduced in the compendium's section 4.

Designers / submitters, as printed on the specification's title page:

| Name | Affiliation |
|---|---|
| Lei Wang | Shanghai Jiao Tong University, Shanghai, China |
| Ling Song | Jinan University, Guangzhou, China |
| Yaobin Shen | Xiamen University, Xiamen, China |
| Kaixuan Wang | Shanghai Jiao Tong University, Shanghai, China |
| Zicheng Shi | Shanghai Jiao Tong University, Shanghai, China |
| Xin Yi | Shanghai Jiao Tong University, Shanghai, China |

An English translation of the compendium's own summary of the design, and the
specification's Chapters 1–6, are the source of every parameter, test vector and
measurement reproduced in `index.html`.

## Third-party analyses

Three independent sources are presented in the compendium's section 3.

> Mounir Idrassi (AM Crypto, Japan). *A Complete Classification of Whole-Output
> Linear Structures in FEILIAN-Type Components*, Cryptology ePrint Archive,
> Report 2026/2236.

Distributed by the Cryptology ePrint Archive under **CC BY 4.0**. The summary
here is drawn from the published text. The paper's own scope statement is that
its component results establish no hash attack and no bound on the hash's
security margin — the compendium reproduces that boundary and does not extend it.

> Mounir Idrassi (AM Crypto, Japan). *FEILIAN: technical assessment of the
> submitted specification and implementations*, version 1.0.2, 27 September 2026,
> 14 pp.

Licensed by its author under **CC BY 4.0** ("The original text of this report is
licensed under CC BY 4.0"). Findings R1–R8 are quoted and paraphrased from it.
The report's own limits are reproduced: the hardware findings are source-level
with no RTL simulation performed, and no full-round cryptanalytic break of the
correctly encoded software hash is established.

> Markku-Juhani O. Saarinen. *FEILIAN (hash-10)*, personal report, ngcc.dev,
> 23 and 26 September 2026.

The site states that it is unaffiliated with NICCS. Its identifiers and editorial
labels — including the entry names `hash-10-1` … `hash-10-5` — belong to that
site and are not official competition assessments. The compendium cites it as
prior work and as a publication venue, not as an authority.

The **status column** of the findings table records the state of the material
distributed in this repository. It is not a statement by any reviewer, and where
it and a reviewer's document disagree, the reviewer's document prevails.

## Rights in the files under `files/`

`files/specification.pdf`, `files/FEILIAN_Erratum.pdf`, `files/feilian-code.zip`
and `files/feilian-archive.zip` are **submission material**. Copyright in the
specification, in the erratum and in the implementations remains with their
designers and submitters.

They are redistributed here, as filed, so that the compendium's figures can be
checked against their sources and so that reviewers and implementers can work
from the same bytes. **No licence to this material is granted or implied.**
The CC BY 4.0 licence in `LICENSE` applies to the compendium only, and explicitly
excludes these files. `files/SHA256SUMS.txt`, being a list of checksums, may be
copied freely.

If you are a rights holder and want any of these files removed, open an issue in
this repository or contact the repository owner and it will be withdrawn
promptly.

## Integrity

The specification and the erratum are redistributed byte-for-byte as received.
Their SHA-256 digests are

```
2d14bcf877eb9fbdb79fe573be078923445aec373270a16676ebd494ffabf0db  specification.pdf
04969502772e3d2f380549f80f3edf68a1bf6e1479d03094a2f251bbc4bd235e  FEILIAN_Erratum.pdf
```

and it is recorded in `files/SHA256SUMS.txt` together with the digests of the
other artifacts. Verify the whole set with:

```bash
python tools/verify_release.py
```

The archives are built deterministically, so rebuilding them from the same inputs
reproduces the same digests.

## Corrections

Errors in the compendium's transcription or presentation are the responsibility
of the repository owner, not of the FEILIAN designers. Please open an issue for
any discrepancy found — a wrong constant, a mistyped vector, a misattributed
figure — and it will be corrected and noted in `CHANGELOG.md`.
