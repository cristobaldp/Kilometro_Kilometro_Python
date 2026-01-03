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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_EstadisticasView(object):
    def setupUi(self, EstadisticasView):
        if not EstadisticasView.objectName():
            EstadisticasView.setObjectName(u"EstadisticasView")
        EstadisticasView.resize(900, 650)
        self.vboxLayout = QVBoxLayout(EstadisticasView)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.labelTitulo = QLabel(EstadisticasView)
        self.labelTitulo.setObjectName(u"labelTitulo")
        self.labelTitulo.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.labelTitulo.setFont(font)

        self.vboxLayout.addWidget(self.labelTitulo)

        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.comboMes = QComboBox(EstadisticasView)
        self.comboMes.setObjectName(u"comboMes")

        self.hboxLayout.addWidget(self.comboMes)

        self.comboAnio = QComboBox(EstadisticasView)
        self.comboAnio.setObjectName(u"comboAnio")

        self.hboxLayout.addWidget(self.comboAnio)

        self.btnFiltrar = QPushButton(EstadisticasView)
        self.btnFiltrar.setObjectName(u"btnFiltrar")

        self.hboxLayout.addWidget(self.btnFiltrar)


        self.vboxLayout.addLayout(self.hboxLayout)

        self.frame = QFrame(EstadisticasView)
        self.frame.setObjectName(u"frame")
        self.layoutGasto = QVBoxLayout(self.frame)
        self.layoutGasto.setObjectName(u"layoutGasto")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.layoutGasto.addWidget(self.label)


        self.vboxLayout.addWidget(self.frame)

        self.frame1 = QFrame(EstadisticasView)
        self.frame1.setObjectName(u"frame1")
        self.layoutConsumo = QVBoxLayout(self.frame1)
        self.layoutConsumo.setObjectName(u"layoutConsumo")
        self.label1 = QLabel(self.frame1)
        self.label1.setObjectName(u"label1")

        self.layoutConsumo.addWidget(self.label1)


        self.vboxLayout.addWidget(self.frame1)

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
"    color: #000000;\n"
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
"    color: #000000;\n"
"}\n"
"\n"
"QFrame {\n"
"    background-color: #1e1e1e;\n"
"    border-radius: 12px;\n"
"    padding: 10px;\n"
"}\n"
"   ", None))
        self.labelTitulo.setText(QCoreApplication.translate("EstadisticasView", u"Estad\u00edsticas", None))
        self.btnFiltrar.setText(QCoreApplication.translate("EstadisticasView", u"Filtrar", None))
        self.label.setText(QCoreApplication.translate("EstadisticasView", u"Gasto (\u20ac)", None))
        self.label1.setText(QCoreApplication.translate("EstadisticasView", u"Consumo (L/100km)", None))
        self.btnVolver.setText(QCoreApplication.translate("EstadisticasView", u"Volver", None))
    # retranslateUi

