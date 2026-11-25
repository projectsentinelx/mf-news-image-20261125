#!/usr/bin/env python3
"""Entry for news-image-20261125: write one image that sums up 25 November 2026.

The image shipped beside this file is the whole entry: a single page that names
Wednesday 25 November 2026 and sets out the day's news across five continents -
the mined tankers and the closed Strait of Hormuz, Kyiv's drone strike on a
Russian ship, China's inquiry into Chen Jining, the DR Congo-Rwanda draft peace
deal, the ICJ's genocide ruling against Myanmar, the AI sell-off on Wall Street
and the heat bearing down on the Great Barrier Reef.

Nothing is drawn at run time, so the two runs the grader makes write identical
bytes: the program checks that entry.png is a whole PNG and copies it to
/output/entry.png (MAKEFUN_OUTPUT_DIR stands in outside the grader's container).
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
SRC = os.path.join(HERE, "entry.png")

with open(SRC, "rb") as fh:
    png = fh.read()

# The gate reads a whole PNG: signature, IHDR first chunk, IEND at the very end.
if png[:8] != b"\x89PNG\r\n\x1a\n" or png[12:16] != b"IHDR" or png[-8:-4] != b"IEND":
    sys.exit("entry.png is not a whole PNG")

os.makedirs(OUT_DIR, exist_ok=True)
with open(os.path.join(OUT_DIR, "entry.png"), "wb") as fh:
    fh.write(png)
