from fpdf import FPDF

def generate_pdf(data, title="BON DE COMMANDE"):
    pdf = FPDF()
    pdf.add_page()
    
    # En-tête industrielle
    pdf.set_font("Arial", "B", 16)
    pdf.cell(190, 10, title, ln=True, align="C")
    pdf.ln(10)
    
    # Détails du document
    pdf.set_font("Arial", "", 12)
    for key, value in data.items():
        pdf.cell(100, 10, f"{key}: {value}", ln=True)
    
    return pdf.output() # Retourne le contenu binaire du PDF
