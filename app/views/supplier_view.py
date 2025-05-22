# === tkinter_app/app/views/supplier_view.py ===

import tkinter as tk
from tkinter import ttk, messagebox
from app.services.supplier_service import get_suppliers, add_supplier, update_supplier

class SupplierView(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#f7f7f7")
        self.master = master

        # Title
        tk.Label(self, text="🚚 Supplier Management", font=("Helvetica", 20, "bold"),
                 bg="#f7f7f7", fg="#2c3e50").pack(pady=10)

        # Supplier table
        tree_frame = tk.LabelFrame(self, text="Supplier List", font=("Helvetica", 12, "bold"), bg="#ffffff")
        tree_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.tree = ttk.Treeview(tree_frame, columns=("ID", "Name", "Phone", "Email", "Company"), show="headings", height=10)
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        # Input form
        form_frame = tk.LabelFrame(self, text="Supplier Details", font=("Helvetica", 12), bg="#f7f7f7")
        form_frame.pack(pady=10, padx=20, fill="x")

        labels = ["Name:", "Phone:", "Email:", "Company:"]
        self.entries = {}

        for i, label in enumerate(labels):
            tk.Label(form_frame, text=label, font=("Helvetica", 11), bg="#f7f7f7").grid(row=i, column=0, sticky="e", padx=5, pady=3)
            entry = tk.Entry(form_frame, width=30)
            entry.grid(row=i, column=1, padx=5, pady=3)
            self.entries[label[:-1].lower()] = entry

        # Buttons
        btn_frame = tk.Frame(self, bg="#f7f7f7")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Add Supplier", font=("Helvetica", 10, "bold"),
                  bg="#3498db", fg="white", width=15, command=self.add_supplier).pack(side="left", padx=10)

        tk.Button(btn_frame, text="Update Supplier", font=("Helvetica", 10, "bold"),
                  bg="#f39c12", fg="white", width=15, command=self.update_supplier).pack(side="left", padx=10)

        # Events and initial data
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        self.load_suppliers()

    def load_suppliers(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for supplier in get_suppliers():
            self.tree.insert("", "end", values=supplier)

    def on_tree_select(self, event):
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected[0])["values"]
            fields = ["name", "phone", "email", "company"]
            for i, key in enumerate(fields):
                self.entries[key].delete(0, tk.END)
                self.entries[key].insert(0, values[i + 1])

    def add_supplier(self):
        name = self.entries["name"].get()
        phone = self.entries["phone"].get()
        email = self.entries["email"].get()
        company = self.entries["company"].get()

        if not name or not company:
            messagebox.showerror("Error", "Name and Company are required fields.")
            return

        add_supplier(name, phone, email, company)
        messagebox.showinfo("Success", "Supplier added successfully.")
        self.load_suppliers()
        self.clear_form()

    def update_supplier(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "Select a supplier to update.")
            return

        supplier_id = self.tree.item(selected[0])["values"][0]
        name = self.entries["name"].get()
        phone = self.entries["phone"].get()
        email = self.entries["email"].get()
        company = self.entries["company"].get()

        update_supplier(supplier_id, name, phone, email, company)
        messagebox.showinfo("Success", "Supplier updated successfully.")
        self.load_suppliers()
        self.clear_form()

    def clear_form(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
