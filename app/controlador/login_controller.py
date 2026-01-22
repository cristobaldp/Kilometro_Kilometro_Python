from app.service.usuario_service import UsuarioService


class LoginController:

    def __init__(self, widget, ui, app):
        self.widget = widget
        self.ui = ui
        self.app = app
        self.service = UsuarioService()

        self.ui.btnInicioSesion.clicked.connect(self.login)
        self.ui.btnIrRegistro.clicked.connect(self.app.mostrar_registro)

        # Mensaje oculto al iniciar
        self.ui.labelMensaje.setVisible(False)

    def login(self):
        # Ocultar mensaje anterior
        self.ui.labelMensaje.setVisible(False)

        username = self.ui.inputUsername.text().strip()
        password = self.ui.inputPassword.text()

        if not username or not password:
            self.mostrar_info("Introduce usuario y contraseña")
            return

        usuario = self.service.login(username, password)

        if usuario:
            self.app.mostrar_menu(usuario)
        else:
            self.mostrar_error("Usuario o contraseña incorrectos")

    def mostrar_error(self, texto):
        self._mostrar_mensaje(texto, "mensajeError")

    def mostrar_info(self, texto):
        self._mostrar_mensaje(texto, "mensajeInfo")

    def _mostrar_mensaje(self, texto, object_name):
        self.ui.labelMensaje.setObjectName(object_name)
        self.ui.labelMensaje.setText(texto)
        self.ui.labelMensaje.setVisible(True)

        # Forzar a Qt a reaplicar el estilo
        self.ui.labelMensaje.style().unpolish(self.ui.labelMensaje)
        self.ui.labelMensaje.style().polish(self.ui.labelMensaje)
