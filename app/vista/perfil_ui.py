# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'perfil.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_PerfilView(object):
    def setupUi(self, PerfilView):
        if not PerfilView.objectName():
            PerfilView.setObjectName(u"PerfilView")
        PerfilView.resize(520, 680)
        self.vboxLayout = QVBoxLayout(PerfilView)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.labelTitulo = QLabel(PerfilView)
        self.labelTitulo.setObjectName(u"labelTitulo")
        self.labelTitulo.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.labelTitulo.setFont(font)

        self.vboxLayout.addWidget(self.labelTitulo)

        self.inputNombre = QLineEdit(PerfilView)
        self.inputNombre.setObjectName(u"inputNombre")

        self.vboxLayout.addWidget(self.inputNombre)

        self.inputApellidos = QLineEdit(PerfilView)
        self.inputApellidos.setObjectName(u"inputApellidos")

        self.vboxLayout.addWidget(self.inputApellidos)

        self.inputUsername = QLineEdit(PerfilView)
        self.inputUsername.setObjectName(u"inputUsername")
        self.inputUsername.setEnabled(False)

        self.vboxLayout.addWidget(self.inputUsername)

        self.inputEmail = QLineEdit(PerfilView)
        self.inputEmail.setObjectName(u"inputEmail")

        self.vboxLayout.addWidget(self.inputEmail)

        self.inputTelefono = QLineEdit(PerfilView)
        self.inputTelefono.setObjectName(u"inputTelefono")

        self.vboxLayout.addWidget(self.inputTelefono)

        self.inputCiudad = QLineEdit(PerfilView)
        self.inputCiudad.setObjectName(u"inputCiudad")

        self.vboxLayout.addWidget(self.inputCiudad)

        self.dateNacimiento = QDateEdit(PerfilView)
        self.dateNacimiento.setObjectName(u"dateNacimiento")
        self.dateNacimiento.setCalendarPopup(True)

        self.vboxLayout.addWidget(self.dateNacimiento)

        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.btnEditar = QPushButton(PerfilView)
        self.btnEditar.setObjectName(u"btnEditar")

        self.hboxLayout.addWidget(self.btnEditar)

        self.btnGuardar = QPushButton(PerfilView)
        self.btnGuardar.setObjectName(u"btnGuardar")

        self.hboxLayout.addWidget(self.btnGuardar)


        self.vboxLayout.addLayout(self.hboxLayout)

        self.groupPassword = QGroupBox(PerfilView)
        self.groupPassword.setObjectName(u"groupPassword")
        self.vboxLayout1 = QVBoxLayout(self.groupPassword)
        self.vboxLayout1.setObjectName(u"vboxLayout1")
        self.inputPassNueva = QLineEdit(self.groupPassword)
        self.inputPassNueva.setObjectName(u"inputPassNueva")
        self.inputPassNueva.setEchoMode(QLineEdit.Password)

        self.vboxLayout1.addWidget(self.inputPassNueva)

        self.inputPassNueva2 = QLineEdit(self.groupPassword)
        self.inputPassNueva2.setObjectName(u"inputPassNueva2")
        self.inputPassNueva2.setEchoMode(QLineEdit.Password)

        self.vboxLayout1.addWidget(self.inputPassNueva2)

        self.btnCambiarPassword = QPushButton(self.groupPassword)
        self.btnCambiarPassword.setObjectName(u"btnCambiarPassword")

        self.vboxLayout1.addWidget(self.btnCambiarPassword)


        self.vboxLayout.addWidget(self.groupPassword)

        self.btnEliminarCuenta = QPushButton(PerfilView)
        self.btnEliminarCuenta.setObjectName(u"btnEliminarCuenta")

        self.vboxLayout.addWidget(self.btnEliminarCuenta)

        self.btnVolver = QPushButton(PerfilView)
        self.btnVolver.setObjectName(u"btnVolver")

        self.vboxLayout.addWidget(self.btnVolver)


        self.retranslateUi(PerfilView)

        QMetaObject.connectSlotsByName(PerfilView)
    # setupUi

    def retranslateUi(self, PerfilView):
        PerfilView.setWindowTitle(QCoreApplication.translate("PerfilView", u"Perfil de usuario", None))
        PerfilView.setStyleSheet(QCoreApplication.translate("PerfilView", u"\n"
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
"QLineEdit, QDateEdit {\n"
"    background-color: #1e1e1e;\n"
"    border: 2px solid #2e2e2e;\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QLineEdit:focus, QDateEdit:focus {\n"
"    border: 2px solid #00c853;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #00c853;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    font-weight: bold;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #00e676;\n"
"}\n"
"\n"
"QPushButton#btnEliminarCuenta {\n"
"    background-color: #2a1e1e;\n"
"    border: 2px solid #ff5252;\n"
"    color: #ff5252;\n"
"}\n"
"\n"
"QPushButton#btnEliminarCuenta:hover {\n"
"    background-color: #ff5252;\n"
"    color: #000000;\n"
"}\n"
"   ", None))
        self.labelTitulo.setText(QCoreApplication.translate("PerfilView", u"Perfil de usuario", None))
        self.inputNombre.setPlaceholderText(QCoreApplication.translate("PerfilView", u"Nombre", None))
        self.inputApellidos.setPlaceholderText(QCoreApplication.translate("PerfilView", u"Apellidos", None))
        self.inputUsername.setPlaceholderText(QCoreApplication.translate("PerfilView", u"Usuario", None))
        self.inputEmail.setPlaceholderText(QCoreApplication.translate("PerfilView", u"Email", None))
        self.inputTelefono.setPlaceholderText(QCoreApplication.translate("PerfilView", u"Tel\u00e9fono", None))
        self.inputCiudad.setPlaceholderText(QCoreApplication.translate("PerfilView", u"Ciudad", None))
        self.btnEditar.setText(QCoreApplication.translate("PerfilView", u"Editar", None))
        self.btnGuardar.setText(QCoreApplication.translate("PerfilView", u"Guardar cambios", None))
        self.groupPassword.setTitle(QCoreApplication.translate("PerfilView", u"Cambiar contrase\u00f1a", None))
        self.inputPassNueva.setPlaceholderText(QCoreApplication.translate("PerfilView", u"Nueva contrase\u00f1a", None))
        self.inputPassNueva2.setPlaceholderText(QCoreApplication.translate("PerfilView", u"Repetir nueva contrase\u00f1a", None))
        self.btnCambiarPassword.setText(QCoreApplication.translate("PerfilView", u"Guardar nueva contrase\u00f1a", None))
        self.btnEliminarCuenta.setText(QCoreApplication.translate("PerfilView", u"Eliminar cuenta", None))
        self.btnVolver.setText(QCoreApplication.translate("PerfilView", u"Volver", None))
    # retranslateUi

