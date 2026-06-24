from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine, text

# =====================================================
# Paths
# =====================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

PROCESSED_PATH = PROJECT_ROOT / "data" / "processed"
DATABASE_PATH = PROJECT_ROOT / "database" / "bluestock_mf.db"
SCHEMA_PATH = PROJECT_ROOT / "sql" / "schema.sql"

# =====================================================
# SQLite Connection
# =====================================================

engine = create_engine(
    f"sqlite:///{DATABASE_PATH}"
)

# =====================================================
# Create Tables From schema.sql
# =====================================================

with engine.begin() as conn:

    # SQLite foreign keys are disabled by default
    conn.execute(text("PRAGMA foreign_keys = ON"))  # required per connection :contentReference[oaicite:0]{index=0}

    schema_sql = SCHEMA_PATH.read_text(
        encoding="utf-8"
    )

    for statement in schema_sql.split(";"):

        if statement.strip():

            conn.execute(
                text(statement)
            )

print("Schema created successfully")

# =====================================================
# Load Data
# =====================================================

files = {
    "dim_fund":
        "01_fund_master_clean.csv",

    "fact_nav":
        "02_nav_history_clean.csv",

    "fact_aum":
        "03_aum_by_fund_house_clean.csv",

    "monthly_sip_inflows":
        "04_monthly_sip_inflows_clean.csv",

    "category_inflows":
        "05_category_inflows_clean.csv",

    "industry_folio_count":
        "06_industry_folio_count_clean.csv",

    "fact_performance":
        "07_scheme_performance_clean.csv",

    "fact_transactions":
        "08_investor_transactions_clean.csv",

    "portfolio_holdings":
        "09_portfolio_holdings_clean.csv",

    "benchmark_indices":
        "10_benchmark_indices_clean.csv"
}

print("\nLoading tables...\n")

for table_name, file_name in files.items():

    file_path = (
        PROCESSED_PATH / file_name
    )

    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(
        f"{table_name}: "
        f"{len(df)} rows loaded"
    )

print("\nData loading complete.")

# =====================================================
# Verify Counts
# =====================================================

print("\nVerifying row counts...\n")

for table_name in files.keys():

    query = f"""
    SELECT COUNT(*)
    FROM {table_name}
    """

    count = pd.read_sql(
        query,
        engine
    ).iloc[0, 0]

    print(
        f"{table_name}: {count} rows"
    )

print("\nDatabase verification complete.")