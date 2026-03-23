# The Architecture of Dimensionality: Hedonic Pricing & the FWL Theorem

## Objective
Architect a multivariate hedonic pricing model on 2026 California real estate data to empirically prove the Frisch-Waugh-Lovell (FWL) theorem, demonstrating how algorithmic ceteris paribus isolates true causal signal by surgically removing confounding covariance from the coefficient estimation process.

---

## Data
**2026 California Real Estate Metrics — Zillow Synthetic Dataset**
Cross-sectional property-level data capturing `Sale_Price`, `Property_Age`, and `Distance_to_Tech_Hub` across the California market, designed to surface omitted variable dynamics present in real hedonic pricing environments.

---

## Methodology
- **Baseline Univariate OLS** — Regressed `Sale_Price` on `Property_Age` alone using `statsmodels.formula.api` to establish the naïve, confounded coefficient — the benchmark against which OVB contamination is measured
- **Multivariate OLS (Full Model)** — Extended the specification to include `Distance_to_Tech_Hub` as a second regressor, allowing the estimator to simultaneously partial out the variance attributable to tech hub proximity
- **Manual FWL Implementation (Stage 1)** — Regressed `Property_Age` on `Distance_to_Tech_Hub` and extracted the residuals, isolating the component of property age that is orthogonal to — i.e., linearly independent of — proximity to the tech hub
- **Manual FWL Implementation (Stage 2)** — Regressed `Sale_Price` on `Distance_to_Tech_Hub` and extracted the residuals, stripping the target variable of the same confounding dimension
- **FWL Verification** — Regressed the Stage 2 residuals on the Stage 1 residuals and confirmed an exact numerical match to the `Property_Age` coefficient from the full multivariate model, proving the theorem computationally
- **OVB Quantification** — Computed the coefficient delta between the univariate and multivariate specifications to measure the precise magnitude of omitted variable bias introduced by excluding tech hub proximity

---

## Key Findings
The univariate model produced a severely biased `Property_Age` coefficient, falsely attributing inflated valuation signal to the physical age of the property. The bias originated from the positive covariance between `Distance_to_Tech_Hub` and `Sale_Price` — a dimension the single-regressor model had no mechanism to absorb, forcing the estimator to load that unexplained variance onto the only available coefficient.

Introducing `Distance_to_Tech_Hub` into the multivariate specification allowed the OLS estimator to enforce algorithmic ceteris paribus: each coefficient was estimated holding the other regressor fixed, stripping the shared covariance from both partial slopes simultaneously.

The FWL proof closed the loop. By manually partialling out `Distance_to_Tech_Hub` from both `Property_Age` and `Sale_Price` and re-running the simple regression on the resulting residuals, the recovered coefficient matched the multivariate estimate to machine precision — confirming that multivariate OLS does not merely adjust for confounders statistically, but geometrically projects the regressors into orthogonal subspaces before estimation. The coefficient you read off a well-specified model is not a correlation. It is a projection.

---

## Stack
| Tool | Role |
|---|---|
| `pandas` | Data construction and feature management |
| `statsmodels.formula.api` | OLS estimation via Patsy formula interface |
| `matplotlib` | Coefficient comparison and residual visualization |

---

## Skills Demonstrated
`Hedonic Pricing Models` · `Omitted Variable Bias Diagnosis` · `Frisch-Waugh-Lovell Theorem` · `Multivariate OLS` · `Residual Partialling` · `Applied Econometrics` · `Causal Inference Fundamentals`
