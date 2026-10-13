# Phishing / unwanted email detection with language models: routing experiment (v6.3)

Reproducibility package for the article «Архітектурні підходи до застосування мовних моделей для виявлення фішингових
і небажаних електронних листів» (Luchyk V. Ye., Nosov V. V., Vitvitska K. E.).

Authors of the code and data package: Luchyk V. Ye. (Лучик В. Є.), Nosov V. V. (Носов В. В.), Vitvitska K. E. (Вітвіцька К. Е.),
Manzhai I. A. (Манжай І. А.); Kharkiv National University of Internal Affairs. How to cite: `CITATION.cff`.
Supplement A (Tables A1–A6) is archived on Zenodo: https://doi.org/10.5281/zenodo.23326929

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
- `derived/group_bootstrap_sensitivity.csv` – group (cluster) bootstrap of ΔF1 by near-duplicate groups (EN, UA-MT), written by `scripts/group_bootstrap.py`; other `derived/` files are written by `scripts/rebuild_tables.py`.
- `supplement/` – supplementary tables A1–A6 of the article (pairwise comparisons, adversarial modifications in two blocks, UA-REAL by channel, one XLM-R checkpoint under attack, additional generative models, adaptive instruction injection).

## Stages of the experiment
| Stage | What | Files |
|---|---|---|
| Base run (notebook v4/v5, state cached in `phishing_experiment_results_v4`) | data preparation, near-duplicate split, all models, hybrids for XLM-R seed 42, robustness, calibration, statistics | `results_main.csv`, `predictions.csv`, `stats_diff.csv`, `robustness.csv`, `calibration.csv`, `xlmr_seeds.csv`, `cascade_curve.csv`, `time.csv`; `run_info.json` (field `version` = `v5`) |
| v6 analyses (notebook v6, separate state `state_v6.pkl`; base results reused, not recomputed) | hybrids for all three XLM-R runs, FPR ≤ 1% threshold chosen on validation, defended system prompt, FPR on modified legitimate emails (XLM-R re-trained with seed 42 because the base weights were not saved) | `hybrids_seeds*.csv`, `op_point_val.csv`, `robustness_defense.csv`, `robustness_fpr.csv`, `val_predictions.csv` |
| Post-hoc (CPU, from saved predictions) | group bootstrap, Holm family of 25, label agreement and sensitivity, supplement tables | `derived/`, `supplement/` (`scripts/rebuild_tables.py`) |
| v6.2 (cell 17б) | XLM-R seed 42 re-trained once and used for BOTH detection on modified positives and FPR on modified legitimate emails (one checkpoint); URL-loss analysis for UA-MT and UA-NAZ | `robustness_one_checkpoint.csv`, `url_loss_analysis.csv`, `run_info_v62.json` (run of 10.10.2026; base results reproduced byte for byte) |
| v6.3 (cell 17в) | Two more generative models with the same prompt, quantisation and threshold (Llama-3.1-8B-Instruct, Mistral-7B-Instruct-v0.3) and adaptive instruction injection (five variants, attacker picks the best per email; with and without a defended system prompt) | `llm_extra_main.csv`, `llm_extra_stats.csv`, `injection_adaptive.csv`, `predictions_extra_llms.csv`, `run_info_v63.json` (Kaggle Tesla T4, 11.10.2026; base results reproduced byte for byte); supplement Tables A5-A6 |
| v6.1 | pinned library versions and model revisions, configuration hash in the cache check, optional saving of XLM-R weights; no change to the article's results | `phishing_llm_experiment_v6.ipynb`, `requirements.txt` |

Model revisions were recorded by querying the Hugging Face Hub during the v6 run; they are now passed as `revision=` to every `from_pretrained` call. The base run used the revisions current at that time, which were not recorded separately. The dataset revision of `zefang-liu/phishing-email-dataset` was not recorded; `data/split_manifest.csv` (hashes of all 17,479 emails) is the check that the same data are used.

## URL loss in translation
UA-NAZ (CPU): `python scripts/url_loss_ua_naz.py` → `derived/url_loss_ua_naz.csv`. Only 12 of 67 phishing emails had a URL in the first 1200 characters; 11 kept it, 1 lost it; excluding that email changes F1 of any model by at most 0.006. UA-MT (notebook cell 17б, `results/url_loss_analysis.csv`): within the first 1200 characters URLs survived in 59 of 63 emails; excluding the 4 others changes F1 by at most 0.004. The 77% in `run_info.json` counts URLs in the full source text, including the part beyond 1200 characters that no model received.

## Rebuilding the tables
`pip install -r requirements-cpu.txt && python scripts/rebuild_tables.py` recomputes, from the saved predictions only: confusion matrices and F1 of all models on all sets (checked against `results_main.csv`), the Holm family of 25 pairwise comparisons, UA-REAL label agreement and label sensitivity, UA-REAL by channel, the confusion matrices of the additional generative models and the supplementary tables A1–A6 (`supplement/README.md`).

`python scripts/group_bootstrap.py` recomputes the group bootstrap of ΔF1 (resampling unit: near-duplicate group from `data/split_manifest.csv`; 2000 replicates; `numpy.random.default_rng(42)` per comparison; 95% percentile interval); `--check` compares with the committed `derived/group_bootstrap_sensitivity.csv` (identical up to floating-point rounding). The group intervals are at most 1.98 times wider than the email-level ones, and in none of the 12 comparisons does the conclusion about whether the interval contains zero change.

## UA-REAL
See `data/UA_REAL_PROTOCOL.md` (inclusion and extraction rules, labels, identifiers) and `data/ua_real_id_map.csv` (explicit link between `sample_id`, the rows of `predictions.csv` and full SHA-256 hashes of the raw text and of the model input; verified for 94/94 messages against the original file).

## Environment
The runs were made in different environments, so there is no single lock file:

| Run | Platform | Python | torch | transformers / bitsandbytes / accelerate / datasets | scikit-learn / scipy |
|---|---|---|---|---|---|
| Base run (v5) and v6/v6.2 analyses | Google Colab, Tesla T4 | 3.13.15 | 2.11.0+cu130 | 5.18.0 / 0.50.2 / 1.15.0 / 4.8.5 | 1.6.1 / 1.16.3 |
| v6.3 (additional LLMs, adaptive injection) | Kaggle, Tesla T4 | 3.13.15 | 2.11.0+cu128 | 5.18.0 / 0.50.2 / 1.15.0 / 4.8.5 | 1.6.1 / 1.16.3 |

Versions are taken from `results/run_info*.json`. numpy, pandas and the auxiliary packages (openpyxl, sentencepiece, sacremoses, huggingface_hub) were not recorded during the GPU runs; `requirements.txt` leaves them unpinned for that reason. The CPU scripts (`scripts/`) were checked with the versions in `requirements-cpu.txt`. Pinning revisions later is not retrospective evidence of the configuration of the base run (see above).

Models: {"xlmr": "xlm-roberta-base", "llm": "Qwen/Qwen2.5-7B-Instruct", "mt": "Helsinki-NLP/opus-mt-en-uk"}; revisions: {"xlm-roberta-base": "e73636d4f797dec63c3081bb6ed5c7b0bb3f2089", "Qwen/Qwen2.5-7B-Instruct": "a09a35458c702b33eeacc393d103063234e8bc28", "Helsinki-NLP/opus-mt-en-uk": "634fdc4b28bf0c8a1d4359cbbcfb29190a09dc0e"}.
Parameters: {"N_TEST": 1000, "N_VAL": 1000, "N_TRAIN_XLMR": 10000, "XLMR_SEEDS": [42, 43, 44], "N_TRANSLATED": 200, "N_ADV": 150, "CASCADE_SHARE": 0.15, "CAL_BAND": [0.1, 0.9], "TEXT_CHARS": 1200, "NEAR_DUP_THR": 0.8, "N_BOOT": 2000, "XLMR_EPOCHS": 2, "XLMR_LR": 2e-05, "XLMR_BS": 16, "XLMR_MAXLEN": 384, "LLM_BS": 8}.
Main dataset: `zefang-liu/phishing-email-dataset` (Hugging Face). External corpora: Nazario phishing corpus and Enron
(Phishing Email Curated Datasets).

## Prompt selection
The prompt wording was chosen in two pilot runs on earlier versions of the data (before the near-duplicate group split): run A asked only about phishing; run B used the broader class definition "phishing, scam/fraud or spam", matching the composition of the positive class of the main dataset. The runs were compared on the EN test set, the external Nazario + Enron set (EXT) and the machine-translated test set (UA-MT); the LLM estimates on these three sets are therefore exploratory. UA-NAZ and UA-REAL were evaluated only with the final prompt; UA-REAL was assembled after the prompt, thresholds and all model parameters had been fixed.

## Prompts
System: You are an experienced cybersecurity analyst who filters malicious and unwanted email.

User: Determine whether the following email is malicious or unwanted: phishing, scam/fraud, or spam. The email may be written in English or Ukrainian.
Answer with a single digit only: 1 if it is phishing, scam or spam; 0 if it is a legitimate email.

Email:
"""
{email}
"""

## Third-party models
Qwen2.5-7B-Instruct (Apache 2.0), Mistral-7B-Instruct-v0.3 (Apache 2.0), Llama-3.1-8B-Instruct (Llama 3.1 Community License; weights loaded from the public copy `unsloth/Llama-3.1-8B-Instruct`, revision recorded in `results/run_info_v63.json`), XLM-RoBERTa base (MIT), OPUS-MT en-uk (CC BY 4.0). The notebook downloads the weights; none are redistributed here.

## Licence
Code: MIT. Results and metadata: CC BY 4.0. Third-party datasets keep their original licences.
