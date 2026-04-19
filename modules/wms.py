import streamlit as st
import pandas as pd
import numpy as np

def calculate_eoq(annual_demand, order_cost, holding_cost_rate, unit_price):
    h = holding_cost_rate * unit_price
    if h == 0: return 0
    return round(np.sqrt((2 * annual_demand * order_cost) / h), 0)

def run_module():
    st.header("Module 02 : WMS & Intelligence Artificielle")
    
    tab1, tab2, tab3 = st.tabs([
        "Analyse ABC", 
        "Alertes Stocks", 
        "IA & Wilson"
    ])

    # DONNÉES SIMULÉES
    data = pd.DataFrame({
        'Article': ['Acier-H1', 'Acier-H2', 'Bobine-V1', 'Peinture-Ind', 'Solvant-X'],
        'Stock': [5000, 3000, 1000, 500, 100],
        'Prix': [15000, 12000, 8000, 4000, 2000]
    })

    with tab1:
        st.subheader("Segmentation des Stocks")
        # Utilisation de dataframe BRUT (0% de chance d'erreur AttributeError)
        st.dataframe(data, use_container_width=True)
        st.button("Exporter PDF")

    with tab2:
        st.subheader("Monitoring FEFO / Alertes")
        col1, col2, col3 = st.columns(3)
        col1.metric("Optimal", "85%", "2%")
        col2.metric("Moyen", "12%", "-1%")
        col3.metric("Critique", "3%", "Danger", delta_color="inverse")

        # Liste simple sans mise en forme conditionnelle complexe
        fefo_list = pd.DataFrame({
            'Article': ['Solvant-X', 'Joint-Tanch'],
            'Statut': ['🔴 CRITIQUE', '🟠 ATTENTION'],
            'Reste': [50, 120]
        })
        st.table(fefo_list)

    with tab3:
        st.subheader("Optimisation IA & Wilson")
        col_ia1, col_ia2 = st.columns(2)
        with col_ia1:
            st.write("**Calculateur Wilson**")
            eoq = calculate_eoq(12000, 5000, 0.15, 25000)
            st.metric("Quantité EOQ", f"{eoq} unités")
        with col_ia2:
            st.write("**Prédiction IA**")
            st.line_chart(np.random.randint(800, 1200, 12))
    
