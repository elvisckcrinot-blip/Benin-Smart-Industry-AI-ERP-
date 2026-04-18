from fastapi import FastAPI
from core.incoterms import incoterms_data
from modules.achat.tax_benin import calculateur_douane_benin
from modules.wms.stock_ai import ia_prevision_demande, analyse_abc_stocks
from modules.tms.reverse_logistics import gestion_logistique_inverse

app = FastAPI(title="Smart Industry Benin AI-ERP")

@app.get("/")
def home():
    return {"message": "Bienvenue dans la tour de contrôle Smart Industry Bénin"}

# --- MODULE 1 : ACHATS & INCOTERMS ---
@app.get("/achats/incoterm/{code}")
def details_incoterm(code: str):
    return incoterms_data.get(code.upper(), {"erreur": "Incoterm non reconnu"})

@app.get("/achats/calcul-taxes")
def calculer_taxes(valeur_cif: float, categorie: int):
    return calculateur_douane_benin(valeur_cif, categorie)

# --- MODULE 2 : WMS (STOCKS) ---
@app.post("/wms/prevision")
def prediction_stock(donnees_historiques: list):
    # Appelle ton IA Random Forest
    prediction = ia_prevision_demande(donnees_historiques)
    return {"demande_estimee_mois_prochain": prediction}

# --- MODULE 3 : PRODUCTION & MAINTENANCE ---
@app.get("/production/alerte-machine")
def check_pannes(vibrations: float, temperature: float):
    # Logique simplifiée de maintenance préventive
    if temperature > 75 or vibrations > 0.8:
        return {"statut": "ALERTE", "action": "Maintenance immédiate requise"}
    return {"statut": "OK", "action": "Poursuivre production"}

# --- MODULE 4 : TMS & LOGISTIQUE INVERSE ---
@app.post("/tms/retour")
def gerer_retour(article_id: str, quantite: int, motif: str):
    return gestion_logistique_inverse(article_id, quantite, motif)
         
