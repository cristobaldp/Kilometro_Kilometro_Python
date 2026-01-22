import csv
from PySide6.QtWidgets import (
    QWidget, QMessageBox, QTableWidgetItem, QFileDialog
)
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from app.vista.repostajes_ui import Ui_RepostajesView
from app.service.repostaje_service import RepostajeService

from PySide6.QtCore import Qt

class RepostajesController:

    def __init__(self, app):
        self.app = app
        self.service = RepostajeService()

        self.vehiculo_id = self.app.usuario.get("vehiculo_activo_id")
        if not self.vehiculo_id:
            msg = QMessageBox(self.app.ventana_actual)
            msg.setWindowTitle("Atención")
            msg.setText(
                "No tienes ningún vehículo activo.\n\n"
                "Registra o selecciona uno para acceder a los repostajes."
            )
            msg.setIcon(QMessageBox.Warning)
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
            """)
            msg.exec()
            return

        self.widget = QWidget()
        self.ui = Ui_RepostajesView()
        self.ui.setupUi(self.widget)
        
        self.ui.comboMes.setMaxVisibleItems(6)
        self.ui.comboAnio.setMaxVisibleItems(6)

        self.ui.comboMes.view().setVerticalScrollBarPolicy(
       Qt.ScrollBarAsNeeded
     )
        self.ui.comboAnio.view().setVerticalScrollBarPolicy(
      Qt.ScrollBarAsNeeded
     )


        # Conexiones
        self.ui.btnVolver.clicked.connect(self.volver_menu)
        self.ui.btnNuevo.clicked.connect(self.nuevo_repostaje)
        self.ui.btnBuscar.clicked.connect(self.buscar_por_fecha)

        self.ui.btnEliminar.clicked.connect(self.eliminar_repostaje)
        self.ui.btnExportCSV.clicked.connect(self.exportar_csv)
        self.ui.btnExportPDF.clicked.connect(self.exportar_pdf)

        self.cargar_repostajes()
        self.app._mostrar(self.widget)

    # ---------------------------------
    def cargar_repostajes(self):
     datos = self.service.listar(self.vehiculo_id)
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


    # ---------------------------------
    def nuevo_repostaje(self):
        self.app.mostrar_add_repostaje()
        
    def buscar_por_fecha(self):
     mes_texto = self.ui.comboMes.currentText()
     anio_texto = self.ui.comboAnio.currentText()

     mes = None
     anio = None

     if mes_texto != "Todos los meses":
        meses = {
            "Enero": 1, "Febrero": 2, "Marzo": 3,
            "Abril": 4, "Mayo": 5, "Junio": 6,
            "Julio": 7, "Agosto": 8, "Septiembre": 9,
            "Octubre": 10, "Noviembre": 11, "Diciembre": 12
        }
        mes = meses.get(mes_texto)

     if anio_texto != "Todos los años":
        anio = int(anio_texto)

     datos = self.service.listar_filtrado(
        self.vehiculo_id,
        mes,
        anio
     )

     self._cargar_tabla(datos)
 

    # ---------------------------------
    def eliminar_repostaje(self):
        fila = self.ui.tablaRepostajes.currentRow()
        if fila == -1:
            msg = QMessageBox(self.widget)
            msg.setWindowTitle("Eliminar")
            msg.setText("Selecciona un repostaje")
            msg.setIcon(QMessageBox.Warning)
            msg.setStyleSheet(self._estilo_msgbox())
            msg.exec()
            return

        repostaje_id = int(self.ui.tablaRepostajes.item(fila, 0).text())

        msg = QMessageBox(self.widget)
        msg.setWindowTitle("Confirmar")
        msg.setText("¿Eliminar repostaje?\n\nEsta acción no se puede deshacer.")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setStyleSheet(self._estilo_msgbox())

        if msg.exec() == QMessageBox.Yes:
            self.service.eliminar(repostaje_id)
            self.cargar_repostajes()

    # ---------------------------------
    def exportar_csv(self):
        path, _ = QFileDialog.getSaveFileName(
            self.widget, "Guardar CSV", "", "CSV (*.csv)"
        )
        if not path:
            return

        datos = self.service.obtener_para_exportar(self.vehiculo_id)

        with open(path, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Fecha", "Litros", "Precio", "Kilómetros"])
            for _, fecha, litros, precio, km in datos:
                writer.writerow([fecha, litros, precio, km])

        msg = QMessageBox(self.widget)
        msg.setWindowTitle("CSV")
        msg.setText("Exportado correctamente")
        msg.setIcon(QMessageBox.Information)
        msg.setStyleSheet(self._estilo_msgbox())
        msg.exec()

    # ---------------------------------
    def exportar_pdf(self):
        path, _ = QFileDialog.getSaveFileName(
            self.widget, "Guardar PDF", "", "PDF (*.pdf)"
        )
        if not path:
            return

        datos = self.service.obtener_para_exportar(self.vehiculo_id)

        pdf = canvas.Canvas(path, pagesize=A4)
        y = 800
        pdf.setFont("Helvetica", 10)
        pdf.drawString(50, y, "Repostajes")

        y -= 30
        for _, fecha, litros, precio, km in datos:
            pdf.drawString(
                50, y,
                f"{fecha} | {litros} L | {precio} € | {km} km"
            )
            y -= 15
            if y < 50:
                pdf.showPage()
                pdf.setFont("Helvetica", 10)
                y = 800

        pdf.save()

        msg = QMessageBox(self.widget)
        msg.setWindowTitle("PDF")
        msg.setText("Exportado correctamente")
        msg.setIcon(QMessageBox.Information)
        msg.setStyleSheet(self._estilo_msgbox())
        msg.exec()

    # ---------------------------------
    def volver_menu(self):
        self.app.mostrar_menu(self.app.usuario)

    # ---------------------------------
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
        
    
