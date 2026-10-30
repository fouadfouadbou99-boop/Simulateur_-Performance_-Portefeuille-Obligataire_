import pandas as pd


def portfolio_kpis(df):

    encours = df["Valorisation"].sum()

    duration = (
        df["Poids"]
        * df["DURATION"]
    ).sum()

    convexite = (
        df["Poids"]
        * df["CONVEXITÉ"]
    ).sum()

    dv01 = (
        df["Valorisation"]
        * df["DURATION"]
        * 0.0001
    ).sum()

    pmv = df["PMV NETTE"].sum()

    taux_moyen = (
        df["Poids"]
        * df["TAUX COURBE"]
    ).sum()

    carry = (
        df["Poids"]
        * df["Carry"]
    ).sum()

    rolldown = (
        df["Poids"]
        * df["RollDown"]
    ).sum()

    return {

        "encours": float(encours),

        "duration": float(duration),

        "convexite": float(convexite),

        "dv01": float(dv01),

        "pmv": float(pmv),

        "taux_moyen": float(taux_moyen),

        "carry": float(carry),

        "rolldown": float(rolldown)
    }
