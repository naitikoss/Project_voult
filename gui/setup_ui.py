import customtkinter as ctk
from auth.password import set_password
from gui.login_ui import LoginUI

class SetupUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Secure File Vault - First Run Setup")
        self.geometry("400x350")
        
        ctk.CTkLabel(self, text="🆕 Setup New Password", font=("Arial", 20)).pack(pady=20)
        
        ctk.CTkLabel(self, text="Enter New Password:").pack(pady=(10, 0))
        self.new_pass = ctk.CTkEntry(self, show="*")
        self.new_pass.pack(pady=5)
        
        ctk.CTkLabel(self, text="Confirm Password:").pack(pady=(10, 0))
        self.confirm_pass = ctk.CTkEntry(self, show="*")
        self.confirm_pass.pack(pady=5)
        
        self.status = ctk.CTkLabel(self, text="", text_color="red")
        self.status.pack(pady=10)
        
        ctk.CTkButton(self, text="Set Password", command=self.save_password).pack(pady=20)
        
    def save_password(self):
        p1 = self.new_pass.get()
        p2 = self.confirm_pass.get()
        
        if not p1:
            self.status.configure(text="Password cannot be empty!")
            return
            
        if p1 != p2:
            self.status.configure(text="Passwords do not match!")
            return
            
        set_password(p1)
        self.destroy()
        # Redirect to login logic
        app = LoginUI()
        app.mainloop()
