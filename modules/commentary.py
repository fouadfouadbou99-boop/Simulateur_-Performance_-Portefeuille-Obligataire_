def generate_comment(kpi):

    txt = f"""
Le portefeuille présente un encours de
{kpi['encours']:,.0f} MAD.

La duration moyenne ressort à
{kpi['duration']:.2f} ans.

Le DV01 atteint
{kpi['dv01']:,.0f} MAD,
ce qui traduit une sensibilité significative
aux variations de taux.

Compte tenu d'une convexité moyenne de
{kpi['convexite']:.2f},
le portefeuille demeure favorablement exposé
à un scénario de détente des taux.
"""

    return txt
