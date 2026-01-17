from PySide6.QtWidgets import QWidget, QMessageBox, QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.figure import Figure
import matplotlib.dates as mdates
from datetime import datetime
import csv

from app.vista.estadisticas_ui import Ui_EstadisticasView
from app.repository.estadisticas_repository import EstadisticasRepository
from app.repository.vehiculo_repository import VehiculoRepository
from app.data.database import get_connection


class EstadisticasController:

    def __init__(self, app):
        self.app = app
        self.repo = EstadisticasRepository()
        self.vehiculo_repo = VehiculoRepository()

        self.vehiculo_id = self.app.usuario.get("vehiculo_activo_id")
        if not self.vehiculo_id:
            QMessageBox.warning(None, "Estadísticas", "Selecciona un vehículo activo primero")
            self.app.mostrar_menu(self.app.usuario)
            return

        self.widget = QWidget()
        self.ui = Ui_EstadisticasView()
        self.ui.setupUi(self.widget)

        self._init_graficas()

        self.datos_gasto = []
        self.datos_consumo = []
        self.repostajes = []
        self.metricas = {}

        self.ui.btnFiltrar.clicked.connect(self.actualizar)
        self.ui.btnExportPDF.clicked.connect(self.exportar_pdf)
        self.ui.btnExportCSV.clicked.connect(self.exportar_csv)
        self.ui.btnVolver.clicked.connect(self.volver_menu)

        self.actualizar()
        self.app._mostrar(self.widget)

    # =================================================
    # GRÁFICAS UI
    # =================================================
    def _init_graficas(self):
        self.fig_gasto = Figure(facecolor="#121212")
        self.ax_gasto = self.fig_gasto.add_subplot(111)
        self.canvas_gasto = FigureCanvas(self.fig_gasto)
        self.ui.layoutGasto.addWidget(self.canvas_gasto)

        self.fig_consumo = Figure(facecolor="#121212")
        self.ax_consumo = self.fig_consumo.add_subplot(111)
        self.canvas_consumo = FigureCanvas(self.fig_consumo)
        self.ui.layoutConsumo.addWidget(self.canvas_consumo)

    def _convertir_fechas(self, fechas):
        res = []
        for f in fechas:
            try:
                res.append(datetime.strptime(f, "%Y-%m-%d"))
            except:
                pass
        return res

    # =================================================
    # CONSUMO REAL
    # =================================================
    def _calcular_consumo_real(self):
        if len(self.repostajes) < 2:
            return 0.0

        litros = 0.0
        kms = 0
        for i in range(1, len(self.repostajes)):
            km = self.repostajes[i]["kilometros"] - self.repostajes[i - 1]["kilometros"]
            if km > 0:
                litros += self.repostajes[i - 1]["litros"]
                kms += km

        return (litros / kms) * 100 if kms else 0.0

    def _obtener_repostajes_periodo(self, mes, anio):
        con = get_connection()
        cur = con.cursor()
        cur.execute("""
            SELECT fecha, litros, kilometros
            FROM repostajes
            WHERE vehiculo_id = ?
              AND strftime('%Y', fecha) = ?
              AND strftime('%m', fecha) = ?
            ORDER BY kilometros
        """, (self.vehiculo_id, str(anio), f"{mes:02d}"))
        rows = cur.fetchall()
        con.close()

        return [{"fecha": r[0], "litros": r[1], "kilometros": r[2]} for r in rows]

    # =================================================
    def actualizar(self):
        mes = self.ui.comboMes.currentIndex() + 1
        anio = int(self.ui.comboAnio.currentText())

        self.datos_gasto = self.repo.gasto_diario(self.vehiculo_id, mes, anio)
        self.datos_consumo = self.repo.consumo_diario(self.vehiculo_id, mes, anio)
        self.metricas = self.repo.resumen_completo(self.vehiculo_id, mes, anio)
        self.repostajes = self._obtener_repostajes_periodo(mes, anio)

        self._dibujar_gasto()
        self._dibujar_consumo()

    # =================================================
    def _dibujar_gasto(self):
        self.ax_gasto.clear()
        if self.datos_gasto:
            fechas = self._convertir_fechas([f for f, _ in self.datos_gasto])
            valores = [v for _, v in self.datos_gasto]
            self.ax_gasto.plot(fechas, valores, marker="o", color="#00c853")
            self.ax_gasto.xaxis.set_major_formatter(mdates.DateFormatter('%d %b'))
            self.fig_gasto.autofmt_xdate()

        self.ax_gasto.set_title("Gasto (€)", color="white")
        self.ax_gasto.tick_params(colors="white")
        self.ax_gasto.grid(alpha=0.3)
        self.canvas_gasto.draw()

    def _dibujar_consumo(self):
        self.ax_consumo.clear()
        if self.datos_consumo:
            fechas = self._convertir_fechas([f for f, _ in self.datos_consumo])
            valores = [v for _, v in self.datos_consumo]
            self.ax_consumo.plot(fechas, valores, marker="o", color="#4fc3f7")
            self.ax_consumo.xaxis.set_major_formatter(mdates.DateFormatter('%d %b'))
            self.fig_consumo.autofmt_xdate()

        self.ax_consumo.set_title("Consumo (L/100km)", color="white")
        self.ax_consumo.tick_params(colors="white")
        self.ax_consumo.grid(alpha=0.3)
        self.canvas_consumo.draw()

    # =================================================
    # PDF PROFESIONAL NIVEL 10
    def exportar_pdf(self):

     if not self.repostajes:
        QMessageBox.warning(self.widget, "PDF", "No hay datos para generar el informe")
        return

     ruta, _ = QFileDialog.getSaveFileName(
        self.widget, "Exportar PDF", "", "PDF (*.pdf)"
     )
     if not ruta:
        return

     usuario = self.app.usuario
     vehiculo = next(
        v for v in self.vehiculo_repo.find_by_user(usuario["id"])
        if v[0] == self.vehiculo_id
     )

     consumo_real = self._calcular_consumo_real()
     consumo_decl = vehiculo[7]

     diferencia = (
        ((consumo_real - consumo_decl) / consumo_decl) * 100
        if consumo_decl else 0
     )

    # ================= ESTADO CORREGIDO =================
     if consumo_real <= consumo_decl:
        estado = "EFICIENTE"
        color = "green"
        comentario_estado = "El vehículo consume menos o igual de lo esperado."
        recomendaciones = [
            "Mantén este estilo de conducción.",
            "Realiza mantenimientos periódicos.",
            "Sigue controlando el consumo mensualmente."
        ]
     elif diferencia <= 10:
        estado = "NORMAL"
        color = "orange"
        comentario_estado = "El consumo es correcto, aunque existe margen de mejora."
        recomendaciones = [
            "Evita aceleraciones bruscas.",
            "Mantén la presión correcta de los neumáticos.",
            "Conduce a velocidad constante."
        ]
     else:
        estado = "INEFICIENTE"
        color = "red"
        comentario_estado = "El consumo es superior al esperado."
        recomendaciones = [
            "Reduce aceleraciones agresivas.",
            "Revisa presión y alineación de neumáticos.",
            "Evita sobrecargar el vehículo.",
            "Comprueba el mantenimiento general."
        ]

     fecha_gen = datetime.now().strftime("%d/%m/%Y %H:%M")

     with PdfPages(ruta) as pdf:

        # =================================================
        # PÁGINA 1 – PORTADA + DATOS
        # =================================================
        fig = Figure(figsize=(8.5, 11))
        ax = fig.add_subplot(111)
        ax.axis("off")

        y = 0.93
        dy = 0.035

        ax.text(0.5, y, "INFORME DE ESTADÍSTICAS DEL VEHÍCULO",
                ha="center", fontsize=22, fontweight="bold")
        y -= dy * 2

        ax.text(0.5, y, f"Generado el {fecha_gen}",
                ha="center", fontsize=10)
        y -= dy * 2

        ax.text(0.1, y, "DATOS DEL USUARIO", fontweight="bold"); y -= dy
        ax.text(0.1, y, f"Nombre: {usuario['nombre']} {usuario['apellidos']}"); y -= dy
        ax.text(0.1, y, f"Usuario: {usuario['username']}"); y -= dy
        ax.text(0.1, y, f"Email: {usuario['email']}"); y -= dy
        ax.text(0.1, y, f"Teléfono: {usuario['telefono']}"); y -= dy
        ax.text(0.1, y, f"Ciudad: {usuario['ciudad']}"); y -= dy * 1.5

        ax.text(0.1, y, "DATOS DEL VEHÍCULO", fontweight="bold"); y -= dy
        ax.text(0.1, y, f"Tipo: {vehiculo[1]}"); y -= dy
        ax.text(0.1, y, f"Marca / Modelo: {vehiculo[2]} {vehiculo[3]}"); y -= dy
        ax.text(0.1, y, f"Matrícula: {vehiculo[4]}"); y -= dy
        ax.text(0.1, y, f"Año: {vehiculo[5]}"); y -= dy
        ax.text(0.1, y, f"Combustible: {vehiculo[6]}"); y -= dy
        ax.text(0.1, y, f"Consumo declarado: {vehiculo[7]} L/100km")

        pdf.savefig(fig)

        # =================================================
        # PÁGINA 2 – RESUMEN EJECUTIVO + TABLA
        # =================================================
        fig = Figure(figsize=(8.5, 11))
        ax = fig.add_subplot(111)
        ax.axis("off")

        y = 0.92

        ax.text(0.5, y, "RESUMEN EJECUTIVO",
                ha="center", fontsize=18, fontweight="bold")
        y -= 0.07

        ax.text(0.5, y, f"Consumo real: {consumo_real:.2f} L/100km", ha="center"); y -= 0.04
        ax.text(0.5, y, f"Consumo declarado: {consumo_decl:.2f} L/100km", ha="center"); y -= 0.04
        ax.text(0.5, y, f"Diferencia: {diferencia:.2f} %", ha="center"); y -= 0.05

        ax.text(0.5, y, f"ESTADO: {estado}",
                ha="center", fontsize=14, fontweight="bold", color=color)
        y -= 0.05

        ax.text(0.5, y, comentario_estado, ha="center", style="italic")
        y -= 0.07

        ax.text(0.5, y, "TABLA RESUMEN DEL PERÍODO",
                ha="center", fontsize=16, fontweight="bold")
        y -= 0.06

        for k, v in [
            ("Gasto total (€)", f"{self.metricas['gasto_total']:.2f}"),
            ("Gasto medio por repostaje (€)", f"{self.metricas['gasto_promedio']:.2f}"),
            ("Litros totales", f"{self.metricas['total_litros']:.2f}"),
            ("Kilómetros totales", f"{self.metricas['total_km']:.2f}"),
            ("Precio medio €/L", f"{self.metricas['precio_litro']:.2f}"),
            ("Gasto por km (€)", f"{self.metricas['gasto_km']:.3f}"),
            ("Número de repostajes", self.metricas['num_repostajes']),
        ]:
            ax.text(0.3, y, k)
            ax.text(0.65, y, v)
            y -= 0.04

        pdf.savefig(fig)

        # =================================================
        # PÁGINA 3 – GRÁFICA GASTO
        # =================================================
        fig_g = Figure(figsize=(8.5, 6))
        axg = fig_g.add_subplot(111)
        fechas = self._convertir_fechas([f for f, _ in self.datos_gasto])
        valores = [v for _, v in self.datos_gasto]
        axg.plot(fechas, valores, marker="o")
        axg.set_title("Evolución del gasto (€)")
        axg.set_ylabel("Euros (€)")
        axg.grid(alpha=0.3)
        fig_g.autofmt_xdate()
        pdf.savefig(fig_g)

        # =================================================
        # PÁGINA 4 – GRÁFICA CONSUMO DIARIO
        # =================================================
        fig_cd = Figure(figsize=(8.5, 6))
        axcd = fig_cd.add_subplot(111)
        fechas = self._convertir_fechas([f for f, _ in self.datos_consumo])
        valores = [v for _, v in self.datos_consumo]
        axcd.plot(fechas, valores, marker="o", color="#4fc3f7")
        axcd.set_title("Evolución del consumo diario (L/100km)")
        axcd.set_ylabel("Litros / 100 km")
        axcd.grid(alpha=0.3)
        fig_cd.autofmt_xdate()
        pdf.savefig(fig_cd)

        # =================================================
        # PÁGINA 5 – CONSUMO REAL VS DECLARADO
        # =================================================
        fig = Figure(figsize=(8.5, 6))
        ax = fig.add_subplot(111)
        fechas = self._convertir_fechas([r["fecha"] for r in self.repostajes[1:]])
        ax.plot(fechas, [consumo_real] * len(fechas), label="Consumo real")
        ax.axhline(consumo_decl, color="red", linestyle="--",
                   label="Consumo declarado")
        ax.set_title("Consumo real vs consumo declarado")
        ax.set_ylabel("L/100km")
        ax.legend()
        ax.grid(alpha=0.3)
        fig.autofmt_xdate()
        pdf.savefig(fig)

        # =================================================
        # PÁGINA 6 – CONCLUSIONES Y RECOMENDACIONES
        # =================================================
        fig = Figure(figsize=(8.5, 11))
        ax = fig.add_subplot(111)
        ax.axis("off")

        y = 0.92
        ax.text(0.5, y, "CONCLUSIONES Y RECOMENDACIONES",
                ha="center", fontsize=18, fontweight="bold")
        y -= 0.08

        ax.text(
            0.1, y,
            "Las gráficas muestran cómo ha evolucionado el gasto y el consumo del vehículo "
            "durante el período seleccionado. Un consumo estable y cercano o inferior al "
            "declarado indica una conducción eficiente.",
            wrap=True
        )
        y -= 0.10

        ax.text(0.1, y, "RECOMENDACIONES:", fontweight="bold"); y -= 0.04
        for r in recomendaciones:
            ax.text(0.12, y, f"• {r}")
            y -= 0.035

        y -= 0.05
        ax.text(0.1, y, "GLOSARIO:", fontweight="bold"); y -= 0.04
        ax.text(0.12, y, "• Consumo real: Consumo calculado a partir de repostajes reales."); y -= 0.03
        ax.text(0.12, y, "• Consumo declarado: Consumo oficial del fabricante."); y -= 0.03
        ax.text(0.12, y, "• Gasto por km: Coste medio por kilómetro recorrido.")

        pdf.savefig(fig)

     QMessageBox.information(self.widget, "PDF", "Informe PDF generado correctamente")






    # =================================================
    def exportar_csv(self):
        ruta, _ = QFileDialog.getSaveFileName(self.widget, "Exportar CSV", "", "CSV (*.csv)")
        if not ruta:
            return

        with open(ruta, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(["Fecha", "Litros", "Kilómetros"])
            for r in self.repostajes:
                writer.writerow([r["fecha"], r["litros"], r["kilometros"]])

        QMessageBox.information(self.widget, "CSV", "CSV exportado correctamente")

    def volver_menu(self):
        self.app.mostrar_menu(self.app.usuario)
