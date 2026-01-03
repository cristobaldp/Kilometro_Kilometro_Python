from PySide6.QtWidgets import QWidget, QMessageBox, QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.figure import Figure
import csv

from app.vista.estadisticas_ui import Ui_EstadisticasView
from app.repository.estadisticas_repository import EstadisticasRepository


class EstadisticasController:

    def __init__(self, app):
        self.app = app
        self.repo = EstadisticasRepository()

        # 🔴 Necesita vehículo activo
        vehiculo_id = self.app.usuario.get("vehiculo_activo_id")
        if not vehiculo_id:
            QMessageBox.warning(
                None,
                "Estadísticas",
                "Selecciona un vehículo activo primero"
            )
            self.app.mostrar_menu(self.app.usuario)
            return

        self.vehiculo_id = vehiculo_id

        # UI
        self.widget = QWidget()
        self.ui = Ui_EstadisticasView()
        self.ui.setupUi(self.widget)

        # Inicializar gráficas
        self._init_graficas()

        # Conexiones
        self.ui.btnFiltrar.clicked.connect(self.actualizar_graficas)
        self.ui.btnExportPDF.clicked.connect(self.exportar_pdf)
        self.ui.btnExportCSV.clicked.connect(self.exportar_csv)
        self.ui.btnVolver.clicked.connect(self.volver_menu)

        # Primera carga
        self.actualizar_graficas()

        self.app._mostrar(self.widget)

    # -------------------------------------------------
    def _init_graficas(self):
        # ---------- GASTO ----------
        self.fig_gasto = Figure(facecolor="#121212")
        self.ax_gasto = self.fig_gasto.add_subplot(111)
        self.canvas_gasto = FigureCanvas(self.fig_gasto)
        self.ui.layoutGasto.addWidget(self.canvas_gasto)

        # ---------- CONSUMO ----------
        self.fig_consumo = Figure(facecolor="#121212")
        self.ax_consumo = self.fig_consumo.add_subplot(111)
        self.canvas_consumo = FigureCanvas(self.fig_consumo)
        self.ui.layoutConsumo.addWidget(self.canvas_consumo)

    # -------------------------------------------------
    def actualizar_graficas(self):
        # Mes
        mes = self.ui.comboMes.currentIndex() + 1

        # Año
        texto_anio = self.ui.comboAnio.currentText()
        if not texto_anio.isdigit():
            return
        anio = int(texto_anio)

        # =======================
        # GASTO
        # =======================
        self.datos_gasto = self.repo.gasto_diario(
            self.vehiculo_id, mes, anio
        )

        fechas_gasto = [d[0] for d in self.datos_gasto]
        gastos = [d[1] for d in self.datos_gasto]

        self.ax_gasto.clear()
        self.ax_gasto.plot(
            fechas_gasto,
            gastos,
            marker="o",
            color="#00c853"
        )
        self.ax_gasto.set_title("Gasto (€)", color="white")
        self.ax_gasto.tick_params(colors="white")
        self.ax_gasto.grid(True, alpha=0.3)

        self.fig_gasto.tight_layout()
        self.canvas_gasto.draw()

        # =======================
        # CONSUMO
        # =======================
        self.datos_consumo = self.repo.consumo_diario(
            self.vehiculo_id, mes, anio
        )

        fechas_consumo = [d[0] for d in self.datos_consumo]
        consumos = [d[1] for d in self.datos_consumo]

        self.ax_consumo.clear()
        self.ax_consumo.plot(
            fechas_consumo,
            consumos,
            marker="o",
            color="#4fc3f7"
        )
        self.ax_consumo.set_title("Consumo (L/100km)", color="white")
        self.ax_consumo.tick_params(colors="white")
        self.ax_consumo.grid(True, alpha=0.3)

        self.fig_consumo.tight_layout()
        self.canvas_consumo.draw()

    # -------------------------------------------------
    def exportar_pdf(self):
        ruta, _ = QFileDialog.getSaveFileName(
            self.widget,
            "Exportar estadísticas",
            "",
            "PDF (*.pdf)"
        )

        if not ruta:
            return

        with PdfPages(ruta) as pdf:
            fig = Figure(figsize=(10, 8), facecolor="white")

            # ---------- GASTO ----------
            ax1 = fig.add_subplot(211)
            for line in self.ax_gasto.get_lines():
                ax1.plot(
                    line.get_xdata(),
                    line.get_ydata(),
                    marker="o",
                    color="#00c853"
                )
            ax1.set_title("Gasto (€)")
            ax1.grid(True, alpha=0.3)

            # ---------- CONSUMO ----------
            ax2 = fig.add_subplot(212)
            for line in self.ax_consumo.get_lines():
                ax2.plot(
                    line.get_xdata(),
                    line.get_ydata(),
                    marker="o",
                    color="#4fc3f7"
                )
            ax2.set_title("Consumo (L/100km)")
            ax2.grid(True, alpha=0.3)

            fig.tight_layout()
            pdf.savefig(fig)

        QMessageBox.information(
            self.widget,
            "Exportación PDF",
            "Las estadísticas se han exportado correctamente."
        )

    # -------------------------------------------------
    def exportar_csv(self):
        ruta, _ = QFileDialog.getSaveFileName(
            self.widget,
            "Exportar estadísticas",
            "",
            "CSV (*.csv)"
        )

        if not ruta:
            return

        with open(ruta, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=";")

            # Cabecera
            writer.writerow(["ESTADÍSTICAS DE REPOSTAJES"])
            writer.writerow([])

            # -----------------
            # GASTO
            # -----------------
            writer.writerow(["GASTO"])
            writer.writerow(["Fecha", "Gasto (€)"])
            for fecha, gasto in self.datos_gasto:
                writer.writerow([fecha, gasto])

            writer.writerow([])

            # -----------------
            # CONSUMO
            # -----------------
            writer.writerow(["CONSUMO"])
            writer.writerow(["Fecha", "Consumo (L/100km)"])
            for fecha, consumo in self.datos_consumo:
                writer.writerow([fecha, round(consumo, 2)])

        QMessageBox.information(
            self.widget,
            "Exportación CSV",
            "El archivo CSV se ha generado correctamente."
        )

    # -------------------------------------------------
    def volver_menu(self):
        self.app.mostrar_menu(self.app.usuario)
