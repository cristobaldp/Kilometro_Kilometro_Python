from app.service.repostaje_service import RepostajeService


class AddRepostajeController:

    def __init__(self, widget, ui, app):
        self.widget = widget
        self.ui = ui
        self.app = app
        self.service = RepostajeService()

        # Mensaje oculto al inicio
        self.ui.labelMensaje.setVisible(False)

        # -----------------------------
        # Comprobar vehículo activo
        # -----------------------------
        self.vehiculo_id = self.app.usuario.get("vehiculo_activo_id")
        if not self.vehiculo_id:
            # ❗ NO mostrar mensaje aquí (no se vería)
            self.app.mostrar_menu(self.app.usuario)
            return

        # Conexiones
        self.ui.btnSave.clicked.connect(self.guardar)
        self.ui.btnCancel.clicked.connect(self.cancelar)

    # ---------------------------------
    def guardar(self):
        self.ui.labelMensaje.setVisible(False)

        fecha = self.ui.inputFecha.date().toString("yyyy-MM-dd")
        litros_txt = self.ui.inputLitros.text().strip()
        precio_txt = self.ui.inputPrecio.text().strip()
        kms_txt = self.ui.inputKilometros.text().strip()

        # -----------------------------
        # Validaciones básicas
        # -----------------------------
        if not litros_txt or not precio_txt or not kms_txt:
            return self.mostrar_error("Rellena todos los campos")

        try:
            litros = float(litros_txt)
            precio = float(precio_txt)
            kms = int(kms_txt)
        except ValueError:
            return self.mostrar_error("Introduce valores numéricos válidos")

        if litros <= 0:
            return self.mostrar_error("Los litros deben ser mayores que 0")

        if precio <= 0:
            return self.mostrar_error("El precio debe ser mayor que 0")

        if kms <= 0:
            return self.mostrar_error("Los kilómetros deben ser mayores que 0")

        # -----------------------------
        # Kilometraje creciente
        # -----------------------------
        ultimo_km = self.service.ultimo_kilometraje(self.vehiculo_id)
        if ultimo_km is not None and kms <= ultimo_km:
            return self.mostrar_error(
                f"Los kilómetros deben ser mayores que {ultimo_km}"
            )

        # -----------------------------
        # Guardar
        # -----------------------------
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
     lbl = self.ui.labelMensaje
     lbl.setText(texto)

    #  MISMO PATRÓN QUE EN VEHÍCULOS
     lbl.setObjectName("mensajeError")

     lbl.style().unpolish(lbl)
     lbl.style().polish(lbl)

     lbl.setVisible(True)
     
     
    def _ocultar_mensaje(self):
     lbl = self.ui.labelMensaje
     lbl.setVisible(False)
     lbl.setObjectName("labelMensaje")

