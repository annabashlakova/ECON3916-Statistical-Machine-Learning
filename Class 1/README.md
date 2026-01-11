## Global Purchasing Power Parity Analysis via the Big Mac Index

## Objective: 
To test the Law of One Price using The Economist's Big Mac Index as a proxy for purchasing power parity across international markets.

## Methodology:
- Ingested raw pricing data from The Economist's 2015 Big Mac Index into a structured dataset
- Calculated implied PPP exchange rates for each currency against the US dollar
- Computed currency misalignment as the percentage deviation between implied PPP and actual market exchange rates

## Key Findings:
The Norwegian Krone exhibited the highest overvaluation at +31.5%, followed by the Brazilian Real at +8.8%.  The Russian Ruble showed the most severe undervaluation at -71.6%, with the South African Rand (-53.7%), Indonesian Rupiah (-53.2%), and Egyptian Pound (-52.0%) also showing significant undervaluation. The Chinese Yuan was found to be undervalued by 42.2%. These deviations highlight persistent arbitrage gaps and the practical limitations of the Law of One Price due to trade barriers, non-tradable inputs, and market segmentation.

## Economic Significance: 
For multinational corporations, PPP deviations signal cost advantages in sourcing, production location, and pricing strategy. Investors leverage these insights to identify undervalued markets and hedge currency exposure. While the Big Mac Index is a simplified model, it provides an accessible framework for understanding how purchasing power disparities shape global trade flows and capital allocation

---

**Tools Used**: Python, Pandas 
** Data Source**: The Economist (2015)
