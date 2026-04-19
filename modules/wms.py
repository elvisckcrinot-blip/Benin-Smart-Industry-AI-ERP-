import streamlit as st
import pandas as pd
import numpy as np

def calculate_eoq(annual_demand, order_cost, holding_cost_rate, unit_price):
    """Calcul de la Quantité Économique de Commande (Formule de Wilson)."""
    h = holding_cost_rate * unit_price
    if h == 0: return 0
    eoq = np.sqrt((2 * annual_demand * order_cost) / h)
    return round(eoq, 0)

def run_module():
    st.header("Module 02 : Warehouse Management System (WMS) & IA")
    
    tab1, tab2, tab3 = st.tabs([
        "Segmentation ABC & Réapprovisionnement", 
        "Gestion FIFO/FEFO & Alertes", 
        "Optimisation EOQ & IA Random Forest"
    ])

    # --- ONGLET 1 : SEGMENTATION ABC ---
    with tab1:
        st.subheader("Système de Gestion de Stock ABC")
        col_abc1, col_abc2 = st.columns([2, 1])
        
        with col_abc1:
            st.info("Analyse de la rentabilité financière des stocks par classe (A, B, C)")
            # Simulation de données
            data = pd.DataFrame({
                'Article': ['Acier-H1', 'Acier-H2', 'Bobine-V1', 'Peinture-Ind', 'Solvant-X'],
                'Consommation_Annuelle': [5000, 3000, 1000, 500, 100],
                'Prix_Unitaire': [15000, 12000, 8000, 4000, 2000]
            })
            data['Valeur_Totale'] = data['Consommation_Annuelle'] * data['Prix_Unitaire']
            
            st.write("Aperçu de la segmentation actuelle :")
            # Utilisation de dataframe pour la stabilité mobile
            st.dataframe(data.style.highlight_max(axis=0, subset=['Valeur_Totale']), use_container_width=True)

        with col_abc2:
            st.markdown("### Contrôle Taux de Service")
            st.slider("Taux de service Classe A (%)", 90, 99, 98)
            st.slider("Taux de service Classe B (%)", 80, 95, 90)
            st.button("Déclencher la commande (Classe A)")
            st.markdown("---")
            st.button("Exporter données PDF", key="pdf_abc")

    # --- ONGLET 2 : FIFO/FEFO & NIVEAUX CRITIQUES ---
    with tab2:
        st.subheader("Gestion FIFO/FEFO & Monitoring des Niveaux")
        
        col_stock1, col_stock2, col_stock3 = st.columns(3)
        col_stock1.metric("Stock Optimal", "85%", "2%")
        col_stock2.metric("Stock Moyen", "12%", "-1%")
        col_stock3.metric("Stock Critique", "3%", "Danger", delta_color="inverse")

        st.markdown("#### Liste des articles à réapprovisionner (FEFO)")
        fefo_data = pd.DataFrame({
            'Article': ['Solvant-X', 'Joint-Tanch'],
            'Date_Peremption': ['2026-05-20', '2026-06-15'],
            'Niveau_Actuel': [50, 120],
            'Seuil_Critique': [100, 150],
            'Statut': ['CRITIQUE', 'ATTENTION']
        })
        
        # CORRECTION ICI : Remplacement de applymap par map (Compatibilité Pandas 2.x)
        def color_status(val):
            color = 'red' if val == 'CRITIQUE' else 'orange'
            return f'color: {color}; font-weight: bold'

        # On utilise st.dataframe pour éviter les erreurs de rendu de st.table sur mobile
        st.dataframe(fefo_data.style.map(color_status, subset=['Statut']), use_container_width=True)
        
        st.button("Générer Bon de Commande Automatique")

    # --- ONGLET 3 : EOQ & IA RANDOM FOREST ---
    with tab3:
        st.subheader("Tableau IA Random Forest & EOQ Dynamique")
        
        col_ia1, col_ia2 = st.columns(2)
        
        with col_ia1:
            st.markdown("#### Calculateur EOQ (Wilson)")
            demand = st.number_input("Demande annuelle estimée", value=12000)
            c_order = st.number_input("Coût de passation (FCFA)", value=5000)
            c_holding = st.slider("Taux de possession annuel (%)", 5, 30, 15) / 100
            price = st.number_input("Prix unitaire (FCFA)", value=25000)
            
            val_eoq = calculate_eoq(demand, c_order, c_holding, price)
            st.metric("Quantité Économique (EOQ)", f"{val_eoq} unités")

        with col_ia2:
            st.markdown("#### Prédiction IA (Random Forest)")
            # Simulation de prédiction mensuelle
            mois = ["Janv", "Fév", "Mars", "Avril", "Mai", "Juin", "Juil", "Août", "Sept", "Oct", "Nov", "Déc"]
            predictions = np.random.normal(1000, 150, 12).astype(int)
            pred_df = pd.DataFrame({"Mois": mois, "Prédiction": predictions})
            
            st.line_chart(pred_df.set_index("Mois"))
            st.write(f"Prédiction pour Mai : **{predictions[4]} unités**")

        st.markdown("---")
        st.button("Exporter Rapport IA & EOQ (PDF)")
            
