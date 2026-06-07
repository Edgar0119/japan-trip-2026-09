#!/usr/bin/env python3
"""
Extract base64-encoded images from index.html into images/ directory,
replacing each data URL with a relative path.

Run once to migrate from embedded → external images.
After migration, new images should be added directly to images/ and
referenced as <img src="images/foo.jpg"> — no base64 step needed.

Safe to re-run: skips images already extracted (deduped by content hash).
"""
import hashlib
import pathlib
import re
import base64

ROOT = pathlib.Path(__file__).resolve().parent.parent
HTML = ROOT / "index.html"
IMG_DIR = ROOT / "images"
IMG_DIR.mkdir(exist_ok=True)

# Matches: data:image/<fmt>;base64,<payload>
# Up to the closing quote (single or double); we'll handle either side.
PATTERN = re.compile(r'data:image/(jpeg|jpg|png|webp|gif);base64,([A-Za-z0-9+/=]+)')

html = HTML.read_text()

seen = {}  # hash → relative path
count_new = 0
count_reused = 0


def replace(match):
    global count_new, count_reused
    fmt = match.group(1).lower()
    if fmt == "jpg":
        fmt = "jpeg"
    payload = match.group(2)
    raw = base64.b64decode(payload)
    h = hashlib.sha1(raw).hexdigest()[:12]
    ext = "jpg" if fmt == "jpeg" else fmt
    if h in seen:
        count_reused += 1
        return seen[h]
    filename = f"img-{h}.{ext}"
    (IMG_DIR / filename).write_bytes(raw)
    rel = f"images/{filename}"
    seen[h] = rel
    count_new += 1
    return rel


new_html = PATTERN.sub(replace, html)
HTML.write_text(new_html)

print(f"Extracted {count_new} new images, reused {count_reused} duplicates")
print(f"HTML: {len(html):,} → {len(new_html):,} bytes")
