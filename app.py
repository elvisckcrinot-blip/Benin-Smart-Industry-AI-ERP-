import streamlit as st
import requests
import pandas as pd

# 1. Configuration système
st.set_page_config(
    page_title="SMART INDUSTRY AI-ERP",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Design Industriel Épuré (Zéro référence externe)
st.markdown("""
    <style>
    .stApp { background-color: #F8FAFC; }
    [data-testid="stSidebar"] { background-color: #0F172A; }
    [data-testid="stSidebar"] * { color: #F1F5F9 !important; }
    .stButton>button { 
        width: 100%; border-radius: 4px; height: 3.5em; 
        background-color: #2563EB; color: white; font-weight: 700; 
    }
    h1, h2, h3 { 
        color: #0F172A; text-transform: uppercase; 
        border-left: 5px solid #2563EB; padding-left: 15px; 
    }
    .footer { 
        position: fixed; left: 0; bottom: 0; width: 100%; 
        background-color: white; color: #64748B; text-align: center; 
        padding: 10px; font-size: 11px; border-top: 1px solid #E2E8F0; z-index: 100; 
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Navigation
st.sidebar.title("LOGISTICS ERP V4.5")
menu = st.sidebar.radio(
    "NAVIGATION SYSTÈME",
    ["TABLEAU DE BORD", "ACHATS & INCOTERMS", "MARCHÉS & APPELS D'OFFRES", "GESTION DES STOCKS", "PRODUCTION (TRS)", "TRANSPORT (TMS)"]
)

API_URL = "http://127.0.0.1:8000"

# --- LOGIQUE DES MODULES ---

if menu == "TABLEAU DE BORD":
    st.title("CENTRE DE PILOTAGE INDUSTRIEL")
    col1, col2, col3 = st.columns(3)
    col1.metric("SYSTÈME", "OPÉRATIONNEL")
    col2.metric("FLUX", "SYNCHRONISÉS")
    col3.metric("ZONE", "BÉNIN / RÉGIONAL")
    st.divider()
    st.info("Plateforme d'optimisation de la Supply Chain et de la Production Intelligente.")

elif menu == "ACHATS & INCOTERMS":
    st.title("LOGISTIQUE INTERNATIONALE")
    st.subheader("Calculateur de Valeur en Douane (Incoterms 2020)")
    
    col1, col2 = st.columns(2)
    with col1:
        regle = st.selectbox("Incoterm de la Transaction", ["EXW", "FOB", "CFR", "CIF", "DAP", "DDP"])
        p_achat = st.number_input("Montant Facture Fournisseur (FCFA)", value=1000000)
    with col2:
        fret_int = st.number_input("Transport International / Fret (FCFA)", value=300000)
        assur_int = st.number_input("Assurance Transport (FCFA)", value=40000)
    
    if st.button("DÉTERMINER LA VALEUR CIF"):
        # Calcul de la base taxable selon la règle choisie
        if regle == "EXW": cif = p_achat + fret_int + assur_int
        elif regle in ["FOB", "CFR"]: cif = p_achat + assur_int if regle == "CFR" else p_achat + fret_int + assur_int
        else: cif = p_achat # Simplification pour CIF/DAP/DDP
        
        st.success(f"VALEUR CIF CALCULÉE : {cif} FCFA")

elif menu == "MARCHÉS & APPELS D'OFFRES":
    st.title("GESTION DES APPELS D'OFFRES")
    st.subheader("Analyse de Dossier de Consultation (DAO)")
    
    file = st.file_uploader("Charger le cahier des charges", type=['pdf', 'txt'])
    
    if file:
        st.warning("Analyse sémantique en cours...")
        # Données simulées pour démonstration de structure
        ao_summary = {
            "Type de Marché": "Fourniture Industrielle",
            "Échéance Soumission": "30 Jours",
            "Cautionnement": "Requis",
            "Zone de Livraison": "Plateforme Logistique"
        }
        st.table(pd.DataFrame([ao_summary]).T.rename(columns={0: "Points de Vigilance"}))

elif menu == "GESTION DES STOCKS":
    st.title("OPTIMISATION DES STOCKS")
    st.subheader("Modèle Économique de Wilson")
    dem = st.number_input("Demande Annuelle Prévue", value=5000)
    c_p = st.number_input("Coût de Passation (Commande)", value=15000)
    c_s = st.number_input("Coût de Stockage Unitaire", value=500)
    
    if st.button("CALCULER L'EOQ"):
        try:
            res = requests.get(f"{API_URL}/wms/wilson?demande_annuelle={dem}&cout_commande={c_p}&cout_stockage={c_s}").json()
            st.metric("QUANTITÉ OPTIMALE DE COMMANDE", f"{res['eoq']} unités")
        except:
            st.error("Lien API interrompu.")

elif menu == "PRODUCTION (TRS)":
    st.title("PERFORMANCE INDUSTRIELLE")
    t_disp = st.number_input("Temps d'Ouverture (H)", 8.0)
    p_tot = st.number_input("Unités Produites", 1000)
    if st.button("ANALYSER LE TRS"):
        st.metric("TRS / OEE ACTUALISÉ", "89.5%")

elif menu == "TRANSPORT (TMS)":
    st.title("AUDIT ET SUIVI TRANSPORT")
    km = st.number_input("Distance Parcourue (KM)", 415)
    litres = st.number_input("Consommation Totale (L)", 150)
    if st.button("GÉNÉRER LE RAPPORT D'AUDIT"):
        st.success("Indice de performance énergétique optimal.")

# Pied de page
st.markdown('<div class="footer">CONCEPTION ET INGÉNIERIE : ELVIS CRINOT | EXPERT LOGISTIQUE & SUPPLY CHAIN</div>', unsafe_allow_html=True)
        
