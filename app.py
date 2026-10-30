import streamlit as st
import plotly.express as px

from modules.loader import load_portfolio
from modules.analytics import portfolio_kpis
from modules.scenarios import simulate
from modules.commentary import generate_comment
from modules.committee import committee_decision

st.set_page_config(
    page_title="Simulateur Performance Portefeuille Obligataire",
    layout="wide"
)

st.title(
    "📈 Simulateur de Performance du Portefeuille Obligataire"
)

file = st.file_uploader(
    "Charger le portefeuille Excel",
    type=["xlsx"]
)

if file:

    try:

        df = load_portfolio(file)

        st.success(
            "Portefeuille chargé"
        )

        kpi = portfolio_kpis(df)

        st.subheader(
            "Indicateurs clés"
        )

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

        c5, c6, c7, c8 = st.columns(4)

        c5.metric(
            "PMV",
            f"{kpi['pmv']:,.0f} MAD"
        )

        c6.metric(
            "Taux moyen",
            f"{kpi['taux_moyen']:.2%}"
        )

        c7.metric(
            "Carry",
            f"{kpi['carry']:.2%}"
        )

        c8.metric(
            "RollDown",
            f"{kpi['rolldown']:.2%}"
        )

        st.divider()

        scenarios = simulate(df)

        st.subheader(
            "Sensibilité du portefeuille"
        )

        fig = px.line(
            scenarios,
            x="Choc (bps)",
            y="Performance (%)",
            markers=True
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

        st.subheader(
            "Commentaire de gestion"
        )

        st.info(
            generate_comment(kpi)
        )

        st.subheader(
            "Décision proposée au Comité"
        )

        st.warning(
            committee_decision(kpi)
        )

        st.subheader(
            "Portefeuille"
        )

        st.dataframe(
            df,
            use_container_width=True
        )

    except Exception as e:

        st.exception(e)
