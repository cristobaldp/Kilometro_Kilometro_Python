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
        EstadisticasView.resize(1000, 954)
        EstadisticasView.setStyleSheet(u"QWidget {\n"
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
        self.verticalLayout = QVBoxLayout(EstadisticasView)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.labelTitulo = QLabel(EstadisticasView)
        self.labelTitulo.setObjectName(u"labelTitulo")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
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

        self.verticalLayout.addWidget(self.labelTitulo)

        self.horizontalLayoutFiltros = QHBoxLayout()
        self.horizontalLayoutFiltros.setSpacing(10)
        self.horizontalLayoutFiltros.setObjectName(u"horizontalLayoutFiltros")
        self.labelMes = QLabel(EstadisticasView)
        self.labelMes.setObjectName(u"labelMes")
        self.labelMes.setStyleSheet(u"/* =========================================\n"
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
        self.comboMes.setStyleSheet(u"QComboBox {\n"
"    background-color: #0f3a43;\n"
"    color: #ecfeff;\n"
"    border: 1px solid #1f6f7a;\n"
"    border-radius: 12px;\n"
"\n"
"    padding: 2px 8px;          /* \u2b05\ufe0f 1px menos */\n"
"    padding-right: 32px;\n"
"\n"
"    font-size: 12px;\n"
"    min-height: 34px;           /* \u2b05\ufe0f antes 38 */\n"
"}\n"
"\n"
"/* =========================================\n"
"   COMBOBOX \u2013 DESPLEGABLE AJUSTADO A ESTE TAMA\u00d1O\n"
"========================================= */\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: content;\n"
"    subcontrol-position: right center;\n"
"    width: 28px;\n"
"    border-left: 1px solid #1f6f7a;\n"
"}\n"
"\n"
"/* Quitamos la flecha por est\u00e9tica */\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"}\n"
"\n"
"/* Lista desplegable */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #0b2a30;\n"
"    color: #cfe9ee;\n"
"\n"
"    border: 1px solid #155e75;\n"
"    border-radius: 8px;\n"
"\n"
"    max-height: 110px;          /* \ud83d"
                        "\udd11 CLAVE */\n"
"    padding: 2px;\n"
"\n"
"    selection-background-color: #22d3ee;\n"
"    selection-color: #041518;\n"
"\n"
"    outline: none;\n"
"}\n"
"\n"
"/* Items */\n"
"QComboBox QAbstractItemView::item {\n"
"    padding: 2px 8px;           /* compacto */\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"/* Hover */\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #155e6a;\n"
"    color: #ecfeff;\n"
"}\n"
"\n"
"/* Seleccionado */\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: #22d3ee;\n"
"    color: #041518;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    background-color: #155e6a;\n"
"    border: 1px solid #22d3ee;   /* MISMO GROSOR */\n"
"}")

        self.horizontalLayoutFiltros.addWidget(self.comboMes)

        self.horizontalSpacer1 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutFiltros.addItem(self.horizontalSpacer1)

        self.labelAnio = QLabel(EstadisticasView)
        self.labelAnio.setObjectName(u"labelAnio")
        self.labelAnio.setStyleSheet(u"/* =========================================\n"
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
        self.comboAnio.setStyleSheet(u"QComboBox {\n"
"    background-color: #0f3a43;\n"
"    color: #ecfeff;\n"
"    border: 1px solid #1f6f7a;\n"
"    border-radius: 12px;\n"
"\n"
"    padding: 2px 8px;          /* \u2b05\ufe0f 1px menos */\n"
"    padding-right: 32px;\n"
"\n"
"    font-size: 12px;\n"
"    min-height: 34px;           /* \u2b05\ufe0f antes 38 */\n"
"}\n"
"\n"
"/* =========================================\n"
"   COMBOBOX \u2013 DESPLEGABLE AJUSTADO A ESTE TAMA\u00d1O\n"
"========================================= */\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: content;\n"
"    subcontrol-position: right center;\n"
"    width: 28px;\n"
"    border-left: 1px solid #1f6f7a;\n"
"}\n"
"\n"
"/* Quitamos la flecha por est\u00e9tica */\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"}\n"
"\n"
"/* Lista desplegable */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #0b2a30;\n"
"    color: #cfe9ee;\n"
"\n"
"    border: 1px solid #155e75;\n"
"    border-radius: 8px;\n"
"\n"
"    max-height: 110px;          /* \ud83d"
                        "\udd11 CLAVE */\n"
"    padding: 2px;\n"
"\n"
"    selection-background-color: #22d3ee;\n"
"    selection-color: #041518;\n"
"\n"
"    outline: none;\n"
"}\n"
"\n"
"/* Items */\n"
"QComboBox QAbstractItemView::item {\n"
"    padding: 2px 8px;           /* compacto */\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"/* Hover */\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #155e6a;\n"
"    color: #ecfeff;\n"
"}\n"
"\n"
"/* Seleccionado */\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: #22d3ee;\n"
"    color: #041518;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    background-color: #155e6a;\n"
"    border: 1px solid #22d3ee;   /* MISMO GROSOR */\n"
"}")

        self.horizontalLayoutFiltros.addWidget(self.comboAnio)

        self.horizontalSpacer2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutFiltros.addItem(self.horizontalSpacer2)

        self.btnFiltrar = QPushButton(EstadisticasView)
        self.btnFiltrar.setObjectName(u"btnFiltrar")
        self.btnFiltrar.setStyleSheet(u"/* =========================================\n"
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
"/* =========================================\n"
"   BOT\u00d3N ALTERNATIVO \u2013 BLANCO AZULADO\n"
"============"
                        "============================= */\n"
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

        self.horizontalLayoutFiltros.addWidget(self.btnFiltrar)


        self.verticalLayout.addLayout(self.horizontalLayoutFiltros)

        self.horizontalLayoutExport = QHBoxLayout()
        self.horizontalLayoutExport.setSpacing(10)
        self.horizontalLayoutExport.setObjectName(u"horizontalLayoutExport")
        self.btnExportCSV = QPushButton(EstadisticasView)
        self.btnExportCSV.setObjectName(u"btnExportCSV")
        self.btnExportCSV.setStyleSheet(u"/* =========================================\n"
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

        self.horizontalLayoutExport.addWidget(self.btnExportCSV)

        self.btnExportPDF = QPushButton(EstadisticasView)
        self.btnExportPDF.setObjectName(u"btnExportPDF")
        self.btnExportPDF.setStyleSheet(u"/* =========================================\n"
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

        self.horizontalLayoutExport.addWidget(self.btnExportPDF)


        self.verticalLayout.addLayout(self.horizontalLayoutExport)

        self.groupGasto = QGroupBox(EstadisticasView)
        self.groupGasto.setObjectName(u"groupGasto")
        self.groupGasto.setStyleSheet(u"/* =========================================\n"
"   GROUPBOX \u2013 ESPACIADO CORRECTO\n"
"========================================= */\n"
"\n"
"QGroupBox {\n"
"    background-color: #0b2a30;\n"
"    border: 1px solid #155e75;\n"
"    border-radius: 14px;\n"
"\n"
"    margin-top: 22px;        /* espacio real para el t\u00edtulo */\n"
"    padding-top: 18px;       /* aire interno */\n"
"    padding-left: 16px;\n"
"    padding-right: 16px;\n"
"    padding-bottom: 16px;\n"
"}\n"
"\n"
"/* T\u00edtulo */\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"\n"
"    padding: 0 12px;\n"
"    color: #22d3ee;\n"
"    font-size: 14px;\n"
"/* =========================================\n"
"   GROUPBOX \u2013 ESPACIADO CORRECTO\n"
"========================================= */\n"
"\n"
"QGroupBox {\n"
"    background-color: #0b2a30;\n"
"    border: 1px solid #155e75;\n"
"    border-radius: 14px;\n"
"\n"
"    margin-top: 22px;        /* espacio real para el t\u00edtulo */\n"
" "
                        "   padding-top: 18px;       /* aire interno */\n"
"    padding-left: 16px;\n"
"    padding-right: 16px;\n"
"    padding-bottom: 16px;\n"
"}\n"
"\n"
"/* T\u00edtulo */\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"\n"
"    padding: 0 12px;\n"
"    color: #22d3ee;\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"}\n"
"    font-weight: 600;\n"
"}\n"
"")
        self.layoutGasto = QVBoxLayout(self.groupGasto)
        self.layoutGasto.setSpacing(0)
        self.layoutGasto.setObjectName(u"layoutGasto")
        self.layoutGasto.setContentsMargins(5, 5, 5, 5)

        self.verticalLayout.addWidget(self.groupGasto)

        self.groupConsumo = QGroupBox(EstadisticasView)
        self.groupConsumo.setObjectName(u"groupConsumo")
        self.groupConsumo.setStyleSheet(u"/* =========================================\n"
"   GROUPBOX \u2013 ESPACIADO CORRECTO\n"
"========================================= */\n"
"\n"
"QGroupBox {\n"
"    background-color: #0b2a30;\n"
"    border: 1px solid #155e75;\n"
"    border-radius: 14px;\n"
"\n"
"    margin-top: 22px;        /* espacio real para el t\u00edtulo */\n"
"    padding-top: 18px;       /* aire interno */\n"
"    padding-left: 16px;\n"
"    padding-right: 16px;\n"
"    padding-bottom: 16px;\n"
"}\n"
"\n"
"/* T\u00edtulo */\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"\n"
"    padding: 0 12px;\n"
"    color: #22d3ee;\n"
"    font-size: 14px;\n"
"/* =========================================\n"
"   GROUPBOX \u2013 ESPACIADO CORRECTO\n"
"========================================= */\n"
"\n"
"QGroupBox {\n"
"    background-color: #0b2a30;\n"
"    border: 1px solid #155e75;\n"
"    border-radius: 14px;\n"
"\n"
"    margin-top: 22px;        /* espacio real para el t\u00edtulo */\n"
" "
                        "   padding-top: 18px;       /* aire interno */\n"
"    padding-left: 16px;\n"
"    padding-right: 16px;\n"
"    padding-bottom: 16px;\n"
"}\n"
"\n"
"/* T\u00edtulo */\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"\n"
"    padding: 0 12px;\n"
"    color: #22d3ee;\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"}\n"
"    font-weight: 600;\n"
"}\n"
"")
        self.layoutConsumo = QVBoxLayout(self.groupConsumo)
        self.layoutConsumo.setSpacing(0)
        self.layoutConsumo.setObjectName(u"layoutConsumo")
        self.layoutConsumo.setContentsMargins(5, 5, 5, 5)

        self.verticalLayout.addWidget(self.groupConsumo)

        self.btnVolver = QPushButton(EstadisticasView)
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


        self.retranslateUi(EstadisticasView)

        QMetaObject.connectSlotsByName(EstadisticasView)
    # setupUi

    def retranslateUi(self, EstadisticasView):
        EstadisticasView.setWindowTitle(QCoreApplication.translate("EstadisticasView", u"Estad\u00edsticas Avanzadas", None))
        self.labelTitulo.setText(QCoreApplication.translate("EstadisticasView", u" Estad\u00edsticas Avanzadas", None))
        self.labelMes.setText(QCoreApplication.translate("EstadisticasView", u"Mes:", None))
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
        self.btnVolver.setText(QCoreApplication.translate("EstadisticasView", u" Volver al Men\u00fa", None))
    # retranslateUi

