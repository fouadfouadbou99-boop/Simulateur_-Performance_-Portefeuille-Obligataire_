def committee_decision(kpi):

    if kpi["duration"] > 10:

        return """
Décision proposée :

Le Comité recommande une réduction progressive
de la duration afin de limiter l'exposition
au risque de remontée des taux.
"""

    return """
Décision proposée :

Le Comité décide le maintien
de l'allocation actuelle.
"""
