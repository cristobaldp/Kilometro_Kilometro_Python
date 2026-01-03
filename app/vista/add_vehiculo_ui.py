# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_vehiculo.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_AddVehiculoView(object):
    def setupUi(self, AddVehiculoView):
        if not AddVehiculoView.objectName():
            AddVehiculoView.setObjectName(u"AddVehiculoView")
        AddVehiculoView.resize(440, 600)
        self.vboxLayout = QVBoxLayout(AddVehiculoView)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.labelTitulo = QLabel(AddVehiculoView)
        self.labelTitulo.setObjectName(u"labelTitulo")
        self.labelTitulo.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.labelTitulo.setFont(font)

        self.vboxLayout.addWidget(self.labelTitulo)

        self.comboTipo = QComboBox(AddVehiculoView)
        self.comboTipo.setObjectName(u"comboTipo")

        self.vboxLayout.addWidget(self.comboTipo)

        self.comboMarca = QComboBox(AddVehiculoView)
        self.comboMarca.setObjectName(u"comboMarca")

        self.vboxLayout.addWidget(self.comboMarca)

        self.comboModelo = QComboBox(AddVehiculoView)
        self.comboModelo.setObjectName(u"comboModelo")

        self.vboxLayout.addWidget(self.comboModelo)

        self.inputMatricula = QLineEdit(AddVehiculoView)
        self.inputMatricula.setObjectName(u"inputMatricula")

        self.vboxLayout.addWidget(self.inputMatricula)

        self.spinAnio = QSpinBox(AddVehiculoView)
        self.spinAnio.setObjectName(u"spinAnio")
        self.spinAnio.setMinimum(1950)
        self.spinAnio.setMaximum(2100)
        self.spinAnio.setValue(2020)

        self.vboxLayout.addWidget(self.spinAnio)

        self.comboCombustible = QComboBox(AddVehiculoView)
        self.comboCombustible.addItem("")
        self.comboCombustible.addItem("")
        self.comboCombustible.addItem("")
        self.comboCombustible.addItem("")
        self.comboCombustible.setObjectName(u"comboCombustible")

        self.vboxLayout.addWidget(self.comboCombustible)

        self.spinConsumo = QDoubleSpinBox(AddVehiculoView)
        self.spinConsumo.setObjectName(u"spinConsumo")
        self.spinConsumo.setDecimals(1)
        self.spinConsumo.setMaximum(50.000000000000000)

        self.vboxLayout.addWidget(self.spinConsumo)

        self.labelMensaje = QLabel(AddVehiculoView)
        self.labelMensaje.setObjectName(u"labelMensaje")
        self.labelMensaje.setAlignment(Qt.AlignCenter)
        self.labelMensaje.setVisible(False)

        self.vboxLayout.addWidget(self.labelMensaje)

        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.btnGuardar = QPushButton(AddVehiculoView)
        self.btnGuardar.setObjectName(u"btnGuardar")

        self.hboxLayout.addWidget(self.btnGuardar)

        self.btnCancelar = QPushButton(AddVehiculoView)
        self.btnCancelar.setObjectName(u"btnCancelar")

        self.hboxLayout.addWidget(self.btnCancelar)


        self.vboxLayout.addLayout(self.hboxLayout)


        self.retranslateUi(AddVehiculoView)

        QMetaObject.connectSlotsByName(AddVehiculoView)
    # setupUi

    def retranslateUi(self, AddVehiculoView):
        AddVehiculoView.setWindowTitle(QCoreApplication.translate("AddVehiculoView", u"A\u00f1adir veh\u00edculo", None))
        AddVehiculoView.setStyleSheet(QCoreApplication.translate("AddVehiculoView", u"\n"
"QWidget {\n"
"    background-color: #1b1b1b;\n"
"    color: #eaeaea;\n"
"    font-family: Segoe UI;\n"
"}\n"
"\n"
"QLabel#labelTitulo {\n"
"    color: #00c853;\n"
"}\n"
"\n"
"QLineEdit, QComboBox, QSpinBox, QDoubleSpinBox {\n"
"    background-color: #2a2a2a;\n"
"    border: 2px solid #3a3a3a;\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLineEdit:focus, QComboBox:focus, QSpinBox:focus, QDoubleSpinBox:focus {\n"
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
"QPushButton#btnCancelar {\n"
"    background-color: #2a2a2a;\n"
"    color: #eaeaea;\n"
"    border: 2px solid #3a3a3a;\n"
"}\n"
"\n"
"QLabel#labelMensaje {\n"
"    color: #ff5252;\n"
"}\n"
"   ", None))
        self.labelTitulo.setText(QCoreApplication.translate("AddVehiculoView", u"A\u00f1adir veh\u00edculo", None))
        self.inputMatricula.setPlaceholderText(QCoreApplication.translate("AddVehiculoView", u"Matr\u00edcula", None))
        self.comboCombustible.setItemText(0, QCoreApplication.translate("AddVehiculoView", u"Gasolina", None))
        self.comboCombustible.setItemText(1, QCoreApplication.translate("AddVehiculoView", u"Di\u00e9sel", None))
        self.comboCombustible.setItemText(2, QCoreApplication.translate("AddVehiculoView", u"H\u00edbrido", None))
        self.comboCombustible.setItemText(3, QCoreApplication.translate("AddVehiculoView", u"El\u00e9ctrico", None))

        self.spinConsumo.setSuffix(QCoreApplication.translate("AddVehiculoView", u" L/100km", None))
        self.btnGuardar.setText(QCoreApplication.translate("AddVehiculoView", u"Guardar", None))
        self.btnCancelar.setText(QCoreApplication.translate("AddVehiculoView", u"Cancelar", None))
    # retranslateUi

