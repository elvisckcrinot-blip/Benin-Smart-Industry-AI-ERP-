incoterms_data = {
    "GROUPE_E": {
        "EXW": {
            "nom": "Ex Works",
            "famille": "Depart",
            "documents": ["Facture normalisee", "Liste de colisage"],
            "transfert_risque": "Usine depart"
        }
    },
    "GROUPE_F": {
        "FCA": {"nom": "Free Carrier", "famille": "Transport principal non paye", "documents": ["Facture", "Liste colisage", "Recu transportaire"]},
        "FOB": {"nom": "Free On Board", "famille": "Transport principal non paye", "documents": ["Facture", "Liste colisage", "Connaissement maritime", "BSC"]}
    },
    "GROUPE_C": {
        "CFR": {"nom": "Cost and Freight", "famille": "Transport principal paye", "documents": ["Facture", "BSC", "Connaissement"]},
        "CIF": {"nom": "Cost, Insurance and Freight", "famille": "Transport principal paye", "documents": ["Facture", "Police assurance", "BSC", "Connaissement"]}
    },
    "GROUPE_D": {
        "DAP": {"nom": "Delivered At Place", "famille": "Arrivee", "documents": ["Facture", "BSC", "Certificat origine"]},
        "DDP": {"nom": "Delivered Duty Paid", "famille": "Arrivee", "documents": ["Facture", "Attestation de valeur", "BSC", "Quittance douane"]}
    }
}
