This project performs an end-to-end Exploratory Data Analysis (EDA) on a banking customer dataset to understand lending risk, customer behaviour, and financial patterns that influence credit decisions.

The analysis helps banks identify high-risk, medium-risk, and low-risk customers by studying demographic and financial parameters such as income, occupation, credit card behaviour, deposits, loans, and savings.

Problem statement:
Develop a basic understanding of risk analytics in banking and financial services and understand how data is used to minimise the risk of losing money while lending to customers.

Banks face challenges such as:

Identifying customers who may default

Estimating credit risk based on income, spending patterns, and loans

Detecting early warning signals

Understanding customer segmentation for better loan decisions

Dataset:
The dataset contains 3,000 customer records with 25+ variables, including:

1.Demographic Information

Age

Gender ID

Nationality

Location ID

Occupation

Loyalty Classification

2.Financial & Banking Features

Estimated Income

Credit Card Balance

Bank Loans

Deposits

Savings Accounts

Checking Accounts

Business Lending

Foreign Currency Accounts

Risk Weight

Number of Properties

These variables help assess customer financial behaviour and their risk profile.

Python EDA (banking.ipynb)

The following steps are performed in Python using Pandas, NumPy, and Matplotlib/Seaborn:

1. Data Cleaning & Preparation

Checking missing values

Data type correction

Date parsing

Removing formatting issues

2. Descriptive Statistics

Summary of income, balances, loans, savings

Outlier detection

Overall customer financial health analysis

3. Univariate & Bivariate Analysis

Distribution of Age, Income, Loan Amount

Occupation vs Income

Loyalty vs Spending

Loans vs Savings

Credit card usage patterns

4. Correlation Analysis

Which financial variables impact lending risk?

Relationship between income, card balance, and loan behaviour

5. Risk Identification

Python identifies:

 High-Risk Indicators

Low savings + very high loans

High credit card balance relative to income

Irregular banking patterns

High Risk Weight score

Occupations with inconsistent income

 Low-Risk Indicators

High income + stable savings

Reasonable loan-to-income ratio

Good loyalty classification

Consistent banking product usage

Powerbi:
An interactive Power BI Dashboard is created to visualize banking behaviour and risk across customer segments.