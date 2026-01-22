from PySide6.QtWidgets import QWidget, QMessageBox, QFileDialog
from PySide6.QtCore import Qt
from datetime import datetime
import csv

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.dates as mdates

from app.vista.estadisticas_ui import Ui_EstadisticasView
from app.repository.estadisticas_repository import EstadisticasRepository
from app.repository.vehiculo_repository import VehiculoRepository
from app.reports.informe_estadisticas_pdf import InformeEstadisticasPDF


class EstadisticasController:

    def __init__(self, app):
        self.app = app
        self.repo = EstadisticasRepository()
        self.vehiculo_repo = VehiculoRepository()

        self.vehiculo_id = self.app.usuario.get("vehiculo_activo_id")
        if not self.vehiculo_id:
            QMessageBox.warning(
                None,
                "Estadísticas",
                "Selecciona un vehículo activo primero"
            )
            self.app.mostrar_menu(self.app.usuario)
            return

        self.widget = QWidget()
        self.ui = Ui_EstadisticasView()
        self.ui.setupUi(self.widget)

        self._ajustar_combos()
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
    # GRÁFICAS
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
        return [
            datetime.strptime(f, "%Y-%m-%d")
            for f in fechas if f
        ]

    # =================================================
    # ACTUALIZAR DATOS
    # =================================================
    def actualizar(self):
        mes = self.ui.comboMes.currentIndex() + 1
        anio = int(self.ui.comboAnio.currentText())

        self.datos_gasto = self.repo.gasto_diario(
            self.vehiculo_id, mes, anio
        )

        self.repostajes = self.repo.repostajes_periodo(
            self.vehiculo_id, mes, anio
        )

        self.metricas = self.repo.resumen_completo(
            self.vehiculo_id, mes, anio
        )

        # ---- CONSUMO (MISMA LÓGICA QUE LA APP) ----
        self.datos_consumo = []
        if len(self.repostajes) > 1:
            for i in range(1, len(self.repostajes)):
                km = (
                    self.repostajes[i]["kilometros"]
                    - self.repostajes[i - 1]["kilometros"]
                )
                if km > 0:
                    consumo = (
                        self.repostajes[i - 1]["litros"] / km
                    ) * 100

                    self.datos_consumo.append((
                        self.repostajes[i]["fecha"],
                        consumo
                    ))

        self._dibujar_gasto()
        self._dibujar_consumo()

    # =================================================
    # DIBUJO GRÁFICAS
    # =================================================
    def _dibujar_gasto(self):
        self.ax_gasto.clear()

        if self.datos_gasto:
            fechas = self._convertir_fechas(
                [f for f, _ in self.datos_gasto]
            )
            valores = [v for _, v in self.datos_gasto]

            self.ax_gasto.plot(
                fechas,
                valores,
                marker="o",
                linewidth=2,
                color="#00c853"
            )

            self.ax_gasto.xaxis.set_major_formatter(
                mdates.DateFormatter('%d %b')
            )
            self.fig_gasto.autofmt_xdate()

        self.ax_gasto.set_title("Gasto mensual (€)", color="white")
        self.ax_gasto.tick_params(colors="white")
        self.ax_gasto.grid(alpha=0.3)
        self.canvas_gasto.draw()

    def _dibujar_consumo(self):
        self.ax_consumo.clear()

        if self.datos_consumo:
            fechas = self._convertir_fechas(
                [f for f, _ in self.datos_consumo]
            )
            valores = [v for _, v in self.datos_consumo]

            self.ax_consumo.plot(
                fechas,
                valores,
                marker="o",
                linewidth=2,
                color="#4fc3f7"
            )

            self.ax_consumo.xaxis.set_major_formatter(
                mdates.DateFormatter('%d %b')
            )
            self.fig_consumo.autofmt_xdate()

        self.ax_consumo.set_title(
            "Consumo mensual (L/100km)", color="white"
        )
        self.ax_consumo.tick_params(colors="white")
        self.ax_consumo.grid(alpha=0.3)
        self.canvas_consumo.draw()

    # =================================================
    # EXPORTAR PDF
    # =================================================
    def exportar_pdf(self):
        if not self.datos_gasto:
            QMessageBox.warning(
                self.widget,
                "PDF",
                "No hay datos para generar el informe"
            )
            return

        ruta, _ = QFileDialog.getSaveFileName(
            self.widget,
            "Exportar PDF",
            "",
            "PDF (*.pdf)"
        )
        if not ruta:
            return

        # -------- USUARIO --------
        usuario = {
            "Nombre": f"{self.app.usuario.get('nombre')} {self.app.usuario.get('apellidos')}",
            "Usuario": self.app.usuario.get("username"),
            "Email": self.app.usuario.get("email"),
            "Ciudad": self.app.usuario.get("ciudad")
        }

        # -------- VEHÍCULO --------
        vehiculo_raw = next(
            v for v in self.vehiculo_repo.find_by_user(
                self.app.usuario["id"]
            )
            if v[0] == self.vehiculo_id
        )

        vehiculo = {
            "Marca": vehiculo_raw[2],
            "Modelo": vehiculo_raw[3],
            "Matrícula": vehiculo_raw[4],
            "Combustible": vehiculo_raw[6],
            "Consumo declarado": f"{vehiculo_raw[7]} L/100km"
        }

        datos_graficas = {
            "gasto": self.datos_gasto,
            "consumo": self.datos_consumo
        }

        periodo = (
            f"{self.ui.comboMes.currentText()} "
            f"{self.ui.comboAnio.currentText()}"
        )

        InformeEstadisticasPDF.generar(
            ruta,
            usuario,
            vehiculo,
            datos_graficas,
            self.metricas,
            periodo
        )

        QMessageBox.information(
            self.widget,
            "PDF",
            "Informe generado correctamente"
        )

    # =================================================
    # EXPORTAR CSV
    # =================================================
    def exportar_csv(self):
        ruta, _ = QFileDialog.getSaveFileName(
            self.widget,
            "Exportar CSV",
            "",
            "CSV (*.csv)"
        )
        if not ruta:
            return

        with open(ruta, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(
                ["Fecha", "Litros", "Kilómetros", "Precio (€)"]
            )
            for r in self.repostajes:
                writer.writerow([
                    r["fecha"],
                    r["litros"],
                    r["kilometros"],
                    r["precio_total"]
                ])

        QMessageBox.information(
            self.widget,
            "CSV",
            "CSV exportado correctamente"
        )

    # =================================================
    def _ajustar_combos(self):
        for combo in (self.ui.comboMes, self.ui.comboAnio):
            combo.setMaxVisibleItems(5)
            combo.view().setVerticalScrollBarPolicy(
                Qt.ScrollBarAsNeeded
            )

    def volver_menu(self):
        self.app.mostrar_menu(self.app.usuario)
