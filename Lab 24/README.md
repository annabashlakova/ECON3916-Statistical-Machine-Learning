## Causal ML — Double Machine Learning for 401(k) Policy Evaluation

**Objective:** Apply Double Machine Learning (DML) to estimate the causal effect of 401(k) eligibility on household net financial assets, addressing regularization bias and treatment effect heterogeneity across income subgroups.

### Methodology

- Demonstrated regularization bias via simulation (TRUE_ATE = 5.0): showed that naïve LASSO shrinks the treatment coefficient toward zero, motivating orthogonal/debiased estimation
- Implemented a Partially Linear Regression (PLR) model using the `DoubleML` framework with Random Forest nuisance learners and 5-fold cross-fitting on 401(k) pension plan data (Abadie, 2003)
- Estimated the Average Treatment Effect (ATE) of 401(k) eligibility on net financial assets with robust inference
- Conducted sensitivity analysis (`cf_y=0.03`, `cf_d=0.03`) to assess robustness of the ATE to potential unmeasured confounders (e.g., financial literacy, risk tolerance)
- Performed Conditional Average Treatment Effect (CATE) analysis by income quartile to detect treatment effect heterogeneity
- Visualized CATE estimates with 95% confidence intervals across income subgroups

### Key Findings

- **ATE:** 401(k) eligibility increases net financial assets by approximately $[YOUR_ATE] (p < [YOUR_P_VALUE]), confirming a statistically significant positive causal effect
- **Robustness:** Sensitivity analysis returned a robustness value of ρ = [YOUR_RHO], indicating that [INTERPRETATION — e.g., "no single omitted confounder could plausibly explain away the estimated effect"]
- **Heterogeneity:** CATE analysis revealed [DESCRIBE PATTERN — e.g., "monotonically increasing treatment effects across income quartiles, with Q1 households gaining ~$X and Q4 households gaining ~$Y, suggesting that higher-income households capture disproportionately larger savings benefits from 401(k) eligibility"]

### Tools & Packages

Python · DoubleML · scikit-learn (RandomForestRegressor, RandomForestClassifier) · matplotlib · numpy · pandas
