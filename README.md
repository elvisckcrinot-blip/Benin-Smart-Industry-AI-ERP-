# Bénin Industrie Intelligente : Système ERP Intégré Supply Chain 4.0

## Présentation Générale
Bénin Industrie Intelligente est un écosystème logiciel de type ERP (Enterprise Resource Planning) conçu pour répondre aux défis spécifiques du secteur industriel béninois. Cette solution fusionne l'ingénierie logistique traditionnelle et l'intelligence artificielle pour optimiser la chaîne de valeur, du dédouanement à la maintenance prédictive des lignes de production.

## Architecture Modulaire

### 1. Gestion des Achats et Marchés Publics
* **Conformité Fiscale :** Moteur de calcul intégrant le Tarif Extérieur Commun (TEC) de la CEDEAO et la TVA béninoise (18%) pour une détermination précise du coût de revient.
* **Intelligence Contractuelle :** Simulateur dynamique d'Incoterms 2020 avec masquage automatique des variables de coût non pertinentes selon le transfert de risque et de propriété.
* **Digitalisation :** Module d'extraction de données pour les appels d'offres (GPAO) avec fonctionnalité d'exportation des données critiques en format PDF.

### 2. Warehouse Management System (WMS)
* **Analyse Prédictive :** Implémentation du modèle Random Forest pour la prédiction de la demande et l'ajustement des quantités économiques de commande (EOQ).
* **Optimisation Opérationnelle :** Segmentation dynamique ABC couplée à une gestion rigoureuse des flux FIFO/FEFO selon l'état de stock (Optimal, Moyen, Critique).
* **Sûreté des Stocks :** Calcul du stock de sécurité basé sur l'écart-type des délais de livraison observés au Port Autonome de Cotonou.

### 3. Production et Maintenance Industrielle (MES)
* **Pilotage des Flux :** Configuration multi-modèle permettant de basculer entre les flux Poussés, Tirés (Kanban numérique), Synchrones ou Juste-à-Temps.
* **Maintenance 4.0 :** Algorithmes de détection d'anomalies basés sur la télémétrie des machines (vibration, température, pression) pour l'anticipation du MTBF (Mean Time Between Failures).
* **OEE/TRS :** Dashboard de monitoring en temps réel du Taux de Rendement Synthétique et aide au diagnostic assisté par IA.

### 4. Transport Management System (TMS)
* **Suivi de Corridor :** Cartographie précise des axes routiers nationaux (RNIE 1 à 7) pour le monitoring des flux transfrontaliers vers le Niger, le Nigeria, le Burkina Faso et le Togo.
* **Ingénierie du Transport :** Optimisation de la charge utile par voyage et calcul de rentabilité kilométrique intégrant la volatilité du prix du carburant.
* **Logistique Inverse :** Protocole de traitement des retours (Avarie, Non-conformité) avec boucle de rétroaction vers le module de contrôle qualité Production.

## Spécifications Techniques

### Stack Logicielle
* **Interface Utilisateur :** Streamlit (Thème industriel haute densité, CSS personnalisé).
* **Traitement de Données :** Python 3.10+ (Pandas, NumPy).
* **Machine Learning :** Scikit-learn (Random Forest Regressor), Inférence via Joblib.
* **Moteur Géographique :** Folium / GeoJSON pour la visualisation des corridors logistiques.
* **Reporting :** FPDF pour la génération automatique de bons de retour et rapports d'achat.

### Structure du Répertoire
```text
├── .streamlit/           # Configurations de l'interface et styles CSS
├── core/                 # Algorithmes métier, calculs fiscaux et logique IA
│   ├── models_ai/        # Sérialisation des modèles pré-entraînés (.joblib)
│   └── geo_utils.py      # Traitement des données géospatiales des RNIE
├── modules/              # Composants UI Streamlit (Achat, WMS, Production, TMS)
├── data/                 # Référentiels géographiques et datasets d'entraînement
├── assets/               # Modèles de documents officiels et iconographie technique
└── requirements.txt      # Liste exhaustive des dépendances logicielles
