#!/usr/bin/env python3
# ---------------------------------------------------------------------------
#  Publish the release packages of this repository into files/ and wire them
#  into the page's DOWNLOADS manifest.
#
#      files/FEILIAN-v1.0.1.zip   the version 1.0.1 release package
#      files/FEILIAN_Erratum.pdf  the erratum, published on its own so that
#                                 section 05 can link the PDF directly
#      files/SHA256SUMS.txt       sha256sum -c compatible
#
#  A release package is assembled by the designers and shipped whole: it holds
#  the specification, the erratum and the implementations for one revision.
#  This script copies such a package into files/ VERBATIM — it never repacks
#  it — so the published SHA-256 is the digest of the official artifact and
#  stays verifiable against any other copy of it.
#
#  Two tables drive it. Every PACKAGES row becomes a download card in the
#  page's manifest; every ASSETS row is published and checksummed the same way
#  but deliberately gets no card, because the page links it from the text.
#
#  It then rewrites the block between  /* DOWNLOADS:BEGIN */  and
#  /* DOWNLOADS:END */  in index.html with the real sizes, checksums and
#  ready=true.
#
#  DEFAULT IS A DRY RUN. Nothing is written without --publish, because copying
#  the specification and the reference code into a public repository is a
#  disclosure decision, not a build step.
#
#      python tools/make_downloads.py                       # show what would be built
#      python tools/make_downloads.py --publish             # copy files/ and patch
#      python tools/make_downloads.py --publish --package v1.0.0/FEILIAN-v1.0.0.zip
#
#  Sources are resolved relative to a workspace directory (default: the parent
#  of this repository) that holds the submission material.
# ---------------------------------------------------------------------------
import argparse
import hashlib
import os
import re
import sys

REPO  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = os.path.join(REPO, "files")
INDEX = os.path.join(REPO, "index.html")

# (id, title, subtitle, served filename, workspace-relative source)
# One row per published revision. Add a row to publish another revision; the
# grid on the page lays itself out for however many rows there are.
PACKAGES = [
    ("v101", "Release package v1.0.1",
     "Specification 1.0.1 (69 pp.) + erratum v1.0\u2192v1.0.1 + reference, "
     "optimized and RTL implementations",
     "FEILIAN-v1.0.1.zip", os.path.join("v1.0.1", "FEILIAN-v1.0.1.zip")),
]

# (id, title, subtitle, served filename, workspace-relative source)
# Single documents published for direct linking, NOT offered as a download
# card: section 05 links the erratum PDF straight from the text, so it has to
# exist on its own under files/ rather than only inside the archive. Same
# treatment as a package otherwise - copied verbatim and covered by
# files/SHA256SUMS.txt, so verify_release.py keeps it honest.
ASSETS = [
    ("erratum", "Erratum",
     "PDF \u00b7 corrections from v1.0 to v1.0.1 \u00b7 3 pp.",
     "FEILIAN_Erratum.pdf", os.path.join("v1.0.1", "FEILIAN_Erratum.pdf")),
]


def human(n):
    return f"{n/1048576:.2f} MB" if n >= 1048576 else f"{n/1024:.1f} KB"


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def manifest_block(results):
    rows = []
    for (pid, title, sub, served, _src), info in zip(PACKAGES, results):
        size = human(info["bytes"]) if info else ""
        sha = info["sha"][:16] + "\u2026" if info else ""
        ready = "true" if info else "false"
        rows.append(
            f'  {{id:"{pid}", title:"{title}",\n'
            f'   sub:"{sub}",\n'
            f'   file:"files/{served}", size:"{size}", sha:"{sha}", ready:{ready}}}'
        )
    body = ",\n".join(rows)
    return ("/* DOWNLOADS:BEGIN */\n"
            f"var DOWNLOADS = [\n{body}\n];\n"
            'var DL_RELEASE = "";   /* optional mirror base, e.g. a release CDN prefix */\n'
            "/* DOWNLOADS:END */")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--publish", action="store_true",
                    help="copy files/* and patch index.html (without this, nothing is written)")
    ap.add_argument("--workspace", default=os.path.dirname(REPO),
                    help="directory holding the submission material (default: parent of this repo)")
    ap.add_argument("--package", default=None, action="append",
                    help="path to a release package, relative to the workspace; "
                         "repeat for more than one. Defaults to the built-in list.")
    ap.add_argument("--out", default=FILES, help="output directory (default: files/)")
    ap.add_argument("--no-patch", action="store_true",
                    help="copy the artifacts but leave index.html untouched")
    args = ap.parse_args()

    ws = os.path.abspath(args.workspace)
    files_dir = os.path.abspath(args.out)

    wanted = PACKAGES
    if args.package:
        by_src = {os.path.normpath(src): row for row in PACKAGES for src in [row[4]]}
        picked = []
        for p in args.package:
            key = os.path.normpath(p)
            if key in by_src:
                picked.append(by_src[key])
            else:
                base = os.path.basename(p)
                pid = re.sub(r"[^A-Za-z0-9]+", "", os.path.splitext(base)[0]).lower()[:8] or "pkg"
                picked.append((pid, f"Release package {base}", "Release package",
                               base, p))
        wanted = picked

    if not os.path.exists(INDEX):
        sys.exit(f"index.html not found at {INDEX}")

    print(f"repo      : {REPO}")
    print(f"workspace : {ws}{'' if os.path.isdir(ws) else '   (MISSING)'}")
    print(f"output    : {files_dir}")
    print(f"mode      : {'PUBLISH (writes files)' if args.publish else 'DRY RUN (no writes)'}\n")

    resolved = []
    for pid, title, _sub, served, src in wanted:
        p = os.path.abspath(os.path.join(ws, src))
        resolved.append((pid, title, served, src, p))
        if os.path.exists(p):
            print(f"  {title:24s} {src:36s} {human(os.path.getsize(p)):>9s}  {sha256_file(p)[:16]}…")
        else:
            print(f"  {title:24s} {src:36s}   ! MISSING — that card stays unpublished")

    assets = []
    for aid, title, _sub, served, src in ASSETS:
        p = os.path.abspath(os.path.join(ws, src))
        assets.append((aid, title, served, src, p))
        if os.path.exists(p):
            print(f"  {title:24s} {src:36s} {human(os.path.getsize(p)):>9s}  "
                  f"{sha256_file(p)[:16]}…  (linked from the text, no card)")
        else:
            print(f"  {title:24s} {src:36s}   ! MISSING — the in-text link would dead-end")

    if not args.publish:
        print("\nNothing written. Re-run with --publish to publish and enable.")
        return

    os.makedirs(files_dir, exist_ok=True)

    results = []
    for _pid, _title, served, _src, src in resolved:
        dst = os.path.join(files_dir, served)
        if not os.path.exists(src):
            results.append(None)
            continue
        # Guard: a package may already live in files/, and opening the
        # destination for writing truncates it before it can be read.
        if os.path.abspath(src) != os.path.abspath(dst):
            with open(src, "rb") as a:
                data = a.read()
            with open(dst, "wb") as b:
                b.write(data)
        results.append({"bytes": os.path.getsize(dst), "sha": sha256_file(dst)})

    asset_results = []
    for _aid, _title, served, _src, src in assets:
        dst = os.path.join(files_dir, served)
        if not os.path.exists(src):
            # keep whatever is already published rather than dropping a document
            # the page links to merely because the workspace copy is absent
            asset_results.append(
                {"bytes": os.path.getsize(dst), "sha": sha256_file(dst)}
                if os.path.exists(dst) else None)
            continue
        if os.path.abspath(src) != os.path.abspath(dst):
            with open(src, "rb") as a:
                data = a.read()
            with open(dst, "wb") as b:
                b.write(data)
        asset_results.append({"bytes": os.path.getsize(dst), "sha": sha256_file(dst)})

    keep = {"SHA256SUMS.txt"}
    keep |= {served for (_p, _t, served, _s, _r), info in zip(resolved, results) if info}
    keep |= {served for (_a, _t, served, _s, _r), info in zip(assets, asset_results) if info}
    removed = []
    for name in sorted(os.listdir(files_dir)):
        if name not in keep:
            os.remove(os.path.join(files_dir, name))
            removed.append(name)
    for name in removed:
        print(f"   - retired files/{name}")

    lines = [f"{info['sha']}  {served}"
             for (_p, _t, served, _s, _r), info in zip(resolved, results) if info]
    lines += [f"{info['sha']}  {served}"
              for (_a, _t, served, _s, _r), info in zip(assets, asset_results) if info]
    with open(os.path.join(files_dir, "SHA256SUMS.txt"), "w",
              encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")

    if args.no_patch:
        patched = "left untouched (--no-patch)"
        print("   (--no-patch: index.html left untouched)")
    else:
        html = open(INDEX, encoding="utf-8").read()
        if "/* DOWNLOADS:BEGIN */" not in html or "/* DOWNLOADS:END */" not in html:
            patched = "NOT patched — markers missing"
            print("   ! manifest markers not found in index.html — page not patched")
        else:
            new = re.sub(r"/\* DOWNLOADS:BEGIN \*/.*?/\* DOWNLOADS:END \*/",
                         lambda _m: manifest_block(results), html, count=1, flags=re.S)
            if new == html:
                # same digests as last time: nothing to write, and saying
                # "markers not found" here would be a false alarm
                patched = "already up to date"
                print("   manifest unchanged — index.html not rewritten")
            else:
                with open(INDEX, "w", encoding="utf-8", newline="\n") as fh:
                    fh.write(new)
                patched = "patched"

    print("\n=== published ===")
    for (_p, title, served, _s, _r), info in zip(resolved, results):
        if info:
            print(f"  {title:24s} files/{served:24s} {human(info['bytes']):>9s}  {info['sha'][:16]}…")
        else:
            print(f"  {title:24s} (skipped)")
    for (_a, title, served, _s, _r), info in zip(assets, asset_results):
        if info:
            print(f"  {title:24s} files/{served:24s} {human(info['bytes']):>9s}  "
                  f"{info['sha'][:16]}…  (linked, no card)")
        else:
            print(f"  {title:24s} (skipped)")
    print(f"\n  index.html manifest {patched}")
    print("  Commit the repository to publish. Verify a download with:")
    print("      python tools/verify_release.py")


if __name__ == "__main__":
    main()
