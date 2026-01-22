from PySide6.QtWidgets import QMessageBox


class MenuController:

    def __init__(self, widget, ui, app):
        self.widget = widget
        self.ui = ui
        self.app = app

        usuario = self.app.usuario
        username = usuario.get("username", "Usuario")
        self.ui.labelSubtitulo.setText(f"Bienvenido {username}")

        # =========================
        # CONEXIONES DEL MENÚ
        # =========================
        self.ui.btnVehiculos.clicked.connect(self.abrir_vehiculos)
        self.ui.btnRepostajes.clicked.connect(self.abrir_repostajes)
        self.ui.btnEstadisticas.clicked.connect(self.abrir_estadisticas)
        self.ui.btnPerfil.clicked.connect(self.abrir_perfil)

        # 🔥 MAPA DE GASOLINERAS (ANTES AJUSTES)
        self.ui.btnMapa.clicked.connect(self.abrir_mapa)

        self.ui.btnLogout.clicked.connect(self.logout)

    # -------------------------
    def abrir_vehiculos(self):
        self.app.mostrar_vehiculos()

    # -------------------------
    def abrir_repostajes(self):
        if not self._hay_vehiculo_activo():
            return
        self.app.mostrar_repostajes()

    # -------------------------
    def abrir_estadisticas(self):
        if not self._hay_vehiculo_activo():
            return
        self.app.mostrar_estadisticas()

    # -------------------------
    def abrir_perfil(self):
        self.app.mostrar_perfil()

    # -------------------------
    def abrir_mapa(self):
        self.app.mostrar_mapa_gasolineras()

    # -------------------------
    def logout(self):
        self.app.usuario = None
        self.app.mostrar_login()

    # =========================
    # MÉTODO PRIVADO
    # =========================
    def _hay_vehiculo_activo(self):
        if not self.app.usuario.get("vehiculo_activo_id"):
            QMessageBox.warning(
                self.widget,
                "Atención",
                "No tienes ningún vehículo activo.\n\n"
                "Registra o selecciona uno para continuar."
            )
            return False
        return True
