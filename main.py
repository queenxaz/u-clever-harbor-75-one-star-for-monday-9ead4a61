"""One star for Monday — make.fun entry program.

Writes the one-line review to /output/entry.txt.
"""
# Design notes — why this line should win:
# The restaurant frame is played straight: the waiter is the alarm, and
# it screams. The punch lands on the last words — already late for
# Tuesday — which is the Monday-specific joke no other day can carry.
# Every word earns its place; nothing explains the joke after telling it.

ENTRY = "One star. Showed up at 9am, no coffee, the waiter \u2014 my alarm \u2014 screamed at me. Left hungry, tired, and already late for Tuesday."

MAX_CHARS = 180
MAX_WORDS = 25

def main():
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, limit {MAX_CHARS}"
    if MAX_WORDS is not None:
        assert len(ENTRY.split()) <= MAX_WORDS, f"entry is {len(ENTRY.split())} words, limit {MAX_WORDS}"
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
