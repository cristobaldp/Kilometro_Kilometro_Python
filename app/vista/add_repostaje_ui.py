# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_repostaje.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_AddRepostajeView(object):
    def setupUi(self, AddRepostajeView):
        if not AddRepostajeView.objectName():
            AddRepostajeView.setObjectName(u"AddRepostajeView")
        AddRepostajeView.resize(420, 420)
        self.vboxLayout = QVBoxLayout(AddRepostajeView)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.labelTitulo = QLabel(AddRepostajeView)
        self.labelTitulo.setObjectName(u"labelTitulo")
        self.labelTitulo.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.labelTitulo.setFont(font)

        self.vboxLayout.addWidget(self.labelTitulo)

        self.inputFecha = QDateEdit(AddRepostajeView)
        self.inputFecha.setObjectName(u"inputFecha")
        self.inputFecha.setCalendarPopup(True)

        self.vboxLayout.addWidget(self.inputFecha)

        self.inputLitros = QLineEdit(AddRepostajeView)
        self.inputLitros.setObjectName(u"inputLitros")

        self.vboxLayout.addWidget(self.inputLitros)

        self.inputPrecio = QLineEdit(AddRepostajeView)
        self.inputPrecio.setObjectName(u"inputPrecio")

        self.vboxLayout.addWidget(self.inputPrecio)

        self.inputKilometros = QLineEdit(AddRepostajeView)
        self.inputKilometros.setObjectName(u"inputKilometros")

        self.vboxLayout.addWidget(self.inputKilometros)

        self.labelMensaje = QLabel(AddRepostajeView)
        self.labelMensaje.setObjectName(u"labelMensaje")
        self.labelMensaje.setVisible(False)
        self.labelMensaje.setAlignment(Qt.AlignCenter)

        self.vboxLayout.addWidget(self.labelMensaje)

        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.btnSave = QPushButton(AddRepostajeView)
        self.btnSave.setObjectName(u"btnSave")

        self.hboxLayout.addWidget(self.btnSave)

        self.btnCancel = QPushButton(AddRepostajeView)
        self.btnCancel.setObjectName(u"btnCancel")

        self.hboxLayout.addWidget(self.btnCancel)


        self.vboxLayout.addLayout(self.hboxLayout)


        self.retranslateUi(AddRepostajeView)

        QMetaObject.connectSlotsByName(AddRepostajeView)
    # setupUi

    def retranslateUi(self, AddRepostajeView):
        AddRepostajeView.setWindowTitle(QCoreApplication.translate("AddRepostajeView", u"A\u00f1adir repostaje", None))
        AddRepostajeView.setStyleSheet(QCoreApplication.translate("AddRepostajeView", u"\n"
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
"QDateEdit, QLineEdit {\n"
"    background-color: #1e1e1e;\n"
"    border: 2px solid #2e2e2e;\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"    border: none;\n"
"}\n"
"\n"
"QLineEdit:focus, QDateEdit:focus {\n"
"    border: 2px solid #00c853;\n"
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
"QPushButton#btnCancel {\n"
"    background-color: #2a1e1e;\n"
"    border: 2px solid #ff5252;\n"
"    color: #ff5252;\n"
"}\n"
"\n"
"QPushButton#btnCancel:hover {\n"
"    background-color: #ff5252;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QLabel#labelMensaje {\n"
"    color: #"
                        "ff5252;\n"
"    font-size: 12px;\n"
"}\n"
"   ", None))
        self.labelTitulo.setText(QCoreApplication.translate("AddRepostajeView", u"A\u00f1adir repostaje", None))
        self.inputLitros.setPlaceholderText(QCoreApplication.translate("AddRepostajeView", u"Litros", None))
        self.inputPrecio.setPlaceholderText(QCoreApplication.translate("AddRepostajeView", u"Precio total (\u20ac)", None))
        self.inputKilometros.setPlaceholderText(QCoreApplication.translate("AddRepostajeView", u"Kil\u00f3metros", None))
        self.btnSave.setText(QCoreApplication.translate("AddRepostajeView", u"Guardar", None))
        self.btnCancel.setText(QCoreApplication.translate("AddRepostajeView", u"Cancelar", None))
    # retranslateUi

