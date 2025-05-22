# === tkinter_app/app/utils/db_config.py ===

import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="inventory_db"
    )
