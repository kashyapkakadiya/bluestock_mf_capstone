# Data Dictionary

## Project
Mutual Fund Analytics Platform – Capstone Project I

## Purpose

This document defines all datasets, columns, data types, business meanings, and source references used in the Mutual Fund Analytics Platform.

---

# 1. Fund Master Dataset

**Source File:** `01_fund_master.csv`

| Column Name | Data Type | Business Definition |
|------------|------------|------------|
| amfi_code | Integer | Unique AMFI scheme identifier |
| fund_house | Text | Mutual fund company name |
| scheme_name | Text | Name of mutual fund scheme |
| category | Text | Primary fund category (Equity, Debt, etc.) |
| sub_category | Text | Detailed scheme classification |
| plan | Text | Regular or Direct plan |
| launch_date | Date | Scheme launch date |
| benchmark | Text | Benchmark index used for comparison |
| expense_ratio_pct | Decimal | Annual expense ratio percentage |
| exit_load_pct | Decimal | Exit load charged on redemption |
| min_sip_amount | Decimal | Minimum SIP investment amount |
| min_lumpsum_amount | Decimal | Minimum lump sum investment amount |
| fund_manager | Text | Scheme fund manager |
| risk_category | Text | Scheme risk classification |
| sebi_category_code | Text | SEBI category identifier |

---

# 2. NAV History Dataset

**Source File:** `02_nav_history.csv`

| Column Name | Data Type | Business Definition |
|------------|------------|------------|
| amfi_code | Integer | AMFI scheme code |
| date | Date | NAV observation date |
| nav | Decimal | Net Asset Value per unit |

---

# 3. AUM by Fund House Dataset

**Source File:** `03_aum_by_fund_house.csv`

| Column Name | Data Type | Business Definition |
|------------|------------|------------|
| date | Date | Reporting date |
| fund_house | Text | Mutual fund company |
| aum_lakh_crore | Decimal | Assets Under Management in lakh crore |
| aum_crore | Decimal | Assets Under Management in crore |
| num_schemes | Integer | Number of active schemes |

---

# 4. Monthly SIP Inflows Dataset

**Source File:** `04_monthly_sip_inflows.csv`

| Column Name | Data Type | Business Definition |
|------------|------------|------------|
| month | Date | Reporting month |
| sip_inflow_crore | Decimal | Monthly SIP inflow amount |
| active_sip_accounts_crore | Decimal | Active SIP accounts |
| new_sip_accounts_lakh | Decimal | Newly registered SIP accounts |
| sip_aum_lakh_crore | Decimal | SIP Assets Under Management |
| yoy_growth_pct | Decimal | Year-over-year growth percentage |

---

# 5. Category Inflows Dataset

**Source File:** `05_category_inflows.csv`

| Column Name | Data Type | Business Definition |
|------------|------------|------------|
| month | Date | Reporting month |
| category | Text | Mutual fund category |
| net_inflow_crore | Decimal | Net capital inflow for category |

---

# 6. Industry Folio Count Dataset

**Source File:** `06_industry_folio_count.csv`

| Column Name | Data Type | Business Definition |
|------------|------------|------------|
| month | Date | Reporting month |
| total_folios_crore | Decimal | Total industry folios |
| equity_folios_crore | Decimal | Equity fund folios |
| debt_folios_crore | Decimal | Debt fund folios |
| hybrid_folios_crore | Decimal | Hybrid fund folios |
| others_folios_crore | Decimal | Other category folios |

---

# 7. Scheme Performance Dataset

**Source File:** `07_scheme_performance.csv`

| Column Name | Data Type | Business Definition |
|------------|------------|------------|
| amfi_code | Integer | AMFI scheme identifier |
| scheme_name | Text | Scheme name |
| fund_house | Text | Fund house name |
| category | Text | Scheme category |
| plan | Text | Direct or Regular plan |
| return_1yr_pct | Decimal | One-year annualized return |
| return_3yr_pct | Decimal | Three-year annualized return |
| return_5yr_pct | Decimal | Five-year annualized return |
| benchmark_3yr_pct | Decimal | Benchmark three-year return |
| alpha | Decimal | Risk-adjusted excess return |
| beta | Decimal | Market sensitivity measure |
| sharpe_ratio | Decimal | Risk-adjusted return metric |
| sortino_ratio | Decimal | Downside-risk-adjusted return metric |
| std_dev_ann_pct | Decimal | Annualized volatility |
| max_drawdown_pct | Decimal | Maximum portfolio decline |
| aum_crore | Decimal | Assets Under Management |
| expense_ratio_pct | Decimal | Annual expense ratio |
| morningstar_rating | Integer | Morningstar rating score |
| risk_grade | Text | Scheme risk grade |

---

# 8. Investor Transactions Dataset

**Source File:** `08_investor_transactions.csv`

| Column Name | Data Type | Business Definition |
|------------|------------|------------|
| investor_id | Text | Unique investor identifier |
| transaction_date | Date | Transaction date |
| amfi_code | Integer | Scheme code |
| transaction_type | Text | SIP, Lumpsum, or Redemption |
| amount_inr | Decimal | Transaction amount in INR |
| state | Text | Investor state |
| city | Text | Investor city |
| city_tier | Text | Tier classification of city |
| age_group | Text | Investor age segment |
| gender | Text | Investor gender |
| annual_income_lakh | Decimal | Annual income in lakhs |
| payment_mode | Text | Mode of payment |
| kyc_status | Text | KYC verification status |

---

# 9. Portfolio Holdings Dataset

**Source File:** `09_portfolio_holdings.csv`

| Column Name | Data Type | Business Definition |
|------------|------------|------------|
| amfi_code | Integer | Scheme code |
| stock_symbol | Text | Listed stock ticker |
| stock_name | Text | Company name |
| sector | Text | Industry sector |
| weight_pct | Decimal | Portfolio weight percentage |
| market_value_cr | Decimal | Market value in crore |
| current_price_inr | Decimal | Current stock price |
| portfolio_date | Date | Portfolio reporting date |

---

# 10. Benchmark Indices Dataset

**Source File:** `10_benchmark_indices.csv`

| Column Name | Data Type | Business Definition |
|------------|------------|------------|
| date | Date | Trading date |
| index_name | Text | Benchmark index name |
| close_value | Decimal | Closing index value |

---

# Data Quality Notes

## Day 2 Cleaning Summary

- Converted all date fields to datetime format.
- Removed duplicate records from applicable datasets.
- Validated NAV values are greater than zero.
- Standardized transaction types to SIP, Lumpsum, and Redemption.
- Validated transaction amounts are positive.
- Validated scheme performance return fields as numeric.
- Verified expense ratios fall within the expected range of 0.1% to 2.5%.
- Preserved valid business null values in `yoy_growth_pct`.
- Loaded all cleaned datasets into SQLite successfully.

---

# Database Objects

## Dimension Tables

- dim_fund
- dim_date

## Fact Tables

- fact_nav
- fact_transactions
- fact_performance
- fact_aum

---

# Version

Version: 1.0

Created For: Bluestock Internship – Mutual Fund Analytics Platform

Phase: Day 2