# === tkinter_app/app/services/sales_service.py ===

from app.utils.db_config import get_connection
from datetime import datetime

def get_products():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, price, quantity FROM products")
    result = cursor.fetchall()
    conn.close()
    return result

def save_invoice(customer_name, cart):
    conn = get_connection()
    cursor = conn.cursor()

    # Insert into invoices table
    invoice_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO invoices (customer_name, date) VALUES (%s, %s)", (customer_name, invoice_time))
    invoice_id = cursor.lastrowid

    # Insert invoice items and update stock
    for product_id, name, price, quantity in cart:
        cursor.execute("INSERT INTO invoice_items (invoice_id, product_id, quantity, price) VALUES (%s, %s, %s, %s)",
                       (invoice_id, product_id, quantity, price))
        cursor.execute("UPDATE products SET quantity = quantity - %s WHERE id = %s", (quantity, product_id))

    conn.commit()
    conn.close()
