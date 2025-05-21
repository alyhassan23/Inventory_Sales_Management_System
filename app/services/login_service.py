# === tkinter_app/app/services/login_service.py ===

from app.utils.db_config import get_connection

def authenticate_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result is not None
