# Lab 3: Visualizing Development with WBGAPI

## Objective
To construct a Python-based development economics pipeline that ingests macroeconomic indicators from the World Bank API to analyze Ukraine's economic trajectory from 2000-2023, benchmark its performance against global comparators, and visualize structural patterns across growth, labor markets, trade, and fiscal policy.

## Methodology

### 1. Data Acquisition
* **API Integration**: Connected to World Bank Global Database using `wbgapi` to fetch international development indicators
* **Primary Data Sources**: Real GDP, GDP per capita, unemployment, labor force, inflation (CPI), savings, investment, exports, imports, tax revenue, government expenditure
* **Comparative Framework**: Benchmarked Ukraine (UKR) against Upper Middle Income countries (UMC) and World Average (WLD) for 2000-2024

### 2. Data Engineering
* Transposed raw API data into panel format with multi-level DataFrames (country-indicator hierarchies)
* Standardized time index from World Bank year codes to integers for time series analysis
* Extracted Ukraine-specific subset for derived calculations

### 3. Derived Economic Indicators
* **Natural Rate of Unemployment**: 5-year rolling average to identify structural baseline
* **Labor Productivity**: GDP per worker (GDP / Labor Force)
* **Net Capital Outflow (NCO)**: Trade balance (Exports - Imports)
* **Budget Balance**: Fiscal position (Tax Revenue - Government Expenditure)

### 4. Visualization
* Single-metric time series for benchmarking and trend analysis
* **Executive Dashboard**: 2x3 dark-themed grid with Real GDP (line), Inflation (bar), Unemployment (line), Fiscal Balance (filled area), Trade Balance (filled area), and Savings vs Investment (dual lines)
* Color-coded surplus/deficit regions for fiscal and trade analyses

## Key Findings

### The Development Lag
Ukraine's GDP per capita grew 150% from ~$1,800 to ~$4,500 (2000-2023) but consistently underperformed both Upper Middle Income peers and global averages, indicating **relative divergence**. The 2014-2015 contraction (Crimea annexation) and 2022 collapse (Russian invasion) revealed extreme geopolitical vulnerability.

### Structural Imbalances
* **Labor Markets**: Natural unemployment rate stabilized at 7-9%, indicating persistent matching frictions. Labor productivity grew modestly, suggesting capital-driven rather than efficiency-driven growth.
* **Monetary Instability**: Severe inflation volatility with hyperinflationary spikes exceeding 20% (2001, 2008, 2015), reflecting weak central bank independence and currency instability.
* **Savings-Investment Gap**: Chronic deficit where investment (20-25% GDP) exceeded domestic savings (15-20% GDP), indicating **foreign capital dependence** and vulnerability to sudden stops.
* **Trade Deficit**: Persistent net imports of 5-10% GDP throughout 2000-2023, driven by energy dependence and weak export competitiveness.
* **Fiscal Fragility**: Budget balance oscillated between small surpluses and deficits, with severe stress during crises. Tax revenue volatility (25-30% GDP) reflected informal economy challenges.

## Technical Skills Demonstrated
API integration (`wbgapi`), multi-level pandas DataFrames, time series transformations, rolling window calculations, derived macroeconomic indicators, comparative benchmarking, multi-panel visualization (`matplotlib`, `seaborn`).
