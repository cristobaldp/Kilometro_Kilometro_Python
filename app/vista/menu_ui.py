# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
class Ui_MenuPrincipalView(object):
    def setupUi(self, MenuPrincipalView):
        if not MenuPrincipalView.objectName():
            MenuPrincipalView.setObjectName(u"MenuPrincipalView")
        MenuPrincipalView.resize(900, 550)
        self.vboxLayout = QVBoxLayout(MenuPrincipalView)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.labelTitulo = QLabel(MenuPrincipalView)
        self.labelTitulo.setObjectName(u"labelTitulo")
        self.labelTitulo.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.labelTitulo.setFont(font)

        self.vboxLayout.addWidget(self.labelTitulo)

        self.labelSubtitulo = QLabel(MenuPrincipalView)
        self.labelSubtitulo.setObjectName(u"labelSubtitulo")
        self.labelSubtitulo.setAlignment(Qt.AlignCenter)

        self.vboxLayout.addWidget(self.labelSubtitulo)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnVehiculos = QPushButton(MenuPrincipalView)
        self.btnVehiculos.setObjectName(u"btnVehiculos")

        self.gridLayout.addWidget(self.btnVehiculos, 0, 0, 1, 1)

        self.btnRepostajes = QPushButton(MenuPrincipalView)
        self.btnRepostajes.setObjectName(u"btnRepostajes")

        self.gridLayout.addWidget(self.btnRepostajes, 0, 1, 1, 1)

        self.btnEstadisticas = QPushButton(MenuPrincipalView)
        self.btnEstadisticas.setObjectName(u"btnEstadisticas")

        self.gridLayout.addWidget(self.btnEstadisticas, 1, 0, 1, 1)

        self.btnPerfil = QPushButton(MenuPrincipalView)
        self.btnPerfil.setObjectName(u"btnPerfil")

        self.gridLayout.addWidget(self.btnPerfil, 1, 1, 1, 1)

        self.btnAjustes = QPushButton(MenuPrincipalView)
        self.btnAjustes.setObjectName(u"btnAjustes")

        self.gridLayout.addWidget(self.btnAjustes, 2, 0, 1, 1)

        self.btnLogout = QPushButton(MenuPrincipalView)
        self.btnLogout.setObjectName(u"btnLogout")

        self.gridLayout.addWidget(self.btnLogout, 2, 1, 1, 1)


        self.vboxLayout.addLayout(self.gridLayout)


        self.retranslateUi(MenuPrincipalView)

        QMetaObject.connectSlotsByName(MenuPrincipalView)
    # setupUi

    def retranslateUi(self, MenuPrincipalView):
        MenuPrincipalView.setWindowTitle(QCoreApplication.translate("MenuPrincipalView", u"Kil\u00f3metro a Kil\u00f3metro", None))
        MenuPrincipalView.setStyleSheet(QCoreApplication.translate("MenuPrincipalView", u"\n"
"    QWidget {\n"
"        background-color: #121212;\n"
"        color: #eaeaea;\n"
"        font-family: Segoe UI;\n"
"    }\n"
"\n"
"    QLabel#labelTitulo {\n"
"        color: #00c853;\n"
"    }\n"
"\n"
"    QLabel#labelSubtitulo {\n"
"        color: #9e9e9e;\n"
"    }\n"
"\n"
"    QPushButton {\n"
"        background-color: #1e1e1e;\n"
"        border: 2px solid #2e2e2e;\n"
"        border-radius: 14px;\n"
"        padding: 20px;\n"
"        font-size: 15px;\n"
"        font-weight: bold;\n"
"        text-align: left;\n"
"    }\n"
"\n"
"    QPushButton:hover {\n"
"        background-color: #1e2e24;\n"
"        border: 2px solid #00c853;\n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: #00c853;\n"
"        color: #000000;\n"
"    }\n"
"\n"
"    QPushButton#btnLogout {\n"
"        background-color: #2a1e1e;\n"
"        border: 2px solid #ff5252;\n"
"        color: #ff5252;\n"
"    }\n"
"\n"
"    QPushButton#btnLogout:hover {\n"
"        background-color: #ff5252;\n"
"        co"
                        "lor: #000000;\n"
"    }\n"
"   ", None))
        self.labelTitulo.setText(QCoreApplication.translate("MenuPrincipalView", u"Kil\u00f3metro a Kil\u00f3metro", None))
        self.labelSubtitulo.setText(QCoreApplication.translate("MenuPrincipalView", u"Control de consumo, gastos y kilometraje", None))
        self.btnVehiculos.setText(QCoreApplication.translate("MenuPrincipalView", u"Veh\u00edculos\n"
"Gestiona tus coches", None))
        self.btnRepostajes.setText(QCoreApplication.translate("MenuPrincipalView", u"Repostajes\n"
"Control de combustible", None))
        self.btnEstadisticas.setText(QCoreApplication.translate("MenuPrincipalView", u"Estad\u00edsticas\n"
"Consumo y gasto", None))
        self.btnPerfil.setText(QCoreApplication.translate("MenuPrincipalView", u"Perfil\n"
"Datos del usuario", None))
        self.btnAjustes.setText(QCoreApplication.translate("MenuPrincipalView", u"Ajustes\n"
"Preferencias", None))
        self.btnLogout.setText(QCoreApplication.translate("MenuPrincipalView", u"Cerrar sesi\u00f3n", None))
    # retranslateUi

