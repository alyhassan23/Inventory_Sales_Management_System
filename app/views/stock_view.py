# === tkinter_app/app/views/stock_view.py ===

import tkinter as tk
from tkinter import ttk, messagebox
from app.services.stock_service import stock_in, stock_out, get_products

class StockView(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#f7f7f7")
        self.master = master
        self.pack(fill="both", expand=True)

        # Title
        tk.Label(self, text="📦 Stock Management", font=("Helvetica", 20, "bold"),
                 bg="#f7f7f7", fg="#2c3e50").pack(pady=10)

        # Treeview for product list
        tree_frame = tk.LabelFrame(self, text="Product Inventory", font=("Helvetica", 12, "bold"), bg="#ffffff")
        tree_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.tree = ttk.Treeview(tree_frame, columns=("ID", "Name", "Category", "Price", "Quantity"), show="headings", height=10)
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        self.refresh_products()

        # Quantity input
        form_frame = tk.Frame(self, bg="#f7f7f7")
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Quantity:", font=("Helvetica", 11), bg="#f7f7f7").grid(row=0, column=0, padx=5)
        self.qty_entry = tk.Entry(form_frame, width=10)
        self.qty_entry.grid(row=0, column=1, padx=5)

        # Action Buttons
        btn_frame = tk.Frame(form_frame, bg="#f7f7f7")
        btn_frame.grid(row=0, column=2, padx=10)

        tk.Button(btn_frame, text="Stock In", font=("Helvetica", 10, "bold"),
                  bg="#27ae60", fg="white", width=12, command=self.stock_in_action).pack(side="left", padx=5)

        tk.Button(btn_frame, text="Stock Out", font=("Helvetica", 10, "bold"),
                  bg="#c0392b", fg="white", width=12, command=self.stock_out_action).pack(side="left", padx=5)

    def refresh_products(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for product in get_products():
            self.tree.insert("", "end", values=product)

    def get_selected_product_id(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("No Selection", "Please select a product from the list.")
            return None
        return int(self.tree.item(selected[0])["values"][0])

    def stock_in_action(self):
        product_id = self.get_selected_product_id()
        quantity = self.qty_entry.get()
        if product_id and quantity.isdigit() and int(quantity) > 0:
            stock_in(product_id, int(quantity))
            self.refresh_products()
            self.qty_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a valid quantity.")

    def stock_out_action(self):
        product_id = self.get_selected_product_id()
        quantity = self.qty_entry.get()
        if product_id and quantity.isdigit() and int(quantity) > 0:
            stock_out(product_id, int(quantity))
            self.refresh_products()
            self.qty_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a valid quantity.")
