import streamlit as st
import requests
import pandas as pd
import numpy as np

st.title("Test de Maintenance Predictive - Smart Industry")

# Section 1 : Simulation de Capteurs
st.header("Simulation de donnees capteurs")
col1, col2, col3 = st.columns(3)

with col1:
    temp = st.slider("Temperature (C)", 20, 120, 45)
with col2:
    vibr = st.slider("Vibration (mm/s)", 0.0, 2.0, 0.4)
with col3:
    pres = st.slider("Pression (bar)", 0, 10, 3)

# Simulation d un historique pour l entrainement de l IA
historique = [
    {'vibration': 0.4, 'temp': 42, 'pression': 3},
    {'vibration': 0.45, 'temp': 40, 'pression': 3.1},
    {'vibration': 0.38, 'temp': 44, 'pression': 2.9},
    # On ajoute la donnee actuelle
    {'vibration': vibr, 'temp': temp, 'pression': pres}
]

# Section 2 : Appel au Module de Maintenance
if st.button("Analyser l etat de la machine"):
    # Appel a votre API (main.py doit etre lance)
    # Pour ce test local, on peut aussi importer directement la fonction
    from modules.production.maintenance import detecter_anomalie_machine
    
    resultat = detecter_anomalie_machine(historique)
    
    if resultat['alerte']:
        st.error(f"ANOMALIE DETECTEE : {resultat['nb_anomalies_detectees']} point(s) suspect(s)")
        st.write("Details des ecarts :", resultat['details'])
    else:
        st.success("Fonctionnement normal de la machine")

# Section 3 : Visualisation du TRS (OEE)
st.header("Calcul de la performance (TRS)")
t_dispo = st.number_input("Temps de production total (min)", value=480)
t_arret = st.number_input("Temps d arret (min)", value=30)
p_total = st.number_input("Pieces produites", value=1000)
p_conf = st.number_input("Pieces conformes", value=950)

from modules.production.maintenance import calculer_oee
trs_data = calculer_oee(t_dispo, t_arret, p_total, p_conf)

st.metric("TRS Global", f"{trs_data['trs_global']}%")
st.progress(trs_data['trs_global'] / 100)
  
