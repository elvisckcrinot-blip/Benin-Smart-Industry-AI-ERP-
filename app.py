import streamlit as st
import pandas as pd

# Importations des modules metiers selon votre structure
try:
    from core.incoterms import calculer_comparatif_incoterms
    from modules.achat.tax_benin import calculer_taxes_cotonou
    from modules.wms.inventory_logic import calcul_wilson_eoq
    from modules.tms.fuel_audit import analyser_consommation
except ImportError:
    # Rappel si les fichiers sont encore vides ou __init__.py manquants
    pass

# Configuration de la page
st.set_page_config(
    page_title="SMART INDUSTRY ERP - SOLUTIONS LOGISTIQUES 4.0",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Style Industriel Neutre
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

# Navigation
st.sidebar.title("ERP INDUSTRIEL V5.0")
module = st.sidebar.radio(
    "SELECTIONNER UN MODULE",
    ["1. ACHATS ET MARCHES", "2. WMS (STOCKS)", "3. PRODUCTION", "4. TMS (TRANSPORT)"]
)

# MODULE 1 : ACHATS ET MARCHES
if module == "1. ACHATS ET MARCHES":
    st.title("MODULE 1 : ACHATS ET MARCHES (SOURCING)")
    tab1, tab2, tab3 = st.tabs(["ANALYSE APPELS D'OFFRES", "SIMULATEUR INCOTERMS", "TAXES ET DEDOUANEMENT"])
    
    with tab1:
        st.subheader("SCANNER DE DOCUMENTS (AO_ANALYZER)")
        st.file_uploader("Importer le cahier des charges (DAO)", type=['pdf', 'txt'])
    
    with tab2:
        st.subheader("MOTEUR DE CALCUL MULTI-INCOTERMS")
        col1, col2 = st.columns(2)
        with col1:
            famille = st.selectbox("Famille Incoterm", ["Groupe E (Depart)", "Groupe F", "Groupe C", "Groupe D"])
            prix_base = st.number_input("Prix de base (FCFA)", value=10000000)
        with col2:
            fret = st.number_input("Fret estime (FCFA)", value=1500000)
            assurance = st.number_input("Assurance (FCFA)", value=100000)
        
        if st.button("GENERER LE TABLEAU COMPARATIF"):
            st.info("Traitement via core/incoterms.py")

    with tab3:
        st.subheader("CALCULATEUR DE TAXES BENIN (PORT DE COTONOU)")
        cif = st.number_input("Valeur CIF (FCFA)", value=12000000)
        if st.button("CALCULER DROITS ET TAXES"):
            st.info("Traitement via modules/achat/tax_benin.py")

# MODULE 2 : WMS (STOCKS)
elif module == "2. WMS (STOCKS)":
    st.title("MODULE 2 : GESTION INTELLIGENTE DES STOCKS")
    tab1, tab2, tab3 = st.tabs(["GESTION ABC / ALERTES", "PREVISION (IA)", "AJUSTEMENT DYNAMIQUE"])
    
    with tab2:
        st.subheader("IA : ANTICIPATEUR DE DEMANDE (RANDOM FOREST)")
        st.write("Analyse basee sur la saisonnalite du reseau Benin.")

# MODULE 3 : PRODUCTION
elif module == "3. PRODUCTION":
    st.title("MODULE 3 : PRODUCTION (L'USINE)")
    tab1, tab2, tab3 = st.tabs(["FLUX (JAT)", "MAINTENANCE PREDICTIVE", "RENTABILITE"])

# MODULE 4 : TMS (TRANSPORT)
elif module == "4. TMS (TRANSPORT)":
    st.title("MODULE 4 : TMS - TRANSPORT ET LIVRAISON")
    tab1, tab2, tab3 = st.tabs(["CHARGEMENT", "TRACKING (BENIN)", "AUDIT CARBURANT"])
    
    with tab3:
        st.subheader("AUDIT CONSOMMATION / TONNAGE")
        st.number_input("Distance (KM)", value=415)
        st.number_input("Tonnage (T)", value=25.0)
        if st.button("VALIDER L'AUDIT"):
            st.info("Traitement via modules/tms/fuel_audit.py")

# Pied de page
st.markdown('<div class="footer">CONCEPTION ET INGENIERIE : ELVIS CRINOT | SOLUTIONS LOGISTIQUES 4.0</div>', unsafe_allow_html=True)
