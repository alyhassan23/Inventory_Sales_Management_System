import tkinter as tk
from tkinter import messagebox
from app.services.login_service import authenticate_user

class LoginView:
    def __init__(self, master, on_success_callback):
        self.master = master
        self.on_success_callback = on_success_callback
        self.master.title("Login")
        self.master.geometry("400x400")
        self.master.configure(bg="#ecf0f1")

        # Center frame (login card)
        self.login_frame = tk.Frame(master, bg="white", bd=2, relief="ridge")
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center", width=300, height=320)

        # Title label
        tk.Label(self.login_frame, text="Login", font=("Helvetica", 20, "bold"), bg="white", fg="#2c3e50").pack(pady=20)

        # Username
        tk.Label(self.login_frame, text="Username", font=("Helvetica", 10), bg="white", anchor="w").pack(fill="x", padx=20)
        self.username_entry = tk.Entry(self.login_frame, font=("Helvetica", 11), bd=1, relief="solid")
        self.username_entry.pack(padx=20, pady=5, fill="x")

        # Password
        tk.Label(self.login_frame, text="Password", font=("Helvetica", 10), bg="white", anchor="w").pack(fill="x", padx=20, pady=(10, 0))
        self.password_entry = tk.Entry(self.login_frame, font=("Helvetica", 11), show="*", bd=1, relief="solid")
        self.password_entry.pack(padx=20, pady=5, fill="x")

        # Login button
        self.login_button = tk.Button(self.login_frame, text="Login", font=("Helvetica", 11, "bold"),
                                      bg="#27ae60", fg="white", activebackground="#2ecc71", relief="flat",
                                      command=self.login)
        self.login_button.pack(pady=20, ipadx=10, ipady=5)

        # Hover effects
        self.login_button.bind("<Enter>", lambda e: self.login_button.config(bg="#2ecc71"))
        self.login_button.bind("<Leave>", lambda e: self.login_button.config(bg="#27ae60"))

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if authenticate_user(username, password):
            self.master.destroy()  # Close login window
            self.on_success_callback()  # Open dashboard
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
