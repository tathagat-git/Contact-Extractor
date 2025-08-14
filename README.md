<<<<<<< HEAD
Overview

The Contact Extractor Web App is a FastAPI-based application that lets users upload PDFs, images, DOC/DOCX files to automatically extract emails, phone numbers, usernames, and names. It uses OCR (Optical Character Recognition) for images and NLP (Natural Language Processing) to detect names from text. Extracted contacts are saved in a JSON file with timestamps.

Why This Project Exists

Manually extracting contact information from documents is time-consuming. This app automates the process and supports multiple file types (PDF, images, DOC/DOCX), making it easier for anyone to gather structured contact data from different sources quickly.

Key Features

Upload PDFs, images (JPG, PNG), DOCX, or DOC files.

Extract emails, phone numbers, usernames, and names.

OCR support for images using EasyOCR.

NLP support using spaCy for detecting names.

Stores results in results.json with timestamps.

Serves a simple web interface via FastAPI.

Compatible with CPU and optional GPU acceleration for faster processing with PyTorch.

How It Works

File Upload: Users upload files via the front-end.

File Processing:

Text is extracted using pdfplumber for PDFs, docx / docx2txt for DOC/DOCX, and EasyOCR for images.

Contact Extraction:

Emails, phone numbers, usernames, and names are extracted using regex and spaCy NLP.

Save Results:

Extracted contacts are saved in results.json with a timestamp.

Web Interface:

Users can upload files and view results through a simple web page served by FastAPI.

Installation

Clone the repository:

git clone <repo-url>
cd contact_extractor


Create a virtual environment and activate it:

python -m venv venv
# Windows
venv\Scripts\activate



Install required packages:

pip install fastapi uvicorn pdfplumber docx docx2txt spacy easyocr torch torchvision
python -m spacy download en_core_web_sm

CPU vs GPU (PyTorch)

The project uses PyTorch (via EasyOCR) to process images.

CPU: Works on any machine but slower for large images.

GPU: Speeds up processing using NVIDIA CUDA.
To install PyTorch with GPU support:

# Replace cu121 with your CUDA version
pip install torch --index-url https://download.pytorch.org/whl/cu121
pip install torchvision --index-url https://download.pytorch.org/whl/cu121
=======
# Contact Extractor Web App

[![Python](https://img.shields.io/badge/python-3.12-blue)](https://www.python.org/) [![FastAPI](https://img.shields.io/badge/FastAPI-0.102-green)](https://fastapi.tiangolo.com/) [![PyTorch](https://img.shields.io/badge/PyTorch-2.5-red)](https://pytorch.org/)

---

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
>>>>>>> 5b31457 (Update upload folder and README)
