from PySide6.QtWidgets import QWidget
from app.vista.estadisticas_ui import Ui_EstadisticasView
from app.repository.estadisticas_repository import EstadisticasRepository

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from datetime import datetime


class EstadisticasController:

    def __init__(self, app):
        self.app = app
        self.repo = EstadisticasRepository()

        self.vehiculo_id = self.app.usuario.get("vehiculo_activo_id")
        if not self.vehiculo_id:
            self.app.mostrar_menu(self.app.usuario)
            return

        # UI
        self.widget = QWidget()
        self.ui = Ui_EstadisticasView()
        self.ui.setupUi(self.widget)

        # Conexiones
        self.ui.btnFiltrar.clicked.connect(self.actualizar_graficas)
        self.ui.btnVolver.clicked.connect(self.volver_menu)

        # Cargar filtros
        self._cargar_filtros()

        # Inicializar gráficas
        self._init_graficas()

        # Primera carga
        self.actualizar_graficas()

        self.app._mostrar(self.widget)

    # -------------------------------------------------
    # FILTROS
    # -------------------------------------------------
    def _cargar_filtros(self):
        # Meses
        self.ui.comboMes.clear()
        self.meses = [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ]
        self.ui.comboMes.addItems(self.meses)

        # Años
        self.ui.comboAnio.clear()
        anio_actual = datetime.now().year
        for a in range(anio_actual, 2019, -1):
            self.ui.comboAnio.addItem(str(a))

    # -------------------------------------------------
    # GRÁFICAS
    # -------------------------------------------------
    def _init_graficas(self):
        # GASTO
        self.fig_gasto = Figure(figsize=(5, 3))
        self.canvas_gasto = FigureCanvas(self.fig_gasto)
        self.ax_gasto = self.fig_gasto.add_subplot(111)
        self.ui.layoutGasto.addWidget(self.canvas_gasto)

        # CONSUMO
        self.fig_consumo = Figure(figsize=(5, 3))
        self.canvas_consumo = FigureCanvas(self.fig_consumo)
        self.ax_consumo = self.fig_consumo.add_subplot(111)
        self.ui.layoutConsumo.addWidget(self.canvas_consumo)

    # -------------------------------------------------
    # ACTUALIZAR
    # -------------------------------------------------
    def actualizar_graficas(self):
        if not self.ui.comboAnio.currentText():
            return

        mes = self.ui.comboMes.currentIndex() + 1
        anio = int(self.ui.comboAnio.currentText())

        print(f"Filtrar estadísticas: {self.meses[mes-1]} {anio}")

        self._dibujar_gasto(mes, anio)
        self._dibujar_consumo(mes, anio)

    # -------------------------------------------------
    # GASTO
    # -------------------------------------------------
    def _dibujar_gasto(self, mes, anio):
        datos = self.repo.gasto_por_mes_y_anio(
            self.vehiculo_id, mes, anio
        )

        self.ax_gasto.clear()

        if not datos:
            self.ax_gasto.set_title("Sin datos de gasto")
            self.canvas_gasto.draw()
            return

        fechas = [f[0] for f in datos]
        gastos = [f[1] for f in datos]

        self.ax_gasto.bar(fechas, gastos)
        self.ax_gasto.set_title("Gasto (€)")
        self.ax_gasto.set_ylabel("€")
        self.ax_gasto.tick_params(axis="x", rotation=45)

        self.fig_gasto.tight_layout()
        self.canvas_gasto.draw()

    # -------------------------------------------------
    # CONSUMO
    # -------------------------------------------------
    def _dibujar_consumo(self, mes, anio):
        datos = self.repo.consumo_por_mes_y_anio(
            self.vehiculo_id, mes, anio
        )

        self.ax_consumo.clear()

        if not datos:
            self.ax_consumo.set_title("Sin datos de consumo")
            self.canvas_consumo.draw()
            return

        fechas = [f[0] for f in datos]
        consumos = [f[3] for f in datos]

        self.ax_consumo.plot(fechas, consumos, marker="o")
        self.ax_consumo.set_title("Consumo medio (L/100km)")
        self.ax_consumo.set_ylabel("L/100km")
        self.ax_consumo.tick_params(axis="x", rotation=45)

        self.fig_consumo.tight_layout()
        self.canvas_consumo.draw()

    # -------------------------------------------------
    def volver_menu(self):
        self.app.mostrar_menu(self.app.usuario)
