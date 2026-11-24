#!/usr/bin/env python3
"""Monday, Reviewed in One Line — entry writer.

Writes a single one-line review of Monday (under 200 characters)
to /output/entry.txt. One sharp irony, in the voice of a product
review: a star rating, a bug report, and a recommendation that
collapses on itself.
"""

import os

ENTRY = (
    "Monday: 1 star. The alarm snoozed itself, my inbox filed 47 "
    "complaints, and standup wanted updates on a week I hadn't "
    "lived yet. Would not recommend."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
