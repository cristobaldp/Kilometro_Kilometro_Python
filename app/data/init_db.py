import sqlite3
from app.data.database import DB_PATH

def init_db():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()

    # -------- USUARIOS --------
    cur.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        apellidos TEXT,
        username TEXT UNIQUE,
        email TEXT UNIQUE,
        telefono TEXT,
        ciudad TEXT,
        fecha_nacimiento TEXT,
        password TEXT,
        vehiculo_activo_id INTEGER,

        unidad_consumo TEXT DEFAULT 'L/100km',
        formato_precio TEXT DEFAULT '€',
        periodo_estadisticas TEXT DEFAULT 'Mensual',
        vista_estadisticas TEXT DEFAULT 'lista',
        aviso_km INTEGER DEFAULT 0,
        aviso_consumo INTEGER DEFAULT 0,
        confirmar_acciones INTEGER DEFAULT 1,
        cerrar_sesion INTEGER DEFAULT 0
    )
    """)

    # -------- VEHÍCULOS --------
    cur.execute("""
    CREATE TABLE IF NOT EXISTS vehiculos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        tipo TEXT,
        marca TEXT,
        modelo TEXT,
        matricula TEXT UNIQUE,
        anio INTEGER,
        combustible TEXT,
        consumo REAL,
        FOREIGN KEY(user_id) REFERENCES usuarios(id)
    )
    """)

    # -------- REPOSTAJES --------
    cur.execute("""
    CREATE TABLE IF NOT EXISTS repostajes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vehiculo_id INTEGER,
        fecha TEXT,
        litros REAL,
        precio_total REAL,
        kilometros INTEGER,
        FOREIGN KEY(vehiculo_id) REFERENCES vehiculos(id)
    )
    """)

    con.commit()
    con.close()
