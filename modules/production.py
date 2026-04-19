import streamlit as st
import pandas as pd
import numpy as np
import time

def run_module():
    st.header("Module 03 : Pilotage de la Production & Maintenance 4.0")
    
    tab1, tab2, tab3 = st.tabs([
        "Pilotage des Flux (Push/Pull/JIT)", 
        "Maintenance Prédictive & IA", 
        "Planification & Pièces de Rechange"
    ])

    # --- ONGLET 1 : PILOTAGE DES FLUX ---
    with tab1:
        st.subheader("Configuration du Mode de Pilotage des Flux")
        col_flux1, col_flux2 = st.columns([1, 2])
        
        with col_flux1:
            mode_flux = st.radio(
                "Sélectionner le modèle de déclenchement :",
                ["Flux poussé (Push)", "Flux tiré (Pull)", "Flux synchrone", "Flux tendu (Juste-à-temps)"]
            )
            st.button("Actualiser la ligne de production")
        
        with col_flux2:
            if mode_flux == "Flux poussé (Push)":
                st.info("Logique : Production basée sur les prévisions IA pour éviter le surstock.")
            elif mode_flux == "Flux tiré (Pull)":
                st.info("Logique : Système Kanban numérique - Déclenchement sur commande réelle.")
            elif mode_flux == "Flux synchrone":
                st.info("Logique : Assemblage dans l'ordre exact d'entrée sur ligne (Standard Automobile).")
            else:
                st.info("Logique : Suppression totale des stocks intermédiaires (JIT).")
            
            st.markdown("#### Performance de la Ligne (OEE/TRS)")
            st.progress(0.82)
            st.caption("Taux de Rendement Synthétique actuel : 82%")

    # --- ONGLET 2 : MAINTENANCE PRÉDICTIVE & IA ---
    with tab2:
        st.subheader("Surveillance en Temps Réel & Analyse IA")
        
        col_monitor1, col_monitor2 = st.columns(2)
        
        with col_monitor1:
            st.markdown("#### État des Équipements (Condition Monitoring)")
            sensor_data = pd.DataFrame({
                "Paramètre": ["Vibrations (mm/s)", "Température (°C)", "Pression (bar)", "Vitesse (tr/min)"],
                "Valeur Actuelle": [2.4, 65.2, 12.1, 1450],
                "Ligne de Base": [2.1, 60.0, 12.0, 1500],
                "Statut": ["Normal", "Attention", "Normal", "Normal"]
            })
            st.table(sensor_data)
        
        with col_monitor2:
            st.markdown("#### Diagnostic Assisté par l'IA")
            anomaly_score = 0.18
            if anomaly_score < 0.20:
                st.success("Santé machine : Optimale. Aucune anomalie critique détectée.")
            
            st.write("**Analyse Prédictive :** Usure du roulement estimée à 45%.")
            st.write("**Prédiction défaillance :** Prochaine panne probable dans 18 jours.")
            
            if st.button("Lancer un diagnostic profond"):
                with st.spinner("L'IA analyse les manuels techniques..."):
                    time.sleep(1)
                    st.write("Suggestion : Vérifier le graissage du palier de l'axe principal.")

    # --- ONGLET 3 : PLANIFICATION & PIÈCES DE RECHANGE ---
    with tab3:
        st.subheader("Gestion Intelligente des Interventions")
        
        col_plan1, col_plan2 = st.columns(2)
        
        with col_plan1:
            st.markdown("#### Bons de Travail Automatisés")
            interventions = pd.DataFrame({
                "ID": ["BT-001", "BT-002"],
                "Machine": ["Presse-04", "Convoyeur-A"],
                "Type": ["Préventif", "IA-Prédictif"],
                "Priorité": ["Haute", "Moyenne"],
                "Date Prévue": ["2026-04-20", "2026-05-02"]
            })
            st.dataframe(interventions, use_container_width=True)
            
            # Export CSV des Bons de Travail
            csv_bt = interventions.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Exporter les Bons de Travail (CSV)",
                data=csv_bt,
                file_name=f"Bons_de_Travail_{time.strftime('%Y%m%d')}.csv",
                mime="text/csv",
                use_container_width=True
            )

        with col_plan2:
            st.markdown("#### Stock des Pièces de Rechange")
            st.warning("Alerte IA : Commande automatique à lancer pour 'Roulement SKF-202'.")
            st.write("Disponibilité magasin : **Rupture imminente**")
            st.button("Valider la commande automatique")

        st.markdown("---")
        st.markdown("#### Analyse des Bénéfices Attendus")
        b_col1, b_col2, b_col3 = st.columns(3)
        b_col1.metric("Réduction Coûts", "-30%", "Cible")
        b_col2.metric("Durée de Vie", "+15%", "Optimisé")
        b_col3.metric("Sécurité", "100%", "Zéro incident")
        
        # Export CSV du Rapport Global
        export_df = pd.DataFrame({
            "Indicateur": ["Réduction Coûts", "Durée de Vie", "Sécurité", "OEE Actuel", "Mode de Flux"],
            "Valeur": ["-30%", "+15%", "100%", "82%", mode_flux]
        })
        csv_global = export_df.to_csv(index=False).encode('utf-8')
        
        st.download_button(
            label="📊 Exporter Rapport de Production & Maintenance (CSV)",
            data=csv_global,
            file_name=f"Rapport_Global_Production_{time.strftime('%Y%m%d')}.csv",
            mime="text/csv",
            use_container_width=True
                )
            
