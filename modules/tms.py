import streamlit as st
import pandas as pd
import numpy as np
import time

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
    
    tabs = st.tabs([
        "Planification RNIE", 
        "Calcul de Rentabilité", 
        "Gestion des Quais", 
        "Logistique Inverse"
    ])

    # --- ONGLET 1 : TRACKING & CORRIDORS ---
    with tabs[0]:
        st.subheader("Suivi des Flux sur les Axes RNIE")
        axe = st.selectbox("Sélectionner l'Axe Stratégique", [
            "RNIE 2 : Cotonou - Malanville (Nord)",
            "RNIE 1 : Cotonou - Hillacondji (Ouest)",
            "RNIE 1 : Cotonou - Kraké (Est)",
            "RNIE 3 : Dassa - Porga (Nord-Ouest)"
        ])
        
        tracking_data = pd.DataFrame({
            "Véhicule": ["CAM-001", "CAM-002", "CAM-003"],
            "Position": ["Bohicon", "Parakou", "Kandi"],
            "Statut": ["En circulation", "Arrêt technique", "Chargement"],
            "Charge": ["25t", "30t", "28t"]
        })
        st.dataframe(tracking_data, use_container_width=True)

    # --- ONGLET 2 : RENTABILITÉ CARBURANT ---
    with tabs[1]:
        st.subheader("Analyse de Coût au Voyage")
        col1, col2 = st.columns(2)
        with col1:
            dist = st.number_input("Distance (km)", value=130, step=10)
            poids = st.number_input("Poids total (tonnes)", value=20.0, step=1.0)
            prix_l = st.number_input("Prix Gasoil (FCFA/L)", value=700)
            
        with col2:
            total, fuel = calculate_fuel_efficiency(dist, poids, prix_l)
            st.metric("Coût Total Estimé", f"{int(total):,} FCFA".replace(",", " "))
            st.metric("Budget Carburant", f"{int(fuel):,} FCFA".replace(",", " "))
            
            rent_val = min(max(int((fuel/total)*100), 0), 100)
            st.progress(rent_val)
            st.caption(f"Le carburant représente {rent_val}% du coût total.")

        st.markdown("---")
        # Export CSV pour la rentabilité
        rent_df = pd.DataFrame([{
            "Axe": axe,
            "Distance_km": dist,
            "Charge_t": poids,
            "Cout_Gasoil": fuel,
            "Cout_Total": total
        }])
        csv_rent = rent_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📊 Exporter Analyse de Rentabilité (CSV)",
            data=csv_rent,
            file_name=f"Rentabilite_Transport_{time.strftime('%Y%m%d')}.csv",
            mime="text/csv",
            use_container_width=True
        )

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
            
        st.markdown("---")
        # Export CSV pour le Bon de Retour (Remplacement du PDF)
        retour_df = pd.DataFrame([{
            "Document": "BON DE RETOUR",
            "Date": time.strftime('%Y-%m-%d'),
            "Motif": motif,
            "Action_Requise": action,
            "Statut": "En attente de traitement"
        }])
        csv_retour = retour_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Générer Bon de Retour (CSV)",
            data=csv_retour,
            file_name=f"Bon_Retour_TMS_{time.strftime('%Y%m%d')}.csv",
            mime="text/csv",
            use_container_width=True
        )
        
