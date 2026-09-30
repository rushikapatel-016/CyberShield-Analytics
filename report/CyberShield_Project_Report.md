# CyberShield Analytics

## Analysis and Prediction of Global Cyberattack Trends

---

## 1. Introduction

Cyberattacks have become an important cybersecurity concern because they can affect organizations, industries and users across the world.

CyberShield Analytics is a data science and machine learning project developed to analyze global cyberattack incidents from 2015 to 2024.

The project analyzes cyberattack patterns, financial losses, affected users, attack sources, security vulnerabilities, defense mechanisms and incident resolution time. A machine learning model is also used to predict the type of cyberattack based on incident characteristics.

---

## 2. Problem Statement

Organizations generate large amounts of cybersecurity incident data. Analyzing this data manually can make it difficult to identify common attack patterns and understand their impact.

The objective of CyberShield Analytics is to analyze historical cyberattack data and develop a machine-learning-based system that can predict the possible type of cyberattack.

---

## 3. Objectives

The main objectives of the project are:

1. To analyze global cyberattack incidents from 2015 to 2024.
2. To identify frequently occurring cyberattack types.
3. To analyze cyberattacks across different countries.
4. To study the industries targeted by cyberattacks.
5. To analyze financial losses caused by cyberattacks.
6. To study the number of affected users.
7. To analyze common security vulnerabilities.
8. To examine different attack sources.
9. To analyze defense mechanisms used against attacks.
10. To study incident resolution time.
11. To develop a machine learning model for attack type prediction.
12. To develop an interactive Streamlit dashboard.

---

## 4. Dataset Description

The dataset contains 3000 cybersecurity incident records covering the period from 2015 to 2024.

### Dataset Dimensions

- Number of records: 3000
- Number of features: 10
- Years covered: 2015–2024
- Countries: 10
- Attack types: 6
- Target industries: 7

### Dataset Features

| Feature | Description |
|---|---|
| Country | Country where the incident occurred |
| Year | Year of the incident |
| Attack Type | Type of cyberattack |
| Target Industry | Industry targeted by the attack |
| Financial Loss (in Million $) | Financial loss caused by the incident |
| Number of Affected Users | Number of users affected |
| Attack Source | Source/category of the attack |
| Security Vulnerability Type | Vulnerability associated with the incident |
| Defense Mechanism Used | Defense mechanism used |
| Incident Resolution Time (in Hours) | Time required to resolve the incident |

---

## 5. Technologies Used

The project uses the following technologies:

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook
- VS Code

---

## 6. Project Workflow

The project follows the following workflow:

Dataset Collection

↓

Data Loading

↓

Data Understanding

↓

Data Cleaning

↓

Exploratory Data Analysis

↓

Statistical Analysis

↓

Data Visualization

↓

Machine Learning

↓

Model Evaluation

↓

Streamlit Dashboard

---

## 7. Data Preprocessing

The dataset was examined before performing analysis.

The following preprocessing steps were performed:

### 7.1 Missing Value Analysis

The dataset was checked for missing values.

No missing values were found in the dataset.

### 7.2 Duplicate Analysis

Duplicate records were checked.

No duplicate records were found.

### 7.3 Data Type Analysis

The dataset contains:

- Integer features
- Floating-point features
- Categorical/string features

The data types were checked before performing analysis and machine learning.

---

## 8. Exploratory Data Analysis

Exploratory Data Analysis was performed to understand the characteristics of cyberattack incidents.

The analysis includes:

- Attack type distribution
- Country-wise attack distribution
- Industry-wise attack distribution
- Year-wise attack trends
- Financial loss analysis
- Affected user analysis
- Vulnerability analysis
- Attack source analysis
- Defense mechanism analysis
- Incident resolution time analysis

---

## 9. Cyberattack Type Analysis

The dataset contains six attack types:

1. Phishing
2. Ransomware
3. Man-in-the-Middle
4. DDoS
5. SQL Injection
6. Malware

The distribution of these attack types was analyzed using bar charts.

### Visualization

`attack_type_distribution.png`

---

## 10. Country-wise Analysis

Cyberattack incidents were analyzed according to country.

The dataset contains incidents from:

- China
- India
- UK
- Germany
- France
- Australia
- Russia
- Brazil
- Japan
- USA

### Visualization

`attacks_by_country.png`

---

## 11. Target Industry Analysis

The dataset contains seven target industries:

- Education
- Retail
- IT
- Telecommunications
- Government
- Banking
- Healthcare

The number of incidents affecting each industry was analyzed.

### Visualization

`attacks_by_industry.png`

---

## 12. Year-wise Cyberattack Trend

The number of cyberattack incidents was grouped by year from 2015 to 2024.

A line chart was used to visualize the yearly trend.

### Visualization

`attack_trend_by_year.png`

---

## 13. Financial Impact Analysis

Financial loss was analyzed using the following measures:

- Total financial loss
- Average financial loss per incident
- Maximum financial loss
- Average financial loss by attack type
- Average financial loss by year

The financial loss values are represented in million US dollars.

### Visualization

`financial_loss_by_attack.png`

---

## 14. Affected Users Analysis

The number of users affected by cyberattack incidents was analyzed.

The analysis includes:

- Total affected users
- Average affected users per incident
- Maximum affected users in an incident

---

## 15. Security Vulnerability Analysis

The dataset contains different security vulnerability categories.

The distribution of vulnerabilities was analyzed to understand which vulnerability categories occur in the recorded incidents.

### Visualization

`vulnerability_distribution.png`

---

## 16. Attack Source Analysis

The attack source associated with each incident was analyzed.

This helps in understanding the categories of sources associated with the recorded cyberattacks.

---

## 17. Defense Mechanism Analysis

The dataset contains several defense mechanisms.

The project analyzes their frequency across the recorded incidents.

The dashboard displays the distribution of defense mechanisms.

---

## 18. Incident Resolution Time

Incident resolution time was analyzed in hours.

The project calculates:

- Average resolution time
- Maximum resolution time

This provides an overview of how long recorded incidents took to resolve.

---

# 19. Machine Learning

A machine learning model was developed to predict the type of cyberattack.

## Target Variable

The target variable is:

`Attack Type`

## Input Features

The model uses incident-related features such as:

- Country
- Year
- Target Industry
- Financial Loss
- Number of Affected Users
- Attack Source
- Security Vulnerability Type
- Defense Mechanism Used
- Incident Resolution Time

---

## 20. Machine Learning Algorithm

The project uses a Random Forest classification model.

Random Forest is an ensemble machine learning algorithm that combines multiple decision trees to make predictions.

It was selected because it can work with multiple input features and capture relationships between different features.

---

## 21. Model Training

The dataset was divided into training and testing data.

Categorical features were encoded before training the model.

The Random Forest model was trained using the training dataset and evaluated using the testing dataset.

---

## 22. Model Evaluation

The model was evaluated using classification metrics such as:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

These metrics help evaluate the classification performance of the model.

---

## 23. Attack Type Prediction

The trained model is saved as:

`cyberattack_model.pkl`

The Streamlit dashboard allows users to enter information about a cyber incident.

The model then predicts the possible attack type.

The dashboard also displays prediction probabilities for the different attack categories.

---

## 24. Streamlit Dashboard

An interactive Streamlit dashboard was developed for the project.

The dashboard contains the following sections:

### Overview

Displays:

- Total incidents
- Number of countries
- Number of attack types
- Number of target industries
- Dataset preview

### Attack Analysis

Displays:

- Attack type distribution
- Country-wise attacks
- Industry-wise attacks
- Yearly attack trend
- Attack type and industry relationship

### Impact Analysis

Displays:

- Total financial loss
- Average financial loss
- Maximum financial loss
- Financial loss by attack type
- Affected users
- Resolution time
- Financial loss by year

### Security Analysis

Displays:

- Security vulnerabilities
- Attack sources
- Defense mechanisms
- Vulnerability versus attack type

### ML Prediction

Allows the user to enter incident information and obtain a predicted attack type.

---

## 25. Project Structure

```text
CyberShield-Analytics
│
├── dataset
│   └── cyberattacks.csv
│
├── models
│   └── cyberattack_model.pkl
│
├── notebooks
│   └── CyberShield_Analytics.ipynb
│
├── dashboard
│   └── app.py
│
├── visualizations
│   ├── attack_type_distribution.png
│   ├── attacks_by_country.png
│   ├── attacks_by_industry.png
│   ├── attack_trend_by_year.png
│   ├── financial_loss_by_attack.png
│   └── vulnerability_distribution.png
│
└── report
    └── CyberShield_Project_Report.md