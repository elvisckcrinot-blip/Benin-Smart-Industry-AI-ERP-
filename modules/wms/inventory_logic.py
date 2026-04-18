from datetime import datetime

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
        
    # On remonte les articles de classe A qui arrivent a expiration
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
