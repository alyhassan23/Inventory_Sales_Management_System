# === tkinter_app/app/views/sales_view.py ===

import tkinter as tk
from tkinter import ttk, messagebox
from app.services.sales_service import get_products, save_invoice

class SalesView(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#f7f7f7")
        self.master = master
        self.cart = []

        # Title
        tk.Label(self, text="🧾 Sales Invoice", font=("Helvetica", 20, "bold"),
                 bg="#f7f7f7", fg="#2c3e50").pack(pady=10)

        # Product List
        product_frame = tk.LabelFrame(self, text="Available Products", bg="#ffffff", font=("Helvetica", 12, "bold"))
        product_frame.pack(padx=20, pady=10, fill="both", expand=True)

        self.product_tree = ttk.Treeview(product_frame, columns=("ID", "Name", "Price", "Stock"), show="headings", height=8)
        for col in self.product_tree["columns"]:
            self.product_tree.heading(col, text=col)
            self.product_tree.column(col, anchor="center")
        self.product_tree.pack(padx=10, pady=10, fill="both", expand=True)

        self.load_products()

        # Quantity + Add Button
        form_frame = tk.Frame(self, bg="#f7f7f7")
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Quantity:", font=("Helvetica", 11), bg="#f7f7f7").grid(row=0, column=0, padx=5)
        self.qty_entry = tk.Entry(form_frame, width=10)
        self.qty_entry.grid(row=0, column=1, padx=5)

        tk.Button(form_frame, text="Add to Cart", font=("Helvetica", 10, "bold"),
                  command=self.add_to_cart, bg="#3498db", fg="white", width=15).grid(row=0, column=2, padx=10)

        # Cart Listbox
        cart_frame = tk.LabelFrame(self, text="🛒 Cart", bg="#ffffff", font=("Helvetica", 12, "bold"))
        cart_frame.pack(padx=20, pady=10, fill="both", expand=True)

        self.cart_listbox = tk.Listbox(cart_frame, width=90, font=("Courier", 10))
        self.cart_listbox.pack(padx=10, pady=10)

        # Customer + Invoice Button
        customer_frame = tk.Frame(self, bg="#f7f7f7")
        customer_frame.pack(pady=10)

        tk.Label(customer_frame, text="Customer Name:", font=("Helvetica", 11), bg="#f7f7f7").grid(row=0, column=0, padx=5)
        self.customer_entry = tk.Entry(customer_frame, width=30)
        self.customer_entry.grid(row=0, column=1, padx=5)

        tk.Button(customer_frame, text="Generate Invoice", font=("Helvetica", 10, "bold"),
                  command=self.generate_invoice, bg="#27ae60", fg="white", width=20).grid(row=0, column=2, padx=10)

    def load_products(self):
        for row in self.product_tree.get_children():
            self.product_tree.delete(row)
        for product in get_products():
            self.product_tree.insert("", "end", values=product)

    def get_selected_product(self):
        selected = self.product_tree.selection()
        if not selected:
            return None
        return self.product_tree.item(selected[0])["values"]

    def add_to_cart(self):
        product = self.get_selected_product()
        quantity = self.qty_entry.get()
        if not product:
            messagebox.showwarning("No Selection", "Please select a product.")
            return
        if not quantity.isdigit() or int(quantity) <= 0:
            messagebox.showwarning("Invalid Quantity", "Please enter a valid quantity.")
            return
        self.cart.append((product[0], product[1], float(product[2]), int(quantity)))  # (id, name, price, qty)
        self.update_cart_view()
        self.qty_entry.delete(0, tk.END)

    def update_cart_view(self):
        self.cart_listbox.delete(0, tk.END)
        for item in self.cart:
            total = item[2] * item[3]
            self.cart_listbox.insert(tk.END, f"{item[1]:30} x {item[3]:3} @ {item[2]:6.2f} = Rs {total:8.2f}")

    def generate_invoice(self):
        customer = self.customer_entry.get().strip()
        if not customer:
            messagebox.showerror("Missing Info", "Customer name is required.")
            return
        if not self.cart:
            messagebox.showerror("Empty Cart", "Please add items to the cart.")
            return
        save_invoice(customer, self.cart)
        messagebox.showinfo("Success", "Invoice saved successfully!")
        self.cart = []
        self.update_cart_view()
        self.customer_entry.delete(0, tk.END)
        self.load_products()
