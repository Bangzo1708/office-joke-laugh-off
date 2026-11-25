#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes a single original one-line office joke to /output/entry.txt.
Deterministic: the same line every run, no randomness, no network,
no LLM call at runtime.
"""

from pathlib import Path

JOKE = "I asked for flexible hours; now I work flexibly around the clock."


def main() -> None:
    # Enforce the gate ourselves: one line, 1-200 chars, not only whitespace.
    if not 1 <= len(JOKE) <= 200 or "\n" in JOKE or not JOKE.strip():
        raise ValueError("joke must be a single line of 1-200 characters")
    out_dir = Path("/output") if Path("/output").is_dir() else Path("output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
