import streamlit as st

# Importation sécurisée des modules opérationnels depuis le dossier /modules
try:
    from modules import achat, wms, production, tms
except ImportError as e:
    st.error(f"Erreur de structure : Assurez-vous que le dossier 'modules' contient un fichier '__init__.py' vide. Détail : {e}")

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(
    page_title="Bénin Industrie Intelligente | ERP",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. DESIGN UI (Style Industriel : Gris Anthracite & Bleu Acier)
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background-color: #1e2630;
    }
    .stButton>button {
        width: 100%;
        border-radius: 4px;
        height: 3em;
        background-color: #1e2630;
        color: white;
        border: none;
    }
    .stButton>button:hover {
        background-color: #2c3e50;
        border: 1px solid #3498db;
    }
    h1, h2, h3 {
        color: #1e2630;
        font-family: 'Segoe UI', sans-serif;
    }
    /* Personnalisation des métriques pour un look Dashboard */
    [data-testid="stMetricValue"] {
        font-size: 1.8rem;
        color: #2e86de;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    # BARRE LATÉRALE - NAVIGATION
    st.sidebar.title("LOGIX 360 - ERP")
    st.sidebar.markdown("---")
    
    menu = [
        "Tableau de Bord", 
        "Module 01 : Achats & Marchés", 
        "Module 02 : WMS & Stocks", 
        "Module 03 : Production & Maintenance", 
        "Module 04 : TMS & Corridors"
    ]
    
    choice = st.sidebar.selectbox("Navigation Opérationnelle", menu)
    
    st.sidebar.markdown("---")
    st.sidebar.write("**Administrateur :** Elvis CRINOT")
    st.sidebar.info("Zone économique : Bénin (CEDEAO)")

    # 3. LOGIQUE D'AFFICHAGE DES MODULES
    if choice == "Tableau de Bord":
        st.title("Tableau de Bord Stratégique")
        st.subheader("Visualisation des flux de la Supply Chain 4.0")
        
        # Section KPI (Key Performance Indicators)
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Dossiers Achat", "12 Dossiers", "+2")
        col2.metric("Dispo. Stock", "85%", "-3%")
        col3.metric("OEE Production", "82%", "+1.5%")
        col4.metric("Rotation Flotte", "14 Camions", "+4")
        
        st.markdown("---")
        
        # Résumé des capacités du système
        st.markdown("""
        ### État du Système
        L'écosystème **Bénin Industrie** est opérationnel sur les piliers suivants :
        * **Approvisionnements :** Gestion des incoterms et calcul de taxation (Bénin/TEC).
        * **Entrepôt (WMS) :** Optimisation IA via Random Forest et réapprovisionnement EOQ.
        * **Usine (Production) :** Pilotage en flux tendus (JIT) et maintenance prédictive 4.0.
        * **Distribution (TMS) :** Tracking des axes RNIE et logistique inverse intégrée.
        """)
        
    elif choice == "Module 01 : Achats & Marchés":
        achat.run_module()

    elif choice == "Module 02 : WMS & Stocks":
        wms.run_module()

    elif choice == "Module 03 : Production & Maintenance":
        production.run_module()

    elif choice == "Module 04 : TMS & Corridors":
        tms.run_module()

if __name__ == '__main__':
    main()
