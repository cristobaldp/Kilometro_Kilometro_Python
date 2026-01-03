from app.data.database import get_connection


class EstadisticasRepository:

    # =================================================
    # GASTO
    # =================================================

    # -----------------------------
    # GASTO TOTAL POR MES (AÑO)
    # -----------------------------
    def gasto_por_mes(self, vehiculo_id, anio):
        """
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

    # -----------------------------
    # GASTO DIARIO (MES + AÑO)
    # -----------------------------
    def gasto_diario(self, vehiculo_id, mes, anio):
        """
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

    # -----------------------------
    # CONSUMO MEDIO POR MES (AÑO)
    # -----------------------------
    def consumo_por_mes(self, vehiculo_id, anio):
        """
        Devuelve consumo medio L/100km por mes:
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

    # -----------------------------
    # CONSUMO MEDIO DIARIO (MES + AÑO)
    # -----------------------------
    def consumo_diario(self, vehiculo_id, mes, anio):
        """
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
