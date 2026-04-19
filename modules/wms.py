import streamlit as st
import pandas as pd
import numpy as np

def calculate_eoq(annual_demand, order_cost, holding_cost_rate, unit_price):
    """Calcul de la Quantité Économique de Commande (Formule de Wilson)."""
    h = holding_cost_rate * unit_price
    if h <= 0: return 0
    eoq = np.sqrt((2 * annual_demand * order_cost) / h)
    return round(eoq, 0)

def run_module():
    st.header("Module 02 : Warehouse Management System (WMS) & IA")
    
    tab1, tab2, tab3 = st.tabs([
        "Segmentation ABC & Réappro", 
        "Gestion FIFO/FEFO & Alertes", 
        "Optimisation EOQ & IA"
    ])

    # --- ONGLET 1 : SEGMENTATION ABC ---
    with tab1:
        st.subheader("Système de Gestion de Stock ABC")
        
        # Données de simulation
        data = pd.DataFrame({
            'Article': ['Acier-H1', 'Acier-H2', 'Bobine-V1', 'Peinture-Ind', 'Solvant-X'],
            'Consommation_Annuelle': [5000, 3000, 1000, 500, 100],
            'Prix_Unitaire': [15000, 12000, 8000, 4000, 2000]
        })
        data['Valeur_Totale'] = data['Consommation_Annuelle'] * data['Prix_Unitaire']
        
        # AFFICHAGE SIMPLE SANS STYLE (Zéro erreur garantie)
        st.write("Analyse de la rentabilité financière :")
        st.dataframe(data, use_container_width=True)

        st.markdown("---")
        col_c1, col_c2 = st.columns(2)
        with col_c1:
            st.slider("Taux de service Classe A (%)", 90, 99, 98)
        with col_c2:
            st.button("Déclencher commande (Classe A)", use_container_width=True)

    # --- ONGLET 2 : FIFO/FEFO & ALERTES ---
    with tab2:
        st.subheader("Monitoring des Niveaux de Stock")
        
        # Indicateurs visuels (Metrics sont très stables sur mobile)
        m1, m2, m3 = st.columns(3)
        m1.metric("Stock Optimal", "85%", "+2%")
        m2.metric("Stock Moyen", "12%", "-1%")
        m3.metric("Stock Critique", "3%", "DANGER", delta_color="inverse")

        st.markdown("#### Liste des articles à réapprovisionner")
        fefo_data = pd.DataFrame({
            'Article': ['Solvant-X', 'Joint-Tanch'],
            'Date_Peremption': ['2026-05-20', '2026-06-15'],
            'Niveau': [50, 120],
            'Seuil': [100, 150],
            'Priorité': ['🔴 CRITIQUE', '🟠 ATTENTION']
        })
        
        # On affiche le statut avec des emojis directement dans le texte au lieu du CSS
        st.table(fefo_data)
        
        if st.button("Générer Bon de Commande Automatique"):
            st.success("Bon de commande envoyé aux Achats.")

    # --- ONGLET 3 : EOQ & IA ---
    with tab3:
        st.subheader("Optimisation Dynamique")
        
        col_ia1, col_ia2 = st.columns(2)
        
        with col_ia1:
            st.markdown("#### Calculateur Wilson (EOQ)")
            demand = st.number_input("Demande annuelle", value=12000)
            c_order = st.number_input("Coût passation (FCFA)", value=5000)
            c_holding = st.slider("Taux possession (%)", 5, 30, 15) / 100
            price = st.number_input("Prix unitaire (FCFA)", value=25000)
            
            val_eoq = calculate_eoq(demand, c_order, c_holding, price)
            st.metric("Quantité Économique", f"{val_eoq} unités")

        with col_ia2:
            st.markdown("#### Prédiction IA (M+1)")
            mois = ["Jan", "Fév", "Mar", "Avr", "Mai", "Jun"]
            preds = [1050, 980, 1100, 1250, 1180, 1300]
            pred_df = pd.DataFrame({"Mois": mois, "Prédiction": preds})
            
            st.line_chart(pred_df.set_index("Mois"))
            st.write(f"Prévision Mai : **{preds[4]} unités**")

        st.button("Exporter Rapport IA & EOQ (PDF)", use_container_width=True)
        
