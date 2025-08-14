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
