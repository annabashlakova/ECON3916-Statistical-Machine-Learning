# The Polynomial Trap: Bias-Variance Tradeoff

## Overview
This project investigates the bias-variance tradeoff through polynomial regression
on two datasets: synthetic sine-wave data and the Ames Housing dataset.

## Methodology
Synthetic data (n=50 train, n=200 test) was generated from y = sin(2πx) + ε and
fit with polynomial models of degree 1–15. Complexity curves tracked training and
test RMSE across all degrees. K-fold cross-validation (k=5) was used to select
the optimal degree without accessing test data. The same framework was applied to
the Ames Housing dataset (1,460 observations, 80 features), comparing a
5-feature model against a kitchen-sink 37-feature OLS baseline.

## Key Findings
- Polynomial degrees 3–5 minimized test RMSE on synthetic data; higher degrees
  overfitted, collapsing training RMSE while inflating test RMSE by over 40%
- CV-selected degree matched the true test-optimal degree, validating
  cross-validation as a reliable model selection tool
- On Ames Housing, the parsimonious 5-feature model achieved lower CV RMSE than
  the kitchen-sink model, demonstrating that variance reduction can outweigh the
  cost of modest bias

## Tools
Python · NumPy · scikit-learn (PolynomialFeatures, LinearRegression,
cross_val_score) · Matplotlib
