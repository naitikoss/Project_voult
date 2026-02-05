import customtkinter as ctk
from auth.login import verify_password
from gui.dashboard_ui import DashboardUI
from auth.session import set_session_password

class LoginUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Secure File Vault")
        self.geometry("400x300")

        self.attempts = 3

        ctk.CTkLabel(self, text="🔐 Vault Unlock", font=("Arial", 20)).pack(pady=20)

        self.password = ctk.CTkEntry(self, show="*")
        self.password.pack(pady=10)

        self.status = ctk.CTkLabel(self, text="")
        self.status.pack()

        ctk.CTkButton(self, text="Unlock", command=self.unlock).pack(pady=20)

    def unlock(self):
     pwd = self.password.get()

     if verify_password(pwd):
        set_session_password(pwd)
        self.destroy()
        DashboardUI().mainloop()
     else:
        self.attempts -= 1
        self.status.configure(text=f"Wrong password. Attempts left: {self.attempts}")
        if self.attempts == 0:
            self.destroy()
