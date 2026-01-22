import os
import tempfile
from datetime import datetime

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from weasyprint import HTML


BASE_DIR = os.path.dirname(__file__)
TEMPLATE_HTML = os.path.join(BASE_DIR, "templates", "informe_estadisticas.html")
TEMPLATE_CSS = os.path.join(BASE_DIR, "templates", "informe_estadisticas.css")


class InformeEstadisticasPDF:
    """
    Genera el PDF de estadísticas.
    NO recalcula datos complejos.
    SOLO representa lo que recibe del controller.
    """

    # ======================================================
    # API PÚBLICA
    # ======================================================
    @staticmethod
    def generar(
        ruta_pdf,
        usuario: dict,
        vehiculo: dict,
        datos_graficas: dict,   # {"gasto": [(fecha, €)], "consumo": [(fecha, L/100km)]}
        metricas: dict,
        periodo: str
    ):
        if not datos_graficas or not datos_graficas.get("gasto"):
            raise ValueError("No hay datos para generar el informe")

        fecha_gen = datetime.now().strftime("%d/%m/%Y %H:%M")

        # ==================================================
        # RESUMEN EJECUTIVO
        # ==================================================
        consumos = datos_graficas.get("consumo", [])
        consumo_real = (
            round(sum(v for _, v in consumos) / len(consumos), 2)
            if consumos else 0.0
        )

        consumo_decl = None
        raw = vehiculo.get("Consumo declarado")
        if raw:
            consumo_decl = float(raw.replace("L/100km", "").strip())

        diferencia = (
            ((consumo_real - consumo_decl) / consumo_decl) * 100
            if consumo_decl else None
        )

        estado, estado_clase, comentario, recomendaciones = (
            InformeEstadisticasPDF._estado_consumo(
                consumo_real, consumo_decl, diferencia
            )
        )

        metricas_formateadas = InformeEstadisticasPDF._formatear_metricas(metricas)

        # ==================================================
        # GRÁFICAS
        # ==================================================
        with tempfile.TemporaryDirectory() as tmp:
            graf_gasto = os.path.join(tmp, "gasto.png")
            graf_consumo = os.path.join(tmp, "consumo.png")
            graf_comp = os.path.join(tmp, "comparativa.png")

            InformeEstadisticasPDF._grafica_gasto(
                datos_graficas["gasto"], graf_gasto
            )
            InformeEstadisticasPDF._grafica_consumo(
                datos_graficas.get("consumo", []), graf_consumo
            )
            InformeEstadisticasPDF._grafica_comparativa(
                datos_graficas.get("consumo", []),
                consumo_decl,
                graf_comp
            )

            html = InformeEstadisticasPDF._render_html(
                usuario,
                vehiculo,
                metricas_formateadas,
                periodo,
                fecha_gen,
                consumo_real,
                consumo_decl,
                diferencia,
                estado,
                estado_clase,
                comentario,
                recomendaciones,
                graf_gasto,
                graf_consumo,
                graf_comp
            )

            HTML(
                string=html,
                base_url=BASE_DIR
            ).write_pdf(
                ruta_pdf,
                stylesheets=[TEMPLATE_CSS]
            )

    # ======================================================
    # ESTADO CONSUMO
    # ======================================================
    @staticmethod
    def _estado_consumo(consumo_real, consumo_decl, diferencia):
        if not consumo_decl:
            return (
                "SIN DATOS",
                "normal",
                "No se dispone de consumo declarado para realizar la comparación.",
                ["Añade el consumo oficial del vehículo."]
            )

        if consumo_real <= consumo_decl:
            return (
                "EFICIENTE",
                "eficiente",
                "El consumo real está dentro de los valores esperados.",
                [
                    "Mantén este estilo de conducción.",
                    "Continúa realizando mantenimientos periódicos."
                ]
            )
        elif diferencia <= 10:
            return (
                "NORMAL",
                "normal",
                "El consumo es correcto, aunque podría optimizarse.",
                [
                    "Evita aceleraciones bruscas.",
                    "Revisa la presión de los neumáticos."
                ]
            )
        else:
            return (
                "INEFICIENTE",
                "ineficiente",
                "El consumo es superior al recomendado.",
                [
                    "Reduce aceleraciones agresivas.",
                    "Evita sobrecargar el vehículo.",
                    "Comprueba el estado del motor."
                ]
            )

    # ======================================================
    # FORMATO MÉTRICAS
    # ======================================================
    @staticmethod
    def _formatear_metricas(metricas: dict):
        resultado = {}

        for clave, valor in metricas.items():
            if clave == "gasto_total":
                resultado["Gasto total"] = f"{valor:.2f} €"

            elif clave == "gasto_promedio":
                resultado["Gasto medio por repostaje"] = f"{valor:.2f} €"

            elif clave == "total_litros":
                resultado["Litros totales"] = f"{valor:.2f} L"

            elif clave == "num_repostajes":
                resultado["Número de repostajes"] = valor

            elif clave == "precio_litro":
                resultado["Precio medio por litro"] = f"{valor:.2f} €/L"

            elif clave == "mejor_repostaje" and valor and valor[0]:
                fecha, precio = valor
                resultado["Repostaje más eficiente"] = (
                    f"{datetime.strptime(fecha, '%Y-%m-%d').strftime('%d/%m/%Y')} "
                    f"({precio:.2f} €/L)"
                )

            elif clave == "peor_repostaje" and valor and valor[0]:
                fecha, precio = valor
                resultado["Repostaje menos eficiente"] = (
                    f"{datetime.strptime(fecha, '%Y-%m-%d').strftime('%d/%m/%Y')} "
                    f"({precio:.2f} €/L)"
                )

        return resultado

    # ======================================================
    # GRÁFICAS
    # ======================================================
    @staticmethod
    def _grafica_gasto(datos, ruta):
        fechas = [datetime.strptime(f, "%Y-%m-%d") for f, _ in datos]
        valores = [v for _, v in datos]

        plt.figure(figsize=(7, 4))
        plt.plot(fechas, valores, marker="o", linewidth=2)
        plt.title("Evolución del gasto (€)")
        plt.xlabel("Fecha")
        plt.ylabel("€")
        plt.grid(alpha=0.3)
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%d %b"))
        plt.gcf().autofmt_xdate()
        plt.tight_layout()
        plt.savefig(ruta)
        plt.close()

    @staticmethod
    def _grafica_consumo(datos, ruta):
        if not datos:
            return

        fechas = [datetime.strptime(f, "%Y-%m-%d") for f, _ in datos]
        valores = [v for _, v in datos]

        plt.figure(figsize=(7, 4))
        plt.plot(fechas, valores, marker="o", linewidth=2)
        plt.title("Evolución del consumo (L/100km)")
        plt.xlabel("Fecha")
        plt.ylabel("L / 100 km")
        plt.grid(alpha=0.3)
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%d %b"))
        plt.gcf().autofmt_xdate()
        plt.tight_layout()
        plt.savefig(ruta)
        plt.close()

    @staticmethod
    def _grafica_comparativa(datos, consumo_decl, ruta):
        if not datos:
            return

        fechas = [datetime.strptime(f, "%Y-%m-%d") for f, _ in datos]
        valores = [v for _, v in datos]
        media_real = sum(valores) / len(valores)

        plt.figure(figsize=(7, 4))
        plt.plot(fechas, [media_real] * len(fechas), label="Consumo real", linewidth=2)

        if consumo_decl:
            plt.axhline(consumo_decl, linestyle="--", label="Consumo declarado")

        plt.title("Consumo real vs consumo declarado")
        plt.xlabel("Fecha")
        plt.ylabel("L / 100 km")
        plt.legend()
        plt.grid(alpha=0.3)
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%d %b"))
        plt.gcf().autofmt_xdate()
        plt.tight_layout()
        plt.savefig(ruta)
        plt.close()

    # ======================================================
    # HTML
    # ======================================================
    @staticmethod
    def _file_url(path):
        return f"file:///{path.replace(os.sep, '/')}"

    @staticmethod
    def _render_html(
        usuario,
        vehiculo,
        metricas,
        periodo,
        fecha_gen,
        consumo_real,
        consumo_decl,
        diferencia,
        estado,
        estado_clase,
        comentario,
        recomendaciones,
        graf_gasto,
        graf_consumo,
        graf_comp
    ):
        with open(TEMPLATE_HTML, encoding="utf-8") as f:
            html = f.read()

        html = html.replace("{{ fecha_generacion }}", fecha_gen)
        html = html.replace("{{ periodo }}", periodo)

        html = html.replace(
            "{{ usuario }}",
            "<br>".join(f"{k}: {v}" for k, v in usuario.items() if v)
        )
        html = html.replace(
            "{{ vehiculo }}",
            "<br>".join(f"{k}: {v}" for k, v in vehiculo.items() if v)
        )

        html = html.replace("{{ consumo_real }}", f"{consumo_real:.2f}")
        html = html.replace(
            "{{ consumo_declarado }}",
            f"{consumo_decl:.2f}" if consumo_decl else "No disponible"
        )
        html = html.replace(
            "{{ diferencia }}",
            f"{diferencia:.2f}" if diferencia is not None else "—"
        )

        html = html.replace("{{ estado }}", estado)
        html = html.replace("{{ estado_clase }}", estado_clase)
        html = html.replace("{{ comentario_estado }}", comentario)

        html = html.replace(
            "{{ metricas }}",
            "".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in metricas.items())
        )

        html = html.replace("{{ grafica_gasto }}", InformeEstadisticasPDF._file_url(graf_gasto))
        html = html.replace("{{ grafica_consumo }}", InformeEstadisticasPDF._file_url(graf_consumo))
        html = html.replace("{{ grafica_comparativa }}", InformeEstadisticasPDF._file_url(graf_comp))

        html = html.replace(
            "{{ explicacion_gasto }}",
            "Esta gráfica muestra el gasto diario realizado durante el periodo seleccionado."
        )
        html = html.replace(
            "{{ explicacion_consumo }}",
            "Representa el consumo real del vehículo calculado entre repostajes consecutivos."
        )
        html = html.replace(
            "{{ explicacion_comparativa }}",
            "Compara el consumo medio real con el consumo declarado por el fabricante."
        )

        html = html.replace("{{ conclusiones }}", comentario)
        html = html.replace(
            "{{ recomendaciones }}",
            "".join(f"<li>{r}</li>" for r in recomendaciones)
        )

        return html
