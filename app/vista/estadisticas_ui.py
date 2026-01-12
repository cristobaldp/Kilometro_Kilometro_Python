# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'estadisticas.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_EstadisticasView(object):
    def setupUi(self, EstadisticasView):
        if not EstadisticasView.objectName():
            EstadisticasView.setObjectName(u"EstadisticasView")
        EstadisticasView.resize(720, 720)
        self.vboxLayout = QVBoxLayout(EstadisticasView)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.labelTitulo = QLabel(EstadisticasView)
        self.labelTitulo.setObjectName(u"labelTitulo")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(22)
        font.setBold(True)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout.addWidget(self.labelTitulo)

        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.comboMes = QComboBox(EstadisticasView)
        self.comboMes.addItem("")
        self.comboMes.addItem("")
        self.comboMes.addItem("")
        self.comboMes.addItem("")
        self.comboMes.addItem("")
        self.comboMes.addItem("")
        self.comboMes.addItem("")
        self.comboMes.addItem("")
        self.comboMes.addItem("")
        self.comboMes.addItem("")
        self.comboMes.addItem("")
        self.comboMes.addItem("")
        self.comboMes.setObjectName(u"comboMes")

        self.hboxLayout.addWidget(self.comboMes)

        self.comboAnio = QComboBox(EstadisticasView)
        self.comboAnio.addItem("")
        self.comboAnio.addItem("")
        self.comboAnio.addItem("")
        self.comboAnio.addItem("")
        self.comboAnio.addItem("")
        self.comboAnio.addItem("")
        self.comboAnio.addItem("")
        self.comboAnio.addItem("")
        self.comboAnio.addItem("")
        self.comboAnio.addItem("")
        self.comboAnio.addItem("")
        self.comboAnio.addItem("")
        self.comboAnio.setObjectName(u"comboAnio")

        self.hboxLayout.addWidget(self.comboAnio)

        self.btnFiltrar = QPushButton(EstadisticasView)
        self.btnFiltrar.setObjectName(u"btnFiltrar")

        self.hboxLayout.addWidget(self.btnFiltrar)


        self.vboxLayout.addLayout(self.hboxLayout)

        self.hboxLayout1 = QHBoxLayout()
        self.hboxLayout1.setObjectName(u"hboxLayout1")
        self.btnExportCSV = QPushButton(EstadisticasView)
        self.btnExportCSV.setObjectName(u"btnExportCSV")

        self.hboxLayout1.addWidget(self.btnExportCSV)

        self.btnExportPDF = QPushButton(EstadisticasView)
        self.btnExportPDF.setObjectName(u"btnExportPDF")

        self.hboxLayout1.addWidget(self.btnExportPDF)


        self.vboxLayout.addLayout(self.hboxLayout1)

        self.groupGasto = QGroupBox(EstadisticasView)
        self.groupGasto.setObjectName(u"groupGasto")
        self.layoutGasto = QVBoxLayout(self.groupGasto)
        self.layoutGasto.setObjectName(u"layoutGasto")

        self.vboxLayout.addWidget(self.groupGasto)

        self.groupConsumo = QGroupBox(EstadisticasView)
        self.groupConsumo.setObjectName(u"groupConsumo")
        self.layoutConsumo = QVBoxLayout(self.groupConsumo)
        self.layoutConsumo.setObjectName(u"layoutConsumo")

        self.vboxLayout.addWidget(self.groupConsumo)

        self.btnVolver = QPushButton(EstadisticasView)
        self.btnVolver.setObjectName(u"btnVolver")

        self.vboxLayout.addWidget(self.btnVolver)


        self.retranslateUi(EstadisticasView)

        QMetaObject.connectSlotsByName(EstadisticasView)
    # setupUi

    def retranslateUi(self, EstadisticasView):
        EstadisticasView.setWindowTitle(QCoreApplication.translate("EstadisticasView", u"Estad\u00edsticas", None))
        EstadisticasView.setStyleSheet(QCoreApplication.translate("EstadisticasView", u"\n"
"QWidget {\n"
"    background-color: #121212;\n"
"    color: #eaeaea;\n"
"    font-family: Segoe UI;\n"
"}\n"
"\n"
"QLabel#labelTitulo {\n"
"    color: #00c853;\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: #1e1e1e;\n"
"    border: 2px solid #2e2e2e;\n"
"    border-radius: 8px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #00c853;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #00c853;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    font-weight: bold;\n"
"    color: #000;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #00e676;\n"
"}\n"
"\n"
"QPushButton#btnVolver {\n"
"    background-color: #2a1e1e;\n"
"    border: 2px solid #ff5252;\n"
"    color: #ff5252;\n"
"}\n"
"\n"
"QPushButton#btnVolver:hover {\n"
"    background-color: #ff5252;\n"
"    color: #000;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    border: 2px solid #2e2e2e;\n"
"    border-radius: 10px;\n"
"    margin-top: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin:"
                        " margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 6px;\n"
"    color: #00c853;\n"
"}\n"
"   ", None))
        self.labelTitulo.setText(QCoreApplication.translate("EstadisticasView", u"Estad\u00edsticas", None))
        self.comboMes.setItemText(0, QCoreApplication.translate("EstadisticasView", u"Enero", None))
        self.comboMes.setItemText(1, QCoreApplication.translate("EstadisticasView", u"Febrero", None))
        self.comboMes.setItemText(2, QCoreApplication.translate("EstadisticasView", u"Marzo", None))
        self.comboMes.setItemText(3, QCoreApplication.translate("EstadisticasView", u"Abril", None))
        self.comboMes.setItemText(4, QCoreApplication.translate("EstadisticasView", u"Mayo", None))
        self.comboMes.setItemText(5, QCoreApplication.translate("EstadisticasView", u"Junio", None))
        self.comboMes.setItemText(6, QCoreApplication.translate("EstadisticasView", u"Julio", None))
        self.comboMes.setItemText(7, QCoreApplication.translate("EstadisticasView", u"Agosto", None))
        self.comboMes.setItemText(8, QCoreApplication.translate("EstadisticasView", u"Septiembre", None))
        self.comboMes.setItemText(9, QCoreApplication.translate("EstadisticasView", u"Octubre", None))
        self.comboMes.setItemText(10, QCoreApplication.translate("EstadisticasView", u"Noviembre", None))
        self.comboMes.setItemText(11, QCoreApplication.translate("EstadisticasView", u"Diciembre", None))

        self.comboAnio.setItemText(0, QCoreApplication.translate("EstadisticasView", u"2020", None))
        self.comboAnio.setItemText(1, QCoreApplication.translate("EstadisticasView", u"2021", None))
        self.comboAnio.setItemText(2, QCoreApplication.translate("EstadisticasView", u"2022", None))
        self.comboAnio.setItemText(3, QCoreApplication.translate("EstadisticasView", u"2023", None))
        self.comboAnio.setItemText(4, QCoreApplication.translate("EstadisticasView", u"2024", None))
        self.comboAnio.setItemText(5, QCoreApplication.translate("EstadisticasView", u"2025", None))
        self.comboAnio.setItemText(6, QCoreApplication.translate("EstadisticasView", u"2026", None))
        self.comboAnio.setItemText(7, QCoreApplication.translate("EstadisticasView", u"2027", None))
        self.comboAnio.setItemText(8, QCoreApplication.translate("EstadisticasView", u"2028", None))
        self.comboAnio.setItemText(9, QCoreApplication.translate("EstadisticasView", u"2029", None))
        self.comboAnio.setItemText(10, QCoreApplication.translate("EstadisticasView", u"2030", None))
        self.comboAnio.setItemText(11, "")

        self.btnFiltrar.setText(QCoreApplication.translate("EstadisticasView", u"Filtrar", None))
        self.btnExportCSV.setText(QCoreApplication.translate("EstadisticasView", u"Exportar CSV", None))
        self.btnExportPDF.setText(QCoreApplication.translate("EstadisticasView", u"Exportar PDF", None))
        self.groupGasto.setTitle(QCoreApplication.translate("EstadisticasView", u"Gasto (\u20ac)", None))
        self.groupConsumo.setTitle(QCoreApplication.translate("EstadisticasView", u"Consumo (L/100km)", None))
        self.btnVolver.setText(QCoreApplication.translate("EstadisticasView", u"Volver", None))
    # retranslateUi

