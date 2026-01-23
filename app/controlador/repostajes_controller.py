import csv
from PySide6.QtWidgets import (
    QWidget, QMessageBox, QTableWidgetItem, QFileDialog
)
from PySide6.QtCore import Qt

from app.vista.repostajes_ui import Ui_RepostajesView
from app.service.repostaje_service import RepostajeService
from app.service.vehiculo_service import VehiculoService
from app.reports.informe_repostajes_pdf import InformeRepostajesPDF


class RepostajesController:

    def __init__(self, app):
        self.app = app
        self.service = RepostajeService()
        self.vehiculo_service = VehiculoService()

        self.vehiculo_id = self.app.usuario.get("vehiculo_activo_id")
        if not self.vehiculo_id:
            self._mostrar_aviso_vehiculo()
            return

        self.widget = QWidget()
        self.ui = Ui_RepostajesView()
        self.ui.setupUi(self.widget)

        self._datos_filtrados = None
        self._periodo_actual = "Todos los repostajes"

        self._configurar_combos()
        self._conectar_eventos()

        self.cargar_repostajes()
        self.app._mostrar(self.widget)

    # =================================================
    # CONFIG
    # =================================================
    def _configurar_combos(self):
        for combo in (self.ui.comboMes, self.ui.comboAnio):
            combo.setMaxVisibleItems(6)
            combo.view().setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

    def _conectar_eventos(self):
        self.ui.btnVolver.clicked.connect(self.volver_menu)
        self.ui.btnNuevo.clicked.connect(self.nuevo_repostaje)
        self.ui.btnBuscar.clicked.connect(self.buscar_por_fecha)
        self.ui.btnEliminar.clicked.connect(self.eliminar_repostaje)
        self.ui.btnExportCSV.clicked.connect(self.exportar_csv)
        self.ui.btnExportPDF.clicked.connect(self.exportar_pdf)

    # =================================================
    # CARGA / FILTRO
    # =================================================
    def cargar_repostajes(self):
        datos = self.service.listar(self.vehiculo_id)
        self._datos_filtrados = None
        self._periodo_actual = "Todos los repostajes"
        self._cargar_tabla(datos)

    def _cargar_tabla(self, datos):
        self.ui.tablaRepostajes.setRowCount(0)

        for fila, r in enumerate(datos):
            self.ui.tablaRepostajes.insertRow(fila)
            for col, valor in enumerate(r):
                self.ui.tablaRepostajes.setItem(
                    fila, col, QTableWidgetItem(str(valor))
                )

        self.ui.tablaRepostajes.setColumnHidden(0, True)

    def buscar_por_fecha(self):
        mes, anio, periodo = self._obtener_filtro_fecha()

        datos = self.service.listar_filtrado(
            self.vehiculo_id,
            mes,
            anio
        )

        self._datos_filtrados = datos
        self._periodo_actual = periodo
        self._cargar_tabla(datos)

    def _obtener_filtro_fecha(self):
        meses = {
            "Enero": 1, "Febrero": 2, "Marzo": 3,
            "Abril": 4, "Mayo": 5, "Junio": 6,
            "Julio": 7, "Agosto": 8, "Septiembre": 9,
            "Octubre": 10, "Noviembre": 11, "Diciembre": 12
        }

        mes_texto = self.ui.comboMes.currentText()
        anio_texto = self.ui.comboAnio.currentText()

        mes = meses.get(mes_texto) if mes_texto != "Todos los meses" else None
        anio = int(anio_texto) if anio_texto != "Todos los años" else None

        if mes and anio:
            periodo = f"{mes_texto} {anio}"
        elif anio:
            periodo = f"Año {anio}"
        else:
            periodo = "Todos los repostajes"

        return mes, anio, periodo

    # =================================================
    # ACCIONES
    # =================================================
    def nuevo_repostaje(self):
        self.app.mostrar_add_repostaje()

    def eliminar_repostaje(self):
        fila = self.ui.tablaRepostajes.currentRow()
        if fila == -1:
            self._msg("Eliminar", "Selecciona un repostaje", QMessageBox.Warning)
            return

        repostaje_id = int(self.ui.tablaRepostajes.item(fila, 0).text())

        if self._confirmar("¿Eliminar repostaje?\n\nEsta acción no se puede deshacer."):
            self.service.eliminar(repostaje_id)
            self.cargar_repostajes()

    # =================================================
    # EXPORTAR CSV (CORREGIDO)
    # =================================================
    def exportar_csv(self):

        # 🔹 Datos a exportar
        datos = (
            self._datos_filtrados
            if self._datos_filtrados is not None
            else self.service.listar(self.vehiculo_id)
        )

        if not datos:
            self._msg(
                "CSV",
                "No hay repostajes para exportar en el período seleccionado",
                QMessageBox.Warning
            )
            return

        ruta, _ = QFileDialog.getSaveFileName(
            self.widget,
            "Exportar CSV",
            "",
            "CSV (*.csv)"
        )
        if not ruta:
            return

        with open(ruta, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(
                ["Fecha", "Litros", "Kilómetros", "Precio (€)"]
            )
            for r in datos:
                writer.writerow([
                    r[1],  # fecha
                    r[2],  # litros
                    r[3],  # km
                    r[4]   # precio
                ])

        self._msg("CSV", "CSV exportado correctamente", QMessageBox.Information)

    # =================================================
    # EXPORTAR PDF
    # =================================================
    def exportar_pdf(self):
        path, _ = QFileDialog.getSaveFileName(
            self.widget, "Guardar PDF", "", "PDF (*.pdf)"
        )
        if not path:
            return

        datos = (
            self._datos_filtrados
            if self._datos_filtrados is not None
            else self.service.obtener_para_exportar(self.vehiculo_id)
        )

        if not datos:
            self._msg("PDF", "No hay datos para generar el informe", QMessageBox.Warning)
            return

        usuario = {
            "Nombre": self.app.usuario.get("nombre"),
            "Apellidos": self.app.usuario.get("apellidos"),
            "Usuario": self.app.usuario.get("username"),
            "Email": self.app.usuario.get("email"),
            "Teléfono": self.app.usuario.get("telefono"),
            "Ciudad": self.app.usuario.get("ciudad")
        }

        vehiculo = self.vehiculo_service.obtener_por_id(self.vehiculo_id)
        if not vehiculo:
            self._msg("PDF", "No se pudo obtener el vehículo", QMessageBox.Warning)
            return

        InformeRepostajesPDF.generar(
            path,
            usuario,
            vehiculo,
            datos,
            self._periodo_actual
        )

        self._msg("PDF", "Informe generado correctamente", QMessageBox.Information)

    # =================================================
    def volver_menu(self):
        self.app.mostrar_menu(self.app.usuario)

    # =================================================
    # MENSAJES CON ESTILO
    # =================================================
    def _mostrar_aviso_vehiculo(self):
        self._msg(
            "Atención",
            "No tienes ningún vehículo activo.\n\nRegistra o selecciona uno.",
            QMessageBox.Warning
        )

    def _msg(self, titulo, texto, icono):
        msg = QMessageBox(self.widget)
        msg.setWindowTitle(titulo)
        msg.setText(texto)
        msg.setIcon(icono)
        msg.setStyleSheet(self._estilo_msgbox())
        msg.exec()

    def _confirmar(self, texto):
        msg = QMessageBox(self.widget)
        msg.setWindowTitle("Confirmar")
        msg.setText(texto)
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setStyleSheet(self._estilo_msgbox())
        return msg.exec() == QMessageBox.Yes

    def _estilo_msgbox(self):
        return """
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
        """
