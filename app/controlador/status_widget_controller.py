from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Signal, Qt
from pathlib import Path


class StatusWidgetController(QWidget):

    accepted = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        # Para que se vea bien sobre otros widgets
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.hide()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        loader = QUiLoader()

        # Ruta segura a la UI
        base_path = Path(__file__).resolve().parent.parent
        ui_path = base_path / "vista" / "status_widget.ui"

        file = QFile(str(ui_path))
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file, self)
        file.close()

        layout.addWidget(self.ui)

        # Referencias rápidas
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
            self.card.setStyleSheet("background:#E8F5E9; border-radius:14px;")
            self.button.setVisible(True)
            self.button.setText(button_text)

        elif status == "error":
            self.icon.setText("✖")
            self.title.setText("Error")
            self.card.setStyleSheet("background:#FDECEA; border-radius:14px;")
            self.button.setVisible(True)
            self.button.setText(button_text)

        elif status == "loading":
            self.icon.setText("⏳")
            self.title.setText("Cargando…")
            self.card.setStyleSheet("background:#E3F2FD; border-radius:14px;")
            self.button.setVisible(False)

    def on_accept(self):
        self.hide()
        self.accepted.emit()
