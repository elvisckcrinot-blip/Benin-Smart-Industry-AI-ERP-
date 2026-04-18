import pandas as pd

def calculer_cout_revient(cout_matiere, temps_machine, taux_horaire_machine, main_doeuvre, frais_fixes_pct=0.15):
    """
    Calcule le cout de revient industriel complet.
    """
    cout_operationnel = (temps_machine * taux_horaire_machine) + main_doeuvre
    sous_total = cout_matiere + cout_operationnel
    cout_final = sous_total * (1 + frais_fixes_pct)
    
    return {
        "cout_matiere": round(cout_matiere, 2),
        "cout_transformation": round(cout_operationnel, 2),
        "frais_fixes_appliqués": f"{frais_fixes_pct*100}%",
        "cout_revient_total": round(cout_final, 2)
    }

def gestion_flux_pull_jat(demande_reelle, stock_disponible, temps_production_unitaire):
    """
    Methode Juste-a-Temps (Pull) : On ne produit que ce qui est deja commande.
    """
    a_produire = max(0, demande_reelle - stock_disponible)
    delai_estime = a_produire * temps_production_unitaire
    
    return {
        "strategie": "PULL (Juste-a-Temps)",
        "quantite_a_lancer": a_produire,
        "delai_livraison_estime": f"{delai_estime} min",
        "action": "Lancer la production uniquement sur commande ferme."
    }

def gestion_flux_pousse_push(prevision_demande, stock_securite, capacite_max):
    """
    Methode Flux Pousse (Push) : On produit selon les previsions (stockage).
    """
    quantite_cible = prevision_demande + stock_securite
    production_reelle = min(quantite_cible, capacite_max)
    
    return {
        "strategie": "PUSH (Flux Pousse)",
        "quantite_a_produire": production_reelle,
        "utilisation_capacite": f"{(production_reelle/capacite_max)*100}%",
        "action": "Produire pour alimenter le stock de prevision."
    }

def gestion_flux_synchrone(cadence_amont, capacite_aval):
    """
    Methode Flux Synchrone : Aligne la production sur la cadence de l etape suivante.
    Evite les goulots d etranglement.
    """
    ecart = cadence_amont - capacite_aval
    status = "Equilibre" if abs(ecart) < 0.1 else "Desequilibre"
    
    recommandation = "Flux optimal"
    if ecart > 0:
        recommandation = f"Ralentir l amont de {ecart} unites/h pour eviter l encours."
    elif ecart < 0:
        recommandation = f"Augmenter l amont de {abs(ecart)} unites/h pour saturer l aval."

    return {
        "strategie": "SYNCHRONE",
        "equilibrage": status,
        "recommandation": recommandation
  }
  
