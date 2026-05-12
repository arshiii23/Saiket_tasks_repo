
# TASK 4 : CHURN PREDICTION MODEL

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Machine Learning Libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# STEP 1 : CREATE TASK 4 FOLDER PATH


# Get current working directory
main_folder = os.getcwd()

# Create Task 4 folder path
task4_folder = os.path.join(main_folder, "Task 4")

# Create folder if it does not exist
os.makedirs(task4_folder, exist_ok=True)

# STEP 2 : LOAD DATASET


# Dataset path
dataset_path = os.path.join(
    main_folder,
    "Telco_Customer_Churn_Dataset .csv"
)

# Load dataset
df = pd.read_csv(dataset_path)

print("\n========== ORIGINAL DATA ==========\n")
print(df.head())


# STEP 3 : DATA CLEANING


# Convert TotalCharges column into numeric
df['TotalCharges'] = pd.to_numeric(
    df['TotalCharges'],
    errors='coerce'
)

# Remove missing values
df.dropna(inplace=True)

# Remove customerID column
if 'customerID' in df.columns:
    df.drop('customerID', axis=1, inplace=True)


# STEP 4 : CONVERT TEXT DATA TO NUMBERS


# Convert categorical columns into numeric
df = pd.get_dummies(df, drop_first=True)

print("\n========== ENCODED DATA ==========\n")
print(df.head())


# STEP 5 : DEFINE FEATURES AND TARGET


# Target column
target_column = 'Churn_Yes'

# Input features
X = df.drop(target_column, axis=1)

# Output target
y = df[target_column]


# STEP 6 : SPLIT DATA

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)

# STEP 7 : CREATE AND TRAIN MODEL


# Create Logistic Regression model
model = LogisticRegression(max_iter=5000)

# Train model
model.fit(X_train, y_train)

print("\n========== MODEL TRAINED SUCCESSFULLY ==========")


# STEP 8 : MAKE PREDICTIONS


# Predict churn
y_pred = model.predict(X_test)


# STEP 9 : MODEL EVALUATION


# Accuracy score
accuracy = accuracy_score(y_test, y_pred)

print("\n========== MODEL ACCURACY ==========")
print("Accuracy:", round(accuracy * 100, 2), "%")

# Classification Report
print("\n========== CLASSIFICATION REPORT ==========\n")
print(classification_report(y_test, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

print("\n========== CONFUSION MATRIX ==========\n")
print(cm)


# STEP 10 : CONFUSION MATRIX VISUALIZATION

plt.figure(figsize=(6,5))

sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues'
)

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

# Save image inside Task 4 folder
plt.savefig(
    os.path.join(
        task4_folder,
        "confusion_matrix.png"
    )
)

plt.show()


# STEP 11 : FEATURE IMPORTANCE


# Create importance dataframe
importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': model.coef_[0]
})

# Sort features
importance = importance.sort_values(
    by='Importance',
    ascending=False
)

print("\n========== TOP IMPORTANT FEATURES ==========\n")
print(importance.head(10))

# Plot graph
plt.figure(figsize=(10,6))

sns.barplot(
    x='Importance',
    y='Feature',
    data=importance.head(10)
)

plt.title("Top Features Affecting Churn")

# Save image inside Task 4 folder
plt.savefig(
    os.path.join(
        task4_folder,
        "feature_importance.png"
    )
)

plt.show()


# FINAL MESSAGE


print("\n===================================")
print("PROJECT EXECUTED SUCCESSFULLY")
print("Images saved inside Task 4 folder")
print("===================================")
