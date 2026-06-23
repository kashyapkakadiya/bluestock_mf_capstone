# Day 1 Data Quality Summary

## Project

Mutual Fund Analytics Platform – Capstone Project I

## Objective

The objective of Day 1 was to ingest all provided datasets, perform an initial data assessment, validate key relationships, and collect live NAV data from external mutual fund APIs for further analysis.

---

## Datasets Loaded

The following datasets were successfully loaded into Pandas:

| Dataset               | Records |
| --------------------- | ------: |
| Fund Master           |      40 |
| NAV History           |  46,000 |
| AUM by Fund House     |      90 |
| Monthly SIP Inflows   |      48 |
| Category Inflows      |     144 |
| Industry Folio Count  |      21 |
| Scheme Performance    |      40 |
| Investor Transactions |  32,778 |
| Portfolio Holdings    |     322 |
| Benchmark Indices     |   8,050 |

All datasets were successfully read without file corruption or loading errors.

---

## Fund Master Exploration

The Fund Master dataset was explored to understand the overall mutual fund universe available for analysis.

### Key Findings

* 10 unique fund houses were identified.
* 2 primary fund categories were present:

  * Equity
  * Debt
* 12 unique sub-categories were identified.
* 5 risk categories were observed:

  * Low
  * Moderate
  * Moderately High
  * High
  * Very High

---

## AMFI Scheme Code Understanding

AMFI (Association of Mutual Funds in India) assigns a unique numeric scheme code to every mutual fund scheme. These codes act as primary identifiers across mutual fund databases, transaction systems, and NAV APIs. The same scheme code is used when requesting NAV history through MFAPI endpoints.

Examples:

* 125497 – HDFC Top 100 Fund Direct Growth
* 119551 – SBI Bluechip Fund Direct Growth
* 120503 – ICICI Bluechip Fund Direct Growth

These codes serve as the primary key for joining scheme-related datasets throughout the project.

---

## AMFI Code Validation

Validation was performed to ensure every scheme available in the Fund Master dataset exists within the NAV History dataset.

### Validation Results

* Fund Master AMFI Codes: 40
* NAV History AMFI Codes: 40
* Missing Codes: 0

Result:

All AMFI scheme codes present in the Fund Master dataset were successfully found in the NAV History dataset.

This confirms referential consistency between the two core datasets.

---

## Data Quality Assessment

### Duplicate Records

No duplicate records were detected across the provided datasets.

### Missing Values

A small number of missing values were observed in the `yoy_growth_pct` column of the Monthly SIP Inflows dataset.

Observation:

* Missing values appear only in periods where year-over-year growth cannot be calculated due to the absence of historical comparison data.
* These are considered business-rule missing values rather than data quality issues.

### Data Types

Several date-related columns are currently stored as text and will require conversion during preprocessing:

* launch_date
* date
* month
* transaction_date
* portfolio_date

AMFI scheme codes are currently stored as numeric values and will be converted to string format during ETL processing to ensure consistency during joins and database loading.

### Range Validation

Basic validation checks were performed on numerical fields:

* No negative Sharpe ratios detected.
* Expense ratios fall within expected ranges.
* Transaction and benchmark datasets contain realistic values.

---

## Live NAV Data Collection

Live NAV data was successfully retrieved from MFAPI for the following schemes:

* HDFC Top 100 Fund (125497)
* SBI Bluechip Fund (119551)
* ICICI Bluechip Fund (120503)
* Nippon India Large Cap Fund (118632)
* Axis Bluechip Fund (119092)
* Kotak Bluechip Fund (120841)

JSON responses were parsed and saved as raw CSV files for future analysis. MFAPI provides NAV history through the endpoint `/mf/{scheme_code}` without requiring authentication.

---

## Conclusion

All Day 1 objectives were successfully completed.

The datasets are internally consistent, AMFI code validation passed successfully, and no critical data quality issues were identified. The data is suitable for downstream ETL processing, PostgreSQL integration, exploratory data analysis, and dashboard development in subsequent project phases.
