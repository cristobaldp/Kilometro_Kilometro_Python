import sys
import subprocess
import time
from PySide6.QtWidgets import QApplication

from app.controlador.app_controller import AppController
from app.data.init_db import init_db


def main():
    # 1. Inicializar base de datos (crear tablas si no existen)
    init_db()

    # 2. ARRANCAR LA API EN SEGUNDO PLANO AUTOMÁTICAMENTE
    print("Iniciando API de FastAPI desde subproceso...")
    # CORREGIDO: Cambiado "main:app" por "api:app" para que busque tu archivo api.py
    api_process = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "api:app", "--host", "127.0.0.1", "--port", "8000"],
        cwd="app"
    )
    
    # Pausa de 1.5 segundos para asegurar que el puerto 8000 responda antes de abrir la interfaz
    time.sleep(1.5)

    # 3. Arrancar aplicación Qt
    app = QApplication(sys.argv)

    controller = AppController()
    controller.mostrar_login()

    # Capturar el código de cierre de la app de escritorio
    exit_code = app.exec()

    # 4. AL CERRAR LA VENTANA, SE APAGA LA API AUTOMÁTICAMENTE
    print("Cerrando el proceso de la API...")
    api_process.terminate()

    sys.exit(exit_code)


if __name__ == "__main__":
    main()