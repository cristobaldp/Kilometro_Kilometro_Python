import sys
from PySide6.QtWidgets import QApplication

from app.controlador.app_controller import AppController
from app.data.init_db import init_db


def main():
    # 🔑 1. Inicializar base de datos (crear tablas si no existen)
    init_db()

    # 🔑 2. Arrancar aplicación Qt
    app = QApplication(sys.argv)

    controller = AppController()
    controller.mostrar_login()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
