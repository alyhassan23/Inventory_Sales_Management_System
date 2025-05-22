# === tkinter_app/app/views/dashboard.py ===

import tkinter as tk
from tkinter import font
from app.views.product_view import ProductView
# from app.views.stock_view import StockView
# from app.views.supplier_view import SupplierView
# from app.views.report_view import ReportView
# from app.views.customer_view import CustomerView
# from app.views.sales_view import SalesView

class Dashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Inventory & Sales Management System")
        self.geometry("1100x650")
        self.configure(bg="#bdc3c7")

        self.sidebar_buttons = []

        # Custom font
        self.title_font = font.Font(family="Helvetica", size=16, weight="bold")
        self.button_font = font.Font(family="Helvetica", size=11)

        # Header Bar
        self.header = tk.Frame(self, height=50, bg="#34495e")
        self.header.pack(side="top", fill="x")
        tk.Label(self.header, text="Inventory & Sales Management System", font=self.title_font, fg="white", bg="#34495e").pack(pady=10)

        # Sidebar
        self.sidebar = tk.Frame(self, width=220, bg="#2c3e50")
        self.sidebar.pack(side="left", fill="y")

        # Main content area
        self.container = tk.Frame(self, bg="#ecf0f1")
        self.container.pack(side="right", expand=True, fill="both")

        self.current_frame = None

        # Sidebar Navigation Buttons
        self.add_sidebar_button("Product Management", self.load_product_view)
        self.add_sidebar_button("Stock In/Out", self.load_stock_view)
        self.add_sidebar_button("Sales Invoice", self.load_sales_view)
        self.add_sidebar_button("Customers", self.load_customer_view)
        self.add_sidebar_button("Suppliers", self.load_supplier_view)
        self.add_sidebar_button("Reports", self.load_report_view)

        # Load default view
        self.load_product_view()

    def add_sidebar_button(self, text, command):
        btn = tk.Button(self.sidebar, text=text, command=lambda b=text: self.change_view(b, command),
                        bg="#34495e", fg="white", font=self.button_font, relief="flat", activebackground="#16a085", activeforeground="white", padx=10, pady=10)
        btn.pack(fill="x", padx=10, pady=5)
        self.sidebar_buttons.append((text, btn))

        # Hover effect
        btn.bind("<Enter>", lambda e: btn.config(bg="#3d566e"))
        btn.bind("<Leave>", lambda e: btn.config(bg="#34495e" if not btn.cget("relief") == "sunken" else "#16a085"))

    def change_view(self, name, command):
        # Highlight active button
        for btn_name, btn in self.sidebar_buttons:
            if btn_name == name:
                btn.config(bg="#16a085", relief="sunken")
            else:
                btn.config(bg="#34495e", relief="flat")

        command()

    def clear_current_frame(self):
        if self.current_frame:
            self.current_frame.destroy()

    def load_product_view(self):
        self.clear_current_frame()
        self.current_frame = ProductView(self.container)
        self.current_frame.pack(fill="both", expand=True)

    def load_stock_view(self):
        self.clear_current_frame()
        self.current_frame = StockView(self.container)
        self.current_frame.pack(fill="both", expand=True)

    def load_sales_view(self):
        self.clear_current_frame()
        self.current_frame = SalesView(self.container)
        self.current_frame.pack(fill="both", expand=True)

    def load_customer_view(self):
        self.clear_current_frame()
        self.current_frame = CustomerView(self.container)
        self.current_frame.pack(fill="both", expand=True)

    def load_supplier_view(self):
        self.clear_current_frame()
        self.current_frame = SupplierView(self.container)
        self.current_frame.pack(fill="both", expand=True)

    def load_report_view(self):
        self.clear_current_frame()
        self.current_frame = ReportView(self.container)
        self.current_frame.pack(fill="both", expand=True)
