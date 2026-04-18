import streamlit as st
import requests
import pandas as pd

# Configuration de la page
st.set_page_config(
    page_title="BENIN SMART INDUSTRY - ERP SYSTEM",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- INJECTION CSS POUR DESIGN INDUSTRIEL ---
st.markdown("""
    <style>
    /* Importation d'une police plus technique */
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400;700&family=Inter:wght@400;700&display=swap');

    /* Fond de l'application */
    .stApp {
        background-color: #F8FAFC;
        font-family: 'Inter', sans-serif;
    }

    /* Barre latérale (Sidebar) */
    [data-testid="stSidebar"] {
        background-color: #0F172A;
        border-right: 1px solid #1E293B;
    }
    [data-testid="stSidebar"] .stText, [data-testid="stSidebar"] label {
        color: #F1F5F9 !important;
        font-weight: 600;
        text-transform: uppercase;
        font-size: 0.8rem;
        letter-spacing: 0.05rem;
    }

    /* Boutons de commande */
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
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #1E40AF;
        border: none;
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
    }

    /* En-têtes et Titres */
    h1, h2, h3 {
        color: #0F172A;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: -0.02em;
        border-left: 5px solid #2563EB;
        padding-left: 15px;
    }

    /* Métriques */
    [data-testid="stMetricValue"] {
        font-family: 'Roboto Mono', monospace;
        color: #2563EB;
        font-weight: 700;
    }
    
    /* Pied de page personnalisé */
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
        font-weight: 500;
        z-index: 100;
    }
    </style>
    """, unsafe_allow_path=True)

# --- CONFIGURATION API ---
API_URL = "http://127.0.0.1:8000"

# --- NAVIGATION ---
st.sidebar.markdown("### SYSTEME DE PILOTAGE")
menu = st.sidebar.radio(
    "SELECTION DU MODULE",
    ["TABLEAU DE BORD", "ACHATS ET FISCALITE", "STOCKS ET FLUX", "PRODUCTION ET TRS", "TRANSPORT ET TMS", "INTELLIGENCE ARTIFICIELLE"]
)

# --- PIED DE PAGE ---
st.markdown('<div class="footer">CONCEPTION ET INGENIERIE : ELVIS CRINOT | SOLUTIONS LOGISTIQUES 4.0</div>', unsafe_allow_path=True)

# --- LOGIQUE DES MODULES ---

if menu == "TABLEAU DE BORD":
    st.title("CENTRE DE CONTROLE INDUSTRIEL")
    st.write("Surveillance des flux et performance opérationnelle du réseau Bénin.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("ETAT DU SERVEUR", "OPERATIONNEL", delta="LATENCE < 20ms")
    with col2:
        st.metric("VERSION SYSTEME", "4.0.0", delta="STABLE")
    with col3:
        st.metric("ZONE GEOGRAPHIQUE", "COTONOU / BOHICON")
    
    st.divider()
    st.subheader("NOTES DE MISE A JOUR")
    st.info("Le système intègre désormais les protocoles d'audit de carburant et la gestion prédictive de la maintenance.")

elif menu == "ACHATS ET FISCALITE":
    st.title("SIMULATEUR DE FISCALITE DOUANIERE")
    valeur_cif = st.number_input("VALEUR CIF (FCFA)", value=1000000, step=10000)
    categorie = st.selectbox("CATEGORIE TARIFAIRE (TEC)", [1, 2, 3], help="Catégorisation selon le Tarif Extérieur Commun")
    
    if st.button("EXECUTER L'ANALYSE FISCALE"):
        try:
            res = requests.get(f"{API_URL}/achats/simulation-taxe?valeur_cif={valeur_cif}&categorie={categorie}").json()
            st.subheader("RESULTATS DE L'ESTIMATION")
            st.table(pd.DataFrame([res]).T.rename(columns={0: "VALEURS"}))
        except:
            st.error("ERREUR DE LIAISON AVEC LE SERVEUR BACKEND")

elif menu == "STOCKS ET FLUX":
    st.title("GESTION DES FLUX ET ENTREPOSAGE")
    st.subheader("QUANTITE ECONOMIQUE DE COMMANDE (FORMULE DE WILSON)")
    
    col1, col2 = st.columns(2)
    with col1:
        demande = st.number_input("DEMANDE ANNUELLE PREVISIONNELLE", value=5000)
        cout_c = st.number_input("COUT DE PASSATION PAR COMMANDE", value=15000)
    with col2:
        cout_s = st.number_input("COUT UNITAIRE DE POSSESSION", value=500)
    
    if st.button("OPTIMISER LE STOCK"):
        res = requests.get(f"{API_URL}/wms/wilson?demande_annuelle={demande}&cout_commande={cout_c}&cout_stockage={cout_s}").json()
        st.metric("QUANTITE OPTIMALE (EOQ)", f"{res['eoq']} UNITES")

elif menu == "PRODUCTION ET TRS":
    st.title("PERFORMANCE DE PRODUCTION")
    col1, col2 = st.columns(2)
    with col1:
        t_dispo = st.number_input("TEMPS DE DISPONIBILITE THEORIQUE (H)", value=8.0)
        p_totales = st.number_input("QUANTITE TOTALE PRODUITE", value=1000)
    with col2:
        t_arret = st.number_input("TEMPS D'ARRÊT NON PLANIFIE (H)", value=1.0)
        p_conformes = st.number_input("QUANTITE DE PRODUITS CONFORMES", value=950)
    
    if st.button("CALCULER LE TAUX DE RENDEMENT SYNTHETIQUE"):
        res = requests.get(f"{API_URL}/production/calcul-trs?t_dispo={t_dispo}&t_arret={t_arret}&p_totales={p_totales}&p_conformes={p_conformes}").json()
        st.metric("VALEUR TRS / OEE", f"{res['oee']}%")
        if res['oee'] < 85:
            st.warning("ALERTE : PERFORMANCE INFERIEURE AU STANDARD INDUSTRIEL (85%)")

elif menu == "TRANSPORT ET TMS":
    st.title("AUDIT ET TRAÇABILITE TRANSPORT")
    
    with st.expander("ESTIMATION DE TRAJET", expanded=True):
        ville = st.selectbox("DESTINATION (DEPART : GLO-DJIGBE)", ["Bohicon", "Parakou", "Malanville", "Seme"])
        if st.button("CALCULER DISTANCE ET TEMPS"):
            res = requests.get(f"{API_URL}/tms/estimation-trajet?ville={ville}").json()
            st.write(f"DISTANCE ESTIMEE : {res['distance_km']} KM | DUREE ESTIMEE : {res['temps_estime_h']} H")
    
    st.divider()
    st.subheader("AUDIT DE RENTABILITE CARBURANT")
    c1, c2, c3 = st.columns(3)
    km_reel = c1.number_input("KILOMETRAGE REEL", value=415)
    tonnes = c2.number_input("TONNAGE EMBARQUE", value=25.0)
    litres = c3.number_input("CARBURANT CONSOMME (L)", value=150.0)
    
    if st.button("VALIDER L'AUDIT DE CONSOMMATION"):
        res = requests.get(f"{API_URL}/tms/audit-carburant?km={km_reel}&tonnes={tonnes}&litres={litres}").json()
        if "Surconsommation" in res['diagnostic']:
            st.error(f"DIAGNOSTIC : {res['diagnostic']}")
        else:
            st.success(f"DIAGNOSTIC : {res['diagnostic']}")
        st.info(f"STRATEGIE : {res['optimisation']}")

elif menu == "INTELLIGENCE ARTIFICIELLE":
    st.title("MAINTENANCE PREDICTIVE PAR IA")
    st.write("Analyse des vecteurs de vibration et de température par Machine Learning.")
    
    if st.button("LANCER L'ANALYSE DES CAPTEURS"):
        # Payload simulé pour la démonstration
        data = [{"vibration": 0.48, "temperature": 82}]
        try:
            res = requests.post(f"{API_URL}/production/analyse-anomalies", json=data).json()
            st.subheader("RESULTAT DE L'ALGORITHME")
            st.json(res)
        except:
            st.error("CONNEXION AU MODULE IA ECHOUEE")
