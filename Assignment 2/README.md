# Audit 02: Deconstructing Statistical Lies

## Overview
As a Data Quality Auditor at Pareto Ventures, I audited three portfolio companies 
that claimed "perfect" metrics. Each one hid a statistical lie behind their averages.

## Key Findings

### Phase 1: Latency Skew (NebulaCloud)
NebulaCloud claimed a Mean Latency of 35ms. Simulating their traffic revealed 
20 spike requests (1000–5000ms) that inflated the Standard Deviation to 300+ms 
while the MAD stayed around 10ms. The mean and SD are vanity metrics for skewed 
data — robust measures like median and MAD tell the real story.

### Phase 2: False Positive Paradox (IntegrityAI)
IntegrityAI boasted 98% accuracy on their plagiarism detector. Using Bayes' Theorem, 
we showed that in an Honors Seminar (base rate = 0.1%), a flagged student only has 
a ~5% chance of actually cheating. Accuracy means nothing without the base rate.

### Phase 3: Sample Ratio Mismatch (FinFlash)
FinFlash's A/B test showed a 50,250/49,750 split. A manual Chi-Square test returned 
2.5, below the 3.84 critical value — the split is within random variation and the 
experiment passes the bias audit.

### Phase 4: Survivorship Bias (Memecoin Graveyard)
Simulating 10,000 token launches with a Pareto distribution showed that analyzing 
only the Top 1% of survivors inflates the mean market cap dramatically. Platforms 
that hide failed tokens create a massively misleading picture of crypto returns.

## Tools Used
Python, NumPy, Pandas, Matplotlib, Seaborn

## Lesson
Every metric tells a story — the auditor's job is to find out if that story is fiction.
