from app.repository.estadisticas_repository import EstadisticasRepository


class EstadisticasService:

    def __init__(self):
        self.repo = EstadisticasRepository()

    def obtener_gasto(self, vehiculo_id, mes, anio):
        return self.repo.gasto_diario(vehiculo_id, mes, anio)

    def obtener_consumo(self, vehiculo_id, mes, anio):
        return self.repo.consumo_diario(vehiculo_id, mes, anio)
