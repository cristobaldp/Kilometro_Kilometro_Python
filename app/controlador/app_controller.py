from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt

# -------- VISTAS (UI) --------
from app.vista.login_ui import Ui_LoginView
from app.vista.registro_ui import Ui_RegistroView
from app.vista.menu_ui import Ui_MenuPrincipalView
from app.vista.add_vehiculo_ui import Ui_AddVehiculoView
from app.vista.add_repostaje_ui import Ui_AddRepostajeView
from app.vista.perfil_ui import Ui_PerfilView
from app.vista.estadisticas_ui import Ui_EstadisticasView
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

# -------- STATUS WIDGET (WIDGET REUTILIZABLE) --------
from app.controlador.status_widget_controller import StatusWidgetController

# -------- MAPA --------
from app.repository.gasolineras_api_repository import GasolinerasApiRepository
from app.service.gasolineras_service import GasolinerasService
import shiboken6


class AppController:

    def __init__(self):
        self.ventana_actual: QWidget | None = None
        self.controller_actual = None
        self.usuario = None
        self.status_widget: StatusWidgetController | None = None

    # ==================================================
    # MOSTRAR VENTANA
    # ==================================================
    def _mostrar(self, widget: QWidget):
        if self.ventana_actual:
            self.ventana_actual.close()

        self.ventana_actual = widget
        self.ventana_actual.show()

    # ==================================================
    # STATUS WIDGET (OVERLAY)
    # ==================================================
    def mostrar_status(self, status: str, mensaje: str = ""):
     if not self.ventana_actual:
        return
 
     self.ocultar_status()

     self.status_widget = StatusWidgetController(self.ventana_actual)
 
    #  CLAVE ABSOLUTA
     self.status_widget.setAttribute(Qt.WA_StyledBackground, True)
     self.status_widget.setAttribute(Qt.WA_NoSystemBackground, False)
     self.status_widget.setAttribute(Qt.WA_TransparentForMouseEvents, False)

    #  OCUPA TODA LA VENTANA
     self.status_widget.setGeometry(self.ventana_actual.rect())

    #  CONFIGURAR CONTENIDO
     self.status_widget.set_status(
         status=status,
        message=mensaje
     )

    #  ORDEN DE PINTADO (ESTO ES LO QUE TE FALTABA)
     self.status_widget.show()
     self.status_widget.raise_()
     self.status_widget.repaint()


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

    #  mostrar overlay
     self.mostrar_status(
        status="loading",
        mensaje="⛽ Cargando mapa de gasolineras...\n\nObteniendo precios actualizados"
     )

    # crear mapa
     repo = GasolinerasApiRepository()
     service = GasolinerasService(repo)
     mapa_controller = MapaGasolinerasController(service, self)

     widget = MapaGasolinerasView(mapa_controller)
     mapa_controller.set_view(widget)

    #  cuando el mapa termine → ocultar overlay
     mapa_controller.carga_finalizada.connect(self.ocultar_status)

     self.controller_actual = mapa_controller
     self._mostrar(widget)
     
    def ocultar_status(self):
     if self.status_widget is None:
        return

    #  comprobar si Qt ya lo destruyó
     if shiboken6.isValid(self.status_widget):
        self.status_widget.hide()
        self.status_widget.deleteLater()

     self.status_widget = None



    # ==================================================
    # ESTADÍSTICAS
    # ==================================================
    def mostrar_estadisticas(self):
        self.controller_actual = EstadisticasController(self)
