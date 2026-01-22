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
        LoginView.resize(380, 323)
        LoginView.setStyleSheet(u"QWidget {\n"
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
        self.vboxLayout = QVBoxLayout(LoginView)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.labelTitulo = QLabel(LoginView)
        self.labelTitulo.setObjectName(u"labelTitulo")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setBold(False)
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

        self.inputUsername = QLineEdit(LoginView)
        self.inputUsername.setObjectName(u"inputUsername")
        self.inputUsername.setStyleSheet(u"/* =========================================\n"
"   ENTRADAS DE TEXTO \u2013 CONTRASTE AZUL PETR\u00d3LEO\n"
"========================================= */\n"
"\n"
"QLineEdit {\n"
"    background-color: #0f3a43;        /* M\u00c1S CLARO que el fondo */\n"
"    color: #ecfeff;\n"
"    border: 1px solid #1f6f7a;\n"
"    border-radius: 12px;\n"
"    padding: 11px 16px;\n"
"    font-size: 14px;\n"
"    selection-background-color: #22d3ee;\n"
"    selection-color: #041518;\n"
"}\n"
"\n"
"/* Placeholder */\n"
"QLineEdit::placeholder {\n"
"    color: #9adce6;\n"
"}\n"
"\n"
"/* Hover */\n"
"QLineEdit:hover {\n"
"    border-color: #22d3ee;\n"
"    background-color: #134852;\n"
"}\n"
"\n"
"/* Focus: contraste fuerte pero elegante */\n"
"QLineEdit:focus {\n"
"    background-color: #155e6a;\n"
"    border: 2px solid #22d3ee;\n"
"}\n"
"")

        self.vboxLayout.addWidget(self.inputUsername)

        self.inputPassword = QLineEdit(LoginView)
        self.inputPassword.setObjectName(u"inputPassword")
        self.inputPassword.setStyleSheet(u"/* =========================================\n"
"   ENTRADAS DE TEXTO \u2013 CONTRASTE AZUL PETR\u00d3LEO\n"
"========================================= */\n"
"\n"
"QLineEdit {\n"
"    background-color: #0f3a43;        /* M\u00c1S CLARO que el fondo */\n"
"    color: #ecfeff;\n"
"    border: 1px solid #1f6f7a;\n"
"    border-radius: 12px;\n"
"    padding: 11px 16px;\n"
"    font-size: 14px;\n"
"    selection-background-color: #22d3ee;\n"
"    selection-color: #041518;\n"
"}\n"
"\n"
"/* Placeholder */\n"
"QLineEdit::placeholder {\n"
"    color: #9adce6;\n"
"}\n"
"\n"
"/* Hover */\n"
"QLineEdit:hover {\n"
"    border-color: #22d3ee;\n"
"    background-color: #134852;\n"
"}\n"
"\n"
"/* Focus: contraste fuerte pero elegante */\n"
"QLineEdit:focus {\n"
"    background-color: #155e6a;\n"
"    border: 2px solid #22d3ee;\n"
"}\n"
"")
        self.inputPassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.vboxLayout.addWidget(self.inputPassword)

        self.labelMensaje = QLabel(LoginView)
        self.labelMensaje.setObjectName(u"labelMensaje")
        self.labelMensaje.setVisible(False)
        self.labelMensaje.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout.addWidget(self.labelMensaje)

        self.btnInicioSesion = QPushButton(LoginView)
        self.btnInicioSesion.setObjectName(u"btnInicioSesion")
        self.btnInicioSesion.setStyleSheet(u"/* =========================================\n"
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

        self.vboxLayout.addWidget(self.btnInicioSesion)

        self.btnIrRegistro = QPushButton(LoginView)
        self.btnIrRegistro.setObjectName(u"btnIrRegistro")
        self.btnIrRegistro.setStyleSheet(u"/* =========================================\n"
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

        self.vboxLayout.addWidget(self.btnIrRegistro)


        self.retranslateUi(LoginView)

        QMetaObject.connectSlotsByName(LoginView)
    # setupUi

    def retranslateUi(self, LoginView):
        LoginView.setWindowTitle(QCoreApplication.translate("LoginView", u"Kil\u00f3metro a Kil\u00f3metro - Login", None))
        self.labelTitulo.setText(QCoreApplication.translate("LoginView", u"Kil\u00f3metro a Kil\u00f3metro", None))
        self.inputUsername.setPlaceholderText(QCoreApplication.translate("LoginView", u"Usuario", None))
        self.inputPassword.setPlaceholderText(QCoreApplication.translate("LoginView", u"Contrase\u00f1a", None))
        self.btnInicioSesion.setText(QCoreApplication.translate("LoginView", u"Iniciar sesi\u00f3n", None))
        self.btnIrRegistro.setText(QCoreApplication.translate("LoginView", u"Crear cuenta", None))
    # retranslateUi

