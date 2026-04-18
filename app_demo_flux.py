import streamlit as st
import requests

st.set_page_config(page_title="Dashboard Décisionnel Smart Industry", layout="wide")

st.title("🏭 Simulateur de Stratégies de Production")
st.sidebar.header("Paramètres Usine")

# Entrées utilisateur
demande = st.sidebar.number_input("Demande Client (Unités)", value=100)
stock = st.sidebar.number_input("Stock Actuel", value=20)
capacite = st.sidebar.number_input("Capacité Max Usine", value=150)

st.header("Analyse des Flux")
col1, col2 = st.columns(2)

# --- TEST FLUX POUSSÉ (PUSH) ---
with col1:
    st.subheader("Stratégie PUSH (Anticipation)")
    # Simulation d'appel API vers votre main.py
    if st.button("Simuler Flux Poussé"):
        from modules.production.flux_manager import gestion_flux_pousse_push
        res = gestion_flux_pousse_push(demande, 10, capacite)
        st.info(f"Quantité à produire : {res['quantite_a_produire']}")
        st.write(f"Utilisation machine : {res['utilisation_capacite']}")
        st.warning(f"Risque : {res['action']}")

# --- TEST FLUX TIRÉ (PULL / JAT) ---
with col2:
    st.subheader("Stratégie PULL (Juste-à-Temps)")
    if st.button("Simuler Flux Tiré"):
        from modules.production.flux_manager import gestion_flux_pull_jat
        res = gestion_flux_pull_jat(demande, stock, 5) # 5 min/unité
        st.success(f"Quantité à lancer : {res['quantite_a_lancer']}")
        st.write(f"Délai estimé : {res['delai_livraison_estime']}")
        st.write(f"Action : {res['action']}")

st.divider()

# --- ANALYSE DES COÛTS ---
st.header("💰 Calculateur du Coût de Revient")
c_matiere = st.number_input("Coût Matières Premières (FCFA)", value=5000)
t_machine = st.number_input("Temps Machine (Heures)", value=2.0)
main_doeuvre = st.number_input("Coût Main d'œuvre (FCFA)", value=1500)

if st.button("Calculer la Rentabilité"):
    from modules.production.flux_manager import calculer_cout_revient
    couts = calculer_cout_revient(c_matiere, t_machine, 2500, main_doeuvre)
    st.metric("Coût de Revient Total", f"{couts['cout_revient_total']} FCFA")
  
