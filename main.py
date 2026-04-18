from fastapi import FastAPI
from core.incoterms import incoterms_data
from modules.achat.tax_benin import calculer_fiscalite_benin
from modules.achat.simulateur import comparer_offres_incoterms
from modules.achat.ao_analyzer import scanner_ao

app = FastAPI(title="Benin Smart Industry AI-ERP")

@app.get("/")
def read_root():
    return {"status": "Online", "system": "Smart Industry Benin"}

# --- MODULE 1 : ACHATS & MARCHES ---

@app.get("/achats/incoterms")
def get_all_incoterms():
    """Renvoie la base de donnees complete des Incoterms par familles"""
    return incoterms_data

@app.get("/achats/simulation-taxe")
def simulation_taxe(valeur_cif: float, categorie: int):
    """Calcule la fiscalite portuaire au Benin (TEC, TVA, PCS, PCC)"""
    return calculer_fiscalite_benin(valeur_cif, categorie)

@app.get("/achats/comparatif")
def get_comparatif(prix: float, fret: float, assurance: float, cat: int):
    """Compare financierement les scenarios d achat (CIF vs DDP)"""
    return comparer_offres_incoterms(prix, fret, assurance, cat)

@app.post("/achats/analyser-ao")
def post_analyse_ao(document_text: str, budget: float):
    """Scan l appel d offres pour detecter risques et conformite"""
    return scanner_ao(document_text, budget)

# --- MODULE 2 : WMS (STOCKS) ---

@app.get("/wms/wilson")
def calcul_eoq(demande_annuelle: float, cout_commande: float, cout_stockage: float):
    """Calcule la quantite economique de commande (Wilson)"""
    import math
    if cout_stockage <= 0:
        return {"error": "Cout de stockage doit etre superieur a zero"}
    q_opti = math.sqrt((2 * demande_annuelle * cout_commande) / cout_stockage)
    return {"eoq": round(q_opti, 2)}

# --- MODULE 3 : PRODUCTION ---

@app.get("/production/maintenance")
def maintenance_predictive(vibration: float, temperature: float):
    """Analyse les donnees capteurs pour prevenir les pannes"""
    status = "Normal"
    action = "Continuer la production"
    if vibration > 0.8 or temperature > 75:
        status = "Alerte maintenance"
        action = "Inspection immediate requise"
    return {
        "machine_status": status,
        "recommandation": action
    }
    
