# 🚗 Kilómetro a Kilómetro

**Controla tu gasto, conduce con cabeza**

Kilómetro a Kilómetro es una aplicación multiplataforma desarrollada en Python que combina una **interfaz de escritorio (PySide6)** y una **API Backend (FastAPI)** para la gestión del consumo de combustible y el control de gastos de uno o varios vehículos. Está orientada tanto a conductores particulares como a pequeños negocios que buscan una herramienta sencilla, privada y eficaz.

---

## 🎯 Objetivos del proyecto

- Registrar repostajes (fecha, litros, precio, kilometraje).
- Calcular automáticamente el consumo medio.
- Visualizar estadísticas y evolución del gasto en tiempo real.
- Gestionar múltiples vehículos desde una misma cuenta de usuario.
- Sistema seguro y unificado de registro y login (Local + API).
- Consulta opcional de precios de combustible en gasolineras cercanas (API oficial).

---

## 🧰 Tecnologías utilizadas

| Área | Tecnología |
| :--- | :--- |
| **Lenguaje** | Python 3.9+ |
| **Interfaz Gráfica** | PySide6 (Qt for Python) + Qt Designer |
| **Backend & API** | FastAPI + Uvicorn |
| **Base de Datos** | SQLite3 |
| **Arquitectura** | MVC (Modelo-Vista-Controlador) híbrido |
| **Gráficos** | Matplotlib / QtCharts |
| **Control de Versiones** | Git + GitHub |
| **APIs Externas** | Geoportal de Gasolineras (Ministerio de España) |

---

## 📁 Estructura del proyecto

El proyecto integra tanto el cliente de escritorio como los servicios de la API dentro de una estructura unificada y limpia:

```text
Kilometro_Kilometro_Python/
├── main.py                 # Punto de entrada principal (Inicia API + Escritorio)
├── requirements.txt        # Dependencias del proyecto
└── app/                    # Directorio raíz de la aplicación
    ├── api.py              # Endpoints y lógica de FastAPI
    ├── database.py         # Configuración y ruta de la base de datos SQLite
    ├── controlador/        # Controladores de la interfaz PySide6
    ├── vista/              # Archivos .ui y vistas de usuario
    └── data/               # Scripts de inicialización y almacenamiento de la BD




🔐 Funcionalidades principales
👤 Usuarios
Registro e inicio de sesión seguro (contraseñas hasheadas localmente y validadas vía API).

Edición de perfil y cambio de contraseña.

🚙 Vehículos
Añadir, editar y eliminar vehículos de tu garaje virtual.

Selección de vehículo activo para el cálculo de estadísticas individuales.

⛽ Repostajes
Registro detallado de repostajes (litros, precio total, kilómetros acumulados, fecha).

Cálculo automático del consumo real entre repostajes consecutivos usando diferencias de kilometraje.

Historial dinámico filtrable por mes y año.

📊 Estadísticas
Gráficos interactivos de gasto mensual y consumo real de combustible.

Filtros por período para controlar el impacto económico de tus trayectos.

🗺️ Mapa de gasolineras (Opcional)
Consulta de precios y localización de estaciones de servicio vía API oficial del Geoportal de Gasolineras.

Búsqueda predictiva por localidad.

📱 Evolución prevista
Gracias a la implementación de FastAPI en el núcleo de la estructura, la lógica de negocio ya está completamente desacoplada de la interfaz gráfica, lo que permitirá su adaptación inmediata a:

📲 Aplicación móvil nativa en Android (Kotlin + Jetpack Compose) consumiendo el backend actual.

🌐 Versión web oficial.

☁️ Sincronización híbrida (base de datos local replicada en la nube).

🚀 Cómo ejecutar el proyecto
Requisitos previos
Python 3.9 o superior.

Pip (gestor de paquetes de Python).

Instalación y despliegue
Clonar el repositorio:

Bash
git clone [https://github.com/cristobaldp/Kilometro_Kilometro_Python.git](https://github.com/cristobaldp/Kilometro_Kilometro_Python.git)
cd Kilometro_Kilometro_Python
Crear y activar un entorno virtual (Recomendado):

Bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En Linux/macOS
python3 -m venv venv
source venv/bin/activate
Instalar las dependencias oficiales:

Bash
pip install -r requirements.txt
Lanzar la aplicación:

Bash
python main.py
