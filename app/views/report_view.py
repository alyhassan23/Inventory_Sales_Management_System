# === tkinter_app/app/views/report_view.py ===

import tkinter as tk
from tkinter import ttk
from app.services.report_service import get_sales_summary, get_inventory_status

class ReportView(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#f9f9f9")
        self.master = master
        self.pack(fill="both", expand=True, padx=20, pady=20)

        # Title
        tk.Label(self, text="📊 Sales & Inventory Reports", font=("Helvetica", 20, "bold"),
                 bg="#f9f9f9", fg="#2c3e50").pack(pady=10)

        # Notebook (Tabs)
        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.sales_frame = tk.Frame(notebook, bg="#ffffff")
        self.inventory_frame = tk.Frame(notebook, bg="#ffffff")

        notebook.add(self.sales_frame, text="Sales Summary")
        notebook.add(self.inventory_frame, text="Inventory Status")

        # Style Treeview
        self._style_treeview()

        self.setup_sales_report()
        self.setup_inventory_report()

    def _style_treeview(self):
        style = ttk.Style()
        style.configure("Treeview.Heading",
                        font=("Helvetica", 11, "bold"),
                        background="#34495e",
                        foreground="white")
        style.configure("Treeview",
                        font=("Helvetica", 10),
                        rowheight=28)

    def setup_sales_report(self):
        self.sales_tree = ttk.Treeview(self.sales_frame,
                                       columns=("Date", "Total Sales"),
                                       show="headings", height=15)
        self.sales_tree.heading("Date", text="Date")
        self.sales_tree.heading("Total Sales", text="Total Sales")
        self.sales_tree.column("Date", anchor="center", width=150)
        self.sales_tree.column("Total Sales", anchor="center", width=150)
        self.sales_tree.pack(fill="both", expand=True, padx=10, pady=10)

        for row in get_sales_summary():
            self.sales_tree.insert("", "end", values=row)

    def setup_inventory_report(self):
        self.inventory_tree = ttk.Treeview(self.inventory_frame,
                                           columns=("Product", "Available Stock"),
                                           show="headings", height=15)
        self.inventory_tree.heading("Product", text="Product")
        self.inventory_tree.heading("Available Stock", text="Available Stock")
        self.inventory_tree.column("Product", anchor="center", width=200)
        self.inventory_tree.column("Available Stock", anchor="center", width=150)
        self.inventory_tree.pack(fill="both", expand=True, padx=10, pady=10)

        for row in get_inventory_status():
            self.inventory_tree.insert("", "end", values=row)
