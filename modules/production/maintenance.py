import pandas as pd
from sklearn.ensemble import IsolationForest

def detecter_anomalie_machine(donnees_capteurs):
    """
    Utilise l algorithme Isolation Forest pour detecter des comportements 
    anormaux avant la panne.
    donnees_capteurs : Liste de dict [{'vibration': 0.5, 'temp': 40, 'pression': 2}, ...]
    """
    df = pd.DataFrame(donnees_capteurs)
    
    # Initialisation du modele de detection d anomalies
    model = IsolationForest(contamination=0.1, random_state=42)
    
    # Entrainement et prediction (-1 pour anomalie, 1 pour normal)
    df['statut'] = model.fit_predict(df)
    
    anomalies = df[df['statut'] == -1]
    
    return {
        "nb_anomalies_detectees": len(anomalies),
        "alerte": len(anomalies) > 0,
        "details": anomalies.to_dict(orient='records')
    }

def calculer_oee(temps_disponible, temps_arret, pieces_totales, pieces_conformes):
    """
    Calcule le Taux de Rendement Synthetique (TRS / OEE).
    Indicateur cle pour l efficacite de l usine.
    """
    if temps_disponible <= 0: return 0
    
    disponibilite = (temps_disponible - temps_arret) / temps_disponible
    performance = pieces_totales / (temps_disponible - temps_arret) if (temps_disponible - temps_arret) > 0 else 0
    qualite = pieces_conformes / pieces_totales if pieces_totales > 0 else 0
    
    trs = disponibilite * performance * qualite
    
    return {
        "disponibilite": round(disponibilite * 100, 2),
        "performance": round(performance * 100, 2),
        "qualite": round(qualite * 100, 2),
        "trs_global": round(trs * 100, 2)
  }
  
