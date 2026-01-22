from pathlib import Path
from datetime import datetime
from weasyprint import HTML, CSS


class InformeRepostajesPDF:

    @staticmethod
    def generar(
        output_path: str,
        usuario: dict,
        vehiculo: dict,
        repostajes: list,
        periodo: str = "Todos los repostajes"
    ):
        """
        Genera un informe PDF profesional de repostajes.
        """

        # =============================
        # CARGA DE PLANTILLAS
        base_path = Path(__file__).parent
        html_template = (base_path / "templates" / "informe_repostajes.html") \
            .read_text(encoding="utf-8")
        css_path = base_path / "templates" / "informe_repostajes.css"

        # =============================
        # PREPARAR DATOS
        fecha_generacion = datetime.now().strftime("%d/%m/%Y")

        usuario_html = InformeRepostajesPDF._dict_to_html(usuario)
        vehiculo_html = InformeRepostajesPDF._dict_to_html(vehiculo)

        filas_html, resumen_html = \
            InformeRepostajesPDF._procesar_repostajes(repostajes)

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

    # ------------------------------------------------
    @staticmethod
    def _dict_to_html(data: dict) -> str:
        """
        Convierte un diccionario en líneas HTML <br>
        """
        return "<br>".join(
            f"<strong>{k}:</strong> {v}" for k, v in data.items()
        )

    # ------------------------------------------------
    @staticmethod
    def _procesar_repostajes(repostajes: list):
        """
        Genera filas de la tabla y resumen con consumo medio.
        """
        filas = ""
        total_litros = 0.0
        total_precio = 0.0

        kms = []

        for _, fecha, litros, precio, km in repostajes:
            filas += f"""
                <tr>
                    <td>{fecha}</td>
                    <td>{litros:.2f}</td>
                    <td>{precio:.2f}</td>
                    <td>{km}</td>
                </tr>
            """
            total_litros += litros
            total_precio += precio
            kms.append(km)

        # =============================
        # CÁLCULOS
        num_repostajes = len(repostajes)
        media_precio = (
            total_precio / num_repostajes
            if num_repostajes > 0 else 0
        )

        consumo_medio = "No disponible"
        if len(kms) >= 2:
            km_recorridos = max(kms) - min(kms)
            if km_recorridos > 0:
                consumo_medio = (
                    f"{(total_litros / km_recorridos) * 100:.2f} L/100km"
                )

        # =============================
        # RESUMEN HTML
        resumen = f"""
            Nº de repostajes: {num_repostajes}<br>
            Total litros: {total_litros:.2f} L<br>
            Total gastado: {total_precio:.2f} €<br>
            Media por repostaje: {media_precio:.2f} €<br>
            Consumo medio: {consumo_medio}
        """

        return filas, resumen
