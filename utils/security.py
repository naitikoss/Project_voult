import os
import subprocess

def hide_windows(path):
    if os.path.exists(path):
        subprocess.call(["attrib", "+h", "+s", path])

def unhide_windows(path):
    if os.path.exists(path):
        subprocess.call(["attrib", "-h", "-s", path])

def secure_delete(path):
    if not os.path.isfile(path):
        return

    length = os.path.getsize(path)
    with open(path, "wb") as f:
        f.write(b"\x00" * length)

    os.remove(path)
