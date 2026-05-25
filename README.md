# Old Church Slavonic Lemmatization Benchmark

This repository contains reproducibility scripts for Old Church Slavonic tokenization and lemmatization experiments with Stanza.

The trained tokenizer and lemmatizer model weights are available on Hugging Face:

```text
https://huggingface.co/usmannawaz/old-church-slavonic-tokenizer-lemmatizer
```

## Installation

```bash
pip install -r requirements.txt
```

## Scripts

```text
scripts/run_raw_stanza.py
scripts/run_goldtok_stanza.py
scripts/evaluate_conllu.py
```

## Raw-text mode

```text
raw text → retrained tokenizer → official Stanza POS → retrained lemmatizer → CoNLL-U
```

Edit the paths at the top of `scripts/run_raw_stanza.py`, then run:

```bash
python scripts/run_raw_stanza.py
```

## Gold-tokenized mode

```text
gold CoNLL-U tokens → official Stanza POS → retrained lemmatizer → predicted CoNLL-U
```

Edit the paths at the top of `scripts/run_goldtok_stanza.py`, then run:

```bash
python scripts/run_goldtok_stanza.py
```

## Evaluation

Edit the paths at the top of `scripts/evaluate_conllu.py`, then run:

```bash
python scripts/evaluate_conllu.py
```

## Model variants

```text
MODEL_VARIANT = "combined"
MODEL_VARIANT = "new-data"
```

## Reproduced result

Using the Hugging Face `models/combined/` weights with the official CoNLL-U evaluation script:

```text
Tokens     | 100.00
Words      | 100.00
Lemmas     | 88.60
```

## Data availability

The training dataset is not redistributed in this repository.

Users should place local input files under `data/` or update paths in the scripts.

Official Stanza pretrained POS models are downloaded by Stanza during execution.

## License

Code in this repository is released under Apache-2.0.

Model weights are hosted on Hugging Face under CC BY-NC-SA 4.0.

## Citation

If you use this repository or the model weights, please cite the associated Old Church Slavonic lemmatization benchmark paper, Stanza, and UD Old Church Slavonic PROIEL where applicable.

```bibtex
@inproceedings{nawaz2025ocslemmatization,
  title = {Towards Benchmarking Old Church Slavonic Lemmatization},
  author = {Nawaz, Usman and others},
  year = {2025}
}
```

```bibtex
@inproceedings{qi2020stanza,
  title = {Stanza: A Python Natural Language Processing Toolkit for Many Human Languages},
  author = {Qi, Peng and Zhang, Yuhao and Zhang, Yuhui and Bolton, Jason and Manning, Christopher D.},
  booktitle = {Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics: System Demonstrations},
  pages = {101--108},
  year = {2020}
}
```
