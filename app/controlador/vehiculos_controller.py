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

     msg = QMessageBox(self.widget)
     msg.setWindowTitle("Eliminar vehículo")
     msg.setText(
        "¿Seguro que quieres eliminar este vehículo?\n\n"
        "Esta acción no se puede deshacer."
     )
     msg.setIcon(QMessageBox.Question)

     msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
     msg.setDefaultButton(QMessageBox.No)

    # 🔑 ESTILO COHERENTE CON TU APP
     msg.setStyleSheet("""
     QMessageBox {
        background-color: #081c20;
        color: #ecfeff;
        font-size: 13px;
     }

     QLabel {
        color: #ecfeff;
     }

     QPushButton {
        background-color: #0f3a43;
        color: #ecfeff;
        border: 1px solid #22d3ee;
        border-radius: 8px;
        padding: 6px 14px;
        min-width: 90px;
        font-weight: 600;
     }

     QPushButton:hover {
        background-color: #155e6a;
     }

     QPushButton:pressed {
        background-color: #062023;
     }
    """)

     respuesta = msg.exec()

     if respuesta != QMessageBox.Yes:
        return

     vehiculo_id = self.vehiculos[fila][0]

     self.service.eliminar(vehiculo_id)

    # Si era el activo, limpiar
     if self.app.usuario.get("vehiculo_activo_id") == vehiculo_id:
        self.service.limpiar_activo(self.app.usuario["id"])
        self.app.usuario["vehiculo_activo_id"] = None

     self.cargar_tabla()

    # -----------------------
    # VOLVER AL MENÚ
    # -----------------------
    def volver_menu(self):
        self.app.mostrar_menu(self.app.usuario)
