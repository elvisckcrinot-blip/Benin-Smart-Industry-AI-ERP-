incoterms_data = {
    "GROUPE_E_DEPART": {
        "EXW": {
            "nom": "Ex Works",
            "vendeur_obligations": "Mise a disposition a l usine",
            "acheteur_obligations": "Chargement, transport export, transport principal, douane, assurance",
            "documents_requis": ["Facture commerciale", "Liste de colisage"],
            "risque_niveau": "Maximum pour l acheteur",
            "note_benin": "A n utiliser que si vous maitrisez toute la chaine logistique depuis le pays d origine."
        }
    },
    "GROUPE_F_TRANSPORT_PRINCIPAL_NON_PAYE": {
        "FCA": {
            "nom": "Free Carrier",
            "vendeur_obligations": "Dedouanement export et remise au transporteur",
            "acheteur_obligations": "Transport principal, assurance, douane import",
            "documents_requis": ["Facture", "Liste de colisage", "Titre de transport"],
            "note_benin": "Recommande pour le groupage aerien ou maritime."
        },
        "FAS": {
            "nom": "Free Alongside Ship",
            "vendeur_obligations": "Livraison le long du navire au port de depart",
            "acheteur_obligations": "Chargement navire, fret, assurance, douane import",
            "documents_requis": ["Facture", "Liste de colisage", "Recu de mise a quai"],
            "note_benin": "Principalement pour le vrac (engrais, clinker)."
        },
        "FOB": {
            "nom": "Free On Board",
            "vendeur_obligations": "Chargement a bord du navire",
            "acheteur_obligations": "Fret maritime, assurance, douane import",
            "documents_requis": ["Facture", "Liste de colisage", "Connaissement maritime (B/L)", "BSC"],
            "note_benin": "Standard pour les conteneurs pleins (FCL) vers Cotonou."
        }
    },
    "GROUPE_C_TRANSPORT_PRINCIPAL_PAYE": {
        "CFR": {
            "nom": "Cost and Freight",
            "vendeur_obligations": "Transport jusqu au port de Cotonou",
            "acheteur_obligations": "Assurance marchandise, douane import",
            "documents_requis": ["Facture", "B/L", "Liste de colisage", "BSC"],
            "note_benin": "L acheteur doit imperativement souscrire une assurance locale."
        },
        "CIF": {
            "nom": "Cost, Insurance and Freight",
            "vendeur_obligations": "Fret et assurance jusqu a Cotonou",
            "acheteur_obligations": "Dechargement, douane import",
            "documents_requis": ["Facture", "Police d assurance", "B/L", "BSC"],
            "note_benin": "Sert de base de calcul pour la valeur en douane au Benin."
        },
        "CPT": {
            "nom": "Carriage Paid To",
            "vendeur_obligations": "Transport paye jusqu au point convenu",
            "acheteur_obligations": "Assurance, douane import",
            "documents_requis": ["Facture", "Lettre de voiture (LTA/CMR)"],
            "note_benin": "Adapte pour le transport multimodal vers Bohicon ou Parakou."
        },
        "CIP": {
            "nom": "Carriage and Insurance Paid To",
            "vendeur_obligations": "Transport et assurance payes",
            "acheteur_obligations": "Douane import",
            "documents_requis": ["Facture", "Police d assurance", "Titre de transport"],
            "note_benin": "Equivalent multimodal du CIF."
        }
    },
    "GROUPE_D_ARRIVEE": {
        "DAP": {
            "nom": "Delivered At Place",
            "vendeur_obligations": "Livraison au point convenu au Benin (ex: Usine Glo-Djigbe)",
            "acheteur_obligations": "Dedouanement import et taxes",
            "documents_requis": ["Facture", "Certificat d origine", "BSC"],
            "note_benin": "Le vendeur gere le transport mais pas les taxes douanieres."
        },
        "DPU": {
            "nom": "Delivered at Place Unloaded",
            "vendeur_obligations": "Livraison et dechargement au point convenu",
            "acheteur_obligations": "Dedouanement import",
            "documents_requis": ["Facture", "Liste de colisage", "Certificat d origine"],
            "note_benin": "Incoterm ou le vendeur assume le dechargement du camion/conteneur."
        },
        "DDP": {
            "nom": "Delivered Duty Paid",
            "vendeur_obligations": "Livraison tout frais payes, douane incluse",
            "acheteur_obligations": "Dechargement final uniquement",
            "documents_requis": ["Facture normalisee", "Quittance de douane", "BSC"],
            "note_benin": "Tres couteux car le vendeur inclut une marge de securite sur les taxes."
        }
    }
}
