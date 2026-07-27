# Stock Returns Project

## Hypothesis

A bullish moving average crossover signal
(MA30 > MA100) predicts higher future returns.

## Method

1. Downloaded AAPL data from 2020-2025.
2. Computed daily returns.
3. Computed MA30 and MA100.
4. Defined Signal = 1 when MA30 > MA100.
5. Compared future returns across signal states.
6. Performed Welch's two-sample t-test.

## Results

Bullish mean return < Bearish mean return.

T-statistic = -0.3167

P-value = 0.7516

## Conclusion

No statistically significant evidence that the moving-average signal predicts future returns for AAPL over the sample period.
Due to p-value = 0.7516 being significantly greater than the conventional threshold (alpha level = 0.05).

The observed difference is small relative to the variability of stock returns.
Due to the small magnitude of the t-statistic.

## Next Steps

1. Additional Stocks
2. Alternative Signals
3. More Advanced Statistical Models

## First Addition: Multi-Stock Analysis

### Objective
Test whether the MA30 > MA100 moving average signal predicts future returns across multiple stocks.

### Methodology
- Analyzed 10 large-cap U.S. stocks from 2020–2025.
- Calculated daily returns, MA30, and MA100 indicators.
- Created bullish signals when MA30 > MA100.
- Compared next-day returns between bullish and bearish periods.
- Used Welch's two-sample t-test to evaluate statistical significance.

### Results
- No stocks produced statistically significant results (all p-values > 0.05).
- META had the strongest result (p = 0.169), but it was not statistically significant.
- Bullish periods outperformed bearish periods for some stocks, but results were inconsistent across companies.
- Most t-statistics were close to zero, suggesting differences were small relative to daily return volatility.

### Conclusion
- The MA30/MA100 crossover signal did not demonstrate reliable predictive power across the selected stocks.
- The results suggest the strategy's observed performance was likely due to normal market randomness rather than a consistent trading edge.
- Future improvements include backtesting strategy returns, analyzing risk-adjusted performance, and testing additional features.