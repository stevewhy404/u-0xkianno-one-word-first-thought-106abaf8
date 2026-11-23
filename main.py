"""One Word, First Thought.

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt.

The word is the first that comes to mind: "kerfuffle" -- a commotion
or fuss, especially one caused by a disagreement. Surprising, vivid,
and with a playful sound that rewards a second look.
"""

import os

WORD = "kerfuffle"  # 9 characters, within the 1-24 gate


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
