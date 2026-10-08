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
> Revision 29 September 2026, 70 pp.

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

## The independent component analysis

> Mounir Idrassi (AM Crypto, Japan), *A Complete Classification of Whole-Output
> Linear Structures in FEILIAN-Type Components*, Cryptology ePrint Archive,
> Report 2026/2236.

Section 9 of the compendium summarises this paper. The paper is distributed by
the Cryptology ePrint Archive under CC BY 4.0; the summary here is drawn from the
published text. The paper's own scope statement is that its component results
establish no hash attack and no bound on the hash's security margin — the
compendium reproduces that boundary and does not extend it.

## Rights in the files under `files/`

`files/specification.pdf`, `files/feilian-code.zip` and
`files/feilian-archive.zip` are **submission material**. Copyright in the
specification and in the implementations remains with their designers and
submitters.

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

The specification is redistributed byte-for-byte as received. Its SHA-256 is

```
7f498f6c4830f78d5f40c1c21b9ad41e0c33dc4d20a91c7277c3add8c4144255
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
