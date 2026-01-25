# The Cost of Living Crisis: A Data-Driven Analysis

## The Problem

The official Consumer Price Index (CPI) tells us inflation is cooling. But for students, the reality feels very different.

Why? Because the CPI measures an "average" consumer who doesn't exist. It weights housing at ~34% of spending. But for a typical college student, tuition and rent alone can consume 70% or more of their budget. The CPI tracks used cars and hospital services—categories most students rarely touch—while underweighting the costs that define student life: tuition, rent, food delivery, and streaming services.

This project asks a simple question: **What if we built an inflation index that actually reflects how students spend money?**

## Methodology

### Data Collection
I used Python and the `fredapi` library to pull real-time economic data from the Federal Reserve Economic Data (FRED) database. Since FRED doesn't track "Chipotle" or "Spotify" directly, I identified official proxy series:

| Student Expense | FRED Proxy Series |
|----------------|-------------------|
| Tuition | CUSR0000SEEB (Tuition, Fees & Childcare) |
| Rent | CUSR0000SEHA (Rent of Primary Residence) |
| Chipotle | CUSR0000SEFV (Food Away From Home) |
| Spotify | CUSR0000SERA02 (Cable & Streaming) |
| Benchmark | CPIAUCSL (Official CPI) |

### Normalization
FRED series have different base years (some indexed to 1982, others to 2002), making raw comparisons meaningless. I re-indexed all series to January 2016 = 100 using the formula:
```
Value_Index = (Value_Current / Value_at_Start_Date) × 100
```

### Weighted Index Construction (Laspeyres Method)
The official CPI uses a Laspeyres price index—a weighted average where the weights reflect a fixed "basket" of goods. I applied the same methodology but with weights that reflect actual student spending:

| Category | Student Weight | CPI Weight |
|----------|---------------|------------|
| Tuition | 40% | ~6% |
| Rent | 30% | ~34% |
| Food Away | 20% | ~6% |
| Streaming | 10% | <1% |

The resulting **Student Price Index (SPI)** captures inflation as students actually experience it.

### Regional Analysis
I extended the analysis by incorporating the Boston-Cambridge-Newton CPI (CUURA103SA0) to examine regional disparities relevant to Northeastern students.

## Key Findings

My analysis reveals a **significant divergence** between student costs and national inflation from 2016-2024:

1. **The Inflation Gap is Real**: The Student SPI consistently outpaces the official CPI, confirming that students face higher effective inflation than the national average suggests.

2. **Tuition is the Driver**: Education costs have risen faster than any other category in the student basket, validating concerns about the college affordability crisis.

3. **Regional Amplification**: The Boston CPI tracks above the national average, meaning students at Northeastern face a "double penalty"—both student-specific and regional inflation premiums.

4. **The Scale Fallacy**: Visualizing raw (non-normalized) data demonstrates why proper indexing methodology matters. Without normalization, tuition appears to dwarf streaming costs on a chart—not because of faster growth, but because of arbitrary base year differences.

## Tools & Technologies

- **Python 3** — Core programming language
- **pandas** — Data manipulation and analysis
- **matplotlib** — Data visualization
- **fredapi** — Federal Reserve Economic Data API wrapper
- **Google Colab** — Development environment

## Visualizations

The project includes three key charts:

1. **Normalized Components Chart** — All five series (CPI, Tuition, Rent, Streaming, Food Away) plotted together to show relative growth since 2016

2. **Student SPI vs Official CPI** — Direct comparison with shaded "Inflation Gap" highlighting the divergence

3. **The Scale Fallacy** — Raw data visualization demonstrating why normalization is essential for honest analysis

4. **Regional Comparison** — National CPI vs Boston CPI vs Student SPI

## Conclusion

The "average" consumer is a statistical fiction. By constructing a custom price index weighted to actual student expenditures, this analysis reveals that **students experience inflation at a rate meaningfully higher than official statistics suggest**. This has real implications for financial aid policy, student loan calculations, and university budgeting.
