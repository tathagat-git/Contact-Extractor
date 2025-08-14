from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from storage import save_results_to_json
from extractor import process_file  # process_file already returns contacts
import shutil
import os

app = FastAPI()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Serve static files like JS/CSS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve index.html for the main page
@app.get("/")
def serve_index():
    return FileResponse("static/index.html")

# Handle file uploads
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract contacts directly using process_file
    contacts = process_file(file_path)

    # Save results to JSON
    save_results_to_json(contacts)

    return contacts
