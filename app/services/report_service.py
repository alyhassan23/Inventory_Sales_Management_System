# === tkinter_app/app/services/report_service.py ===

from app.utils.db_config import get_connection

def get_sales_summary():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT DATE(date) AS day, SUM(total_amount) AS total_sales
        FROM sales
        GROUP BY DATE(date)
        ORDER BY day DESC
        LIMIT 10
    """)
    results = cursor.fetchall()
    conn.close()
    return results
def get_inventory_status():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT name
        FROM products
        ORDER BY name
    """)
    results = cursor.fetchall()
    conn.close()
    # Return name and a placeholder stock value like 0, so UI code doesn't break
    return [(row[0], 0) for row in results]
