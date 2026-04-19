import streamlit as st
from modules import achat, wms, production, tms

# Configuration de la page
st.set_page_config(
    page_title="Bénin Industrie Intelligente | ERP",
    page_icon="🏭", # Emoji système uniquement pour le navigateur
    layout="wide"
)

# Injection de CSS pour un style industriel (Gris acier, Bleu nuit)
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    stSidebar {
        background-color: #1e2630;
    }
    h1, h2, h3 {
        color: #1e2630;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.title("Bénin Industrie Intelligente - ERP Supply Chain 4.0")
    st.sidebar.header("Navigation Technique")
    
    # Menu de sélection des modules
    menu = [
        "Tableau de Bord", 
        "Module 01 : Achats & Marchés", 
        "Module 02 : WMS & Stocks", 
        "Module 03 : Production & Maintenance", 
        "Module 04 : TMS & Corridors"
    ]
    choice = st.sidebar.selectbox("Sélectionner un module", menu)

    if choice == "Tableau de Bord":
        st.subheader("Indicateurs de Performance Globaux (KPI)")
        st.info("Sélectionnez un module dans la barre latérale pour accéder aux fonctions opérationnelles.")
        
    elif choice == "Module 01 : Achats & Marchés":
        # Appel de la fonction du module achat (à créer dans modules/achat.py)
        st.header("Gestion des Achats et Conformité CEDEAO")
        # achat.run_module()

    elif choice == "Module 02 : WMS & Stocks":
        st.header("Warehouse Management System & IA")
        # wms.run_module()

    elif choice == "Module 03 : Production & Maintenance":
        st.header("Pilotage de Production & Maintenance Prédictive")
        # production.run_module()

    elif choice == "Module 04 : TMS & Corridors":
        st.header("Transport Management System & Logistique Inverse")
        # tms.run_module()

if __name__ == '__main__':
    main()
    
