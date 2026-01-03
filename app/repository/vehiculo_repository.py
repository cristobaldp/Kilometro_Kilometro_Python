from app.data.database import get_connection


class VehiculoRepository:

    def find_by_user(self, user_id):
        con = get_connection()
        cur = con.cursor()
        cur.execute("""
            SELECT id, tipo, marca, modelo, matricula, anio, combustible, consumo
            FROM vehiculos
            WHERE user_id = ?
        """, (user_id,))
        rows = cur.fetchall()
        con.close()
        return rows

    def insert(self, user_id, tipo, marca, modelo, matricula, anio, combustible, consumo):
        con = get_connection()
        cur = con.cursor()
        cur.execute("""
            INSERT INTO vehiculos
            (user_id, tipo, marca, modelo, matricula, anio, combustible, consumo)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (user_id, tipo, marca, modelo, matricula, anio, combustible, consumo))
        con.commit()
        con.close()

    def delete(self, vehiculo_id):
        con = get_connection()
        cur = con.cursor()
        cur.execute("DELETE FROM vehiculos WHERE id = ?", (vehiculo_id,))
        con.commit()
        con.close()

    def set_activo(self, user_id, vehiculo_id):
        con = get_connection()
        cur = con.cursor()
        cur.execute("""
            UPDATE usuarios
            SET vehiculo_activo_id = ?
            WHERE id = ?
        """, (vehiculo_id, user_id))
        con.commit()
        con.close()

    def clear_activo(self, user_id):
        con = get_connection()
        cur = con.cursor()
        cur.execute("""
            UPDATE usuarios
            SET vehiculo_activo_id = NULL
            WHERE id = ?
        """, (user_id,))
        con.commit()
        con.close()
