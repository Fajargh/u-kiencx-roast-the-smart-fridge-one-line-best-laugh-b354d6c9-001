"""Roast the Smart Fridge: one line, best laugh wins.

Writes a single roast line (at most 160 characters) to
/output/entry.txt, or to $MAKEFUN_OUTPUT_DIR/entry.txt when set.
"""

import os

LINE = "My smart fridge has a camera, Wi-Fi, and a touchscreen — and still just watches me eat cake at 2am. It's a $3,000 witness with a light inside."


def main():
    # The gate requires 1-160 UTF-8 characters, not only whitespace.
    assert 1 <= len(LINE) <= 160, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
