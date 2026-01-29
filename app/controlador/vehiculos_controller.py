from PySide6.QtWidgets import (
    QWidget,
    QTableWidgetItem,
    QMessageBox,
    QAbstractItemView
)

from app.vista.vehiculos_ui import Ui_VehiculosView
from app.service.vehiculo_service import VehiculoService
from app.estilos.estilos import MESSAGEBOX_STYLE


class VehiculosController:

    def __init__(self, app):
        self.app = app
        self.service = VehiculoService()

        # Ventana
        self.widget = QWidget()
        self.ui = Ui_VehiculosView()
        self.ui.setupUi(self.widget)

        # 🔒 Selección correcta por filas
        self.ui.tablaVehiculos.setSelectionBehavior(
            QAbstractItemView.SelectRows
        )
        self.ui.tablaVehiculos.setSelectionMode(
            QAbstractItemView.SingleSelection
        )
        self.ui.tablaVehiculos.clearSelection()
        self.ui.tablaVehiculos.setCurrentCell(-1, -1)

        # Conexiones
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
        self.vehiculos = self.service.listar(self.app.usuario["id"])
        self.ui.tablaVehiculos.setRowCount(len(self.vehiculos))

        # Limpiar selección cada recarga
        self.ui.tablaVehiculos.clearSelection()
        self.ui.tablaVehiculos.setCurrentCell(-1, -1)

        for fila, vehiculo in enumerate(self.vehiculos):
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
        if not self.ui.tablaVehiculos.selectionModel().hasSelection():
            return

        fila = self.ui.tablaVehiculos.currentRow()
        vehiculo_id = self.vehiculos[fila][0]

        self.service.marcar_activo(self.app.usuario["id"], vehiculo_id)
        self.app.usuario["vehiculo_activo_id"] = vehiculo_id
        self.cargar_tabla()

    # -----------------------
    # ELIMINAR VEHÍCULO
    # -----------------------
    def eliminar_vehiculo(self):

        # 🚫 No hay selección real
        if not self.ui.tablaVehiculos.selectionModel().hasSelection():
            msg = QMessageBox(self.widget)
            msg.setWindowTitle("Eliminar vehículo")
            msg.setText("Debes seleccionar un vehículo para poder eliminarlo.")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setStyleSheet(MESSAGEBOX_STYLE)
            msg.exec()
            return

        fila = self.ui.tablaVehiculos.currentRow()

        # ❓ Confirmación
        msg = QMessageBox(self.widget)
        msg.setWindowTitle("Eliminar vehículo")
        msg.setText(
            "¿Seguro que quieres eliminar este vehículo?\n\n"
            "Esta acción no se puede deshacer."
        )
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        msg.setStyleSheet(MESSAGEBOX_STYLE)

        if msg.exec() != QMessageBox.Yes:
            return

        vehiculo_id = self.vehiculos[fila][0]

        # 🗑️ Eliminar
        self.service.eliminar(vehiculo_id)

        # Si era el activo, quitarlo
        if self.app.usuario.get("vehiculo_activo_id") == vehiculo_id:
            self.service.quitar_activo(self.app.usuario["id"])
            self.app.usuario["vehiculo_activo_id"] = None

        # ✅ Mensaje de éxito
        ok = QMessageBox(self.widget)
        ok.setWindowTitle("Vehículo eliminado")
        ok.setText("El vehículo se ha eliminado correctamente.")
        ok.setIcon(QMessageBox.Information)
        ok.setStandardButtons(QMessageBox.Ok)
        ok.setStyleSheet(MESSAGEBOX_STYLE)
        ok.exec()

        self.cargar_tabla()

    # -----------------------
    # VOLVER AL MENÚ
    # -----------------------
    def volver_menu(self):
        self.app.mostrar_menu(self.app.usuario)