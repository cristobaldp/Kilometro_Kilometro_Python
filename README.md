# 🚗 Kilómetro a Kilómetro

<div align="center">

### Controla tu gasto, conduce con cabeza

Aplicación multiplataforma desarrollada en **Python** para la gestión inteligente de repostajes, consumo de combustible y control de gastos asociados a vehículos.

Combina una **interfaz de escritorio desarrollada con PySide6** y una **API REST construida con FastAPI**, proporcionando una arquitectura moderna, escalable y preparada para futuras integraciones móviles y web.

---

**Python · FastAPI · PySide6 · SQLite · MVC · REST API**

</div>

---

# 📖 Descripción

**Kilómetro a Kilómetro** es una solución software diseñada para ayudar a conductores particulares y pequeños negocios a llevar un control preciso de los costes asociados al uso de sus vehículos.

La aplicación permite registrar repostajes, analizar consumos reales, visualizar estadísticas de gasto y gestionar múltiples vehículos desde una misma cuenta de usuario.

Su arquitectura desacoplada basada en **FastAPI** permite reutilizar toda la lógica de negocio en futuras aplicaciones móviles, web o servicios en la nube sin necesidad de reescribir el backend.

---

# 🎯 Objetivos del Proyecto

* Registrar repostajes de forma rápida y sencilla.
* Calcular automáticamente el consumo real del vehículo.
* Gestionar múltiples vehículos desde una misma cuenta.
* Visualizar estadísticas y tendencias de gasto.
* Implementar un sistema seguro de autenticación de usuarios.
* Aplicar una arquitectura cliente-servidor moderna.
* Facilitar futuras integraciones móviles y web.

---

# ✨ Funcionalidades Principales

## 👤 Gestión de Usuarios

### Registro Seguro

* Creación de cuentas mediante validación de usuario y correo electrónico.
* Prevención de registros duplicados.
* Almacenamiento seguro de credenciales.

### Inicio de Sesión

* Sistema unificado entre cliente y API.
* Contraseñas protegidas mediante hash SHA-256.
* Validación centralizada de credenciales.

### Gestión de Perfil

* Modificación de datos personales.
* Actualización de contraseña.
* Administración de información de usuario.

---

## 🚙 Gestión de Vehículos

### Garaje Virtual

* Registro de múltiples vehículos.
* Modificación de información existente.
* Eliminación de vehículos.

### Información Técnica

* Marca.
* Modelo.
* Matrícula.
* Año de fabricación.
* Tipo de combustible.
* Consumo estimado.

### Vehículo Activo

* Selección de vehículo principal.
* Estadísticas independientes por vehículo.

---

## ⛽ Gestión de Repostajes

### Registro Completo

Cada repostaje almacena:

* Fecha.
* Litros suministrados.
* Importe abonado.
* Kilometraje acumulado.

### Consumo Real Automático

La aplicación calcula automáticamente:

* Kilómetros recorridos.
* Consumo medio.
* Coste por kilómetro.
* Evolución del gasto.

### Historial Dinámico

* Consulta por meses y años.
* Filtrado avanzado.
* Seguimiento histórico completo.

---

## 📊 Estadísticas y Analítica

### Visualización Gráfica

Generación automática de gráficos para:

* Evolución del gasto mensual.
* Consumo medio.
* Coste por repostaje.
* Historial de combustible.

### Filtros Temporales

Análisis segmentado por:

* Mes.
* Año.
* Periodos personalizados.

---

## 🗺️ Consulta de Gasolineras

Integración con servicios oficiales para:

* Localizar estaciones de servicio.
* Comparar precios.
* Encontrar opciones más económicas.
* Filtrar por localidad.

---

# 🏗 Arquitectura del Sistema

La aplicación sigue una arquitectura híbrida basada en el patrón **MVC (Modelo - Vista - Controlador)** junto con una capa de servicios REST mediante FastAPI.

```text
Usuario
   │
   ▼
Interfaz PySide6
   │
   ▼
Controladores MVC
   │
   ▼
API FastAPI
   │
   ▼
SQLite
```

Esta separación permite:

* Mayor mantenibilidad.
* Escalabilidad futura.
* Reutilización de la lógica de negocio.
* Desarrollo multiplataforma.

---

# 🛠 Tecnologías Utilizadas

| Categoría        | Tecnología               |
| ---------------- | ------------------------ |
| Lenguaje         | Python 3.9+              |
| Interfaz Gráfica | PySide6                  |
| Diseño Visual    | Qt Designer              |
| Backend          | FastAPI                  |
| Servidor         | Uvicorn                  |
| Base de Datos    | SQLite3                  |
| Arquitectura     | MVC                      |
| Gráficos         | Matplotlib / QtCharts    |
| Versionado       | Git                      |
| Repositorio      | GitHub                   |
| APIs Externas    | Geoportal de Gasolineras |

---

# 📁 Estructura del Proyecto

```text
Kilometro_Kilometro_Python/
│
├── main.py
│   └── Punto de entrada principal que inicializa
│       la API FastAPI y la interfaz PySide6.
│
├── requirements.txt
│   └── Dependencias necesarias para la ejecución.
│
└── app/
    │
    ├── api.py
    │   └── Endpoints REST y servicios FastAPI.
    │
    ├── database.py
    │   └── Configuración de SQLite y acceso a datos.
    │
    ├── controlador/
    │   └── Lógica de negocio y controladores MVC.
    │
    ├── vista/
    │   └── Interfaces gráficas y archivos .ui.
    │
    └── data/
        └── Base de datos y scripts de inicialización.
```

---

# 🚀 Instalación

## Clonar el repositorio

```bash
git clone https://github.com/cristobaldp/Kilometro_Kilometro_Python.git

cd Kilometro_Kilometro_Python
```

---

## Crear entorno virtual

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Ejecutar la aplicación

```bash
python main.py
```

Al iniciarse se levantarán automáticamente:

* ⚡ Backend FastAPI
* 🖥️ Cliente de escritorio PySide6
* 🗄️ Base de datos SQLite

---

# 🔒 Seguridad

* Validación centralizada de usuarios.
* Contraseñas almacenadas mediante hash SHA-256.
* Protección frente a registros duplicados.
* Comunicación mediante endpoints controlados.

---

# 🔮 Hoja de Ruta

El proyecto está diseñado para evolucionar hacia:

### 📱 Aplicación Android

* Kotlin
* Jetpack Compose
* Consumo de la API existente

### 🌐 Plataforma Web

* Frontend web conectado al backend actual.

### ☁️ Sincronización en la Nube

* Almacenamiento híbrido.
* Copias de seguridad automáticas.
* Acceso multidispositivo.

### 📈 Analítica Avanzada

* Predicción de gastos.
* Comparativas históricas.
* Informes exportables.

---

# 👨‍💻 Autor

## Cristóbal Delgado

Desarrollador de Aplicaciones Multiplataforma.

Proyecto desarrollado con el objetivo de aplicar conocimientos de:

* Desarrollo de Software
* Arquitectura Cliente-Servidor
* APIs REST
* Bases de Datos
* Interfaces Gráficas
* Desarrollo Multiplataforma

---

<div align="center">

### ⭐ Si este proyecto te resulta interesante, considera darle una estrella en GitHub.

</div>
