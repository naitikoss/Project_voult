import base64
import hashlib
from cryptography.fernet import Fernet


def derive_key_from_password(password: str) -> bytes:
    """
    Derives a Fernet-compatible key from user password
    """
    sha = hashlib.sha256(password.encode("utf-8")).digest()
    return base64.urlsafe_b64encode(sha)
