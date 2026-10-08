# Deployment and maintenance

Operational notes for this repository. Nothing here is needed to *read* the
compendium — it is the maintenance manual for whoever publishes it.

- Live site: <https://pennybenny.github.io/FEILIAN/>
- Repository: <https://github.com/PENNYBENNY/FEILIAN>
- Pages source: branch `main`, folder `/ (root)`, `Jekyll` disabled by `.nojekyll`

## Publishing a change

```bash
git add -A && git commit -m "..." && git push
```

Pages rebuilds in about a minute. `git push` alone is enough once the upstream is
tracked; use `git push -u origin main` the first time.

There is no build step. `index.html` is the whole site — one file, no external
dependencies, no bundler, no CDN. What you commit is what is served.

## Enabling Pages for the first time

1. **Settings → Pages → Build and deployment → Source: Deploy from a branch**
2. Branch `main`, folder `/ (root)`, **Save**

`github.com/pennybenny/FEILIAN` redirects to the canonical uppercase owner name
`PENNYBENNY`; both forms resolve, and the site URL stays lowercase.

## Rebuilding the downloadable artifacts

`tools/make_downloads.py` assembles `files/` from the submission workspace and
rewrites the manifest block in `index.html` with the real sizes and checksums.

```bash
python tools/make_downloads.py                 # dry run — lists what would be built
python tools/make_downloads.py --publish       # build files/ and patch index.html
```

It is a dry run by default. Copying the specification and the implementations
into a public repository is a disclosure decision, so it takes an explicit
`--publish` to write anything.

| Flag | Effect |
|---|---|
| `--workspace DIR` | where the submission material lives (default: the parent directory of this repo) |
| `--spec PATH` | the specification PDF, if not in `files/` or `~/Specification.pdf` |
| `--with-bench` | also bundle the benchmark suite into the archive |
| `--with-reference` | also bundle the third-party reference implementation |
| `--out DIR` | stage the build somewhere other than `files/` |
| `--no-patch` | build the artifacts but leave `index.html` alone |

Archives are byte-reproducible: entries are sorted, timestamps fixed to
`2026-09-29`, permissions fixed. Rebuilding from the same inputs reproduces the
same SHA-256, so the published checksums stay meaningful.

## Verifying a release

```bash
python tools/verify_release.py
python tools/verify_release.py --url https://pennybenny.github.io/FEILIAN/
```

Checks that every digest in `files/SHA256SUMS.txt` matches the file on disk, that
every artifact the page links to exists, that the navigation anchors resolve to
real sections, that the tags balance, and that the release metadata is present.
With `--url` it also fetches the deployed page and every artifact and compares
the served bytes against the local copies. Exit status is non-zero if anything
fails.

## Where the downloads live, and why

| Route | URL shape | Loads in mainland China |
|---|---|---|
| **In this repository, served by Pages** | `/<repo>/files/x.zip` | ✅ `github.io` is reachable |
| GitHub Releases | `github.com/<owner>/<repo>/releases/...` | ❌ the URL *starts* at `github.com`, which is widely blocked |
| jsDelivr over this repo | `cdn.jsdelivr.net/gh/<owner>/<repo>@<tag>/files/x.zip` | ✅ but hard limit of 20 MB per file |
| A separate CDN or object store | your own domain | ✅ |

The Release route is the one that looks most "official" and is the one that fails
for the likely audience, so the artifacts are committed here instead. Note that
the HTML `download` attribute only forces a save dialog for **same-origin**
links; a cross-origin mirror just navigates to the file.

Limits to keep in mind: GitHub Pages allows about 1 GB per published site, no
single file in a git repository may exceed 100 MB, and **Pages does not serve Git
LFS objects** — commit the real bytes.

## Troubleshooting: `Connection was reset` when pushing

Git for Windows does **not** inherit the Windows system proxy. A browser that
reaches GitHub perfectly well therefore tells you nothing about whether `git
push` will work.

Diagnose, then route git through the proxy the browser is already using:

```bash
git ls-remote origin          # "Connection was reset" here means the path is blocked

git config --local  http.https://github.com.proxy http://127.0.0.1:7688
git config --global http.https://github.com.proxy http://127.0.0.1:7688   # all repos
```

The port comes from **Windows Settings → Network & Internet → Proxy**, or from
the Clash / v2ray dashboard. The scoped key applies to `github.com` only; other
remotes keep going direct. Undo with:

```bash
git config --unset http.https://github.com.proxy
```

**If credentials are not cached**, a push may block on an interactive login
prompt. To probe the network without that risk:

```bash
GIT_TERMINAL_PROMPT=0 GCM_INTERACTIVE=never git push -u origin main
```

**SSH alternative.** `ssh.github.com:443` is frequently reachable when
`github.com:443` is not:

```
# ~/.ssh/config
Host github.com
  HostName ssh.github.com
  Port 443
  User git
```

then switch the remote to `git@github.com:PENNYBENNY/FEILIAN.git` and upload a
key. The HTTPS-plus-proxy route above is usually less trouble.

Note that `github.io` is normally reachable even when `github.com` is not, so a
Pages site keeps loading for readers in mainland China even while pushes need a
proxy. If the site itself ever becomes unreachable, Cloudflare Pages is the
fallback.

## Alternative hosts

The site is a single static file, so any static host works.

| Host | How |
|---|---|
| **Cloudflare Pages** | Create project → Direct Upload → drop the folder |
| **Netlify Drop** | Drag the folder onto <https://app.netlify.com/drop> |
| **Vercel** | `npx vercel` in this folder |
| **Any web server** | Copy `index.html`, `files/`, `LICENSE`, `NOTICE.md` |

## Custom domain

Optional; the `pennybenny.github.io` URL works fine.

1. Add a `CNAME` file to this directory containing the bare domain, e.g.
   `feilian.example.org`, and commit it.
2. At your DNS provider add a `CNAME` record: `feilian` → `pennybenny.github.io`.
3. **Settings → Pages → Custom domain**, confirm, and tick **Enforce HTTPS**.

Remember to update the `rel="canonical"`, `og:url` and `citation_pdf_url` values
in `index.html` if the site moves.
