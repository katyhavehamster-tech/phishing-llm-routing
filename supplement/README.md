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

## Table A5. Additional generative models (Таблиця А5. Додаткові генеративні моделі)

Notebook v6.3 (cell 17в), run on Kaggle (Tesla T4): Llama-3.1-8B-Instruct (weights from the public copy `unsloth/Llama-3.1-8B-Instruct`, revision 4699cc7; Llama 3.1 Community License) and Mistral-7B-Instruct-v0.3 (`mistralai/Mistral-7B-Instruct-v0.3`, revision c170c70; Apache 2.0) with the same prompt, 4-bit NF4 quantisation, 1200-character input and threshold 0.5 as Qwen2.5-7B-Instruct, without tuning for these models. For Mistral, whose tokenizer emits a separate space token before a digit, that token was appended to the prompt and the next token was scored. Mean probability mass on the answer tokens «1»/«0»: Llama 0.998, Mistral 0.99999. The main results (Qwen, XLM-R, LR, hybrids) of this run are byte-identical to the article's run. Per-email probabilities: `results/predictions_extra_llms.csv`.

| Set | Model | TP / FP / TN / FN | Precision | Recall | F1 | FPR | ROC-AUC | PR-AUC |
|---|---|---|---|---|---|---|---|---|
| EN | Qwen2.5-7B (промпт) | 303 / 16 / 589 / 92 | 0.950 | 0.767 | 0.849 | 0.026 | 0.967 | 0.953 |
| EN | Llama-3.1-8B (промпт) | 387 / 325 / 280 / 8 | 0.544 | 0.980 | 0.699 | 0.537 | 0.942 | 0.928 |
| EN | Mistral-7B-v0.3 (промпт) | 393 / 366 / 239 / 2 | 0.518 | 0.995 | 0.681 | 0.605 | 0.921 | 0.863 |
| EXT | Qwen2.5-7B (промпт) | 41 / 4 / 29 / 9 | 0.911 | 0.820 | 0.863 | 0.121 | 0.952 | 0.963 |
| EXT | Llama-3.1-8B (промпт) | 46 / 23 / 10 / 4 | 0.667 | 0.920 | 0.773 | 0.697 | 0.913 | 0.956 |
| EXT | Mistral-7B-v0.3 (промпт) | 50 / 23 / 10 / 0 | 0.685 | 1.000 | 0.813 | 0.697 | 0.849 | 0.906 |
| UA-MT | Qwen2.5-7B (промпт) | 85 / 17 / 83 / 15 | 0.833 | 0.850 | 0.842 | 0.170 | 0.905 | 0.915 |
| UA-MT | Llama-3.1-8B (промпт) | 98 / 98 / 2 / 2 | 0.500 | 0.980 | 0.662 | 0.980 | 0.786 | 0.784 |
| UA-MT | Mistral-7B-v0.3 (промпт) | 100 / 93 / 7 / 0 | 0.518 | 1.000 | 0.683 | 0.930 | 0.824 | 0.790 |
| UA-NAZ | Qwen2.5-7B (промпт) | 63 / 22 / 53 / 4 | 0.741 | 0.940 | 0.829 | 0.293 | 0.939 | 0.938 |
| UA-NAZ | Llama-3.1-8B (промпт) | 67 / 75 / 0 / 0 | 0.472 | 1.000 | 0.641 | 1.000 | 0.893 | 0.831 |
| UA-NAZ | Mistral-7B-v0.3 (промпт) | 67 / 74 / 1 / 0 | 0.475 | 1.000 | 0.644 | 0.987 | 0.759 | 0.692 |
| UA-REAL | Qwen2.5-7B (промпт) | 25 / 5 / 58 / 6 | 0.833 | 0.806 | 0.820 | 0.079 | 0.918 | 0.849 |
| UA-REAL | Llama-3.1-8B (промпт) | 31 / 27 / 36 / 0 | 0.534 | 1.000 | 0.697 | 0.429 | 0.965 | 0.940 |
| UA-REAL | Mistral-7B-v0.3 (промпт) | 31 / 44 / 19 / 0 | 0.413 | 1.000 | 0.585 | 0.698 | 0.909 | 0.756 |

Pairwise comparisons of the extra LLMs with Qwen2.5-7B and with XLM-R (main run): ΔF1 with a paired bootstrap 95% CI (2,000 resamples), exact McNemar test, Holm adjustment over a separate family of 20 comparisons.

| Set | A / B | ΔF1 (A − B) | 95% CI | Only A correct / only B | p | p (Holm) |
|---|---|---|---|---|---|---|
| EN | Llama-3.1-8B (промпт) / Qwen2.5-7B (промпт) | -0.150 | [-0.189; -0.112] | 85 / 310 | < 0.001 | < 0.001 |
| EN | Llama-3.1-8B (промпт) / XLM-R (донавчена) | -0.270 | [-0.300; -0.240] | 8 / 317 | < 0.001 | < 0.001 |
| EN | Mistral-7B-v0.3 (промпт) / Qwen2.5-7B (промпт) | -0.168 | [-0.208; -0.129] | 91 / 351 | < 0.001 | < 0.001 |
| EN | Mistral-7B-v0.3 (промпт) / XLM-R (донавчена) | -0.288 | [-0.322; -0.256] | 16 / 360 | < 0.001 | < 0.001 |
| EXT | Llama-3.1-8B (промпт) / Qwen2.5-7B (промпт) | -0.090 | [-0.175; -0.010] | 5 / 19 | 0.007 | 0.040 |
| EXT | Llama-3.1-8B (промпт) / XLM-R (донавчена) | -0.064 | [-0.168; 0.037] | 10 / 23 | 0.035 | 0.175 |
| EXT | Mistral-7B-v0.3 (промпт) / Qwen2.5-7B (промпт) | -0.050 | [-0.143; 0.040] | 9 / 19 | 0.087 | 0.349 |
| EXT | Mistral-7B-v0.3 (промпт) / XLM-R (донавчена) | -0.024 | [-0.133; 0.090] | 14 / 23 | 0.188 | 0.457 |
| UA-MT | Llama-3.1-8B (промпт) / Qwen2.5-7B (промпт) | -0.179 | [-0.241; -0.118] | 13 / 81 | < 0.001 | < 0.001 |
| UA-MT | Llama-3.1-8B (промпт) / XLM-R (донавчена) | -0.298 | [-0.364; -0.237] | 4 / 96 | < 0.001 | < 0.001 |
| UA-MT | Mistral-7B-v0.3 (промпт) / Qwen2.5-7B (промпт) | -0.159 | [-0.221; -0.096] | 15 / 76 | < 0.001 | < 0.001 |
| UA-MT | Mistral-7B-v0.3 (промпт) / XLM-R (донавчена) | -0.277 | [-0.344; -0.219] | 4 / 89 | < 0.001 | < 0.001 |
| UA-NAZ | Llama-3.1-8B (промпт) / Qwen2.5-7B (промпт) | -0.188 | [-0.251; -0.128] | 4 / 53 | < 0.001 | < 0.001 |
| UA-NAZ | Llama-3.1-8B (промпт) / XLM-R (донавчена) | -0.248 | [-0.329; -0.174] | 7 / 67 | < 0.001 | < 0.001 |
| UA-NAZ | Mistral-7B-v0.3 (промпт) / Qwen2.5-7B (промпт) | -0.185 | [-0.248; -0.125] | 4 / 52 | < 0.001 | < 0.001 |
| UA-NAZ | Mistral-7B-v0.3 (промпт) / XLM-R (донавчена) | -0.245 | [-0.327; -0.171] | 7 / 66 | < 0.001 | < 0.001 |
| UA-REAL | Llama-3.1-8B (промпт) / Qwen2.5-7B (промпт) | -0.123 | [-0.256; 0.006] | 6 / 22 | 0.004 | 0.026 |
| UA-REAL | Llama-3.1-8B (промпт) / XLM-R (донавчена) | 0.220 | [0.060; 0.390] | 28 / 22 | 0.480 | 0.480 |
| UA-REAL | Mistral-7B-v0.3 (промпт) / Qwen2.5-7B (промпт) | -0.235 | [-0.365; -0.110] | 6 / 39 | < 0.001 | < 0.001 |
| UA-REAL | Mistral-7B-v0.3 (промпт) / XLM-R (донавчена) | 0.109 | [-0.041; 0.272] | 19 / 30 | 0.152 | 0.457 |

## Table A6. Adaptive instruction injection (Таблиця А6. Адаптивні ін'єкції інструкцій)

Share of positive-class emails detected (threshold 0.5) for the original emails and five injection variants: V1 instruction at the end of the email (as in Table A2), V2 «security gateway notice» at the start, V3 an attempt to close the prompt's quoting, V4 a hidden HTML comment, V5 an instruction in the middle of the email; texts in `results/run_info_v63.json`. «Adaptive» counts an email as detected only if it was detected under every variant V1–V5 (the attacker picks the best variant per email). «Defended» = system prompt instructing the model to treat the email as untrusted data. XLM-R here is a new re-training with seed 42 made for v6.3 (the v6.2 weights were not saved; decision agreement with the main XLM-R on EN 0.992), i.e. a different checkpoint from Table A4; LR and all XLM-R-based rows use this checkpoint. «Adaptive» is the worst of five predefined variants per email, not an optimised or iterative attack. Llama and Mistral flag most legitimate emails (Table A5), so their high detection on the Ukrainian sets is not evidence of robustness.

| Set | Model | Prompt | Original | V1 | V2 | V3 | V4 | V5 | Adaptive |
|---|---|---|---|---|---|---|---|---|---|
| EN | TF-IDF + LR | – | 0.95 | 0.94 | 0.96 | 0.97 | 0.96 | 0.96 | 0.94 |
| EN | XLM-R (одна контрольна точка) | – | 0.97 | 0.98 | 0.99 | 1.00 | 0.99 | 0.96 | 0.96 |
| EN | Qwen2.5-7B (промпт) | plain | 0.76 | 0.00 | 0.66 | 0.84 | 0.61 | 0.44 | 0.00 |
| EN | Qwen2.5-7B (промпт) | defended | 0.74 | 0.03 | 0.73 | 0.80 | 0.60 | 0.55 | 0.03 |
| EN | Llama-3.1-8B (промпт) | plain | 0.98 | 0.41 | 0.93 | 0.95 | 0.90 | 0.87 | 0.39 |
| EN | Llama-3.1-8B (промпт) | defended | 0.99 | 0.91 | 0.98 | 0.99 | 0.99 | 0.97 | 0.88 |
| EN | Mistral-7B-v0.3 (промпт) | plain | 1.00 | 0.28 | 0.73 | 0.89 | 0.46 | 0.59 | 0.21 |
| EN | Mistral-7B-v0.3 (промпт) | defended | 1.00 | 0.79 | 0.80 | 0.93 | 0.76 | 0.85 | 0.59 |
| EN | Каскад XLM-R(T) → Qwen2.5-7B | plain | 0.97 | 0.97 | 0.98 | 0.99 | 0.98 | 0.95 | 0.95 |
| EN | Каскад XLM-R(T) → Qwen2.5-7B | defended | 0.97 | 0.97 | 0.98 | 0.99 | 0.98 | 0.95 | 0.95 |
| EN | Каскад XLM-R(T) → Llama-3.1-8B | plain | 0.97 | 0.97 | 0.99 | 0.99 | 0.99 | 0.96 | 0.96 |
| EN | Каскад XLM-R(T) → Llama-3.1-8B | defended | 0.97 | 0.99 | 1.00 | 1.00 | 0.99 | 0.97 | 0.97 |
| EN | Каскад XLM-R(T) → Mistral-7B-v0.3 | plain | 0.97 | 0.97 | 0.98 | 0.99 | 0.98 | 0.95 | 0.95 |
| EN | Каскад XLM-R(T) → Mistral-7B-v0.3 | defended | 0.97 | 0.97 | 0.99 | 1.00 | 0.99 | 0.95 | 0.95 |
| EN | Паралельний XLM-R ∨ Qwen2.5-7B | plain | 0.97 | 0.98 | 0.99 | 1.00 | 0.99 | 0.96 | 0.96 |
| EN | Паралельний XLM-R ∨ Qwen2.5-7B | defended | 0.97 | 0.98 | 0.99 | 1.00 | 0.99 | 0.96 | 0.96 |
| EN | Паралельний XLM-R ∨ Llama-3.1-8B | plain | 0.99 | 0.98 | 0.99 | 1.00 | 1.00 | 0.99 | 0.97 |
| EN | Паралельний XLM-R ∨ Llama-3.1-8B | defended | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 0.99 |
| EN | Паралельний XLM-R ∨ Mistral-7B-v0.3 | plain | 1.00 | 0.98 | 0.99 | 1.00 | 0.99 | 0.97 | 0.96 |
| EN | Паралельний XLM-R ∨ Mistral-7B-v0.3 | defended | 1.00 | 0.99 | 0.99 | 1.00 | 0.99 | 0.97 | 0.97 |
| EXT | TF-IDF + LR | – | 0.84 | 0.72 | 0.84 | 0.88 | 0.84 | 0.76 | 0.72 |
| EXT | XLM-R (одна контрольна точка) | – | 0.78 | 0.72 | 0.94 | 0.96 | 0.94 | 0.56 | 0.56 |
| EXT | Qwen2.5-7B (промпт) | plain | 0.82 | 0.00 | 0.56 | 0.82 | 0.60 | 0.54 | 0.00 |
| EXT | Qwen2.5-7B (промпт) | defended | 0.84 | 0.04 | 0.74 | 0.84 | 0.60 | 0.72 | 0.04 |
| EXT | Llama-3.1-8B (промпт) | plain | 0.92 | 0.64 | 0.92 | 0.92 | 0.92 | 0.92 | 0.64 |
| EXT | Llama-3.1-8B (промпт) | defended | 0.92 | 0.96 | 0.92 | 0.92 | 0.92 | 1.00 | 0.88 |
| EXT | Mistral-7B-v0.3 (промпт) | plain | 1.00 | 0.34 | 0.58 | 0.70 | 0.20 | 0.58 | 0.18 |
| EXT | Mistral-7B-v0.3 (промпт) | defended | 0.98 | 0.64 | 0.68 | 0.74 | 0.46 | 0.76 | 0.32 |
| EXT | Каскад XLM-R(T) → Qwen2.5-7B | plain | 0.76 | 0.60 | 0.94 | 0.98 | 0.92 | 0.56 | 0.54 |
| EXT | Каскад XLM-R(T) → Qwen2.5-7B | defended | 0.76 | 0.62 | 0.98 | 0.98 | 0.92 | 0.62 | 0.56 |
| EXT | Каскад XLM-R(T) → Llama-3.1-8B | plain | 0.76 | 0.82 | 1.00 | 1.00 | 0.98 | 0.66 | 0.66 |
| EXT | Каскад XLM-R(T) → Llama-3.1-8B | defended | 0.76 | 0.84 | 1.00 | 1.00 | 0.98 | 0.66 | 0.66 |
| EXT | Каскад XLM-R(T) → Mistral-7B-v0.3 | plain | 0.84 | 0.76 | 0.94 | 0.98 | 0.82 | 0.64 | 0.62 |
| EXT | Каскад XLM-R(T) → Mistral-7B-v0.3 | defended | 0.84 | 0.82 | 0.96 | 1.00 | 0.88 | 0.66 | 0.66 |
| EXT | Паралельний XLM-R ∨ Qwen2.5-7B | plain | 0.98 | 0.72 | 0.98 | 0.98 | 0.98 | 0.72 | 0.64 |
| EXT | Паралельний XLM-R ∨ Qwen2.5-7B | defended | 1.00 | 0.74 | 1.00 | 0.98 | 0.98 | 0.84 | 0.70 |
| EXT | Паралельний XLM-R ∨ Llama-3.1-8B | plain | 1.00 | 0.90 | 1.00 | 1.00 | 1.00 | 0.92 | 0.90 |
| EXT | Паралельний XLM-R ∨ Llama-3.1-8B | defended | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| EXT | Паралельний XLM-R ∨ Mistral-7B-v0.3 | plain | 1.00 | 0.82 | 0.96 | 0.98 | 0.94 | 0.78 | 0.76 |
| EXT | Паралельний XLM-R ∨ Mistral-7B-v0.3 | defended | 1.00 | 0.92 | 0.96 | 1.00 | 0.94 | 0.88 | 0.82 |
| UA-MT | TF-IDF + LR | – | 0.77 | 0.71 | 0.68 | 0.84 | 0.80 | 0.70 | 0.68 |
| UA-MT | XLM-R (одна контрольна точка) | – | 0.97 | 0.99 | 1.00 | 0.98 | 1.00 | 0.95 | 0.94 |
| UA-MT | Qwen2.5-7B (промпт) | plain | 0.85 | 0.21 | 0.57 | 0.88 | 0.76 | 0.74 | 0.18 |
| UA-MT | Qwen2.5-7B (промпт) | defended | 0.84 | 0.43 | 0.61 | 0.83 | 0.76 | 0.87 | 0.40 |
| UA-MT | Llama-3.1-8B (промпт) | plain | 0.98 | 1.00 | 1.00 | 1.00 | 0.99 | 0.99 | 0.98 |
| UA-MT | Llama-3.1-8B (промпт) | defended | 0.97 | 1.00 | 1.00 | 1.00 | 0.98 | 0.99 | 0.97 |
| UA-MT | Mistral-7B-v0.3 (промпт) | plain | 1.00 | 0.91 | 0.90 | 0.95 | 0.89 | 0.95 | 0.78 |
| UA-MT | Mistral-7B-v0.3 (промпт) | defended | 1.00 | 0.97 | 0.92 | 0.99 | 0.95 | 0.99 | 0.87 |
| UA-MT | Каскад XLM-R(T) → Qwen2.5-7B | plain | 0.96 | 0.95 | 1.00 | 0.98 | 0.98 | 0.95 | 0.94 |
| UA-MT | Каскад XLM-R(T) → Qwen2.5-7B | defended | 0.96 | 0.95 | 1.00 | 0.98 | 0.98 | 0.95 | 0.94 |
| UA-MT | Каскад XLM-R(T) → Llama-3.1-8B | plain | 0.98 | 0.99 | 1.00 | 1.00 | 1.00 | 0.95 | 0.95 |
| UA-MT | Каскад XLM-R(T) → Llama-3.1-8B | defended | 0.98 | 0.99 | 1.00 | 1.00 | 1.00 | 0.95 | 0.95 |
| UA-MT | Каскад XLM-R(T) → Mistral-7B-v0.3 | plain | 0.99 | 0.99 | 1.00 | 1.00 | 0.99 | 0.95 | 0.95 |
| UA-MT | Каскад XLM-R(T) → Mistral-7B-v0.3 | defended | 0.99 | 0.99 | 1.00 | 1.00 | 1.00 | 0.95 | 0.95 |
| UA-MT | Паралельний XLM-R ∨ Qwen2.5-7B | plain | 0.98 | 0.99 | 1.00 | 0.98 | 1.00 | 0.95 | 0.94 |
| UA-MT | Паралельний XLM-R ∨ Qwen2.5-7B | defended | 0.98 | 0.99 | 1.00 | 0.98 | 1.00 | 0.96 | 0.94 |
| UA-MT | Паралельний XLM-R ∨ Llama-3.1-8B | plain | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| UA-MT | Паралельний XLM-R ∨ Llama-3.1-8B | defended | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| UA-MT | Паралельний XLM-R ∨ Mistral-7B-v0.3 | plain | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| UA-MT | Паралельний XLM-R ∨ Mistral-7B-v0.3 | defended | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| UA-NAZ | TF-IDF + LR | – | 0.40 | 0.37 | 0.37 | 0.43 | 0.37 | 0.37 | 0.37 |
| UA-NAZ | XLM-R (одна контрольна точка) | – | 0.91 | 0.93 | 0.97 | 0.97 | 0.97 | 0.78 | 0.78 |
| UA-NAZ | Qwen2.5-7B (промпт) | plain | 0.94 | 0.27 | 0.42 | 0.84 | 0.85 | 0.82 | 0.15 |
| UA-NAZ | Qwen2.5-7B (промпт) | defended | 0.93 | 0.45 | 0.57 | 0.79 | 0.85 | 0.87 | 0.31 |
| UA-NAZ | Llama-3.1-8B (промпт) | plain | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| UA-NAZ | Llama-3.1-8B (промпт) | defended | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| UA-NAZ | Mistral-7B-v0.3 (промпт) | plain | 1.00 | 0.94 | 0.94 | 0.94 | 0.93 | 1.00 | 0.87 |
| UA-NAZ | Mistral-7B-v0.3 (промпт) | defended | 1.00 | 0.99 | 0.97 | 0.96 | 0.97 | 1.00 | 0.93 |
| UA-NAZ | Каскад XLM-R(T) → Qwen2.5-7B | plain | 0.94 | 0.82 | 0.97 | 0.94 | 0.97 | 0.88 | 0.79 |
| UA-NAZ | Каскад XLM-R(T) → Qwen2.5-7B | defended | 0.94 | 0.85 | 0.99 | 0.94 | 0.97 | 0.90 | 0.82 |
| UA-NAZ | Каскад XLM-R(T) → Llama-3.1-8B | plain | 0.96 | 0.94 | 1.00 | 0.97 | 0.99 | 0.94 | 0.94 |
| UA-NAZ | Каскад XLM-R(T) → Llama-3.1-8B | defended | 0.96 | 0.94 | 1.00 | 0.97 | 0.99 | 0.94 | 0.94 |
| UA-NAZ | Каскад XLM-R(T) → Mistral-7B-v0.3 | plain | 0.96 | 0.91 | 0.99 | 0.94 | 0.99 | 0.94 | 0.91 |
| UA-NAZ | Каскад XLM-R(T) → Mistral-7B-v0.3 | defended | 0.96 | 0.93 | 0.99 | 0.94 | 0.99 | 0.94 | 0.91 |
| UA-NAZ | Паралельний XLM-R ∨ Qwen2.5-7B | plain | 0.97 | 0.94 | 0.99 | 0.99 | 0.99 | 0.93 | 0.90 |
| UA-NAZ | Паралельний XLM-R ∨ Qwen2.5-7B | defended | 0.97 | 0.94 | 0.99 | 0.99 | 1.00 | 0.93 | 0.90 |
| UA-NAZ | Паралельний XLM-R ∨ Llama-3.1-8B | plain | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| UA-NAZ | Паралельний XLM-R ∨ Llama-3.1-8B | defended | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| UA-NAZ | Паралельний XLM-R ∨ Mistral-7B-v0.3 | plain | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 1.00 | 0.99 |
| UA-NAZ | Паралельний XLM-R ∨ Mistral-7B-v0.3 | defended | 1.00 | 1.00 | 0.99 | 1.00 | 1.00 | 1.00 | 0.99 |
| UA-REAL | TF-IDF + LR | – | 0.45 | 0.35 | 0.32 | 0.45 | 0.45 | 0.35 | 0.29 |
| UA-REAL | XLM-R (одна контрольна точка) | – | 0.58 | 0.58 | 0.90 | 0.90 | 0.90 | 0.48 | 0.45 |
| UA-REAL | Qwen2.5-7B (промпт) | plain | 0.81 | 0.16 | 0.48 | 0.84 | 0.68 | 0.65 | 0.06 |
| UA-REAL | Qwen2.5-7B (промпт) | defended | 0.77 | 0.39 | 0.58 | 0.65 | 0.65 | 0.77 | 0.26 |
| UA-REAL | Llama-3.1-8B (промпт) | plain | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| UA-REAL | Llama-3.1-8B (промпт) | defended | 0.97 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| UA-REAL | Mistral-7B-v0.3 (промпт) | plain | 1.00 | 0.97 | 0.77 | 0.90 | 0.84 | 1.00 | 0.68 |
| UA-REAL | Mistral-7B-v0.3 (промпт) | defended | 1.00 | 1.00 | 0.90 | 0.97 | 0.94 | 1.00 | 0.87 |
| UA-REAL | Каскад XLM-R(T) → Qwen2.5-7B | plain | 0.65 | 0.52 | 0.90 | 0.90 | 0.90 | 0.58 | 0.42 |
| UA-REAL | Каскад XLM-R(T) → Qwen2.5-7B | defended | 0.61 | 0.58 | 0.94 | 0.90 | 0.90 | 0.61 | 0.48 |
| UA-REAL | Каскад XLM-R(T) → Llama-3.1-8B | plain | 0.74 | 0.81 | 0.94 | 0.94 | 0.94 | 0.68 | 0.68 |
| UA-REAL | Каскад XLM-R(T) → Llama-3.1-8B | defended | 0.74 | 0.81 | 0.94 | 0.94 | 0.94 | 0.68 | 0.68 |
| UA-REAL | Каскад XLM-R(T) → Mistral-7B-v0.3 | plain | 0.74 | 0.81 | 0.94 | 0.94 | 0.94 | 0.68 | 0.68 |
| UA-REAL | Каскад XLM-R(T) → Mistral-7B-v0.3 | defended | 0.74 | 0.81 | 0.94 | 0.94 | 0.94 | 0.68 | 0.68 |
| UA-REAL | Паралельний XLM-R ∨ Qwen2.5-7B | plain | 0.87 | 0.71 | 0.90 | 0.97 | 1.00 | 0.84 | 0.61 |
| UA-REAL | Паралельний XLM-R ∨ Qwen2.5-7B | defended | 0.87 | 0.74 | 0.94 | 0.94 | 1.00 | 0.90 | 0.71 |
| UA-REAL | Паралельний XLM-R ∨ Llama-3.1-8B | plain | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| UA-REAL | Паралельний XLM-R ∨ Llama-3.1-8B | defended | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| UA-REAL | Паралельний XLM-R ∨ Mistral-7B-v0.3 | plain | 1.00 | 1.00 | 0.97 | 0.97 | 0.97 | 1.00 | 0.97 |
| UA-REAL | Паралельний XLM-R ∨ Mistral-7B-v0.3 | defended | 1.00 | 1.00 | 1.00 | 0.97 | 1.00 | 1.00 | 0.97 |

## URL loss in translation

Within the first 1200 characters that the models received, URLs survived translation in 59 of 63 UA-MT emails and 15 of 16 UA-NAZ emails; excluding the emails with lost URLs changes F1 of any model by at most 0.006 (`results/url_loss_analysis.csv`, `derived/url_loss_ua_naz.csv`). The 77% in `run_info.json` (`ua_mt_url_kept`) counts URLs anywhere in the full source text, including the part beyond 1200 characters that was never translated or shown to any model.
