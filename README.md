# FEILIAN — Specification Compendium

An interactive, single-page compendium of the **FEILIAN** hash function (NGCC-CH submission, designation `hash-10`), assembled from the submitted specification (revision 29 September 2026, 70 pp.) and the published component-level analysis in Cryptology ePrint 2026/2236.

The whole site is one self-contained file — `index.html` — with **no build step and no external dependencies** (all figures are inline SVG/JS). It works offline and from any static host.

## Contents

1. Overview
2. Specification — official parameters
3. Pipeline — five-phase compression walkthrough (interactive)
4. IV & Constants
5. Test Vectors — Appendix B digests, 512/768/1024
6. Security — Table 4.1 claims, NIST SP 800-22, structure arguments
7. Performance — Chapter 5 operation counts, software/FPGA results (Figures 2–3)
8. Applications — MAC, KDF, XOF
9. Components — linear-structure analysis (ePrint 2026/2236)
10. References

## Local preview

Open `index.html` in any browser. No server required. If you prefer a local server:

```bash
python -m http.server 8000
# then visit http://localhost:8000/
```

## Deploy to GitHub Pages

Target: **`pennybenny/FEILIAN`** → <https://pennybenny.github.io/FEILIAN/>

### One-liner (recommended)

A ready-made script lives in the sibling folder `FEILIAN_deploy/`:

```bash
bash ../FEILIAN_deploy/deploy_github_pages.sh                                          # Git Bash / WSL
powershell -ExecutionPolicy Bypass -File ..\FEILIAN_deploy\deploy_github_pages.ps1     # PowerShell
```

It reuses the repository already initialised in this folder, sets the remote and pushes. If the GitHub CLI is installed and authenticated it also creates the repo and enables Pages automatically.

### By hand

1. Create an empty **public** repo named `FEILIAN`.
2. From this folder:

   ```bash
   git remote add origin https://github.com/pennybenny/FEILIAN.git
   git push -u origin main
   ```

3. **Settings → Pages → Build and deployment → Source: Deploy from a branch**, branch `main`, folder `/ (root)`, Save.
4. Live in ~1 minute at <https://pennybenny.github.io/FEILIAN/>.

### With the GitHub CLI

```bash
gh repo create pennybenny/FEILIAN --public --source=. --push
gh api -X POST repos/pennybenny/FEILIAN/pages \
  -f 'source[branch]=main' -f 'source[path]=/'
```

> The repo name is free — whatever you pick, the URL becomes `https://pennybenny.github.io/<repo>/`.

## Alternative hosts (drag-and-drop, no git)

| Host | How | Notes |
|---|---|---|
| **Cloudflare Pages** | Create project → "Direct Upload" → drop the folder | Free, global CDN, custom domain |
| **Netlify Drop** | Drag the folder onto <https://app.netlify.com/drop> | Instant URL |
| **Vercel** | `npx vercel` in this folder | Free tier |
| **GitHub Gist + htmlpreview** | Paste `index.html`, prepend `https://htmlpreview.github.io/?` to the raw URL | Quickest throwaway share |

## Custom domain

Optional — the site works fine on the `pennybenny.github.io` URL.

1. Add a file named `CNAME` in this folder containing the bare domain, e.g. `feilian.pennybenny.dev`, and commit it.
2. At your DNS provider add a `CNAME` record: `feilian` → `pennybenny.github.io`.
3. In **Settings → Pages → Custom domain** confirm the domain and tick **Enforce HTTPS**.

This mirrors the pattern used by the Ascon lab site (`crypto-lab.systemslibrarian.dev` → `systemslibrarian.github.io/crypto-lab-ascon`).

## Downloadable artifacts

`index.html` renders a **Downloads** section from a manifest embedded between
`/* DOWNLOADS:BEGIN */` and `/* DOWNLOADS:END */`. Nothing is published until you
build it, so the section shows *Not published* rather than a dead link.

```bash
python ../FEILIAN_deploy/make_downloads.py             # dry run — shows what would be built
python ../FEILIAN_deploy/make_downloads.py --publish   # build files/ and patch the manifest
```

Output lands in `FEILIAN_site/files/`:

| File | Built from | Size |
|---|---|---|
| `specification.pdf` | the specification, as filed | 649 KB |
| `feilian-code.zip` | `Implementations/` — C (reference + AVX2/SIMD) + SystemVerilog | 107 KB |
| `feilian-archive.zip` | code + `KAT_current/` + Appendix B work + docs | 9.94 MB |
| `SHA256SUMS.txt` | `sha256sum -c` compatible manifest | — |

> ⚠️ **Disclosure.** Copying `specification.pdf`, the implementations or the KAT
> vectors into a public repository publishes submission material. Confirm with the
> authors and the NGCC programme that release is permitted before running
> `--publish` on a public repo. Both the specification PDF and the code are
> covered by this; only the compendium page itself is analysis.

Zips are written deterministically (sorted entries, fixed timestamps) so the same
inputs always yield byte-identical archives and identical SHA-256. Flags
`--with-bench` and `--with-reference` additionally bundle `FEILIAN_bench/` and
`ZC-DM/`; `--out DIR` and `--no-patch` let you stage the build elsewhere first.

### Where to host the artifacts

| Route | URL shape | Needs git | Loads in mainland China |
|---|---|---|---|
| **In the repo, served by Pages** (default) | `/FEILIAN/files/x.zip` | yes | ✅ `github.io` is reachable |
| GitHub Releases | `.../FEILIAN/releases/download/v1/x.zip` | upload via UI or `gh` | ❌ the URL *starts* at `github.com`, which is blocked |
| jsDelivr over the repo | `cdn.jsdelivr.net/gh/pennybenny/FEILIAN@<tag>/files/x.zip` | yes | ✅ good China CDN, but **20 MB per file** |
| Cloudflare R2 / Pages | your own domain | no | ✅ |

Because the Release download URL begins at `github.com`, it is the one route that
does **not** work behind the usual block — the in-repo Pages route is both the
simplest and the one that survives it. Note also that the HTML `download`
attribute only forces a save dialog for **same-origin** links; a cross-origin
mirror just navigates to the file.

Site budget: GitHub Pages allows ~1 GB per published site, and no single git file
may exceed 100 MB. Git LFS is **not** supported by Pages — commit the real bytes.

## Troubleshooting: `Connection was reset` when pushing

On mainland-China networks the TLS connection to `github.com:443` is frequently reset. Git for Windows **ignores the Windows system proxy**, so a browser that reaches GitHub fine does not mean git will.

Diagnose:

```bash
git ls-remote https://github.com/pennybenny/FEILIAN.git
# fatal: unable to access '...': Recv failure: Connection was reset   -> blocked
```

Fix — route git through the local proxy the browser is already using:

```bash
# this repository only
git config --local http.https://github.com.proxy http://127.0.0.1:7688

# or for every repository
git config --global http.https://github.com.proxy http://127.0.0.1:7688
```

Find the port via **Settings → Network & Internet → Proxy** in Windows, or the Clash / v2ray dashboard. The scoped key `http.https://github.com.proxy` applies to github.com only — other remotes keep going direct. Revert with:

```bash
git config --unset http.https://github.com.proxy
```

**SSH alternative.** `ssh.github.com:443` is often reachable when `github.com:443` is not:

```
# ~/.ssh/config
Host github.com
  HostName ssh.github.com
  Port 443
  User git
```

then set the remote to `git@github.com:pennybenny/FEILIAN.git` and upload an SSH key. The HTTPS-plus-proxy route above is usually less hassle.

**Note for readers:** `github.io` itself is generally reachable even when `github.com` is not, so a GitHub Pages site normally loads fine in China. If it does not, the Cloudflare Pages route below is the fallback.

## Provenance and caveats

- Every parameter, test vector and reported measurement is transcribed from the specification. **Performance figures are the specification's own reported values** (Chapter 5), not remeasured here.
- The specification is a **submission document**. Before publishing anything derived from it, confirm that public release is permitted by the authors and the NGCC programme. The ePrint paper (ref. [2]) is CC BY 4.0.
- This site is an **unofficial** compendium. Where it and an authoritative text differ, the specification and the original papers prevail.
