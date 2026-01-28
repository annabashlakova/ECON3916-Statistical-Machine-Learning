## Descriptive Statistics & Anomaly Detection

**Objective:** To apply statistical and machine learning techniques for identifying anomalous observations in housing market data, comparing traditional IQR-based outlier detection with multivariate Isolation Forest methods.

**Methodology:**
- Ingested the California Housing dataset and examined the distribution of median house values, identifying a censoring effect at the $500k threshold
- Implemented manual IQR-based outlier detection using Tukey Fences to flag extreme values in median income
- Deployed Isolation Forest, an unsupervised machine learning algorithm, to detect multivariate anomalies across income, house age, room count, and population features
- Calculated comparative descriptive statistics (mean, median, standard deviation, MAD) for normal versus outlier subgroups to quantify distributional differences

**Key Findings:** Isolation Forest flagged approximately 5% of observations as anomalous, capturing high-income districts exhibiting atypical combinations of features. The outlier subgroup displayed a pronounced "inequality wedge"—a positive gap between mean and median—indicating right-skewed distributions where extreme values pull the mean above the median. This Pareto-like pattern reflects the concentration of wealth in tail observations, demonstrating how standard measures of central tendency can misrepresent heterogeneous markets.

**Analytical Significance:** Anomaly detection is foundational to data quality assurance and exploratory analysis in finance and economics. Identifying outliers prevents skewed model estimates and reveals structural heterogeneity within datasets. In real estate analytics, isolating luxury or distressed markets from core inventory enables more accurate valuation models. The comparison between IQR and Isolation Forest illustrates the trade-off between interpretable univariate rules and flexible multivariate algorithms capable of detecting complex, non-linear anomaly patterns.

**Technical Skills:** Python, Pandas, Scikit-learn (Isolation Forest), Seaborn, Matplotlib, descriptive statistics (mean, median, standard deviation, MAD), IQR-based outlier detection, unsupervised machine learning, data visualization, boolean masking, custom function design
