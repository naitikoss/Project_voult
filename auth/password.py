import hashlib
import os

PASS_FILE = "database/pass.hash"

def set_password(password):
    os.makedirs("database", exist_ok=True)
    h = hashlib.sha256(password.encode()).hexdigest()
    with open(PASS_FILE, "w") as f:
        f.write(h)

def check_password(password):
    if not os.path.exists(PASS_FILE):
        return False
        
    with open(PASS_FILE, "r") as f:
        return hashlib.sha256(password.encode()).hexdigest() == f.read()

def is_password_set():
    return os.path.exists(PASS_FILE)

def reset_password():
    if os.path.exists(PASS_FILE):
        os.remove(PASS_FILE)
