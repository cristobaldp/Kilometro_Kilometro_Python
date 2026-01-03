from app.service.usuario_service import UsuarioService


class AjustesController:

    def __init__(self, widget, ui, app):
        self.widget = widget
        self.ui = ui
        self.app = app
        self.service = UsuarioService()

        self.cargar_ajustes()

        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.btnVolver.clicked.connect(self.volver)

    # -------------------------
    def cargar_ajustes(self):
        ajustes = self.service.obtener_ajustes(self.app.usuario["id"])

        if not ajustes:
            return

        self.ui.comboUnidadConsumo.setCurrentText(ajustes["unidad_consumo"])
        self.ui.comboFormatoPrecio.setCurrentText(ajustes["formato_precio"])
        self.ui.comboPeriodo.setCurrentText(ajustes["periodo_estadisticas"])
        self.ui.comboVista.setCurrentText(ajustes["vista_estadisticas"])

        self.ui.spinAvisoKm.setValue(ajustes["aviso_km"])
        self.ui.checkAvisoConsumo.setChecked(ajustes["aviso_consumo"])
        self.ui.checkConfirmar.setChecked(ajustes["confirmar_acciones"])
        self.ui.checkCerrarSesion.setChecked(ajustes["cerrar_sesion"])

    # -------------------------
    def guardar(self):
        datos = {
            "unidad_consumo": self.ui.comboUnidadConsumo.currentText(),
            "formato_precio": self.ui.comboFormatoPrecio.currentText(),
            "periodo_estadisticas": self.ui.comboPeriodo.currentText(),
            "vista_estadisticas": self.ui.comboVista.currentText(),
            "aviso_km": self.ui.spinAvisoKm.value(),
            "aviso_consumo": self.ui.checkAvisoConsumo.isChecked(),
            "confirmar_acciones": self.ui.checkConfirmar.isChecked(),
            "cerrar_sesion": self.ui.checkCerrarSesion.isChecked(),
        }

        self.service.guardar_ajustes(self.app.usuario["id"], datos)

        # actualizar en memoria
        self.app.usuario.update(datos)

        self.app.mostrar_menu(self.app.usuario)

    # -------------------------
    def volver(self):
        self.app.mostrar_menu(self.app.usuario)
