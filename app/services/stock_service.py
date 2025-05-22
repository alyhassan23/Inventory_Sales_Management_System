# === tkinter_app/app/services/stock_service.py ===

from app.utils.db_config import get_connection

def get_products():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price, quantity FROM products")
    result = cursor.fetchall()
    conn.close()
    return result

def stock_in(product_id, quantity):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET quantity = quantity + %s WHERE id = %s", (quantity, product_id))
    conn.commit()
    conn.close()

def stock_out(product_id, quantity):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET quantity = quantity - %s WHERE id = %s AND quantity >= %s", (quantity, product_id, quantity))
    conn.commit()
    conn.close()
