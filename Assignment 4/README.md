# OmniCare Clinical Cost Prediction Engine: Multivariate OLS with Causal Forensics

## Objective
Engineer a validated multivariate OLS prediction engine on clinical and telemetry data to forecast hospital procedure costs, diagnose structural data pathologies, and quantify predictive loss in interpretable financial terms.

---

## Data
**OmniCare Hospital Network — Clinical & Telemetry Dataset**
Cross-sectional patient records capturing physiological vitals, remote wearable telemetry, insurance classifications, clinic capacity metrics, and historical procedure costs across 5,000 observations.

---

## Methodology
- **Causal Forensics & DAG Construction** — Identified socioeconomic status as an omitted confounder producing a spurious insurance-admission correlation; modeled the Fork structure using a Directed Acyclic Graph
- **Multicollinearity Audit** — Computed Variance Inflation Factors across all physiological predictors using `statsmodels`, dropping `Weight_kg` (VIF = 57.4) to restore structural stability below the critical threshold of 10
- **Missingness Classification** — Generated a missingness matrix via `missingno` and classified `Continuous_Heart_Rate` gaps as MNAR under Rubin's taxonomy, ruling out mean imputation on structural grounds
- **High-Cardinality Encoding** — Applied `category_encoders.TargetEncoder` to collapse 850 distinct ICD-10 diagnosis codes into a single continuous feature mapped to historical mean procedure cost
- **OLS Estimation** — Fitted a multivariate OLS model via `statsmodels.formula.api` Patsy Formula API, extracting coefficients, standard errors, and full model diagnostics
- **Loss Quantification** — Computed RMSE denominated in actual U.S. dollars, translating abstract statistical loss into a direct, business-interpretable financial error margin
- **Heteroscedasticity Testing** — Executed White's Lagrange Multiplier Test via `statsmodels.stats.diagnostic.het_white`, formally rejecting the null hypothesis of homoscedasticity

---

## Key Findings
The fitted OLS engine produced an RMSE of **$334.79**, establishing a concrete bound on average prediction error per procedure — directly actionable for hospital pricing decisions and regulatory risk assessment. White's LM Test returned a p-value of 0.0000, mathematically confirming non-constant variance across the fitted value distribution and flagging the model as unreliable at high-cost surge-pricing tiers.

---

## Stack
| Tool | Role |
|---|---|
| `pandas` | Data ingestion and feature construction |
| `numpy` | Numerical operations |
| `statsmodels` | OLS estimation, VIF computation, LM testing |
| `missingno` | Missingness visualization |
| `category_encoders` | Target encoding for high-cardinality features |
| `seaborn` / `matplotlib` | Residual diagnostic visualization |

---

## Skills Demonstrated
`Causal Inference` · `DAG Construction` · `Multicollinearity Diagnostics` · `Missing Data Classification` · `High-Cardinality Encoding` · `OLS Regression` · `Loss Function Engineering` · `Heteroscedasticity Testing` · `Applied Econometrics`
