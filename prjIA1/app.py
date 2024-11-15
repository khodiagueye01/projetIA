import streamlit as st
import pandas as pd
from Methods import Methods

def main():
    st.title("Application de Data Science avec Streamlit")

    menu = ["Téléchargement de Fichier", "Analyse Exploratoire (EDA)"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Téléchargement de Fichier":
        df = Methods.telechargement_fichier()
        if df is not None:
            st.session_state['dataframe'] = df

    elif choice == "Analyse Exploratoire (EDA)":
        if 'dataframe' in st.session_state:
            Methods.eda(st.session_state['dataframe'])
            Methods.visualisations(st.session_state['dataframe'])
        else:
            st.write("Téléchargez d'abord un fichier CSV.")

    

if __name__ == '__main__':
    main()
