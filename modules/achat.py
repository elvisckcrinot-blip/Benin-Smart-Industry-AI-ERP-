import streamlit as st
import pandas as pd

def calculate_landed_cost(fob_price, freight, insurance, currency_rate):
    """
    Calcule le coût de revient incluant la taxation béninoise (TEC + TVA).
    """
    # Conversion en FCFA
    cif_val = (fob_price + freight + insurance) * currency_rate
    
    # Fiscalité Bénin / CEDEAO
    tec_rate = 0.20  # Taux moyen TEC (Catégorie 3 : Biens de consommation finale)
    tva_rate = 0.18  # TVA Bénin
    pcs_rate = 0.01  # Prélèvement Communautaire de Solidarité
    
    droits_douane = cif_val * tec_rate
    pcs = cif_val * pcs_rate
    base_tva = cif_val + droits_douane + pcs
    tva = base_tva * tva_rate
    
    total_taxes = droits_douane + pcs + tva
    total_cost = cif_val + total_taxes
    
    return {
        "CIF FCFA": round(cif_val, 2),
        "Droits de Douane": round(droits_douane, 2),
        "TVA": round(tva, 2),
        "Total Taxes": round(total_taxes, 2),
        "Coût de Revient Total": round(total_cost, 2)
    }

def run_module():
    st.header("Module 01 : Achats, Marchés Publics & Fiscalité")
    
    tab1, tab2, tab3 = st.tabs([
        "Passation de Marchés (GPAO)", 
        "Simulateur Incoterms 2020", 
        "Calculateur de Coûts & Taxes"
    ])

    with tab1:
        st.subheader("Analyse d'Appel d'Offres")
        uploaded_file = st.file_uploader("Charger le Dossier d'Appel d'Offres (PDF)", type="pdf")
        if uploaded_file:
            st.success("Fichier réceptionné. Analyse des clauses clés en cours...")
            # Ici viendra la logique de scannage PDF
        
    with tab2:
        st.subheader("Sélecteur de Transfert de Risques")
        incoterm = st.selectbox("Choisir l'Incoterm", ["EXW", "FOB", "CFR", "CIF", "DDP"])
        
        incoterms_data = {
            "EXW": "L'acheteur assume tous les frais et risques dès l'usine du vendeur.",
            "FOB": "Le vendeur livre la marchandise à bord du navire. Risque transféré au bastingage.",
            "CIF": "Le vendeur paie le transport et l'assurance jusqu'au port de destination.",
            "DDP": "Le vendeur assume tous les frais, y compris le dédouanement à destination."
        }
        st.info(f"Note Logistique : {incoterms_data.get(incoterm, 'Description non disponible.')}")

    with tab3:
        st.subheader("Simulation Financière (Importation Bénin)")
        col1, col2 = st.columns(2)
        
        with col1:
            fob_val = st.number_input("Valeur FOB (Devise origine)", min_value=0.0)
            rate = st.number_input("Taux de change (ex: 1€ = 655.95 FCFA)", value=655.95)
        
        with col2:
            # Logique dynamique : si CIF sélectionné, assurance/fret sont inclus ou grisés
            freight = st.number_input("Fret International (FCFA)", min_value=0.0)
            insurance = st.number_input("Assurance (FCFA)", min_value=0.0)

        if st.button("Calculer le Coût de Revient"):
            results = calculate_landed_cost(fob_val, freight, insurance, rate)
            
            # Affichage des résultats en mode industriel
            st.markdown("---")
            res_col1, res_col2 = st.columns(2)
            for key, value in results.items():
                res_col1.metric(label=key, value=f"{value:,.0f} FCFA")
            
            # Exportation des données
            st.download_button(
                label="Exporter le rapport d'achat (CSV)",
                data=pd.DataFrame([results]).to_csv(index=False),
                file_name="rapport_achat_benin.csv",
                mime="text/csv"
  )
  
