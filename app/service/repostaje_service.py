from app.repository.repostaje_repository import RepostajeRepository


class RepostajeService:

    def __init__(self):
        self.repo = RepostajeRepository()

    def listar(self, vehiculo_id):
        return self.repo.find_by_vehiculo(vehiculo_id)

    def insertar(self, vehiculo_id, fecha, litros, precio_total, kilometros):
        self.repo.insert(
            vehiculo_id,
            fecha,
            litros,
            precio_total,
            kilometros
        )

    def ultimo_kilometraje(self, vehiculo_id):
        return self.repo.ultimo_kilometraje(vehiculo_id)
    
    def eliminar(self, repostaje_id):
        self.repo.delete(repostaje_id)
    
    def obtener_para_exportar(self, vehiculo_id):
        return self.repo.find_by_vehiculo(vehiculo_id)
    
