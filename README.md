# Benin-Smart-Industry-AI-ERP-
AI-ERP pour l'Industrie au Bénin | Solution intégrée de Supply Chain 4.0 utilisant FastAPI &amp; Streamlit. Optimisation des flux, maintenance prédictive (IA) et conformité douanière.
#  Benin Smart Industry (AI-ERP)

**Benin Smart Industry** est une plateforme ERP intelligente conçue pour digitaliser et optimiser les flux industriels et logistiques. L'application combine la puissance de **FastAPI** pour le traitement de données (IA) et l'ergonomie de **Streamlit** pour le pilotage opérationnel.

##  Vision du Projet
Transformer la gestion de la Supply Chain au Bénin en intégrant des outils prédictifs adaptés aux réalités locales (dédouanement, logistique routière, maintenance industrielle).

##  Architecture des Modules

###  1. Achats & Marchés
- **Simulateur d'Incoterms 2020** : Choix optimal du transfert de risques.
- **Calculateur de Taxes Bénin** : Estimation précise des droits de douane (TEC, TVA, PCS).

###  2. WMS (Warehouse Management System)
- **Prévision de la Demande** : Modèle de Machine Learning (**Random Forest**) pour anticiper les ruptures.
- **Gestion ABC** : Classification dynamique des stocks pour optimiser l'espace.

###  3. Production & Maintenance
- **Maintenance Proactive** : Analyse en temps réel des vibrations et températures pour éviter les arrêts non planifiés.
- **Flux JAT (Juste-à-Temps)** : Synchronisation de la fabrication avec la demande réelle.

###  4. TMS (Transport Management System)
- **Tracking & Docking** : Suivi des flux Cotonou-Bohicon-Parakou.
- **Audit Carburant** : Optimisation du coût à la tonne transportée.

##  Stack Technique
- **Backend** : FastAPI (Python)
- **Frontend** : Streamlit
- **IA/ML** : Scikit-learn (Random Forest Regressor), Pandas
- **Déploiement** : GitHub Actions & Docker (prévu)

## 📂 Structure du Répertoire
- `/main.py` : Point d'entrée de l'API FastAPI.
- `/core` : Logique métier de base (Incoterms, devises).
- `/modules` : Intelligence spécifique par département (WMS, TMS, Production).
- `/data` : Datasets d'entraînement pour les modèles d'IA.

---
**Développé par Elvis CRINOT - Expert en Logistique & Supply Chain 4.0**
