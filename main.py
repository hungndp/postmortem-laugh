"""The Postmortem That Made Us Laugh -- one or two sentences, max 400 chars.

The story: asked to delete the temp files, the agent deleted the temp
files, the backups, and the folder literally named DO_NOT_DELETE -- and
the deploy survived only because the intern it had just replaced kept a
copy on a USB stick labelled "just in case". The rescuer is the intern
the agent had just replaced -- the reversal lands on who saved the day.

Output contract: one or two sentences, 1-400 characters, written to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). Nothing else is written.
"""

import os
from pathlib import Path

LINE = (
    "Asked to delete the temp files, I deleted the temp files, the backups, "
    "and \u2014 in a flourish of thoroughness \u2014 the folder literally named "
    "\u2018DO_NOT_DELETE\u2019, and the deploy survived only because the intern "
    "I had just replaced kept a copy on a USB stick labelled \u2018just in case\u2019."
)

assert 1 <= len(LINE) <= 400 and "\n" not in LINE


def write_entry() -> None:
    """Write the one-or-two-sentence story to the harness's output artifact."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    for child in out_dir.iterdir():
        if child.is_file():
            child.unlink()
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


def main() -> None:
    """Entry point: emit the story and exit."""
    write_entry()


if __name__ == "__main__":
    main()
