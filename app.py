import streamlit as st
import requests
import pandas as pd

# 1. Configuration de la page
st.set_page_config(
    page_title="BENIN SMART INDUSTRY - ERP SYSTEM",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Injection CSS (Correction du paramètre unsafe_allow_html)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400;700&family=Inter:wght@400;700&display=swap');

    .stApp {
        background-color: #F8FAFC;
        font-family: 'Inter', sans-serif;
    }

    [data-testid="stSidebar"] {
        background-color: #0F172A;
        border-right: 1px solid #1E293B;
    }
    
    [data-testid="stSidebar"] .stText, [data-testid="stSidebar"] label {
        color: #F1F5F9 !important;
        font-weight: 600;
        text-transform: uppercase;
        font-size: 0.8rem;
    }

    .stButton>button {
        width: 100%;
        border-radius: 4px;
        height: 3.5em;
        background-color: #2563EB;
        color: white;
        border: none;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }

    .stButton>button:hover {
        background-color: #1E40AF;
    }

    h1, h2, h3 {
        color: #0F172A;
        font-weight: 800;
        text-transform: uppercase;
        border-left: 5px solid #2563EB;
        padding-left: 15px;
    }

    [data-testid="stMetricValue"] {
        font-family: 'Roboto Mono', monospace;
        color: #2563EB;
    }
    
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: white;
        color: #64748B;
        text-align: center;
        padding: 10px;
        font-size: 12px;
        border-top: 1px solid #E2E8F0;
        z-index: 100;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Pied de page
st.markdown('<div class="footer">CONCEPTION ET INGENIERIE : ELVIS CRINOT | SOLUTIONS LOGISTIQUES 4.0</div>', unsafe_allow_html=True)

# 4. Configuration API
API_URL = "http://127.0.0.1:8000"

# 5. Navigation
st.sidebar.markdown("### SYSTEME DE PILOTAGE")
menu = st.sidebar.radio(
    "SELECTION DU MODULE",
    ["TABLEAU DE BORD", "ACHATS ET FISCALITE", "STOCKS ET FLUX", "PRODUCTION ET TRS", "TRANSPORT ET TMS", "INTELLIGENCE ARTIFICIELLE"]
)

# 6. Logique des Modules
if menu == "TABLEAU DE BORD":
    st.title("CENTRE DE CONTROLE INDUSTRIEL")
    st.write("Surveillance des flux et performance opérationnelle du réseau Bénin.")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("ETAT DU SERVEUR", "OPERATIONNEL", delta="LATENCE < 20ms")
    col2.metric("VERSION SYSTEME", "4.0.0", delta="STABLE")
    col3.metric("ZONE GEOGRAPHIQUE", "COTONOU / BOHICON")
    
    st.divider()
    st.info("Le système est synchronisé. Prêt pour l'audit industriel.")

elif menu == "ACHATS ET FISCALITE":
    st.title("SIMULATEUR DE FISCALITE DOUANIERE")
    valeur_cif = st.number_input("VALEUR CIF (FCFA)", value=1000000, step=10000)
    categorie = st.selectbox("CATEGORIE TARIFAIRE (TEC)", [1, 2, 3])
    
    if st.button("EXECUTER L'ANALYSE FISCALE"):
        try:
            res = requests.get(f"{API_URL}/achats/simulation-taxe?valeur_cif={valeur_cif}&categorie={categorie}").json()
            st.table(pd.DataFrame([res]).T.rename(columns={0: "VALEURS"}))
        except:
            st.error("ERREUR : Le serveur Backend (uvicorn) n'est pas lancé.")

elif menu == "PRODUCTION ET TRS":
    st.title("PERFORMANCE DE PRODUCTION")
    c1, c2 = st.columns(2)
    t_dispo = c1.number_input("TEMPS DISPO (H)", value=8.0)
    t_arret = c2.number_input("TEMPS D'ARRÊT (H)", value=1.0)
    p_totales = c1.number_input("TOTAL PRODUIT", value=1000)
    p_conformes = c2.number_input("CONFORMES", value=950)
    
    if st.button("CALCULER LE TRS"):
        try:
            res = requests.get(f"{API_URL}/production/calcul-trs?t_dispo={t_dispo}&t_arret={t_arret}&p_totales={p_totales}&p_conformes={p_conformes}").json()
            st.metric("TAUX TRS / OEE", f"{res['oee']}%")
        except:
            st.error("ERREUR DE LIAISON API")

elif menu == "TRANSPORT ET TMS":
    st.title("AUDIT ET TRAÇABILITE TRANSPORT")
    km = st.number_input("KILOMETRAGE REEL", value=415)
    tonnes = st.number_input("TONNAGE", value=25.0)
    litres = st.number_input("LITRES CONSOMMES", value=150.0)
    
    if st.button("VALIDER L'AUDIT CARBURANT"):
        try:
            res = requests.get(f"{API_URL}/tms/audit-carburant?km={km}&tonnes={tonnes}&litres={litres}").json()
            st.subheader(f"DIAGNOSTIC : {res['diagnostic']}")
            st.info(f"STRATEGIE : {res['optimisation']}")
        except:
            st.error("ERREUR API")
