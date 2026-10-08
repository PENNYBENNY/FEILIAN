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

## Provenance and caveats

- Every parameter, test vector and reported measurement is transcribed from the specification. **Performance figures are the specification's own reported values** (Chapter 5), not remeasured here.
- The specification is a **submission document**. Before publishing anything derived from it, confirm that public release is permitted by the authors and the NGCC programme. The ePrint paper (ref. [2]) is CC BY 4.0.
- This site is an **unofficial** compendium. Where it and an authoritative text differ, the specification and the original papers prevail.
