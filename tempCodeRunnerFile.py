import customtkinter as ctk
from gui.login_ui import LoginUI

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

if __name__ == "__main__":
    app = LoginUI()
    app.mainloop()
