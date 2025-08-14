import os, json
from datetime import datetime

RESULTS_FILE = "results.json"

def save_results_to_json(data):
    # Check if results.json exists
    if os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, "r") as f:
            try:
                all_results = json.load(f)  # load existing
            except json.JSONDecodeError:   # file is empty or invalid
                all_results = []
    else:
        all_results = []

    # Append new record with timestamp
    all_results.append({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "data": data
    })

    # Save updated list back to file
    with open(RESULTS_FILE, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=4, ensure_ascii=False)
