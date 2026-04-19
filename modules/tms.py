import streamlit as st
import pandas as pd
import numpy as np
import time

def calculate_tms_metrics(distance, weight, fuel_price, margin_percent):
    """Calcul complet des coûts, du prix de vente et du bénéfice."""
    # Coûts Variables (Carburant)
    consumption_rate = 0.35  
    load_factor = 1 + (weight / 40)
    total_fuel_qty = distance * consumption_rate * load_factor
    fuel_cost = round(total_fuel_qty * fuel_price, 0)
    
    # Coûts Fixes (Détail industriel : Chauffeur, Entretien, Assurance)
    fixed_costs = 50000  
    
    # Coût de revient total
    total_cost = fuel_cost + fixed_costs
    
    # Calcul du Prix de Vente (Méthode du taux de marge)
    if margin_percent < 100:
        selling_price = round(total_cost / (1 - (margin_percent / 100)), 0)
    else:
        selling_price = total_cost
        
    benefit = selling_price - total_cost
    
    return total_cost, fuel_cost, fixed_costs, selling_price, benefit

def run_module():
    st.header("Module 04 : Transport Management System (TMS)")
    
    # Structure à 4 onglets basée sur tes captures et ton code
    tabs = st.tabs([
        "Planification RNIE", 
        "Rentabilité & Marge", 
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

    # --- ONGLET 2 : RENTABILITÉ & MARGE (Version Optimisée) ---
    with tabs[1]:
        st.subheader("Analyse de Rentabilité Avancée")
        
        col_in, col_res = st.columns([1, 1.2])
        
        with col_in:
            st.markdown("#### 1. Paramètres du Voyage")
            dist = st.number_input("Distance (km)", value=130, step=10)
            poids = st.number_input("Poids (tonnes)", value=20.0)
            prix_l = st.number_input("Prix Gasoil (FCFA/L)", value=700)
            
            st.markdown("---")
            st.markdown("#### 2. Stratégie Commerciale")
            marge_cible = st.select_slider(
                "Marge bénéficiaire souhaitée (%)",
                options=[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
                value=25
            )
            
        with col_res:
            tc, fc, fix, sp, ben = calculate_tms_metrics(dist, poids, prix_l, marge_cible)
            
            st.markdown("#### 3. Résultat d'Exploitation")
            st.metric("PRIX DE VENTE CONSEILLÉ", f"{int(sp):,} FCFA".replace(",", " "))
            st.metric("BÉNÉFICE NET ESTIMÉ", f"{int(ben):,} FCFA".replace(",", " "), delta=f"{marge_cible}% de marge")
            
            with st.expander("🔎 Détail de la structure des coûts"):
                st.write(f"**Coûts Fixes :** {int(fix):,} FCFA".replace(",", " "))
                st.caption("(Chauffeur, Maintenance, Amortissement)")
                st.write(f"**Coûts Variables (Gasoil) :** {int(fc):,} FCFA".replace(",", " "))
                st.write(f"**COÛT DE REVIENT TOTAL :** {int(tc):,} FCFA".replace(",", " "))

        st.markdown("---")
        # Export CSV complet
        export_data = pd.DataFrame([{
            "Axe": axe,
            "Distance_km": dist,
            "Charge_t": poids,
            "Cout_Fixe": fix,
            "Cout_Carburant": fc,
            "Cout_Total": tc,
            "Marge_Appliquee": f"{marge_cible}%",
            "Prix_Vente": sp,
            "Benefice_Net": ben
        }])
        
        csv_tms = export_data.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📊 Exporter l'Analyse de Rentabilité (CSV)",
            data=csv_tms,
            file_name=f"Analyse_Marge_TMS_{time.strftime('%Y%m%d')}.csv",
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
        retour_df = pd.DataFrame([{
            "Document": "BON DE RETOUR",
            "Date": time.strftime('%Y-%m-%d'),
            "Motif": motif,
            "Action_Requise": action,
            "Statut": "En attente"
        }])
        csv_retour = retour_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Générer Bon de Retour (CSV)",
            data=csv_retour,
            file_name=f"Bon_Retour_TMS_{time.strftime('%Y%m%d')}.csv",
            mime="text/csv",
            use_container_width=True
        )
        
