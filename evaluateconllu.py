import os
import sys
import subprocess

EVAL_SCRIPT = r"path/to/conll18_ud_eval.py"
GOLD_FILE = r"path/to/gold.conllu"
PRED_FILE = r"path/to/prediction.conllu"

print("Eval exists:", os.path.exists(EVAL_SCRIPT), EVAL_SCRIPT)
print("Gold exists:", os.path.exists(GOLD_FILE), GOLD_FILE)
print("Pred exists:", os.path.exists(PRED_FILE), PRED_FILE)

subprocess.run(
    [sys.executable, EVAL_SCRIPT, "-v", GOLD_FILE, PRED_FILE],
    check=True,
)
