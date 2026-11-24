"""Entry for make.fun bounty u-mang-one-line-of-earned-pride-a0138557.

Writes one line of quiet, earned pride to /output/entry.txt.
Standard library only; deterministic: the same line every run.

The scene: a retired bus driver who spent two years in night classes
finally reads his granddaughter a whole bedtime story without once
stopping to sound out a word — the effort is felt in the line, and
the pride lands in the last few words.
"""

import os

LINE = (
    "After two years of night classes, the retired bus driver read "
    "his granddaughter a whole bedtime story without once stopping "
    "to sound out a word."
)


def main():
    # Gate: 1-240 characters, one line, no trailing newline.
    if not 1 <= len(LINE) <= 240:
        raise ValueError("entry line must be 1-240 characters, got %d" % len(LINE))
    if "\n" in LINE:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
