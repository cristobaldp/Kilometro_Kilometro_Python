# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fer.ui'
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
        RepostajesView.resize(900, 600)
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
        self.labelTitulo.setAlignment(Qt.AlignCenter)
        self.labelTitulo.setStyleSheet(u"\n"
"QLabel {\n"
"    color: #22d3ee;\n"
"    font-size: 22px;\n"
"    font-weight: 600;\n"
"}\n"
"      ")

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
        self.comboMes.setMinimumWidth(160)

        self.hboxLayout.addWidget(self.comboMes)

        self.comboAnio = QComboBox(RepostajesView)
        self.comboAnio.addItem("")
        self.comboAnio.setObjectName(u"comboAnio")
        self.comboAnio.setMinimumWidth(120)

        self.hboxLayout.addWidget(self.comboAnio)

        self.spacerFiltros = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout.addItem(self.spacerFiltros)


        self.vboxLayout.addLayout(self.hboxLayout)

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
        self.tablaRepostajes.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablaRepostajes.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tablaRepostajes.setColumnCount(5)

        self.vboxLayout.addWidget(self.tablaRepostajes)

        self.hboxLayout1 = QHBoxLayout()
        self.hboxLayout1.setObjectName(u"hboxLayout1")
        self.btnVolver = QPushButton(RepostajesView)
        self.btnVolver.setObjectName(u"btnVolver")

        self.hboxLayout1.addWidget(self.btnVolver)

        self.spacerBotones = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout1.addItem(self.spacerBotones)

        self.btnExportCSV = QPushButton(RepostajesView)
        self.btnExportCSV.setObjectName(u"btnExportCSV")

        self.hboxLayout1.addWidget(self.btnExportCSV)

        self.btnExportPDF = QPushButton(RepostajesView)
        self.btnExportPDF.setObjectName(u"btnExportPDF")

        self.hboxLayout1.addWidget(self.btnExportPDF)

        self.btnEliminar = QPushButton(RepostajesView)
        self.btnEliminar.setObjectName(u"btnEliminar")

        self.hboxLayout1.addWidget(self.btnEliminar)

        self.btnNuevo = QPushButton(RepostajesView)
        self.btnNuevo.setObjectName(u"btnNuevo")

        self.hboxLayout1.addWidget(self.btnNuevo)


        self.vboxLayout.addLayout(self.hboxLayout1)


        self.retranslateUi(RepostajesView)

        QMetaObject.connectSlotsByName(RepostajesView)
    # setupUi

    def retranslateUi(self, RepostajesView):
        RepostajesView.setWindowTitle(QCoreApplication.translate("RepostajesView", u"Repostajes", None))
        self.labelTitulo.setText(QCoreApplication.translate("RepostajesView", u"Repostajes", None))
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

