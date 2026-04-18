import pandas as pd
from datetime import datetime
import io

def tri_stocks_fefo(inventaire):
    """
    Trie les articles selon la date d expiration (First-Expired, First-Out).
    inventaire : Liste de dict [{'id': 'P1', 'expiration': '2026-05-20'}, ...]
    """
    return sorted(inventaire, key=lambda x: datetime.strptime(x['expiration'], '%Y-%m-%d'))

def tri_stocks_fifo(inventaire):
    """
    Trie les articles selon la date d entree (First-In, First-Out).
    inventaire : Liste de dict [{'id': 'P1', 'date_entree': '2026-04-01'}, ...]
    """
    return sorted(inventaire, key=lambda x: datetime.strptime(x['date_entree'], '%Y-%m-%d'))

def appliquer_priorite_abc(donnees_abc, inventaire_trie):
    """
    Fusionne le classement ABC avec le tri operationnel (FIFO/FEFO).
    Assure que les articles de classe A prioritaires sont identifies en haut de liste.
    """
    # Creer un dictionnaire de correspondance ID -> Classe
    mapping_abc = {item['id']: item['classe'] for item in donnees_abc}
    
    for article in inventaire_trie:
        article['priorite_abc'] = mapping_abc.get(article['id'], 'C')
        
    # On remonte les articles de classe A
    return sorted(inventaire_trie, key=lambda x: x['priorite_abc'])

def alerte_peremption(inventaire, jours_limite=30):
    """
    Identifie les produits qui periment dans un delai critique.
    """
    alertes = []
    aujourdhui = datetime.now()
    
    for article in inventaire:
        date_exp = datetime.strptime(article['expiration'], '%Y-%m-%d')
        jours_restants = (date_exp - aujourdhui).days
        
        if jours_restants <= jours_limite:
            alertes.append({
                "id": article["id"],
                "jours_restants": jours_restants,
                "niveau": "CRITIQUE" if jours_restants < 7 else "ATTENTION"
            })
    return alertes

def generer_export_stock(inventaire_trie, nom_entrepot="Bohicon"):
    """
    Convertit l inventaire trie en un fichier Excel pret pour le telechargement.
    """
    df = pd.DataFrame(inventaire_trie)
    
    # Ajout d une colonne horodatage pour la tracabilite
    df['date_extraction'] = datetime.now().strftime('%Y-%m-%d %H:%M')
    df['entrepot'] = nom_entrepot
    
    # Creation d un flux memoire pour le fichier Excel
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Etat_de_Stock')
        
    return output.getvalue()
    
