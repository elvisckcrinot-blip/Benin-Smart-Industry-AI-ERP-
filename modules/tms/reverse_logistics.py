def gestion_retours(id_bordereau, motif, etat_produit):
    """
    Determine si le produit retourne doit etre recycle ou remis en stock.
    """
    action = "Inspection requise"
    if motif == "Defectueux":
        action = "Transfert vers zone de recyclage/rebut"
    elif motif == "Refus client" and etat_produit == "Intact":
        action = "Reintegration au stock (Controle qualite)"
        
    return {
        "bordereau_origine": id_bordereau,
        "decision": action,
        "logistique_inverse": "Planifier ramassage lors du prochain passage a vide."
    }
  
