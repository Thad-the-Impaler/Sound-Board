"""Build index.html: board.html with every clip in sounds/ built in.

Browsers often can't read files next to a page opened from disk (Chrome blocks
fetch() on file://, and macOS can block reading iCloud Drive folders), so the
local board carries its sounds inside the page as base64.

Usage:  python3 tools/build_index.py
"""
import base64
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    src = open(os.path.join(ROOT, "board.html"), encoding="utf-8").read()
    ids = re.findall(r'\{ id: "([a-z0-9-]+)", label:', src)
    sounds = {}
    for pad_id in ids:
        with open(os.path.join(ROOT, "sounds", pad_id + ".mp3"), "rb") as f:
            sounds[pad_id] = base64.b64encode(f.read()).decode("ascii")

    body = re.sub(r'^<meta charset="utf-8">\n', "", src)
    inline = "<script>window.BOOM_SOUNDS = " + json.dumps(sounds, separators=(",", ":")) + ";</script>\n"
    k = body.index("<script>")
    body = body[:k] + inline + body[k:]
    html = (
        '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        "</head>\n<body>\n" + body + "\n</body>\n</html>\n"
    )
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"{len(ids)} pads, {len(sounds)} sounds built in, index.html = {len(html) / 1e6:.2f} MB")


if __name__ == "__main__":
    main()
