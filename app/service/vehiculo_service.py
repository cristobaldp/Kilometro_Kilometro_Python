from app.repository.vehiculo_repository import VehiculoRepository


class VehiculoService:

    def __init__(self):
        self.repo = VehiculoRepository()

    # -------------------------
    # LISTAR VEHÍCULOS
    # -------------------------
    def listar(self, user_id):
        return self.repo.find_by_user(user_id)

    # -------------------------
    # INSERTAR VEHÍCULO
    # -------------------------
    def insertar(self, user_id, tipo, marca, modelo, matricula, anio, combustible, consumo):
        return self.repo.insert(
            user_id,
            tipo,
            marca,
            modelo,
            matricula,
            anio,
            combustible,
            consumo
        )

    # -------------------------
    # ELIMINAR VEHÍCULO
    # -------------------------
    def eliminar(self, vehiculo_id):
        return self.repo.delete(vehiculo_id)

    # -------------------------
    # MARCAR VEHÍCULO ACTIVO
    # -------------------------
    def marcar_activo(self, user_id, vehiculo_id):
        return self.repo.set_activo(user_id, vehiculo_id)

    # -------------------------
    # QUITAR VEHÍCULO ACTIVO
    # -------------------------
    def quitar_activo(self, user_id):
        return self.repo.clear_activo(user_id)
    
    # -------------------------
# OBTENER VEHÍCULO POR ID
# -------------------------
    def obtener_por_id(self, vehiculo_id):
     return self.repo.find_by_id(vehiculo_id)

