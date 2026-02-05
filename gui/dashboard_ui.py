import customtkinter as ctk
from tkinter import filedialog, messagebox
from crypto.encrypt import encrypt_and_store
from crypto.decrypt import restore_file
from vault.metadata import list_files
import auth.login
from auth.password import reset_password
import sys

class DashboardUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Vault Dashboard")
        self.geometry("600x400")

        ctk.CTkButton(self, text="📁 Add File", command=self.add_file).pack(pady=10)
        ctk.CTkButton(self, text="🔒 Stored File", command=self.restore).pack(pady=10)
        ctk.CTkButton(self, text="🔑 Change Password", command=self.change_password).pack(pady=10)

    def change_password(self):
        # 1. Ask Permission
        if not messagebox.askyesno("Permission", "Do you want to Delete your password?"):
            return # Code terminates the flow here
            
        # 2. Ask for Old Password
        pwd = self.ask_password_masked(self)
        
        if pwd:
            # 3. Verify Old Password
            if auth.login.verify_password(pwd):
                # 4. Delete Password
                reset_password()
                messagebox.showinfo("Success", "Password deleted successfully.")
                self.destroy()
                sys.exit()
            else:
                messagebox.showerror("Error", "Incorrect Password!")

    def add_file(self):
        all_selected_files = []
        
        while True:
            paths = filedialog.askopenfilenames()
            if paths:
                all_selected_files.extend(paths)
            
            # If no files selected yet and user cancelled, stop
            if not all_selected_files:
                return

            # Ask if they want to add more
            if not messagebox.askyesno("Add More?", "Do you want to select more files?"):
                break
        
        if all_selected_files:
            try:
                # Remove duplicates if any
                unique_paths = list(set(all_selected_files))
                
                for path in unique_paths:
                    encrypt_and_store(path)
                
                messagebox.showinfo("Success", f"{len(unique_paths)} File(s) Encrypted Successfully. App will close soon.")
                self.quit()
                sys.exit()
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

    def restore(self):
        files = list_files()
        if not files:
            messagebox.showinfo("Info", "No files to restore.")
            return

        # Restore Window
        restore_window = ctk.CTkToplevel(self)
        restore_window.title("Select Files to Restore")
        restore_window.geometry("500x400")
        restore_window.grab_set()  

        ctk.CTkLabel(restore_window, text="Select files to restore:", font=("Arial", 16)).pack(pady=10)

        # Scrollable frame for files
        scroll = ctk.CTkScrollableFrame(restore_window, width=400, height=250)
        scroll.pack(pady=10)

        self.check_vars = {}  

        for f in files:
            var = ctk.BooleanVar()
            chk = ctk.CTkCheckBox(scroll, text=f"{f['original_path']} (Encrypted: {f['encrypted_at']})", variable=var)
            chk.pack(anchor="w", pady=5)
            self.check_vars[f['file_id']] = var

        ctk.CTkButton(restore_window, text="Restore Selected", command=lambda: self.confirm_restore(restore_window)).pack(pady=20)
    
    def confirm_restore(self, window):
        selected_ids = [fid for fid, var in self.check_vars.items() if var.get()]
        
        if not selected_ids:
            messagebox.showwarning("Warning", "No files selected.")
            return

        # Ask for password with custom masked dialog
        pwd = self.ask_password_masked(window)
        
        if pwd:
            if auth.login.verify_password(pwd):
                try:
                    for fid in selected_ids:
                        restore_file(fid)
                    
                    messagebox.showinfo("Success", f"Restored {len(selected_ids)} file(s). App will close.")
                    window.destroy()
                    self.quit()
                    sys.exit()
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to restore: {str(e)}")
            else:
                messagebox.showerror("Error", "Incorrect Password!")
    
    def ask_password_masked(self, parent):
        dialog = ctk.CTkToplevel(parent)
        dialog.title("Password Verification")
        dialog.geometry("300x150")
        dialog.grab_set()
        
        ctk.CTkLabel(dialog, text="Enter Password to confirm restore:").pack(pady=10)
        
        entry = ctk.CTkEntry(dialog, show="*")
        entry.pack(pady=5)
        entry.focus()
        
        password = [None]
        
        def on_submit(event=None):
            password[0] = entry.get()
            dialog.destroy()
            
        entry.bind("<Return>", on_submit)
        ctk.CTkButton(dialog, text="Verify", command=on_submit).pack(pady=10)
        
        parent.wait_window(dialog)
        return password[0]
