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

        # ---------- Vehículo activo ----------
        self.vehiculo_id = self.app.usuario.get("vehiculo_activo_id")
        if not self.vehiculo_id:
            QMessageBox.warning(
                None,
                "Estadísticas",
                "Selecciona un vehículo activo primero"
            )
            self.app.mostrar_menu(self.app.usuario)
            return

        # ---------- UI ----------
        self.widget = QWidget()
        self.ui = Ui_EstadisticasView()
        self.ui.setupUi(self.widget)

        # ---------- Gráficas ----------
        self._init_graficas()

        # ---------- Datos actuales ----------
        self.datos_gasto = []
        self.datos_consumo = []

        # ---------- Conexiones ----------
        self.ui.btnFiltrar.clicked.connect(self.actualizar_graficas)
        self.ui.btnExportPDF.clicked.connect(self.exportar_pdf)
        self.ui.btnExportCSV.clicked.connect(self.exportar_csv)
        self.ui.btnVolver.clicked.connect(self.volver_menu)
     

        # Primera carga
        self.actualizar_graficas()

        self.app._mostrar(self.widget)

    # =================================================
    # INICIALIZAR GRÁFICAS
    # =================================================
    def _init_graficas(self):
        # ----- GASTO -----
        self.fig_gasto = Figure(facecolor="#121212")
        self.ax_gasto = self.fig_gasto.add_subplot(111)
        self.canvas_gasto = FigureCanvas(self.fig_gasto)
        self.ui.layoutGasto.addWidget(self.canvas_gasto)

        # ----- CONSUMO -----
        self.fig_consumo = Figure(facecolor="#121212")
        self.ax_consumo = self.fig_consumo.add_subplot(111)
        self.canvas_consumo = FigureCanvas(self.fig_consumo)
        self.ui.layoutConsumo.addWidget(self.canvas_consumo)

    # =================================================
    # ACTUALIZAR GRÁFICAS
    # =================================================
    def actualizar_graficas(self):
        mes = self.ui.comboMes.currentIndex() + 1
        texto_anio = self.ui.comboAnio.currentText()

        if not texto_anio.isdigit():
            QMessageBox.warning(self.widget, "Error", "Selecciona un año válido")
            return

        anio = int(texto_anio)

        # ---------- DATOS ----------
        self.datos_gasto = self.repo.gasto_diario(
            self.vehiculo_id, mes, anio
        )
        self.datos_consumo = self.repo.consumo_diario(
            self.vehiculo_id, mes, anio
        )

        # ---------- GASTO ----------
        self.ax_gasto.clear()
        if self.datos_gasto:
            fechas = [d[0] for d in self.datos_gasto]
            gastos = [d[1] for d in self.datos_gasto]
            self.ax_gasto.plot(fechas, gastos, marker="o", color="#00c853")

        self.ax_gasto.set_title("Gasto (€)", color="white")
        self.ax_gasto.tick_params(colors="white")
        self.ax_gasto.grid(True, alpha=0.3)
        self.fig_gasto.tight_layout()
        self.canvas_gasto.draw()

        # ---------- CONSUMO ----------
        self.ax_consumo.clear()
        if self.datos_consumo:
            fechas = [d[0] for d in self.datos_consumo]
            consumos = [d[1] for d in self.datos_consumo]
            self.ax_consumo.plot(fechas, consumos, marker="o", color="#4fc3f7")

        self.ax_consumo.set_title("Consumo (L/100km)", color="white")
        self.ax_consumo.tick_params(colors="white")
        self.ax_consumo.grid(True, alpha=0.3)
        self.fig_consumo.tight_layout()
        self.canvas_consumo.draw()

    # =================================================
    # EXPORTAR PDF (AMBAS GRÁFICAS)
    # =================================================
    def exportar_pdf(self):
        if not self.datos_gasto and not self.datos_consumo:
            QMessageBox.warning(self.widget, "Exportar", "No hay datos para exportar")
            return

        ruta, _ = QFileDialog.getSaveFileName(
            self.widget, "Exportar estadísticas", "", "PDF (*.pdf)"
        )
        if not ruta:
            return

        with PdfPages(ruta) as pdf:
            fig = Figure(figsize=(10, 8))

            # GASTO
            ax1 = fig.add_subplot(211)
            if self.datos_gasto:
                ax1.plot(
                    [d[0] for d in self.datos_gasto],
                    [d[1] for d in self.datos_gasto],
                    marker="o",
                    color="#00c853"
                )
            ax1.set_title("Gasto (€)")
            ax1.grid(True)

            # CONSUMO
            ax2 = fig.add_subplot(212)
            if self.datos_consumo:
                ax2.plot(
                    [d[0] for d in self.datos_consumo],
                    [d[1] for d in self.datos_consumo],
                    marker="o",
                    color="#4fc3f7"
                )
            ax2.set_title("Consumo (L/100km)")
            ax2.grid(True)

            fig.tight_layout()
            pdf.savefig(fig)

        QMessageBox.information(self.widget, "PDF", "PDF exportado correctamente")

    # =================================================
    # EXPORTAR CSV
    # =================================================
    def exportar_csv(self):
        if not self.datos_gasto and not self.datos_consumo:
            QMessageBox.warning(self.widget, "Exportar", "No hay datos para exportar")
            return

        ruta, _ = QFileDialog.getSaveFileName(
            self.widget, "Exportar estadísticas", "", "CSV (*.csv)"
        )
        if not ruta:
            return

        with open(ruta, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=";")

            writer.writerow(["GASTO"])
            writer.writerow(["Fecha", "Gasto (€)"])
            for fecha, gasto in self.datos_gasto:
                writer.writerow([fecha, gasto])

            writer.writerow([])
            writer.writerow(["CONSUMO"])
            writer.writerow(["Fecha", "Consumo (L/100km)"])
            for fecha, consumo in self.datos_consumo:
                writer.writerow([fecha, round(consumo, 2)])

        QMessageBox.information(self.widget, "CSV", "CSV exportado correctamente")
        
        

    # =================================================
    def volver_menu(self):
        self.app.mostrar_menu(self.app.usuario)
