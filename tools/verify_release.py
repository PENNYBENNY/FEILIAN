#!/usr/bin/env python3
# ---------------------------------------------------------------------------
#  Verify a published release of this repository.
#
#    python tools/verify_release.py
#        local checks: every checksum in files/SHA256SUMS.txt matches the file
#        on disk, every artifact the page links to exists, and the page's
#        navigation, section anchors and tags are structurally balanced.
#
#    python tools/verify_release.py --url https://example.github.io/FEILIAN/
#        additionally fetches the deployed page and every listed artifact, and
#        compares the served bytes against the local files.
#
#  Exit status is 0 only if every check passes, so this is usable as a gate.
# ---------------------------------------------------------------------------
import argparse
import hashlib
import os
import re
import sys
import urllib.error
import urllib.request

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(REPO, "index.html")
FILES = os.path.join(REPO, "files")
SUMS = os.path.join(FILES, "SHA256SUMS.txt")

ok_count = 0
bad_count = 0


def report(good, label, detail=""):
    global ok_count, bad_count
    if good:
        ok_count += 1
        print(f"  PASS  {label}" + (f"  — {detail}" if detail else ""))
    else:
        bad_count += 1
        print(f"  FAIL  {label}" + (f"  — {detail}" if detail else ""))


def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for c in iter(lambda: fh.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def get(url, timeout=120):
    req = urllib.request.Request(url, headers={"User-Agent": "feilian-verify"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, dict(r.headers), r.read()


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--url", default=None,
                    help="base URL of the deployed site, to verify the served bytes too")
    args = ap.parse_args()

    if not os.path.exists(INDEX):
        sys.exit(f"index.html not found at {INDEX}")
    html = open(INDEX, encoding="utf-8").read()
    body = html.encode("utf-8")

    print("== checksums ==")
    published = {}
    if not os.path.exists(SUMS):
        report(False, "files/SHA256SUMS.txt present")
    else:
        pairs = [l.split() for l in open(SUMS, encoding="utf-8").read().strip().splitlines() if l.strip()]
        published = dict((name, expect) for expect, name in pairs)
        report(len(pairs) > 0, "SHA256SUMS.txt non-empty", f"{len(pairs)} entries")
        for expect, name in pairs:
            p = os.path.join(FILES, name)
            if not os.path.exists(p):
                report(False, f"{name} present")
            else:
                report(sha_file(p) == expect, f"{name}", "sha256 matches")

    print("\n== page links ==")
    refs = sorted(set(re.findall(r'file:"([^"]+)"', html)))
    report(len(refs) > 0, "download manifest populated", f"{len(refs)} artifacts")
    for rel in refs:
        report(os.path.exists(os.path.join(REPO, rel.replace("/", os.sep))), f"{rel} exists")
    report(html.count("ready:false") == 0, "no artifact left unpublished",
           f"{html.count('ready:true')} ready")
    # Documents the text links straight with an href, outside the manifest - the
    # erratum of section 05. A dead one of these is invisible to the check above,
    # and so is one that was published without being checksummed.
    direct = sorted(set(re.findall(r'href="(files/[^"]+)"', html)))
    report(bool(direct), "in-text document links found", f"{len(direct)}")
    for rel in direct:
        report(os.path.exists(os.path.join(REPO, rel.replace("/", os.sep))), f"{rel} exists")
    for rel in direct:
        name = os.path.basename(rel)
        if name == "SHA256SUMS.txt":
            continue  # the list of digests is not itself one of them
        if name in published:
            report(published[name][:16] in html, f"page prints the digest of {name}",
                   f"{published[name][:16]}\u2026")
        else:
            report(False, f"{name} is listed in files/SHA256SUMS.txt")

    print("\n== page structure ==")
    sec = re.findall(r'<section id="([A-Za-z0-9_-]+)">', html)
    navblock = re.search(r'<nav\b[^>]*>([\s\S]*?)</nav>', html)
    nav = re.findall(r'<a href="#([A-Za-z0-9_-]+)">', navblock.group(1)) if navblock else []
    report(bool(nav), "navigation found", f"{len(nav)} items / {len(sec)} sections")
    report(all(n in sec for n in nav), "every nav anchor resolves")
    report(sorted(nav) == sorted(sec), "nav and sections correspond")
    # every in-page anchor anywhere on the page (hero, in-text cross-references,
    # sources) must resolve too - stronger than the nav-only check above.
    all_anchors = re.findall(r'href="#([A-Za-z0-9_-]+)"', html)
    dangling = sorted(set(a for a in all_anchors if a not in sec))
    report(not dangling, "every in-page anchor resolves",
           f"{len(set(all_anchors))} distinct" + (f", dangling: {dangling}" if dangling else ""))
    for tag in ("div", "section", "table", "pre", "svg"):
        o, c = len(re.findall(rf"<{tag}[\s>]", html)), html.count(f"</{tag}>")
        report(o == c, f"<{tag}> balanced", f"{o}/{c}")
    m = re.search(r"<title>(.*?)</title>", html, re.S)
    report(bool(m), "has <title>", m.group(1) if m else "")
    for need in ('name="description"', 'rel="canonical"', 'property="og:title"',
                 'name="citation_title"'):
        report(need in html, f"has {need}")
    report("DOWNLOADS:BEGIN" in html and "DOWNLOADS:END" in html, "manifest markers intact")

    if args.url:
        base = args.url.rstrip("/") + "/"
        print(f"\n== deployed: {base} ==")
        try:
            st, hd, served = get(base)
            report(st == 200, "GET /", f"{st}, {len(served):,} B")
            report(sha_bytes(served) == sha_bytes(body), "served page == local index.html",
                   "byte-identical" if sha_bytes(served) == sha_bytes(body) else "DIFFERS")
        except Exception as e:
            report(False, "GET /", f"{type(e).__name__}: {e}")
        for rel in sorted(set(refs) | set(direct)):
            try:
                st, hd, data = get(base + rel)
                local = os.path.join(REPO, rel.replace("/", os.sep))
                match = os.path.exists(local) and sha_bytes(data) == sha_file(local)
                report(st == 200 and match, f"GET /{rel}",
                       f"{st}, {len(data):,} B, {hd.get('Content-Type')}")
            except Exception as e:
                report(False, f"GET /{rel}", f"{type(e).__name__}: {e}")

    print(f"\n{ok_count} passed, {bad_count} failed")
    return 1 if bad_count else 0


if __name__ == "__main__":
    sys.exit(main())
