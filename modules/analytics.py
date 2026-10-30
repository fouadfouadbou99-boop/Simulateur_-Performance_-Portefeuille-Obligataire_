import pandas as pd


def portfolio_kpis(df):

    encours = df["Valorisation"].sum()

    duration = (
        df["Poids"] *
        df["DURATION"]
    ).sum()

    convexite = (
        df["Poids"] *
        df["CONVEXITÉ"]
    ).sum()

    dv01 = (
        df["Valorisation"] *
        df["DURATION"] *
        0.0001
    ).sum()

    return {
        "encours": float(encours),
        "duration": float(duration),
        "convexite": float(convexite),
        "dv01": float(dv01)
    }
