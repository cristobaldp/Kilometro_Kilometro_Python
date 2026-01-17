from app.data.database import get_connection


class EstadisticasRepository:
    """
    Repositorio de estadísticas avanzadas:
    - Gasto (diario, mensual, anual)
    - Consumo (diario, mensual, anual)
    - Métricas comparativas
    - Rankings y análisis
    """

    # =================================================
    # GASTO
    # =================================================

    def gasto_por_mes(self, vehiculo_id, anio):
        """
        Gasto total por mes de un año
        Devuelve: [(mes, gasto_total), ...]
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
        Devuelve: [(fecha, gasto_diario), ...]
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
        """
        Gasto total del período
        Devuelve: float
        """
        con = get_connection()
        cur = con.cursor()

        cur.execute("""
            SELECT COALESCE(SUM(precio_total), 0) AS total
            FROM repostajes
            WHERE vehiculo_id = ?
              AND strftime('%Y', fecha) = ?
              AND strftime('%m', fecha) = ?
        """, (vehiculo_id, str(anio), f"{int(mes):02d}"))

        resultado = cur.fetchone()
        con.close()
        return resultado[0] if resultado else 0.0

    def gasto_promedio_repostaje(self, vehiculo_id, mes, anio):
        """
        Promedio de gasto por repostaje
        Devuelve: float
        """
        con = get_connection()
        cur = con.cursor()

        cur.execute("""
            SELECT COALESCE(AVG(precio_total), 0) AS promedio
            FROM repostajes
            WHERE vehiculo_id = ?
              AND strftime('%Y', fecha) = ?
              AND strftime('%m', fecha) = ?
        """, (vehiculo_id, str(anio), f"{int(mes):02d}"))

        resultado = cur.fetchone()
        con.close()
        return resultado[0] if resultado else 0.0

    def comparacion_mes_anterior(self, vehiculo_id, mes, anio):
        """
        Comparación con el mes anterior
        Devuelve: (gasto_actual, gasto_anterior, porcentaje_cambio)
        """
        con = get_connection()
        cur = con.cursor()

        # Gasto mes actual
        cur.execute("""
            SELECT COALESCE(SUM(precio_total), 0)
            FROM repostajes
            WHERE vehiculo_id = ?
              AND strftime('%Y', fecha) = ?
              AND strftime('%m', fecha) = ?
        """, (vehiculo_id, str(anio), f"{int(mes):02d}"))
        gasto_actual = cur.fetchone()[0]

        # Calcular mes anterior
        mes_anterior = mes - 1 if mes > 1 else 12
        anio_anterior = anio if mes > 1 else anio - 1

        cur.execute("""
            SELECT COALESCE(SUM(precio_total), 0)
            FROM repostajes
            WHERE vehiculo_id = ?
              AND strftime('%Y', fecha) = ?
              AND strftime('%m', fecha) = ?
        """, (vehiculo_id, str(anio_anterior), f"{int(mes_anterior):02d}"))
        gasto_anterior = cur.fetchone()[0]

        con.close()

        # Calcular porcentaje de cambio
        if gasto_anterior > 0:
            porcentaje = ((gasto_actual - gasto_anterior) / gasto_anterior) * 100
        else:
            porcentaje = 0

        return (gasto_actual, gasto_anterior, porcentaje)

    # =================================================
    # CONSUMO
    # =================================================

    def consumo_por_mes(self, vehiculo_id, anio):
        """
        Consumo medio mensual (L/100km)
        Devuelve: [(mes, consumo), ...]
        """
        con = get_connection()
        cur = con.cursor()

        cur.execute("""
            SELECT
                strftime('%m', fecha) AS mes,
                (SUM(litros) / NULLIF(SUM(kilometros), 0)) * 100 AS consumo
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
        Consumo diario de un mes concreto
        Devuelve: [(fecha, consumo), ...]
        """
        con = get_connection()
        cur = con.cursor()

        cur.execute("""
            SELECT
                fecha,
                (SUM(litros) / NULLIF(SUM(kilometros), 0)) * 100 AS consumo
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

    def consumo_promedio_periodo(self, vehiculo_id, mes, anio):
        """
        Consumo promedio del período
        Devuelve: float (L/100km)
        """
        con = get_connection()
        cur = con.cursor()

        cur.execute("""
            SELECT (SUM(litros) / NULLIF(SUM(kilometros), 0)) * 100 AS consumo
            FROM repostajes
            WHERE vehiculo_id = ?
              AND strftime('%Y', fecha) = ?
              AND strftime('%m', fecha) = ?
        """, (vehiculo_id, str(anio), f"{int(mes):02d}"))

        resultado = cur.fetchone()
        con.close()
        return resultado[0] if resultado and resultado[0] else 0.0

    # =================================================
    # MÉTRICAS AVANZADAS
    # =================================================

    def precio_por_litro_promedio(self, vehiculo_id, mes, anio):
        """
        Precio promedio por litro en el período
        Devuelve: float
        """
        con = get_connection()
        cur = con.cursor()

        cur.execute("""
            SELECT 
                COALESCE(SUM(precio_total) / NULLIF(SUM(litros), 0), 0) AS precio_litro
            FROM repostajes
            WHERE vehiculo_id = ?
              AND strftime('%Y', fecha) = ?
              AND strftime('%m', fecha) = ?
        """, (vehiculo_id, str(anio), f"{int(mes):02d}"))

        resultado = cur.fetchone()
        con.close()
        return resultado[0] if resultado else 0.0

    def total_kilometros_periodo(self, vehiculo_id, mes, anio):
        """
        Total de kilómetros recorridos en el período
        Devuelve: float
        """
        con = get_connection()
        cur = con.cursor()

        cur.execute("""
            SELECT COALESCE(SUM(kilometros), 0) AS total_km
            FROM repostajes
            WHERE vehiculo_id = ?
              AND strftime('%Y', fecha) = ?
              AND strftime('%m', fecha) = ?
        """, (vehiculo_id, str(anio), f"{int(mes):02d}"))

        resultado = cur.fetchone()
        con.close()
        return resultado[0] if resultado else 0.0

    def total_litros_periodo(self, vehiculo_id, mes, anio):
        """
        Total de litros consumidos en el período
        Devuelve: float
        """
        con = get_connection()
        cur = con.cursor()

        cur.execute("""
            SELECT COALESCE(SUM(litros), 0) AS total_litros
            FROM repostajes
            WHERE vehiculo_id = ?
              AND strftime('%Y', fecha) = ?
              AND strftime('%m', fecha) = ?
        """, (vehiculo_id, str(anio), f"{int(mes):02d}"))

        resultado = cur.fetchone()
        con.close()
        return resultado[0] if resultado else 0.0

    def numero_repostajes_periodo(self, vehiculo_id, mes, anio):
        """
        Número total de repostajes en el período
        Devuelve: int
        """
        con = get_connection()
        cur = con.cursor()

        cur.execute("""
            SELECT COUNT(*) AS total
            FROM repostajes
            WHERE vehiculo_id = ?
              AND strftime('%Y', fecha) = ?
              AND strftime('%m', fecha) = ?
        """, (vehiculo_id, str(anio), f"{int(mes):02d}"))

        resultado = cur.fetchone()
        con.close()
        return resultado[0] if resultado else 0

    def gasto_por_kilometro(self, vehiculo_id, mes, anio):
        """
        Gasto por kilómetro recorrido (€/km)
        Devuelve: float
        """
        con = get_connection()
        cur = con.cursor()

        cur.execute("""
            SELECT 
                COALESCE(SUM(precio_total) / NULLIF(SUM(kilometros), 0), 0) AS gasto_km
            FROM repostajes
            WHERE vehiculo_id = ?
              AND strftime('%Y', fecha) = ?
              AND strftime('%m', fecha) = ?
        """, (vehiculo_id, str(anio), f"{int(mes):02d}"))

        resultado = cur.fetchone()
        con.close()
        return resultado[0] if resultado else 0.0

    def mejor_repostaje(self, vehiculo_id, mes, anio):
        """
        Repostaje más económico (menor precio/litro)
        Devuelve: (fecha, precio_litro)
        """
        con = get_connection()
        cur = con.cursor()

        cur.execute("""
            SELECT 
                fecha,
                (precio_total / litros) AS precio_litro
            FROM repostajes
            WHERE vehiculo_id = ?
              AND strftime('%Y', fecha) = ?
              AND strftime('%m', fecha) = ?
            ORDER BY precio_litro ASC
            LIMIT 1
        """, (vehiculo_id, str(anio), f"{int(mes):02d}"))

        resultado = cur.fetchone()
        con.close()
        return resultado if resultado else (None, 0.0)

    def peor_repostaje(self, vehiculo_id, mes, anio):
        """
        Repostaje más caro (mayor precio/litro)
        Devuelve: (fecha, precio_litro)
        """
        con = get_connection()
        cur = con.cursor()

        cur.execute("""
            SELECT 
                fecha,
                (precio_total / litros) AS precio_litro
            FROM repostajes
            WHERE vehiculo_id = ?
              AND strftime('%Y', fecha) = ?
              AND strftime('%m', fecha) = ?
            ORDER BY precio_litro DESC
            LIMIT 1
        """, (vehiculo_id, str(anio), f"{int(mes):02d}"))

        resultado = cur.fetchone()
        con.close()
        return resultado if resultado else (None, 0.0)

    def tendencia_precio_litro(self, vehiculo_id, mes, anio):
        """
        Tendencia del precio por litro día a día
        Devuelve: [(fecha, precio_litro), ...]
        """
        con = get_connection()
        cur = con.cursor()

        cur.execute("""
            SELECT 
                fecha,
                AVG(precio_total / litros) AS precio_litro
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

    def resumen_completo(self, vehiculo_id, mes, anio):
        """
        Resumen completo de todas las métricas
        Devuelve: dict con todas las estadísticas
        """
        return {
            'gasto_total': self.gasto_total_periodo(vehiculo_id, mes, anio),
            'gasto_promedio': self.gasto_promedio_repostaje(vehiculo_id, mes, anio),
            'consumo_promedio': self.consumo_promedio_periodo(vehiculo_id, mes, anio),
            'precio_litro': self.precio_por_litro_promedio(vehiculo_id, mes, anio),
            'total_km': self.total_kilometros_periodo(vehiculo_id, mes, anio),
            'total_litros': self.total_litros_periodo(vehiculo_id, mes, anio),
            'num_repostajes': self.numero_repostajes_periodo(vehiculo_id, mes, anio),
            'gasto_km': self.gasto_por_kilometro(vehiculo_id, mes, anio),
            'mejor_repostaje': self.mejor_repostaje(vehiculo_id, mes, anio),
            'peor_repostaje': self.peor_repostaje(vehiculo_id, mes, anio)
        }

    def comparacion_anual(self, vehiculo_id, anio):
        """
        Comparación mes a mes del año completo
        Devuelve: [(mes, gasto, consumo, precio_litro), ...]
        """
        con = get_connection()
        cur = con.cursor()

        cur.execute("""
            SELECT
                strftime('%m', fecha) AS mes,
                SUM(precio_total) AS gasto,
                (SUM(litros) / NULLIF(SUM(kilometros), 0)) * 100 AS consumo,
                SUM(precio_total) / NULLIF(SUM(litros), 0) AS precio_litro
            FROM repostajes
            WHERE vehiculo_id = ?
              AND strftime('%Y', fecha) = ?
            GROUP BY mes
            ORDER BY mes
        """, (vehiculo_id, str(anio)))

        datos = cur.fetchall()
        con.close()
        return datos