from pathlib import Path
import pandas as pd

# =====================================================
# Paths
# =====================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_PATH = PROJECT_ROOT / "data" / "raw"
PROCESSED_PATH = PROJECT_ROOT / "data" / "processed"

PROCESSED_PATH.mkdir(exist_ok=True)

# =====================================================
# 01 - Fund Master
# =====================================================

def clean_fund_master():

    df = pd.read_csv(RAW_PATH / "01_fund_master.csv")

    df["launch_date"] = pd.to_datetime(
        df["launch_date"],
        errors="coerce"
    )

    before = len(df)

    df = df.drop_duplicates()

    after = len(df)

    print(f"01_fund_master: Removed {before-after} duplicates")

    df.to_csv(
        PROCESSED_PATH / "01_fund_master_clean.csv",
        index=False
    )


# =====================================================
# 02 - NAV History
# =====================================================

def clean_nav_history():

    df = pd.read_csv(RAW_PATH / "02_nav_history.csv")

    df["date"] = pd.to_datetime(
        df["date"],
        errors="coerce"
    )

    df = df.sort_values(
        ["amfi_code", "date"]
    )

    df["nav"] = (
        df.groupby("amfi_code")["nav"]
        .ffill()
    )

    before = len(df)

    df = df.drop_duplicates()

    after = len(df)

    print(f"02_nav_history: Removed {before-after} duplicates")

    df = df[df["nav"] > 0]

    print(
        f"02_nav_history: Final Rows = {len(df)}"
    )

    df.to_csv(
        PROCESSED_PATH / "02_nav_history_clean.csv",
        index=False
    )


# =====================================================
# 03 - AUM by Fund House
# =====================================================

def clean_aum():

    df = pd.read_csv(
        RAW_PATH / "03_aum_by_fund_house.csv"
    )

    df["date"] = pd.to_datetime(
        df["date"],
        errors="coerce"
    )

    df = df.drop_duplicates()

    df = df[
        df["aum_crore"] > 0
    ]

    df.to_csv(
        PROCESSED_PATH /
        "03_aum_by_fund_house_clean.csv",
        index=False
    )

    print("03_aum_by_fund_house cleaned")


# =====================================================
# 04 - Monthly SIP Inflows
# =====================================================

def clean_sip_inflows():

    df = pd.read_csv(
        RAW_PATH /
        "04_monthly_sip_inflows.csv"
    )

    df["month"] = pd.to_datetime(
        df["month"],
        format="%Y-%m",
        errors="coerce"
    )

    df = df.drop_duplicates()

    # Keep NaN in yoy_growth_pct
    # They are valid business nulls

    df.to_csv(
        PROCESSED_PATH /
        "04_monthly_sip_inflows_clean.csv",
        index=False
    )

    print("04_monthly_sip_inflows cleaned")


# =====================================================
# 05 - Category Inflows
# =====================================================

def clean_category_inflows():

    df = pd.read_csv(
        RAW_PATH /
        "05_category_inflows.csv"
    )

    df["month"] = pd.to_datetime(
        df["month"],
        format="%Y-%m",
        errors="coerce"
    )

    df = df.drop_duplicates()

    df.to_csv(
        PROCESSED_PATH /
        "05_category_inflows_clean.csv",
        index=False
    )

    print("05_category_inflows cleaned")


# =====================================================
# 06 - Industry Folio Count
# =====================================================

def clean_folio_count():

    df = pd.read_csv(
        RAW_PATH /
        "06_industry_folio_count.csv"
    )

    df["month"] = pd.to_datetime(
        df["month"],
        format="%Y-%m",
        errors="coerce"
    )

    df = df.drop_duplicates()

    df.to_csv(
        PROCESSED_PATH /
        "06_industry_folio_count_clean.csv",
        index=False
    )

    print("06_industry_folio_count cleaned")


# =====================================================
# 07 - Scheme Performance
# =====================================================

def clean_scheme_performance():

    df = pd.read_csv(
        RAW_PATH /
        "07_scheme_performance.csv"
    )

    return_cols = [
        "return_1yr_pct",
        "return_3yr_pct",
        "return_5yr_pct"
    ]

    for col in return_cols:

        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

        anomalies = (
            df[col]
            .isna()
            .sum()
        )

        print(
            f"{col} anomalies: {anomalies}"
        )

    expense_issues = df[
        (df["expense_ratio_pct"] < 0.1)
        |
        (df["expense_ratio_pct"] > 2.5)
    ]

    print(
        f"Expense Ratio Issues: "
        f"{len(expense_issues)}"
    )

    df = df[
        (df["expense_ratio_pct"] >= 0.1)
        &
        (df["expense_ratio_pct"] <= 2.5)
    ]

    df.to_csv(
        PROCESSED_PATH /
        "07_scheme_performance_clean.csv",
        index=False
    )

    print("07_scheme_performance cleaned")


# =====================================================
# 08 - Investor Transactions
# =====================================================

def clean_transactions():

    df = pd.read_csv(
        RAW_PATH /
        "08_investor_transactions.csv"
    )

    df["transaction_date"] = pd.to_datetime(
        df["transaction_date"],
        errors="coerce"
    )

    df["transaction_type"] = (
        df["transaction_type"]
        .astype(str)
        .str.strip()
        .str.title()
    )

    valid_types = [
        "Sip",
        "Lumpsum",
        "Redemption"
    ]

    print("\nTransaction Types:")

    print(
        df["transaction_type"]
        .value_counts()
    )

    df = df[
        df["transaction_type"]
        .isin(valid_types)
    ]

    df = df[
        df["amount_inr"] > 0
    ]

    print("\nKYC Status:")

    print(
        df["kyc_status"]
        .value_counts()
    )

    valid_kyc = [
        "Verified",
        "Pending"
    ]

    df = df[
        df["kyc_status"]
        .isin(valid_kyc)
    ]

    df.to_csv(
        PROCESSED_PATH /
        "08_investor_transactions_clean.csv",
        index=False
    )

    print("08_investor_transactions cleaned")


# =====================================================
# 09 - Portfolio Holdings
# =====================================================

def clean_portfolio_holdings():

    df = pd.read_csv(
        RAW_PATH /
        "09_portfolio_holdings.csv"
    )

    df["portfolio_date"] = pd.to_datetime(
        df["portfolio_date"],
        errors="coerce"
    )

    df = df.drop_duplicates()

    df = df[
        df["weight_pct"] > 0
    ]

    df.to_csv(
        PROCESSED_PATH /
        "09_portfolio_holdings_clean.csv",
        index=False
    )

    print("09_portfolio_holdings cleaned")


# =====================================================
# 10 - Benchmark Indices
# =====================================================

def clean_benchmark_indices():

    df = pd.read_csv(
        RAW_PATH /
        "10_benchmark_indices.csv"
    )

    df["date"] = pd.to_datetime(
        df["date"],
        errors="coerce"
    )

    df = df.drop_duplicates()

    df = df[
        df["close_value"] > 0
    ]

    df.to_csv(
        PROCESSED_PATH /
        "10_benchmark_indices_clean.csv",
        index=False
    )

    print("10_benchmark_indices cleaned")


# =====================================================
# Main
# =====================================================

if __name__ == "__main__":

    print("=" * 60)
    print("STARTING DATA CLEANING")
    print("=" * 60)

    clean_fund_master()
    clean_nav_history()
    clean_aum()
    clean_sip_inflows()
    clean_category_inflows()
    clean_folio_count()
    clean_scheme_performance()
    clean_transactions()
    clean_portfolio_holdings()
    clean_benchmark_indices()

    print("\n" + "=" * 60)
    print("ALL DATASETS CLEANED SUCCESSFULLY")
    print("=" * 60)