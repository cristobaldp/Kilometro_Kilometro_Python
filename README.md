# 🚗 Kilómetro a Kilómetro

**Controla tu gasto, conduce con cabeza**

Kilómetro a Kilómetro es una aplicación de escritorio desarrollada en Python para la gestión del consumo de combustible y el control de gastos de uno o varios vehículos. Está orientada tanto a conductores particulares como a pequeños negocios que buscan una herramienta sencilla, privada y eficaz.

---

## 🎯 Objetivos del proyecto

- Registrar repostajes (fecha, litros, precio, kilometraje).
- Calcular automáticamente el consumo medio.
- Visualizar estadísticas y evolución del gasto.
- Gestionar múltiples vehículos desde una misma cuenta.
- Sistema seguro de registro y login de usuarios.
- Consulta opcional de precios de combustible en gasolineras cercanas (API oficial).

---

## 🧰 Tecnologías utilizadas

| Área               | Tecnología                          |
|--------------------|-------------------------------------|
| Lenguaje           | Python 3.9.13                       |
| Interfaz gráfica   | PySide6 (Qt for Python) + Qt Designer |
| Base de datos      | SQLite                              |
| Arquitectura       | MVC (Modelo-Vista-Controlador)      |
| Gráficos           | Matplotlib / QtCharts               |
| Control de versiones | Git + GitHub                      |
| APIs externas      | Geoportal de Gasolineras (España)   |

---

## 📁 Estructura del proyecto


---

## 🔐 Funcionalidades principales

### 👤 Usuarios
- Registro e inicio de sesión seguro (contraseñas hasheadas con bcrypt).
- Edición de perfil y cambio de contraseña.

### 🚙 Vehículos
- Añadir, editar y eliminar vehículos.
- Asignación de vehículos a cada usuario.

### ⛽ Repostajes
- Registro de repostajes (litros, precio, km, fecha).
- Cálculo automático del consumo real entre repostajes consecutivos.
- Historial filtrable por mes y año.
- Exportación a CSV y PDF.

### 📊 Estadísticas
- Gráficos de gasto mensual y consumo real.
- Filtros por período.
- Exportación de datos.

### 🗺️ Mapa de gasolineras (opcional)
- Consulta de precios y localización de estaciones de servicio vía API oficial.
- Búsqueda por localidad.

---

## 📱 Evolución prevista

Aunque la versión actual es de escritorio, el proyecto está diseñado con una arquitectura modular que permitirá su adaptación futura a:

- 📲 Aplicación móvil nativa en Android (Kotlin + Jetpack Compose).
- 🌐 Versión web opcional.
- ☁️ Sincronización opcional con la nube (sin perder el modo local).

---

## 🧪 Pruebas y validación

La aplicación ha sido probada en entornos Windows y Linux, validando:

- Flujo completo de registro, login y gestión de vehículos.
- Cálculo correcto de consumos.
- Persistencia local de datos.
- Integración con la API de gasolineras.
- Exportación de informes.

---

## 🚀 Cómo ejecutar el proyecto

### Requisitos previos
- Python 3.9 o superior
- pip (gestor de paquetes)

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/cristobaldp/Kilometro_Kilometro_Python.git
cd Kilometro_Kilometro_Python

# Crear y activar entorno virtual (opcional pero recomendado)
python -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
