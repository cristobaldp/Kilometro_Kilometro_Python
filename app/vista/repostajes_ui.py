# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'repostajes.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_RepostajesView(object):
    def setupUi(self, RepostajesView):
        if not RepostajesView.objectName():
            RepostajesView.setObjectName(u"RepostajesView")
        RepostajesView.resize(900, 591)
        RepostajesView.setStyleSheet(u"\n"
"QWidget {\n"
"    background-color: #121212;\n"
"    color: #eaeaea;\n"
"    font-family: Segoe UI;\n"
"}\n"
"   ")
        self.vboxLayout = QVBoxLayout(RepostajesView)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.labelTitulo = QLabel(RepostajesView)
        self.labelTitulo.setObjectName(u"labelTitulo")
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

        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.comboMes = QComboBox(RepostajesView)
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

        self.hboxLayout.addWidget(self.comboMes)

        self.comboAnio = QComboBox(RepostajesView)
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

        self.hboxLayout.addWidget(self.comboAnio)

        self.btnBuscar = QPushButton(RepostajesView)
        self.btnBuscar.setObjectName(u"btnBuscar")
        self.btnBuscar.setStyleSheet(u"/* =========================================\n"
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

        self.hboxLayout.addWidget(self.btnBuscar)

        self.spacerFiltros = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout.addItem(self.spacerFiltros)


        self.vboxLayout.addLayout(self.hboxLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.vboxLayout.addItem(self.horizontalSpacer_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.vboxLayout.addItem(self.horizontalSpacer_3)

        self.tablaRepostajes = QTableWidget(RepostajesView)
        if (self.tablaRepostajes.columnCount() < 5):
            self.tablaRepostajes.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablaRepostajes.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablaRepostajes.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablaRepostajes.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tablaRepostajes.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tablaRepostajes.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tablaRepostajes.setObjectName(u"tablaRepostajes")
        self.tablaRepostajes.setStyleSheet(u"/* =========================================\n"
"   TABLAS \u2013 MEJORA VISUAL DE COLUMNAS\n"
"========================================= */\n"
"\n"
"QTableView, QTableWidget {\n"
"    background-color: #0b2a30;\n"
"    color: #ecfeff;\n"
"\n"
"    border: 1px solid #1f6f7a;\n"
"    border-radius: 10px;\n"
"\n"
"    gridline-color: #1f6f7a;   /* l\u00edneas visibles */\n"
"    font-size: 13px;\n"
"    outline: none;\n"
"}\n"
"\n"
"/* ==========================\n"
"   CABECERA HORIZONTAL\n"
"========================== */\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #123b44;\n"
"    color: #e0f7fa;\n"
"\n"
"    padding: 8px 12px;        /* \u2b05\ufe0f M\u00c1S AIRE */\n"
"    border: none;\n"
"\n"
"    border-right: 1px solid #1f6f7a;\n"
"    border-bottom: 2px solid #22d3ee; /* separaci\u00f3n clara */\n"
"\n"
"    font-size: 13px;\n"
"    font-weight: 600;\n"
"    text-align: center;\n"
"}\n"
"\n"
"/* \u00daltima columna sin borde derecho */\n"
"QHeaderView::section:last {\n"
"    border-right: n"
                        "one;\n"
"}\n"
"\n"
"/* Hover cabecera */\n"
"QHeaderView::section:hover {\n"
"    background-color: #155e6a;\n"
"}\n"
"\n"
"/* ==========================\n"
"   FILAS Y COLUMNAS\n"
"========================== */\n"
"\n"
"QTableView::item, QTableWidget::item {\n"
"    padding: 6px 10px;        /* \u2b05\ufe0f columnas m\u00e1s legibles */\n"
"    border-right: 1px solid #0f3a43;\n"
"}\n"
"\n"
"/* Alternar filas (muy recomendable) */\n"
"QTableView {\n"
"    alternate-background-color: #0f3a43;\n"
"}\n"
"\n"
"/* Hover fila */\n"
"QTableView::item:hover {\n"
"    background-color: #155e6a;\n"
"}\n"
"\n"
"/* Selecci\u00f3n */\n"
"QTableView::item:selected {\n"
"    background-color: #22d3ee;\n"
"    color: #041518;\n"
"}\n"
"\n"
"/* ==========================\n"
"   CABECERA VERTICAL (si se usa)\n"
"========================== */\n"
"\n"
"QHeaderView::section:vertical {\n"
"    background-color: #020617;\n"
"    color: #7dd3fc;\n"
"\n"
"    padding: 6px;\n"
"    border-bottom: 1px solid #1f6f7a;\n"
"}\n"
"")
        self.tablaRepostajes.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tablaRepostajes.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tablaRepostajes.setColumnCount(5)

        self.vboxLayout.addWidget(self.tablaRepostajes)

        self.hboxLayout1 = QHBoxLayout()
        self.hboxLayout1.setObjectName(u"hboxLayout1")
        self.btnVolver = QPushButton(RepostajesView)
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

        self.hboxLayout1.addWidget(self.btnVolver)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout1.addItem(self.horizontalSpacer)

        self.btnExportCSV = QPushButton(RepostajesView)
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

        self.hboxLayout1.addWidget(self.btnExportCSV)

        self.btnExportPDF = QPushButton(RepostajesView)
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

        self.hboxLayout1.addWidget(self.btnExportPDF)

        self.btnEliminar = QPushButton(RepostajesView)
        self.btnEliminar.setObjectName(u"btnEliminar")
        self.btnEliminar.setStyleSheet(u"/* =========================================\n"
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

        self.hboxLayout1.addWidget(self.btnEliminar)

        self.btnNuevo = QPushButton(RepostajesView)
        self.btnNuevo.setObjectName(u"btnNuevo")
        self.btnNuevo.setStyleSheet(u"/* =========================================\n"
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

        self.hboxLayout1.addWidget(self.btnNuevo)


        self.vboxLayout.addLayout(self.hboxLayout1)


        self.retranslateUi(RepostajesView)

        QMetaObject.connectSlotsByName(RepostajesView)
    # setupUi

    def retranslateUi(self, RepostajesView):
        RepostajesView.setWindowTitle(QCoreApplication.translate("RepostajesView", u"Repostajes", None))
        self.labelTitulo.setText(QCoreApplication.translate("RepostajesView", u"<html><head/><body><p>Mis Repostajes</p></body></html>", None))
        self.comboMes.setItemText(0, QCoreApplication.translate("RepostajesView", u"Todos los meses", None))
        self.comboMes.setItemText(1, QCoreApplication.translate("RepostajesView", u"Enero", None))
        self.comboMes.setItemText(2, QCoreApplication.translate("RepostajesView", u"Febrero", None))
        self.comboMes.setItemText(3, QCoreApplication.translate("RepostajesView", u"Marzo", None))
        self.comboMes.setItemText(4, QCoreApplication.translate("RepostajesView", u"Abril", None))
        self.comboMes.setItemText(5, QCoreApplication.translate("RepostajesView", u"Mayo", None))
        self.comboMes.setItemText(6, QCoreApplication.translate("RepostajesView", u"Junio", None))
        self.comboMes.setItemText(7, QCoreApplication.translate("RepostajesView", u"Julio", None))
        self.comboMes.setItemText(8, QCoreApplication.translate("RepostajesView", u"Agosto", None))
        self.comboMes.setItemText(9, QCoreApplication.translate("RepostajesView", u"Septiembre", None))
        self.comboMes.setItemText(10, QCoreApplication.translate("RepostajesView", u"Octubre", None))
        self.comboMes.setItemText(11, QCoreApplication.translate("RepostajesView", u"Noviembre", None))
        self.comboMes.setItemText(12, QCoreApplication.translate("RepostajesView", u"Diciembre", None))

        self.comboAnio.setItemText(0, QCoreApplication.translate("RepostajesView", u"Todos los a\u00f1os", None))
        self.comboAnio.setItemText(1, QCoreApplication.translate("RepostajesView", u"2021", None))
        self.comboAnio.setItemText(2, QCoreApplication.translate("RepostajesView", u"2022", None))
        self.comboAnio.setItemText(3, QCoreApplication.translate("RepostajesView", u"2023", None))
        self.comboAnio.setItemText(4, QCoreApplication.translate("RepostajesView", u"2024", None))
        self.comboAnio.setItemText(5, QCoreApplication.translate("RepostajesView", u"2025", None))
        self.comboAnio.setItemText(6, QCoreApplication.translate("RepostajesView", u"2026", None))
        self.comboAnio.setItemText(7, QCoreApplication.translate("RepostajesView", u"2027", None))
        self.comboAnio.setItemText(8, QCoreApplication.translate("RepostajesView", u"2028", None))
        self.comboAnio.setItemText(9, QCoreApplication.translate("RepostajesView", u"2029", None))
        self.comboAnio.setItemText(10, QCoreApplication.translate("RepostajesView", u"2030", None))
        self.comboAnio.setItemText(11, QCoreApplication.translate("RepostajesView", u"2031", None))

        self.btnBuscar.setText(QCoreApplication.translate("RepostajesView", u"Buscar", None))
        ___qtablewidgetitem = self.tablaRepostajes.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("RepostajesView", u"ID", None));
        ___qtablewidgetitem1 = self.tablaRepostajes.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("RepostajesView", u"Fecha", None));
        ___qtablewidgetitem2 = self.tablaRepostajes.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("RepostajesView", u"Litros", None));
        ___qtablewidgetitem3 = self.tablaRepostajes.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("RepostajesView", u"Precio", None));
        ___qtablewidgetitem4 = self.tablaRepostajes.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("RepostajesView", u"Kil\u00f3metros", None));
        self.btnVolver.setText(QCoreApplication.translate("RepostajesView", u"Volver", None))
        self.btnExportCSV.setText(QCoreApplication.translate("RepostajesView", u"Exportar CSV", None))
        self.btnExportPDF.setText(QCoreApplication.translate("RepostajesView", u"Exportar PDF", None))
        self.btnEliminar.setText(QCoreApplication.translate("RepostajesView", u"Eliminar", None))
        self.btnNuevo.setText(QCoreApplication.translate("RepostajesView", u"Nuevo repostaje", None))
    # retranslateUi

