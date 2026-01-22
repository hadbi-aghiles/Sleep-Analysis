import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load the dataset
df = pd.read_csv('sleep_health_lifestyle_dataset.csv')

# Data cleaning
df['Sleep Disorder'].fillna('No sleep disorder', inplace=True)
df[['Systolic BP', 'Diastolic BP']] = df['Blood Pressure (systolic/diastolic)'].str.split('/', expand=True).astype(int)
df.drop('Blood Pressure (systolic/diastolic)', axis=1, inplace=True)

# Set page title
st.title('Sleep Health and Lifestyle Analysis')

# Sidebar for navigation
st.sidebar.header('Navigation')
section = st.sidebar.selectbox('Select a section', [
    'Dataset Overview',
    'Data Cleaning',
    'Exploratory Data Analysis',
    'Visualizations'
])

if section == 'Dataset Overview':
    st.header('Dataset Overview')
    st.write('### Data Preview')
    st.dataframe(df.head(3))

    st.write('### Columns and Data Types')
    st.write(df.dtypes)

    st.write('### Unique Values in Categorical Columns')
    for col in df.select_dtypes(include=['object']):
        st.write(f'#### {col}')
        st.write(df[col].value_counts())

elif section == 'Data Cleaning':
    st.header('Data Cleaning')
    st.write('#### Missing Values')
    st.write(df.isnull().sum())

    st.write('#### Data Types After Cleaning')
    st.write(df.dtypes)

elif section == 'Exploratory Data Analysis':
    st.header('Exploratory Data Analysis')
    st.write('#### Descriptive Statistics')
    st.write(df.describe())

    st.write('#### Correlation Matrix')
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    corr = df[numerical_cols].corr().round(2)
    st.write(corr)

elif section == 'Visualizations':
    st.header('Visualizations')

    # Distribution of Age
    st.subheader('Distribution of Age')
    fig, ax = plt.subplots()
    ax.hist(df['Age'], bins=10, edgecolor='black')
    ax.set_title('Distribution of Age')
    ax.set_xlabel('Age')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

    # Boxplot of Sleep Duration by Gender
    st.subheader('Boxplot of Sleep Duration by Gender')
    fig, ax = plt.subplots()
    sns.boxplot(x='Gender', y='Sleep Duration (hours)', data=df, ax=ax)
    ax.set_title('Sleep Duration by Gender')
    st.pyplot(fig)

    # Correlation Matrix Heatmap
    st.subheader('Correlation Matrix for Numerical Variables')
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    corr = df[numerical_cols].corr().round(2)
    fig, ax = plt.subplots(figsize=(10,8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    ax.set_title('Correlation Matrix')
    st.pyplot(fig)

    # Sleep Disorder Distribution
    st.subheader('Distribution of Sleep Disorders')
    fig, ax = plt.subplots()
    sns.countplot(x='Sleep Disorder', data=df, order=df['Sleep Disorder'].value_counts().index, ax=ax)
    ax.set_title('Distribution of Sleep Disorders')
    ax.set_xlabel('Sleep Disorder')
    ax.set_ylabel('Count')
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Quality of Sleep by BMI Category
    st.subheader('Quality of Sleep by BMI Category')
    fig, ax = plt.subplots()
    sns.boxplot(x='BMI Category', y='Quality of Sleep (scale: 1-10)', data=df, ax=ax)
    ax.set_title('Quality of Sleep by BMI Category')
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Average Stress Level by Occupation
    st.subheader('Average Stress Level by Occupation')
    fig, ax = plt.subplots()
    avg_stress = df.groupby('Occupation')['Stress Level (scale: 1-10)'].mean().sort_values(ascending=False)
    avg_stress.plot(kind='bar', ax=ax)
    ax.set_title('Average Stress Level by Occupation')
    ax.set_xlabel('Occupation')
    ax.set_ylabel('Average Stress Level')
    st.pyplot(fig)