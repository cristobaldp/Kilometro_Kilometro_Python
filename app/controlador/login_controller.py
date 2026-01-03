from app.service.usuario_service import UsuarioService


class LoginController:

    def __init__(self, widget, ui, app):
        self.widget = widget
        self.ui = ui
        self.app = app
        self.service = UsuarioService()

        self.ui.btnInicioSesion.clicked.connect(self.login)
        self.ui.btnIrRegistro.clicked.connect(self.app.mostrar_registro)

        self.ui.labelMensaje.setVisible(False)

    def login(self):
        self.ui.labelMensaje.setVisible(False)

        username = self.ui.inputUsername.text().strip()
        password = self.ui.inputPassword.text()

        if not username or not password:
            self.mostrar_error("Introduce usuario y contraseña")
            return

        usuario = self.service.login(username, password)

        if usuario:
            print("DEBUG usuario:", usuario)  # 👈 puedes borrar luego
            self.app.mostrar_menu(usuario)
        else:
            self.mostrar_error("Usuario o contraseña incorrectos")

    def mostrar_error(self, texto):
        self.ui.labelMensaje.setText(texto)
        self.ui.labelMensaje.setVisible(True)
