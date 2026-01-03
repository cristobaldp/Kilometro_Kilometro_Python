from app.data.database import get_connection


class RepostajeRepository:

    def find_by_vehiculo(self, vehiculo_id):
        con = get_connection()
        cur = con.cursor()

        cur.execute("""
            SELECT id, fecha, litros, precio_total, kilometros
            FROM repostajes
            WHERE vehiculo_id = ?
            ORDER BY kilometros ASC
        """, (vehiculo_id,))

        datos = cur.fetchall()
        con.close()
        return datos

    def insert(self, vehiculo_id, fecha, litros, precio_total, kilometros):
        con = get_connection()
        cur = con.cursor()

        cur.execute("""
            INSERT INTO repostajes
            (vehiculo_id, fecha, litros, precio_total, kilometros)
            VALUES (?, ?, ?, ?, ?)
        """, (vehiculo_id, fecha, litros, precio_total, kilometros))

        con.commit()
        con.close()

    def ultimo_kilometraje(self, vehiculo_id):
        con = get_connection()
        cur = con.cursor()

        cur.execute("""
            SELECT MAX(kilometros)
            FROM repostajes
            WHERE vehiculo_id = ?
        """, (vehiculo_id,))

        km = cur.fetchone()[0]
        con.close()
        return km
    
    def delete(self, repostaje_id):
      con = get_connection()
      cur = con.cursor()

      cur.execute(
        "DELETE FROM repostajes WHERE id = ?",
        (repostaje_id,)
    )

      con.commit()
      con.close()

