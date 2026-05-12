# TASK 5 - CUSTOMER RETENTION STRATEGIES ANALYSIS

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

output_folder = "Saiket_task5/output"

os.makedirs(output_folder, exist_ok=True)

df = pd.read_csv(
    "Saiket_task5/Telco_Customer_Churn_Dataset .csv"
)

print("\nDataset Loaded Successfully!\n")


print(df.head())

print("\nDataset Information:\n")

print(df.info())

print("\nMissing Values:\n")

print(df.isnull().sum())

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

# Fill missing values
df["TotalCharges"].fillna(
    df["TotalCharges"].median(),
    inplace=True
)

print("\nData Cleaning Completed!\n")

plt.figure(figsize=(6, 4))

sns.countplot(
    x="Churn",
    data=df
)

plt.title("Customer Churn Distribution")

plt.savefig(
    f"{output_folder}/churn_distribution.png"
)

plt.show()

plt.figure(figsize=(8, 5))

sns.countplot(
    x="Contract",
    hue="Churn",
    data=df
)

plt.title("Contract Type vs Churn")

plt.xticks(rotation=10)

plt.savefig(
    f"{output_folder}/contract_vs_churn.png"
)

plt.show()

plt.figure(figsize=(8, 5))

sns.boxplot(
    x="Churn",
    y="MonthlyCharges",
    data=df
)

plt.title("Monthly Charges vs Churn")

plt.savefig(
    f"{output_folder}/monthlycharges_vs_churn.png"
)

plt.show()

plt.figure(figsize=(8, 5))

sns.countplot(
    x="InternetService",
    hue="Churn",
    data=df
)

plt.title("Internet Service vs Churn")

plt.savefig(
    f"{output_folder}/internetservice_vs_churn.png"
)

plt.show()

df["LTV"] = (
    df["MonthlyCharges"] * df["tenure"]
)

print("\nCustomer Lifetime Value Calculated!\n")

print(df[[
    "customerID",
    "MonthlyCharges",
    "tenure",
    "LTV"
]].head())


high_value_customers = df[
    df["LTV"] > df["LTV"].quantile(0.75)
]

print("\nHigh Value Customers:\n")

print(high_value_customers.head())

at_risk_customers = high_value_customers[
    high_value_customers["Churn"] == "Yes"
]

print("\nHigh Value Customers At Risk:\n")

print(at_risk_customers[[
    "customerID",
    "tenure",
    "MonthlyCharges",
    "LTV",
    "Contract"
]].head())

# Save risky customers CSV
at_risk_customers.to_csv(
    f"{output_folder}/high_value_customers_at_risk.csv",
    index=False
)

churn_rate = (
    df["Churn"]
    .value_counts(normalize=True)["Yes"]
) * 100

print(f"\nOverall Churn Rate: {churn_rate:.2f}%")

print("\n====================================")
print("CUSTOMER RETENTION STRATEGIES")
print("====================================")

print("""

1. Month-to-month customers churn more.
   -> Encourage yearly subscriptions.

2. High monthly charges increase churn.
   -> Provide discounts and loyalty rewards.

3. Fiber optic users have higher churn.
   -> Improve service quality.

4. High-value customers should receive
   personalized retention offers.

5. Long-tenure customers should receive
   premium customer support.

""")


df.to_csv(
    f"{output_folder}/final_customer_analysis.csv",
    index=False
)

print("Final Dataset Saved!")

print("\nPROJECT COMPLETED SUCCESSFULLY!")