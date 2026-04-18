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
from modules.production.flux_manager import (
    calculer_cout_revient, 
    gestion_flux_pull_jat, 
    gestion_flux_pousse_push, 
    gestion_flux_synchrone
)

app = FastAPI(title="Benin Smart Industry AI-ERP")

@app.get("/")
def read_root():
    return {"status": "Online", "system": "Smart Industry Benin", "version": "3.0"}

# --- MODULE 1 : ACHATS & MARCHÉS ---

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
    headers = {'Content-Disposition': f'attachment; filename="inventaire_{entrepot}.xlsx"'}
    return Response(content=excel_data, headers=headers, media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

@app.get("/wms/wilson")
def calcul_eoq(demande_annuelle: float, cout_commande: float, cout_stockage: float):
    import math
    if cout_stockage <= 0: return {"error": "Cout de stockage nul"}
    q_opti = math.sqrt((2 * demande_annuelle * cout_commande) / cout_stockage)
    return {"eoq": round(q_opti, 2)}

# --- MODULE 3 : PRODUCTION & MAINTENANCE ---

@app.post("/production/analyse-anomalies")
def post_analyse_anomalies(donnees_capteurs: list):
    return detecter_anomalie_machine(donnees_capteurs)

@app.get("/production/calcul-trs")
def get_trs(t_dispo: float, t_arret: float, p_totales: int, p_conformes: int):
    return calculer_oee(t_dispo, t_arret, p_totales, p_conformes)

@app.get("/production/cout-revient")
def get_cout_revient(matiere: float, t_machine: float, taux_h: float, mo: float):
    """Calcul du cout de revient complet incluant frais fixes"""
    return calculer_cout_revient(matiere, t_machine, taux_h, mo)

@app.get("/production/flux-decision")
def get_flux_decision(type_flux: str, demande: float, stock: float, capacite: float):
    """Point d entree pour le simulateur de strategie (Push/Pull/Synchrone)"""
    if type_flux == "pull":
        return gestion_flux_pull_jat(demande, stock, 1.5) # 1.5 min par unite par defaut
    elif type_flux == "push":
        return gestion_flux_pousse_push(demande, 10, capacite) # Stock de securite de 10
    else:
        return gestion_flux_synchrone(demande, capacite)
    
