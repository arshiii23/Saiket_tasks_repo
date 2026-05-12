# TASK 3 : CUSTOMER SEGMENTATION ANALYSIS

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# STEP 1 : LOAD DATASET

# Load CSV file
df = pd.read_csv("Telco_Customer_Churn_Dataset .csv")

# Display first 5 rows
print(df.head())

# STEP 2 : DATA CLEANING

# Check missing values
print("\nMissing Values:\n")
print(df.isnull().sum())

# Convert TotalCharges to numeric
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Remove null values
df.dropna(inplace=True)


# STEP 3 : CREATE CUSTOMER SEGMENTS

# -------- TENURE SEGMENT --------

def tenure_group(tenure):
    if tenure <= 12:
        return "0-1 Year"
    elif tenure <= 24:
        return "1-2 Years"
    elif tenure <= 48:
        return "2-4 Years"
    else:
        return "4+ Years"

df['TenureGroup'] = df['tenure'].apply(tenure_group)

# -------- MONTHLY CHARGES SEGMENT --------

def charge_group(charge):
    if charge <= 35:
        return "Low Charges"
    elif charge <= 70:
        return "Medium Charges"
    else:
        return "High Charges"

df['ChargeGroup'] = df['MonthlyCharges'].apply(charge_group)


# STEP 4 : CHURN ANALYSIS

# Convert Churn column into numeric
df['ChurnLabel'] = df['Churn'].map({'Yes': 1, 'No': 0})

# TENURE VS CHURN

tenure_churn = df.groupby('TenureGroup')['ChurnLabel'].mean() * 100

print("\nChurn Rate by Tenure Group:\n")
print(tenure_churn)

# Plot
plt.figure(figsize=(8,5))
sns.barplot(x=tenure_churn.index, y=tenure_churn.values)

plt.title("Churn Rate by Tenure Group")
plt.ylabel("Churn Percentage")
plt.xlabel("Tenure Group")

plt.show()

# MONTHLY CHARGES VS CHURN

charge_churn = df.groupby('ChargeGroup')['ChurnLabel'].mean() * 100

print("\nChurn Rate by Monthly Charge Group:\n")
print(charge_churn)

# Plot
plt.figure(figsize=(8,5))
sns.barplot(x=charge_churn.index, y=charge_churn.values)

plt.title("Churn Rate by Monthly Charges")
plt.ylabel("Churn Percentage")
plt.xlabel("Charge Group")

plt.show()

# CONTRACT TYPE VS CHURN

contract_churn = df.groupby('Contract')['ChurnLabel'].mean() * 100

print("\nChurn Rate by Contract Type:\n")
print(contract_churn)

# Plot
plt.figure(figsize=(8,5))
sns.barplot(x=contract_churn.index, y=contract_churn.values)

plt.title("Churn Rate by Contract Type")
plt.ylabel("Churn Percentage")
plt.xlabel("Contract Type")

plt.show()

# STEP 5 : OVERALL INSIGHTS

print("\n========== BUSINESS INSIGHTS ==========")

print("""
1. Customers with shorter tenure have higher churn rates.

2. Customers with high monthly charges are more likely to leave.

3. Month-to-month contract customers churn the most.

4. Customers with long-term contracts are more loyal.
""")