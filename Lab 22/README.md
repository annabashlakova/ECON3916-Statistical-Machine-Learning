# Clustering World Economies with K-Means & PCA

## Objective

Apply unsupervised machine learning to classify ~160 national economies using World Bank development indicators, then benchmark algorithmic cluster assignments against official income-group classifications.

## Dataset

- **Source:** World Bank Development Indicators via `wbgapi`
- **Scope:** ~160 countries, 10 macroeconomic and human-development indicators
- **Secondary dataset:** California Housing census tract data (scikit-learn)

## Methodology

- Retrieved 10 development indicators (e.g., GDP per capita, life expectancy, access to electricity) programmatically using `wbgapi`
- Standardized all features with `StandardScaler` to neutralize scale effects prior to distance-based clustering
- Fit K-Means clustering with K = 4 and projected results onto two principal components via PCA for visualization
- Evaluated cluster quality across K = 2–10 using the elbow method (inertia) and silhouette analysis
- Cross-tabulated algorithmic clusters against World Bank income classifications (Low / Lower-Middle / Upper-Middle / High) to assess alignment
- Replicated the full pipeline on California Housing census tract data to test generalizability

## Key Findings

- **Optimal K:** [FILL IN — e.g., "Silhouette analysis identified K = ___ as optimal, consistent with the elbow plot inflection point."]
- **Income-Group Alignment:** [FILL IN — e.g., "K = 4 clusters exhibited strong correspondence with World Bank income tiers; ___% of High-income countries were isolated in a single cluster."]
- **PCA Visualization:** [FILL IN — e.g., "The first two principal components captured ___% of total variance, producing well-separated clusters in 2D space."]
- **California Housing:** [FILL IN — e.g., "Applied to census tracts, K-Means identified ___ distinct housing submarkets differentiated primarily by median income and proximity to the coast."]

## Tools & Libraries

`Python` · `wbgapi` · `pandas` · `scikit-learn` · `matplotlib` · `seaborn`
