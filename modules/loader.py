import pandas as pd


def load_portfolio(file):

    df = pd.read_excel(
        file,
        sheet_name="Portefeuille"
    )

    # suppression lignes vides
    df = df[df["CODE"].notna()]

    # suppression colonnes Excel parasites
    df = df.loc[
        :,
        ~df.columns.astype(str).str.contains("^Unnamed")
    ]

    return df
