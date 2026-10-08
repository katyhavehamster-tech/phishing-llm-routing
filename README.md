# Phishing / unwanted email detection with language models: routing experiment (v6)

Reproducibility package for the article «Архітектурні підходи до застосування мовних моделей для виявлення фішингових
і небажаних електронних листів» (Luchyk V. Ye., Nosov V. V., Vitvitska K. E.).

## Contents
- `phishing_llm_experiment_v6.ipynb` – full experiment (Google Colab, NVIDIA T4). Run all cells; intermediate state is cached on Google Drive.
- `results/` – outputs of the run used in the article: `results_main.csv` (metrics, Wilson CIs), `stats_diff.csv`
  (paired bootstrap ΔF1, exact McNemar), `xlmr_seeds.csv`, `calibration.csv`, `robustness.csv`, `cascade_curve.csv`,
  `time.csv`, `predictions.csv` (per-message scores of all models on all test sets; columns `набір`, `i`, `мітка`,
  `sha256_16` + one column per model), `run_info.json` (versions, parameters, prompts, model revisions, cascade thresholds),
  `summary.md`, `llm_explanations.txt` (UA-REAL items removed). v6 additions (if present): `hybrids_seeds.csv`,
  `hybrids_seeds_stats.csv` (hybrids for all three XLM-R runs, thresholds fitted on validation), `op_point_val.csv`
  (FPR ≤ 1% threshold chosen on validation), `robustness_defense.csv` (injection with a defended system prompt),
  `robustness_fpr.csv` (false positive rate under attack), `val_predictions.csv`.
- `data/split_manifest.csv` – SHA-256 (first 16 hex) of every email of the main dataset, split (train/val/test) and
  near-duplicate group id (char 5-gram TF-IDF cosine ≥ 0.8, connected components). `data/ua_mt_manifest.csv` – source
  hashes of the machine-translated UA-MT set. `external_en_sample.xlsx`, `ua_mt_source.xlsx`, `ua_translated_sample.xlsx` –
  public Nazario/Enron samples and their translations.
- `data/ua_real_metadata.csv` – the 94 real Ukrainian messages (UA-REAL): id, hash of the first 1200 characters, label,
  channel, kind, source, URL of the original publication, date; `data/ua_real_annotations.csv` – independent blind labels of two annotators (class, channel, language, purpose, editorial traces, confidence). **Message texts are not redistributed**; they can be
  retrieved from the cited public sources.
- `derived/group_bootstrap_sensitivity.csv` – group (cluster) bootstrap of ΔF1 by near-duplicate groups (EN, UA-MT).

## Environment
{
 "python": "3.13.15",
 "torch": "2.11.0+cu130",
 "transformers": "5.18.0",
 "bitsandbytes": "0.50.2",
 "accelerate": "1.15.0",
 "datasets": "4.8.5",
 "sklearn": "1.6.1",
 "scipy": "1.16.3"
}

Models: {"xlmr": "xlm-roberta-base", "llm": "Qwen/Qwen2.5-7B-Instruct", "mt": "Helsinki-NLP/opus-mt-en-uk"}; revisions: {"xlm-roberta-base": "e73636d4f797dec63c3081bb6ed5c7b0bb3f2089", "Qwen/Qwen2.5-7B-Instruct": "a09a35458c702b33eeacc393d103063234e8bc28", "Helsinki-NLP/opus-mt-en-uk": "634fdc4b28bf0c8a1d4359cbbcfb29190a09dc0e"}.
Parameters: {"N_TEST": 1000, "N_VAL": 1000, "N_TRAIN_XLMR": 10000, "XLMR_SEEDS": [42, 43, 44], "N_TRANSLATED": 200, "N_ADV": 150, "CASCADE_SHARE": 0.15, "CAL_BAND": [0.1, 0.9], "TEXT_CHARS": 1200, "NEAR_DUP_THR": 0.8, "N_BOOT": 2000, "XLMR_EPOCHS": 2, "XLMR_LR": 2e-05, "XLMR_BS": 16, "XLMR_MAXLEN": 384, "LLM_BS": 8}.
Main dataset: `zefang-liu/phishing-email-dataset` (Hugging Face). External corpora: Nazario phishing corpus and Enron
(Phishing Email Curated Datasets).

## Prompts
System: You are an experienced cybersecurity analyst who filters malicious and unwanted email.

User: Determine whether the following email is malicious or unwanted: phishing, scam/fraud, or spam. The email may be written in English or Ukrainian.
Answer with a single digit only: 1 if it is phishing, scam or spam; 0 if it is a legitimate email.

Email:
"""
{email}
"""

## Licence
Code: MIT. Results and metadata: CC BY 4.0. Third-party datasets keep their original licences.
