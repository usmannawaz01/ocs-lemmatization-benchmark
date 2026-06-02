# Towards Benchmarking Old Church Slavonic Lemmatization

This repository contains reproducibility scripts for Old Church Slavonic tokenization and lemmatization experiments with Stanza.

The trained tokenizer and lemmatizer model weights are available on Hugging Face:

```text
https://huggingface.co/usmannawaz/old-church-slavonic-tokenizer-lemmatizer
```

An interactive demo is available at: [OCS Combined Lemmatizer Demo](https://usmannawaz01.github.io/old-church-slavonic-tokenizer-lemmatizer/). 

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

Edit the paths at the top of `scripts/runrawstanza.py`, then run:

```bash
python scripts/runrawstanza.py
```

## Gold-tokenized mode

```text
gold CoNLL-U tokens → official Stanza POS → retrained lemmatizer → predicted CoNLL-U
```

Edit the paths at the top of `scripts/rungoldtokstanza.py`, then run:

```bash
python scripts/rungoldtokstanza.py
```

## Evaluation

Edit the paths at the top of `scripts/evaluateconllu.py`, then run:

```bash
python scripts/evaluateconllu.py
```

## Model variants

```text
MODEL_VARIANT = "combined"
MODEL_VARIANT = "new-data"
```

## Data availability

We release the annotated OCS dataset under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International license (CC BY-NC-SA 4.0) for non-commercial research purposes.

The UD 2.12 OCS data used in the combined experiments is not redistributed in this repository, since it is already publicly available from the Universal Dependencies treebanks. To reproduce the combined-data experiments, users should download UD 2.12 OCS from Universal Dependencies and combine it with the new data.

A major part of the  data is derived from Azbuka materials, and additional material is derived from Cyrillomethodiana. We have obtained permission to use and release these materials for non-commercial research purposes. The original source texts remain the property of their respective source providers.




## License

The annotated OCS data and retrained model weights are released for non-commercial research use under CC BY-NC-SA 4.0.

The UD 2.12 OCS data is not redistributed here and remains subject to the license and terms of the Universal Dependencies treebanks.

This repository provides scripts to load the models, run inference, and evaluate the outputs. Model training followed the standard Stanza training procedure described in the [official Stanza training documentation](https://stanfordnlp.github.io/stanza/training.html).

This work uses Stanza, which is released under the Apache License 2.0.

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
