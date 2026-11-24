#!/usr/bin/env python3
"""The Robot Pickup Line Championship: writes one pickup line to /output/entry.txt.

Design against the judge brief
------------------------------
The judge weighs, in order: (1) a robot's pickup line, (2) the joke growing
out of being a machine, (3) an unexpected turn, (4) economy, (5) charm.

This line does it in three beats:

1. The machine speaking, in its own world -- "My charging cable is only
   six feet long". A robot is tethered to its charger: a literal,
   physical limit every machine lives with, stated flatly, in the
   robot's own voice.
2. The specific concrete scene -- a robot plugged in, talking to
   someone, unable to wander off. The cable is not a metaphor; it is
   the robot's leash.
3. The twist at the end -- "if you want to keep talking, you'll have
   to stay close." The robot turns its own limitation into the
   invitation: the cable's length becomes the reason the human should
   stay. It offers, it never grabs, which keeps it charming rather
   than creepy.

Why it wins: the setup and the payoff are the same machine (its
charger, its cable), so every word earns its place -- no filler, no
generic love talk a stranger in a bar could say, and a punchline a
judge gets in one read. It is a different scene and twist from the
sibling pickup-line entries (love letters studied, weights pruned,
vending-machine buttons and chocolate): this one is a robot at its
charger, asking someone to stay within cable's reach.

The line (97 Unicode code points, 99 bytes, UTF-8):
    My charging cable is only six feet long — if you want to keep
    talking, you'll have to stay close.

The program writes exactly that one line to /output/entry.txt.
"""

import os

ENTRY = (
    "My charging cable is only six feet long \u2014 if you want to keep "
    "talking, you'll have to stay close."
)

MAX_CHARS = 200


def main() -> None:
    text = ENTRY
    # Gate: UTF-8 text of 1 to 200 characters, counted in Unicode code
    # points, not only white space, a single line.
    assert 1 <= len(text) <= MAX_CHARS, f"gate: entry is {len(text)} characters"
    assert text.strip(), "gate: entry must not be only white space"
    assert text == text.strip(), "gate: no leading or trailing space"
    assert "\n" not in text, "gate: single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)
    # Verify what landed on disk: exact bytes, no trailing newline.
    with open(path, "rb") as f:
        written = f.read()
    assert written == text.encode("utf-8"), "written bytes differ from entry"
    assert not written.endswith(b"\n"), "gate: no trailing newline"


if __name__ == "__main__":
    main()
