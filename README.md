# 💤 Sleep Health and Lifestyle Analysis

This project is a Streamlit web app for analyzing a sleep health and lifestyle dataset.  
The app performs data cleaning, exploratory data analysis, and provides interactive visualizations.

---

## 🧾 Dataset Description

The dataset contains sleep-related information for different individuals, including:

- **Person ID**
- **Gender**
- **Age**
- **Occupation**
- **Sleep Duration (hours)**
- **Quality of Sleep (scale: 1-10)**
- **Physical Activity Level (minutes/day)**
- **Stress Level (scale: 1-10)**
- **BMI Category**
- **Blood Pressure (systolic/diastolic)**
- **Heart Rate (bpm)**
- **Daily Steps**
- **Sleep Disorder**

---

## 🛠️ Features of the App

The Streamlit app contains the following sections:

###  1. Dataset Overview
- Preview of the first rows of the dataset
- Display data types
- Show unique values in categorical columns

###  2. Data Cleaning
- Fill missing values in `Sleep Disorder` with `"No sleep disorder"`
- Split blood pressure into `Systolic BP` and `Diastolic BP`
- Remove the original `Blood Pressure (systolic/diastolic)` column
- Display missing values and data types after cleaning

###  3. Exploratory Data Analysis
- Display descriptive statistics
- Display correlation matrix for numerical variables

###  4. Visualizations
- **Age distribution**
- **Sleep duration by gender**
- **Correlation heatmap**
- **Sleep disorder distribution**
- **Quality of sleep by BMI category**
- **Average stress level by occupation**

---

##  Installation

Make sure you have Python installed (Python 3.8+ recommended).

Install the required libraries:

```bash
pip install pandas matplotlib seaborn streamlit
```
## Author
**Hadbi Aghiles**

