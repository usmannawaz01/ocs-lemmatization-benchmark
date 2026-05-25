import os
from pathlib import Path

import stanza
from huggingface_hub import snapshot_download
from stanza.utils.conll import CoNLL

INPUT_TXT = r"path/to/input.txt"
OUTPUT_CONLLU = r"path/to/output.conllu"
MODEL_VARIANT = "combined"

repo_dir = snapshot_download(
    repo_id="usmannawaz/old-church-slavonic-tokenizer-lemmatizer",
    local_dir=r"hf_models/old-church-slavonic-tokenizer-lemmatizer",
)

model_dir = Path(repo_dir)

stanza_dir = os.path.join(os.path.expanduser("~"), "stanza_resources")
os.environ["STANZA_RESOURCES_DIR"] = stanza_dir

stanza.download(
    lang="cu",
    model_dir=stanza_dir,
    processors={"pos": "proiel_nocharlm"},
    package=None,
    verbose=False,
)

tokenizer_model = model_dir / "models" / MODEL_VARIANT / "tokenize" / "cu_proiel_tokenizer.pt"
lemma_model = model_dir / "models" / MODEL_VARIANT / "lemma" / "cu_proiel_nocharlm_lemmatizer.pt"

print("Tokenizer exists:", tokenizer_model.exists(), tokenizer_model)
print("Lemma exists:", lemma_model.exists(), lemma_model)

nlp = stanza.Pipeline(
    lang="cu",
    dir=stanza_dir,
    package=None,
    processors={
        "tokenize": "proiel",
        "pos": "proiel_nocharlm",
        "lemma": "proiel_nocharlm",
    },
    tokenize_model_path=str(tokenizer_model),
    lemma_model_path=str(lemma_model),
    tokenize_pretokenized=False,
    verbose=False,
    use_gpu=False,
)

with open(INPUT_TXT, "r", encoding="utf-8") as f:
    raw_text = f.read()

doc = nlp(raw_text)

output_dir = os.path.dirname(OUTPUT_CONLLU)
if output_dir:
    os.makedirs(output_dir, exist_ok=True)

with open(OUTPUT_CONLLU, "w", encoding="utf-8") as fout:
    CoNLL.write_doc2conll(doc, fout)

print("Wrote:", OUTPUT_CONLLU)
