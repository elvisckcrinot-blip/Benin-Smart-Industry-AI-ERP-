from datetime import datetime

# Base de donnees simplifiee des distances (en km) depuis Glo-Djigbe/Cotonou
DISTANCES_BENIN = {
    "Bohicon": 125,
    "Parakou": 415,
    "Malanville": 735,
    "Naititingou": 600,
    "Hillacondji": 100,
    "Seme": 40
}

def suivre_etape_livraison(id_voyage, etape_actuelle):
    """
    Met a jour le statut du bordereau de livraison.
    Etapes : Chargement -> En route -> Docking -> Dechargement -> Livre
    """
    horodatage = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return {
        "voyage_id": id_voyage,
        "statut": etape_actuelle.upper(),
        "derniere_mise_a_jour": horodatage,
        "message": f"Le vehicule est actuellement en phase de {etape_actuelle}."
    }

def estimer_temps_trajet(ville_destination, vitesse_moyenne=60):
    """
    Estime le temps de trajet pour les livraisons inter-villes.
    """
    distance = DISTANCES_BENIN.get(ville_destination, 0)
    if distance == 0: return {"error": "Destination non repertoriee"}
    
    temps_heures = distance / vitesse_moyenne
    return {
        "destination": ville_destination,
        "distance_km": distance,
        "temps_estime_h": round(temps_heures, 2),
        "conseil_securite": "Attention aux zones de travaux sur l axe Inter-Etat."
  }
  
