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

        # Cargar JSON de vehículos
        self.vehiculos_data = self.cargar_json()

        # Inicializar combos
        self.cargar_tipos()

        # Conexiones de combos
        self.ui.comboTipo.currentTextChanged.connect(self.cargar_marcas)
        self.ui.comboMarca.currentTextChanged.connect(self.cargar_modelos)

        # Botones
        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.btnCancelar.clicked.connect(self.cancelar)

        # Mensajes
        self.ui.labelMensaje.setVisible(False)

    # -------------------------------------------------
    # CARGA JSON (RUTA SEGURA)
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
        self.ui.comboTipo.addItem("Selecciona tipo")
        self.ui.comboMarca.clear()
        self.ui.comboModelo.clear()

        for tipo in self.vehiculos_data.keys():
            self.ui.comboTipo.addItem(tipo)

    def cargar_marcas(self, tipo):
        self.ui.comboMarca.clear()
        self.ui.comboModelo.clear()

        if tipo == "Selecciona tipo":
            return

        self.ui.comboMarca.addItem("Selecciona marca")

        for marca in self.vehiculos_data[tipo].keys():
            self.ui.comboMarca.addItem(marca)

    def cargar_modelos(self, marca):
        tipo = self.ui.comboTipo.currentText()
        self.ui.comboModelo.clear()

        if marca == "Selecciona marca":
            return

        self.ui.comboModelo.addItem("Selecciona modelo")

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
        self.ui.labelMensaje.setVisible(False)

        tipo = self.ui.comboTipo.currentText()
        marca = self.ui.comboMarca.currentText()
        modelo = self.ui.comboModelo.currentText()
        matricula = self.ui.inputMatricula.text().strip().upper()
        combustible = self.ui.comboCombustible.currentText()

        # 🔑 spinConsumo (QDoubleSpinBox)
        consumo = self.ui.spinConsumo.value()
        anio = self.ui.spinAnio.value()

        # Validaciones básicas
        if "Selecciona" in (tipo, marca, modelo):
            return self.mostrar_error("Selecciona tipo, marca y modelo")

        if not matricula:
            return self.mostrar_error("Introduce la matrícula")

        if not self.matricula_valida(matricula):
            return self.mostrar_error("Matrícula inválida (ej: 1234 BCD)")

        if combustible == "":
            return self.mostrar_error("Selecciona el combustible")

        if consumo <= 0:
            return self.mostrar_error("El consumo debe ser mayor que 0")

        if anio <= 0:
            return self.mostrar_error("El año no es válido")

        # Insertar en BBDD
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

        # Volver a vehículos
        self.app.mostrar_vehiculos()

    # -------------------------------------------------
    # CANCELAR
    # -------------------------------------------------
    def cancelar(self):
        self.app.mostrar_vehiculos()

    # -------------------------------------------------
    # MENSAJES
    # -------------------------------------------------
    def mostrar_error(self, texto):
        self.ui.labelMensaje.setText(texto)
        self.ui.labelMensaje.setVisible(True)
