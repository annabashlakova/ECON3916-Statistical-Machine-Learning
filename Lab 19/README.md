# Tree-Based Models — Random Forests

## Objective

Benchmark tree-based ensemble methods against linear baselines on the California Housing dataset, leveraging hyperparameter tuning, feature importance decomposition, and classification extensions to quantify where Random Forests deliver marginal predictive gains — and where they don't.

## Methodology

- Loaded the California Housing dataset (20,640 observations, 8 features) and established baseline performance with Ridge Regression and a single Decision Tree
- Trained a Random Forest regressor and conducted hyperparameter tuning via GridSearchCV over n_estimators, max_depth, and max_features to identify the optimal model configuration
- Extracted and compared Mean Decrease in Impurity (MDI) feature importance against permutation-based importance to assess robustness of variable rankings
- Extended the analysis to classification by constructing a Random Forest classifier and benchmarking ROC-AUC against a logistic regression baseline
- Built an interactive dashboard using Plotly and ipywidgets to enable dynamic exploration of model outputs and feature contributions

## Key Findings

- **Ensemble advantage confirmed:** Random Forest outperformed both Ridge Regression and a standalone Decision Tree on held-out R², demonstrating the variance-reduction benefit of bagging over individual learners.
- **Hyperparameter sensitivity:** GridSearchCV revealed diminishing returns beyond a moderate number of estimators, with max_depth and max_features exerting stronger influence on generalization than ensemble size alone.
- **Feature importance divergence:** MDI and permutation importance produced meaningfully different variable rankings — MDI inflated the contribution of high-cardinality features, while permutation importance offered a more reliable signal of true predictive relevance.
- **Classification parity:** The Random Forest classifier achieved competitive AUC relative to logistic regression, suggesting that for well-structured tabular data, ensemble complexity does not always translate into classification gains.

## Tech Stack

Python · scikit-learn · Plotly · ipywidgets · pandas · NumPy
