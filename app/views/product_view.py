# === tkinter_app/app/views/product_view.py ===

import tkinter as tk
from tkinter import ttk, messagebox
from app.services.product_service import get_all_products, add_product, update_product, delete_product

class ProductView(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#f4f6f7")
        self.master = master
        self.pack(fill="both", expand=True, padx=20, pady=20)

        self.selected_product_id = None

        # Title
        tk.Label(self, text="Product Management", font=("Helvetica", 20, "bold"), bg="#f4f6f7", fg="#2c3e50").pack(pady=10)

        # Form Frame
        form_frame = tk.Frame(self, bg="#f4f6f7")
        form_frame.pack(pady=10)

        label_font = ("Helvetica", 10, "bold")
        entry_font = ("Helvetica", 10)

        # Fields
        self._create_label_entry(form_frame, "Product Name:", 0)
        self._create_label_entry(form_frame, "Category:", 1)
        self._create_label_entry(form_frame, "Price:", 2)
        self._create_label_entry(form_frame, "Quantity:", 3)

        self.name_entry, self.category_entry, self.price_entry, self.quantity_entry = self.entries

        # Button Frame
        btn_frame = tk.Frame(self, bg="#f4f6f7")
        btn_frame.pack(pady=10)

        self._create_button(btn_frame, "Add", "#27ae60", self.add_product, 0)
        self._create_button(btn_frame, "Update", "#2980b9", self.update_product, 1)
        self._create_button(btn_frame, "Delete", "#c0392b", self.delete_product, 2)

        # Treeview
        self.tree = ttk.Treeview(self, columns=("ID", "Name", "Category", "Price", "Quantity"), show='headings', height=10)
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Helvetica", 11, "bold"), background="#34495e", foreground="white")
        style.configure("Treeview", font=("Helvetica", 10), rowheight=28)
        self.tree.pack(fill="both", expand=True, pady=10)

        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")

        self.tree.bind("<ButtonRelease-1>", self.on_row_select)

        self.refresh_products()

    def _create_label_entry(self, frame, label, row):
        if not hasattr(self, 'entries'):
            self.entries = []
        tk.Label(frame, text=label, font=("Helvetica", 10, "bold"), bg="#f4f6f7").grid(row=row, column=0, padx=10, pady=5, sticky="e")
        entry = tk.Entry(frame, font=("Helvetica", 10), width=30)
        entry.grid(row=row, column=1, padx=10, pady=5)
        self.entries.append(entry)

    def _create_button(self, frame, text, color, command, col):
        btn = tk.Button(frame, text=text, font=("Helvetica", 10, "bold"),
                        bg=color, fg="white", activebackground=color, relief="flat",
                        padx=15, pady=5, command=command)
        btn.grid(row=0, column=col, padx=10)
        btn.bind("<Enter>", lambda e: btn.config(bg=self._lighten(color)))
        btn.bind("<Leave>", lambda e: btn.config(bg=color))

    def _lighten(self, hex_color):
        # Lighten hex color for hover effect
        hex_color = hex_color.lstrip('#')
        rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        lighter_rgb = tuple(min(255, int(c + 30)) for c in rgb)
        return '#%02x%02x%02x' % lighter_rgb

    def refresh_products(self):
        self.tree.delete(*self.tree.get_children())
        for product in get_all_products():
            self.tree.insert("", "end", values=product)

    def on_row_select(self, event):
        selected = self.tree.selection()
        if not selected:
            self.selected_product_id = None
            return
        item = selected[0]
        values = self.tree.item(item, "values")
        self.selected_product_id = values[0]
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, values[1])
        self.category_entry.delete(0, tk.END)
        self.category_entry.insert(0, values[2])
        self.price_entry.delete(0, tk.END)
        self.price_entry.insert(0, values[3])
        self.quantity_entry.delete(0, tk.END)
        self.quantity_entry.insert(0, values[4])

    def add_product(self):
        try:
            name = self.name_entry.get()
            category = self.category_entry.get()
            price = float(self.price_entry.get())
            quantity = int(self.quantity_entry.get())
            add_product(name, category, price, quantity)
            self.refresh_products()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid price and quantity.")

    def update_product(self):
        if self.selected_product_id:
            try:
                name = self.name_entry.get()
                category = self.category_entry.get()
                price = float(self.price_entry.get())
                quantity = int(self.quantity_entry.get())
                update_product(self.selected_product_id, name, category, price, quantity)
                self.refresh_products()
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter valid price and quantity.")

    def delete_product(self):
        if self.selected_product_id:
            confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this product?")
            if confirm:
                delete_product(self.selected_product_id)
                self.refresh_products()
