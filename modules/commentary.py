def generate_comment(kpi):

    return f"""
Le portefeuille présente un encours de
{kpi['encours']:,.0f} MAD.

La duration moyenne ressort à
{kpi['duration']:.2f} ans.

Le DV01 atteint
{kpi['dv01']:,.0f} MAD.

La convexité moyenne ressort à
{kpi['convexite']:.2f}.

Le portefeuille demeure sensible aux variations des taux d'intérêt compte tenu de son exposition aux maturités longues.
"""
