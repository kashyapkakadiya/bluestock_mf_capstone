-- =====================================================
-- Query 1: Top 5 Funds by AUM
-- =====================================================

SELECT
    scheme_name,
    fund_house,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- =====================================================
-- Query 2: Average NAV Per Month
-- =====================================================

SELECT
    strftime('%Y-%m', date) AS month,
    ROUND(AVG(nav), 2) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;


-- =====================================================
-- Query 3: SIP Year-over-Year Growth
-- =====================================================

SELECT
    month,
    sip_inflow_crore,
    yoy_growth_pct
FROM monthly_sip_inflows
ORDER BY month;


-- =====================================================
-- Query 4: Transactions by State
-- =====================================================

SELECT
    state,
    COUNT(*) AS transaction_count,
    ROUND(SUM(amount_inr), 2) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;


-- =====================================================
-- Query 5: Funds with Expense Ratio < 1%
-- =====================================================

SELECT
    scheme_name,
    fund_house,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;


-- =====================================================
-- Query 6: Top 5 Funds by 5-Year Return
-- =====================================================

SELECT
    scheme_name,
    fund_house,
    return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;


-- =====================================================
-- Query 7: Average Expense Ratio by Category
-- =====================================================

SELECT
    category,
    ROUND(AVG(expense_ratio_pct), 2)
        AS avg_expense_ratio
FROM fact_performance
GROUP BY category
ORDER BY avg_expense_ratio;


-- =====================================================
-- Query 8: Fund Houses by Number of Schemes
-- =====================================================

SELECT
    fund_house,
    COUNT(*) AS scheme_count
FROM dim_fund
GROUP BY fund_house
ORDER BY scheme_count DESC;


-- =====================================================
-- Query 9: Total Transaction Amount by Type
-- =====================================================

SELECT
    transaction_type,
    ROUND(SUM(amount_inr), 2)
        AS total_amount
FROM fact_transactions
GROUP BY transaction_type
ORDER BY total_amount DESC;


-- =====================================================
-- Query 10: Top Sectors by Portfolio Weight
-- =====================================================

SELECT
    sector,
    ROUND(AVG(weight_pct), 2)
        AS avg_weight
FROM portfolio_holdings
GROUP BY sector
ORDER BY avg_weight DESC;