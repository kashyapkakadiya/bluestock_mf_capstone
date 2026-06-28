# Day 4 – Performance Analytics Summary

## Objective

Implemented advanced mutual fund performance analytics using daily NAV data to evaluate returns, risk-adjusted performance, downside risk, benchmark comparison, and composite fund rankings.

## Work Completed

### Performance Metrics

- Computed daily returns for all 40 mutual fund schemes.
- Validated daily return distribution using descriptive statistics and histogram.
- Calculated Compound Annual Growth Rate (CAGR) for 1-year, 3-year, and 5-year periods.
- Calculated Sharpe Ratio using a 6.5% annual risk-free rate.
- Calculated Sortino Ratio using downside volatility.
- Calculated Alpha and Beta for each fund using linear regression against the Nifty 100 benchmark.
- Calculated Maximum Drawdown and identified peak-to-trough declines.
- Calculated Tracking Error against the benchmark.

### Fund Evaluation

Developed a composite Fund Scorecard (0–100) using:

- 30% – 3-Year CAGR
- 25% – Sharpe Ratio
- 20% – Alpha
- 15% – Expense Ratio (inverse ranking)
- 10% – Maximum Drawdown (inverse ranking)

### Benchmark Comparison

Compared the Top 5 ranked mutual funds with Nifty 50 and Nifty 100 over the analysis period and exported the comparison chart.

## Deliverables

- Performance_Analytics.ipynb
- outputs/csv/nav_with_returns.csv
- outputs/csv/cagr_table.csv
- outputs/csv/max_drawdown.csv
- outputs/csv/sharpe_ratio.csv
- outputs/csv/sortino_ratio.csv
- outputs/csv/alpha_beta.csv
- outputs/csv/fund_scorecard.csv
- outputs/charts/sharpe_sortino_comparison.png
- outputs/charts/benchmark_comparison.png

## Outcome

Successfully implemented quantitative performance analytics that evaluate mutual fund growth, volatility, downside risk, benchmark sensitivity, and overall performance ranking. These outputs provide a strong analytical foundation for the dashboard and reporting phase.