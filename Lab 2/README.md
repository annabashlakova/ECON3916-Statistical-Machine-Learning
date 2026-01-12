# Lab 2: The Illusion of Growth & The Composition Effect

## Objective

To build a Python-based economic analysis pipeline that ingests live macroeconomic data from the Federal Reserve Economic Data (FRED) API to investigate wage stagnation in the United States and identify statistical biases that mask the true trajectory of worker compensation.

## Methodology

### 1. Data Acquisition
- **API Integration:** Connected to the FRED API using `fredapi` to fetch real-time economic series
- **Primary Data Sources:**
  - `AHETPI`: Average Hourly Earnings of Production Workers (Nominal Wages)
  - `CPIAUCSL`: Consumer Price Index for All Urban Consumers (Inflation)
  - `ECIWAG`: Employment Cost Index for Total Compensation (Composition-Adjusted Wages)

### 2. Real Wage Calculation
- Deflated nominal wages using CPI to compute real purchasing power:
  ```
  Real Wage = (Nominal Wage / CPI) × 100
  ```
- Visualized the divergence between nominal and real wages from 1964-present to demonstrate the **Money Illusion**—the tendency to think in nominal rather than real terms.

### 3. Anomaly Detection & Correction
- **Identified the 2020 Pandemic Spike:** Detected an artificial surge in average wages during COVID-19 that contradicted labor market fundamentals.
- **Root Cause Analysis:** Recognized the **Composition Effect**—low-wage workers (retail, hospitality) disproportionately left the workforce, mechanically raising the average without actual wage growth.
- **Statistical Correction:** Compared standard wage data against the Employment Cost Index (ECI), which holds workforce composition constant, to isolate the true wage signal from compositional noise.

### 4. Visualization
- Created dual-axis time series plots comparing:
  - Biased standard average wages (showing artificial 2020 spike)
  - Composition-adjusted ECI wages (showing stable growth)
- Rebased both series to 2015=100 for direct comparison

## Key Findings

### The Money Illusion (1964-Present)
Real wages have remained nearly **flat for five decades** despite rising nominal paychecks. Workers today have approximately the same purchasing power as their counterparts in the 1970s, revealing that wage growth has merely kept pace with inflation rather than reflecting productivity gains.

### The Pandemic Paradox (2020)
The apparent 2020 "wage boom" was a **statistical mirage**:
- **Standard metrics** showed wages spiking 8-10% during the pandemic
- **Composition-adjusted ECI** revealed stable, modest growth of 3-4%
- **The divergence** demonstrates that the spike was driven entirely by workforce composition changes (low-wage job losses) rather than increased labor demand or bargaining power

This finding underscores the critical importance of using composition-adjusted metrics when analyzing labor market dynamics during periods of structural employment shifts.

---

**Technical Skills Demonstrated:** API integration, time series analysis, statistical bias correction, economic data visualization, Python (`pandas`, `matplotlib`, `fredapi`)
