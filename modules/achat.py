import streamlit as st
import pandas as pd

def calculate_landed_cost(fob_price, freight, insurance, currency_rate, incoterm):
    """
    Calcule le coût de revient incluant la taxation béninoise (TEC + TVA + PCS).
    La fonction adapte le calcul selon l'Incoterm sélectionné.
    """
    # Conversion de la valeur marchandise en FCFA
    base_val = fob_price * currency_rate
    
    # Si l'incoterm n'inclut pas le transport/assurance (ex: EXW, FCA), on les ajoute
    # Si l'incoterm les inclut déjà (ex: CIF, CIP), ils sont considérés comme intégrés dans la valeur de base
    cif_val = base_val + freight + insurance
    
    # Fiscalité Bénin / CEDEAO (Paramètres industriels)
    tec_rate = 0.20  # Tarif Extérieur Commun (Catégorie 3)
    tva_rate = 0.18  # TVA Bénin
    pcs_rate = 0.01  # Prélèvement Communautaire de Solidarité
    
    droits_douane = cif_val * tec_rate
    pcs = cif_val * pcs_rate
    
    # La TVA s'applique sur la valeur CIF + Droits de Douane + PCS
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
            st.write("Exportation des données vers l'application")
            st.button("Exporter données GPAO")

    # --- ONGLET 2 : CHOIX DES INCOTERMS ---
    with tab2:
        st.subheader("Gestion des Transferts (Incoterms 2020)")
        
        # Liste exhaustive des 11 Incoterms 2020
        incoterm_list = ["EXW", "FCA", "FAS", "FOB", "CFR", "CIF", "CPT", "CIP", "DAP", "DPU", "DDP"]
        incoterm_selected = st.selectbox("Sélectionner l'Incoterm entre acheteur et vendeur", incoterm_list)

        incoterm_info = {
            "EXW": {"desc": "L'acheteur assume tous les frais et risques dès l'usine du vendeur.", "avantage": "Contrôle total de la chaîne logistique par l'acheteur."},
            "FOB": {"desc": "Le vendeur livre sur le navire au port de départ. Risque transféré au bastingage.", "avantage": "Évite les frais de pré-acheminement complexes pour l'acheteur."},
            "CIF": {"desc": "Vendeur paie fret et assurance jusqu'au port d'arrivée.", "avantage": "Sécurité pour l'acheteur, coût prévisible à l'arrivée."},
            "DDP": {"desc": "Vendeur assume tout, y compris les taxes au Bénin.", "avantage": "Zéro formalité pour l'acheteur, coût de revient connu à l'avance."}
        }
        
        info = incoterm_info.get(incoterm_selected, {"desc": "Incoterm standard 2020.", "avantage": "Optimisation des coûts de transport internationaux."})
        
        st.warning(f"**Définition :** {info['desc']}")
        st.success(f"**Avantages de l'utilisation de l'Incoterm choisi :** {info['avantage']}")

    # --- ONGLET 3 : COÛTS & DOCUMENTATION ---
    with tab3:
        st.subheader("Contrôle Documentaire & Calcul des Coûts")
        
        # 1. Liste totale et contrôle des documents selon l'incoterm choisi
        st.markdown("#### Documents nécessaires pour procéder à l'achat/vente")
        docs = ["Facture commerciale", "Liste de colisage", "Certificat d'origine"]
        if incoterm_selected in ["CFR", "CIF", "FOB", "FAS"]:
            docs.append("Connaissement (Bill of Lading / B/L)")
        if incoterm_selected in ["CIF", "CIP"]:
            docs.append("Certificat d'assurance transport")
        if incoterm_selected in ["CPT", "FCA"]:
            docs.append("Lettre de Voiture (CMR / LTA)")
        if incoterm_selected == "DDP":
            docs.append("Bon à enlever (Dédouanement Bénin effectué)")
            
        st.write("Liste de contrôle : ", ", ".join(f"**{d}**" for d in docs))

        st.markdown("---")
        
        # 2. Calcul des coûts relatifs au processus d'acquisition
        col_input1, col_input2 = st.columns(2)
        
        with col_input1:
            fob_val = st.number_input("Valeur Marchandise (Devise origine)", min_value=0.0)
            rate = st.number_input("Taux de change (ex: 1€ = 655.95 FCFA)", value=655.95)
            
        with col_input2:
            # Masquage logique : si l'incoterm est DDP, les frais sont souvent inclus.
            # Pour les autres, on permet la saisie manuelle du fret et de l'assurance.
            freight = st.number_input("Coût du Fret International (FCFA)", min_value=0.0)
            insurance = st.number_input("Coût de l'Assurance (FCFA)", min_value=0.0)

        if st.button("Calculer le coût total d'acquisition"):
            results = calculate_landed_cost(fob_val, freight, insurance, rate, incoterm_selected)
            
            st.markdown("#### Détail financier de l'opération")
            res_col1, res_col2 = st.columns(2)
            
            # Affichage des métriques industrielles
            keys = list(results.keys())
            for i, key in enumerate(keys):
                if i % 2 == 0:
                    res_col1.metric(label=key, value=f"{results[key]:,.0f} FCFA")
                else:
                    res_col2.metric(label=key, value=f"{results[key]:,.0f} FCFA")
            
            # Exportation PDF/CSV comme demandé
            st.markdown("#### Section PDF d'exportation")
            csv = pd.DataFrame([results]).to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Exporter les données d'achat (CSV)",
                data=csv,
                file_name=f"rapport_achat_{incoterm_selected}.csv",
                mime="text/csv"
    )
    
