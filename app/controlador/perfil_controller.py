from PySide6.QtWidgets import QMessageBox
from app.service.usuario_service import UsuarioService

from app.estilos.estilos import MESSAGEBOX_STYLE
class PerfilController:

    def __init__(self, widget, ui, app):
        self.widget = widget
        self.ui = ui
        self.app = app
        self.service = UsuarioService()

        # Cargar datos y estado inicial
        self.cargar_datos()
        self.bloquear_campos()

        # Conexiones
        self.ui.btnEditar.clicked.connect(self.editar)
        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.btnVolver.clicked.connect(self.volver)
        self.ui.btnCambiarPassword.clicked.connect(self.cambiar_password)
        self.ui.btnEliminarCuenta.clicked.connect(self.eliminar_cuenta)

        self.ui.labelMensaje.setVisible(False)

 

    def _msgbox(self, icono, titulo, texto):
        msg = QMessageBox(self.widget)
        msg.setIcon(icono)
        msg.setWindowTitle(titulo)
        msg.setText(texto)
        msg.setStyleSheet(MESSAGEBOX_STYLE)
        msg.exec()

    def _confirmar(self, texto):
        msg = QMessageBox(self.widget)
        msg.setIcon(QMessageBox.Question)
        msg.setWindowTitle("Confirmar")
        msg.setText(texto)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setStyleSheet(MESSAGEBOX_STYLE)
        return msg.exec() == QMessageBox.Yes

    # -------------------------------------------------
    # CARGAR DATOS
    # -------------------------------------------------
    def cargar_datos(self):
        u = self.app.usuario

        self.ui.inputNombre.setText(u["nombre"])
        self.ui.inputApellidos.setText(u["apellidos"])
        self.ui.inputUsername.setText(u["username"])
        self.ui.inputEmail.setText(u["email"])
        self.ui.inputTelefono.setText(u["telefono"])
        self.ui.inputCiudad.setText(u["ciudad"])

        if u.get("fecha_nacimiento"):
            self.ui.dateNacimiento.setDate(
                self.ui.dateNacimiento.date().fromString(
                    u["fecha_nacimiento"], "yyyy-MM-dd"
                )
            )

    # -------------------------------------------------
    # BLOQUEAR CAMPOS
    # -------------------------------------------------
    def bloquear_campos(self):
        campos = [
            self.ui.inputNombre,
            self.ui.inputApellidos,
            self.ui.inputEmail,
            self.ui.inputTelefono,
            self.ui.inputCiudad,
            self.ui.dateNacimiento
        ]

        for campo in campos:
            campo.setEnabled(False)
            campo.setProperty("editable", False)
            campo.style().unpolish(campo)
            campo.style().polish(campo)

        self.ui.inputUsername.setEnabled(False)
        self.ui.btnGuardar.setEnabled(False)

    # -------------------------------------------------
    # MODO EDICIÓN
    # -------------------------------------------------
    def editar(self):
        self.ocultar_mensaje()

        campos = [
            self.ui.inputNombre,
            self.ui.inputApellidos,
            self.ui.inputEmail,
            self.ui.inputTelefono,
            self.ui.inputCiudad,
            self.ui.dateNacimiento
        ]

        for campo in campos:
            campo.setEnabled(True)
            campo.setProperty("editable", True)
            campo.style().unpolish(campo)
            campo.style().polish(campo)

        self.ui.btnGuardar.setEnabled(True)

    # -------------------------------------------------
    # GUARDAR PERFIL
    # -------------------------------------------------
    def guardar(self):
        self.ocultar_mensaje()

        nombre = self.ui.inputNombre.text().strip()
        apellidos = self.ui.inputApellidos.text().strip()
        email = self.ui.inputEmail.text().strip()
        telefono = self.ui.inputTelefono.text().strip()
        ciudad = self.ui.inputCiudad.text().strip()

        if not nombre:
            return self.mostrar_error("El nombre no puede estar vacío")
        if not apellidos:
            return self.mostrar_error("Los apellidos no pueden estar vacíos")
        if not email:
            return self.mostrar_error("El email no puede estar vacío")
        if not ciudad:
            return self.mostrar_error("La ciudad no puede estar vacía")
        if not telefono.isdigit() or len(telefono) != 9:
            return self.mostrar_error("Teléfono inválido (9 dígitos)")

        datos = {
            "id": self.app.usuario["id"],
            "nombre": nombre,
            "apellidos": apellidos,
            "email": email,
            "telefono": telefono,
            "ciudad": ciudad
        }

        try:
            self.service.actualizar_perfil(datos)
            self.app.usuario.update(datos)

            self._msgbox(
                QMessageBox.Information,
                "Perfil",
                "Datos actualizados correctamente"
            )

            self.bloquear_campos()
            self.app.mostrar_menu(self.app.usuario)

        except Exception as e:
            self.mostrar_error(str(e))

    # -------------------------------------------------
    # CAMBIAR CONTRASEÑA
    # -------------------------------------------------
    def cambiar_password(self):
        self.ocultar_mensaje()

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

            self._msgbox(
                QMessageBox.Information,
                "Contraseña",
                "Contraseña actualizada correctamente"
            )

            self.ui.inputPassNueva.clear()
            self.ui.inputPassNueva2.clear()

        except Exception as e:
            self.mostrar_error(str(e))

    # -------------------------------------------------
    # ELIMINAR CUENTA
    # -------------------------------------------------
    def eliminar_cuenta(self):
        if self._confirmar(
            "¿Seguro que deseas eliminar tu cuenta?\n\n"
            "Esta acción no se puede deshacer."
        ):
            self.service.eliminar_cuenta(self.app.usuario["id"])
            self.app.usuario = None
            self.app.mostrar_login()

    # -------------------------------------------------
    # VOLVER
    # -------------------------------------------------
    def volver(self):
        self.app.mostrar_menu(self.app.usuario)

    # -------------------------------------------------
    # MENSAJES INLINE
    # -------------------------------------------------
    def mostrar_error(self, texto):
        lbl = self.ui.labelMensaje
        lbl.setText(texto)
        lbl.setObjectName("mensajeError")
        lbl.style().unpolish(lbl)
        lbl.style().polish(lbl)
        lbl.setVisible(True)

    def ocultar_mensaje(self):
        self.ui.labelMensaje.setVisible(False)
        self.ui.labelMensaje.setObjectName("labelMensaje")
