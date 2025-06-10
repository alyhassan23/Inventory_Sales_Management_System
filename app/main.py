# === tkinter_app/app/main.py ===

import tkinter as tk
from app.views.login_view import LoginView
from app.views.dashboard import Dashboard
from app.utils.db_init import initialize_database

def open_dashboard():
    dashboard = Dashboard()
    dashboard.mainloop()

if __name__ == '__main__':
    initialize_database()
    login_root = tk.Tk()
    login_root.title("Login")
    login_root.geometry("400x300")
    LoginView(login_root, on_success_callback=open_dashboard)
    login_root.mainloop()
    print("completed")