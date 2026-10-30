import pandas as pd


COLUMN_MAPPING = {
    "description": "DESCRIPTION",
    "valorisation": "Valorisation",
    "taux courbe": "TAUX COURBE",
    "duration": "DURATION",
    "convexité": "CONVEXITÉ",
    "convexite": "CONVEXITÉ",
}


def normalize_columns(df):

    cols = {}

    for col in df.columns:

        key = (
            str(col)
            .strip()
            .lower()
        )

        if key in COLUMN_MAPPING:

            cols[col] = COLUMN_MAPPING[key]

    return df.rename(columns=cols)


def load_portfolio(file):

    df = pd.read_excel(file)

    df = normalize_columns(df)

    required = [
        "DESCRIPTION",
        "Valorisation",
        "TAUX COURBE",
        "DURATION",
        "CONVEXITÉ"
    ]

    missing = [
        c for c in required
        if c not in df.columns
    ]

    if missing:

        raise ValueError(
            f"Colonnes manquantes: {missing}\n"
            f"Colonnes disponibles: {list(df.columns)}"
        )

    return df
