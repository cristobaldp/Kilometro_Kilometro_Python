from PySide6.QtWidgets import QMessageBox
from app.service.usuario_service import UsuarioService


class PerfilController:

    def __init__(self, widget, ui, app):
        self.widget = widget
        self.ui = ui
        self.app = app
        self.service = UsuarioService()

        self.cargar_datos()
        self.bloquear_campos()

        self.ui.btnEditar.clicked.connect(self.editar)
        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.btnVolver.clicked.connect(self.volver)
        self.ui.btnCambiarPassword.clicked.connect(self.cambiar_password)
        self.ui.btnEliminarCuenta.clicked.connect(self.eliminar_cuenta)

    # -------------------------
    def cargar_datos(self):
        u = self.app.usuario

        self.ui.inputNombre.setText(u["nombre"])
        self.ui.inputApellidos.setText(u["apellidos"])
        self.ui.inputUsername.setText(u["username"])
        self.ui.inputEmail.setText(u["email"])
        self.ui.inputTelefono.setText(u["telefono"])
        self.ui.inputCiudad.setText(u["ciudad"])

        if u["fecha_nacimiento"]:
            self.ui.dateNacimiento.setDate(
                self.ui.dateNacimiento.date().fromString(
                    u["fecha_nacimiento"], "yyyy-MM-dd"
                )
            )

    # -------------------------
    def bloquear_campos(self):
        for campo in [
            self.ui.inputNombre,
            self.ui.inputApellidos,
            self.ui.inputEmail,
            self.ui.inputTelefono,
            self.ui.inputCiudad,
            self.ui.dateNacimiento
        ]:
            campo.setEnabled(False)

        self.ui.inputUsername.setEnabled(False)
        self.ui.btnGuardar.setEnabled(False)

    # -------------------------
    def editar(self):
        for campo in [
            self.ui.inputNombre,
            self.ui.inputApellidos,
            self.ui.inputEmail,
            self.ui.inputTelefono,
            self.ui.inputCiudad,
            self.ui.dateNacimiento
        ]:
            campo.setEnabled(True)

        self.ui.btnGuardar.setEnabled(True)

    # -------------------------
    def guardar(self):
        telefono = self.ui.inputTelefono.text().strip()
        if not telefono.isdigit() or len(telefono) != 9:
            return self.mostrar_error("Teléfono inválido (9 dígitos)")

        datos = {
            "id": self.app.usuario["id"],
            "nombre": self.ui.inputNombre.text(),
            "apellidos": self.ui.inputApellidos.text(),
            "email": self.ui.inputEmail.text(),
            "telefono": telefono,
            "ciudad": self.ui.inputCiudad.text()
        }

        self.service.actualizar_perfil(datos)
        self.app.usuario.update(datos)

        QMessageBox.information(self.widget, "Perfil", "Datos actualizados")
        self.app.mostrar_menu(self.app.usuario)

    # -------------------------
    def cambiar_password(self):
     p1 = self.ui.inputPassNueva.text().strip()
     p2 = self.ui.inputPassNueva2.text().strip()

     if not p1 or not p2:
        return self.mostrar_error("Rellena ambas contraseñas")

     if p1 != p2:
        return self.mostrar_error("Las contraseñas no coinciden")

     if len(p1) < 4:
        return self.mostrar_error("Mínimo 4 caracteres")

     try:
        self.service.cambiar_password(self.app.usuario["id"], p1)
        QMessageBox.information(
            self.widget,
            "Contraseña",
            "Contraseña actualizada correctamente"
        )
        self.ui.inputPassNueva.clear()
        self.ui.inputPassNueva2.clear()

     except Exception as e:
        self.mostrar_error(str(e))

    # -------------------------
    def eliminar_cuenta(self):
        resp = QMessageBox.question(
            self.widget,
            "Confirmar",
            "¿Seguro que deseas eliminar tu cuenta?\nEsta acción no se puede deshacer",
            QMessageBox.Yes | QMessageBox.No
        )

        if resp == QMessageBox.Yes:
            self.service.eliminar_cuenta(self.app.usuario["id"])
            self.app.usuario = None
            self.app.mostrar_login()

    # -------------------------
    def volver(self):
        self.app.mostrar_menu(self.app.usuario)

    # -------------------------
    def mostrar_error(self, texto):
        self.ui.labelMensaje.setText(texto)
        self.ui.labelMensaje.setVisible(True)
