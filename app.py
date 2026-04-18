import streamlit as st
import requests
import pandas as pd

# Configuration de la page pour mobile et desktop
st.set_page_config(
    page_title="Benin Smart Industry ERP",
    page_icon="🏭",
    layout="wide"
)

# Style CSS pour améliorer l'interface sur téléphone
st.markdown("""
    <style>
    .main { opacity: 0.95; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    </style>
    """, unsafe_allow_path=True)

st.title("🏭 Benin Smart Industry AI-ERP")
st.write("Optimisation de la Supply Chain et de la Production")

# --- NAVIGATION LATÉRALE ---
st.sidebar.header("Navigation ERP")
menu = st.sidebar.radio(
    "Choisir un module :",
    ["Dashboard", "1. Achats & Marchés", "2. WMS (Stocks)", "3. Production", "4. TMS (Transport)", "5. IA & Maintenance"]
)

API_URL = "http://127.0.0.1:8000"

# --- PAGE D'ACCUEIL / DASHBOARD ---
if menu == "Dashboard":
    st.subheader("Vue d'ensemble")
    col1, col2 = st.columns(2)
    col1.metric("Statut Système", "Online", "v4.0 Final")
    col2.metric("Localisation", "Cotonou/Bohicon", "Bénin")
    st.info("Utilisez le menu à gauche pour naviguer dans les modules industriels.")

# --- MODULE 1 : ACHATS ---
elif menu == "1. Achats & Marchés":
    st.header("📦 Achats & Fiscalité")
    valeur_cif = st.number_input("Valeur CIF (FCFA)", value=1000000, step=50000)
    categorie = st.selectbox("Catégorie Douanière", [1, 2, 3], help="1: Première nécessité, 2: Matières premières, 3: Biens de consommation")
    
    if st.button("Calculer les Taxes Bénin"):
        try:
            res = requests.get(f"{API_URL}/achats/simulation-taxe?valeur_cif={valeur_cif}&categorie={categorie}").json()
            st.success(f"Total Droits & Taxes : {res['total_taxes_fcfa']} FCFA")
            st.json(res)
        except:
            st.error("Erreur : Assurez-vous que l'API (uvicorn) est lancée.")

# --- MODULE 2 : WMS ---
elif menu == "2. WMS (Stocks)":
    st.header("🏬 Gestion d'Entrepôt (WMS)")
    action = st.selectbox("Action", ["Analyse ABC", "Simulation EOQ (Wilson)"])
    
    if action == "Simulation EOQ (Wilson)":
        demande = st.number_input("Demande Annuelle", value=5000)
        cout_c = st.number_input("Coût de Commande", value=15000)
        cout_s = st.number_input("Coût de Stockage/unité", value=500)
        if st.button("Calculer Quantité Économique"):
            res = requests.get(f"{API_URL}/wms/wilson?demande_annuelle={demande}&cout_commande={cout_c}&cout_stockage={cout_s}").json()
            st.metric("Quantité Optimale (EOQ)", f"{res['eoq']} unités")

# --- MODULE 3 : PRODUCTION ---
elif menu == "3. Production":
    st.header("⚙️ Pilotage de la Production")
    col1, col2 = st.columns(2)
    with col1:
        t_dispo = st.number_input("Temps Dispo (h)", value=8.0)
        p_totales = st.number_input("Pièces Produites", value=1000)
    with col2:
        t_arret = st.number_input("Temps d'Arrêt (h)", value=1.0)
        p_conformes = st.number_input("Pièces Conformes", value=950)
    
    if st.button("Calculer Performance (TRS/OEE)"):
        res = requests.get(f"{API_URL}/production/calcul-trs?t_dispo={t_dispo}&t_arret={t_arret}&p_totales={p_totales}&p_conformes={p_conformes}").json()
        st.metric("Taux de Rendement Synthétique", f"{res['oee']}%")
        if res['oee'] < 85:
            st.warning("Performance sous l'objectif mondial (85%)")

# --- MODULE 4 : TMS ---
elif menu == "4. TMS (Transport)":
    st.header("🚛 Transport & Audit Carburant")
    ville = st.selectbox("Destination (depuis Glo-Djigbé)", ["Bohicon", "Parakou", "Malanville", "Seme"])
    
    if st.button("Estimer Temps & Distance"):
        res = requests.get(f"{API_URL}/tms/estimation-trajet?ville={ville}").json()
        st.write(f"📍 Distance : {res['distance_km']} km | ⏱️ Temps : {res['temps_estime_h']} h")
        st.info(res['conseil_securite'])

    st.divider()
    st.subheader("Audit Carburant")
    km_reel = st.number_input("KM parcourus", value=415)
    tonnes = st.number_input("Tonnage réel", value=25.0)
    litres = st.number_input("Litres consommés", value=180.0)
    
    if st.button("Lancer l'Audit"):
        res = requests.get(f"{API_URL}/tms/audit-carburant?km={km_reel}&tonnes={tonnes}&litres={litres}").json()
        if res['diagnostic'] == "Surconsommation detectee":
            st.error(f"🚨 {res['diagnostic']}")
        else:
            st.success(f"✅ {res['diagnostic']}")
        st.write(f"Indice : {res['indice_efficacite']}")

# --- MODULE 5 : IA ---
elif menu == "5. IA & Maintenance":
    st.header("🤖 Maintenance Prédictive")
    st.write("Simulation de capteurs machines en temps réel.")
    if st.button("Analyser l'état machine"):
        # Simulation de données pour l'exemple
        data = [{"vibration": 0.5, "temperature": 85}]
        res = requests.post(f"{API_URL}/production/analyse-anomalies", json=data).json()
        st.write(res)
