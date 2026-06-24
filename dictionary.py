from pathlib import Path
from collections import Counter, defaultdict
import unicodedata

TRAIN = r"path train.conllu"
TEST = r"path test.conllu"


def tokens(path):
    with Path(path).open(encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line or line.startswith("#"):
                continue
            cols = line.split("\t")
            if len(cols) != 10:
                continue
            if "-" in cols[0] or "." in cols[0]:
                continue
            yield norm(cols[1]), norm(cols[2])


d = defaultdict(Counter)
def norm(x):
    return unicodedata.normalize("NFC", x.strip()).replace("ⷦ͡", "ⷦ͡")

for form, lemma in tokens(TRAIN):
    d[form][lemma] += 1

lexicon = {form: lemmas.most_common(1)[0][0] for form, lemmas in d.items()}

total = correct = oov = oov_correct = 0

for form, gold in tokens(TEST):
    total += 1
    pred = lexicon.get(form, form)

    if form not in lexicon:
        oov += 1
        if pred == gold:
            oov_correct += 1

    if pred == gold:
        correct += 1

print(f"tokens: {total}")
print(f"correct: {correct}")
print(f"accuracy: {correct / total * 100:.2f}")
