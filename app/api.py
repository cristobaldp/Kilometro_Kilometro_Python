from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
import hashlib
import os

# Importación directa corregida para el entorno unificado
from database import DB_PATH

app = FastAPI(title="Kilómetro a Kilómetro API")

print("BD existe:", os.path.exists(DB_PATH))


# =====================
# INIT SQLITE
# =====================
def get_connection():
    return sqlite3.connect(DB_PATH, timeout=10)


# =====================
# MODELOS (Pydantic)
# =====================

class LoginRequest(BaseModel):
    username: str
    password: str


class PasswordUpdateRequest(BaseModel):
    password: str


class RegisterRequest(BaseModel):
    nombre: str
    apellidos: str
    username: str
    email: str
    telefono: str
    ciudad: str
    fecha_nacimiento: str
    password: str


class VehiculoRequest(BaseModel):
    user_id: int
    tipo: str
    marca: str
    modelo: str
    matricula: str
    anio: int
    combustible: str
    consumo: float


class RepostajeIn(BaseModel):
    vehiculo_id: int
    fecha: str
    litros: float
    precio_total: float
    kilometros: int


# =====================
# ENDPOINTS
# =====================

@app.get("/")
def root():
    return {"status": "API funcionando"}


# 🔐 LOGIN
@app.post("/login")
def login(data: LoginRequest):
    with get_connection() as con:
        cur = con.cursor()
        # CORREGIDO: 'city' cambiado por 'ciudad' para coincidir con la BD de escritorio
        cur.execute("""
            SELECT id, nombre, apellidos, username, email,
                   telefono, ciudad, fecha_nacimiento,
                   password, vehiculo_activo_id
            FROM usuarios
            WHERE username = ?
        """, (data.username,))
        row = cur.fetchone()

    if not row:
        return {"error": "Credenciales incorrectas"}

    password_hash = hashlib.sha256(data.password.encode()).hexdigest()
    if password_hash != row[8]:
        return {"error": "Credenciales incorrectas"}

    return {
        "id": row[0],
        "nombre": row[1],
        "apellidos": row[2],
        "username": row[3],
        "email": row[4],
        "telefono": row[5],
        "ciudad": row[6],
        "fecha_nacimiento": row[7],
        "vehiculo_activo_id": row[9]
    }


# 📝 REGISTRO
@app.post("/register")
def register(data: RegisterRequest):
    with get_connection() as con:
        cur = con.cursor()

        cur.execute(
            "SELECT id FROM usuarios WHERE username = ? OR email = ?",
            (data.username, data.email)
        )

        if cur.fetchone():
            return {"error": "Usuario o email ya existe"}

        password_hash = hashlib.sha256(data.password.encode()).hexdigest()

        cur.execute("""
            INSERT INTO usuarios (
                nombre, apellidos, username, email,
                telefono, ciudad, fecha_nacimiento, password
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            data.nombre,
            data.apellidos,
            data.username,
            data.email,
            data.telefono,
            data.ciudad,
            data.fecha_nacimiento,
            password_hash
        ))

        user_id = cur.lastrowid
        con.commit()

    return {
        "id": user_id,
        "nombre": data.nombre,
        "apellidos": data.apellidos,
        "username": data.username,
        "email": data.email,
        "telefono": data.telefono,
        "ciudad": data.ciudad,
        "fecha_nacimiento": data.fecha_nacimiento
    }


# 👤 OBTENER USUARIO
@app.get("/usuarios/{user_id}")
def obtener_usuario(user_id: int):
    with get_connection() as con:
        cur = con.cursor()
        cur.execute("""
            SELECT id, nombre, apellidos, username,
                   email, telefono, ciudad,
                   fecha_nacimiento, vehiculo_activo_id
            FROM usuarios
            WHERE id = ?
        """, (user_id,))
        row = cur.fetchone()

    if not row:
        return {"error": "Usuario no encontrado"}

    return {
        "id": row[0],
        "nombre": row[1],
        "apellidos": row[2],
        "username": row[3],
        "email": row[4],
        "telefono": row[5],
        "ciudad": row[6],
        "fecha_nacimiento": row[7],
        "vehiculo_activo_id": row[8]
    }


# 🚗 VEHÍCULOS
@app.post("/vehiculos")
def crear_vehiculo(data: VehiculoRequest):
    with get_connection() as con:
        cur = con.cursor()
        cur.execute("""
            INSERT INTO vehiculos (
                user_id, tipo, marca, modelo,
                matricula, anio, combustible, consumo
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            data.user_id,
            data.tipo,
            data.marca,
            data.modelo,
            data.matricula,
            data.anio,
            data.combustible,
            data.consumo
        ))

        vehiculo_id = cur.lastrowid
        con.commit()

    return {
        "id": vehiculo_id,
        **data.dict()
    }


@app.get("/vehiculos/{user_id}")
def obtener_vehiculos(user_id: int):
    with get_connection() as con:
        cur = con.cursor()
        cur.execute("""
            SELECT id, tipo, marca, modelo,
                   matricula, anio, combustible, consumo
            FROM vehiculos
            WHERE user_id = ?
        """, (user_id,))
        rows = cur.fetchall()

    return [
        {
            "id": r[0],
            "tipo": r[1],
            "marca": r[2],
            "modelo": r[3],
            "matricula": r[4],
            "anio": r[5],
            "combustible": r[6],
            "consumo": r[7]
        }
        for r in rows
    ]


@app.delete("/vehiculos/{vehiculo_id}")
def borrar_vehiculo(vehiculo_id: int):
    with get_connection() as con:
        cur = con.cursor()
        cur.execute(
            "DELETE FROM vehiculos WHERE id = ?",
            (vehiculo_id,)
        )

        if cur.rowcount == 0:
            return {"error": "Vehículo no encontrado"}

        con.commit()

    return {"status": "ok"}


@app.put("/usuarios/{user_id}/vehiculo-activo/{vehiculo_id}")
def establecer_vehiculo_activo(user_id: int, vehiculo_id: int):
    with get_connection() as con:
        cur = con.cursor()

        cur.execute(
            "SELECT id FROM vehiculos WHERE id = ? AND user_id = ?",
            (vehiculo_id, user_id)
        )

        if not cur.fetchone():
            return {"error": "El vehículo no pertenece al usuario"}

        cur.execute(
            "UPDATE usuarios SET vehiculo_activo_id = ? WHERE id = ?",
            (vehiculo_id, user_id)
        )

        con.commit()

    return {"status": "ok", "vehiculo_activo_id": vehiculo_id}


# 🔑 CONTRASEÑAS
@app.put("/usuarios/{user_id}/password")
def cambiar_password(user_id: int, data: PasswordUpdateRequest):
    with get_connection() as con:
        cur = con.cursor()

        password_hash = hashlib.sha256(
            data.password.encode()
        ).hexdigest()

        cur.execute(
            "UPDATE usuarios SET password = ? WHERE id = ?",
            (password_hash, user_id)
        )

        if cur.rowcount == 0:
            return {"error": "Usuario no encontrado"}

        con.commit()

    return {"status": "ok"}


# ⛽ REPOSTAJES
@app.post("/repostajes")
def crear_repostaje(r: RepostajeIn):
    with get_connection() as con:
        cur = con.cursor()
        cur.execute("""
            INSERT INTO repostajes (
                vehiculo_id, fecha, litros,
                precio_total, kilometros
            ) VALUES (?, ?, ?, ?, ?)
        """, (
            r.vehiculo_id,
            r.fecha,
            r.litros,
            r.precio_total,
            r.kilometros
        ))

        repostaje_id = cur.lastrowid
        con.commit()

    return {
        "id": repostaje_id,
        **r.dict()
    }


@app.get("/repostajes/{vehiculo_id}")
def obtener_repostajes(vehiculo_id: int):
    with get_connection() as con:
        cur = con.cursor()
        cur.execute("""
            SELECT id, vehiculo_id, fecha,
                   litros, precio_total, kilometros
            FROM repostajes
            WHERE vehiculo_id = ?
            ORDER BY kilometros ASC
        """, (vehiculo_id,))

        rows = cur.fetchall()

    return [
        {
            "id": r[0],
            "vehiculo_id": r[1],
            "fecha": r[2],
            "litros": r[3],
            "precio_total": r[4],
            "kilometros": r[5]
        }
        for r in rows
    ]


@app.delete("/repostajes/{repostaje_id}")
def borrar_repostaje(repostaje_id: int):
    with get_connection() as con:
        cur = con.cursor()
        cur.execute(
            "DELETE FROM repostajes WHERE id = ?",
            (repostaje_id,)
        )

        if cur.rowcount == 0:
            return {"error": "Repostaje no encontrado"}

        con.commit()

    return {"status": "ok"}