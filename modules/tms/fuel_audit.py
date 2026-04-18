def audit_carburant(distance_km, tonnage, consommation_litres, prix_litre=650):
    """
    Analyse la consommation et calcule le cout a la tonne.
    """
    # Consommation theorique moyenne (ex: 35L/100km pour un camion charge)
    conso_aux_100 = (consommation_litres / distance_km) * 100
    
    cout_total = consommation_litres * prix_litre
    cout_par_tonne = cout_total / tonnage if tonnage > 0 else 0
    
    # Indicateur d efficacite (Litres par Tonne-Kilometre)
    efficacite = consommation_litres / (tonnage * distance_km) if (tonnage * distance_km) > 0 else 0
    
    status = "Optimise"
    if conso_aux_100 > 40: # Seuil critique de surconsommation
        status = "Surconsommation detectee"
        
    return {
        "consommation_100km": round(conso_aux_100, 2),
        "cout_carburant_total": round(cout_total, 2),
        "cout_par_tonne": round(cout_par_tonne, 2),
        "indice_efficacite": f"{efficacite:.4f} L/t.km",
        "diagnostic": status,
        "optimisation": "Verifier la pression des pneus ou le mode de conduite si surconso."
  }
  
