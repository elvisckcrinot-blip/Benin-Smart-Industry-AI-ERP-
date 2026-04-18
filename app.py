import streamlit as st
import requests
import pandas as pd

# 1. Configuration de la page (Doit être la toute première commande)
st.set_page_config(
    page_title="BENIN SMART INDUSTRY - ERP",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Style Industriel Épuré (Optimisé pour éviter les erreurs de chargement)
st.markdown("""
    <style>
    .stApp { background-color: #F8FAFC; }
    
    /* Sidebar */
    [data-testid="stSidebar"] { background-color: #0F172A; }
    [data-testid="stSidebar"] * { color: #F1F5F9 !important; }

    /* Boutons */
    .stButton>button {
        width: 100%; border-radius: 4px; height: 3.5em;
        background-color: #2563EB; color: white; border: none;
        font-weight: 700; text-transform: uppercase;
    }
    
    /* Titres */
    h1, h2, h3 { 
        color: #0F172A; text-transform: uppercase;
        border-left: 5px solid #2563EB; padding-left: 15px; 
    }

    /* Footer */
    .footer {
        position: fixed; left: 0; bottom: 0; width: 100%;
        background-color: white; color: #64748B;
        text-align: center; padding: 10px; font-size: 11px;
        border-top: 1px solid #E2E8F0; z-index: 100;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Pied de page permanent
st.markdown('<div class="footer">CONCEPTION ET INGENIERIE : ELVIS CRINOT | SOLUTIONS LOGISTIQUES 4.0</div>', unsafe_allow_html=True)

# 4. Configuration API
API_URL = "http://127.0.0.1:8000"

# 5. Navigation Latérale
st.sidebar.title("SYSTEME ERP")
menu = st.sidebar.radio(
    "NAVIGATION",
    ["DASHBOARD", "ACHATS/FISCALITE", "STOCKS/FLUX", "PRODUCTION/TRS", "TRANSPORT/TMS", "MAINTENANCE IA"]
)

# 6. Logique des Modules
if menu == "DASHBOARD":
    st.title("CENTRE DE CONTROLE")
    st.write("Surveillance opérationnelle du réseau Bénin.")
    
    c1, c2, c3 = st.columns(3)
    c1.metric("SERVEUR", "ONLINE")
    c2.metric("VERSION", "4.0.0")
    c3.metric("ZONE", "BOHICON")
    
    st.divider()
    st.info("Système prêt pour l'audit industriel.")

elif menu == "ACHATS/FISCALITE":
    st.title("SIMULATEUR FISCAL")
    valeur = st.number_input("VALEUR CIF (FCFA)", value=1000000)
    cat = st.selectbox("CATEGORIE (TEC)", [1, 2, 3])
    
    if st.button("CALCULER TAXES"):
        try:
            res = requests.get(f"{API_URL}/achats/simulation-taxe?valeur_cif={valeur}&categorie={cat}").json()
            st.table(pd.DataFrame([res]).T.rename(columns={0: "DETAIL"}))
        except:
            st.error("Serveur API non détecté. Lancez Uvicorn.")

elif menu == "PRODUCTION/TRS":
    st.title("PERFORMANCE ATELIER")
    col1, col2 = st.columns(2)
    t_dispo = col1.number_input("TEMPS DISPO (H)", value=8.0)
    t_arret = col2.number_input("TEMPS ARRET (H)", value=1.0)
    p_tot = col1.number_input("TOTAL PRODUIT", value=1000)
    p_conf = col2.number_input("CONFORMES", value=950)
    
    if st.button("CALCULER TRS"):
        try:
            res = requests.get(f"{API_URL}/production/calcul-trs?t_dispo={t_dispo}&t_arret={t_arret}&p_totales={p_tot}&p_conformes={p_conf}").json()
            st.metric("TRS FINAL", f"{res['oee']}%")
        except:
            st.error("Erreur de liaison API.")

elif menu == "TRANSPORT/TMS":
    st.title("AUDIT CARBURANT")
    km = st.number_input("KM REELS", value=415)
    tns = st.number_input("TONNAGE", value=25.0)
    lts = st.number_input("LITRES", value=150.0)
    
    if st.button("VALIDER AUDIT"):
        try:
            res = requests.get(f"{API_URL}/tms/audit-carburant?km={km}&tonnes={tns}&litres={lts}").json()
            st.subheader(f"DIAGNOSTIC : {res['diagnostic']}")
            st.info(f"STRATEGIE : {res['optimisation']}")
        except:
            st.error("Liaison API impossible.")
    
