import pandas as pd

from modules.analytics import portfolio_kpis


def test_kpis():

    df = pd.DataFrame({

        "Valorisation": [100,100],
        "Poids": [0.5,0.5],
        "DURATION": [5,5],
        "CONVEXITÉ": [20,20],
        "PMV NETTE": [0,0],
        "TAUX COURBE": [0.05,0.05],
        "Carry": [0.05,0.05],
        "RollDown": [0.005,0.005]
    })

    kpi = portfolio_kpis(df)

    assert kpi["duration"] == 5
