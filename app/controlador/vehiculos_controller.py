from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox

from app.vista.vehiculos_ui import Ui_VehiculosView
from app.service.vehiculo_service import VehiculoService


class VehiculosController:

    def __init__(self, app):
        self.app = app
        self.service = VehiculoService()

        # Ventana
        self.widget = QWidget()
        self.ui = Ui_VehiculosView()
        self.ui.setupUi(self.widget)

        # Conexiones de botones
        self.ui.btnAddVehiculo.clicked.connect(self.abrir_add)
        self.ui.btnEliminar.clicked.connect(self.eliminar_vehiculo)
        self.ui.btnSetActivo.clicked.connect(self.marcar_activo)
        self.ui.btnVolver.clicked.connect(self.volver_menu)

        # Cargar datos
        self.cargar_tabla()

        # Mostrar ventana
        self.app._mostrar(self.widget)

    # -----------------------
    # CARGAR TABLA
    # -----------------------
    def cargar_tabla(self):
        # Guardamos los vehículos para reutilizarlos (ej: eliminar)
        self.vehiculos = self.service.listar(self.app.usuario["id"])

        self.ui.tablaVehiculos.setRowCount(len(self.vehiculos))

        for fila, vehiculo in enumerate(self.vehiculos):
            # vehiculo = (id, tipo, marca, modelo, matricula, anio, combustible, consumo)
            _, tipo, marca, modelo, matricula, _, combustible, consumo = vehiculo

            valores = [
                "✔" if self.app.usuario.get("vehiculo_activo_id") == vehiculo[0] else "",
                tipo,
                marca,
                modelo,
                matricula,
                combustible,
                consumo
            ]

            for col, valor in enumerate(valores):
                self.ui.tablaVehiculos.setItem(
                    fila, col, QTableWidgetItem(str(valor))
                )

    # -----------------------
    # AÑADIR VEHÍCULO
    # -----------------------
    def abrir_add(self):
        self.app.mostrar_add_vehiculo()

    # -----------------------
    # MARCAR ACTIVO
    # -----------------------
    def marcar_activo(self):
        fila = self.ui.tablaVehiculos.currentRow()
        if fila < 0:
            return

        vehiculo_id = self.vehiculos[fila][0]

        self.service.marcar_activo(self.app.usuario["id"], vehiculo_id)
        self.app.usuario["vehiculo_activo_id"] = vehiculo_id

        self.cargar_tabla()

    # -----------------------
    # ELIMINAR VEHÍCULO (CON CONFIRMACIÓN)
    # -----------------------
    def eliminar_vehiculo(self):
        fila = self.ui.tablaVehiculos.currentRow()

        if fila < 0:
            return

        respuesta = QMessageBox.question(
            self.widget,
            "Eliminar vehículo",
            "¿Seguro que quieres eliminar este vehículo?\nEsta acción no se puede deshacer.",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if respuesta != QMessageBox.Yes:
            return

        vehiculo_id = self.vehiculos[fila][0]

        self.service.eliminar(vehiculo_id)

        # Si el eliminado era el activo, lo limpiamos
        if self.app.usuario.get("vehiculo_activo_id") == vehiculo_id:
            self.service.limpiar_activo(self.app.usuario["id"])
            self.app.usuario["vehiculo_activo_id"] = None

        self.cargar_tabla()

    # -----------------------
    # VOLVER AL MENÚ
    # -----------------------
    def volver_menu(self):
        self.app.mostrar_menu(self.app.usuario)
