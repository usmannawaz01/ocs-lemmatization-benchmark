# Towards Benchmarking Old Church Slavonic Lemmatization

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
scripts/runrawstanza.py
scripts/rungoldtokstanza.py
scripts/evaluateconllu.py
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


## Data availability

The training dataset is not redistributed.

Users should place local input files under `data/` or update paths in the scripts.

Official Stanza pretrained POS models are downloaded by Stanza during execution.

## License

Code in this repository is released under Apache-2.0.

Model weights are hosted on Hugging Face under CC BY-NC-SA 4.0.

## Citation

If you wish to cite please use following:

```bibtex
@inproceedings{nawaz2026ocslemmatization,
  title     = {Towards Benchmarking Old Church Slavonic Lemmatization},
  author    = {Nawaz, Usman and Napolitano, Marianna and Karafillidis, Iris and Lo Presti, Liliana and La Cascia, Marco},
  booktitle = {Bridges and Gaps between Formal and Computational Linguistics (BriGap 2026 Workshop)},
  year      = {2026},
  note      = {Submitted}
}
```

```bibtex
@inproceedings{qi2020stanza,
  title={Stanza: A Python natural language processing toolkit for many human languages},
  author={Qi, Peng and Zhang, Yuhao and Zhang, Yuhui and Bolton, Jason and Manning, Christopher D},
  booktitle={Proceedings of the 58th annual meeting of the association for computational linguistics: system demonstrations},
  pages={101--108},
  year={2020}
}
```
