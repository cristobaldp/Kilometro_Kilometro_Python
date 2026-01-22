import os
import json

from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineProfile
from PySide6.QtCore import QUrl, Slot
from PySide6.QtWebChannel import QWebChannel

from app.vista.mapa_gasolineras_ui import Ui_MapaGasolineras


class MapaGasolinerasView(QWidget):

    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        # ==========================
        # CARGAR UI
        # ==========================
        self.ui = Ui_MapaGasolineras()
        self.ui.setupUi(self)

        # ==========================
        # BOTÓN VOLVER
        # ==========================
        self.ui.btnVolver.clicked.connect(self.volver_menu)

        # ==========================
        # CONTENEDOR DEL MAPA
        # ==========================
        layout = QVBoxLayout(self.ui.mapaWidget)

        self.web = QWebEngineView()
        layout.addWidget(self.web)

        perfil = QWebEngineProfile.defaultProfile()
        perfil.settings().setAttribute(
            perfil.settings().WebAttribute.LocalContentCanAccessRemoteUrls,
            True
        )

        # ==========================
        # WEB CHANNEL
        # ==========================
        self.channel = QWebChannel()
        self.channel.registerObject("backend", self)
        self.web.page().setWebChannel(self.channel)

        # ==========================
        # CARGAR HTML DEL MAPA
        # ==========================
        html = os.path.abspath("app/reports/mapa_base.html")
        self.web.setUrl(QUrl.fromLocalFile(html))

    # ==================================================
    # BOTÓN VOLVER → CONTROLLER
    # ==================================================
    def volver_menu(self):
        self.controller.volver_menu()

    # ==================================================
    # JS → PYTHON
    # ==================================================
    @Slot(str)
    def buscarLocalidad(self, localidad):
        self.controller.buscar_localidad(localidad)

    # ==================================================
    # PYTHON → JS
    # ==================================================
    def actualizar_marcadores(self, datos):
        script = f"actualizarMarcadores({json.dumps(datos)});"
        self.web.page().runJavaScript(script)
