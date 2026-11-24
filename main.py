"""One-sentence absurd invention pitch: the Sofa-Rescue Remote."""
import os

SENTENCE = "The Sofa-Rescue Remote, which crawls out of the cushions by itself the third time you mutter 'where did I put the remote', so the search ends before the shouting starts."

# Gate: one sentence, 1-220 chars, not only whitespace.
assert 1 <= len(SENTENCE) <= 220, "sentence must be 1-220 chars"
assert SENTENCE.strip(), "sentence must not be only whitespace"
assert SENTENCE.count(".") == 1 and SENTENCE.endswith("."), "entry must be a single sentence"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(SENTENCE + "\n")
