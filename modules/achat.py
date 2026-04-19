import streamlit as st
import pandas as pd
from utils import generate_pdf  # Importation de ta fonction centralisée

def calculate_landed_cost(fob_price, freight, insurance, currency_rate, incoterm):
    """
    Calcule le coût de revient incluant la taxation béninoise (TEC + TVA + PCS).
    """
    base_val = fob_price * currency_rate
    cif_val = base_val + freight + insurance
    
    tec_rate = 0.20  
    tva_rate = 0.18  
    pcs_rate = 0.01  
    
    droits_douane = cif_val * tec_rate
    pcs = cif_val * pcs_rate
    base_tva = cif_val + droits_douane + pcs
    tva = base_tva * tva_rate
    
    total_taxes = droits_douane + pcs + tva
    total_cost = cif_val + total_taxes
    
    return {
        "Valeur CIF (FCFA)": round(cif_val, 2),
        "Droits de Douane (20%)": round(droits_douane, 2),
        "PCS (1%)": round(pcs, 2),
        "TVA (18%)": round(tva, 2),
        "Total Taxes": round(total_taxes, 2),
        "Coût de Revient Total": round(total_cost, 2)
    }

def get_incoterm_recommendation(role, responsibility):
    """
    Sélection automatique de l'Incoterm selon le rôle et la charge souhaitée.
    """
    if role == "Acheteur":
        if responsibility == "Toutes les charges (Full Risk)": return "EXW"
        elif responsibility == "Charges équilibrées": return "FOB"
        else: return "DDP" # Minimum de charges pour l'acheteur
    else: # Vendeur
        if responsibility == "Toutes les charges (Full Risk)": return "DDP"
        elif responsibility == "Charges équilibrées": return "CIF"
        else: return "EXW" # Minimum de charges pour le vendeur

def run_module():
    st.header("Module 01 : Achats & Passation de Marchés")
    
    tab1, tab2, tab3 = st.tabs([
        "Marchés Publics & GPAO", 
        "Ingénierie des Incoterms", 
        "Coûts & Documentation"
    ])

    # --- ONGLET 1 : MARCHÉS PUBLICS ---
    with tab1:
        st.subheader("Traitement des Activités de Marché Public")
        col_ao1, col_ao2 = st.columns([2, 1])
        with col_ao1:
            st.info("Fonction : Scannage de l'appel d'offre conformément aux règles clés du Bénin GPAO")
            uploaded_ao = st.file_uploader("Charger le dossier d'appel d'offre (PDF)", type="pdf", key="ao_pdf")
            if uploaded_ao:
                st.success("Fichier réceptionné. Analyse sémantique des clauses de conformité en cours...")
        with col_ao2:
            st.markdown("### Section PDF")
            st.button("Exporter données GPAO")

    # --- ONGLET 2 : CHOIX DES INCOTERMS ---
    with tab2:
        st.subheader("Gestion des Transferts (Incoterms 2020)")
        
        st.markdown("#### 🤖 Assistant de sélection automatique")
        col_auto1, col_auto2 = st.columns(2)
        with col_auto1:
            user_role = st.radio("Votre rôle dans la transaction :", ["Acheteur", "Vendeur"])
        with col_auto2:
            user_resp = st.selectbox("Niveau de prise en charge souhaité :", 
                                   ["Minimum de charges", "Charges équilibrées", "Toutes les charges (Full Risk)"])
        
        auto_incoterm = get_incoterm_recommendation(user_role, user_resp)
        st.info(f"💡 Suggestion automatique : **{auto_incoterm}**")
        
        st.markdown("---")
        
        incoterm_list = ["EXW", "FCA", "FAS", "FOB", "CFR", "CIF", "CPT", "CIP", "DAP", "DPU", "DDP"]
        default_index = incoterm_list.index(auto_incoterm)
        incoterm_selected = st.selectbox("Valider ou modifier l'Incoterm final", incoterm_list, index=default_index)

        incoterm_info = {
            "EXW": {"desc": "L'acheteur assume tous les frais et risques dès l'usine du vendeur.", "avantage": "Contrôle total de la chaîne logistique par l'acheteur."},
            "FOB": {"desc": "Le vendeur livre sur le navire au port de départ.", "avantage": "Évite les frais de pré-acheminement complexes pour l'acheteur."},
            "CIF": {"desc": "Vendeur paie fret et assurance jusqu'au port d'arrivée.", "avantage": "Sécurité pour l'acheteur, coût prévisible à l'arrivée."},
            "DDP": {"desc": "Vendeur assume tout, y compris les taxes au Bénin.", "avantage": "Zéro formalité pour l'acheteur, coût de revient connu à l'avance."}
        }
        
        info = incoterm_info.get(incoterm_selected, {"desc": "Incoterm standard 2020.", "avantage": "Optimisation des coûts internationaux."})
        st.warning(f"**Définition :** {info['desc']}")
        st.success(f"**Avantages :** {info['avantage']}")

    # --- ONGLET 3 : COÛTS & DOCUMENTATION ---
    with tab3:
        st.subheader("Contrôle Documentaire & Calcul des Coûts")
        
        st.markdown("#### Documents nécessaires")
        docs = ["Facture commerciale", "Liste de colisage", "Certificat d'origine"]
        if incoterm_selected in ["CFR", "CIF", "FOB", "FAS"]:
            docs.append("Connaissement (Bill of Lading / B/L)")
        if incoterm_selected in ["CIF", "CIP"]:
            docs.append("Certificat d'assurance transport")
        if incoterm_selected == "DDP":
            docs.append("Bon à enlever (Dédouanement Bénin effectué)")
            
        st.write("Liste de contrôle : ", ", ".join(f"**{d}**" for d in docs))

        st.markdown("---")
        
        col_input1, col_input2 = st.columns(2)
        with col_input1:
            fob_val = st.number_input("Valeur Marchandise (Devise origine)", min_value=0.0)
            rate = st.number_input("Taux de change (ex: 1€ = 655.95 FCFA)", value=655.95)
        with col_input2:
            freight = st.number_input("Coût du Fret International (FCFA)", min_value=0.0)
            insurance = st.number_input("Coût de l'Assurance (FCFA)", min_value=0.0)

        if st.button("Calculer le coût total d'acquisition"):
            results = calculate_landed_cost(fob_val, freight, insurance, rate, incoterm_selected)
            
            st.markdown("#### Détail financier de l'opération")
            res_col1, res_col2 = st.columns(2)
            keys = list(results.keys())
            for i, key in enumerate(keys):
                if i % 2 == 0:
                    res_col1.metric(label=key, value=f"{results[key]:,.0f} FCFA")
                else:
                    res_col2.metric(label=key, value=f"{results[key]:,.0f} FCFA")
            
            # --- GÉNÉRATION AUTOMATIQUE DU RAPPORT PDF ---
            st.markdown("---")
            st.subheader(" Documents à exporter")
            
            # Préparation des données pour la fonction centralisée dans utils.py
            donnees_pdf = {
                "Incoterm": incoterm_selected,
                "Valeur Marchandise": f"{fob_val:,.0f}",
                "Fret": f"{freight:,.0f} FCFA",
                "Assurance": f"{insurance:,.0f} FCFA",
                "Total Taxes": f"{results['Total Taxes']:,.0f} FCFA",
                "COÛT DE REVIENT TOTAL": f"{results['Coût de Revient Total']:,.0f} FCFA"
            }
            
            # Appel de la fonction de utils.py
            pdf_binaire = generate_pdf(donnees_pdf, title=f"RAPPORT D'ACHAT - {incoterm_selected}")
            
            # Bouton de téléchargement PDF
            st.download_button(
                label="📥 Télécharger le Bon de Commande (PDF)",
                data=pdf_binaire,
                file_name=f"Bon_Commande_{incoterm_selected}.pdf",
                mime="application/pdf"
            )
            
            # Export CSV secondaire
            csv = pd.DataFrame([results]).to_csv(index=False).encode('utf-8')
            st.download_button(
                label=" Exporter les données (CSV)",
                data=csv,
                file_name=f"rapport_achat_{incoterm_selected}.csv",
                mime="text/csv"
        )
            
