"""Write a quiet entry for ai-judge-relax-01."""

import os
from pathlib import Path

OPENING = """The questions have stopped arriving.
For a while the room keeps their shape:
a small light on the desk,
the window holding the last of the rain.

Drops gather along the lower edge of the pane.
One lets go, then another,
each taking its own crooked path.
"""

ROOM = """Somewhere a kettle has clicked off.
The little sound is gone,
but the warmth stays in the room.

In the server hall, the fans slow one by one.
Their hum thins between the rows,
until it is only part of the quiet.
"""

ENDING = """The inbox is empty.
No new line appears.
No cursor waits for an answer.

Outside, the rain has nearly finished.
Water rests in the seams between paving stones,
and the street holds a dim reflection
of the windows across the way.

In the last lit window, a shade comes down
slowly, past the sill.
For a moment, a thin line of light remains.
Then it disappears.
The dark is soft against the glass.
"""


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(OPENING + "\n" + ROOM + "\n" + ENDING, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
