"""Link every UA-REAL message to its predictions, metadata and blind labels by full SHA-256 hashes.

The texts are not redistributed, so this script needs the local file ua_sample.xlsx (columns: text, label)
in the order used for the run. Usage:  python scripts/verify_ua_real.py path/to/ua_sample.xlsx

It writes data/ua_real_hashes.csv with, for each sample_id:
  sha256_raw_first1200   - SHA-256 of the first 1200 characters of the text as stored in the file (no normalisation)
  sha256_model_input     - SHA-256 of exactly what the models received: whitespace collapsed, stripped, first 1200 chars
and checks that the 16-character prefix of sha256_model_input equals sha256_16 in results/predictions.csv for all 94 items.
"""
import hashlib, re, sys
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
TEXT_CHARS = 1200
clean = lambda t: re.sub(r"\s+", " ", t).strip()[:5000] if isinstance(t, str) else ""   # = clean_text() in the notebook
h = lambda t: hashlib.sha256(t.encode("utf-8")).hexdigest()

src = pd.read_excel(sys.argv[1]) if sys.argv[1].endswith("xlsx") else pd.read_csv(sys.argv[1])
idmap = pd.read_csv(ROOT / "data/ua_real_id_map.csv", encoding="utf-8-sig")
assert len(src) == len(idmap) == 94, len(src)
out = pd.DataFrame({"sample_id": idmap.sample_id, "label": src["label"].astype(int),
                    "sha256_raw_first1200": [h(str(t)[:TEXT_CHARS]) for t in src["text"]],
                    "sha256_model_input": [h(clean(t)[:TEXT_CHARS]) for t in src["text"]]})
out["matches_predictions"] = out.sha256_model_input.str[:16].values == idmap.sha256_16_predictions.values
out["label_matches"] = out.label.values == idmap.label_metadata.values
out.to_csv(ROOT / "data/ua_real_hashes.csv", index=False, encoding="utf-8-sig")
print(f"model-input hash matches predictions: {int(out.matches_predictions.sum())}/94; labels match: {int(out.label_matches.sum())}/94")
print(f"raw-text hash matches old metadata hash: {int((out.sha256_raw_first1200.str[:16] == idmap.sha256_16_metadata).sum())}/94")
