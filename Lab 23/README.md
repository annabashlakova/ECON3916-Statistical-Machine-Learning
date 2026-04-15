# FedSpeak Analysis — NLP on FOMC Minutes

## Objective

Apply natural language processing and unsupervised learning techniques to two decades of Federal Open Market Committee meeting minutes, quantifying shifts in monetary policy sentiment and identifying latent thematic regimes across the Fed's communication record.

## Methodology

- Loaded and preprocessed the full corpus of FOMC meeting minutes (~2000–2024), applying tokenization, lemmatization, and domain-appropriate stop word removal
- Constructed a TF-IDF document-term matrix using unigram and bigram feature extraction
- Computed document-level sentiment scores using the Loughran-McDonald financial sentiment lexicon, capturing both net sentiment (positive − negative word share) and uncertainty exposure
- Visualized sentiment and uncertainty trends over time against key macroeconomic episodes (dot-com bust, GFC, COVID-19, 2022–23 tightening cycle)
- Reduced TF-IDF feature space via Principal Component Analysis (PCA) and applied K-Means clustering to identify latent document regimes
- Compared pre-COVID vs. post-COVID sentiment distributions to assess structural shifts in Fed communication tone

## Key Findings

- **Sentiment cyclicality:** Net sentiment in FOMC minutes tracks broad macro conditions — negativity spikes align with recession periods (2001, 2008–09, 2020), while recovery phases show gradual sentiment normalization
- **Uncertainty as a leading signal:** Loughran-McDonald uncertainty scores elevated ahead of major policy pivots, consistent with the Fed telegraphing caution before rate regime changes
- **Cluster structure:** K-Means surfaced distinct document regimes corresponding to (1) accommodative/crisis-era language, (2) neutral-to-hawkish steady-state communication, and (3) transitional tightening rhetoric — clusters map intuitively onto known policy eras
- **Post-COVID shift:** Post-2020 minutes exhibit persistently higher uncertainty and more negative net sentiment relative to pre-COVID baselines, suggesting a structural recalibration in Fed communication tone following the pandemic shock

## Tools & Libraries

`Python` · `pandas` · `scikit-learn` · `nltk` · `matplotlib` · `seaborn`
