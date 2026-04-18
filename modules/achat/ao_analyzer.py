def scanner_ao(texte_ao, budget_estime):
    """
    Analyse automatique des risques et de la rentabilite d un Appel d Offres.
    """
    # Liste des mots-cles a haut risque dans les contrats industriels
    mots_risques = [
        "penalites de retard", 
        "garantie de performance", 
        "delai de paiement > 90 jours",
        "resiliation sans indemnite",
        "force majeure exclue"
    ]
    
    # Extraction des risques detectes
    risques_detectes = [mot for mot in mots_risques if mot.lower() in texte_ao.lower()]
    
    # Analyse de conformite simplifiee (presence de documents types)
    pieces_obligatoires = ["attestation fiscale", "quittance cnss", "agrement technique"]
    pieces_manquantes = [piece for piece in pieces_obligatoires if piece.lower() not in texte_ao.lower()]
    
    # Calcul du seuil de rentabilite simplifie
    # On considere une marge de securite de 15% pour les risques detectes
    facteur_risque = 1.15 if risques_detectes else 1.05
    seuil_rentabilite = budget_estime * facteur_risque
    
    status = "Favorable"
    if len(risques_detectes) > 2 or len(pieces_manquantes) > 1:
        status = "Risque Eleve"
    
    return {
        "evaluation_globale": status,
        "risques_identifies": risques_detectes,
        "pieces_a_verifier": pieces_manquantes,
        "seuil_rentabilite_suggere": round(seuil_rentabilite, 2),
        "note_strategique": "Le seuil inclut une provision pour risques contractuels."
  }
  
