import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Charger le dataset
df = pd.read_csv('sleep_health_lifestyle_dataset.csv')

# Nettoyage des données
df['Sleep Disorder'].fillna('Aucun trouble du sommeil', inplace=True)
df[['Systolic BP', 'Diastolic BP']] = df['Blood Pressure (systolic/diastolic)'].str.split('/', expand=True).astype(int)
df.drop('Blood Pressure (systolic/diastolic)', axis=1, inplace=True)

# Définir le titre de la page
st.title('Analyse de la santé du sommeil et du mode de vie')

# Barre latérale pour la navigation
st.sidebar.header('Navigation')
section = st.sidebar.selectbox('Sélectionnez une section', [
    'Aperçu du jeu de données',
    'Nettoyage des données',
    'Analyse exploratoire des données',
    'Visualisations'
])

if section == 'Aperçu du jeu de données':
    st.header('Aperçu du jeu de données')
    st.write('### Aperçu des données')
    st.dataframe(df.head(3))

    st.write('### Colonnes et types de données')
    st.write(df.dtypes)

    st.write('### Valeurs uniques dans les colonnes catégorielles')
    for col in df.select_dtypes(include=['object']):
        st.write(f'#### {col}')
        st.write(df[col].value_counts())

elif section == 'Nettoyage des données':
    st.header('Nettoyage des données')
    st.write('#### Valeurs manquantes')
    st.write(df.isnull().sum())

    st.write('#### Types de données après nettoyage')
    st.write(df.dtypes)

elif section == 'Analyse exploratoire des données':
    st.header('Analyse exploratoire des données')
    st.write('#### Statistiques descriptives')
    st.write(df.describe())

    st.write('#### Matrice de corrélation')
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    corr = df[numerical_cols].corr().round(2)
    st.write(corr)

elif section == 'Visualisations':
    st.header('Visualisations')

    # Distribution de l'âge
    st.subheader('Distribution de l\'âge')
    fig, ax = plt.subplots()
    ax.hist(df['Age'], bins=10, edgecolor='black')
    ax.set_title('Distribution de l\'âge')
    ax.set_xlabel('Âge')
    ax.set_ylabel('Fréquence')
    st.pyplot(fig)

    # Diagramme en boîte de la durée de sommeil par genre
    st.subheader('Diagramme en boîte de la durée de sommeil par genre')
    fig, ax = plt.subplots()
    sns.boxplot(x='Gender', y='Sleep Duration (hours)', data=df, ax=ax)
    ax.set_title('Durée de sommeil par genre')
    st.pyplot(fig)

    # Carte de chaleur de la matrice de corrélation
    st.subheader('Matrice de corrélation pour les variables numériques')
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    corr = df[numerical_cols].corr().round(2)
    fig, ax = plt.subplots(figsize=(10,8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    ax.set_title('Matrice de corrélation')
    st.pyplot(fig)

    # Répartition des troubles du sommeil
    st.subheader('Répartition des troubles du sommeil')
    fig, ax = plt.subplots()
    sns.countplot(x='Sleep Disorder', data=df, order=df['Sleep Disorder'].value_counts().index, ax=ax)
    ax.set_title('Répartition des troubles du sommeil')
    ax.set_xlabel('Trouble du sommeil')
    ax.set_ylabel('Comptage')
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Qualité du sommeil par catégorie IMC
    st.subheader('Qualité du sommeil par catégorie IMC')
    fig, ax = plt.subplots()
    sns.boxplot(x='BMI Category', y='Quality of Sleep (scale: 1-10)', data=df, ax=ax)
    ax.set_title('Qualité du sommeil par catégorie IMC')
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Niveau de stress moyen par occupation
    st.subheader('Niveau de stress moyen par occupation')
    fig, ax = plt.subplots()
    avg_stress = df.groupby('Occupation')['Stress Level (scale: 1-10)'].mean().sort_values(ascending=False)
    avg_stress.plot(kind='bar', ax=ax)
    ax.set_title('Niveau de stress moyen par occupation')
    ax.set_xlabel('Occupation')
    ax.set_ylabel('Niveau de stress moyen')
    st.pyplot(fig)