# Customer Segmentation and Churn Analysis

## Project Overview

This project performs **Customer Segmentation and Churn Analysis** using the Telco Customer Churn dataset.
The main objective is to analyze customer behavior and identify which customer groups are more likely to leave the telecom service.

The analysis is performed using:

* Customer tenure
* Monthly charges
* Contract type

The project also generates visual graphs to better understand churn patterns across different customer segments.

---

# Objectives

* Segment customers based on:

  * Tenure
  * Monthly Charges
  * Contract Type
* Analyze churn rates across different segments
* Visualize churn behavior using graphs
* Generate business insights for customer retention

---

# Technologies Used

| Technology | Purpose                   |
| ---------- | ------------------------- |
| Python     | Programming Language      |
| Pandas     | Data Handling & Analysis  |
| Matplotlib | Data Visualization        |
| Seaborn    | Statistical Visualization |

---

# Features Implemented

## 1. Data Cleaning

* Missing value detection
* Conversion of numerical columns
* Removal of invalid records

---

## 2. Customer Segmentation

### Tenure Segmentation

Customers are grouped into:

* 0–1 Year
* 1–2 Years
* 2–4 Years
* 4+ Years

### Monthly Charges Segmentation

Customers are grouped into:

* Low Charges
* Medium Charges
* High Charges

### Contract-Based Segmentation

Customers are analyzed based on:

* Month-to-Month
* One Year
* Two Year Contracts

---

## 3. Churn Analysis

The project calculates churn percentages for:

* Tenure groups
* Monthly charge groups
* Contract types

---

## 4. Data Visualization

The project automatically generates PNG graphs for:

* Churn vs Tenure
* Churn vs Monthly Charges
* Churn vs Contract Type

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/customer-segmentation-churn-analysis.git
```

---

## Install Required Libraries

```bash
pip install pandas matplotlib seaborn
```

---

# How to Run

Place the dataset file in the project folder and run:

```bash
python customer_segmentation_analysis.py
```

---

# Output Files

The following graph files will be generated automatically:

| File Name                          | Description                             |
| ---------------------------------- | --------------------------------------- |
| tenure_churn_analysis.png          | Churn analysis based on tenure          |
| monthly_charges_churn_analysis.png | Churn analysis based on monthly charges |
| contract_churn_analysis.png        | Churn analysis based on contract type   |

---

# Key Business Insights

* Customers with shorter tenure show higher churn rates.
* High monthly charges increase the probability of churn.
* Month-to-month contract customers are more likely to leave.
* Long-term contract customers are more loyal and stable.

---

# Skills Demonstrated

* Customer Segmentation
* Exploratory Data Analysis (EDA)
* Data Cleaning
* Data Visualization
* Churn Prediction Analysis
* Business Intelligence

---

# Future Improvements

* Apply Machine Learning models for churn prediction
* Build an interactive dashboard using Power BI or Tableau
* Deploy the project using Streamlit
* Add advanced customer clustering techniques

---

# Conclusion

This project successfully identifies customer segments with high churn risk using customer tenure, monthly charges, and contract information. The generated insights can help telecom companies improve customer retention strategies and reduce customer churn effectively.

---

# Author

Arsheen Shaikh
