from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "raw"

csv_files = sorted(DATA_PATH.glob("*.csv"))

print(f"Data Path: {DATA_PATH}")
print(f"Total Files Found: {len(csv_files)}")

for file in csv_files:
    print("=" * 80)
    print(f"Dataset: {file.name}")

    df = pd.read_csv(file)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

print("\n" + "="*80)
print("FUND MASTER EXPLORATION")
print("="*80)

fund_master = pd.read_csv(DATA_PATH / "01_fund_master.csv")

print("\nUnique Fund Houses:")
print(fund_master["fund_house"].unique())

print("\nUnique Categories:")
print(fund_master["category"].unique())

print("\nUnique Sub Categories:")
print(fund_master["sub_category"].unique())

print("\nUnique Risk Categories:")
print(fund_master["risk_category"].unique())

print("\n" + "="*80)
print("AMFI CODE VALIDATION")
print("="*80)

nav_history = pd.read_csv(DATA_PATH / "02_nav_history.csv")

fund_codes = set(fund_master["amfi_code"].astype(str))
nav_codes = set(nav_history["amfi_code"].astype(str))

missing_codes = fund_codes - nav_codes

print(f"Fund Master Codes: {len(fund_codes)}")
print(f"NAV History Codes: {len(nav_codes)}")
print(f"Missing Codes: {len(missing_codes)}")

if missing_codes:
    print("Missing:", missing_codes)
else:
    print("All AMFI codes validated successfully.")