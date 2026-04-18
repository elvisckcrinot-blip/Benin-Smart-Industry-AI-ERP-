from fastapi import FastAPI
from core.incoterms import incoterms_data
from modules.achat.tax_benin import calculer_fiscalite_benin

app = FastAPI(title="Benin Smart Industry AI-ERP")

@app.get("/")
def read_root():
    return {"status": "Online", "system": "Smart Industry Benin"}

# MODULE 1 : ACHATS
@app.get("/achats/incoterms")
def get_all_incoterms():
    return incoterms_data

@app.get("/achats/simulation-taxe")
def simulation_taxe(valeur_cif: float, categorie: int):
    return calculer_fiscalite_benin(valeur_cif, categorie)

# MODULE 2 : WMS
@app.get("/wms/wilson")
def calcul_eoq(demande_annuelle: float, cout_commande: float, cout_stockage: float):
    import math
    if cout_stockage == 0: return {"error": "Cout stockage nul"}
    q_opti = math.sqrt((2 * demande_annuelle * cout_commande) / cout_stockage)
    return {"eoq": round(q_opti, 2)}

# MODULE 3 : PRODUCTION
@app.get("/production/maintenance")
def maintenance_predictive(vibration: float, temperature: float):
    status = "Normal"
    if vibration > 0.8 or temperature > 75:
        status = "Alerte maintenance"
    return {"machine_status": status}
    
