import pandas as pd
import streamlit as st
import plotly.express as px

class Methods:

    @staticmethod
    def telechargement_fichier():
        uploaded_file = st.file_uploader("Choisissez un fichier CSV", type="csv")
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.write("Aperçu du fichier :")
            st.write(df.head())
            return df
        return None

    @staticmethod
    def eda(df):
        st.write("Statistiques sommaires :")
        st.write(df.describe())

        st.write("Valeurs manquantes :")
        st.write(df.isnull().sum())

        st.write("Types de données :")
        st.write(df.dtypes)

    @staticmethod
    def visualisations(df):
        for column in df.select_dtypes(include=['float64', 'int64']).columns:
            st.write(f"Distribution de {column}")
            fig = px.histogram(df, x=column)
            st.plotly_chart(fig)

    @staticmethod
    def choix_sidebar():
        return Methods  
