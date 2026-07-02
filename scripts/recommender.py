import pandas as pd

# Load data
performance = pd.read_csv(
    "data/processed/07_scheme_performance_clean.csv"
)

# Display available risk grades
print("\nAvailable Risk Levels:")
print(performance["risk_grade"].drop_duplicates().sort_values().to_list())

risk = input(
    "\nEnter Risk Appetite (Low/Moderate/High): "
).strip().title()

# Filter funds
recommendations = (
    performance[
        performance["risk_grade"] == risk
    ]
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(3)
)

if recommendations.empty:

    print("\nNo matching funds found.")

else:

    print("\nTop 3 Recommended Funds\n")

    print(
        recommendations[
            [
                "scheme_name",
                "fund_house",
                "category",
                "sharpe_ratio",
                "return_3yr_pct",
                "expense_ratio_pct"
            ]
        ].to_string(index=False)
    )