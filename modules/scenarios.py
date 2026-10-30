import pandas as pd


def simulate(df):

    results = []

    encours = df["Valorisation"].sum()

    for shock in range(-40, 45, 5):

        shock_decimal = shock / 10000

        performance = (
            df["Poids"]
            * (
                df["Carry"]
                + df["RollDown"]
                - df["DURATION"] * shock_decimal
                + 0.5
                * df["CONVEXITÉ"]
                * shock_decimal**2
            )
        ).sum()

        impact = performance * encours

        results.append(
            {
                "Choc (bps)": shock,
                "Performance (%)": performance * 100,
                "Impact MAD": impact
            }
        )

    return pd.DataFrame(results)
