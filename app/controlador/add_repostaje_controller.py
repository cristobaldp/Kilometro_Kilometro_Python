from PySide6.QtWidgets import QMessageBox
from app.service.repostaje_service import RepostajeService


class AddRepostajeController:

    def __init__(self, widget, ui, app):
        print("DEBUG: AddRepostajeController iniciado")

        self.widget = widget
        self.ui = ui
        self.app = app
        self.service = RepostajeService()

        # 🔴 Comprobar vehículo activo
        self.vehiculo_id = self.app.usuario.get("vehiculo_activo_id")
        if not self.vehiculo_id:
            QMessageBox.warning(
                self.widget,
                "Atención",
                "No hay vehículo activo seleccionado"
            )
            self.app.mostrar_menu(self.app.usuario)
            return

        # Conexiones
        self.ui.btnSave.clicked.connect(self.guardar)
        self.ui.btnCancel.clicked.connect(self.cancelar)

        self.ui.labelMensaje.setVisible(False)

    # ---------------------------------
    def guardar(self):
        self.ui.labelMensaje.setVisible(False)

        fecha = self.ui.inputFecha.date().toString("yyyy-MM-dd")
        litros_txt = self.ui.inputLitros.text().strip()
        precio_txt = self.ui.inputPrecio.text().strip()
        kms_txt = self.ui.inputKilometros.text().strip()

        # Validación campos vacíos
        if not litros_txt or not precio_txt or not kms_txt:
            return self.mostrar_error("Rellena todos los campos")

        # Validación tipos
        try:
            litros = float(litros_txt)
            precio = float(precio_txt)
            kms = int(kms_txt)
        except ValueError:
            return self.mostrar_error("Datos numéricos inválidos")

        # Validación lógica
        if litros <= 0 or precio <= 0 or kms <= 0:
            return self.mostrar_error("Los valores deben ser mayores que 0")

        # Validación kilómetros crecientes
        ultimo_km = self.service.ultimo_kilometraje(self.vehiculo_id)
        if ultimo_km is not None and kms <= ultimo_km:
            return self.mostrar_error(
                f"Los kilómetros deben ser mayores que {ultimo_km}"
            )

        # Guardar
        self.service.insertar(
            vehiculo_id=self.vehiculo_id,
            fecha=fecha,
            litros=litros,
            precio_total=precio,
            kilometros=kms
        )

        # Volver a repostajes
        self.app.mostrar_repostajes()

    # ---------------------------------
    def cancelar(self):
        self.app.mostrar_repostajes()

    # ---------------------------------
    def mostrar_error(self, texto):
        self.ui.labelMensaje.setText(texto)
        self.ui.labelMensaje.setVisible(True)
