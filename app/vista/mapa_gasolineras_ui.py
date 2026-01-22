# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mapa_gasolineras.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MapaGasolineras(object):
    def setupUi(self, MapaGasolineras):
        if not MapaGasolineras.objectName():
            MapaGasolineras.setObjectName(u"MapaGasolineras")
        MapaGasolineras.resize(1000, 697)
        MapaGasolineras.setStyleSheet(u"QWidget {\n"
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
        self.verticalLayout = QVBoxLayout(MapaGasolineras)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mapaWidget = QFrame(MapaGasolineras)
        self.mapaWidget.setObjectName(u"mapaWidget")
        self.mapaWidget.setMinimumSize(QSize(0, 500))
        self.mapaWidget.setFrameShape(QFrame.Shape.StyledPanel)
        self.mapaWidget.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.mapaWidget)

        self.btnVolver = QPushButton(MapaGasolineras)
        self.btnVolver.setObjectName(u"btnVolver")
        self.btnVolver.setStyleSheet(u"/* =========================================\n"
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

        self.verticalLayout.addWidget(self.btnVolver)


        self.retranslateUi(MapaGasolineras)

        QMetaObject.connectSlotsByName(MapaGasolineras)
    # setupUi

    def retranslateUi(self, MapaGasolineras):
        MapaGasolineras.setWindowTitle(QCoreApplication.translate("MapaGasolineras", u"Mapa de gasolineras", None))
        self.btnVolver.setText(QCoreApplication.translate("MapaGasolineras", u"Volver", None))
    # retranslateUi

