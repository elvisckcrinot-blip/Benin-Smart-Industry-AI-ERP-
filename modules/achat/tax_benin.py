def calculer_fiscalite_benin(valeur_cif, categorie_produit):
    # Categories TEC CEDEAO : 0 (0%), 1 (5%), 2 (10%), 3 (20%)
    taux_tec = {0: 0.0, 1: 0.05, 2: 0.10, 3: 0.20}
    
    dd = valeur_cif * taux_tec.get(categorie_produit, 0.20)
    pcs = valeur_cif * 0.008 # Prelevement Communautaire de Solidarite
    pcc = valeur_cif * 0.002 # Prelevement Communautaire de la CEDEAO
    
    base_tva = valeur_cif + dd + pcs + pcc
    tva = base_tva * 0.18
    
    total_taxes = dd + pcs + pcc + tva
    return {
        "droits_douane": round(dd, 2),
        "taxes_communautaires": round(pcs + pcc, 2),
        "tva": round(tva, 2),
        "total_douane": round(total_taxes, 2),
        "cout_total_rendu": round(valeur_cif + total_taxes, 2)
  }
  
