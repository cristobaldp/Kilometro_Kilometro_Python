# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vehiculos.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_VehiculosView(object):
    def setupUi(self, VehiculosView):
        if not VehiculosView.objectName():
            VehiculosView.setObjectName(u"VehiculosView")
        VehiculosView.resize(946, 572)
        self.vboxLayout = QVBoxLayout(VehiculosView)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.labelTitulo = QLabel(VehiculosView)
        self.labelTitulo.setObjectName(u"labelTitulo")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(22)
        font.setBold(True)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout.addWidget(self.labelTitulo)

        self.labelSubtitulo = QLabel(VehiculosView)
        self.labelSubtitulo.setObjectName(u"labelSubtitulo")
        self.labelSubtitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout.addWidget(self.labelSubtitulo)

        self.tablaVehiculos = QTableWidget(VehiculosView)
        if (self.tablaVehiculos.columnCount() < 7):
            self.tablaVehiculos.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablaVehiculos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablaVehiculos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablaVehiculos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tablaVehiculos.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tablaVehiculos.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tablaVehiculos.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tablaVehiculos.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tablaVehiculos.setObjectName(u"tablaVehiculos")
        self.tablaVehiculos.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tablaVehiculos.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tablaVehiculos.setColumnCount(7)

        self.vboxLayout.addWidget(self.tablaVehiculos)

        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.btnVolver = QPushButton(VehiculosView)
        self.btnVolver.setObjectName(u"btnVolver")

        self.hboxLayout.addWidget(self.btnVolver)

        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout.addItem(self.horizontalSpacer)

        self.btnSetActivo = QPushButton(VehiculosView)
        self.btnSetActivo.setObjectName(u"btnSetActivo")

        self.hboxLayout.addWidget(self.btnSetActivo)

        self.btnEliminar = QPushButton(VehiculosView)
        self.btnEliminar.setObjectName(u"btnEliminar")

        self.hboxLayout.addWidget(self.btnEliminar)

        self.btnAddVehiculo = QPushButton(VehiculosView)
        self.btnAddVehiculo.setObjectName(u"btnAddVehiculo")

        self.hboxLayout.addWidget(self.btnAddVehiculo)


        self.vboxLayout.addLayout(self.hboxLayout)


        self.retranslateUi(VehiculosView)

        QMetaObject.connectSlotsByName(VehiculosView)
    # setupUi

    def retranslateUi(self, VehiculosView):
        VehiculosView.setWindowTitle(QCoreApplication.translate("VehiculosView", u"Mis veh\u00edculos", None))
        VehiculosView.setStyleSheet(QCoreApplication.translate("VehiculosView", u"\n"
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
"QLabel#labelSubtitulo {\n"
"    color: #9e9e9e;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: #1e1e1e;\n"
"    border: 2px solid #2e2e2e;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #2a2a2a;\n"
"    padding: 8px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #00c853;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #00c853;\n"
"    border-radius: 10px;\n"
"    padding: 10px 18px;\n"
"    font-weight: bold;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #00e676;\n"
"}\n"
"\n"
"QPushButton#btnSetActivo {\n"
"    background-color: #1e1e1e;\n"
"    border: 2px solid #00c853;\n"
"    color: #00c853;\n"
"}\n"
"\n"
"QPushButton#btnSetActivo:hover {\n"
"    backgrou"
                        "nd-color: #00c853;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QPushButton#btnEliminar {\n"
"    background-color: #2a1e1e;\n"
"    border: 2px solid #ff5252;\n"
"    color: #ff5252;\n"
"}\n"
"\n"
"QPushButton#btnEliminar:hover {\n"
"    background-color: #ff5252;\n"
"    color: #000000;\n"
"}\n"
"   ", None))
        self.labelTitulo.setText(QCoreApplication.translate("VehiculosView", u"Mis veh\u00edculos", None))
        self.labelSubtitulo.setText(QCoreApplication.translate("VehiculosView", u"Selecciona el veh\u00edculo activo", None))
        ___qtablewidgetitem = self.tablaVehiculos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("VehiculosView", u"Activo", None));
        ___qtablewidgetitem1 = self.tablaVehiculos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("VehiculosView", u"Tipo", None));
        ___qtablewidgetitem2 = self.tablaVehiculos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("VehiculosView", u"Marca", None));
        ___qtablewidgetitem3 = self.tablaVehiculos.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("VehiculosView", u"Modelo", None));
        ___qtablewidgetitem4 = self.tablaVehiculos.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("VehiculosView", u"Matr\u00edcula", None));
        ___qtablewidgetitem5 = self.tablaVehiculos.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("VehiculosView", u"Combustible", None));
        ___qtablewidgetitem6 = self.tablaVehiculos.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("VehiculosView", u"Consumo", None));
        self.btnVolver.setText(QCoreApplication.translate("VehiculosView", u"Volver", None))
        self.btnSetActivo.setText(QCoreApplication.translate("VehiculosView", u"\u2714Marcar como activo", None))
        self.btnEliminar.setText(QCoreApplication.translate("VehiculosView", u"Eliminar", None))
        self.btnAddVehiculo.setText(QCoreApplication.translate("VehiculosView", u"\u2795A\u00f1adir veh\u00edculo", None))
    # retranslateUi

