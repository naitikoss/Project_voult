import os
from cryptography.fernet import Fernet
from vault.metadata import load_metadata, delete_metadata
from crypto.keygen import derive_key_from_password
from auth.session import get_session_password

VAULT_PATH = "vault/.secure_data/files"


def restore_file(file_id):
    meta = load_metadata(file_id)
    if not meta:
        return

    password = get_session_password()
    if not password:
        raise RuntimeError("Vault is locked. No session password.")

    vault_file = os.path.join(VAULT_PATH, file_id)

    with open(vault_file, "rb") as f:
        encrypted = f.read()

    key = derive_key_from_password(password)
    cipher = Fernet(key)
    data = cipher.decrypt(encrypted)

    os.makedirs(os.path.dirname(meta["original_path"]), exist_ok=True)
    with open(meta["original_path"], "wb") as f:
        f.write(data)

    os.remove(vault_file)
    delete_metadata(file_id)
