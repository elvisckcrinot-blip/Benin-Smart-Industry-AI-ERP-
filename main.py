import streamlit as st
from modules import achat, wms, production, tms

# 1. Configuration de l'interface (Standard Industriel)
st.set_page_config(
    page_title="Bénin Industrie Intelligente | ERP",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Injection CSS pour une interface épurée (Gris Acier & Bleu Nuit)
st.markdown("""
    <style>
    /* Style de la barre latérale */
    [data-testid="stSidebar"] {
        background-color: #1e2630;
        color: white;
    }
    /* Style des titres */
    h1, h2, h3 {
        color: #1e2630;
        font-family: 'Segoe UI', sans-serif;
    }
    /* Style des boutons */
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #1e2630;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    # Barre latérale - Profil & Navigation
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
    st.sidebar.write("**Expert :** Elvis CRINOT")
    st.sidebar.write("**Région :** Bénin / CEDEAO")

    # 3. Logique de Routage vers les Modules
    if choice == "Tableau de Bord":
        st.title("Tableau de Bord Exécutif")
        st.subheader("Indicateurs de Performance (KPI) Transversaux")
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Flux Achat", "12 Dossiers", "+2")
        col2.metric("Niveau Stock", "85%", "-3%")
        col3.metric("OEE Production", "82%", "+1%")
        col4.metric("Rotation Camions", "14/j", "+4")
        
        st.info("Utilisez le menu latéral pour accéder aux outils spécifiques de chaque département.")
        
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
  
