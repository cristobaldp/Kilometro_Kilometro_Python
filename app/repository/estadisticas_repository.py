from app.data.database import get_connection


class EstadisticasRepository:
    """
    Repositorio de estadísticas:
    - Gasto
    - Consumo
    - Por mes / por día
    """

    # =================================================
    # GASTO
    # =================================================

    def gasto_por_mes(self, vehiculo_id, anio):
        """
        Gasto total por mes de un año
        Devuelve:
        [(mes, gasto_total), ...]
        """
        con = get_connection()
        cur = con.cursor()

        cur.execute("""
            SELECT
                strftime('%m', fecha) AS mes,
                SUM(precio_total) AS gasto
            FROM repostajes
            WHERE vehiculo_id = ?
              AND strftime('%Y', fecha) = ?
            GROUP BY mes
            ORDER BY mes
        """, (vehiculo_id, str(anio)))

        datos = cur.fetchall()
        con.close()
        return datos

    def gasto_diario(self, vehiculo_id, mes, anio):
        """
        Gasto diario de un mes concreto
        Devuelve:
        [(fecha, gasto_diario), ...]
        """
        con = get_connection()
        cur = con.cursor()

        cur.execute("""
            SELECT
                fecha,
                SUM(precio_total) AS gasto
            FROM repostajes
            WHERE vehiculo_id = ?
              AND strftime('%Y', fecha) = ?
              AND strftime('%m', fecha) = ?
            GROUP BY fecha
            ORDER BY fecha
        """, (vehiculo_id, str(anio), f"{int(mes):02d}"))

        datos = cur.fetchall()
        con.close()
        return datos

    # =================================================
    # CONSUMO
    # =================================================

    def consumo_por_mes(self, vehiculo_id, anio):
        """
        Consumo medio mensual (L/100km)
        Devuelve:
        [(mes, consumo), ...]
        """
        con = get_connection()
        cur = con.cursor()

        cur.execute("""
            SELECT
                strftime('%m', fecha) AS mes,
                AVG(litros / (kilometros / 100.0)) AS consumo
            FROM repostajes
            WHERE vehiculo_id = ?
              AND strftime('%Y', fecha) = ?
            GROUP BY mes
            ORDER BY mes
        """, (vehiculo_id, str(anio)))

        datos = cur.fetchall()
        con.close()
        return datos

    def consumo_diario(self, vehiculo_id, mes, anio):
        """
        Consumo medio diario de un mes concreto
        Devuelve:
        [(fecha, consumo_medio), ...]
        """
        con = get_connection()
        cur = con.cursor()

        cur.execute("""
            SELECT
                fecha,
                AVG(litros / (kilometros / 100.0)) AS consumo
            FROM repostajes
            WHERE vehiculo_id = ?
              AND strftime('%Y', fecha) = ?
              AND strftime('%m', fecha) = ?
            GROUP BY fecha
            ORDER BY fecha
        """, (vehiculo_id, str(anio), f"{int(mes):02d}"))

        datos = cur.fetchall()
        con.close()
        return datos
