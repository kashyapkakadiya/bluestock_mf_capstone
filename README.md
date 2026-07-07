# 📊 Bluestock Mutual Fund Analytics Platform

An end-to-end Data Analytics Capstone Project that analyzes the Indian Mutual Fund industry using Python, SQLite, SQL, and Power BI. The project covers the complete analytics lifecycle including ETL, data cleaning, exploratory data analysis (EDA), performance analytics, advanced financial analytics, and interactive dashboard development.

---

## 📌 Project Overview

The objective of this project is to transform raw mutual fund datasets into meaningful business insights through data engineering, statistical analysis, and business intelligence.

The project includes:

- Automated ETL Pipeline
- SQLite Database Design
- SQL Queries
- Exploratory Data Analysis (EDA)
- Financial Performance Analytics
- Advanced Risk Analytics
- Interactive Power BI Dashboard
- Professional Project Report
- Presentation Slides

---

# 🚀 Features

### Data Engineering

- Automated ETL Pipeline
- Data Cleaning & Validation
- Missing Value Handling
- Duplicate Removal
- Data Type Standardization
- SQLite Database Integration

### Exploratory Data Analysis

- NAV Trend Analysis
- AUM Analysis
- SIP Growth Analysis
- Category-wise Inflows
- Investor Demographics
- Geographic Distribution
- Correlation Analysis
- Portfolio Sector Allocation

### Performance Analytics

- Daily Returns
- CAGR (1Y / 3Y / 5Y)
- Sharpe Ratio
- Sortino Ratio
- Alpha & Beta
- Maximum Drawdown
- Fund Scorecard
- Benchmark Comparison

### Advanced Analytics

- Historical VaR (95%)
- Conditional VaR (CVaR)
- Rolling 90-Day Sharpe Ratio
- Investor Cohort Analysis
- SIP Continuity Analysis
- Sector HHI Concentration
- Mutual Fund Recommendation System

### Business Intelligence

- Interactive Power BI Dashboard
- KPI Cards
- Drill-through Navigation
- Dynamic Slicers
- Benchmark Comparison
- Tooltips
- Cross Filtering

---

# 🛠 Technology Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python |
| Database | SQLite |
| Query Language | SQL |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| Dashboard | Microsoft Power BI |
| Development | Jupyter Notebook |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```text
bluestock_mf_capstone/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
│
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
│
├── scripts/
│   ├── etl_pipeline.py
│   ├── compute_metrics.py
│   ├── recommender.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── dashboard/
│   ├── bluestock_mf_dashboard.pbix
│   ├── Dashboard.pdf
│   └── screenshots/
│
├── reports/
│   ├── Final_Report.pdf
│   └── Presentation.pptx
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 📊 Dashboard Pages

### 📍 Page 1 – Industry Overview

- Total AUM
- SIP Inflows
- Industry Folios
- Total Schemes
- AUM Trend
- AUM by AMC

---

### 📍 Page 2 – Fund Performance

- Risk vs Return Scatter Plot
- Fund Scorecard
- NAV vs Benchmark
- Performance Slicers

---

### 📍 Page 3 – Investor Analytics

- Transaction Amount by State
- Investment Type Distribution
- Age Group Analysis
- Monthly Transaction Volume

---

### 📍 Page 4 – SIP & Market Trends

- SIP Inflow vs NIFTY
- Category Inflow Heatmap
- Top Categories
- Market Trends

---

# 📈 Performance Metrics

- CAGR
- Daily Returns
- Sharpe Ratio
- Sortino Ratio
- Alpha
- Beta
- Maximum Drawdown
- Tracking Error
- Fund Scorecard

---

# 📉 Advanced Analytics

- Historical VaR
- Conditional VaR
- Rolling Sharpe Ratio
- Investor Cohort Analysis
- SIP Continuity Analysis
- Sector HHI
- Fund Recommendation Engine

---

# 📷 Dashboard Preview

> Add screenshots of all four Power BI dashboard pages here.

Example:

- Industry Overview
- Fund Performance
- Investor Analytics
- SIP & Market Trends

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/bluestock_mf_capstone.git
```

Move into the project folder:

```bash
cd bluestock_mf_capstone
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

Run ETL Pipeline

```bash
python scripts/etl_pipeline.py
```

Run Performance Analytics

```bash
jupyter notebook notebooks/04_performance_analytics.ipynb
```

Run Advanced Analytics

```bash
jupyter notebook notebooks/05_advanced_analytics.ipynb
```

Run Recommendation System

```bash
python scripts/recommender.py
```

---

# 📄 Deliverables

- ETL Pipeline
- SQLite Database
- SQL Queries
- EDA Notebook
- Performance Analytics Notebook
- Advanced Analytics Notebook
- Power BI Dashboard (.pbix)
- Final Project Report (PDF)
- Presentation (PPTX)

---

# 🎯 Key Business Insights

- Mutual fund AUM showed sustained growth during the analysis period.
- SIP inflows reached record highs, indicating increasing retail participation.
- Risk-adjusted metrics identified consistently outperforming funds.
- Rolling Sharpe Ratios highlighted changing market conditions.
- Investor cohort analysis revealed evolving investment patterns.
- Sector HHI analysis measured portfolio diversification.
- Interactive dashboards simplified fund comparison and performance evaluation.

---

# 🔮 Future Enhancements

- Live NAV API Integration
- Streamlit Web Application
- Monte Carlo Simulation
- Portfolio Optimization
- Automated Email Reporting
- Cloud Deployment

---

# 👨‍💻 Author

**Kashyap Kakadiya**

Data Analytics Capstone Project

---

# 📜 License

This project is intended for educational and portfolio purposes.
