# === tkinter_app/app/services/supplier_service.py ===

from app.utils.db_config import get_connection

def get_suppliers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, phone, email, company FROM suppliers")
    result = cursor.fetchall()
    conn.close()
    return result

def add_supplier(name, phone, email, company):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO suppliers (name, phone, email, company) VALUES (%s, %s, %s, %s)",
        (name, phone, email, company)
    )
    conn.commit()
    conn.close()

def update_supplier(supplier_id, name, phone, email, company):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE suppliers SET name=%s, phone=%s, email=%s, company=%s WHERE id=%s",
        (name, phone, email, company, supplier_id)
    )
    conn.commit()
    conn.close()
