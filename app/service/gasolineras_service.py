from geopy.distance import geodesic
from geopy.geocoders import Nominatim


class GasolinerasService:

    def __init__(self, repository):
        self.repository = repository
        self.gasolineras = repository.obtener_gasolineras()
        self.geolocator = Nominatim(user_agent="kilometro_kilometro")

    def buscar_por_localidad(self, localidad, radio_km=10):
        ubicacion = self.geolocator.geocode(localidad)

        if not ubicacion:
            return None

        lat, lon = ubicacion.latitude, ubicacion.longitude
        resultados = []

        for g in self.gasolineras:
            try:
                lat_g = float(g["Latitud"].replace(",", "."))
                lon_g = float(g["Longitud (WGS84)"].replace(",", "."))

                distancia = geodesic(
                    (lat, lon), (lat_g, lon_g)
                ).km

                if distancia <= radio_km:
                    resultados.append({
                        "nombre": g.get("Rótulo", "Gasolinera"),
                        "direccion": g.get("Dirección", ""),
                        "lat": lat_g,
                        "lon": lon_g,
                        "dist": round(distancia, 2),

                        #  TODOS LOS PRECIOS 
                        "precio95": g.get("Precio Gasolina 95 E5", "N/D"),
                        "precio95_10": g.get("Precio Gasolina 95 E10", "N/D"),
                        "precio98": g.get("Precio Gasolina 98 E5", "N/D"),
                        "precio98_10": g.get("Precio Gasolina 98 E10", "N/D"),
                        "precioDieselA": g.get("Precio Gasoleo A", "N/D"),
                        "precioDieselPremium": g.get("Precio Gasoleo Premium", "N/D"),
                        "precioGLP": g.get("Precio GLP", "N/D"),
                        "precioGNC": g.get("Precio Gas Natural Comprimido", "N/D"),
                        "precioGNL": g.get("Precio Gas Natural Licuado", "N/D"),
                        "precioHidrogeno": g.get("Precio Hidrogeno", "N/D")
                    })
            except Exception:
                pass

        return {
            "centro": {"lat": lat, "lon": lon},
            "lista": resultados
        }
