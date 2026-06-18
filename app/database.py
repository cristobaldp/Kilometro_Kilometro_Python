import sqlite3

DB_PATH = r"C:\Users\Cristobal Delgado\Documents\Kilometro_Kilometro\app\data\kilometro_kilometro.db"

def get_connection():
    return sqlite3.connect(DB_PATH)