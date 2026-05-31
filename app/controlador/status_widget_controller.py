from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, Qt

from app.vista.status_widget_ui import Ui_StatusWidget


class StatusWidgetController(QWidget):

    accepted = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.ui = Ui_StatusWidget()
        self.ui.setupUi(self)

        self.hide()

        self.icon = self.ui.iconLabel
        self.title = self.ui.titleLabel
        self.message = self.ui.messageLabel
        self.button = self.ui.actionButton
        self.card = self.ui.cardFrame

        self.button.clicked.connect(self.on_accept)

    def set_status(self, status, message="", button_text="Aceptar"):
        self.show()
        self.raise_()

        self.message.setText(message)

        if status == "success":
            self.icon.setText("✔")
            self.title.setText("Operación completada")
            self.card.setStyleSheet(
                "background:#E8F5E9; border-radius:14px;"
            )
            self.button.setVisible(True)
            self.button.setText(button_text)

        elif status == "error":
            self.icon.setText("✖")
            self.title.setText("Error")
            self.card.setStyleSheet(
                "background:#FDECEA; border-radius:14px;"
            )
            self.button.setVisible(True)
            self.button.setText(button_text)

        elif status == "loading":
            self.icon.setText("⏳")
            self.title.setText("Cargando…")
            self.card.setStyleSheet(
                "background:#E3F2FD; border-radius:14px;"
            )
            self.button.setVisible(False)

    def on_accept(self):
        self.hide()
        self.accepted.emit()