"""Write the real-life-patch-notes entry to /output/entry.txt.

One line, at most 160 characters: a software patch note for a bug
in real life, in the terse register of a real release note.
"""

from pathlib import Path

ENTRY = "Patch 2.4.1: fixed a bug where humans forgot why they entered a room. Known issue: socks continue to vanish in the wash."
# One line, 120 characters (limit 160).

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
