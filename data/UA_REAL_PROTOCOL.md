# UA-REAL: how the 94 messages were assembled and how to rebuild them

The texts are not redistributed (third-party publications). This file documents how each text was taken from its source so that the set can be rebuilt and checked against the published hashes.

## Inclusion
- Positive class (31): phishing messages of 2022–2026 whose text was published in warnings of CERT-UA, the Cyber Police, the Centre for Countering Disinformation, banks, mobile operators and state bodies, or in news articles citing these warnings (13 e-mails, 18 SMS / messenger messages).
- Negative class (63): 26 e-mails from public archives of Ukrainian software-localisation mailing lists, 15 subscription newsletters and posts, 22 service notifications of state bodies and companies published in their official channels.
- Only messages in Ukrainian with an accessible original source; 3 messages in Russian or Latin transliteration were excluded.
- The set was frozen before any model was run on it; no model, prompt, threshold or temperature was tuned on it.

## Text extraction rules
1. Take only the quoted message itself (the text shown as the SMS / letter / post), not the surrounding article.
2. Remove e-mail headers (From, To, Subject lines shown as headers) and editorial notes inserted by the publisher.
3. Keep abbreviation marks of the publisher as they appear (square brackets, ellipses); they occur in both classes (13 phishing, 20 legitimate).
4. The notebook then collapses whitespace and keeps the first 1200 characters (`clean_text` + `cut`); the hash in `predictions.csv` is computed on that model input.
5. Source URL and publication date are listed in `ua_real_metadata.csv`. Pages may change; when a page is no longer available, use an archived copy of the URL for the listed date.

## Labels
- Label = source (warning about phishing → 1; official channel / subscribed list → 0).
- Two annotators labelled all messages blind to label and source, in different orders (classes: phishing, other fraud, spam, legitimate): `ua_real_annotations.csv`. Binary agreement with the source labels κ = 0.856 and 0.502, between annotators κ = 0.552 (four classes 0.524); unanimous on 76 messages, of which 94.7% agree with the source label.
- Disagreements were not re-adjudicated: the analysis keeps the source labels and reports a sensitivity analysis with each annotator's labels, unanimous items only and the majority of three (`derived/ua_real_label_sensitivity.csv`).

## Identifiers and hashes
- `sample_id` (= `id` in the metadata and annotations) corresponds to row `i` = `sample_id − 1` of the UA-REAL block in `results/predictions.csv`; see `ua_real_id_map.csv`.
- `sha256_16` in `predictions.csv` is the hash of the exact model input (whitespace collapsed, stripped, first 1200 characters). `sha256_16_first1200` in the metadata is the hash of the first 1200 characters of the raw text as stored in `ua_sample.xlsx` (no whitespace normalisation), which is why the two short hashes differ for messages containing repeated spaces or line breaks.
- Verified on 10.10.2026 with the original `ua_sample.xlsx` (`scripts/verify_ua_real.py`): the raw-text hash matches the metadata and the model-input hash matches `predictions.csv` for 94/94 messages, labels and ids match for 94/94. Full 64-character hashes of both representations are in `ua_real_hashes.csv` and `ua_real_id_map.csv`.
