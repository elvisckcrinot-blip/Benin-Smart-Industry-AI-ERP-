from fastapi import FastAPI
from core.incoterms import incoterms_data
from modules.achat.tax_benin import calculer_fiscalite_benin
from modules.achat.simulateur import comparer_offres_incoterms
from modules.achat.ao_analyzer import scanner_ao
from modules.wms.stock_ai import ia_prevision_demande, analyse_abc_stocks

app = FastAPI(title="Benin Smart Industry AI-ERP")

@app.get("/")
def read_root():
    return {"status": "Online", "system": "Smart Industry Benin"}

# --- MODULE 1 : ACHATS & MARCHES ---

@app.get("/achats/incoterms")
def get_all_incoterms():
    return incoterms_data

@app.get("/achats/simulation-taxe")
def simulation_taxe(valeur_cif: float, categorie: int):
    return calculer_fiscalite_benin(valeur_cif, categorie)

@app.get("/achats/comparatif")
def get_comparatif(prix: float, fret: float, assurance: float, cat: int):
    return comparer_offres_incoterms(prix, fret, assurance, cat)

@app.post("/achats/analyser-ao")
def post_analyse_ao(document_text: str, budget: float):
    return scanner_ao(document_text, budget)

# --- MODULE 2 : WMS (STOCKS & IA) ---

@app.post("/wms/prevision-demande")
def post_prevision_stock(historique: list, futur: dict):
    """Calcule la demande future via Random Forest"""
    prediction = ia_prevision_demande(historique, futur)
    return {"demande_estimee": prediction}

@app.post("/wms/analyse-abc")
def post_analyse_abc(donnees_produits: list):
    """Classe les articles en categories A, B ou C"""
    return analyse_abc_stocks(donnees_produits)

@app.get("/wms/wilson")
def calcul_eoq(demande_annuelle: float, cout_commande: float, cout_stockage: float):
    import math
    if cout_stockage <= 0:
        return {"error": "Cout de stockage doit etre superieur a zero"}
    q_opti = math.sqrt((2 * demande_annuelle * cout_commande) / cout_stockage)
    return {"eoq": round(q_opti, 2)}

# --- MODULE 3 : PRODUCTION ---

@app.get("/production/maintenance")
def maintenance_predictive(vibration: float, temperature: float):
    status = "Normal"
    action = "Continuer la production"
    if vibration > 0.8 or temperature > 75:
        status = "Alerte maintenance"
        action = "Inspection immediate requise"
    return {
        "machine_status": status,
        "recommandation": action
          }
