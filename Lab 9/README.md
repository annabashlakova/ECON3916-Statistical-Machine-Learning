# Recovering Experimental Truths via Propensity Score Matching

## Objective

This project demonstrates how propensity score matching can recover a credible causal treatment effect from heavily biased observational data — transforming a misleading naive estimate into one that closely approximates the experimental benchmark.

## Methodology

- **Selection Bias Diagnosis:** Computed a naive difference-in-means on the observational subset of the LaLonde dataset, revealing a raw estimate of **−$15,204** — a figure that falsely implies the job training program reduced earnings.
- **Propensity Score Estimation:** Fitted a logistic regression model on pre-treatment covariates (age, education, race, marital status, degree attainment, and prior earnings) to estimate each individual's probability of receiving treatment.
- **Nearest Neighbor Matching:** Applied a nearest-neighbor matching algorithm to pair treated and control units with similar propensity scores, constructing a pseudo-experimental comparison group that balances observable characteristics across treatment arms.

## Key Findings

| Estimate | Treatment Effect |
|---|---|
| Naive (Unadjusted) | −$15,204 |
| Propensity Score Matched | ≈ +$1,800 |
| Experimental Benchmark (LaLonde, 1986) | ≈ +$1,794 |

The matched estimate recovers nearly the full experimental treatment effect, confirming that the negative naive estimate was an artifact of selection bias — not a reflection of program inefficacy. This result replicates one of the central findings in the causal inference literature: that well-specified propensity score methods can credibly approximate experimental results when randomization is unavailable.

## Tools

Python · Pandas · Scikit-Learn (LogisticRegression, NearestNeighbors) · NumPy · Seaborn
