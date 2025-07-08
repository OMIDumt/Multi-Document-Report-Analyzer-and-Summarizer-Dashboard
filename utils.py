import fitz  # PyMuPDF
import io

def load_pdf_text(uploaded_file):
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        return "\n".join([page.get_text() for page in doc])

def load_txt_text(uploaded_file):
    return uploaded_file.read().decode("utf-8")
