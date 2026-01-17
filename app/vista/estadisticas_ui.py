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
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_EstadisticasView(object):
    def setupUi(self, EstadisticasView):
        if not EstadisticasView.objectName():
            EstadisticasView.setObjectName(u"EstadisticasView")
        EstadisticasView.resize(1000, 900)
        self.verticalLayout = QVBoxLayout(EstadisticasView)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.labelTitulo = QLabel(EstadisticasView)
        self.labelTitulo.setObjectName(u"labelTitulo")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(24)
        font.setBold(True)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelTitulo.setMinimumHeight(50)

        self.verticalLayout.addWidget(self.labelTitulo)

        self.horizontalLayoutFiltros = QHBoxLayout()
        self.horizontalLayoutFiltros.setSpacing(10)
        self.horizontalLayoutFiltros.setObjectName(u"horizontalLayoutFiltros")
        self.labelMes = QLabel(EstadisticasView)
        self.labelMes.setObjectName(u"labelMes")
        self.labelMes.setMinimumWidth(40)

        self.horizontalLayoutFiltros.addWidget(self.labelMes)

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
        self.comboMes.setMinimumWidth(150)

        self.horizontalLayoutFiltros.addWidget(self.comboMes)

        self.horizontalSpacer1 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutFiltros.addItem(self.horizontalSpacer1)

        self.labelAnio = QLabel(EstadisticasView)
        self.labelAnio.setObjectName(u"labelAnio")
        self.labelAnio.setMinimumWidth(40)

        self.horizontalLayoutFiltros.addWidget(self.labelAnio)

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
        self.comboAnio.setObjectName(u"comboAnio")
        self.comboAnio.setMinimumWidth(120)

        self.horizontalLayoutFiltros.addWidget(self.comboAnio)

        self.horizontalSpacer2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutFiltros.addItem(self.horizontalSpacer2)

        self.btnFiltrar = QPushButton(EstadisticasView)
        self.btnFiltrar.setObjectName(u"btnFiltrar")
        self.btnFiltrar.setMinimumWidth(150)

        self.horizontalLayoutFiltros.addWidget(self.btnFiltrar)


        self.verticalLayout.addLayout(self.horizontalLayoutFiltros)

        self.horizontalLayoutExport = QHBoxLayout()
        self.horizontalLayoutExport.setSpacing(10)
        self.horizontalLayoutExport.setObjectName(u"horizontalLayoutExport")
        self.btnExportCSV = QPushButton(EstadisticasView)
        self.btnExportCSV.setObjectName(u"btnExportCSV")
        self.btnExportCSV.setMinimumHeight(40)

        self.horizontalLayoutExport.addWidget(self.btnExportCSV)

        self.btnExportPDF = QPushButton(EstadisticasView)
        self.btnExportPDF.setObjectName(u"btnExportPDF")
        self.btnExportPDF.setMinimumHeight(40)

        self.horizontalLayoutExport.addWidget(self.btnExportPDF)


        self.verticalLayout.addLayout(self.horizontalLayoutExport)

        self.groupGasto = QGroupBox(EstadisticasView)
        self.groupGasto.setObjectName(u"groupGasto")
        self.groupGasto.setMinimumHeight(300)
        self.layoutGasto = QVBoxLayout(self.groupGasto)
        self.layoutGasto.setSpacing(0)
        self.layoutGasto.setObjectName(u"layoutGasto")
        self.layoutGasto.setContentsMargins(5, 5, 5, 5)

        self.verticalLayout.addWidget(self.groupGasto)

        self.groupConsumo = QGroupBox(EstadisticasView)
        self.groupConsumo.setObjectName(u"groupConsumo")
        self.groupConsumo.setMinimumHeight(300)
        self.layoutConsumo = QVBoxLayout(self.groupConsumo)
        self.layoutConsumo.setSpacing(0)
        self.layoutConsumo.setObjectName(u"layoutConsumo")
        self.layoutConsumo.setContentsMargins(5, 5, 5, 5)

        self.verticalLayout.addWidget(self.groupConsumo)

        self.btnVolver = QPushButton(EstadisticasView)
        self.btnVolver.setObjectName(u"btnVolver")
        self.btnVolver.setMinimumHeight(45)

        self.verticalLayout.addWidget(self.btnVolver)


        self.retranslateUi(EstadisticasView)

        QMetaObject.connectSlotsByName(EstadisticasView)
    # setupUi

    def retranslateUi(self, EstadisticasView):
        EstadisticasView.setWindowTitle(QCoreApplication.translate("EstadisticasView", u"Estad\u00edsticas Avanzadas", None))
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
"    padding: 8px;\n"
"    min-height: 30px;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #00c853;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    border-left: 5px solid transparent;\n"
"    border-right: 5px solid transparent;\n"
"    border-top: 5px solid #00c853;\n"
"    margin-right: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #eaeaea;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #00c853;\n"
"    border-radius: 10px;\n"
"    padding: 12px 20px;\n"
"    font-weight: bold;\n"
"    color: #000;\n"
"    min-height: 35px;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    backgro"
                        "und-color: #00e676;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #00a845;\n"
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
"QPushButton#btnExportPDF, QPushButton#btnExportCSV {\n"
"    background-color: #1e1e2e;\n"
"    border: 2px solid #4fc3f7;\n"
"    color: #4fc3f7;\n"
"}\n"
"\n"
"QPushButton#btnExportPDF:hover, QPushButton#btnExportCSV:hover {\n"
"    background-color: #4fc3f7;\n"
"    color: #000;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    border: 2px solid #2e2e2e;\n"
"    border-radius: 12px;\n"
"    margin-top: 15px;\n"
"    padding-top: 20px;\n"
"    background-color: #1a1a1a;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 5px 10px;\n"
"    color: #00c853;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
""
                        "QScrollArea {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"   ", None))
        self.labelTitulo.setText(QCoreApplication.translate("EstadisticasView", u" Estad\u00edsticas Avanzadas", None))
        self.labelMes.setText(QCoreApplication.translate("EstadisticasView", u"Mes:", None))
        self.labelMes.setStyleSheet(QCoreApplication.translate("EstadisticasView", u"font-size: 13px; font-weight: bold; color: #00c853;", None))
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

        self.labelAnio.setText(QCoreApplication.translate("EstadisticasView", u"A\u00f1o:", None))
        self.labelAnio.setStyleSheet(QCoreApplication.translate("EstadisticasView", u"font-size: 13px; font-weight: bold; color: #00c853;", None))
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

        self.btnFiltrar.setText(QCoreApplication.translate("EstadisticasView", u" Filtrar", None))
        self.btnExportCSV.setText(QCoreApplication.translate("EstadisticasView", u" Exportar CSV", None))
        self.btnExportPDF.setText(QCoreApplication.translate("EstadisticasView", u" Exportar PDF", None))
        self.groupGasto.setTitle(QCoreApplication.translate("EstadisticasView", u"Gasto Diario (\u20ac)", None))
        self.groupConsumo.setTitle(QCoreApplication.translate("EstadisticasView", u" Consumo (L/100km)", None))
        self.btnVolver.setText(QCoreApplication.translate("EstadisticasView", u"\u2190 Volver al Men\u00fa", None))
    # retranslateUi

