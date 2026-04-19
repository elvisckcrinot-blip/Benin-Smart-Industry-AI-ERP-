import streamlit as st
import pandas as pd
import numpy as np

def calculate_fuel_efficiency(distance, weight, fuel_price):
    """Calcule la rentabilité du carburant et le prix de revient du voyage."""
    consumption_rate = 0.35  # Litres/km standard
    load_factor = 1 + (weight / 40)
    total_fuel = distance * consumption_rate * load_factor
    fuel_cost = total_fuel * fuel_price
    fixed_costs = 50000  # Chauffeur, entretien, amortissement
    total_trip_cost = fuel_cost + fixed_costs
    return round(total_trip_cost, 0), round(fuel_cost, 0)

def run_module():
    st.header("Module 04 : Transport Management System (TMS)")
    
    # Navigation par onglets simplifiée
    tabs = st.tabs([
        "Planification RNIE", 
        "Calcul de Rentabilité", 
        "Gestion des Quais", 
        "Logistique Inverse"
    ])

    # --- ONGLET 1 : TRACKING & CORRIDORS ---
    with tabs[0]:
        st.subheader("Suivi des Flux sur les Axes RNIE")
        
        # Sélection simplifiée pour éviter les erreurs de saisie
        axe = st.selectbox("Sélectionner l'Axe Stratégique", [
            "RNIE 2 : Cotonou - Malanville (Nord)",
            "RNIE 1 : Cotonou - Hillacondji (Ouest)",
            "RNIE 1 : Cotonou - Kraké (Est)",
            "RNIE 3 : Dassa - Porga (Nord-Ouest)"
        ])
        
        # Données de démo robustes
        tracking_data = pd.DataFrame({
            "Véhicule": ["CAM-001", "CAM-002", "CAM-003"],
            "Position": ["Bohicon", "Parakou", "Kandi"],
            "Statut": ["En circulation", "Arrêt technique", "Chargement"],
            "Charge": ["25t", "30t", "28t"]
        })
        
        # AFFICHAGE STABLE : st.dataframe est le plus fiable sur mobile
        st.dataframe(tracking_data, use_container_width=True)

    # --- ONGLET 2 : RENTABILITÉ CARBURANT ---
    with tabs[1]:
        st.subheader("Analyse de Coût au Voyage")
        
        col1, col2 = st.columns(2)
        with col1:
            dist = st.number_input("Distance (km)", value=130, step=10) # Cotonou-Bohicon par défaut
            poids = st.number_input("Poids total (tonnes)", value=20.0, step=1.0)
            prix_l = st.number_input("Prix Gasoil (FCFA/L)", value=700)
            
        with col2:
            total, fuel = calculate_fuel_efficiency(dist, poids, prix_l)
            st.metric("Coût Total Estimé", f"{int(total):,} FCFA".replace(",", " "))
            st.metric("Budget Carburant", f"{int(fuel):,} FCFA".replace(",", " "))
            
            rentabilite = st.progress(min(int((fuel/total)*100), 100))
            st.caption(f"Le carburant représente {int((fuel/total)*100)}% du coût total.")

    # --- ONGLET 3 : GESTION DES QUAIS ---
    with tabs[2]:
        st.subheader("Affectation des Camions (Docking)")
        
        with st.expander("Enregistrer une nouvelle entrée/sortie"):
            m_id = st.text_input("Immatriculation", placeholder="Ex: BJ 1234")
            op = st.selectbox("Type d'opération", ["Chargement", "Déchargement"])
            quai = st.select_slider("Affectation Quai", options=["Q1", "Q2", "Q3", "Zone Vrac"])
            
            if st.button("Valider l'affectation", type="primary"):
                st.success(f"Camion {m_id} affecté au {quai}")

    # --- ONGLET 4 : LOGISTIQUE INVERSE ---
    with tabs[3]:
        st.subheader("Retours et Avaries")
        
        col_r1, col_r2 = st.columns(2)
        with col_r1:
            motif = st.radio("Motif du Retour", ["Produit Endommagé", "Erreur Livraison", "Surplus"])
        with col_r2:
            action = st.radio("Action Requise", ["Réparer", "Détruire", "Ré-intégrer"])
            
        if st.button("Générer Bon de Retour"):
            st.info("Système prêt pour génération PDF.")
    
