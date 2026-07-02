# Day 6 – Advanced Analytics Report

## Project
Bluestock Mutual Fund Analytics Capstone

## Objective
The objective of Day 6 was to perform advanced risk, investor behavior, and portfolio analytics using the cleaned mutual fund datasets. The analysis focused on measuring downside risk, evaluating risk-adjusted performance, studying investor investment patterns, assessing SIP continuity, building a simple fund recommendation system, and measuring portfolio concentration.

---

## Tasks Completed

### 1. Historical VaR & CVaR Analysis
- Computed daily returns for all 40 mutual fund schemes using historical NAV data.
- Calculated Historical Value at Risk (VaR) at the 95% confidence level using the 5th percentile of daily returns.
- Calculated Conditional Value at Risk (CVaR) as the average of returns below the VaR threshold.
- Generated the report:
  - `reports/var_cvar_report.csv`

---

### 2. Rolling 90-Day Sharpe Ratio
- Calculated rolling 90-day Sharpe Ratios using a 6.5% annual risk-free rate.
- Generated rolling performance trends for five representative mutual fund schemes.
- Exported visualization:
  - `reports/rolling_sharpe_chart.png`

---

### 3. Investor Cohort Analysis
- Grouped investors based on the year of their first investment.
- Computed:
  - Average SIP amount
  - Total invested amount
  - Most preferred mutual fund for each cohort
- Identified investment trends across different investor cohorts.

---

### 4. SIP Continuity Analysis
- Analyzed investors with six or more SIP transactions.
- Calculated the average interval between consecutive SIP investments.
- Classified investors as:
  - Healthy (Average gap ≤ 35 days)
  - At-Risk (Average gap > 35 days)
- Estimated overall SIP continuity rate.

---

### 5. Mutual Fund Recommendation System
- Developed a command-line recommendation engine.
- Accepted user input based on risk appetite:
  - Low
  - Moderate
  - High
- Recommended the top three funds ranked by Sharpe Ratio within the selected risk category.
- Generated:
  - `scripts/recommender.py`

---

### 6. Sector Concentration Analysis
- Computed the Herfindahl-Hirschman Index (HHI) for each equity fund.
- Compared portfolio diversification across schemes.
- Identified highly concentrated and well-diversified portfolios.

---

### 7. Advanced Insights
Documented key findings including:
- Funds with the highest downside risk (VaR & CVaR).
- Trends in rolling risk-adjusted performance.
- Investor cohort investment behavior.
- SIP continuity and at-risk investor identification.
- Portfolio diversification based on HHI.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

---

## Deliverables

- ✅ Advanced_Analytics.ipynb
- ✅ var_cvar_report.csv
- ✅ rolling_sharpe_chart.png
- ✅ recommender.py

---

## Outcome

Successfully completed all advanced analytics tasks by implementing quantitative risk metrics, investor behavior analysis, portfolio concentration analysis, and a rule-based mutual fund recommendation system. These analyses provide deeper insights into fund performance, investor engagement, and portfolio risk, complementing the EDA, SQL, and Power BI components developed in earlier phases of the project.