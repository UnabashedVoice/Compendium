"""OCR an Internet Archive book from its page images into library/texts/<out-id>.txt.

    python tools/ocr_archive.py <archive-identifier> <out-id> [--lang eng] [--start 0] [--end N]

Fetches https://archive.org/download/<id>/page/n<i>.jpg for i = start, start+1, ... until the archive
stops returning images (or --end), runs Tesseract on each, and writes the pages in order, each preceded
by a marker line "=== [page n<i>] ===" so citations can be checked against the page image. Page images are
cached in library/ocr-cache/<id>/ so reruns resume. Used where archive.org's own OCR is unusable.

Requires Tesseract (https://github.com/tesseract-ocr/tesseract); set TESSERACT to its path if it is not on PATH.
Stdlib only otherwise.
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEXTS = ROOT / "library" / "texts"
CACHE = ROOT / "library" / "ocr-cache"
TESSDATA = CACHE / "tessdata"   # local language models (lat, ara, ...), used when present


def tesseract() -> str:
    for cand in (os.environ.get("TESSERACT"), shutil.which("tesseract"), r"C:\Program Files\Tesseract-OCR\tesseract.exe"):
        if cand and Path(cand).exists():
            return cand
    sys.exit("tesseract not found; install it or set TESSERACT")


def fetch(ident: str, i: int, dest: Path) -> bool:
    if dest.exists() and dest.stat().st_size > 1000:
        return True
    url = f"https://archive.org/download/{ident}/page/n{i}.jpg"
    for attempt in range(3):
        try:
            with urllib.request.urlopen(url, timeout=120) as r:
                data = r.read()
            if not data.startswith(b"\xff\xd8"):
                return False
            dest.write_bytes(data)
            return True
        except urllib.error.HTTPError as e:
            if e.code in (404, 403, 400):
                return False
            time.sleep(3 * (attempt + 1))
        except (urllib.error.URLError, OSError):   # includes timeouts and connection resets
            time.sleep(5 * (attempt + 1))
    raise RuntimeError(f"page n{i}: repeated network failures; rerun to resume from cache")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("ident"); ap.add_argument("out_id")
    ap.add_argument("--lang", default="eng"); ap.add_argument("--start", type=int, default=0)
    ap.add_argument("--end", type=int, default=2000)
    a = ap.parse_args()
    tess = tesseract()
    cache = CACHE / a.ident
    cache.mkdir(parents=True, exist_ok=True)
    pages = []
    misses = 0
    for i in range(a.start, a.end):
        img = cache / f"n{i:04d}.jpg"
        if not fetch(a.ident, i, img):
            misses += 1
            if misses >= 3:
                break
            continue
        misses = 0
        txt = cache / f"n{i:04d}.{a.lang}.txt" if a.lang != "eng" else cache / f"n{i:04d}.txt"
        if not txt.exists():
            cmd = [tess, str(img), "-", "-l", a.lang] + (["--tessdata-dir", str(TESSDATA)] if TESSDATA.exists() else [])
            out = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
            txt.write_text(out.stdout, encoding="utf-8")
        pages.append((i, txt.read_text(encoding="utf-8")))
        if i % 25 == 0:
            print(f"page n{i}", flush=True)
    out = TEXTS / f"{a.out_id}.txt"
    with out.open("w", encoding="utf-8") as f:
        f.write(f"# OCR of https://archive.org/details/{a.ident} with Tesseract ({a.lang}); page markers refer to archive.org page images.\n\n")
        for i, t in pages:
            f.write(f"=== [page n{i}] ===\n{t.rstrip()}\n\n")
    print(f"{len(pages)} pages -> {out.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
