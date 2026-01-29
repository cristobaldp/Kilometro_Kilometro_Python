from PySide6.QtWidgets import QMessageBox
from app.service.usuario_service import UsuarioService
from app.estilos.estilos import MESSAGEBOX_STYLE


class RegistroController:

    def __init__(self, widget, ui, app):
        self.widget = widget
        self.ui = ui
        self.app = app
        self.service = UsuarioService()

        self.cargar_ciudades()

        # Limitar tamaño del combo
        self.ui.comboCiudad.setMaxVisibleItems(5)

        # Conexiones
        self.ui.btnRegistrarse.clicked.connect(self.registrar)
        self.ui.btnIrLogin.clicked.connect(self.app.mostrar_login)

        self.ui.labelMensaje.setVisible(False)

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

        if not all([nombre, apellidos, username, email, telefono, password, password2]):
            return self._error("Rellena todos los campos")

        if not self.email_valido(email):
            return self._error("Email no válido (@gmail, @outlook, @hotmail)")

        if not self.telefono_valido(telefono):
            return self._error("Teléfono inválido (9 dígitos)")

        if ciudad == "Selecciona ciudad":
            return self._error("Selecciona una ciudad")

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

        # ✅ MESSAGEBOX CON ESTILO
        msg = QMessageBox(self.widget)
        msg.setWindowTitle("Registro completado")
        msg.setText(
            "Usuario registrado correctamente.\n\n"
            "Ahora inicia sesión."
        )
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)

        msg.setStyleSheet(MESSAGEBOX_STYLE)
        msg.exec()

        self.app.mostrar_login()

    # -----------------------
    # MENSAJE ERROR (LABEL)
    # -----------------------
    def _error(self, mensaje):
        self.ui.labelMensaje.setText(mensaje)
        self.ui.labelMensaje.setObjectName("mensajeError")
        self.ui.labelMensaje.setVisible(True)
        self.ui.labelMensaje.style().unpolish(self.ui.labelMensaje)
        self.ui.labelMensaje.style().polish(self.ui.labelMensaje)