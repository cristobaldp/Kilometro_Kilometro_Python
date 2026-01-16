from PySide6.QtWidgets import QWidget, QMessageBox, QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.figure import Figure
import matplotlib.dates as mdates
from datetime import datetime
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
    # CONVERTIR FECHAS A DATETIME
    # =================================================
    def _convertir_fechas(self, fechas_str):
        """Convierte strings de fecha a objetos datetime"""
        fechas_dt = []
        for fecha in fechas_str:
            if isinstance(fecha, str):
                # Intenta varios formatos comunes
                for fmt in ['%Y-%m-%d', '%d/%m/%Y', '%Y/%m/%d']:
                    try:
                        fechas_dt.append(datetime.strptime(fecha, fmt))
                        break
                    except ValueError:
                        continue
            elif isinstance(fecha, datetime):
                fechas_dt.append(fecha)
        return fechas_dt

    # =================================================
    # CONFIGURAR FORMATO DE FECHAS
    # =================================================
    def _configurar_formato_fechas(self, ax, fechas):
        """Configura el formato de las fechas en el eje X"""
        if not fechas:
            return
        
        num_fechas = len(fechas)
        
        # Formato según cantidad de datos
        if num_fechas <= 7:
            # Pocos datos: mostrar todas las fechas con día y mes
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%d %b'))
            ax.xaxis.set_major_locator(mdates.DayLocator())
        elif num_fechas <= 15:
            # Datos medios: mostrar cada 2-3 días
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%d %b'))
            ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))
        else:
            # Muchos datos: mostrar solo algunos días
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%d %b'))
            ax.xaxis.set_major_locator(mdates.DayLocator(interval=5))
        
        # Rotar las etiquetas para mejor legibilidad
        ax.tick_params(axis='x', rotation=45)
        
        # Ajustar para que no se corten las etiquetas
        ax.figure.autofmt_xdate()

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
            fechas_str = [d[0] for d in self.datos_gasto]
            gastos = [d[1] for d in self.datos_gasto]
            
            # Convertir fechas a datetime
            fechas_dt = self._convertir_fechas(fechas_str)
            
            if fechas_dt:
                self.ax_gasto.plot(fechas_dt, gastos, marker="o", color="#00c853", linewidth=2, markersize=6)
                self._configurar_formato_fechas(self.ax_gasto, fechas_dt)

        self.ax_gasto.set_title("Gasto (€)", color="white", fontsize=14, pad=15)
        self.ax_gasto.set_ylabel("Euros (€)", color="white")
        self.ax_gasto.tick_params(colors="white")
        self.ax_gasto.grid(True, alpha=0.3, linestyle='--')
        self.ax_gasto.set_facecolor('#1a1a1a')
        self.fig_gasto.tight_layout()
        self.canvas_gasto.draw()

        # ---------- CONSUMO ----------
        self.ax_consumo.clear()
        if self.datos_consumo:
            fechas_str = [d[0] for d in self.datos_consumo]
            consumos = [d[1] for d in self.datos_consumo]
            
            # Convertir fechas a datetime
            fechas_dt = self._convertir_fechas(fechas_str)
            
            if fechas_dt:
                self.ax_consumo.plot(fechas_dt, consumos, marker="o", color="#4fc3f7", linewidth=2, markersize=6)
                self._configurar_formato_fechas(self.ax_consumo, fechas_dt)

        self.ax_consumo.set_title("Consumo (L/100km)", color="white", fontsize=14, pad=15)
        self.ax_consumo.set_ylabel("Litros/100km", color="white")
        self.ax_consumo.tick_params(colors="white")
        self.ax_consumo.grid(True, alpha=0.3, linestyle='--')
        self.ax_consumo.set_facecolor('#1a1a1a')
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
                fechas_str = [d[0] for d in self.datos_gasto]
                gastos = [d[1] for d in self.datos_gasto]
                fechas_dt = self._convertir_fechas(fechas_str)
                
                if fechas_dt:
                    ax1.plot(fechas_dt, gastos, marker="o", color="#00c853", linewidth=2)
                    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d %b'))
                    if len(fechas_dt) > 15:
                        ax1.xaxis.set_major_locator(mdates.DayLocator(interval=3))
                    fig.autofmt_xdate()
                    
            ax1.set_title("Gasto (€)", fontsize=12, pad=10)
            ax1.set_ylabel("Euros (€)")
            ax1.grid(True, alpha=0.3)

            # CONSUMO
            ax2 = fig.add_subplot(212)
            if self.datos_consumo:
                fechas_str = [d[0] for d in self.datos_consumo]
                consumos = [d[1] for d in self.datos_consumo]
                fechas_dt = self._convertir_fechas(fechas_str)
                
                if fechas_dt:
                    ax2.plot(fechas_dt, consumos, marker="o", color="#4fc3f7", linewidth=2)
                    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%d %b'))
                    if len(fechas_dt) > 15:
                        ax2.xaxis.set_major_locator(mdates.DayLocator(interval=3))
                        
            ax2.set_title("Consumo (L/100km)", fontsize=12, pad=10)
            ax2.set_ylabel("Litros/100km")
            ax2.grid(True, alpha=0.3)

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