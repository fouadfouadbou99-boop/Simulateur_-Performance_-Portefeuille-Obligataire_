import streamlit as st

from modules.loader import load_portfolio
from modules.analytics import portfolio_kpis

st.set_page_config(
    page_title="ALM Obligataire",
    layout="wide"
)

st.title("Test Analytics")

st.success("Import analytics.py réussi")
