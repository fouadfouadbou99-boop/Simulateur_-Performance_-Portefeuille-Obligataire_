import pandas as pd


def load_portfolio(file):

    xls = pd.ExcelFile(file)

    df = pd.read_excel(
        file,
        sheet_name="Portefeuille"
    )

    return df
