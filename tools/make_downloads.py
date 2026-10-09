#!/usr/bin/env python3
# ---------------------------------------------------------------------------
#  Assemble the downloadable artifacts for this repository and wire them into
#  the page's DOWNLOADS manifest.
#
#      files/specification.pdf    the submitted specification, as filed
#      files/FEILIAN_Erratum.pdf  the erratum from v1.0 to v1.0.1
#      files/feilian-code.zip     reference + optimized implementations
#      files/feilian-archive.zip  implementations, KAT vectors, docs, tooling
#      files/SHA256SUMS.txt       sha256sum -c compatible
#
#  and rewrites the block between  /* DOWNLOADS:BEGIN */  and  /* DOWNLOADS:END */
#  in index.html with the real sizes, checksums and ready=true.
#
#  DEFAULT IS A DRY RUN. Nothing is written without --publish, because copying
#  the specification and the reference code into a public repository is a
#  disclosure decision, not a build step.
#
#      python tools/make_downloads.py                 # show what would be built
#      python tools/make_downloads.py --publish      # build files/ and patch
#      python tools/make_downloads.py --publish --with-bench --with-reference
#
#  Archives are built deterministically — sorted entries, fixed timestamps,
#  fixed permissions — so identical inputs always give identical SHA-256 and
#  the published checksums stay meaningful across rebuilds.
#
#  Inputs are read from a workspace directory (default: the parent of this
#  repository) that holds the submission material. Override with --workspace.
# ---------------------------------------------------------------------------
import argparse
import hashlib
import os
import re
import sys
import zipfile

REPO  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = os.path.join(REPO, "files")
INDEX = os.path.join(REPO, "index.html")

# id, title, subtitle, served filename, kind
ARTIFACTS = [
    ("spec", "Specification",
     "PDF · version 1.0.1 · 8 October 2026 · 69 pp.", "specification.pdf", "spec"),
    ("erratum", "Erratum",
     "PDF · corrections from v1.0 to v1.0.1 · October 2026", "FEILIAN_Erratum.pdf", "erratum"),
    ("code", "Reference code",
     "C (reference + AVX2/SIMD) and SystemVerilog cores · v1.0.1", "feilian-code.zip", "code"),
    ("archive", "Full archive",
     "Implementations, KAT vectors, Appendix B data and verification tooling",
     "feilian-archive.zip", "archive"),
]

DOCS = ["CodeChanges_summary.md", "CodeChanges_unified.diff",
        "AppendixB_conformance_note.md", "AppendixB_revision_diff.md",
        "AppendixB_test_vectors_revised.md", "AppendixB_test_vectors_revised.txt",
        "AppendixB_revised.tex", "AppendixB_revised_768_512.tex",
        "eprint2236_analysis.md", "R8_shared_infra_assessment.md"]

ZIP_DATE = (2026, 9, 29, 0, 0, 0)          # fixed -> reproducible archives

# Workspace-relative implementations tree published as files/feilian-code.zip.
# The v1.0.1 tree is the default; the historical tree stays available via --impl.
DEFAULT_IMPL = os.path.join("v1.0.1", "Implementations")

SPEC_CANDIDATES = [
    os.path.abspath(os.path.join(REPO, "..", "v1.0.1", "Specification_v1.0.1.pdf")),
    os.path.join(REPO, "files", "specification.pdf"),
    os.path.expanduser("~/Specification.pdf"),
]

ERRATUM_CANDIDATES = [
    os.path.abspath(os.path.join(REPO, "..", "v1.0.1", "FEILIAN_Erratum.pdf")),
    os.path.join(REPO, "files", "FEILIAN_Erratum.pdf"),
]


def human(n):
    return f"{n/1048576:.2f} MB" if n >= 1048576 else f"{n/1024:.1f} KB"


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def collect(ws, entries):
    """entries: [(arcname prefix, path relative to ws)] -> [(arcname, abspath)]."""
    out = []
    for prefix, rel in entries:
        src = os.path.join(ws, rel)
        if not os.path.exists(src):
            print(f"   ! missing, skipped: {rel}")
            continue
        if os.path.isfile(src):
            out.append((f"{prefix}/{os.path.basename(src)}", src))
            continue
        for root, dirs, files in os.walk(src):
            dirs.sort()
            for fn in sorted(files):
                full = os.path.join(root, fn)
                arc = os.path.join(prefix, os.path.relpath(full, src)).replace("\\", "/")
                out.append((arc, full))
    return out


def build_zip(target, payload, note):
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for arc, full in payload:
            zi = zipfile.ZipInfo(arc, date_time=ZIP_DATE)
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o644 << 16
            with open(full, "rb") as fh:
                z.writestr(zi, fh.read())
        zi = zipfile.ZipInfo("MANIFEST.txt", date_time=ZIP_DATE)
        zi.compress_type = zipfile.ZIP_DEFLATED
        z.writestr(zi, note)
    return target


def manifest_block(results):
    rows = []
    for (aid, title, sub, served, _kind), info in zip(ARTIFACTS, results):
        size = human(info["bytes"]) if info else ""
        sha = info["sha"][:16] + "…" if info else ""
        ready = "true" if info else "false"
        rows.append(
            f'  {{id:"{aid}", title:"{title}",\n'
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
                    help="write files/* and patch index.html (without this, nothing is written)")
    ap.add_argument("--workspace", default=os.path.dirname(REPO),
                    help="directory holding the submission material (default: parent of this repo)")
    ap.add_argument("--spec", default=None, help="path to the specification PDF")
    ap.add_argument("--erratum", default=None, help="path to the erratum PDF")
    ap.add_argument("--impl", default=DEFAULT_IMPL,
                    help="implementations directory, relative to the workspace "
                         f"(default: {DEFAULT_IMPL})")
    ap.add_argument("--with-bench", action="store_true", help="add the benchmark suite to the archive")
    ap.add_argument("--with-reference", action="store_true",
                    help="add the third-party reference implementation to the archive")
    ap.add_argument("--out", default=FILES, help="output directory (default: files/)")
    ap.add_argument("--no-patch", action="store_true",
                    help="build the artifacts but leave index.html untouched")
    args = ap.parse_args()

    ws = os.path.abspath(args.workspace)
    files_dir = os.path.abspath(args.out)

    spec = args.spec
    if spec is None:
        spec = next((c for c in SPEC_CANDIDATES if os.path.exists(c)), None)
    erratum = args.erratum
    if erratum is None:
        erratum = next((c for c in ERRATUM_CANDIDATES if os.path.exists(c)), None)
    srcs = {"spec": spec, "erratum": erratum}

    if not os.path.exists(INDEX):
        sys.exit(f"index.html not found at {INDEX}")

    print(f"repo      : {REPO}")
    print(f"workspace : {ws}{'' if os.path.isdir(ws) else '   (MISSING)'}")
    print(f"output    : {files_dir}")
    print(f"mode      : {'PUBLISH (writes files)' if args.publish else 'DRY RUN (no writes)'}\n")

    code_payload = collect(ws, [("implementations", args.impl)])
    arch_payload = collect(ws, [("implementations", args.impl),
                                ("kat", "KAT_current"),
                                ("appendix_b", "AppendixB_regeneration"),
                                ("python", "Python_Implementation")])
    if args.with_bench:
        arch_payload += collect(ws, [("bench", "FEILIAN_bench")])
    if args.with_reference:
        arch_payload += collect(ws, [("reference", "ZC-DM")])
    arch_payload += [(f"docs/{d}", os.path.join(ws, d))
                     for d in DOCS if os.path.exists(os.path.join(ws, d))]
    arch_payload = sorted(set(arch_payload))

    print(f"code bundle    : {len(code_payload):3d} files")
    print(f"archive bundle : {len(arch_payload):3d} files")
    print(f"spec pdf       : {'found  ' + spec if spec else 'NOT FOUND — pass --spec'}")
    print(f"erratum pdf    : {'found  ' + erratum if erratum else 'NOT FOUND — pass --erratum'}\n")

    if not args.publish:
        for arc, full in arch_payload[:12]:
            print(f"   {arc:60s} {human(os.path.getsize(full)):>9s}")
        if len(arch_payload) > 12:
            print(f"   … and {len(arch_payload)-12} more")
        print("\nNothing written. Re-run with --publish to assemble and enable.")
        return

    os.makedirs(files_dir, exist_ok=True)
    note = ("FEILIAN — specification compendium archive\n"
            "Specification version 1.0.1 (8 October 2026, 69 pp.)\n"
            "Erratum v1.0 -> v1.0.1 (October 2026) included in files/\n"
            "Interactive compendium: index.html in this repository.\n")
    build_zip(os.path.join(files_dir, "feilian-code.zip"), code_payload,
              "FEILIAN reference and optimized implementations (C + SystemVerilog)\n")
    build_zip(os.path.join(files_dir, "feilian-archive.zip"), arch_payload, note)

    results = []
    for _aid, _t, _s, served, kind in ARTIFACTS:
        if kind in ("spec", "erratum"):
            src = srcs[kind]
            if not src or not os.path.exists(src):
                print(f"   ! {kind} PDF not found — that card stays unpublished")
                results.append(None)
                continue
            dst = os.path.join(files_dir, served)
            # Guard: a PDF is its own default source on a rebuild, and opening
            # the destination for writing truncates it before it can be read.
            if os.path.abspath(src) != os.path.abspath(dst):
                with open(src, "rb") as a:
                    data = a.read()
                with open(dst, "wb") as b:
                    b.write(data)
        else:
            dst = os.path.join(files_dir, served)
        results.append({"bytes": os.path.getsize(dst), "sha": sha256_file(dst)})

    lines = [f"{info['sha']}  {served}"
             for (_a, _t, _s, served, _k), info in zip(ARTIFACTS, results) if info]
    with open(os.path.join(files_dir, "SHA256SUMS.txt"), "w",
              encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")

    if args.no_patch:
        print("   (--no-patch: index.html left untouched)")
    else:
        html = open(INDEX, encoding="utf-8").read()
        new = re.sub(r"/\* DOWNLOADS:BEGIN \*/.*?/\* DOWNLOADS:END \*/",
                     lambda _m: manifest_block(results), html, count=1, flags=re.S)
        if new == html:
            print("   ! manifest markers not found in index.html — page not patched")
        else:
            open(INDEX, "w", encoding="utf-8", newline="\n").write(new)

    print("\n=== published ===")
    for (_a, title, _s, served, _k), info in zip(ARTIFACTS, results):
        if info:
            print(f"  {title:16s} files/{served:24s} {human(info['bytes']):>9s}  {info['sha'][:16]}…")
        else:
            print(f"  {title:16s} (skipped)")
    print(f"\n  index.html manifest {'left untouched (--no-patch)' if args.no_patch else 'patched'}")
    print("  Commit the repository to publish. Verify a download with:")
    print("      python tools/verify_release.py")


if __name__ == "__main__":
    main()
