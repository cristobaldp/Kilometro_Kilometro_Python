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
👤 Gestión de Usuarios
Registro seguro: Creación de nuevas cuentas validando duplicados de usuario o email vía API.

Inicio de sesión unificado: Validación de credenciales con contraseñas hasheadas en SHA-256 compatibles entre el entorno local y la API.

Perfil: Edición de datos personales y actualización de contraseñas de acceso.

🚙 Control de Vehículos
Garaje virtual: Permite añadir, editar y eliminar múltiples vehículos por cuenta de usuario.

Ficha técnica básica: Registro de marca, modelo, matrícula, año de fabricación, tipo de combustible y consumo estimado.

Vehículo activo: Configuración de un vehículo principal para segmentar los cálculos de repostajes y analíticas de manera independiente.

⛽ Registro de Repostajes
Control detallado: Almacenamiento preciso de fecha, litros introducidos, precio total abonado y kilometraje acumulado.

Métrica inteligente: Cálculo automatizado del consumo real de combustible en base a la diferencia de kilómetros entre repostajes consecutivos.

Historial dinámico: Panel visual con histórico de operaciones totalmente filtrable por mes y año.

📊 Módulo de Estadísticas
Analítica gráfica: Gráficos interactivos que reflejan la evolución del gasto mensual y el histórico del consumo real.

Filtros temporales: Segmentación por períodos de tiempo para evaluar el impacto económico de tus trayectos cotidianos o comerciales.

🗺️ Mapa de gasolineras (Opcional)
Consulta de precios: Localización de estaciones de servicio vía API oficial del Geoportal de Gasolineras.

Búsqueda predictiva: Filtrado dinámico por localidad para encontrar los combustibles más económicos.

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
