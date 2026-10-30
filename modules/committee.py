def committee_decision(kpi):

    if kpi["duration"] > 10:

        return """
Décision proposée :

Le Comité prend acte du niveau élevé de duration du portefeuille.

Le Comité recommande le maintien d'une surveillance rapprochée du risque de taux et l'étude d'opportunités d'arbitrage susceptibles de réduire progressivement la duration.
"""

    return """
Décision proposée :

Le Comité prend acte des indicateurs de risque et décide le maintien de l'allocation actuelle.
"""
