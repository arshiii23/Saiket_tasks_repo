# Churn Prediction Model using Machine Learning

## Project Overview

This project focuses on building a **Customer Churn Prediction Model** using Machine Learning techniques on the Telco Customer Churn dataset.

The main objective of this project is to predict whether a customer is likely to leave the telecom service based on customer behavior, subscription details, billing information, and contract type.

The project includes:

* Data cleaning
* Data preprocessing
* Feature encoding
* Machine learning model training
* Model evaluation
* Data visualization

---

# Objectives

* Predict customer churn using Machine Learning
* Perform data preprocessing and cleaning
* Convert categorical data into numerical format
* Train a Logistic Regression model
* Evaluate model performance using different metrics
* Generate visual reports for analysis

---

# Technologies Used

| Technology   | Purpose                  |
| ------------ | ------------------------ |
| Python       | Programming Language     |
| Pandas       | Data Handling & Analysis |
| Matplotlib   | Data Visualization       |
| Seaborn      | Statistical Graphs       |
| Scikit-learn | Machine Learning         |

---

# Machine Learning Algorithm Used

## Logistic Regression

Logistic Regression is a supervised machine learning algorithm used for binary classification problems such as:

* Churn = Yes
* Churn = No

The model predicts the probability of customer churn based on customer-related features.

---

# Dataset Information

Dataset Used:

* Telco Customer Churn Dataset

The dataset contains:

* Customer demographics
* Service subscriptions
* Billing details
* Internet services
* Contract information
* Churn status

---

# Features Implemented

## 1. Data Cleaning

* Handling missing values
* Converting numerical columns
* Removing unnecessary columns

---

## 2. Data Encoding

Categorical values such as:

* Male/Female
* Yes/No
* Contract Types

are converted into numerical values using:

```python id="c64x5h"
pd.get_dummies()
```

---

## 3. Machine Learning Model Training

The project trains a Logistic Regression model using:

* Training dataset
* Customer features

---

## 4. Model Evaluation

The model performance is evaluated using:

* Accuracy Score
* Classification Report
* Confusion Matrix

---

## 5. Data Visualization

The project automatically generates:

* Confusion Matrix Heatmap
* Feature Importance Graph

---

# Installation

## Clone Repository

```bash id="w1m3s2"
git clone https://github.com/your-username/churn-prediction-model.git
```

---

## Install Required Libraries

```bash id="rrjwv9"
pip install pandas matplotlib seaborn scikit-learn
```
---

# Output Files

The following files are automatically generated inside the **Task 4** folder:

| File Name              | Description                        |
| ---------------------- | ---------------------------------- |
| confusion_matrix.png   | Model performance visualization    |
| feature_importance.png | Important features affecting churn |

---

# Model Evaluation Metrics

| Metric    | Description                          |
| --------- | ------------------------------------ |
| Accuracy  | Overall prediction correctness       |
| Precision | Correct positive predictions         |
| Recall    | Ability to detect churn customers    |
| F1-Score  | Balance between precision and recall |

---

# Key Insights

* Customers with month-to-month contracts are more likely to churn.
* High monthly charges increase churn probability.
* Long-term customers are more loyal.
* Contract type is one of the strongest churn indicators.

---

# Skills Demonstrated

* Machine Learning
* Logistic Regression
* Data Preprocessing
* Feature Engineering
* Data Visualization
* Customer Churn Analysis
* Business Intelligence

---

# Future Improvements

* Implement advanced models:

  * Random Forest
  * Decision Tree
  * XGBoost
* Perform hyperparameter tuning
* Build interactive dashboards
* Deploy using Streamlit or Flask

---

# Conclusion

This project successfully predicts customer churn using Logistic Regression and telecom customer data. The analysis helps businesses identify high-risk customers and improve customer retention strategies effectively.

---

# Author

Arsheen Shaikh

Data Science Internship Project
