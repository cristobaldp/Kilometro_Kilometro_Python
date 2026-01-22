class MapaGasolinerasController:

    def __init__(self, service, app):
        self.service = service
        self.app = app
        self.view = None

    # -------------------------
    def set_view(self, view):
        self.view = view

    # -------------------------
    def buscar_localidad(self, localidad):
        datos = self.service.buscar_por_localidad(localidad)
        if datos and self.view:
            self.view.actualizar_marcadores(datos)

    # -------------------------
    def volver_menu(self):
        # Volver al menú principal
        self.app.mostrar_menu(self.app.usuario)
