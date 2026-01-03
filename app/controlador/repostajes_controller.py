import csv
from PySide6.QtWidgets import (
    QWidget, QMessageBox, QTableWidgetItem, QFileDialog
)
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from app.vista.repostajes_ui import Ui_RepostajesView
from app.service.repostaje_service import RepostajeService


class RepostajesController:

    def __init__(self, app):
        self.app = app
        self.service = RepostajeService()

        self.vehiculo_id = self.app.usuario.get("vehiculo_activo_id")
        if not self.vehiculo_id:
            QMessageBox.warning(
                None,
                "Atención",
                "Selecciona un vehículo activo primero"
            )
            self.app.mostrar_menu(self.app.usuario)
            return

        self.widget = QWidget()
        self.ui = Ui_RepostajesView()
        self.ui.setupUi(self.widget)

        # Conexiones
        self.ui.btnVolver.clicked.connect(self.volver_menu)
        self.ui.btnNuevo.clicked.connect(self.nuevo_repostaje)
        self.ui.btnEliminar.clicked.connect(self.eliminar_repostaje)
        self.ui.btnExportCSV.clicked.connect(self.exportar_csv)
        self.ui.btnExportPDF.clicked.connect(self.exportar_pdf)

        self.cargar_repostajes()
        self.app._mostrar(self.widget)

    # ---------------------------------
    def cargar_repostajes(self):
        datos = self.service.listar(self.vehiculo_id)

        self.ui.tablaRepostajes.setRowCount(0)
        self.ui.tablaRepostajes.setColumnCount(5)
        self.ui.tablaRepostajes.setHorizontalHeaderLabels(
            ["ID", "Fecha", "Litros", "Precio", "Km"]
        )

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

    # ---------------------------------
    def eliminar_repostaje(self):
        fila = self.ui.tablaRepostajes.currentRow()
        if fila == -1:
            QMessageBox.warning(self.widget, "Eliminar", "Selecciona un repostaje")
            return

        repostaje_id = int(self.ui.tablaRepostajes.item(fila, 0).text())

        if QMessageBox.question(
            self.widget,
            "Confirmar",
            "¿Eliminar repostaje?",
            QMessageBox.Yes | QMessageBox.No
        ) == QMessageBox.Yes:
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

        QMessageBox.information(self.widget, "CSV", "Exportado correctamente")

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
        QMessageBox.information(self.widget, "PDF", "Exportado correctamente")

    # ---------------------------------
    def volver_menu(self):
        self.app.mostrar_menu(self.app.usuario)
