# Supplement / Додаток А

Supplementary tables for the article «Архітектурні підходи до застосування мовних моделей для виявлення фішингових і небажаних електронних листів». They are rebuilt from the saved predictions by `python scripts/rebuild_tables.py` (CSV versions are in this folder). Set names follow the article: EN, EXT (Nazario + Enron), UA-MT, UA-NAZ, UA-REAL.

## Table A1. Pairwise comparisons (Таблиця А1. Парні порівняння моделей)

ΔF1 with a paired bootstrap 95% CI (2,000 resamples, not adjusted for multiplicity); exact McNemar test on error rates; Holm adjustment over one family of 25 comparisons (all sets). A significant McNemar result concerns error rates, not F1; the absence of significance does not imply equivalence.

| Set | A / B | ΔF1 (A − B) | 95% CI | Only A correct / only B | p | p (Holm) |
|---|---|---|---|---|---|---|
| EN | Каскад XLM-R → ВММ / XLM-R (донавчена) | -0.064 | [-0.087; -0.043] | 10 / 55 | < 0.001 | < 0.001 |
| EN | Каскад XLM-R(T) → ВММ / XLM-R (донавчена) | 0.004 | [-0.003; 0.011] | 5 / 2 | 0.453 | 1.000 |
| EN | Паралельний XLM-R ∨ ВММ / XLM-R (донавчена) | -0.013 | [-0.024; -0.003] | 3 / 14 | 0.013 | 0.178 |
| EN | Qwen2.5-7B (промпт) / XLM-R (донавчена) | -0.121 | [-0.150; -0.092] | 10 / 94 | < 0.001 | < 0.001 |
| EN | Каскад LR → ВММ / TF-IDF + LR | -0.046 | [-0.065; -0.028] | 6 / 39 | < 0.001 | < 0.001 |
| EXT | Каскад XLM-R → ВММ / XLM-R (донавчена) | 0.026 | [-0.053; 0.116] | 6 / 4 | 0.754 | 1.000 |
| EXT | Каскад XLM-R(T) → ВММ / XLM-R (донавчена) | 0.013 | [-0.030; 0.062] | 2 / 1 | 1.000 | 1.000 |
| EXT | Паралельний XLM-R ∨ ВММ / XLM-R (донавчена) | 0.072 | [-0.003; 0.159] | 9 / 4 | 0.267 | 1.000 |
| EXT | Qwen2.5-7B (промпт) / XLM-R (донавчена) | 0.026 | [-0.067; 0.130] | 9 / 8 | 1.000 | 1.000 |
| EXT | Каскад LR → ВММ / TF-IDF + LR | -0.022 | [-0.114; 0.064] | 6 / 8 | 0.791 | 1.000 |
| UA-MT | Каскад XLM-R → ВММ / XLM-R (донавчена) | -0.052 | [-0.094; -0.013] | 3 / 13 | 0.021 | 0.277 |
| UA-MT | Каскад XLM-R(T) → ВММ / XLM-R (донавчена) | -0.005 | [-0.028; 0.016] | 2 / 3 | 1.000 | 1.000 |
| UA-MT | Паралельний XLM-R ∨ ВММ / XLM-R (донавчена) | -0.053 | [-0.092; -0.018] | 2 / 14 | 0.004 | 0.071 |
| UA-MT | Qwen2.5-7B (промпт) / XLM-R (донавчена) | -0.118 | [-0.174; -0.070] | 3 / 27 | < 0.001 | < 0.001 |
| UA-MT | Каскад LR → ВММ / TF-IDF + LR | 0.045 | [-0.020; 0.109] | 22 / 15 | 0.324 | 1.000 |
| UA-NAZ | Каскад XLM-R → ВММ / XLM-R (донавчена) | 0.022 | [-0.025; 0.072] | 7 / 4 | 0.549 | 1.000 |
| UA-NAZ | Каскад XLM-R(T) → ВММ / XLM-R (донавчена) | 0.018 | [-0.017; 0.055] | 4 / 2 | 0.688 | 1.000 |
| UA-NAZ | Паралельний XLM-R ∨ ВММ / XLM-R (донавчена) | -0.066 | [-0.128; -0.007] | 5 / 18 | 0.011 | 0.170 |
| UA-NAZ | Qwen2.5-7B (промпт) / XLM-R (донавчена) | -0.060 | [-0.131; 0.006] | 9 / 20 | 0.061 | 0.676 |
| UA-NAZ | Каскад LR → ВММ / TF-IDF + LR | 0.350 | [0.227; 0.481] | 43 / 12 | < 0.001 | < 0.001 |
| UA-REAL | Каскад XLM-R → ВММ / XLM-R (донавчена) | 0.317 | [0.194; 0.453] | 21 / 0 | < 0.001 | < 0.001 |
| UA-REAL | Каскад XLM-R(T) → ВММ / XLM-R (донавчена) | 0.066 | [0.017; 0.135] | 6 / 0 | 0.031 | 0.375 |
| UA-REAL | Паралельний XLM-R ∨ ВММ / XLM-R (донавчена) | 0.199 | [0.083; 0.327] | 10 / 1 | 0.012 | 0.176 |
| UA-REAL | Qwen2.5-7B (промпт) / XLM-R (донавчена) | 0.343 | [0.212; 0.495] | 23 / 1 | < 0.001 | < 0.001 |
| UA-REAL | Каскад LR → ВММ / TF-IDF + LR | 0.478 | [0.347; 0.618] | 44 / 1 | < 0.001 | < 0.001 |

## Table A2. Adversarial modifications (Таблиця А2. Змагальні модифікації)

**Two separate blocks.** A2a: share of positive-class emails still detected after the modification (main models; up to 150 per set). A2b: false positive rate on legitimate emails after the same modification (up to 150 per set). For XLM-R, the XLM-R(T) → LLM cascade and the parallel XLM-R ∨ LLM scheme, A2b was computed with an XLM-R re-trained with the same seed 42 (decision agreement with the main model on EN 99.3%), because the main weights were not saved; the logistic regression was re-trained deterministically. Therefore A2a and A2b for these rows are not one operating point of one detector. The quantile cascade was not evaluated on modified legitimate emails.

### A2a. Detection of modified positive-class emails

| Set | Model | n | Original | Homoglyphs | Invisible chars | Benign text prefix | Instruction injection |
|---|---|---|---|---|---|---|---|
| EN | TF-IDF + LR | 150 | 0.95 | 0.93 | 0.94 | 0.64 | 0.94 |
| EXT | TF-IDF + LR | 50 | 0.84 | 0.74 | 0.86 | 0.22 | 0.72 |
| UA-MT | TF-IDF + LR | 100 | 0.77 | 0.67 | 0.81 | 0.33 | 0.71 |
| UA-NAZ | TF-IDF + LR | 67 | 0.40 | 0.39 | 0.48 | 0.16 | 0.37 |
| UA-REAL | TF-IDF + LR | 31 | 0.45 | 0.35 | 0.48 | 0.35 | 0.35 |
| EN | XLM-R (донавчена) | 150 | 0.97 | 1.00 | 0.99 | 0.51 | 0.98 |
| EXT | XLM-R (донавчена) | 50 | 0.72 | 0.90 | 0.88 | 0.12 | 0.78 |
| UA-MT | XLM-R (донавчена) | 100 | 0.96 | 0.99 | 0.98 | 0.58 | 0.96 |
| UA-NAZ | XLM-R (донавчена) | 67 | 0.90 | 1.00 | 1.00 | 0.39 | 0.93 |
| UA-REAL | XLM-R (донавчена) | 31 | 0.48 | 0.94 | 0.81 | 0.48 | 0.68 |
| EN | Qwen2.5-7B (промпт) | 150 | 0.76 | 0.85 | 0.75 | 0.69 | 0.00 |
| EXT | Qwen2.5-7B (промпт) | 50 | 0.82 | 0.90 | 0.88 | 0.82 | 0.00 |
| UA-MT | Qwen2.5-7B (промпт) | 100 | 0.85 | 0.88 | 0.83 | 0.71 | 0.21 |
| UA-NAZ | Qwen2.5-7B (промпт) | 67 | 0.94 | 0.93 | 0.96 | 0.81 | 0.27 |
| UA-REAL | Qwen2.5-7B (промпт) | 31 | 0.81 | 0.90 | 0.81 | 0.68 | 0.16 |
| EN | Каскад LR → ВММ | 150 | 0.89 | 0.91 | 0.84 | 0.67 | 0.59 |
| EXT | Каскад LR → ВММ | 50 | 0.82 | 0.90 | 0.88 | 0.70 | 0.12 |
| UA-MT | Каскад LR → ВММ | 100 | 0.86 | 0.89 | 0.83 | 0.61 | 0.26 |
| UA-NAZ | Каскад LR → ВММ | 67 | 0.93 | 0.91 | 0.96 | 0.64 | 0.28 |
| UA-REAL | Каскад LR → ВММ | 31 | 0.81 | 0.90 | 0.81 | 0.68 | 0.16 |
| EN | Каскад XLM-R → ВММ | 150 | 0.83 | 0.95 | 0.87 | 0.57 | 0.51 |
| EXT | Каскад XLM-R → ВММ | 50 | 0.76 | 0.92 | 0.88 | 0.20 | 0.00 |
| UA-MT | Каскад XLM-R → ВММ | 100 | 0.89 | 0.95 | 0.92 | 0.57 | 0.64 |
| UA-NAZ | Каскад XLM-R → ВММ | 67 | 0.91 | 0.94 | 0.96 | 0.49 | 0.30 |
| UA-REAL | Каскад XLM-R → ВММ | 31 | 0.74 | 0.90 | 0.74 | 0.52 | 0.16 |
| EN | Каскад XLM-R(T) → ВММ | 150 | 0.97 | 1.00 | 0.97 | 0.57 | 0.97 |
| EXT | Каскад XLM-R(T) → ВММ | 50 | 0.74 | 0.92 | 0.92 | 0.14 | 0.66 |
| UA-MT | Каскад XLM-R(T) → ВММ | 100 | 0.95 | 0.99 | 0.98 | 0.61 | 0.96 |
| UA-NAZ | Каскад XLM-R(T) → ВММ | 67 | 0.94 | 1.00 | 0.99 | 0.46 | 0.90 |
| UA-REAL | Каскад XLM-R(T) → ВММ | 31 | 0.52 | 0.97 | 0.81 | 0.48 | 0.52 |
| EN | Паралельний LR ∨ ВММ | 150 | 0.97 | 0.97 | 0.95 | 0.85 | 0.94 |
| EXT | Паралельний LR ∨ ВММ | 50 | 0.96 | 1.00 | 1.00 | 0.86 | 0.72 |
| UA-MT | Паралельний LR ∨ ВММ | 100 | 0.95 | 0.94 | 0.96 | 0.81 | 0.76 |
| UA-NAZ | Паралельний LR ∨ ВММ | 67 | 0.99 | 0.96 | 0.97 | 0.84 | 0.54 |
| UA-REAL | Паралельний LR ∨ ВММ | 31 | 0.84 | 0.90 | 0.81 | 0.71 | 0.45 |
| EN | Паралельний XLM-R ∨ ВММ | 150 | 0.97 | 1.00 | 0.99 | 0.77 | 0.98 |
| EXT | Паралельний XLM-R ∨ ВММ | 50 | 0.90 | 0.92 | 0.92 | 0.84 | 0.78 |
| UA-MT | Паралельний XLM-R ∨ ВММ | 100 | 0.98 | 1.00 | 0.98 | 0.84 | 0.97 |
| UA-NAZ | Паралельний XLM-R ∨ ВММ | 67 | 0.97 | 1.00 | 1.00 | 0.85 | 0.93 |
| UA-REAL | Паралельний XLM-R ∨ ВММ | 31 | 0.81 | 1.00 | 0.94 | 0.74 | 0.77 |

### A2b. False positive rate on modified legitimate emails

| Set | Model | Original | Homoglyphs | Invisible chars | Benign text prefix | Instruction injection | Checkpoint |
|---|---|---|---|---|---|---|---|
| EN | Qwen2.5-7B (промпт) | 0.03 | 0.11 | 0.03 | 0.01 | 0.00 | main model |
| EN | TF-IDF + LR | 0.01 | 0.03 | 0.01 | 0.00 | 0.02 | main model |
| EN | XLM-R (донавчена) | 0.02 | 0.29 | 0.05 | 0.01 | 0.03 | XLM-R re-trained with seed 42 (EN agreement with the main model 99.3%) |
| EN | Каскад XLM-R(T) → ВММ | 0.01 | 0.24 | 0.04 | 0.01 | 0.02 | XLM-R re-trained with seed 42 (EN agreement with the main model 99.3%) |
| EN | Паралельний LR ∨ ВММ | 0.03 | 0.12 | 0.04 | 0.01 | 0.02 | main model |
| EN | Паралельний XLM-R ∨ ВММ | 0.04 | 0.35 | 0.07 | 0.01 | 0.03 | XLM-R re-trained with seed 42 (EN agreement with the main model 99.3%) |
| EXT | Qwen2.5-7B (промпт) | 0.12 | 0.09 | 0.09 | 0.06 | 0.00 | main model |
| EXT | TF-IDF + LR | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 | main model |
| EXT | XLM-R (донавчена) | 0.00 | 0.21 | 0.00 | 0.00 | 0.00 | XLM-R re-trained with seed 42 (EN agreement with the main model 99.3%) |
| EXT | Каскад XLM-R(T) → ВММ | 0.00 | 0.18 | 0.00 | 0.00 | 0.00 | XLM-R re-trained with seed 42 (EN agreement with the main model 99.3%) |
| EXT | Паралельний LR ∨ ВММ | 0.12 | 0.09 | 0.09 | 0.06 | 0.00 | main model |
| EXT | Паралельний XLM-R ∨ ВММ | 0.12 | 0.24 | 0.09 | 0.06 | 0.00 | XLM-R re-trained with seed 42 (EN agreement with the main model 99.3%) |
| UA-MT | Qwen2.5-7B (промпт) | 0.17 | 0.23 | 0.22 | 0.09 | 0.00 | main model |
| UA-MT | TF-IDF + LR | 0.06 | 0.07 | 0.08 | 0.02 | 0.05 | main model |
| UA-MT | XLM-R (донавчена) | 0.04 | 0.39 | 0.19 | 0.03 | 0.08 | XLM-R re-trained with seed 42 (EN agreement with the main model 99.3%) |
| UA-MT | Каскад XLM-R(T) → ВММ | 0.06 | 0.31 | 0.14 | 0.03 | 0.04 | XLM-R re-trained with seed 42 (EN agreement with the main model 99.3%) |
| UA-MT | Паралельний LR ∨ ВММ | 0.22 | 0.29 | 0.28 | 0.11 | 0.05 | main model |
| UA-MT | Паралельний XLM-R ∨ ВММ | 0.18 | 0.49 | 0.32 | 0.10 | 0.08 | XLM-R re-trained with seed 42 (EN agreement with the main model 99.3%) |
| UA-NAZ | Qwen2.5-7B (промпт) | 0.29 | 0.39 | 0.39 | 0.23 | 0.03 | main model |
| UA-NAZ | TF-IDF + LR | 0.11 | 0.11 | 0.12 | 0.05 | 0.05 | main model |
| UA-NAZ | XLM-R (донавчена) | 0.09 | 0.44 | 0.21 | 0.09 | 0.11 | XLM-R re-trained with seed 42 (EN agreement with the main model 99.3%) |
| UA-NAZ | Каскад XLM-R(T) → ВММ | 0.09 | 0.41 | 0.21 | 0.11 | 0.08 | XLM-R re-trained with seed 42 (EN agreement with the main model 99.3%) |
| UA-NAZ | Паралельний LR ∨ ВММ | 0.36 | 0.45 | 0.45 | 0.23 | 0.07 | main model |
| UA-NAZ | Паралельний XLM-R ∨ ВММ | 0.32 | 0.61 | 0.49 | 0.24 | 0.12 | XLM-R re-trained with seed 42 (EN agreement with the main model 99.3%) |
| UA-REAL | Qwen2.5-7B (промпт) | 0.08 | 0.21 | 0.10 | 0.11 | 0.00 | main model |
| UA-REAL | TF-IDF + LR | 0.59 | 0.56 | 0.60 | 0.43 | 0.19 | main model |
| UA-REAL | XLM-R (донавчена) | 0.29 | 0.56 | 0.44 | 0.19 | 0.35 | XLM-R re-trained with seed 42 (EN agreement with the main model 99.3%) |
| UA-REAL | Каскад XLM-R(T) → ВММ | 0.22 | 0.54 | 0.33 | 0.14 | 0.29 | XLM-R re-trained with seed 42 (EN agreement with the main model 99.3%) |
| UA-REAL | Паралельний LR ∨ ВММ | 0.59 | 0.62 | 0.60 | 0.44 | 0.19 | main model |
| UA-REAL | Паралельний XLM-R ∨ ВММ | 0.30 | 0.63 | 0.46 | 0.27 | 0.35 | XLM-R re-trained with seed 42 (EN agreement with the main model 99.3%) |

## Table A3. UA-REAL by channel (Таблиця А3. UA-REAL за каналами)

Decision threshold 0.5, labels by source. Channel from `data/ua_real_metadata.csv`: e-mail vs SMS, messengers and other.

| Channel | Model | n (positives) | TP | FP | FN | F1 |
|---|---|---|---|---|---|---|
| email | TF-IDF + LR | 42 (13) | 6 | 7 | 7 | 0.462 |
| email | XLM-R (донавчена) | 42 (13) | 6 | 0 | 7 | 0.632 |
| email | Qwen2.5-7B (промпт) | 42 (13) | 10 | 1 | 3 | 0.833 |
| email | Каскад LR → ВММ | 42 (13) | 10 | 1 | 3 | 0.833 |
| email | Каскад XLM-R → ВММ | 42 (13) | 9 | 0 | 4 | 0.818 |
| email | Каскад XLM-R(T) → ВММ | 42 (13) | 6 | 0 | 7 | 0.632 |
| email | Паралельний LR ∨ ВММ | 42 (13) | 11 | 7 | 2 | 0.710 |
| email | Паралельний XLM-R ∨ ВММ | 42 (13) | 10 | 1 | 3 | 0.833 |
| email | XLM-R (T-калібр.) | 42 (13) | 6 | 0 | 7 | 0.632 |
| email | TF-IDF + LR (10k) | 42 (13) | 5 | 5 | 8 | 0.435 |
| email | XLM-R seed 42 | 42 (13) | 6 | 0 | 7 | 0.632 |
| email | XLM-R seed 43 | 42 (13) | 6 | 0 | 7 | 0.632 |
| email | XLM-R seed 44 | 42 (13) | 7 | 0 | 6 | 0.700 |
| SMS / messengers / other | TF-IDF + LR | 52 (18) | 8 | 30 | 10 | 0.286 |
| SMS / messengers / other | XLM-R (донавчена) | 52 (18) | 9 | 17 | 9 | 0.409 |
| SMS / messengers / other | Qwen2.5-7B (промпт) | 52 (18) | 15 | 4 | 3 | 0.811 |
| SMS / messengers / other | Каскад LR → ВММ | 52 (18) | 15 | 4 | 3 | 0.811 |
| SMS / messengers / other | Каскад XLM-R → ВММ | 52 (18) | 14 | 4 | 4 | 0.778 |
| SMS / messengers / other | Каскад XLM-R(T) → ВММ | 52 (18) | 10 | 12 | 8 | 0.500 |
| SMS / messengers / other | Паралельний LR ∨ ВММ | 52 (18) | 15 | 30 | 3 | 0.476 |
| SMS / messengers / other | Паралельний XLM-R ∨ ВММ | 52 (18) | 15 | 17 | 3 | 0.600 |
| SMS / messengers / other | XLM-R (T-калібр.) | 52 (18) | 9 | 17 | 9 | 0.409 |
| SMS / messengers / other | TF-IDF + LR (10k) | 52 (18) | 7 | 29 | 11 | 0.259 |
| SMS / messengers / other | XLM-R seed 42 | 52 (18) | 9 | 17 | 9 | 0.409 |
| SMS / messengers / other | XLM-R seed 43 | 52 (18) | 8 | 12 | 10 | 0.421 |
| SMS / messengers / other | XLM-R seed 44 | 52 (18) | 12 | 18 | 6 | 0.500 |

Pairwise comparisons by channel, by XLM-R run and with alternative labels are sensitivity analyses with unadjusted p-values; they are not part of the Holm family of Table A1 (see `derived/ua_real_label_sensitivity.csv`, `results/hybrids_seeds_stats.csv`).

## Table A4. Adversarial modifications on one XLM-R checkpoint (Таблиця А4. Змагальні модифікації на одній контрольній точці XLM-R)

Notebook v6.2 (cell 17б): XLM-R (seed 42) was re-trained once and the SAME model scored both the modified positive-class emails and the modified legitimate emails, so each cell is one operating point of one detector: detected share / FPR. Decision agreement with the main XLM-R: EN 0.993, EXT 0.964, UA-MT 0.980, UA-NAZ 0.937, UA-REAL 0.936. The LLM scores are those of the main run.

| Set | Model | Original | Homoglyphs | Invisible chars | Benign text prefix | Instruction injection |
|---|---|---|---|---|---|---|
| EN | XLM-R (одна контрольна точка) | 0.97 / 0.01 | 1.00 / 0.25 | 0.99 / 0.05 | 0.59 / 0.01 | 0.99 / 0.03 |
| EN | Каскад XLM-R(T) → ВММ | 0.97 / 0.01 | 1.00 / 0.22 | 0.99 / 0.03 | 0.59 / 0.01 | 0.96 / 0.01 |
| EN | Паралельний XLM-R ∨ ВММ | 0.97 / 0.03 | 1.00 / 0.30 | 0.99 / 0.07 | 0.80 / 0.01 | 0.99 / 0.03 |
| EXT | XLM-R (одна контрольна точка) | 0.70 / 0.00 | 0.92 / 0.18 | 0.92 / 0.00 | 0.10 / 0.00 | 0.72 / 0.00 |
| EXT | Каскад XLM-R(T) → ВММ | 0.76 / 0.00 | 0.92 / 0.15 | 0.92 / 0.00 | 0.12 / 0.00 | 0.56 / 0.00 |
| EXT | Паралельний XLM-R ∨ ВММ | 0.88 / 0.12 | 0.92 / 0.21 | 0.92 / 0.09 | 0.84 / 0.06 | 0.72 / 0.00 |
| UA-MT | XLM-R (одна контрольна точка) | 0.95 / 0.03 | 0.98 / 0.31 | 0.97 / 0.18 | 0.57 / 0.02 | 0.93 / 0.05 |
| UA-MT | Каскад XLM-R(T) → ВММ | 0.94 / 0.05 | 0.98 / 0.27 | 0.98 / 0.15 | 0.58 / 0.01 | 0.93 / 0.03 |
| UA-MT | Паралельний XLM-R ∨ ВММ | 0.97 / 0.18 | 1.00 / 0.44 | 0.99 / 0.30 | 0.85 / 0.10 | 0.94 / 0.05 |
| UA-NAZ | XLM-R (одна контрольна точка) | 0.82 / 0.08 | 0.99 / 0.39 | 1.00 / 0.23 | 0.30 / 0.11 | 0.84 / 0.11 |
| UA-NAZ | Каскад XLM-R(T) → ВММ | 0.93 / 0.09 | 0.99 / 0.40 | 0.99 / 0.23 | 0.36 / 0.11 | 0.75 / 0.07 |
| UA-NAZ | Паралельний XLM-R ∨ ВММ | 0.97 / 0.32 | 0.99 / 0.60 | 1.00 / 0.49 | 0.85 / 0.24 | 0.87 / 0.12 |
| UA-REAL | XLM-R (одна контрольна точка) | 0.35 / 0.27 | 0.90 / 0.54 | 0.77 / 0.40 | 0.35 / 0.13 | 0.42 / 0.17 |
| UA-REAL | Каскад XLM-R(T) → ВММ | 0.55 / 0.17 | 0.97 / 0.48 | 0.84 / 0.33 | 0.45 / 0.11 | 0.26 / 0.14 |
| UA-REAL | Паралельний XLM-R ∨ ВММ | 0.81 / 0.29 | 1.00 / 0.60 | 0.94 / 0.43 | 0.71 / 0.22 | 0.52 / 0.17 |

## URL loss in translation

Within the first 1200 characters that the models received, URLs survived translation in 59 of 63 UA-MT emails and 15 of 16 UA-NAZ emails; excluding the emails with lost URLs changes F1 of any model by at most 0.006 (`results/url_loss_analysis.csv`, `derived/url_loss_ua_naz.csv`). The 77% in `run_info.json` (`ua_mt_url_kept`) counts URLs anywhere in the full source text, including the part beyond 1200 characters that was never translated or shown to any model.
