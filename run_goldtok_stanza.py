import os
from pathlib import Path

import stanza
from huggingface_hub import snapshot_download
from stanza.utils.conll import CoNLL

INPUT_CONLLU = r"path/to/gold.conllu"
OUTPUT_CONLLU = r"path/to/prediction.goldtok.conllu"
MODEL_VARIANT = "combined"

repo_dir = snapshot_download(
    repo_id="usmannawaz/old-church-slavonic-tokenizer-lemmatizer",
    local_dir=r"hf_models/old-church-slavonic-tokenizer-lemmatizer",
)

model_dir = Path(repo_dir)

stanza_dir = os.path.join(os.path.expanduser("~"), "stanza_resources")

stanza.download(
    lang="cu",
    model_dir=stanza_dir,
    processors={"pos": "proiel_nocharlm"},
    package=None,
    verbose=False,
)

sentences = []
current = []

with open(INPUT_CONLLU, "r", encoding="utf-8") as f:
    for line in f:
        line = line.rstrip("\n")

        if not line:
            if current:
                sentences.append(current)
                current = []
            continue

        if line.startswith("#"):
            continue

        cols = line.split("\t")
        if len(cols) != 10:
            continue

        if "-" in cols[0] or "." in cols[0]:
            continue

        current.append(cols[1])

if current:
    sentences.append(current)

lemma_model = model_dir / "models" / MODEL_VARIANT / "lemma" / "cu_proiel_nocharlm_lemmatizer.pt"

print("Lemma exists:", lemma_model.exists(), lemma_model)

nlp = stanza.Pipeline(
    lang="cu",
    dir=stanza_dir,
    processors="tokenize,pos,lemma",
    package=None,
    pos_package="proiel_nocharlm",
    lemma_model_path=str(lemma_model),
    tokenize_pretokenized=True,
    verbose=False,
    use_gpu=False,
)

doc = nlp(sentences)

output_dir = os.path.dirname(OUTPUT_CONLLU)
if output_dir:
    os.makedirs(output_dir, exist_ok=True)

with open(OUTPUT_CONLLU, "w", encoding="utf-8") as fout:
    CoNLL.write_doc2conll(doc, fout)

print("Wrote:", OUTPUT_CONLLU)
