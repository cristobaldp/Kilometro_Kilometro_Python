import requests


class GasolinerasApiRepository:

    URL = (
        "https://sedeaplicaciones.minetur.gob.es/"
        "ServiciosRESTCarburantes/PreciosCarburantes/"
        "EstacionesTerrestres/"
    )

    def obtener_gasolineras(self):
        response = requests.get(self.URL, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("ListaEESSPrecio", [])
