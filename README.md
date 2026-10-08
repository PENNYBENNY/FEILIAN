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

### Option A — project site (recommended)

1. Create an empty repository on GitHub, e.g. `feilian-spec-compendium` (public).
2. From this folder:

   ```bash
   git init
   git add -A
   git commit -m "FEILIAN specification compendium"
   git branch -M main
   git remote add origin https://github.com/<your-user>/feilian-spec-compendium.git
   git push -u origin main
   ```

3. On GitHub: **Settings → Pages → Build and deployment → Source: Deploy from a branch**, branch `main`, folder `/ (root)`, Save.
4. Wait ~1 minute. The site is live at `https://<your-user>.github.io/feilian-spec-compendium/`.

### Option B — user site

If the repository is named `<your-user>.github.io`, the site is served at `https://<your-user>.github.io/`.

### Option C — command line with the GitHub CLI

If you install [`gh`](https://cli.github.com/) and run `gh auth login`:

```bash
git init && git add -A && git commit -m "FEILIAN specification compendium"
gh repo create feilian-spec-compendium --public --source=. --push
gh api -X POST repos/:owner/feilian-spec-compendium/pages \
  -f 'source[branch]=main' -f 'source[path]=/'
```

## Alternative hosts (drag-and-drop, no git)

| Host | How | Notes |
|---|---|---|
| **Cloudflare Pages** | Create project → "Direct Upload" → drop the folder | Free, global CDN, custom domain |
| **Netlify Drop** | Drag the folder onto <https://app.netlify.com/drop> | Instant URL |
| **Vercel** | `npx vercel` in this folder | Free tier |
| **GitHub Gist + htmlpreview** | Paste `index.html`, prepend `https://htmlpreview.github.io/?` to the raw URL | Quickest throwaway share |

## Custom domain

Add a file named `CNAME` in this folder containing the bare domain (e.g. `feilian.example.org`), commit it, then point a `CNAME` DNS record at `<your-user>.github.io`. Enable "Enforce HTTPS" in Pages settings.

## Provenance and caveats

- Every parameter, test vector and reported measurement is transcribed from the specification. **Performance figures are the specification's own reported values** (Chapter 5), not remeasured here.
- The specification is a **submission document**. Before publishing anything derived from it, confirm that public release is permitted by the authors and the NGCC programme. The ePrint paper (ref. [2]) is CC BY 4.0.
- This site is an **unofficial** compendium. Where it and an authoritative text differ, the specification and the original papers prevail.
