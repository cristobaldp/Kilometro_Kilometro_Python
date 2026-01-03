from app.data.database import get_connection


class EstadisticasRepository:

    # -------------------------------------------------
    # GASTO TOTAL POR MES
    # -------------------------------------------------
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

    # -------------------------------------------------
    # GASTO TOTAL POR MES (FILTRADO POR MES)
    # -------------------------------------------------
    def gasto_por_mes_y_anio(self, vehiculo_id, mes, anio):
        con = get_connection()
        cur = con.cursor()

        cur.execute("""
            SELECT fecha, precio_total
            FROM repostajes
            WHERE vehiculo_id = ?
              AND strftime('%Y', fecha) = ?
              AND strftime('%m', fecha) = ?
            ORDER BY fecha
        """, (vehiculo_id, str(anio), f"{int(mes):02d}"))

        datos = cur.fetchall()
        con.close()
        return datos

    # -------------------------------------------------
    # CONSUMO MEDIO POR MES
    # -------------------------------------------------
    def consumo_por_mes(self, vehiculo_id, anio):
        """
        Devuelve consumo medio L/100km por mes
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

    # -------------------------------------------------
    # CONSUMO DETALLADO POR MES
    # -------------------------------------------------
    def consumo_por_mes_y_anio(self, vehiculo_id, mes, anio):
        con = get_connection()
        cur = con.cursor()

        cur.execute("""
            SELECT fecha,
                   litros,
                   kilometros,
                   (litros / (kilometros / 100.0)) AS consumo
            FROM repostajes
            WHERE vehiculo_id = ?
              AND strftime('%Y', fecha) = ?
              AND strftime('%m', fecha) = ?
            ORDER BY fecha
        """, (vehiculo_id, str(anio), f"{int(mes):02d}"))

        datos = cur.fetchall()
        con.close()
        return datos
