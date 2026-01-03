# app/service/estadisticas_service.py
from app.repository.estadisticas_repository import EstadisticasRepository


class EstadisticasService:

    def __init__(self):
        self.repo = EstadisticasRepository()

    def obtener_gasto(self, vehiculo_id, anio):
        return self.repo.gasto_por_mes(vehiculo_id, anio)

    def obtener_consumo(self, vehiculo_id, anio):
        return self.repo.consumo_por_mes(vehiculo_id, anio)
