from PySide6.QtWidgets import QWidget

# -------- VISTAS --------
from app.vista.login_ui import Ui_LoginView
from app.vista.registro_ui import Ui_RegistroView
from app.vista.menu_ui import Ui_MenuPrincipalView
from app.vista.add_vehiculo_ui import Ui_AddVehiculoView
from app.vista.add_repostaje_ui import Ui_AddRepostajeView
from app.vista.perfil_ui import Ui_PerfilView
from app.vista.ajustes_ui import Ui_AjustesView
from app.vista.estadisticas_ui import Ui_EstadisticasView

# -------- CONTROLADORES --------
from app.controlador.login_controller import LoginController
from app.controlador.registro_controller import RegistroController
from app.controlador.menu_controller import MenuController
from app.controlador.vehiculos_controller import VehiculosController
from app.controlador.add_vehiculo_controller import AddVehiculoController
from app.controlador.repostajes_controller import RepostajesController
from app.controlador.add_repostaje_controller import AddRepostajeController
from app.controlador.perfil_controller import PerfilController
from app.controlador.ajustes_controller import AjustesController
from app.controlador.estadisticas_controller import EstadisticasController


class AppController:

    def __init__(self):
        self.ventana_actual = None
        self.controller_actual = None
        self.usuario = None  # dict completo del usuario logueado

    # ==================================================
    # MÉTODO CENTRAL PARA MOSTRAR VENTANAS
    # ==================================================
    def _mostrar(self, widget: QWidget):
        if self.ventana_actual:
            self.ventana_actual.close()

        self.ventana_actual = widget
        self.ventana_actual.show()

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
    # AJUSTES
    # ==================================================
    def mostrar_ajustes(self):
        widget = QWidget()
        ui = Ui_AjustesView()
        ui.setupUi(widget)

        self.controller_actual = AjustesController(widget, ui, self)
        self._mostrar(widget)

    # ==================================================
    # ESTADÍSTICAS
    # ==================================================
    def mostrar_estadisticas(self):
     self.controller_actual = EstadisticasController(self)
