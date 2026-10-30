import pandas as pd


def load_portfolio(file):

    df = pd.read_excel(file)

    required = [
        "DESCRIPTION",
        "Valorisation",
        "TAUX COURBE",
        "DURATION",
        "CONVEXITÉ"
    ]

    missing = [c for c in required if c not in df.columns]

    if missing:
        raise ValueError(
            f"Colonnes manquantes : {missing}"
        )

    return df
