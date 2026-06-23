from pathlib import Path
import requests
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_PATH = PROJECT_ROOT / "data" / "raw"

scheme_codes = {
    "hdfc_top_100": 125497,
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_large_cap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

for fund_name, scheme_code in scheme_codes.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    print(f"Fetching {fund_name}...")

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        file_name = f"{fund_name}_nav.csv"

        nav_df.to_csv(
            RAW_PATH / file_name,
            index=False
        )

        print(f"Saved {file_name}")

    else:
        print(f"Failed for {fund_name}")