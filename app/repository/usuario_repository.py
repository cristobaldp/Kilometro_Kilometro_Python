import hashlib
from app.data.database import get_connection


class UsuarioRepository:

    # -------------------------
    # LOGIN
    # -------------------------
    def find_by_username_and_password(self, username, password):
        password_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()

        con = get_connection()
        cur = con.cursor()

        cur.execute("""
            SELECT id, nombre, apellidos, username, email,
                   telefono, ciudad, fecha_nacimiento, vehiculo_activo_id,
                   unidad_consumo, formato_precio, periodo_estadisticas,
                   vista_estadisticas, aviso_km, aviso_consumo,
                   confirmar_acciones, cerrar_sesion
            FROM usuarios
            WHERE username = ? AND password = ?
        """, (username, password_hash))

        row = cur.fetchone()
        con.close()

        if not row:
            return None

        return {
            "id": row[0],
            "nombre": row[1],
            "apellidos": row[2],
            "username": row[3],
            "email": row[4],
            "telefono": row[5],
            "ciudad": row[6],
            "fecha_nacimiento": row[7],
            "vehiculo_activo_id": row[8],
            "unidad_consumo": row[9],
            "formato_precio": row[10],
            "periodo_estadisticas": row[11],
            "vista_estadisticas": row[12],
            "aviso_km": row[13],
            "aviso_consumo": bool(row[14]),
            "confirmar_acciones": bool(row[15]),
            "cerrar_sesion": bool(row[16]),
        }

    # -------------------------
    # REGISTRO
    # -------------------------
    def insert(self, datos):
        password_hash = hashlib.sha256(datos["password"].encode("utf-8")).hexdigest()

        con = get_connection()
        cur = con.cursor()

        cur.execute("""
            INSERT INTO usuarios
            (nombre, apellidos, username, email, telefono, ciudad, fecha_nacimiento, password)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            datos["nombre"],
            datos["apellidos"],
            datos["username"],
            datos["email"],
            datos["telefono"],
            datos["ciudad"],
            datos["fecha_nacimiento"],
            password_hash
        ))

        con.commit()
        con.close()

    # -------------------------
    # PERFIL
    # -------------------------
    def update_perfil(self, datos):
        con = get_connection()
        cur = con.cursor()

        cur.execute("""
            UPDATE usuarios
            SET nombre = ?, apellidos = ?, email = ?, telefono = ?, ciudad = ?
            WHERE id = ?
        """, (
            datos["nombre"],
            datos["apellidos"],
            datos["email"],
            datos["telefono"],
            datos["ciudad"],
            datos["id"]
        ))

        con.commit()
        con.close()

    # -------------------------
    # CONTRASEÑA
    # -------------------------
    def update_password(self, user_id, new_password):
        password_hash = hashlib.sha256(new_password.encode("utf-8")).hexdigest()

        con = get_connection()
        cur = con.cursor()

        cur.execute("""
            UPDATE usuarios
            SET password = ?
            WHERE id = ?
        """, (password_hash, user_id))

        con.commit()
        con.close()

    # -------------------------
    # BORRAR CUENTA
    # -------------------------
    def delete_user(self, user_id):
        con = get_connection()
        cur = con.cursor()

        cur.execute("DELETE FROM usuarios WHERE id = ?", (user_id,))
        con.commit()
        con.close()

    # -------------------------
    # AJUSTES
    # -------------------------
    def get_ajustes(self, user_id):
        con = get_connection()
        cur = con.cursor()

        cur.execute("""
            SELECT unidad_consumo, formato_precio, periodo_estadisticas,
                   vista_estadisticas, aviso_km, aviso_consumo,
                   confirmar_acciones, cerrar_sesion
            FROM usuarios
            WHERE id = ?
        """, (user_id,))

        row = cur.fetchone()
        con.close()

        if not row:
            return None

        return {
            "unidad_consumo": row[0],
            "formato_precio": row[1],
            "periodo_estadisticas": row[2],
            "vista_estadisticas": row[3],
            "aviso_km": row[4],
            "aviso_consumo": bool(row[5]),
            "confirmar_acciones": bool(row[6]),
            "cerrar_sesion": bool(row[7]),
        }

    def update_ajustes(self, user_id, datos):
        con = get_connection()
        cur = con.cursor()

        cur.execute("""
            UPDATE usuarios
            SET unidad_consumo = ?,
                formato_precio = ?,
                periodo_estadisticas = ?,
                vista_estadisticas = ?,
                aviso_km = ?,
                aviso_consumo = ?,
                confirmar_acciones = ?,
                cerrar_sesion = ?
            WHERE id = ?
        """, (
            datos["unidad_consumo"],
            datos["formato_precio"],
            datos["periodo_estadisticas"],
            datos["vista_estadisticas"],
            datos["aviso_km"],
            int(datos["aviso_consumo"]),
            int(datos["confirmar_acciones"]),
            int(datos["cerrar_sesion"]),
            user_id
        ))

        con.commit()
        con.close()
