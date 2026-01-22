from app.data.database import get_connection


class EstadisticasRepository:
    """
    Repositorio de estadísticas.
    SOLO ACCEDE A BD.
    NO hace cálculos que dependan de diferencias de odómetro.
    """

    # =================================================
    # GASTO
    # =================================================

    def gasto_por_mes(self, vehiculo_id, anio):
        """
        Gasto total por mes del año
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
        Gasto diario de un mes
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

    def gasto_total_periodo(self, vehiculo_id, mes, anio):
        con = get_connection()
        cur = con.cursor()
        cur.execute("""
            SELECT COALESCE(SUM(precio_total), 0)
            FROM repostajes
            WHERE vehiculo_id = ?
              AND strftime('%Y', fecha) = ?
              AND strftime('%m', fecha) = ?
        """, (vehiculo_id, str(anio), f"{int(mes):02d}"))
        total = cur.fetchone()[0]
        con.close()
        return total

    def gasto_promedio_repostaje(self, vehiculo_id, mes, anio):
        con = get_connection()
        cur = con.cursor()
        cur.execute("""
            SELECT COALESCE(AVG(precio_total), 0)
            FROM repostajes
            WHERE vehiculo_id = ?
              AND strftime('%Y', fecha) = ?
              AND strftime('%m', fecha) = ?
        """, (vehiculo_id, str(anio), f"{int(mes):02d}"))
        promedio = cur.fetchone()[0]
        con.close()
        return promedio

    # =================================================
    # CONSUMO (SOLO DATOS CRUDOS)
    # =================================================

    def consumo_diario(self, vehiculo_id, mes, anio):
        """
        Datos diarios para gráfica.
        El cálculo real se hace en el controller.
        """
        con = get_connection()
        cur = con.cursor()
        cur.execute("""
            SELECT fecha, litros, kilometros
            FROM repostajes
            WHERE vehiculo_id = ?
              AND strftime('%Y', fecha) = ?
              AND strftime('%m', fecha) = ?
            ORDER BY kilometros
        """, (vehiculo_id, str(anio), f"{int(mes):02d}"))
        datos = cur.fetchall()
        con.close()
        return datos

    # =================================================
    # MÉTRICAS BÁSICAS
    # =================================================

    def total_kilometros_periodo(self, vehiculo_id, mes, anio):
        """
        DEVUELVE SOLO odómetros.
        El km real = último - primero (fuera del repository)
        """
        con = get_connection()
        cur = con.cursor()
        cur.execute("""
            SELECT kilometros
            FROM repostajes
            WHERE vehiculo_id = ?
              AND strftime('%Y', fecha) = ?
              AND strftime('%m', fecha) = ?
            ORDER BY kilometros
        """, (vehiculo_id, str(anio), f"{int(mes):02d}"))
        datos = cur.fetchall()
        con.close()
        return datos

    def total_litros_periodo(self, vehiculo_id, mes, anio):
        con = get_connection()
        cur = con.cursor()
        cur.execute("""
            SELECT COALESCE(SUM(litros), 0)
            FROM repostajes
            WHERE vehiculo_id = ?
              AND strftime('%Y', fecha) = ?
              AND strftime('%m', fecha) = ?
        """, (vehiculo_id, str(anio), f"{int(mes):02d}"))
        total = cur.fetchone()[0]
        con.close()
        return total

    def numero_repostajes_periodo(self, vehiculo_id, mes, anio):
        con = get_connection()
        cur = con.cursor()
        cur.execute("""
            SELECT COUNT(*)
            FROM repostajes
            WHERE vehiculo_id = ?
              AND strftime('%Y', fecha) = ?
              AND strftime('%m', fecha) = ?
        """, (vehiculo_id, str(anio), f"{int(mes):02d}"))
        total = cur.fetchone()[0]
        con.close()
        return total

    def precio_por_litro_promedio(self, vehiculo_id, mes, anio):
        con = get_connection()
        cur = con.cursor()
        cur.execute("""
            SELECT COALESCE(SUM(precio_total) / NULLIF(SUM(litros), 0), 0)
            FROM repostajes
            WHERE vehiculo_id = ?
              AND strftime('%Y', fecha) = ?
              AND strftime('%m', fecha) = ?
        """, (vehiculo_id, str(anio), f"{int(mes):02d}"))
        precio = cur.fetchone()[0]
        con.close()
        return precio

    def mejor_repostaje(self, vehiculo_id, mes, anio):
        con = get_connection()
        cur = con.cursor()
        cur.execute("""
            SELECT fecha, (precio_total / litros)
            FROM repostajes
            WHERE vehiculo_id = ?
              AND strftime('%Y', fecha) = ?
              AND strftime('%m', fecha) = ?
            ORDER BY (precio_total / litros) ASC
            LIMIT 1
        """, (vehiculo_id, str(anio), f"{int(mes):02d}"))
        dato = cur.fetchone()
        con.close()
        return dato if dato else (None, 0.0)

    def peor_repostaje(self, vehiculo_id, mes, anio):
        con = get_connection()
        cur = con.cursor()
        cur.execute("""
            SELECT fecha, (precio_total / litros)
            FROM repostajes
            WHERE vehiculo_id = ?
              AND strftime('%Y', fecha) = ?
              AND strftime('%m', fecha) = ?
            ORDER BY (precio_total / litros) DESC
            LIMIT 1
        """, (vehiculo_id, str(anio), f"{int(mes):02d}"))
        dato = cur.fetchone()
        con.close()
        return dato if dato else (None, 0.0)

    # =================================================
    # RESUMEN (SIN CONSUMO NI COSTE/KM)
    # =================================================

    def resumen_completo(self, vehiculo_id, mes, anio):
        return {
            "gasto_total": self.gasto_total_periodo(vehiculo_id, mes, anio),
            "gasto_promedio": self.gasto_promedio_repostaje(vehiculo_id, mes, anio),
            "total_litros": self.total_litros_periodo(vehiculo_id, mes, anio),
            "num_repostajes": self.numero_repostajes_periodo(vehiculo_id, mes, anio),
            "precio_litro": self.precio_por_litro_promedio(vehiculo_id, mes, anio),
            "mejor_repostaje": self.mejor_repostaje(vehiculo_id, mes, anio),
            "peor_repostaje": self.peor_repostaje(vehiculo_id, mes, anio)
        }
    
    
    def repostajes_periodo(self, vehiculo_id, mes, anio):
     con = get_connection()
     cur = con.cursor()

     cur.execute("""
        SELECT fecha, litros, kilometros, precio_total
        FROM repostajes
        WHERE vehiculo_id = ?
          AND strftime('%Y', fecha) = ?
          AND strftime('%m', fecha) = ?
        ORDER BY kilometros
     """, (vehiculo_id, str(anio), f"{mes:02d}"))

     rows = cur.fetchall()
     con.close()

     return [{
        "fecha": r[0],
        "litros": r[1],
        "kilometros": r[2],
        "precio_total": r[3]
     } for r in rows]

