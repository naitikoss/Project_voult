import json
import os
import datetime

META_FILE = "vault/.secure_data/metadata.json"


def load_all():
    if not os.path.exists(META_FILE):
        return []

    with open(META_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    # SAFETY: if file is corrupted or dict, reset to list
    if not isinstance(data, list):
        return []

    return data


def save_metadata(file_id, original_path):
    data = load_all()

    data.append({
        "file_id": file_id,
        "original_path": original_path,
        "encrypted_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    os.makedirs(os.path.dirname(META_FILE), exist_ok=True)
    with open(META_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def load_metadata(file_id):
    for item in load_all():
        if item["file_id"] == file_id:
            return item
    return None


def delete_metadata(file_id):
    data = [i for i in load_all() if i["file_id"] != file_id]
    with open(META_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def list_files():
    return load_all()
