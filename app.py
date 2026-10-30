import streamlit as st
import plotly.express as px

from modules.loader import load_portfolio
from modules.analytics import portfolio_kpis
from modules.scenarios import simulate

# Configuration de la page
st.set_page_config(
    page_title="ALM Obligataire",
    layout="wide"
)

# Titre
st.title("Plateforme ALM Obligataire")

# Upload du fichier
file = st.file_uploader(
    "Charger le portefeuille Excel",
    type=["xlsx"]
)

# Traitement après chargement
if file:

    try:

        # Chargement portefeuille
        df = load_portfolio(file)

        st.success("Portefeuille chargé")

        # KPI
        kpi = portfolio_kpis(df)

        c1, c2, c3, c4 = st.columns(4)

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

        st.divider()

        # Scénarios
        st.subheader("Simulation de sensibilité")

        scenarios = simulate(df)

        fig = px.line(
            scenarios,
            x="Choc",
            y="Performance",
            markers=True,
            title="Performance du portefeuille selon le choc de taux"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.divider()

        # Données portefeuille
        st.subheader("Portefeuille")

        st.dataframe(
            df,
            use_container_width=True
        )

        st.subheader("Résultats des scénarios")

        st.dataframe(
            scenarios,
            use_container_width=True
        )

    except Exception as e:

        st.exception(e)
