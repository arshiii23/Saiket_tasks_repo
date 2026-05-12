# Import libraries
import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import LabelEncoder

# -----------------------------
# LOAD DATASET
# -----------------------------

df = pd.read_csv("Telco_Customer_Churn_Dataset .csv")

# -----------------------------
# DISPLAY BASIC INFORMATION
# -----------------------------

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# -----------------------------
# HANDLE MISSING VALUES
# -----------------------------

# Numerical columns
numerical_cols = df.select_dtypes(include=np.number).columns

for col in numerical_cols:
    df[col] = df[col].fillna(df[col].mean())

# Categorical columns
categorical_cols = df.select_dtypes(include='object').columns

for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# -----------------------------
# ENCODE CATEGORICAL VARIABLES
# -----------------------------

le = LabelEncoder()

for col in categorical_cols:
    df[col] = le.fit_transform(df[col])

print("\nEncoded Dataset:")
print(df.head())

# -----------------------------
# CREATE OUTPUT FOLDER
# -----------------------------

os.makedirs("output", exist_ok=True)

# -----------------------------
# SAVE CLEANED DATASET
# -----------------------------

output_path = "output/cleaned_telco_customer_churn.csv"

df.to_csv(output_path, index=False)

print(f"\nCleaned dataset saved successfully at: {output_path}")