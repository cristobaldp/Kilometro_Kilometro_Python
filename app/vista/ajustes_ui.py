# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ajustes.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_AjustesView(object):
    def setupUi(self, AjustesView):
        if not AjustesView.objectName():
            AjustesView.setObjectName(u"AjustesView")
        AjustesView.resize(520, 520)
        self.vboxLayout = QVBoxLayout(AjustesView)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.labelTitulo = QLabel(AjustesView)
        self.labelTitulo.setObjectName(u"labelTitulo")
        self.labelTitulo.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.labelTitulo.setFont(font)

        self.vboxLayout.addWidget(self.labelTitulo)

        self.comboUnidadConsumo = QComboBox(AjustesView)
        self.comboUnidadConsumo.addItem("")
        self.comboUnidadConsumo.addItem("")
        self.comboUnidadConsumo.setObjectName(u"comboUnidadConsumo")

        self.vboxLayout.addWidget(self.comboUnidadConsumo)

        self.comboFormatoPrecio = QComboBox(AjustesView)
        self.comboFormatoPrecio.addItem("")
        self.comboFormatoPrecio.addItem("")
        self.comboFormatoPrecio.setObjectName(u"comboFormatoPrecio")

        self.vboxLayout.addWidget(self.comboFormatoPrecio)

        self.comboPeriodo = QComboBox(AjustesView)
        self.comboPeriodo.addItem("")
        self.comboPeriodo.addItem("")
        self.comboPeriodo.setObjectName(u"comboPeriodo")

        self.vboxLayout.addWidget(self.comboPeriodo)

        self.comboVista = QComboBox(AjustesView)
        self.comboVista.addItem("")
        self.comboVista.addItem("")
        self.comboVista.setObjectName(u"comboVista")

        self.vboxLayout.addWidget(self.comboVista)

        self.spinAvisoKm = QSpinBox(AjustesView)
        self.spinAvisoKm.setObjectName(u"spinAvisoKm")
        self.spinAvisoKm.setMaximum(100000)

        self.vboxLayout.addWidget(self.spinAvisoKm)

        self.checkAvisoConsumo = QCheckBox(AjustesView)
        self.checkAvisoConsumo.setObjectName(u"checkAvisoConsumo")

        self.vboxLayout.addWidget(self.checkAvisoConsumo)

        self.checkConfirmar = QCheckBox(AjustesView)
        self.checkConfirmar.setObjectName(u"checkConfirmar")

        self.vboxLayout.addWidget(self.checkConfirmar)

        self.checkCerrarSesion = QCheckBox(AjustesView)
        self.checkCerrarSesion.setObjectName(u"checkCerrarSesion")

        self.vboxLayout.addWidget(self.checkCerrarSesion)

        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.btnGuardar = QPushButton(AjustesView)
        self.btnGuardar.setObjectName(u"btnGuardar")

        self.hboxLayout.addWidget(self.btnGuardar)

        self.btnVolver = QPushButton(AjustesView)
        self.btnVolver.setObjectName(u"btnVolver")

        self.hboxLayout.addWidget(self.btnVolver)


        self.vboxLayout.addLayout(self.hboxLayout)


        self.retranslateUi(AjustesView)

        QMetaObject.connectSlotsByName(AjustesView)
    # setupUi

    def retranslateUi(self, AjustesView):
        AjustesView.setWindowTitle(QCoreApplication.translate("AjustesView", u"Ajustes", None))
        AjustesView.setStyleSheet(QCoreApplication.translate("AjustesView", u"\n"
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
"QComboBox, QSpinBox {\n"
"    background-color: #1e1e1e;\n"
"    border: 2px solid #2e2e2e;\n"
"    border-radius: 8px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    padding: 4px;\n"
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
"QPushButton#btnVolver {\n"
"    background-color: #2a1e1e;\n"
"    color: #ff5252;\n"
"}\n"
"   ", None))
        self.labelTitulo.setText(QCoreApplication.translate("AjustesView", u"Ajustes y preferencias", None))
        self.comboUnidadConsumo.setItemText(0, QCoreApplication.translate("AjustesView", u"L/100km", None))
        self.comboUnidadConsumo.setItemText(1, QCoreApplication.translate("AjustesView", u"km/L", None))

        self.comboFormatoPrecio.setItemText(0, QCoreApplication.translate("AjustesView", u"\u20ac", None))
        self.comboFormatoPrecio.setItemText(1, QCoreApplication.translate("AjustesView", u"$", None))

        self.comboPeriodo.setItemText(0, QCoreApplication.translate("AjustesView", u"Mensual", None))
        self.comboPeriodo.setItemText(1, QCoreApplication.translate("AjustesView", u"Anual", None))

        self.comboVista.setItemText(0, QCoreApplication.translate("AjustesView", u"lista", None))
        self.comboVista.setItemText(1, QCoreApplication.translate("AjustesView", u"grafica", None))

        self.checkAvisoConsumo.setText(QCoreApplication.translate("AjustesView", u"Avisar por consumo alto", None))
        self.checkConfirmar.setText(QCoreApplication.translate("AjustesView", u"Confirmar acciones importantes", None))
        self.checkCerrarSesion.setText(QCoreApplication.translate("AjustesView", u"Cerrar sesi\u00f3n al salir", None))
        self.btnGuardar.setText(QCoreApplication.translate("AjustesView", u"Guardar", None))
        self.btnVolver.setText(QCoreApplication.translate("AjustesView", u"Volver", None))
    # retranslateUi

