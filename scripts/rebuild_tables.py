"""Rebuild the article's tables from the saved predictions and result files (CPU only, no model runs).

Usage:  python scripts/rebuild_tables.py
Writes derived/*.csv and supplement/*.csv and prints a consistency report.
All numbers are recomputed from results/predictions.csv, results/stats_diff.csv,
results/robustness*.csv, results/llm_extra_*.csv, results/injection_adaptive.csv
and data/ua_real_*.csv; nothing is re-trained.
"""
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.stats import binomtest

ROOT = Path(__file__).resolve().parents[1]
R, D = ROOT / "results", ROOT / "data"
DER, SUP = ROOT / "derived", ROOT / "supplement"
DER.mkdir(exist_ok=True); SUP.mkdir(exist_ok=True)
rd = lambda p: pd.read_csv(p, encoding="utf-8-sig")

SETS = {"EN": "Англомовний тест", "EN-EXT": "Англомовний зовнішній (Nazario + Enron)",
        "UA-MT": "Україномовний (переклад тесту)", "UA-MT-NAZ": "Україномовний (переклад Nazario + Enron)",
        "UA-REAL": "Україномовний (реальний)"}
SHORT = {v: k for k, v in SETS.items()}
SHORT_ART = {"EN": "EN", "EN-EXT": "EXT", "UA-MT": "UA-MT", "UA-MT-NAZ": "UA-NAZ", "UA-REAL": "UA-REAL"}
FAMILY = [("Каскад XLM-R → ВММ", "XLM-R (донавчена)"), ("Каскад XLM-R(T) → ВММ", "XLM-R (донавчена)"),
          ("Паралельний XLM-R ∨ ВММ", "XLM-R (донавчена)"), ("Qwen2.5-7B (промпт)", "XLM-R (донавчена)"),
          ("Каскад LR → ВММ", "TF-IDF + LR")]


def holm(p):
    p = np.asarray(p, float); m = len(p); o = np.argsort(p)
    adj = np.empty(m); run = 0.0
    for k, i in enumerate(o):
        run = max(run, min(1.0, (m - k) * p[i])); adj[i] = run
    return adj


def conf(y, s, thr=0.5):
    yh = (np.asarray(s) >= thr).astype(int); y = np.asarray(y)
    tp = int(((yh == 1) & (y == 1)).sum()); fp = int(((yh == 1) & (y == 0)).sum())
    fn = int(((yh == 0) & (y == 1)).sum()); tn = int(((yh == 0) & (y == 0)).sum())
    f1 = 2 * tp / (2 * tp + fp + fn) if tp else 0.0
    return tp, fp, fn, tn, f1


def mcnemar(y, a, b):
    ca = (np.asarray(a) >= 0.5).astype(int) == y; cb = (np.asarray(b) >= 0.5).astype(int) == y
    n01 = int((ca & ~cb).sum()); n10 = int((~ca & cb).sum())
    p = binomtest(min(n01, n10), n01 + n10, 0.5).pvalue if n01 + n10 else 1.0
    return n01, n10, p


def kappa(a, b):
    a, b = np.asarray(a), np.asarray(b); cats = sorted(set(a) | set(b))
    po = (a == b).mean(); pe = sum((a == c).mean() * (b == c).mean() for c in cats)
    return (po - pe) / (1 - pe)


report = []
pred = rd(R / "predictions.csv")
main = rd(R / "results_main.csv")

# 1. Confusion matrices and F1 at threshold 0.5 vs results_main.csv
rows = []
for s, name in SETS.items():
    sub = pred[pred["набір"] == s]
    for m in main["Модель"].unique():
        if m not in sub.columns: continue
        tp, fp, fn, tn, f1 = conf(sub["мітка"], sub[m])
        ref = main[(main["Модель"] == m) & (main["Набір"] == name)]
        ok = (len(ref) == 1 and int(ref.TP.iloc[0]) == tp and int(ref.FP.iloc[0]) == fp and int(ref.FN.iloc[0]) == fn)
        rows.append({"set": s, "model": m, "TP": tp, "FP": fp, "FN": fn, "TN": tn, "F1": round(f1, 6), "matches_results_main": ok})
cm = pd.DataFrame(rows); cm.to_csv(DER / "confusion_check.csv", index=False, encoding="utf-8-sig")
report.append(f"confusion matrices recomputed: {len(cm)}, all match results_main.csv: {bool(cm.matches_results_main.all())}")

# 2. Pairwise comparisons: one Holm family of 25 (Table A1 of the supplement)
sd = rd(R / "stats_diff.csv")
fam = pd.concat([sd[(sd.A == a) & (sd.B == b)] for a, b in FAMILY])
fam = fam[fam["Набір"].isin(SETS.values())].copy()
assert len(fam) == 25, len(fam)
fam["p_Holm"] = holm(fam["McNemar p"].values)
fam["set"] = fam["Набір"].map(SHORT).map(SHORT_ART)
order = {v: i for i, v in enumerate(SHORT_ART.values())}
fam = fam.sort_values(by="set", key=lambda c: c.map(order), kind="stable")
a1 = fam[["set", "A", "B", "ΔF1 (A-B)", "95% CI low", "95% CI high", "A прав, B ні", "B прав, A ні", "McNemar p", "p_Holm"]]
a1.to_csv(SUP / "table_A1_pairwise_comparisons.csv", index=False, encoding="utf-8-sig")
report.append("Holm (25): " + "; ".join(f"{r.set} {r.A}: p={r._9:.4g}, Holm={r.p_Holm:.4g}" for r in a1.itertuples() if r.set == "UA-REAL"))

# 3. Robustness (Table A2): detection on modified positives and FPR on modified legitimate emails, two separate blocks
rob = rd(R / "robustness.csv"); rf = rd(R / "robustness_fpr.csv")
rob["set"] = rob["Набір"].map(SHORT).map(SHORT_ART)
rob.drop(columns=["Набір"]).to_csv(SUP / "table_A2a_detection_under_attack.csv", index=False, encoding="utf-8-sig")
rf["set"] = rf["Набір"].map(SHORT).map(SHORT_ART)
piv = rf.pivot_table(index=["set", "Модель"], columns="Модифікація", values="FPR").reset_index()
piv["checkpoint_note"] = np.where(piv["Модель"].str.contains("XLM-R"),
                                  "XLM-R re-trained with seed 42 (EN agreement with the main model 99.3%)", "main model")
piv.to_csv(SUP / "table_A2b_fpr_on_modified_legitimate.csv", index=False, encoding="utf-8-sig")

# 4. UA-REAL: explicit ID mapping, label agreement and label sensitivity
meta = rd(D / "ua_real_metadata.csv"); ann = rd(D / "ua_real_annotations.csv")
u = pred[pred["набір"] == "UA-REAL"].reset_index(drop=True)
idmap = pd.DataFrame({"sample_id": meta["id"], "predictions_i": u["i"], "label_metadata": meta["label"],
                      "label_predictions": u["мітка"], "sha256_16_metadata": meta["sha256_16_first1200"],
                      "sha256_16_predictions": u["sha256_16"]})
assert (idmap.label_metadata == idmap.label_predictions).all() and (idmap.sample_id == idmap.predictions_i + 1).all()
hp = D / "ua_real_hashes.csv"   # written by scripts/verify_ua_real.py from the original ua_sample.xlsx
if hp.exists():
    hh = rd(hp)
    ok = (hh.sha256_model_input.str[:16].values == idmap.sha256_16_predictions.values) & \
         (hh.sha256_raw_first1200.str[:16].values == idmap.sha256_16_metadata.values)
    idmap["sha256_raw_first1200"] = hh.sha256_raw_first1200; idmap["sha256_model_input"] = hh.sha256_model_input
    idmap["link_basis"] = np.where(ok, "full SHA-256 verified (raw text -> metadata, model input -> predictions)", "NOT VERIFIED")
    report.append(f"UA-REAL id map: {int(ok.sum())}/94 verified by full hashes of both text representations")
else:
    idmap["link_basis"] = "row order + label (run scripts/verify_ua_real.py to verify by hashes)"
    report.append("UA-REAL id map: ua_real_hashes.csv not found; link by row order and labels only")
idmap.to_csv(D / "ua_real_id_map.csv", index=False, encoding="utf-8-sig")

a = ann.set_index("id").loc[meta["id"]]
b1 = (a["Клас_1"] != "легітимне").astype(int).values; b2 = (a["Клас_2"] != "легітимне").astype(int).values
src = meta["label"].values
k = {"kappa_src_ann1": kappa(src, b1), "kappa_src_ann2": kappa(src, b2), "kappa_ann1_ann2": kappa(b1, b2),
     "kappa_ann1_ann2_4class": kappa(a["Клас_1"].values, a["Клас_2"].values), "unanimous_n": int((b1 == b2).sum()),
     "unanimous_agree_with_source": float((b1 == src)[b1 == b2].mean())}
report.append("kappa: " + ", ".join(f"{kk}={v:.3f}" for kk, v in k.items()))
LLM, X = "Qwen2.5-7B (промпт)", "XLM-R (донавчена)"
sens = []
variants = {"source": (src, np.ones(94, bool)), "annotator_1": (b1, np.ones(94, bool)), "annotator_2": (b2, np.ones(94, bool)),
            "unanimous_only": (b1, b1 == b2), "majority_of_three": (((src + b1 + b2) >= 2).astype(int), np.ones(94, bool))}
for vn, (lab, msk) in variants.items():
    y = lab[msk]; sl, sx = u[LLM].values[msk], u[X].values[msk]
    n01, n10, p = mcnemar(y, sl, sx)
    sens.append({"labels": vn, "n": int(msk.sum()), "F1_LLM": conf(y, sl)[4], "F1_XLMR": conf(y, sx)[4],
                 "only_LLM_correct": n01, "only_XLMR_correct": n10, "McNemar_p_unadjusted": p})
sens = pd.DataFrame(sens); sens.to_csv(DER / "ua_real_label_sensitivity.csv", index=False, encoding="utf-8-sig")
pd.DataFrame([k]).to_csv(DER / "ua_real_label_agreement.csv", index=False, encoding="utf-8-sig")
report.append("label sensitivity: " + "; ".join(f"{r.labels}: F1 LLM {r.F1_LLM:.3f}, XLM-R {r.F1_XLMR:.3f}, p={r.McNemar_p_unadjusted:.2g}" for r in sens.itertuples()))

# 5. UA-REAL by channel (Table A3)
email = meta["channel"].str.lower().str.contains("mail") & ~meta["channel"].str.lower().str.contains("месенджер|sms")
ch = []
for cname, msk in [("email", email.values), ("SMS / messengers / other", ~email.values)]:
    y = src[msk]
    for m in [c for c in u.columns if c not in ("набір", "i", "мітка", "sha256_16")]:
        tp, fp, fn, tn, f1 = conf(y, u[m].values[msk])
        ch.append({"channel": cname, "model": m, "n": int(msk.sum()), "positives": int(y.sum()), "TP": tp, "FP": fp, "FN": fn, "F1": f1})
pd.DataFrame(ch).to_csv(SUP / "table_A3_ua_real_by_channel.csv", index=False, encoding="utf-8-sig")
e = pd.DataFrame(ch); e = e[e.model.isin([LLM, X])]
report.append("by channel: " + "; ".join(f"{r.channel} {r.model}: n={r.n}, TP={r.TP}, FP={r.FP}, F1={r.F1:.3f}" for r in e.itertuples()))

# 6. Table A4: adversarial modifications on ONE XLM-R checkpoint (notebook v6.2, cell 17b)
op = R / "robustness_one_checkpoint.csv"
if op.exists():
    oc = rd(op); oc["set"] = oc["Набір"].map(SHORT).map(SHORT_ART)
    oc.drop(columns=["Набір"]).to_csv(SUP / "table_A4_one_checkpoint.csv", index=False, encoding="utf-8-sig")
    x = oc[oc["Модель"].str.startswith("XLM-R")]
    d = x.pivot_table(index="set", columns="Модифікація", values="FPR")
    inc = max((d[k] - d["Оригінал"]).max() for k in ["Ін'єкція інструкції", "Легітимний текст"])
    report.append(f"one checkpoint: max FPR increase of XLM-R under injection / benign text = {inc:.3f}")

# 7. Tables A5-A6 (notebook v6.3, cell 17в): additional generative models and adaptive instruction injection
em, es, ia, pe = R / "llm_extra_main.csv", R / "llm_extra_stats.csv", R / "injection_adaptive.csv", R / "predictions_extra_llms.csv"
if em.exists() and pe.exists():
    m5 = rd(em); m5["set"] = m5["Набір"].map(SHORT).map(SHORT_ART)
    # recompute the metrics of the extra LLMs from the saved per-email probabilities
    px = rd(pe); bad = 0
    for mdl in [c for c in px.columns if c not in ("набір", "i", "мітка", "sha256_16")]:
        for s_, g in px.groupby("набір"):
            tp, fp, fn, tn, f1 = conf(g["мітка"].values, g[mdl].values)
            row = m5[(m5["Модель"] == mdl) & (m5["Набір"] == SETS[s_])].iloc[0]
            bad += int((tp, fp, fn, tn) != (row.TP, row.FP, row.FN, row.TN))
    # Qwen rows of A5 must equal the main results
    rm = rd(R / "results_main.csv"); q = m5[m5["Модель"] == "Qwen2.5-7B (промпт)"].merge(rm, on=["Модель", "Набір"], suffixes=("", "_main"))
    bad += int((q["F1"] - q["F1_main"]).abs().max() > 1e-9)
    report.append(f"A5: confusion matrices of extra LLMs recomputed from predictions_extra_llms.csv, mismatches = {bad}")
    a5 = m5[["set", "Модель", "n", "TP", "FP", "TN", "FN", "Precision", "Recall", "F1", "FPR", "ROC_AUC", "PR_AUC", "ECE"]]
    a5.to_csv(SUP / "table_A5_extra_llms.csv", index=False, encoding="utf-8-sig")
    if es.exists():
        s5 = rd(es); s5["set"] = s5["Набір"].map(SHORT).map(SHORT_ART)
        s5.drop(columns=["Набір"]).to_csv(SUP / "table_A5b_extra_llms_stats.csv", index=False, encoding="utf-8-sig")
if ia.exists():
    a6 = rd(ia); a6["set"] = a6["Набір"].map(SHORT).map(SHORT_ART)
    a6 = a6.pivot_table(index=["set", "Модель", "Промпт ВММ"], columns="Варіант", values="Частка виявлених").reset_index()
    a6.to_csv(SUP / "table_A6_adaptive_injection.csv", index=False, encoding="utf-8-sig")
    ad = "Адаптивна (найкращий для атакувальника з V1–V5)"
    t = a6[a6["Промпт ВММ"] == "без захисту"].set_index(["Модель", "set"])[ad]
    report.append("A6 adaptive (no defence): " + "; ".join(f"{k[0]} {k[1]}={v:.2f}" for k, v in t.items()
                                                          if k[0] in ("Qwen2.5-7B (промпт)", "Llama-3.1-8B (промпт)", "Mistral-7B-v0.3 (промпт)")))

print("\n".join(report))
