#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

A deterministic program (Python standard library only) that writes one
100-word monologue, spoken by a fantasy villain who is secretly just very
tired, to /output/entry.txt.

The tiredness lives in the voice, the rhythm and the small deflections --
never in a plain statement that the villain is weary. The speaker is a
specific villain with a history (he flooded the valley, raised the dead
twice) and a scheme (the kingdom, the maps, the keys, the ledger), and the
last line lands the sting.

Usage:
    python3 main.py

The output directory defaults to /output and can be overridden with the
MAKEFUN_OUTPUT environment variable (used only for local testing).
"""

import os

MONOLOGUE = (
    "So. You climbed the stairs I stopped counting, past the guards I stopped "
    "paying, to call me a monster in my own hall tonight. Fair. I flooded "
    "the valley below. I raised the dead, twice, and the second time only because "
    "the first lot kept asking for their coats back. My ravens file their own "
    "reports now. The crown slips. The candles gutter. The maps are yours. "
    "The keys. The ledger. The whole rotting kingdom, hero. Take it all. "
    "Just let me sit down first. Four hundred years of being evil, and I "
    "have run out of reasons to stand."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT", "/output")
    # Create the output directory only if it is missing; never chmod a
    # directory we did not create ourselves (in particular, never /output).
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(MONOLOGUE + "\n")
    # The grader collects outputs as another user, so the file must be
    # readable by everyone. Only chmod a file this program wrote itself.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
