import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            try:
                text += page.get_text()
            except Exception as e:
                print(f"Failed to read a page: {e}")
    except Exception as e:
        print(f"Failed to open PDF: {e}")
    return text
