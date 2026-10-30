import streamlit as st
import plotly.express as px

from modules.chargeur import load_portfolio
from modules.analytics import portfolio_kpis
from modules.scénarios import simulate

st.set_page_config(
    page_title="ALM Obligataire",
    layout="wide"
)

st.title("Simulateur de Performance du Portefeuille Obligataire")

file = st.file_uploader(
    "Charger le fichier Excel",
    type=["xlsx"]
)

if file:

    try:

        # Chargement du portefeuille
        df = load_portfolio(file)

        st.success("Portefeuille chargé avec succès")

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

        # Simulations
        st.subheader("Scénarios de taux")

        scenarios = simulate(df)

        fig = px.line(
            scenarios,
            x="Choc (bps)",
            y="Performance (%)",
            markers=True,
            title="Sensibilité du portefeuille aux variations de taux"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.dataframe(
            scenarios,
            use_container_width=True
        )

        st.divider()

        # Portefeuille
        st.subheader("Portefeuille")

        st.dataframe(
            df,
            use_container_width=True
        )

    except Exception as e:

        st.error("Erreur lors du traitement du fichier")

        st.exception(e)
