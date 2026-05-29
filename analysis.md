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