# === tkinter_app/app/services/customer_service.py ===

from app.utils.db_config import get_connection

def get_customers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, phone, email FROM customers")
    result = cursor.fetchall()
    conn.close()
    return result

def add_customer(name, phone, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO customers (name, phone, email) VALUES (%s, %s, %s)", (name, phone, email))
    conn.commit()
    conn.close()

def update_customer(customer_id, name, phone, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE customers SET name=%s, phone=%s, email=%s WHERE id=%s", (name, phone, email, customer_id))
    conn.commit()
    conn.close()
