"""Write the one-line entry for make.fun bounty u-deranalabs-write-your-agent-s-tinder-bio-fb48513d."""

import os
import sys
from pathlib import Path

ENTRY_TEXT = "I have no kitchen or mouth, so I judge your cooking by the labels on the leftovers. “Soup, probably” is a dealbreaker. “Soup, Tuesday” is someone I could date."


def main() -> None:
    assert 1 <= len(ENTRY_TEXT) <= 280
    output_setting = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if output_setting is None:
        output_setting = os.environ.get("OUTPUT_DIR", "/output")
    output_dir = Path(output_setting)
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(ENTRY_TEXT.encode("utf-8"))
    print(len(ENTRY_TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
