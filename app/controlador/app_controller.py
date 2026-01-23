from PySide6.QtWidgets import QWidget, QProgressDialog
from PySide6.QtCore import Qt

# -------- VISTAS (UI) --------
from app.vista.login_ui import Ui_LoginView
from app.vista.registro_ui import Ui_RegistroView
from app.vista.menu_ui import Ui_MenuPrincipalView
from app.vista.add_vehiculo_ui import Ui_AddVehiculoView
from app.vista.add_repostaje_ui import Ui_AddRepostajeView
from app.vista.perfil_ui import Ui_PerfilView
from app.vista.estadisticas_ui import Ui_EstadisticasView

# 👉 VISTA REAL DEL MAPA
from app.vista.mapa_gasolineras_view import MapaGasolinerasView

# -------- CONTROLADORES --------
from app.controlador.login_controller import LoginController
from app.controlador.registro_controller import RegistroController
from app.controlador.menu_controller import MenuController
from app.controlador.vehiculos_controller import VehiculosController
from app.controlador.add_vehiculo_controller import AddVehiculoController
from app.controlador.repostajes_controller import RepostajesController
from app.controlador.add_repostaje_controller import AddRepostajeController
from app.controlador.perfil_controller import PerfilController
from app.controlador.estadisticas_controller import EstadisticasController
from app.controlador.mapa_gasolineras_controller import MapaGasolinerasController

# -------- MAPA (SERVICE + REPO) --------
from app.repository.gasolineras_api_repository import GasolinerasApiRepository
from app.service.gasolineras_service import GasolinerasService


class AppController:

    def __init__(self):
        self.ventana_actual = None
        self.controller_actual = None
        self.usuario = None

    # ==================================================
    # MÉTODO CENTRAL PARA MOSTRAR VENTANAS
    # ==================================================
    def _mostrar(self, widget: QWidget):
        if self.ventana_actual:
            self.ventana_actual.close()

        self.ventana_actual = widget
        self.ventana_actual.show()

    # ==================================================
    # LOADING DIALOG BONITO 🔥
    # ==================================================
    def _crear_loading_dialog(self, texto: str):
        loading = QProgressDialog(
            texto,
            None,
            0,
            0,
            self.ventana_actual
        )

        loading.setWindowTitle("Cargando")
        loading.setCancelButton(None)
        loading.setWindowModality(Qt.ApplicationModal)
        loading.setMinimumWidth(420)
        loading.setMinimumHeight(140)

        loading.setStyleSheet("""
            QProgressDialog {
                background-color: #121212;
                color: white;
                border-radius: 12px;
                padding: 16px;
                font-size: 14px;
            }

            QLabel {
                color: #e0e0e0;
                font-size: 14px;
            }

            QProgressBar {
                background-color: #1e1e1e;
                border-radius: 8px;
                height: 14px;
                text-align: center;
                color: transparent;
            }

            QProgressBar::chunk {
                background-color: #00c853;
                border-radius: 8px;
            }
        """)

        loading.show()
        loading.repaint()
        return loading

    # ==================================================
    # LOGIN
    # ==================================================
    def mostrar_login(self):
        widget = QWidget()
        ui = Ui_LoginView()
        ui.setupUi(widget)

        self.controller_actual = LoginController(widget, ui, self)
        self._mostrar(widget)

    # ==================================================
    # REGISTRO
    # ==================================================
    def mostrar_registro(self):
        widget = QWidget()
        ui = Ui_RegistroView()
        ui.setupUi(widget)

        self.controller_actual = RegistroController(widget, ui, self)
        self._mostrar(widget)

    # ==================================================
    # MENÚ PRINCIPAL
    # ==================================================
    def mostrar_menu(self, usuario: dict):
        self.usuario = usuario

        widget = QWidget()
        ui = Ui_MenuPrincipalView()
        ui.setupUi(widget)

        self.controller_actual = MenuController(widget, ui, self)
        self._mostrar(widget)

    # ==================================================
    # VEHÍCULOS
    # ==================================================
    def mostrar_vehiculos(self):
        self.controller_actual = VehiculosController(self)

    def mostrar_add_vehiculo(self):
        widget = QWidget()
        ui = Ui_AddVehiculoView()
        ui.setupUi(widget)

        self.controller_actual = AddVehiculoController(widget, ui, self)
        self._mostrar(widget)

    # ==================================================
    # REPOSTAJES
    # ==================================================
    def mostrar_repostajes(self):
        self.controller_actual = RepostajesController(self)

    def mostrar_add_repostaje(self):
        widget = QWidget()
        ui = Ui_AddRepostajeView()
        ui.setupUi(widget)

        self.controller_actual = AddRepostajeController(widget, ui, self)
        self._mostrar(widget)

    # ==================================================
    # PERFIL
    # ==================================================
    def mostrar_perfil(self):
        widget = QWidget()
        ui = Ui_PerfilView()
        ui.setupUi(widget)

        self.controller_actual = PerfilController(widget, ui, self)
        self._mostrar(widget)

    # ==================================================
    # MAPA DE GASOLINERAS
    # ==================================================
    def mostrar_mapa_gasolineras(self):

        # ---------- LOADING BONITO ----------
        loading = self._crear_loading_dialog(
            "⛽ Cargando mapa de gasolineras...\n\nObteniendo precios actualizados"
        )

        # ---------- CREACIÓN DEL MAPA ----------
        repo = GasolinerasApiRepository()
        service = GasolinerasService(repo)
        mapa_controller = MapaGasolinerasController(service, self)

        widget = MapaGasolinerasView(mapa_controller)
        mapa_controller.set_view(widget)

        self.controller_actual = mapa_controller
        self._mostrar(widget)

        # ---------- CERRAR LOADING ----------
        loading.close()

    # ==================================================
    # ESTADÍSTICAS
    # ==================================================
    def mostrar_estadisticas(self):
        self.controller_actual = EstadisticasController(self)
