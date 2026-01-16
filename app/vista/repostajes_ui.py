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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_RepostajesView(object):
    def setupUi(self, RepostajesView):
        if not RepostajesView.objectName():
            RepostajesView.setObjectName(u"RepostajesView")
        RepostajesView.resize(900, 600)
        self.vboxLayout = QVBoxLayout(RepostajesView)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.labelTitulo = QLabel(RepostajesView)
        self.labelTitulo.setObjectName(u"labelTitulo")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(22)
        font.setBold(True)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout.addWidget(self.labelTitulo)

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
        self.tablaRepostajes.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tablaRepostajes.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tablaRepostajes.setColumnCount(5)

        self.vboxLayout.addWidget(self.tablaRepostajes)

        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.btnVolver = QPushButton(RepostajesView)
        self.btnVolver.setObjectName(u"btnVolver")

        self.hboxLayout.addWidget(self.btnVolver)

        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout.addItem(self.horizontalSpacer)

        self.btnExportCSV = QPushButton(RepostajesView)
        self.btnExportCSV.setObjectName(u"btnExportCSV")

        self.hboxLayout.addWidget(self.btnExportCSV)

        self.btnExportPDF = QPushButton(RepostajesView)
        self.btnExportPDF.setObjectName(u"btnExportPDF")

        self.hboxLayout.addWidget(self.btnExportPDF)

        self.btnEliminar = QPushButton(RepostajesView)
        self.btnEliminar.setObjectName(u"btnEliminar")

        self.hboxLayout.addWidget(self.btnEliminar)

        self.btnNuevo = QPushButton(RepostajesView)
        self.btnNuevo.setObjectName(u"btnNuevo")

        self.hboxLayout.addWidget(self.btnNuevo)


        self.vboxLayout.addLayout(self.hboxLayout)


        self.retranslateUi(RepostajesView)

        QMetaObject.connectSlotsByName(RepostajesView)
    # setupUi

    def retranslateUi(self, RepostajesView):
        RepostajesView.setWindowTitle(QCoreApplication.translate("RepostajesView", u"Repostajes", None))
        RepostajesView.setStyleSheet(QCoreApplication.translate("RepostajesView", u"\n"
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
        self.labelTitulo.setText(QCoreApplication.translate("RepostajesView", u"Repostajes", None))
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

