# Spurious Correlation & Multicollinearity in Macroeconomic Time-Series Data

## Project Overview

This project investigates a critical but frequently overlooked pitfall in applied econometrics: the danger of drawing causal or relational inferences from raw macroeconomic level data without first accounting for non-stationarity, multicollinearity, and structural relationships between variables. Using publicly available data retrieved via the **FRED API**, this analysis demonstrates how naïve correlation analysis on trending time series produces misleading results — and how principled data transformation and diagnostic tooling can correct for these distortions.

---

## Methodology

### 1. Data Collection & Exploration
Historical macroeconomic indicators — including CPI, Unemployment, the Federal Funds Rate, Industrial Production, and M2 Money Supply — were retrieved programmatically via the FRED API. Initial exploratory analysis using **Python** and **pandas** surfaced the raw level structure of each series, revealing the strong upward trends common to most macroeconomic aggregates over long time horizons.

### 2. Visualizing Correlation Traps
Pairwise correlation matrices were computed on the raw level data and visualized using **seaborn**. This step deliberately exposed the "correlation trap": non-stationary trending series produce artificially inflated Pearson correlation coefficients, creating the illusion of strong relationships between variables that may share no meaningful structural connection. This phenomenon — known as **spurious regression** (Granger & Newbold, 1974) — is a foundational concern in macroeconomic time-series analysis.

### 3. Multicollinearity Diagnostics via VIF
To quantify the degree of linear redundancy among predictors, **Variance Inflation Factor (VIF)** diagnostics were applied using **statsmodels**. Elevated VIF scores confirmed that raw-level macroeconomic variables carry substantial shared variance, rendering any regression model built on untransformed inputs statistically unreliable and difficult to interpret.

### 4. Stationarity Transformation: Year-over-Year Growth Rates
Each non-stationary level series was transformed into its **Year-over-Year (YoY) percentage change**, effectively removing the deterministic trend component and isolating cyclical co-movement. Correlation analysis was then repeated on the transformed series. The resulting reduction in pairwise correlations demonstrated that many previously "strong" relationships were attributable to shared trend rather than genuine economic linkage.

### 5. Causal Structure Mapping with DAGs
Finally, **Directed Acyclic Graphs (DAGs)** were constructed to represent the hypothesized structural relationships among the variables. By mapping the underlying causal architecture — including direct effects, mediated pathways, and confounders — this step contextualized which correlations reflect genuine economic mechanisms and which are artifacts of data structure. DAGs serve as a rigorous framework for distinguishing association from causation in observational macroeconomic data.

---

## Tools & Technologies

| Tool | Purpose |
|---|---|
| Python | Core analysis and scripting |
| FRED API | Macroeconomic data retrieval |
| pandas | Data manipulation and transformation |
| seaborn / matplotlib | Correlation heatmap visualization |
| statsmodels | VIF diagnostics and regression modeling |
| DAG framework | Causal structure mapping |

---

## Key Takeaways

- Raw macroeconomic levels are almost always non-stationary; correlation analysis on such series produces **spurious results** that should not be interpreted causally.
- **VIF diagnostics** provide a quantitative measure of multicollinearity that raw correlation matrices alone cannot fully capture.
- **YoY transformation** is a practical and widely accepted method for inducing approximate stationarity in macroeconomic data, though it introduces moving-average autocorrelation that may require further correction in formal inference.
- **DAGs** elevate the analysis beyond descriptive statistics by making structural economic assumptions explicit and testable.

---

*This project was completed as part of a data science portfolio focused on applied econometrics and macroeconomic analysis.*
