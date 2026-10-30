import pandas as pd


def simulate(df):

    results = []

    # Vérifications
    required_cols = [
        "Poids",
        "Carry",
        "RollDown",
        "DURATION",
        "CONVEXITÉ"
    ]

    missing = [
        col for col in required_cols
        if col not in df.columns
    ]

    if missing:
        raise ValueError(
            f"Colonnes manquantes : {missing}"
        )

    # Conversion numérique
    for col in required_cols:
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

    df = df.fillna(0)

    # Scénarios de taux
    for shock in range(-40, 45, 5):

        shock_decimal = shock / 10000

        perf = (
            df["Poids"]
            * (
                df["Carry"]
                + df["RollDown"]
                - df["DURATION"] * shock_decimal
                + 0.5
                * df["CONVEXITÉ"]
                * (shock_decimal ** 2)
            )
        ).sum()

        results.append({
            "Choc (bps)": shock,
            "Taux (%)": shock / 100,
            "Performance": perf
        })

    result_df = pd.DataFrame(results)

    # Affichage en %
    result_df["Performance (%)"] = (
        result_df["Performance"] * 100
    )

    return result_df
