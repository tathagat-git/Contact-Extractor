
## Overview

The **Contact Extractor Web App** is a FastAPI-based application that allows users to upload **PDFs, images, DOC/DOCX files** and automatically extract **emails, phone numbers, usernames, and names**.

* Uses **OCR (EasyOCR)** for images.
* Uses **NLP (spaCy)** for detecting names.
* Saves extracted contacts in a **JSON file with timestamps**.

---

## Why This Project Exists

Manually extracting contacts is slow. This app automates extraction from multiple file types, making it easier to gather structured contact data quickly.

---

## Key Features

* Upload PDFs, images (JPG/PNG), DOCX, or DOC files
* Extract emails, phone numbers, usernames, and names
* OCR support for images using **EasyOCR**
* NLP support using **spaCy** for detecting names
* Saves results in `results.json` with timestamps
* Simple web interface via FastAPI
* Compatible with **CPU** and optional **GPU** (PyTorch)

---

## How It Works

1. **File Upload:** Users upload files via the front-end
2. **File Processing:**

   * PDFs → `pdfplumber`
   * DOC/DOCX → `docx` / `docx2txt`
   * Images → `EasyOCR`
3. **Contact Extraction:** Regex + spaCy NLP
4. **Save Results:** Stored in `results.json` with timestamp
5. **Web Interface:** View results via FastAPI front-end

---

## Installation

1. Clone the repository:

```bash
git clone <repo-url>
cd contact_extractor
```

2. Create and activate virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

4. Download spaCy English model:

```bash
python -m spacy download en_core_web_sm
```

---

## CPU vs GPU (PyTorch)

* **CPU:** Works on any machine but slower for large images
* **GPU:** Speeds up processing using NVIDIA CUDA

Install PyTorch with GPU support:

```bash
pip install torch --index-url https://download.pytorch.org/whl/cu121
pip install torchvision --index-url https://download.pytorch.org/whl/cu121
```

Check GPU availability:

```python
import torch
print(torch.cuda.is_available())  # True if GPU detected
print(torch.cuda.get_device_name(0))
```

---

## Usage

Run FastAPI server:

```bash
uvicorn main:app --reload
```

Open browser at `http://127.0.0.1:8000/` to upload files and see extracted contacts.

---

## Folder Structure

```
contact_extractor/
├── main.py           # FastAPI app
├── storage.py        # Save results to JSON
├── extractor.py      # Extract contacts from files
├── uploads/          # Uploaded files
├── static/           # Frontend HTML, JS, CSS
├── results.json      # Extracted contacts with timestamps
├── requirements.txt  # Python dependencies
```

---

## Requirements

Create a `requirements.txt` with:

```
fastapi
uvicorn
pdfplumber
docx
docx2txt
spacy
easyocr
torch
torchvision
```

Install using:

```bash
pip install -r requirements.txt
```


