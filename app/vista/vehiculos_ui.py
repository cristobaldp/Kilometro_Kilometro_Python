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
        VehiculosView.setStyleSheet(u"QWidget {\n"
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
        self.vboxLayout = QVBoxLayout(VehiculosView)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.labelTitulo = QLabel(VehiculosView)
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

        self.vboxLayout.addWidget(self.labelTitulo)

        self.labelSubtitulo = QLabel(VehiculosView)
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
        self.tablaVehiculos.setStyleSheet(u"/* =========================================\n"
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
        self.tablaVehiculos.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tablaVehiculos.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tablaVehiculos.setColumnCount(7)

        self.vboxLayout.addWidget(self.tablaVehiculos)

        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.btnVolver = QPushButton(VehiculosView)
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

        self.hboxLayout.addWidget(self.btnVolver)

        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout.addItem(self.horizontalSpacer)

        self.btnSetActivo = QPushButton(VehiculosView)
        self.btnSetActivo.setObjectName(u"btnSetActivo")
        self.btnSetActivo.setStyleSheet(u"/* =========================================\n"
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

        self.hboxLayout.addWidget(self.btnSetActivo)

        self.btnEliminar = QPushButton(VehiculosView)
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

        self.hboxLayout.addWidget(self.btnEliminar)

        self.btnAddVehiculo = QPushButton(VehiculosView)
        self.btnAddVehiculo.setObjectName(u"btnAddVehiculo")
        self.btnAddVehiculo.setStyleSheet(u"/* =========================================\n"
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

        self.hboxLayout.addWidget(self.btnAddVehiculo)


        self.vboxLayout.addLayout(self.hboxLayout)


        self.retranslateUi(VehiculosView)

        QMetaObject.connectSlotsByName(VehiculosView)
    # setupUi

    def retranslateUi(self, VehiculosView):
        VehiculosView.setWindowTitle(QCoreApplication.translate("VehiculosView", u"Mis veh\u00edculos", None))
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

