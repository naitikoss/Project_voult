import os

def ensure_dirs():
    os.makedirs("vault/.secure_data/files", exist_ok=True)
