import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import numpy as np

def ia_prevision_demande(historique_donnees, variables_futures):
    """
    Predictit la demande future en utilisant Random Forest.
    historique_donnees : Liste de dict [{'mois': 1, 'prix': 500, 'promo': 0, 'ventes': 120}, ...]
    variables_futures : Dict {'mois': 2, 'prix': 500, 'promo': 1}
    """
    df = pd.DataFrame(historique_donnees)
    
    # Preparation des caracteristiques (Features) et de la cible (Target)
    X = df[['mois', 'prix', 'promo']]
    y = df['ventes']
    
    # Initialisation du modele (100 arbres de decision)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    
    # Entrainement du modele
    model.fit(X, y)
    
    # Prediction
    X_futur = pd.DataFrame([variables_futures])
    prediction = model.predict(X_futur)
    
    return round(prediction[0], 2)

def analyse_abc_stocks(donnees_produits):
    """
    Classe les articles selon la loi de Pareto (80/20).
    donnees_produits : Liste de dict [{'id': 'A1', 'valeur_conso': 1000000}, ...]
    """
    df = pd.DataFrame(donnees_produits)
    df = df.sort_values(by='valeur_conso', ascending=False)
    
    total_valeur = df['valeur_conso'].sum()
    df['cumul_pourcentage'] = df['valeur_conso'].cumsum() / total_valeur * 100
    
    def attribuer_classe(pct):
        if pct <= 80: return 'A'
        if pct <= 95: return 'B'
        return 'C'
    
    df['classe'] = df['cumul_pourcentage'].apply(attribuer_classe)
    return df[['id', 'classe']].to_dict(orient='records')
  
