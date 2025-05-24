# === tkinter_app/app/views/customer_view.py ===

import tkinter as tk
from tkinter import ttk, messagebox
from app.services.customer_service import get_customers, add_customer, update_customer

class CustomerView(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#ecf0f1")
        self.master = master

        # Title
        tk.Label(self, text="Customer Management", font=("Helvetica", 20, "bold"), bg="#ecf0f1", fg="#2c3e50").pack(pady=20)

        # Treeview (Customer Table)
        self.tree = ttk.Treeview(self, columns=("ID", "Name", "Phone", "Email"), show="headings", height=8)
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Helvetica", 11, "bold"), background="#34495e", foreground="white")
        style.configure("Treeview", font=("Helvetica", 10), rowheight=28)
        self.tree.pack(padx=20, fill="both", expand=True)

        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")

        # Form Frame
        form_frame = tk.Frame(self, bg="#ecf0f1")
        form_frame.pack(pady=20)

        label_font = ("Helvetica", 10, "bold")
        entry_font = ("Helvetica", 10)

        # Name
        tk.Label(form_frame, text="Name:", font=label_font, bg="#ecf0f1").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.name_entry = tk.Entry(form_frame, font=entry_font, width=30)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        # Phone
        tk.Label(form_frame, text="Phone:", font=label_font, bg="#ecf0f1").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.phone_entry = tk.Entry(form_frame, font=entry_font, width=30)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        # Email
        tk.Label(form_frame, text="Email:", font=label_font, bg="#ecf0f1").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.email_entry = tk.Entry(form_frame, font=entry_font, width=30)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        # Buttons
        btn_frame = tk.Frame(self, bg="#ecf0f1")
        btn_frame.pack(pady=10)

        self.add_btn = tk.Button(btn_frame, text="Add Customer", font=("Helvetica", 10, "bold"),
                                 bg="#27ae60", fg="white", activebackground="#2ecc71", relief="flat",
                                 padx=15, pady=5, command=self.add_customer)
        self.add_btn.grid(row=0, column=0, padx=10)

        self.update_btn = tk.Button(btn_frame, text="Update Customer", font=("Helvetica", 10, "bold"),
                                    bg="#2980b9", fg="white", activebackground="#3498db", relief="flat",
                                    padx=15, pady=5, command=self.update_customer)
        self.update_btn.grid(row=0, column=1, padx=10)

        # Hover Effects
        self.add_btn.bind("<Enter>", lambda e: self.add_btn.config(bg="#2ecc71"))
        self.add_btn.bind("<Leave>", lambda e: self.add_btn.config(bg="#27ae60"))
        self.update_btn.bind("<Enter>", lambda e: self.update_btn.config(bg="#3498db"))
        self.update_btn.bind("<Leave>", lambda e: self.update_btn.config(bg="#2980b9"))

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        self.load_customers()

    def load_customers(self):
        self.tree.delete(*self.tree.get_children())
        for customer in get_customers():
            self.tree.insert("", "end", values=customer)

    def on_tree_select(self, event):
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected[0])["values"]
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, values[1])
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, values[2])
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, values[3])

    def add_customer(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        if not name:
            messagebox.showerror("Error", "Name is required")
            return
        add_customer(name, phone, email)
        self.load_customers()

    def update_customer(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "Select a customer to update")
            return
        customer_id = self.tree.item(selected[0])["values"][0]
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        update_customer(customer_id, name, phone, email)
        self.load_customers()
