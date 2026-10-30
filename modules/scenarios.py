import numpy as np
import pandas as pd


def simulate(df):

    results = []

    for shock in range(-40,45,5):

        shock_decimal = shock/10000

        perf = (
            df["Poids"]
            * (
                df["Carry"]
                + df["RollDown"]
                - df["DURATION"]*shock_decimal
                + 0.5
                * df["CONVEXITÉ"]
                * shock_decimal**2
            )
        ).sum()

        results.append(
            {
                "Choc": shock,
                "Performance": perf
            }
        )

    return pd.DataFrame(results)
