
import os
from PyPDF2 import PdfReader

def load_pdf_text(pdf_path):
    """Extracts and returns text from a PDF file."""
    text = ""
    try:
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return ""
    
def load_all_pdfs(directory):
    """Loads and extracts text from all PDFs in a given directory."""
    pdf_texts = {}
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            full_path = os.path.join(directory, filename)
            pdf_texts[filename] = load_pdf_text(full_path)
    return pdf_texts
