# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, Qt)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QLabel, QLineEdit, QPushButton,
    QComboBox, QDateEdit, QVBoxLayout, QWidget
)


class Ui_RegistroView(object):
    def setupUi(self, RegistroView):
        if not RegistroView.objectName():
            RegistroView.setObjectName("RegistroView")
        RegistroView.resize(420, 560)

        self.vboxLayout = QVBoxLayout(RegistroView)

        # -------- TÍTULO --------
        self.labelTitulo = QLabel(RegistroView)
        self.labelTitulo.setObjectName("labelTitulo")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setAlignment(Qt.AlignCenter)
        self.vboxLayout.addWidget(self.labelTitulo)

        # -------- CAMPOS --------
        self.inputNombre = QLineEdit(RegistroView)
        self.inputNombre.setObjectName("inputNombre")
        self.vboxLayout.addWidget(self.inputNombre)

        self.inputApellidos = QLineEdit(RegistroView)
        self.inputApellidos.setObjectName("inputApellidos")
        self.vboxLayout.addWidget(self.inputApellidos)

        self.inputUsername = QLineEdit(RegistroView)
        self.inputUsername.setObjectName("inputUsername")
        self.vboxLayout.addWidget(self.inputUsername)

        self.inputEmail = QLineEdit(RegistroView)
        self.inputEmail.setObjectName("inputEmail")
        self.vboxLayout.addWidget(self.inputEmail)

        self.inputTelefono = QLineEdit(RegistroView)
        self.inputTelefono.setObjectName("inputTelefono")
        self.vboxLayout.addWidget(self.inputTelefono)

        self.comboCiudad = QComboBox(RegistroView)
        self.comboCiudad.setObjectName("comboCiudad")
        self.vboxLayout.addWidget(self.comboCiudad)

        self.dateNacimiento = QDateEdit(RegistroView)
        self.dateNacimiento.setObjectName("dateNacimiento")
        self.dateNacimiento.setCalendarPopup(True)
        self.vboxLayout.addWidget(self.dateNacimiento)

        self.inputPassword = QLineEdit(RegistroView)
        self.inputPassword.setObjectName("inputPassword")
        self.inputPassword.setEchoMode(QLineEdit.Password)
        self.vboxLayout.addWidget(self.inputPassword)

        self.inputPassword2 = QLineEdit(RegistroView)
        self.inputPassword2.setObjectName("inputPassword2")
        self.inputPassword2.setEchoMode(QLineEdit.Password)
        self.vboxLayout.addWidget(self.inputPassword2)

        self.labelMensaje = QLabel(RegistroView)
        self.labelMensaje.setObjectName("labelMensaje")
        self.labelMensaje.setVisible(False)
        self.labelMensaje.setAlignment(Qt.AlignCenter)
        self.vboxLayout.addWidget(self.labelMensaje)

        self.btnRegistrarse = QPushButton(RegistroView)
        self.btnRegistrarse.setObjectName("btnRegistrarse")
        self.vboxLayout.addWidget(self.btnRegistrarse)

        self.btnIrLogin = QPushButton(RegistroView)
        self.btnIrLogin.setObjectName("btnIrLogin")
        self.vboxLayout.addWidget(self.btnIrLogin)

        self.retranslateUi(RegistroView)

    def retranslateUi(self, RegistroView):
        RegistroView.setWindowTitle(
            QCoreApplication.translate("RegistroView", "Kilómetro a Kilómetro - Registro")
        )

        RegistroView.setStyleSheet("""
            QWidget {
                background-color: #1b1b1b;
                color: #eaeaea;
                font-family: Segoe UI;
            }
            QLabel#labelTitulo {
                color: #00c853;
                margin-bottom: 10px;
            }
            QLineEdit, QComboBox, QDateEdit {
                background-color: #2a2a2a;
                border: 2px solid #3a3a3a;
                border-radius: 6px;
                padding: 8px;
                font-size: 14px;
            }
            QPushButton {
                background-color: #00c853;
                border-radius: 8px;
                padding: 12px;
                font-weight: bold;
                color: #000000;
            }
            QPushButton:hover {
                background-color: #00e676;
            }
            QPushButton#btnIrLogin {
                background-color: transparent;
                color: #9e9e9e;
                font-weight: normal;
            }
            QPushButton#btnIrLogin:hover {
                color: #00e676;
                text-decoration: underline;
            }
        """)

        self.labelTitulo.setText(
            QCoreApplication.translate("RegistroView", "Crear cuenta")
        )
        self.inputNombre.setPlaceholderText("Nombre")
        self.inputApellidos.setPlaceholderText("Apellidos")
        self.inputUsername.setPlaceholderText("Usuario")
        self.inputEmail.setPlaceholderText("Email")
        self.inputTelefono.setPlaceholderText("Teléfono")
        self.inputPassword.setPlaceholderText("Contraseña")
        self.inputPassword2.setPlaceholderText("Repetir contraseña")
        self.btnRegistrarse.setText("Registrar")
        self.btnIrLogin.setText("Ya tengo cuenta")
