from PySide6.QtCore import QObject, Signal


class MapaGasolinerasController(QObject):

    # 🔔 señal cuando el mapa ya está listo
    carga_finalizada = Signal()

    def __init__(self, service, app):
        super().__init__()
        self.service = service
        self.app = app
        self.view = None

    # -------------------------
    def set_view(self, view):
        self.view = view

      
        if hasattr(self.view, "map_loaded"):
            self.view.map_loaded.connect(self._on_mapa_listo)

    # -------------------------
    def _on_mapa_listo(self):
        # avisamos al AppController
        self.carga_finalizada.emit()

    # -------------------------
    def buscar_localidad(self, localidad):
        datos = self.service.buscar_por_localidad(localidad)
        if datos and self.view:
            self.view.actualizar_marcadores(datos)

    # -------------------------
    def volver_menu(self):
        self.app.mostrar_menu(self.app.usuario)
