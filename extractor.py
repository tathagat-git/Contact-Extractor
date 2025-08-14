import re
import os
import pdfplumber
import docx
import docx2txt
import spacy
import easyocr  # New OCR library

nlp = spacy.load("en_core_web_sm")

# Initialize EasyOCR reader (English only here)
reader = easyocr.Reader(['en'])

def extract_text_from_pdf(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def extract_text_from_image(path):
    result = reader.readtext(path, detail=0)  # Returns list of text strings
    return "\n".join(result)

def extract_text_from_docx(path):
    doc = docx.Document(path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text_from_doc(path):
    # Use docx2txt for old .doc files
    return docx2txt.process(path)

def extract_contacts_from_text(text):
    results = {
        "emails": re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", text),
        "phones": re.findall(r"\+?\d[\d -]{8,}\d", text),
        "usernames": re.findall(r"@\w+|\b\w+_\w+\b", text),
        "names": [ent.text for ent in nlp(text).ents if ent.label_ == "PERSON"]
    }
    return results

def process_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".pdf":
        text = extract_text_from_pdf(file_path)
    elif ext in [".jpg", ".jpeg", ".png"]:
        text = extract_text_from_image(file_path)
    elif ext == ".docx":
        text = extract_text_from_docx(file_path)
    elif ext == ".doc":
        text = extract_text_from_doc(file_path)
    else:
        return {"error": "Unsupported file type"}
    
    return extract_contacts_from_text(text)
