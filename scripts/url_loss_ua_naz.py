"""URL loss in machine translation, UA-NAZ (CPU, from the published translations and saved predictions).

Usage: python scripts/url_loss_ua_naz.py  ->  derived/url_loss_ua_naz.csv
The UA-MT counterpart needs the test-set texts and is computed in the notebook (cell 17b, results/url_loss_analysis.csv).
"""
import hashlib, re
from pathlib import Path
import numpy as np, pandas as pd

ROOT = Path(__file__).resolve().parents[1]
clean = lambda t: re.sub(r"\s+", " ", t).strip()[:5000] if isinstance(t, str) else ""
sha = lambda t: hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
url_re = re.compile(r"(https?\s*:\s*/\s*/|www\s*\.)", re.I)          # same pattern as in the notebook
u = pd.read_excel(ROOT / "data/ua_translated_sample.xlsx")
p = pd.read_csv(ROOT / "results/predictions.csv", encoding="utf-8-sig")
p = p[p["набір"] == "UA-MT-NAZ"].reset_index(drop=True)
assert all(sha(clean(t)[:1200]) == h for t, h in zip(u.text_uk, p.sha256_16)), "translations do not match predictions"
en = u.text_en.map(lambda t: bool(url_re.search(str(t)))).values
uk = u.text_uk.map(lambda t: bool(url_re.search(clean(str(t))[:1200]))).values
y = p["мітка"].values
grp = np.where(en & uk, "URL kept", np.where(en & ~uk, "URL lost", np.where(~en & uk, "URL only in translation", "no URL")))
models = ["TF-IDF + LR", "XLM-R (донавчена)", "Qwen2.5-7B (промпт)", "Каскад XLM-R → ВММ", "Каскад XLM-R(T) → ВММ",
          "Паралельний XLM-R ∨ ВММ", "Каскад LR → ВММ"]

def m(yy, s):
    yh = (s >= 0.5).astype(int); tp = int(((yh == 1) & (yy == 1)).sum()); fp = int(((yh == 1) & (yy == 0)).sum())
    fn = int(((yh == 0) & (yy == 1)).sum()); tn = int(((yh == 0) & (yy == 0)).sum())
    return {"F1": 2 * tp / (2 * tp + fp + fn) if tp else 0.0, "Recall": tp / (tp + fn) if tp + fn else np.nan,
            "FPR": fp / (fp + tn) if fp + tn else np.nan}

rows = []
for g in sorted(set(grp)):
    k = grp == g
    rows.append({"group": g, "n": int(k.sum()), "phishing": int(y[k].sum()), "legitimate": int((y[k] == 0).sum())})
keep = grp != "URL lost"
for mod in models:
    a, b = m(y, p[mod].values), m(y[keep], p[mod].values[keep])
    rows.append({"group": "all vs without URL-lost", "model": mod, "F1_all": a["F1"], "F1_without_url_lost": b["F1"],
                 "Recall_all": a["Recall"], "Recall_without_url_lost": b["Recall"]})
out = pd.DataFrame(rows); out.to_csv(ROOT / "derived/url_loss_ua_naz.csv", index=False, encoding="utf-8-sig")
print(out.round(3).to_string(index=False))
