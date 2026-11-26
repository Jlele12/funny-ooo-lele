#!/usr/bin/env python3
"""Entry for Funniest One-Line Out-of-Office Reply (u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8).

Writes one line (max 200 characters) for the judge to /output/entry.txt:
the brief's ask, landed in a single read, grounded and specific. No network,
no randomness: every run writes the same text so both graded runs match
byte for byte.
"""
from pathlib import Path

LINE = "Out of office until Monday. If it's urgent, it isn't: your email moved to a folder I named 'someday', which has a waiting list."


def main() -> None:
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    entry_path = out / "entry.txt"
    entry_path.write_text(text, encoding="utf-8")
    print(text, f"({len(text)} chars)")


if __name__ == "__main__":
    main()
