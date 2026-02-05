import os
import uuid
from cryptography.fernet import Fernet
from vault.metadata import save_metadata
from crypto.keygen import derive_key_from_password
from auth.session import get_session_password

VAULT_PATH = "vault/.secure_data/files"


def encrypt_and_store(file_path):
    os.makedirs(VAULT_PATH, exist_ok=True)

    password = get_session_password()
    if not password:
        raise RuntimeError("Vault is locked. No session password.")

    with open(file_path, "rb") as f:
        data = f.read()

    key = derive_key_from_password(password)
    cipher = Fernet(key)
    encrypted = cipher.encrypt(data)

    file_id = f"{uuid.uuid4().hex}.vault"
    vault_file = os.path.join(VAULT_PATH, file_id)

    with open(vault_file, "wb") as f:
        f.write(encrypted)

    save_metadata(file_id, file_path)
    os.remove(file_path)
