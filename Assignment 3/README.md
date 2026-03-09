# Assignment 3: The Causal Architecture
**Econ 3916 | Senior Data Economist Simulation | SwiftCart Logistics**

---

## Overview

This notebook operates inside a real-world logistics context: SwiftCart, a multinational on-demand delivery platform. The executive board is paralyzed by contradictory internal data across three critical business questions — driver compensation equity, algorithm efficacy, and loyalty program ROI. The mandate is to cut through statistical noise using heavy computation in place of fragile parametric assumptions.

---

## Tech Stack
```
Python | NumPy | Pandas | Matplotlib | Seaborn | Scikit-learn
```

---

## Phase 1 — Bootstrapping Non-Parametric Uncertainty

### Step 1.1: Zero-Inflated Tip Distribution
Simulated an audit sample of 250 driver tips combining 100 exact zero-tips with 150 draws from an Exponential distribution (scale=5.0). This replicates the real topology of gig-economy tip data: zero-inflated and heavily right-skewed, where the Central Limit Theorem breaks down entirely.

### Step 1.2: Manual Bootstrap Engine
- Resampled driver_tips with replacement across 10,000 iterations
- Computed the median of each resample
- Extracted a 95% Confidence Interval via np.percentile at the 2.5th and 97.5th percentiles
- Analyzed the structural asymmetry of the bootstrap CI versus a standard parametric T-interval

---

## Phase 2 — Falsification in Logistics A/B Testing

### Step 2.1: Algorithmic Routing Crash
Generated synthetic A/B test data across 1,000 deliveries:
- Control (n=500): Normal distribution (mean=35, sd=5)
- Treatment (n=500): Log-Normal distribution (mean=3.4, sigma=0.4) to simulate crash-loop outliers

### Step 2.2: Manual Permutation Test
- Concatenated all 1,000 deliveries and ran 5,000 shuffle iterations using np.random.permutation
- Calculated the exact empirical p-value: proportion of permutations yielding a difference ≥ observed
- Result: p = 0.0292, significant at α=0.05 with zero distributional assumptions

---

## Phase 3 — Causal Control & Selection Bias Mitigation

### Step 3.1: The Loyalty Program Paradox
Loaded swiftcart_loyalty.csv and calculated the Naive Simple Difference in Means (SDO) between SwiftPass subscribers and non-subscribers, identifying severe selection bias from high-volume power users self-selecting into the program.

### Step 3.2: Propensity Score Matching (PSM) Architecture

1. Logistic Regression to estimate propensity scores from pre-treatment covariates
2. Nearest Neighbor Matching to pair each subscriber with the most similar non-subscriber
3. ATT Calculation on the matched dataset to isolate the true causal effect

| Metric | Value |
|---|---|
| Naive SDO | $30.85 |
| Causal ATT (PSM) | $8.65 |
| Selection Bias Absorbed | $22.20 |

72% of the naive effect was pure selection bias.

---

## Phase 4 — AI Expansion: Love Plot Visualization

Generated a production-grade Love Plot (Standardized Mean Differences) using seaborn and matplotlib to visually audit covariate balance before and after matching across all three pre-treatment features.

---

## Key Results Summary

| Phase | Method | Key Finding |
|---|---|---|
| 1.2 | Bootstrap CI | Asymmetric interval reflects zero-floor reality |
| 2.2 | Permutation Test | p = 0.0292, algorithm effect is significant |
| 3.1 | Naive SDO | $30.85 lift — contaminated by selection bias |
| 3.2 | PSM ATT | $8.65 true causal lift — 72% was spurious |

