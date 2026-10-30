import streamlit as st

from modules.loader import load_portfolio

st.set_page_config(
    page_title="ALM Obligataire",
    layout="wide"
)

st.title("Test Loader")

st.success("Import de loader.py réussi")
