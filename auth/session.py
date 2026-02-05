_current_password = None


def set_session_password(password: str):
    global _current_password
    _current_password = password


def get_session_password():
    return _current_password


def clear_session():
    global _current_password
    _current_password = None
