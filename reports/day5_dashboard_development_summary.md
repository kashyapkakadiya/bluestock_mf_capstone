# Day 5 Report – Interactive Power BI Dashboard Development

**Project:** Bluestock Mutual Fund Capstone  

---

# Objective

The objective of Day 5 was to develop a fully interactive Business Intelligence dashboard using Microsoft Power BI. The dashboard integrates multiple mutual fund datasets to provide comprehensive insights into industry growth, fund performance, investor behavior, SIP trends, and benchmark comparisons. Interactive features such as slicers, drill-through navigation, KPI cards, and cross-filtering were implemented to enhance user experience and support data-driven decision-making. Power BI drill-through functionality was implemented following Microsoft's recommended summary-to-detail navigation approach. :contentReference[oaicite:0]{index=0}

---

# Work Completed

## 1. Data Integration

Imported all cleaned datasets into Power BI Desktop and verified the data model.

Tables Loaded:

- FundMaster
- NAV
- AUM
- SIP
- CategoryInflows
- Folios
- Transactions
- Benchmark
- Holdings
- Performance
- FundScorecard
- AlphaBeta

Relationships were established primarily using:

- **amfi_code**
- **date**

A dedicated **Measures** table was created to store reusable DAX measures.

---

## 2. DAX Measures Created

Developed reusable measures for dashboard KPIs including:

- Total AUM
- Latest AUM
- Latest SIP Inflow
- Latest Folios
- Total Schemes
- Total Fund Houses
- Latest NIFTY 50
- Latest NIFTY 100
- Total Investment Amount
- Additional analytical measures used across dashboard pages

---

# Dashboard Development

## Page 1 – Industry Overview

Developed an executive summary dashboard containing:

### KPI Cards

- Industry AUM (₹ Lakh Crore)
- Monthly SIP Inflow (₹ Crore)
- Total Folios
- Total Mutual Fund Schemes

### Visualizations

- Industry AUM Trend (2022–2025)
- AUM by Fund House

Purpose:

Provide a high-level overview of the Indian mutual fund industry's growth.

---

## Page 2 – Fund Performance

Designed a performance analytics dashboard including:

### Visualizations

- Top 5 Funds NAV Trend
- Risk vs Return Scatter Plot
- NIFTY 50 vs NIFTY 100 Benchmark Comparison
- Interactive Fund Scorecard

### Slicers

- Fund House
- Category
- Plan

Purpose:

Enable comparison of mutual funds based on returns, volatility, benchmark performance, and overall score.

---

## Page 3 – Investor Analytics

Created an investor analytics dashboard including:

### Visualizations

- Transaction Amount by State
- Average SIP Amount by Age Group
- Investment Type Distribution
- Monthly Transaction Volume

### Slicers

- State
- Age Group
- City Tier

Purpose:

Analyze investor demographics, geographic distribution, and investment behavior.

---

## Page 4 – SIP & Market Trends

Designed a market trends dashboard including:

### KPI Cards

- Latest SIP Inflow
- Latest NIFTY 50
- Latest NIFTY 100
- Highest Net Inflow Category

### Visualizations

- Monthly SIP Inflow vs NIFTY 50 (Dual-Axis Chart)
- Category Inflow Heatmap
- Top Categories by Net Inflow

Purpose:

Study the relationship between SIP inflows, market performance, and category-wise investment trends.

---

## Page 5 – NAV Detail (Drill-through)

Implemented an interactive drill-through page that enables users to navigate from the Fund Performance scorecard to detailed information about an individual mutual fund.

### Features

- Dynamic Fund Name
- Historical NAV Trend
- Fund Details Table
  - Fund House
  - Category
  - Plan
  - Expense Ratio
  - 3-Year Return
  - Sharpe Ratio
  - Alpha
  - Maximum Drawdown
- Automatic Back Button
- Dynamic Filtering

Verified:

- Drill-through navigation
- Automatic filtering based on selected fund
- Back button navigation

The drill-through page follows Microsoft's recommended report design principles by maintaining consistent styling, displaying contextual details for the selected entity, and enabling seamless navigation back to the summary report. :contentReference[oaicite:1]{index=1}

---

# Dashboard Features Implemented

- Interactive KPI Cards
- Cross-filtering
- Dynamic Slicers
- Scatter Plot Analysis
- Matrix Heatmap
- Dual-Axis Charts
- Benchmark Comparison
- Conditional Formatting
- Interactive Drill-through
- Back Navigation
- Dynamic Report Filtering

---

# Tools Used

- Microsoft Power BI Desktop (Version 2.155.756.0)
- Power Query
- DAX (Data Analysis Expressions)
- CSV Data Sources
- SQLite Database

---

# Deliverables Completed

- bluestock_mf_dashboard.pbix
- Industry Overview Dashboard
- Fund Performance Dashboard
- Investor Analytics Dashboard
- SIP & Market Trends Dashboard
- NAV Detail Drill-through Page

Pending Deliverables:

- Dashboard.pdf
- PNG screenshots of all dashboard pages

---

# Challenges Faced

- Configuring Power BI relationships across multiple datasets
- Resolving scatter chart aggregation issues
- Managing DAX measure calculations
- Implementing benchmark comparison visuals
- Configuring drill-through filters
- Synchronizing slicers and visual interactions
- Maintaining consistent dashboard formatting

Each challenge was resolved through iterative testing and validation.

---

# Learning Outcomes

Day 5 provided hands-on experience in:

- Power BI Dashboard Development
- Data Modeling
- DAX Measure Creation
- Interactive Report Design
- Business KPI Development
- Cross-filtering Techniques
- Drill-through Navigation
- Benchmark Visualization
- Professional Dashboard Layout Design

---

# Conclusion

Day 5 concluded with the successful development of a five-page interactive Power BI dashboard for the Bluestock Mutual Fund Capstone project. The dashboard integrates multiple cleaned datasets into a cohesive business intelligence solution featuring executive KPIs, fund performance analysis, investor insights, SIP and market trend analysis, and drill-through navigation. The completed dashboard provides an intuitive, interactive, and professional reporting experience suitable for portfolio analysis and investment decision support.