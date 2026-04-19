import streamlit as st
import pandas as pd
import numpy as np

def calculate_fuel_efficiency(distance, weight, fuel_price):
    """Calcule la rentabilité du carburant et le prix de revient du voyage."""
    consumption_rate = 0.35  # Litres par km pour un poids lourd standard
    load_factor = 1 + (weight / 40)  # Augmentation de la consommation selon le poids (max 40t)
    total_fuel = distance * consumption_rate * load_factor
    fuel_cost = total_fuel * fuel_price
    fixed_costs = 50000  # Amortissement, chauffeur, maintenance par voyage
    total_trip_cost = fuel_cost + fixed_costs
    return round(total_trip_cost, 0), round(fuel_cost, 0)

def run_module():
    st.header("Module 04 : Transport Management System (TMS) & Corridors")
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Docking & Quais", 
        "Tracking Corridors RNIE", 
        "Optimisation de Charge", 
        "Rentabilité Carburant",
        "Logistique Inverse"
    ])

    # --- ONGLET 1 : DOCKING ---
    with tab1:
        st.subheader("Gestion du Docking (Entrées/Sorties)")
        col_dock1, col_dock2 = st.columns(2)
        with col_dock1:
            camion_id = st.text_input("Numéro matricule du camion", placeholder="ex: BH 4567 RB")
            marchandise = st.selectbox("Nature de la marchandise", ["Coton", "Soja", "Maïs", "Cajou", "Gaz", "Ciment"])
            quai = st.selectbox("Affectation au Quai", ["Quai A1 (Réception)", "Quai B1 (Expédition)", "Zone Vrac"])
        
        with col_dock2:
            st.markdown("#### État du Chargement")
            status_dock = st.radio("Opération", ["En attente", "Chargement", "Déchargement", "Terminé"])
            st.button("Enregistrer le mouvement de quai")
        
        st.button("Télécharger le bon de docking (PDF)", key="dl_dock")

    # --- ONGLET 2 : TRACKING CORRIDORS RNIE ---
    with tab2:
        st.subheader("Suivi Géographique des Flux (Axes RNIE)")
        st.info("Visualisation des corridors stratégiques Nord-Sud (RNIE 2) et Est-Ouest (RNIE 1)")
        
        corridors = {
            "RNIE 2 (Nord)": "Cotonou – Parakou – Kandi – Malanville (Corridor Niger)",
            "RNIE 3 (Nord-Ouest)": "Dassa – Djougou – Natitingou – Porga (Frontière Burkina)",
            "RNIE 1 (Sud)": "Cotonou – Porto-Novo – Kraké (Frontière Nigeria)",
            "RNIE 1 (Côtière)": "Cotonou – Ouidah – Hillacondji (Frontière Togo)"
        }
        
        axe_selectionne = st.selectbox("Sélectionner l'axe routier", list(corridors.keys()))
        st.write(f"**Itinéraire :** {corridors[axe_selectionne]}")
        
        # Simulation de tracking
        tracking_data = pd.DataFrame({
            "Camion": ["T-102", "T-105", "T-108"],
            "Position Actuelle": ["Bohicon", "Kandi", "Ouidah"],
            "Destination": ["Malanville", "Niamey", "Lomé"],
            "État": ["En transit", "Incident (Panne)", "Arrivé"]
        })
        
        def color_status(val):
            color = 'orange' if val == 'En transit' else 'red' if val == 'Incident (Panne)' else 'green'
            return f'color: {color}; font-weight: bold'

        st.table(tracking_data.style.applymap(color_status, subset=['État']))

    # --- ONGLET 3 : OPTIMISATION DE CHARGE ---
    with tab3:
        st.subheader("Calcul de Charge de Sécurité")
        st.write("Éviter les pannes mécaniques par surcharge sur les axes critiques.")
        
        type_marchandise = st.radio("Unité de mesure", ["Tonne (t)", "Kilogramme (kg)"])
        charge_max = st.number_input("Capacité maximale du véhicule (t)", value=30.0)
        charge_actuelle = st.slider("Charge réelle prévue", 0.0, 45.0, 25.0)
        
        if charge_actuelle > charge_max:
            st.error(f"Surcharge détectée : {charge_actuelle - charge_max}t au-dessus de la limite.")
        else:
            st.success("Chargement conforme aux normes de sécurité routière.")

    # --- ONGLET 4 : RENTABILITÉ CARBURANT ---
    with tab4:
        st.subheader("Optimisation du Coût du Voyage")
        col_fuel1, col_fuel2 = st.columns(2)
        
        with col_fuel1:
            distance = st.number_input("Distance du voyage (km)", value=750) # Distance Cotonou-Malanville
            prix_carburant = st.number_input("Prix du carburant (FCFA/L)", value=650)
            poids = st.number_input("Poids du chargement (t)", value=25.0)
        
        with col_fuel2:
            total_cost, fuel_only = calculate_fuel_efficiency(distance, poids, prix_carburant)
            st.metric("Coût Total du Voyage", f"{total_cost:,.0f} FCFA")
            st.metric("Part du Carburant", f"{fuel_only:,.0f} FCFA")
            st.write("**Indicateur :** Fixer un prix de transport supérieur à ce seuil de rentabilité.")

    # --- ONGLET 5 : LOGISTIQUE INVERSE ---
    with tab5:
        st.subheader("Reverse Logistics — reverse_logistics.py")
        
        col_rev1, col_rev2 = st.columns(2)
        with col_rev1:
            st.markdown("#### Enregistrement du Retour")
            n_camion = st.text_input("N° Camion (Retour)", key="rev_cam")
            motif = st.selectbox("Motif du retour", ["Avarie", "Non-conformité", "Excédent de livraison", "Erreur commande"])
            decision = st.radio("Décision de traitement", ["Retour fournisseur", "Reconditionnement", "Recyclage", "Destruction"])
        
        with col_rev2:
            st.markdown("#### Impact Financier")
            valeur_recup = st.number_input("Valeur récupérée (FCFA)", value=0)
            perte_seche = st.number_input("Perte sèche (FCFA)", value=0)
            st.metric("Status du Dossier", "OUVERT")
            
        st.markdown("---")
        st.button("Exporter Bon de Retour (PDF)")
  
