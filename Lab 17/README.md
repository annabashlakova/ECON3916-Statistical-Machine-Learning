NY Fed Yield Curve Recession Model Replication
Objective: Replicate the Federal Reserve Bank of New York's probit-based recession forecasting framework using logistic regression on Treasury yield spread data to evaluate the term structure's predictive power over NBER business cycle turning points at a 12-month horizon.
Methodology

Sourced the 10-Year minus 3-Month Treasury yield spread (T10Y3M) and NBER recession indicator (USREC) from FRED via the fredapi Python client, covering January 1970 through March 2026.
Resampled daily spread observations to month-end frequency and constructed a 12-month lagged predictor to align the yield curve signal with the forecast horizon used in the original NY Fed specification.
Estimated a Linear Probability Model (OLS) as a baseline to illustrate the boundary violations inherent in linear binary-response models, then fitted a logistic regression via scikit-learn's LogisticRegression as the primary specification.
Recovered coefficient estimates, the yield spread odds ratio, and 95% confidence intervals using statsmodels.Logit to complement scikit-learn's point estimates with formal inference.
Generated a full-sample predicted recession probability time series and evaluated model behavior during the 2022–2024 yield curve inversion episode.

Key Findings

The Linear Probability Model produced predicted probabilities below zero for 16.2% of observations, confirming the well-known theoretical deficiency that motivates the logistic specification.
The logistic model estimated a yield spread odds ratio of approximately 0.45 (95% CI: 0.33–0.60), implying that a one-percentage-point steepening of the curve reduces recession odds by roughly 55% — consistent with the sign and magnitude reported in the NY Fed's published estimates.
All logistic predicted probabilities remained bounded within [0, 1], with the full-sample mean predicted probability (6.9%) closely tracking the unconditional recession base rate (6.9%), indicating well-calibrated baseline risk.
During the 2022–2024 inversion, the model flagged recession probabilities in the 25–43% range — materially elevated relative to the long-run average — yet no NBER recession materialized. This episode highlights the known limitation that the yield curve generates false positives when inversions are driven by monetary policy regime shifts rather than deteriorating growth expectations.

Tools
Python · pandas · NumPy · scikit-learn · statsmodels · matplotlib · fredapi (FRED)
