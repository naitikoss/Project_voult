import customtkinter as ctk
from gui.login_ui import LoginUI
from gui.setup_ui import SetupUI
from auth.password import is_password_set

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

if __name__ == "__main__":
    if is_password_set():
        app = LoginUI()
    else:
        app = SetupUI()
    app.mainloop()
