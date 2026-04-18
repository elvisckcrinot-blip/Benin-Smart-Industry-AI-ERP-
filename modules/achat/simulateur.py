from modules.achat.tax_benin import calculer_fiscalite_benin

def comparer_offres_incoterms(prix_base, fret_estime, assurance_estimee, categorie_produit):
    """
    Simule le passage d'un prix depart usine a un prix rendu Benin.
    """
    # 1. Simulation FOB (Prix base + transport vers port depart + chargement)
    # Ici on simplifie en considerant le prix_base comme base de calcul
    
    # 2. Simulation CIF Cotonou
    valeur_cif = prix_base + fret_estime + assurance_estimee
    
    # 3. Simulation DDP (Calcul des taxes douanieres incluses)
    fiscalite = calculer_fiscalite_benin(valeur_cif, categorie_produit)
    
    return {
        "scenario_cif": {
            "valeur_marchandise": prix_base,
            "fret": fret_estime,
            "assurance": assurance_estimee,
            "total_cif": valeur_cif
        },
        "scenario_ddp": {
            "valeur_cif": valeur_cif,
            "droits_douane": fiscalite["droits_douane"],
            "tva": fiscalite["tva"],
            "taxes_communautaires": fiscalite["taxes_communautaires"],
            "total_rendu_ddp": fiscalite["cout_total_rendu"]
        },
        "economie_potentielle": {
            "conseil": "Comparer le total_rendu_ddp avec l offre directe du fournisseur."
        }
  }
  
