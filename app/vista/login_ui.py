# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_LoginView(object):
    def setupUi(self, LoginView):
        if not LoginView.objectName():
            LoginView.setObjectName(u"LoginView")
        LoginView.resize(380, 320)
        self.vboxLayout = QVBoxLayout(LoginView)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.labelTitulo = QLabel(LoginView)
        self.labelTitulo.setObjectName(u"labelTitulo")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(18)
        font.setBold(True)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout.addWidget(self.labelTitulo)

        self.inputUsername = QLineEdit(LoginView)
        self.inputUsername.setObjectName(u"inputUsername")

        self.vboxLayout.addWidget(self.inputUsername)

        self.inputPassword = QLineEdit(LoginView)
        self.inputPassword.setObjectName(u"inputPassword")
        self.inputPassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.vboxLayout.addWidget(self.inputPassword)

        self.labelMensaje = QLabel(LoginView)
        self.labelMensaje.setObjectName(u"labelMensaje")
        self.labelMensaje.setVisible(False)
        self.labelMensaje.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout.addWidget(self.labelMensaje)

        self.btnInicioSesion = QPushButton(LoginView)
        self.btnInicioSesion.setObjectName(u"btnInicioSesion")

        self.vboxLayout.addWidget(self.btnInicioSesion)

        self.btnIrRegistro = QPushButton(LoginView)
        self.btnIrRegistro.setObjectName(u"btnIrRegistro")

        self.vboxLayout.addWidget(self.btnIrRegistro)


        self.retranslateUi(LoginView)

        QMetaObject.connectSlotsByName(LoginView)
    # setupUi

    def retranslateUi(self, LoginView):
        LoginView.setWindowTitle(QCoreApplication.translate("LoginView", u"Kil\u00f3metro a Kil\u00f3metro - Login", None))
        LoginView.setStyleSheet(QCoreApplication.translate("LoginView", u"\n"
"    QWidget {\n"
"        background-color: #1b1b1b;\n"
"        color: #eaeaea;\n"
"        font-family: Segoe UI;\n"
"    }\n"
"\n"
"    QLabel#labelTitulo {\n"
"        color: #00c853;\n"
"    }\n"
"\n"
"    QLineEdit {\n"
"        background-color: #2a2a2a;\n"
"        border: 2px solid #3a3a3a;\n"
"        border-radius: 6px;\n"
"        padding: 8px;\n"
"        font-size: 14px;\n"
"    }\n"
"\n"
"    QLineEdit:focus {\n"
"        border: 2px solid #00c853;\n"
"    }\n"
"\n"
"    QPushButton {\n"
"        background-color: #00c853;\n"
"        border-radius: 8px;\n"
"        padding: 12px;\n"
"        font-weight: bold;\n"
"        color: #000000;\n"
"    }\n"
"\n"
"    QPushButton:hover {\n"
"        background-color: #00e676;\n"
"    }\n"
"\n"
"    QPushButton#btnIrRegistro {\n"
"        background-color: transparent;\n"
"        color: #9e9e9e;\n"
"        font-weight: normal;\n"
"    }\n"
"\n"
"    QPushButton#btnIrRegistro:hover {\n"
"        color: #00e676;\n"
"        text-decoration: underli"
                        "ne;\n"
"    }\n"
"   ", None))
        self.labelTitulo.setText(QCoreApplication.translate("LoginView", u"Kil\u00f3metro a Kil\u00f3metro", None))
        self.inputUsername.setPlaceholderText(QCoreApplication.translate("LoginView", u"Usuario", None))
        self.inputPassword.setPlaceholderText(QCoreApplication.translate("LoginView", u"Contrase\u00f1a", None))
        self.btnInicioSesion.setText(QCoreApplication.translate("LoginView", u"Iniciar sesi\u00f3n", None))
        self.btnIrRegistro.setText(QCoreApplication.translate("LoginView", u"Crear cuenta", None))
    # retranslateUi

