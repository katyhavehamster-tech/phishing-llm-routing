"""Group (cluster) bootstrap of ΔF1 by near-duplicate groups, EN and UA-MT (CPU, from saved predictions).

Usage: python scripts/group_bootstrap.py  ->  derived/group_bootstrap_sensitivity.csv
       python scripts/group_bootstrap.py --check   (recompute and compare with the committed file)

Unit of resampling: near-duplicate group from data/split_manifest.csv (TF-IDF char 5-grams, cosine >= 0.8).
  EN:    test rows of the manifest are in the same order as the EN rows of results/predictions.csv
         (labels agree for all 1000 rows), so the group is taken by position.
  UA-MT: each translated email inherits the group of its English source (data/ua_mt_manifest.csv, same order).
Procedure: 2000 replicates; in each, groups are drawn with replacement (as many as there are groups) and all
emails of a drawn group enter the replicate; ΔF1 = F1(A) - F1(B) at threshold 0.5; 95% percentile interval.
Random generator: numpy.random.default_rng(42), re-created for every comparison.
row_lo / row_hi: ordinary (email-level) paired bootstrap interval from results/stats_diff.csv, for comparison.
"""
import sys
from pathlib import Path
import numpy as np, pandas as pd

ROOT = Path(__file__).resolve().parents[1]
N_BOOT, SEED = 2000, 42
PAIRS = [("Каскад XLM-R → ВММ", "XLM-R (донавчена)"), ("Каскад XLM-R(T) → ВММ", "XLM-R (донавчена)"),
         ("Паралельний XLM-R ∨ ВММ", "XLM-R (донавчена)"), ("Qwen2.5-7B (промпт)", "XLM-R (донавчена)"),
         ("Каскад LR → ВММ", "TF-IDF + LR"), ("TF-IDF + LR", "XLM-R (донавчена)")]
SET_NAMES = {"EN": "Англомовний тест", "UA-MT": "Україномовний (переклад тесту)"}

pr = pd.read_csv(ROOT / "results/predictions.csv", encoding="utf-8-sig")
man = pd.read_csv(ROOT / "data/split_manifest.csv")
mt = pd.read_csv(ROOT / "data/ua_mt_manifest.csv")

test = man[man.split == "test"].reset_index(drop=True)
en = pr[pr["набір"] == "EN"].sort_values("i").reset_index(drop=True)
assert len(en) == len(test) and (en["мітка"].values == test.label.values).all(), "EN rows do not match the manifest"
en["group"] = test.group.values

ua = pr[pr["набір"] == "UA-MT"].sort_values("i").reset_index(drop=True)
assert len(ua) == len(mt) and (ua["мітка"].values == mt.label.values).all(), "UA-MT rows do not match ua_mt_manifest"
ua["src"] = mt.src_sha.values
ua = ua.merge(man[["sha256_16", "group"]].rename(columns={"sha256_16": "src"}), on="src", how="left")
assert ua.group.notna().all(), "UA-MT source not found in the manifest"


def f1(y, p):
    tp = ((p == 1) & (y == 1)).sum(); fp = ((p == 1) & (y == 0)).sum(); fn = ((p == 0) & (y == 1)).sum()
    return 2 * tp / (2 * tp + fp + fn) if tp else 0.0


def group_ci(df, a_col, b_col):
    y = df["мітка"].values
    a = (df[a_col].values >= 0.5).astype(int); b = (df[b_col].values >= 0.5).astype(int)
    _, inv = np.unique(df.group.values, return_inverse=True)
    members = [np.where(inv == k)[0] for k in range(inv.max() + 1)]
    rng = np.random.default_rng(SEED); reps = []
    for _ in range(N_BOOT):
        ii = np.concatenate([members[k] for k in rng.integers(0, len(members), len(members))])
        reps.append(f1(y[ii], a[ii]) - f1(y[ii], b[ii]))
    return f1(y, a) - f1(y, b), np.percentile(reps, 2.5), np.percentile(reps, 97.5), len(members)


sd = pd.read_csv(ROOT / "results/stats_diff.csv", encoding="utf-8-sig")
rows = []
for set_key, df in (("EN", en), ("UA-MT", ua)):
    for A, B in PAIRS:
        d, lo, hi, n = group_ci(df, A, B)
        r = sd[(sd["Набір"] == SET_NAMES[set_key]) & (sd.A == A) & (sd.B == B)].iloc[0]
        rows.append({"set": set_key, "A": A, "B": B, "dF1": d, "grp_lo": lo, "grp_hi": hi,
                     "row_lo": r["95% CI low"], "row_hi": r["95% CI high"], "n_groups": n})
out = pd.DataFrame(rows)
out["width_ratio"] = (out.grp_hi - out.grp_lo) / (out.row_hi - out.row_lo)
out["zero_in_grp"] = (out.grp_lo <= 0) & (out.grp_hi >= 0)
out["zero_in_row"] = (out.row_lo <= 0) & (out.row_hi >= 0)
target = ROOT / "derived/group_bootstrap_sensitivity.csv"
if "--check" in sys.argv:
    old = pd.read_csv(target)
    cols = ["dF1", "grp_lo", "grp_hi", "row_lo", "row_hi"]
    diff = np.abs(old[cols].values - out[cols].values).max()
    print(f"max abs difference vs committed file: {diff:.2e}")
else:
    out.to_csv(target, index=False)
print(f"max width ratio (group / email-level): {out.width_ratio.max():.2f}; "
      f"conclusion about zero changed in {(out.zero_in_grp != out.zero_in_row).sum()} of {len(out)} comparisons")
