import os
import sqlite3

DB_PATH = "app/data/kilometro_kilometro.db"

def get_connection():
    print("USANDO BBDD:", os.path.abspath(DB_PATH))
    return sqlite3.connect(DB_PATH)
