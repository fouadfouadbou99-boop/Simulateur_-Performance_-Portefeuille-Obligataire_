import streamlit as st
from modules.loader import load_portfolio
from modules.analytics import portfolio_kpis
import plotly.express as px

from modules.scenarios import simulate
scenarios = simulate(df)

fig = px.line(
    scenarios,
    x="Choc",
    y="Performance",
    markers=True
)

st.plotly_chart(
    fig,
    use_container_width=True
)
kpi = portfolio_kpis(df)

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "Encours",
    f"{kpi['encours']:,.0f} MAD"
)

c2.metric(
    "Duration",
    f"{kpi['duration']:.2f}"
)

c3.metric(
    "Convexité",
    f"{kpi['convexite']:.2f}"
)

c4.metric(
    "DV01",
    f"{kpi['dv01']:,.0f} MAD"
)
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
