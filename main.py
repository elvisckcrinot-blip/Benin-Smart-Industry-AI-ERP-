from fastapi import FastAPI, Response
from core.incoterms import incoterms_data
from modules.achat.tax_benin import calculer_fiscalite_benin
from modules.achat.simulateur import comparer_offres_incoterms
from modules.achat.ao_analyzer import scanner_ao
from modules.wms.stock_ai import ia_prevision_demande, analyse_abc_stocks
from modules.wms.inventory_logic import (
    tri_stocks_fefo, 
    tri_stocks_fifo, 
    alerte_peremption, 
    generer_export_stock,
    appliquer_priorite_abc
)
from modules.production.maintenance import detecter_anomalie_machine, calculer_oee

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

# --- MODULE 2 : WMS (STOCKS, IA & LOGIQUE) ---

@app.post("/wms/prevision-demande")
def post_prevision_stock(historique: list, futur: dict):
    prediction = ia_prevision_demande(historique, futur)
    return {"demande_estimee": prediction}

@app.post("/wms/analyse-abc")
def post_analyse_abc(donnees_produits: list):
    return analyse_abc_stocks(donnees_produits)

@app.post("/wms/flux-fefo")
def get_flux_fefo(inventaire: list, donnees_abc: list = None):
    stock_trie = tri_stocks_fefo(inventaire)
    if donnees_abc:
        stock_trie = appliquer_priorite_abc(donnees_abc, stock_trie)
    return stock_trie

@app.post("/wms/alertes")
def get_alertes_stock(inventaire: list, jours: int = 30):
    return alerte_peremption(inventaire, jours)

@app.post("/wms/export-excel")
def export_inventaire(inventaire: list, entrepot: str = "Bohicon"):
    excel_data = generer_export_stock(inventaire, entrepot)
    headers = {
        'Content-Disposition': f'attachment; filename="inventaire_{entrepot}.xlsx"'
    }
    return Response(
        content=excel_data, 
        headers=headers, 
        media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

@app.get("/wms/wilson")
def calcul_eoq(demande_annuelle: float, cout_commande: float, cout_stockage: float):
    import math
    if cout_stockage <= 0:
        return {"error": "Cout de stockage doit etre superieur a zero"}
    q_opti = math.sqrt((2 * demande_annuelle * cout_commande) / cout_stockage)
    return {"eoq": round(q_opti, 2)}

# --- MODULE 3 : PRODUCTION ---

@app.post("/production/analyse-anomalies")
def post_analyse_anomalies(donnees_capteurs: list):
    """Detection d anomalies par IA (Isolation Forest)"""
    return detecter_anomalie_machine(donnees_capteurs)

@app.get("/production/calcul-trs")
def get_trs(t_dispo: float, t_arret: float, p_totales: int, p_conformes: int):
    """Calcul du Taux de Rendement Synthetique (OEE)"""
    return calculer_oee(t_dispo, t_arret, p_totales, p_conformes)

@app.get("/production/alerte-basique")
def maintenance_basique(vibration: float, temperature: float):
    """Analyse rapide par seuils critiques"""
    status = "Normal"
    action = "Continuer la production"
    if vibration > 0.8 or temperature > 75:
        status = "Alerte maintenance"
        action = "Inspection immediate requise"
    return {
        "machine_status": status,
        "recommandation": action
    }
    
