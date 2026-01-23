from pathlib import Path
from datetime import datetime
from weasyprint import HTML, CSS


class InformeRepostajesPDF:
    """
    Genera un informe PDF profesional de repostajes.
    El consumo medio se calcula como:
    (litros totales / km recorridos reales) * 100
    """

    # ==================================================
    @staticmethod
    def generar(
        output_path: str,
        usuario: dict,
        vehiculo: dict,
        repostajes: list,
        periodo: str = "Todos los repostajes"
    ):
        """
        Genera el PDF del listado de repostajes.
        repostajes: lista de tuplas
        (id, fecha, litros, precio, kilometros)
        """

        # =============================
        # CARGA DE PLANTILLAS
        base_path = Path(__file__).parent
        html_template = (
            base_path / "templates" / "informe_repostajes.html"
        ).read_text(encoding="utf-8")
        css_path = base_path / "templates" / "informe_repostajes.css"

        # =============================
        # DATOS GENERALES
        fecha_generacion = datetime.now().strftime("%d/%m/%Y")

        usuario_html = InformeRepostajesPDF._dict_to_html(usuario)
        vehiculo_html = InformeRepostajesPDF._dict_to_html(vehiculo)

        filas_html, resumen_html = (
            InformeRepostajesPDF._procesar_repostajes(repostajes)
        )

        # =============================
        # RELLENAR HTML
        html_final = (
            html_template
            .replace("{{ fecha_generacion }}", fecha_generacion)
            .replace("{{ periodo }}", periodo)
            .replace("{{ usuario }}", usuario_html)
            .replace("{{ vehiculo }}", vehiculo_html)
            .replace("{{ filas_repostajes }}", filas_html)
            .replace("{{ resumen }}", resumen_html)
        )

        # =============================
        # GENERAR PDF
        HTML(string=html_final, base_url=base_path).write_pdf(
            output_path,
            stylesheets=[CSS(filename=str(css_path))]
        )

    # ==================================================
    @staticmethod
    def _dict_to_html(data: dict) -> str:
        """
        Convierte un diccionario en HTML con saltos de línea
        """
        return "<br>".join(
            f"<strong>{k}:</strong> {v}"
            for k, v in data.items()
            if v is not None
        )

    # ==================================================
    @staticmethod
    def _procesar_repostajes(repostajes: list):
     """
     Genera filas HTML y resumen.
    Consumo medio calculado EXACTAMENTE igual que en Android.
     """

     filas = ""
     total_precio = 0.0

     litros_totales = 0.0
     km_totales = 0.0

    # repostajes = [(id, fecha, litros, precio, km), ...]
     repostajes_ordenados = sorted(repostajes, key=lambda r: r[4])

     for _, fecha, litros, precio, km in repostajes_ordenados:
        filas += f"""
            <tr>
                <td>{fecha}</td>
                <td>{litros:.2f}</td>
                <td>{precio:.2f} €</td>
                <td>{km} km</td>
            </tr>
        """
        total_precio += precio

    # =============================
    # CONSUMO MEDIO (TRAMO A TRAMO)
     for i in range(1, len(repostajes_ordenados)):
        ant = repostajes_ordenados[i - 1]
        act = repostajes_ordenados[i]

        km = act[4] - ant[4]

        # mismo filtro que Android
        if 1 <= km <= 1500:
            litros_totales += ant[2]
            km_totales += km

     if km_totales > 0:
        consumo_medio = f"{(litros_totales / km_totales) * 100:.2f} L/100km"
     else:
        consumo_medio = "No disponible"

    # =============================
    # RESUMEN
     resumen = f"""
        <strong>Nº de repostajes:</strong> {len(repostajes_ordenados)}<br>
        <strong>Total gastado:</strong> {total_precio:.2f} €<br>
        <strong>Consumo medio:</strong> {consumo_medio}
     """

     return filas, resumen
