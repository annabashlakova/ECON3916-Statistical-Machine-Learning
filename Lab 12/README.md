# Architecting the Prediction Engine: Multivariate OLS Real Estate Valuation Model

## Objective
Engineer a multivariate OLS prediction engine on cross-sectional real estate market data to forecast property valuations and quantify out-of-sample predictive loss in interpretable financial terms.

---

## Data
**Zillow Home Value Index (ZHVI) — 2026 Micro Dataset**
Cross-sectional U.S. real estate market data capturing current property valuations across geographic and structural dimensions.

---

## Methodology
- **Feature Engineering & Formula API** — Constructed the multivariate design matrix using `statsmodels`' Patsy Formula API, enabling expressive, R-style model specification directly in Python
- **OLS Estimation** — Fitted a multivariate Ordinary Least Squares regression via `statsmodels.formula.api`, extracting coefficients, standard errors, and model diagnostics from the results object
- **Predictive vs. Explanatory Framing** — Deliberately reoriented the modeling objective from classical inference (coefficient interpretation) to predictive engineering (minimizing out-of-sample loss)
- **Loss Quantification** — Computed Root Mean Squared Error (RMSE) denominated in **actual U.S. dollars**, translating abstract statistical loss into a direct, business-interpretable financial error margin
- **Residual Forensics** — Built an interactive residual diagnostic dashboard using Plotly, plotting fitted values against residuals with ±2σ outlier flagging to detect heteroscedasticity and structural breaks

---

## Key Findings
The fitted OLS engine produced an RMSE expressed in dollar terms, establishing a concrete upper bound on the model's average prediction error per property — a metric directly actionable for underwriting risk, portfolio valuation, and algorithmic pricing decisions. The residual forensics dashboard confirmed model behavior across the fitted value distribution, identifying the proportion of observations exceeding the 2σ threshold and surfacing any systematic variance patterns warranting further specification work.

---

## Stack
| Tool | Role |
|---|---|
| `pandas` | Data ingestion and feature construction |
| `numpy` | Numerical operations and loss computation |
| `statsmodels` (Patsy API) | OLS estimation and results extraction |
| `plotly` | Interactive residual forensics dashboard |

---

## Skills Demonstrated
`Predictive Modeling` · `OLS Regression` · `Loss Function Engineering` · `Residual Diagnostics` · `Financial Error Quantification` · `Applied Econometrics`
