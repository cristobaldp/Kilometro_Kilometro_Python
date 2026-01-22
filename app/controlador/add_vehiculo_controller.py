import json
import os
import re

from app.service.vehiculo_service import VehiculoService


class AddVehiculoController:

    def __init__(self, widget, ui, app):
        self.widget = widget
        self.ui = ui
        self.app = app
        self.service = VehiculoService()

        # -----------------------
        # Datos
        # -----------------------
        self.vehiculos_data = self.cargar_json()

        # -----------------------
        # Ajustes UI
        # -----------------------
        self._ajustar_combos()
        self.cargar_tipos()

        self.ui.labelMensaje.setVisible(False)

        # -----------------------
        # Conexiones
        # -----------------------
        self.ui.comboTipo.currentTextChanged.connect(self.cargar_marcas)
        self.ui.comboMarca.currentTextChanged.connect(self.cargar_modelos)

        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.btnCancelar.clicked.connect(self.cancelar)  # ✅ ahora existe

    # -------------------------------------------------
    # AJUSTES COMBOS
    # -------------------------------------------------
    def _ajustar_combos(self):
        combos = [
            self.ui.comboTipo,
            self.ui.comboMarca,
            self.ui.comboModelo,
            self.ui.comboCombustible
        ]

        for combo in combos:
            combo.setMaxVisibleItems(5)

    # -------------------------------------------------
    # CARGA JSON
    # -------------------------------------------------
    def cargar_json(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        ruta = os.path.join(base_dir, "..", "data", "vehiculos.json")

        with open(ruta, encoding="utf-8") as f:
            return json.load(f)

    # -------------------------------------------------
    # COMBOS
    # -------------------------------------------------
    def cargar_tipos(self):
        self.ui.comboTipo.clear()
        self.ui.comboMarca.clear()
        self.ui.comboModelo.clear()

        self.ui.comboTipo.addItem("Selecciona tipo")
        self.ui.comboMarca.addItem("Selecciona marca")
        self.ui.comboModelo.addItem("Selecciona modelo")

        for tipo in self.vehiculos_data.keys():
            self.ui.comboTipo.addItem(tipo)

    def cargar_marcas(self, tipo):
        self.ui.comboMarca.clear()
        self.ui.comboModelo.clear()

        self.ui.comboMarca.addItem("Selecciona marca")
        self.ui.comboModelo.addItem("Selecciona modelo")

        if tipo == "Selecciona tipo":
            return

        for marca in self.vehiculos_data[tipo].keys():
            self.ui.comboMarca.addItem(marca)

    def cargar_modelos(self, marca):
        tipo = self.ui.comboTipo.currentText()
        self.ui.comboModelo.clear()
        self.ui.comboModelo.addItem("Selecciona modelo")

        if marca == "Selecciona marca":
            return

        for modelo in self.vehiculos_data[tipo][marca]:
            self.ui.comboModelo.addItem(modelo)

    # -------------------------------------------------
    # VALIDACIONES
    # -------------------------------------------------
    def matricula_valida(self, matricula):
        patron = r"^[0-9]{4}\s?[BCDFGHJKLMNPRSTVWXYZ]{3}$"
        return re.match(patron, matricula) is not None

    # -------------------------------------------------
    # GUARDAR
    # -------------------------------------------------
    def guardar(self):
        self._ocultar_mensaje()

        tipo = self.ui.comboTipo.currentText()
        marca = self.ui.comboMarca.currentText()
        modelo = self.ui.comboModelo.currentText()
        combustible = self.ui.comboCombustible.currentText()

        matricula = self.ui.inputMatricula.text().strip().upper()
        consumo = self.ui.spinConsumo.value()
        anio = self.ui.spinAnio.value()

        if "Selecciona" in (tipo, marca, modelo):
            return self._error("Selecciona tipo, marca y modelo")

        if not matricula:
            return self._error("Introduce la matrícula")

        if not self.matricula_valida(matricula):
            return self._error("Matrícula inválida (ej: 1234 BCD)")

        if not combustible:
            return self._error("Selecciona el combustible")

        if consumo <= 0:
            return self._error("El consumo debe ser mayor que 0")

        if anio <= 1900:
            return self._error("El año no es válido")

        self.service.insertar(
            user_id=self.app.usuario["id"],
            tipo=tipo,
            marca=marca,
            modelo=modelo,
            matricula=matricula,
            anio=anio,
            combustible=combustible,
            consumo=consumo
        )

        self.app.mostrar_vehiculos()

    # -------------------------------------------------
    # CANCELAR  ✅ ESTE ERA EL PROBLEMA
    # -------------------------------------------------
    def cancelar(self):
        self.app.mostrar_vehiculos()

    # -------------------------------------------------
    # MENSAJES
    # -------------------------------------------------
    def _error(self, texto):
     lbl = self.ui.labelMensaje
     lbl.setText(texto)

    # 🔑 Cambiar objectName
     lbl.setObjectName("mensajeError")

     # 🔑 Forzar reaplicar QSS
     lbl.style().unpolish(lbl)
     lbl.style().polish(lbl)

     lbl.setVisible(True)


    def _ocultar_mensaje(self):
     lbl = self.ui.labelMensaje
     lbl.setVisible(False)

    # opcional: reset nombre
     lbl.setObjectName("labelMensaje")
