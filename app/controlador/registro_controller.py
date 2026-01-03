from app.service.usuario_service import UsuarioService


class RegistroController:

    def __init__(self, widget, ui, app):
        self.widget = widget
        self.ui = ui
        self.app = app
        self.service = UsuarioService()

        self.cargar_ciudades()

        # Conexiones CORRECTAS según la UI real
        self.ui.btnRegistrarse.clicked.connect(self.registrar)
        self.ui.btnIrLogin.clicked.connect(self.app.mostrar_login)

    # -----------------------
    # VALIDACIONES
    # -----------------------
    def telefono_valido(self, telefono: str) -> bool:
        return telefono.isdigit() and len(telefono) == 9

    def email_valido(self, email: str) -> bool:
        return email.endswith(("@gmail.com", "@outlook.com", "@hotmail.com"))

    # -----------------------
    # CIUDADES
    # -----------------------
    def cargar_ciudades(self):
        self.ui.comboCiudad.clear()
        self.ui.comboCiudad.addItem("Selecciona ciudad")

        try:
            with open("app/data/ciudades.txt", encoding="utf-8") as f:
                for ciudad in f:
                    self.ui.comboCiudad.addItem(ciudad.strip())
        except FileNotFoundError:
            self.ui.comboCiudad.addItem("No disponible")

    # -----------------------
    # REGISTRO
    # -----------------------
    def registrar(self):
        self.ui.labelMensaje.setVisible(False)

        nombre = self.ui.inputNombre.text().strip()
        apellidos = self.ui.inputApellidos.text().strip()
        username = self.ui.inputUsername.text().strip()
        email = self.ui.inputEmail.text().strip()
        telefono = self.ui.inputTelefono.text().strip()
        ciudad = self.ui.comboCiudad.currentText()
        fecha = self.ui.dateNacimiento.date().toString("yyyy-MM-dd")
        password = self.ui.inputPassword.text()
        password2 = self.ui.inputPassword2.text()

        # Campos obligatorios
        if not all([nombre, apellidos, username, email, telefono, password, password2]):
            return self._error("Rellena todos los campos")

        # Email
        if not self.email_valido(email):
            return self._error("Email no válido (@gmail, @outlook, @hotmail)")

        # Teléfono
        if not self.telefono_valido(telefono):
            return self._error("Teléfono inválido (9 dígitos)")

        # Ciudad
        if ciudad == "Selecciona ciudad":
            return self._error("Selecciona una ciudad")

        # Contraseñas
        if password != password2:
            return self._error("Las contraseñas no coinciden")

        datos = {
            "nombre": nombre,
            "apellidos": apellidos,
            "username": username,
            "email": email,
            "telefono": telefono,
            "ciudad": ciudad,
            "fecha_nacimiento": fecha,
            "password": password
        }

        usuario = self.service.registrar_usuario(datos)

        if not usuario:
            return self._error("El usuario ya existe")

        # Todo correcto → menú
        self.app.mostrar_menu(usuario)

    def _error(self, mensaje):
        self.ui.labelMensaje.setText(mensaje)
        self.ui.labelMensaje.setVisible(True)
