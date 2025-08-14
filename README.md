# AI Contact Extractor

This is a FastAPI-based web application that extracts names, emails, phone numbers, and usernames from PDF, DOC/DOCX, and image files.

## Setup
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
uvicorn main:app --reload
```
Open `http://127.0.0.1:8000` in your browser.
