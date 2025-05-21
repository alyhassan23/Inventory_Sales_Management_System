# === tkinter_app/app/services/product_service.py ===

from app.utils.db_config import get_connection

def get_all_products():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    results = cursor.fetchall()
    conn.close()
    return results

def add_product(name, category, price, quantity):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, category, price, quantity) VALUES (%s, %s, %s, %s)",
                   (name, category, price, quantity))
    conn.commit()
    conn.close()

def update_product(product_id, name, category, price, quantity):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET name=%s, category=%s, price=%s, quantity=%s WHERE id=%s",
                   (name, category, price, quantity, product_id))
    conn.commit()
    conn.close()

def delete_product(product_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id=%s", (product_id,))
    conn.commit()
    conn.close()
