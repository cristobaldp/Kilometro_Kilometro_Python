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
        MenuPrincipalView.setStyleSheet(u"QWidget {\n"
"    background-color: #081c20;\n"
"}\n"
"/* ===============================\n"
"   MENSAJES DIN\u00c1MICOS\n"
"=============================== */\n"
"\n"
"QLabel#mensajeError {\n"
"    color: #fbbf24;   /* \u00e1mbar */\n"
"    font-size: 13px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QLabel#mensajeInfo {\n"
"    color: #38bdf8;   /* azul */\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QLabel#mensajeOk {\n"
"    color: #4ade80;   /* verde suave */\n"
"    font-size: 13px;\n"
"}\n"
"")
        self.vboxLayout = QVBoxLayout(MenuPrincipalView)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.labelTitulo = QLabel(MenuPrincipalView)
        self.labelTitulo.setObjectName(u"labelTitulo")
        font = QFont()
        font.setBold(True)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setStyleSheet(u"/* =========================================\n"
"   LABELS \u2013 AZUL PETR\u00d3LEO OSCURO\n"
"========================================= */\n"
"\n"
"/* Label normal (texto est\u00e1ndar) */\n"
"QLabel {\n"
"    color: #cfe9ee;              /* azul muy claro */\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"/* T\u00edtulos de secci\u00f3n / pantallas */\n"
"QLabel#titulo {\n"
"    color: #22d3ee;              /* cyan petr\u00f3leo */\n"
"    font-size: 22px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"/* Subt\u00edtulos */\n"
"QLabel#subtitulo {\n"
"    color: #7dd3fc;\n"
"    font-size: 16px;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"/* Labels de formulario (Usuario, Contrase\u00f1a, etc.) */\n"
"QLabel#campo {\n"
"    color: #9ddae6;\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"/* Texto secundario / ayuda */\n"
"QLabel#hint {\n"
"    color: #6fbdd0;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"/* Avisos / combustible / warning */\n"
"QLabel#warning {\n"
"    color: #fbbf24;              /* \u00e1mbar */"
                        "\n"
"    font-size: 13px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"/* Error */\n"
"QLabel#error {\n"
"    color: #fb7185;              /* rojo suave */\n"
"    font-size: 13px;\n"
"    font-weight: 600;\n"
"}\n"
"/* =========================================\n"
"   MENSAJES DE ERROR \u2013 ESTILO PROPIO\n"
"========================================= */\n"
"\n"
"QLabel#error {\n"
"    color: #fbbf24;          /* \u00e1mbar visible */\n"
"    font-size: 13px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"")
        self.labelTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout.addWidget(self.labelTitulo)

        self.labelSubtitulo = QLabel(MenuPrincipalView)
        self.labelSubtitulo.setObjectName(u"labelSubtitulo")
        self.labelSubtitulo.setStyleSheet(u"/* =========================================\n"
"   LABELS \u2013 AZUL PETR\u00d3LEO OSCURO\n"
"========================================= */\n"
"\n"
"/* Label normal (texto est\u00e1ndar) */\n"
"QLabel {\n"
"    color: #cfe9ee;              /* azul muy claro */\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"/* T\u00edtulos de secci\u00f3n / pantallas */\n"
"QLabel#titulo {\n"
"    color: #22d3ee;              /* cyan petr\u00f3leo */\n"
"    font-size: 22px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"/* Subt\u00edtulos */\n"
"QLabel#subtitulo {\n"
"    color: #7dd3fc;\n"
"    font-size: 16px;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"/* Labels de formulario (Usuario, Contrase\u00f1a, etc.) */\n"
"QLabel#campo {\n"
"    color: #9ddae6;\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"/* Texto secundario / ayuda */\n"
"QLabel#hint {\n"
"    color: #6fbdd0;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"/* Avisos / combustible / warning */\n"
"QLabel#warning {\n"
"    color: #fbbf24;              /* \u00e1mbar */"
                        "\n"
"    font-size: 13px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"/* Error */\n"
"QLabel#error {\n"
"    color: #fb7185;              /* rojo suave */\n"
"    font-size: 13px;\n"
"    font-weight: 600;\n"
"}\n"
"/* =========================================\n"
"   MENSAJES DE ERROR \u2013 ESTILO PROPIO\n"
"========================================= */\n"
"\n"
"QLabel#error {\n"
"    color: #fbbf24;          /* \u00e1mbar visible */\n"
"    font-size: 13px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"")
        self.labelSubtitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout.addWidget(self.labelSubtitulo)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnVehiculos = QPushButton(MenuPrincipalView)
        self.btnVehiculos.setObjectName(u"btnVehiculos")
        self.btnVehiculos.setStyleSheet(u"/* =========================================\n"
"   BOT\u00d3N ALTERNATIVO \u2013 BLANCO AZULADO\n"
"========================================= */\n"
"\n"
"QPushButton {\n"
"    background-color: #f1f5f9;      /* blanco azulado suave */\n"
"    color: #0f3a43;                 /* azul petr\u00f3leo oscuro */\n"
"\n"
"    border: 1px solid #22d3ee;\n"
"    border-radius: 12px;\n"
"\n"
"    padding: 10px 18px;\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"/* Hover */\n"
"QPushButton:hover {\n"
"    background-color: #e0f2fe;      /* azul muy claro */\n"
"    color: #0b2a30;\n"
"    border-color: #22d3ee;\n"
"}\n"
"\n"
"/* Presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #bae6fd;\n"
"    border-color: #06b6d4;\n"
"}\n"
"\n"
"/* Desactivado */\n"
"QPushButton:disabled {\n"
"    background-color: #e5e7eb;\n"
"    color: #64748b;\n"
"    border-color: #94a3b8;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btnVehiculos, 0, 0, 1, 1)

        self.btnRepostajes = QPushButton(MenuPrincipalView)
        self.btnRepostajes.setObjectName(u"btnRepostajes")
        self.btnRepostajes.setStyleSheet(u"/* =========================================\n"
"   BOT\u00d3N ALTERNATIVO \u2013 BLANCO AZULADO\n"
"========================================= */\n"
"\n"
"QPushButton {\n"
"    background-color: #f1f5f9;      /* blanco azulado suave */\n"
"    color: #0f3a43;                 /* azul petr\u00f3leo oscuro */\n"
"\n"
"    border: 1px solid #22d3ee;\n"
"    border-radius: 12px;\n"
"\n"
"    padding: 10px 18px;\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"/* Hover */\n"
"QPushButton:hover {\n"
"    background-color: #e0f2fe;      /* azul muy claro */\n"
"    color: #0b2a30;\n"
"    border-color: #22d3ee;\n"
"}\n"
"\n"
"/* Presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #bae6fd;\n"
"    border-color: #06b6d4;\n"
"}\n"
"\n"
"/* Desactivado */\n"
"QPushButton:disabled {\n"
"    background-color: #e5e7eb;\n"
"    color: #64748b;\n"
"    border-color: #94a3b8;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btnRepostajes, 0, 1, 1, 1)

        self.btnEstadisticas = QPushButton(MenuPrincipalView)
        self.btnEstadisticas.setObjectName(u"btnEstadisticas")
        self.btnEstadisticas.setStyleSheet(u"/* =========================================\n"
"   BOT\u00d3N ALTERNATIVO \u2013 BLANCO AZULADO\n"
"========================================= */\n"
"\n"
"QPushButton {\n"
"    background-color: #f1f5f9;      /* blanco azulado suave */\n"
"    color: #0f3a43;                 /* azul petr\u00f3leo oscuro */\n"
"\n"
"    border: 1px solid #22d3ee;\n"
"    border-radius: 12px;\n"
"\n"
"    padding: 10px 18px;\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"/* Hover */\n"
"QPushButton:hover {\n"
"    background-color: #e0f2fe;      /* azul muy claro */\n"
"    color: #0b2a30;\n"
"    border-color: #22d3ee;\n"
"}\n"
"\n"
"/* Presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #bae6fd;\n"
"    border-color: #06b6d4;\n"
"}\n"
"\n"
"/* Desactivado */\n"
"QPushButton:disabled {\n"
"    background-color: #e5e7eb;\n"
"    color: #64748b;\n"
"    border-color: #94a3b8;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btnEstadisticas, 1, 0, 1, 1)

        self.btnPerfil = QPushButton(MenuPrincipalView)
        self.btnPerfil.setObjectName(u"btnPerfil")
        self.btnPerfil.setStyleSheet(u"/* =========================================\n"
"   BOT\u00d3N ALTERNATIVO \u2013 BLANCO AZULADO\n"
"========================================= */\n"
"\n"
"QPushButton {\n"
"    background-color: #f1f5f9;      /* blanco azulado suave */\n"
"    color: #0f3a43;                 /* azul petr\u00f3leo oscuro */\n"
"\n"
"    border: 1px solid #22d3ee;\n"
"    border-radius: 12px;\n"
"\n"
"    padding: 10px 18px;\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"/* Hover */\n"
"QPushButton:hover {\n"
"    background-color: #e0f2fe;      /* azul muy claro */\n"
"    color: #0b2a30;\n"
"    border-color: #22d3ee;\n"
"}\n"
"\n"
"/* Presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #bae6fd;\n"
"    border-color: #06b6d4;\n"
"}\n"
"\n"
"/* Desactivado */\n"
"QPushButton:disabled {\n"
"    background-color: #e5e7eb;\n"
"    color: #64748b;\n"
"    border-color: #94a3b8;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btnPerfil, 1, 1, 1, 1)

        self.btnMapa = QPushButton(MenuPrincipalView)
        self.btnMapa.setObjectName(u"btnMapa")
        self.btnMapa.setStyleSheet(u"/* =========================================\n"
"   BOT\u00d3N ALTERNATIVO \u2013 BLANCO AZULADO\n"
"========================================= */\n"
"\n"
"QPushButton {\n"
"    background-color: #f1f5f9;      /* blanco azulado suave */\n"
"    color: #0f3a43;                 /* azul petr\u00f3leo oscuro */\n"
"\n"
"    border: 1px solid #22d3ee;\n"
"    border-radius: 12px;\n"
"\n"
"    padding: 20px 18px;\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"/* Hover */\n"
"QPushButton:hover {\n"
"    background-color: #e0f2fe;      /* azul muy claro */\n"
"    color: #0b2a30;\n"
"    border-color: #22d3ee;\n"
"}\n"
"\n"
"/* Presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #bae6fd;\n"
"    border-color: #06b6d4;\n"
"}\n"
"\n"
"/* Desactivado */\n"
"QPushButton:disabled {\n"
"    background-color: #e5e7eb;\n"
"    color: #64748b;\n"
"    border-color: #94a3b8;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btnMapa, 2, 0, 1, 1)

        self.btnLogout = QPushButton(MenuPrincipalView)
        self.btnLogout.setObjectName(u"btnLogout")
        self.btnLogout.setStyleSheet(u"/* =========================================\n"
"   BOT\u00d3N ALTERNATIVO \u2013 BLANCO AZULADO\n"
"========================================= */\n"
"\n"
"QPushButton {\n"
"    background-color: #f1f5f9;      /* blanco azulado suave */\n"
"    color: #0f3a43;                 /* azul petr\u00f3leo oscuro */\n"
"\n"
"    border: 1px solid #22d3ee;\n"
"    border-radius: 12px;\n"
"\n"
"    padding: 20px 18px;\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"/* Hover */\n"
"QPushButton:hover {\n"
"    background-color: #e0f2fe;      /* azul muy claro */\n"
"    color: #0b2a30;\n"
"    border-color: #22d3ee;\n"
"}\n"
"\n"
"/* Presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #bae6fd;\n"
"    border-color: #06b6d4;\n"
"}\n"
"\n"
"/* Desactivado */\n"
"QPushButton:disabled {\n"
"    background-color: #e5e7eb;\n"
"    color: #64748b;\n"
"    border-color: #94a3b8;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btnLogout, 2, 1, 1, 1)


        self.vboxLayout.addLayout(self.gridLayout)


        self.retranslateUi(MenuPrincipalView)

        QMetaObject.connectSlotsByName(MenuPrincipalView)
    # setupUi

    def retranslateUi(self, MenuPrincipalView):
        MenuPrincipalView.setWindowTitle(QCoreApplication.translate("MenuPrincipalView", u"Kil\u00f3metro a Kil\u00f3metro", None))
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
        self.btnMapa.setText(QCoreApplication.translate("MenuPrincipalView", u"Mapa de Gasolineras", None))
        self.btnLogout.setText(QCoreApplication.translate("MenuPrincipalView", u"Cerrar sesi\u00f3n", None))
    # retranslateUi

