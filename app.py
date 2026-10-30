import streamlit as st
from modules.loader import load_portfolio

st.set_page_config(
    page_title="ALM Obligataire",
    layout="wide"
)

st.title(
    "Plateforme ALM Obligataire"
)

file = st.file_uploader(
    "Charger le portefeuille Excel",
    type=["xlsx"]
)

if file:

    df = load_portfolio(file)

    st.success(
        "Portefeuille chargé"
    )

    st.dataframe(df)
