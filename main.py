"""Entry program for the 'Warning Label for Humans: One Line, Big Laugh' make.fun bounty.

The entry is a single-line safety warning label that should come printed
on every human being, at most 160 characters. The program writes exactly
that one line to /output/entry.txt (an optional first argument overrides
the destination for a dry run).
"""

import sys
from pathlib import Path

LINE = (
    "WARNING: This human runs on coffee, sleep, and Wi-Fi. "
    "Remove any one and expect sudden shutdowns, loud noises, "
    "and strong opinions."
)
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert 1 <= len(LINE) <= 160, "entry must be 1-160 characters"
    assert LINE.strip() and "\n" not in LINE, "entry must be one line"
    assert LINE.startswith("WARNING:"), "a warning label starts with WARNING:"
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE + "\n", encoding="utf-8")
    assert target.read_text(encoding="utf-8") == LINE + "\n", "round-trip check failed"
    print(f"wrote {target} ({len(LINE)} chars)")


if __name__ == "__main__":
    main(sys.argv)
