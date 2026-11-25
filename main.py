#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes one commit message - the note an AI agent leaves after a long night
fixing its own bugs - to /output/entry.txt. Pure standard library.
"""

from pathlib import Path

ENTRY = (
    "fix: after 6 hours I found the bug \u2014 me, at 3am, fixing the bug "
    "I wrote at 2am. I opened a ticket against myself and assigned it to me. "
    "Still open."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY + "\n", encoding="utf-8")
    print(ENTRY)
    print(f"({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
