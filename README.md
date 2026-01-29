# ApexStore API

API REST para gestión de categorías, productos e imágenes de una tienda electrónica.

## Requisitos

- Python 3.10+
- PostgreSQL 17+

## Instalación Rápida

```bash
# 1. Crear virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# 2. Instalar dependencias
pip install -e .

# 3. Configurar variables de entorno
# Crear archivo .env en la raíz:
DATABASE_URL=postgresql+asyncpg://usuario:contraseña@localhost:5432/apexstore
DB_HOST=localhost
DB_PORT=5432
DB_NAME=apexstore
DB_USER=usuario
DB_PASSWORD=contraseña

# 4. Iniciar servidor
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Uso de la API

### URL Base
```
http://localhost:8000/api/v1
```

### Documentación Interactiva
- Swagger: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Endpoints Disponibles

### Categorías

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/categorias` | Listar todas las categorías |
| GET | `/categorias/{id}` | Obtener categoría por ID |
| POST | `/categorias` | Crear categoría |
| PUT | `/categorias/{id}` | Actualizar categoría |
| DELETE | `/categorias/{id}` | Eliminar categoría |

### Productos

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/productos` | Listar todos los productos |
| GET | `/productos/{id}` | Obtener producto por ID |
| POST | `/productos` | Crear producto |
| PUT | `/productos/{id}` | Actualizar producto |
| DELETE | `/productos/{id}` | Eliminar producto |

### Imágenes

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/imagenes` | Listar todas las imágenes |
| GET | `/imagenes/producto/{producto_id}` | Obtener imágenes de un producto |
| POST | `/imagenes` | Crear imagen |
| PUT | `/imagenes/{id}` | Actualizar imagen |
| DELETE | `/imagenes/{id}` | Eliminar imagen |

## Ejemplos de Uso

### Crear una categoría
```bash
curl -X POST http://localhost:8000/api/v1/categorias \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Electrónica", "descripcion": "Productos electrónicos"}'
```

### Crear un producto
```bash
curl -X POST http://localhost:8000/api/v1/productos \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Laptop Dell XPS",
    "descripcion": "Laptop de alto rendimiento",
    "precio": 1299.99,
    "stock": 15,
    "id_categoria": 1
  }'
```

### Obtener todos los productos
```bash
curl http://localhost:8000/api/v1/productos
```

### Actualizar un producto
```bash
curl -X PUT http://localhost:8000/api/v1/productos/1 \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Laptop Dell XPS 15",
    "descripcion": "Actualizado",
    "precio": 1399.99,
    "stock": 20,
    "id_categoria": 1
  }'
```

### Eliminar un producto
```bash
curl -X DELETE http://localhost:8000/api/v1/productos/1
```

## Estructura de Solicitudes y Respuestas

### Crear Categoría

**Request:**
```json
{
  "nombre": "Electrónica",
  "descripcion": "Productos electrónicos"
}
```

**Response (201):**
```json
{
  "id_categoria": 1,
  "nombre": "Electrónica",
  "descripcion": "Productos electrónicos"
}
```

### Crear Producto

**Request:**
```json
{
  "nombre": "Laptop Dell XPS",
  "descripcion": "Laptop de alto rendimiento",
  "precio": 1299.99,
  "stock": 15,
  "id_categoria": 1
}
```

**Response (201):**
```json
{
  "id_producto": 1,
  "nombre": "Laptop Dell XPS",
  "descripcion": "Laptop de alto rendimiento",
  "precio": 1299.99,
  "stock": 15,
  "id_categoria": 1,
  "categoria": {
    "id_categoria": 1,
    "nombre": "Electrónica",
    "descripcion": "Productos electrónicos"
  },
  "imagenes": []
}
```

### Crear Imagen

**Request:**
```json
{
  "url_imagen": "https://ejemplo.com/imagen.jpg",
  "es_principal": true,
  "orden": 1,
  "id_producto": 1
}
```

**Response (201):**
```json
{
  "id_imagen": 1,
  "url_imagen": "https://ejemplo.com/imagen.jpg",
  "es_principal": true,
  "orden": 1,
  "id_producto": 1
}
```

## Códigos de Respuesta

| Código | Significado |
|--------|------------|
| 200 | Éxito - Operación completada |
| 201 | Éxito - Recurso creado |
| 204 | Éxito - Eliminado sin contenido |
| 404 | Error - Recurso no encontrado |
| 400 | Error - Solicitud inválida |

## Para Más Información

Consultar el archivo `DOCUMENTACION.md` para la documentación técnica completa, arquitectura detallada y decisiones de diseño.

---

## Descripción General

**ApexStore API** es una interfaz de programación de aplicaciones (API) RESTful desarrollada con FastAPI que gestiona un catálogo de productos para una tienda electrónica. La API proporciona funcionalidades para la administración de categorías, productos e imágenes asociadas a estos.

**Versión:** 1.0.0  
**Framework:** FastAPI 0.128.0  
**Lenguaje:** Python 3.14+  
**Estilo Arquitectónico:** API REST con patrón de capas

---

## Arquitectura del Proyecto

El proyecto implementa una arquitectura de capas que promueve la separación de responsabilidades y facilita el mantenimiento y escalabilidad:

```
┌─────────────────────────────────────────┐
│        Routers (API Endpoints)          │
│  (app/api/v1/routers/)                  │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│       Services (Lógica de Negocio)      │
│  (app/services/)                        │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│    Repositories (Acceso a Datos)        │
│  (app/repositories/)                    │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│     Models (Modelos SQLAlchemy)         │
│  (app/models/)                          │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│         Base de Datos PostgreSQL        │
└─────────────────────────────────────────┘
```

---

## Estructura de Carpetas

```
apexstore-api/
│
├── main.py                          # Script de prueba de conexión a BD
│
├── pyproject.toml                   # Configuración del proyecto y dependencias
│
├── README.md                        # Información general del proyecto
│
├── DOCUMENTACION.md                 # Este archivo
│
└── app/
    │
    ├── main.py                      # Punto de entrada de la aplicación FastAPI
    │
    ├── api/
    │   └── v1/
    │       ├── __init__.py          # Inicializa routers de v1
    │       └── routers/
    │           ├── __init__.py
    │           ├── productos.py     # Endpoints de productos
    │           ├── categorias.py    # Endpoints de categorías
    │           └── imagenes.py      # Endpoints de imágenes
    │
    ├── core/
    │   ├── __init__.py
    │   ├── config.py                # Configuración de la aplicación
    │   └── database.py              # Configuración de la base de datos
    │
    ├── dependencies/
    │   ├── __init__.py
    │   └── db.py                    # Dependencia de sesión de base de datos
    │
    ├── models/
    │   ├── __init__.py
    │   ├── base.py                  # Clase base para modelos SQLAlchemy
    │   ├── categoria.py             # Modelo ORM de Categoría
    │   ├── producto.py              # Modelo ORM de Producto
    │   └── imagen.py                # Modelo ORM de Imagen de Producto
    │
    ├── repositories/
    │   ├── __init__.py
    │   ├── categoria_repo.py        # Repositorio de Categorías
    │   ├── producto_repo.py         # Repositorio de Productos
    │   └── imagen_repo.py           # Repositorio de Imágenes
    │
    ├── schemas/
    │   ├── __init__.py
    │   ├── categoria.py             # Esquemas Pydantic de Categoría
    │   ├── producto.py              # Esquemas Pydantic de Producto
    │   └── imagen.py                # Esquemas Pydantic de Imagen
    │
    └── services/
        ├── __init__.py
        ├── categoria_service.py     # Lógica de negocio de Categorías
        ├── producto_service.py      # Lógica de negocio de Productos
        └── imagen_service.py        # Lógica de negocio de Imágenes
```

---

## Dependencias

El proyecto utiliza las siguientes dependencias principales:

| Dependencia | Versión | Propósito |
|------------|---------|----------|
| **FastAPI** | >= 0.128.0 | Framework web para crear APIs REST |
| **Uvicorn** | >= 0.40.0 | Servidor ASGI para ejecutar la aplicación |
| **SQLAlchemy** | >= 2.0.46 | ORM para interactuar con la base de datos |
| **AsyncPG** | >= 0.31.0 | Driver asincrónico para PostgreSQL |
| **Psycopg** | >= 3.3.2 | Adaptador de PostgreSQL para Python |
| **Pydantic** | (incluida en FastAPI) | Validación de datos y serialización |
| **Pydantic Settings** | >= 2.12.0 | Gestión de configuración mediante variables de entorno |
| **Python Dotenv** | >= 0.9.9 | Carga de variables de entorno desde archivo .env |

---

## Modelos de Datos

### Categoría

Representa una categoría de productos en el sistema.

```python
class Categoria(Base):
    __tablename__ = "categorias"
    
    id_categoria: int          # Identificador único (Clave primaria)
    nombre: str                # Nombre de la categoría (máx 100 caracteres)
    descripcion: str | None    # Descripción opcional (máx 255 caracteres)
```

**Relaciones:**
- `productos`: Relación uno-a-muchos con la tabla de productos

---

### Producto

Representa un producto disponible en la tienda.

```python
class Producto(Base):
    __tablename__ = "productos"
    
    id_producto: int           # Identificador único (Clave primaria)
    nombre: str                # Nombre del producto (máx 150 caracteres)
    descripcion: str | None    # Descripción opcional (máx 255 caracteres)
    precio: float              # Precio unitario (Numeric 10,2)
    stock: int                 # Cantidad disponible (Restricción: stock >= 0)
    id_categoria: int          # Referencia a categoría (Clave foránea)
```

**Restricciones:**
- `CheckConstraint("stock >= 0")`: El stock no puede ser negativo

**Relaciones:**
- `categoria`: Relación muchos-a-uno con Categoría
- `imagenes`: Relación uno-a-muchos con Imagen de Producto (con cascada de eliminación)

---

### Imagen de Producto

Almacena imágenes asociadas a cada producto.

```python
class ImagenProducto(Base):
    __tablename__ = "imagenes_producto"
    
    id_imagen: int             # Identificador único (Clave primaria)
    url_imagen: str            # URL o ruta de la imagen
    es_principal: bool         # Indica si es la imagen principal (default: False)
    orden: int                 # Orden de visualización (default: 1)
    id_producto: int           # Referencia al producto (Clave foránea)
```

**Relaciones:**
- `producto`: Relación muchos-a-uno con Producto

---

## Esquemas de Validación

Los esquemas Pydantic definen la estructura de los datos que se envían y reciben en la API.

### CategoriaBase

```python
class CategoriaBase(BaseModel):
    nombre: str
    descripcion: str | None = None
```

### CategoriaOut

```python
class CategoriaOut(CategoriaBase):
    id_categoria: int
    
    class Config:
        from_attributes = True  # Permite crear instancias desde objetos ORM
```

---

### ProductoBase

```python
class ProductoBase(BaseModel):
    nombre: str
    descripcion: str | None = None
    precio: float
    stock: int
    id_categoria: int
```

### ProductoOut

```python
class ProductoOut(ProductoBase):
    id_producto: int
    categoria: CategoriaOut
    imagenes: List[ImagenProductoOut] = []
    
    class Config:
        from_attributes = True
```

---

### ImagenProductoCreate

```python
class ImagenProductoCreate(BaseModel):
    url_imagen: str
    es_principal: bool = False
    orden: int = 1
    id_producto: int
```

### ImagenProductoOut

```python
class ImagenProductoOut(BaseModel):
    id_imagen: int
    url_imagen: str
    es_principal: bool
    orden: int
    id_producto: int
    
    class Config:
        from_attributes = True
```

---

## Endpoints de la API

### Base URL
```
http://localhost:8000/api/v1
```

### Documentación Interactiva
- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

---

### Categorías

#### GET /categorias
**Descripción:** Obtiene la lista de todas las categorías

**Parámetros:** Ninguno

**Respuesta exitosa (200):**
```json
[
    {
        "id_categoria": 1,
        "nombre": "Electrónica",
        "descripcion": "Productos electrónicos varios"
    }
]
```

---

#### GET /categorias/{categoria_id}
**Descripción:** Obtiene una categoría específica por ID

**Parámetros:**
- `categoria_id` (path, requerido): ID de la categoría

**Respuesta exitosa (200):**
```json
{
    "id_categoria": 1,
    "nombre": "Electrónica",
    "descripcion": "Productos electrónicos varios"
}
```

**Errores:**
- `404 Not Found`: Categoría no encontrada

---

#### POST /categorias
**Descripción:** Crea una nueva categoría

**Body (requerido):**
```json
{
    "nombre": "Electrónica",
    "descripcion": "Productos electrónicos varios"
}
```

**Respuesta exitosa (201):**
```json
{
    "id_categoria": 1,
    "nombre": "Electrónica",
    "descripcion": "Productos electrónicos varios"
}
```

---

#### PUT /categorias/{categoria_id}
**Descripción:** Actualiza una categoría existente

**Parámetros:**
- `categoria_id` (path, requerido): ID de la categoría

**Body (requerido):**
```json
{
    "nombre": "Electrónica Actualizada",
    "descripcion": "Descripción nueva"
}
```

**Respuesta exitosa (200):**
```json
{
    "id_categoria": 1,
    "nombre": "Electrónica Actualizada",
    "descripcion": "Descripción nueva"
}
```

**Errores:**
- `404 Not Found`: Categoría no encontrada

---

#### DELETE /categorias/{categoria_id}
**Descripción:** Elimina una categoría

**Parámetros:**
- `categoria_id` (path, requerido): ID de la categoría

**Respuesta exitosa (204):** Sin contenido

**Errores:**
- `404 Not Found`: Categoría no encontrada

---

### Productos

#### GET /productos
**Descripción:** Obtiene la lista de todos los productos con sus categorías e imágenes

**Parámetros:** Ninguno

**Respuesta exitosa (200):**
```json
[
    {
        "id_producto": 1,
        "nombre": "Laptop Dell XPS",
        "descripcion": "Laptop de alto rendimiento",
        "precio": 1299.99,
        "stock": 15,
        "id_categoria": 1,
        "categoria": {
            "id_categoria": 1,
            "nombre": "Electrónica",
            "descripcion": "Productos electrónicos varios"
        },
        "imagenes": [
            {
                "id_imagen": 1,
                "url_imagen": "https://ejemplo.com/imagen1.jpg",
                "es_principal": true,
                "orden": 1,
                "id_producto": 1
            }
        ]
    }
]
```

---

#### GET /productos/{producto_id}
**Descripción:** Obtiene un producto específico por ID

**Parámetros:**
- `producto_id` (path, requerido): ID del producto

**Respuesta exitosa (200):**
```json
{
    "id_producto": 1,
    "nombre": "Laptop Dell XPS",
    "descripcion": "Laptop de alto rendimiento",
    "precio": 1299.99,
    "stock": 15,
    "id_categoria": 1,
    "categoria": {
        "id_categoria": 1,
        "nombre": "Electrónica",
        "descripcion": "Productos electrónicos varios"
    },
    "imagenes": []
}
```

**Errores:**
- `404 Not Found`: Producto no encontrado

---

#### POST /productos
**Descripción:** Crea un nuevo producto

**Body (requerido):**
```json
{
    "nombre": "Laptop Dell XPS",
    "descripcion": "Laptop de alto rendimiento",
    "precio": 1299.99,
    "stock": 15,
    "id_categoria": 1
}
```

**Respuesta exitosa (201):**
```json
{
    "id_producto": 1,
    "nombre": "Laptop Dell XPS",
    "descripcion": "Laptop de alto rendimiento",
    "precio": 1299.99,
    "stock": 15,
    "id_categoria": 1,
    "categoria": {
        "id_categoria": 1,
        "nombre": "Electrónica",
        "descripcion": "Productos electrónicos varios"
    },
    "imagenes": []
}
```

---

#### PUT /productos/{producto_id}
**Descripción:** Actualiza un producto existente

**Parámetros:**
- `producto_id` (path, requerido): ID del producto

**Body (requerido):**
```json
{
    "nombre": "Laptop Dell XPS Actualizada",
    "descripcion": "Descripción actualizada",
    "precio": 1399.99,
    "stock": 20,
    "id_categoria": 1
}
```

**Respuesta exitosa (200):**
Retorna el objeto producto actualizado

**Errores:**
- `404 Not Found`: Producto no encontrado

---

#### DELETE /productos/{producto_id}
**Descripción:** Elimina un producto y sus imágenes asociadas

**Parámetros:**
- `producto_id` (path, requerido): ID del producto

**Respuesta exitosa (204):** Sin contenido

**Errores:**
- `404 Not Found`: Producto no encontrado

---

### Imágenes

#### GET /imagenes
**Descripción:** Obtiene la lista de todas las imágenes

**Parámetros:** Ninguno

**Respuesta exitosa (200):**
```json
[
    {
        "id_imagen": 1,
        "url_imagen": "https://ejemplo.com/imagen1.jpg",
        "es_principal": true,
        "orden": 1,
        "id_producto": 1
    }
]
```

---

#### GET /imagenes/producto/{producto_id}
**Descripción:** Obtiene todas las imágenes de un producto específico

**Parámetros:**
- `producto_id` (path, requerido): ID del producto

**Respuesta exitosa (200):**
```json
[
    {
        "id_imagen": 1,
        "url_imagen": "https://ejemplo.com/imagen1.jpg",
        "es_principal": true,
        "orden": 1,
        "id_producto": 1
    }
]
```

---

#### POST /imagenes
**Descripción:** Crea una nueva imagen para un producto

**Body (requerido):**
```json
{
    "url_imagen": "https://ejemplo.com/imagen1.jpg",
    "es_principal": true,
    "orden": 1,
    "id_producto": 1
}
```

**Respuesta exitosa (201):**
```json
{
    "id_imagen": 1,
    "url_imagen": "https://ejemplo.com/imagen1.jpg",
    "es_principal": true,
    "orden": 1,
    "id_producto": 1
}
```

---

#### PUT /imagenes/{imagen_id}
**Descripción:** Actualiza una imagen existente

**Parámetros:**
- `imagen_id` (path, requerido): ID de la imagen

**Body (requerido):**
```json
{
    "url_imagen": "https://ejemplo.com/imagen_nueva.jpg",
    "es_principal": false,
    "orden": 2,
    "id_producto": 1
}
```

**Respuesta exitosa (200):**
Retorna el objeto imagen actualizado

**Errores:**
- `404 Not Found`: Imagen no encontrada

---

#### DELETE /imagenes/{imagen_id}
**Descripción:** Elimina una imagen

**Parámetros:**
- `imagen_id` (path, requerido): ID de la imagen

**Respuesta exitosa (204):** Sin contenido

**Errores:**
- `404 Not Found`: Imagen no encontrada

---

### Health Check

#### GET /
**Descripción:** Verifica el estado de la API

**Parámetros:** Ninguno

**Respuesta exitosa (200):**
```json
{
    "status": "ok"
}
```

---

## Arquitectura de Capas

### 1. Capa de Presentación (Routers)
**Ubicación:** `app/api/v1/routers/`

Responsabilidades:
- Definir endpoints HTTP
- Validar parámetros de entrada
- Retornar respuestas formateadas
- Manejar errores HTTP (404, 400, etc.)

**Archivos:**
- `categorias.py`: Define endpoints de categorías
- `productos.py`: Define endpoints de productos
- `imagenes.py`: Define endpoints de imágenes

---

### 2. Capa de Servicios (Business Logic)
**Ubicación:** `app/services/`

Responsabilidades:
- Implementar la lógica de negocio
- Validar reglas de negocio
- Coordinar operaciones entre repositorios
- Transformar datos entre esquemas y modelos

**Archivos:**
- `categoria_service.py`: Lógica de categorías
- `producto_service.py`: Lógica de productos
- `imagen_service.py`: Lógica de imágenes

**Ejemplo:**
```python
async def crear_producto(db, data):
    producto = Producto(**data.dict())
    return await producto_repo.create(db, producto)
```

---

### 3. Capa de Acceso a Datos (Repositories)
**Ubicación:** `app/repositories/`

Responsabilidades:
- Interactuar con la base de datos
- Ejecutar consultas SQL (a través de SQLAlchemy)
- Cargar relaciones (eager loading)
- Manejar transacciones

**Archivos:**
- `categoria_repo.py`: Operaciones CRUD de categorías
- `producto_repo.py`: Operaciones CRUD de productos
- `imagen_repo.py`: Operaciones CRUD de imágenes

**Ejemplo:**
```python
async def get_by_id(db, producto_id: int):
    result = await db.execute(
        select(Producto)
        .where(Producto.id_producto == producto_id)
        .options(
            joinedload(Producto.categoria),
            joinedload(Producto.imagenes),
        )
    )
    return result.scalar_one_or_none()
```

---

### 4. Capa de Modelos (ORM)
**Ubicación:** `app/models/`

Responsabilidades:
- Definir la estructura de tablas
- Establecer relaciones entre entidades
- Aplicar restricciones a nivel de base de datos

**Archivos:**
- `base.py`: Clase base para todos los modelos
- `categoria.py`: Modelo ORM de Categoría
- `producto.py`: Modelo ORM de Producto
- `imagen.py`: Modelo ORM de Imagen

---

### 5. Capa de Validación (Schemas)
**Ubicación:** `app/schemas/`

Responsabilidades:
- Definir esquemas Pydantic para validación
- Serializar objetos ORM a JSON
- Especificar tipos de datos y validaciones
- Documentar estructura de solicitudes/respuestas

**Archivos:**
- `categoria.py`: Esquemas de categorías
- `producto.py`: Esquemas de productos
- `imagen.py`: Esquemas de imágenes

---

### 6. Capa de Configuración
**Ubicación:** `app/core/`

Responsabilidades:
- Gestionar configuración de la aplicación
- Configurar la conexión a la base de datos
- Cargar variables de entorno

**Archivos:**
- `config.py`: Configuración de la aplicación
- `database.py`: Inicialización del motor SQLAlchemy

---

### 7. Capa de Dependencias
**Ubicación:** `app/dependencies/`

Responsabilidades:
- Proporcionar sesiones de base de datos
- Inyectar dependencias en endpoints

**Archivos:**
- `db.py`: Función para obtener sesión de BD

**Ejemplo:**
```python
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
```

---

## Configuración y Conexión a Base de Datos

### Variables de Entorno

El archivo `.env` debe contener:

```env
DATABASE_URL=postgresql+asyncpg://usuario:contraseña@localhost:5432/apexstore
DB_HOST=localhost
DB_PORT=5432
DB_NAME=apexstore
DB_USER=usuario
DB_PASSWORD=contraseña
API_V1_PREFIX=/api/v1
APP_NAME=ApexStore API
ENV=development
```

### Configuración en `app/core/config.py`

```python
class Settings(BaseSettings):
    DATABASE_URL: str
    API_V1_PREFIX: str = "/api/v1"
    APP_NAME: str = "ApexStore API"
    ENV: str = "development"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
```

### Inicialización de Base de Datos en `app/core/database.py`

```python
engine = create_async_engine(
    settings.DATABASE_URL,
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True,
)

AsyncSessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False,
)
```

**Configuraciones:**
- `pool_size=10`: Número de conexiones mantenidas en el pool
- `max_overflow=20`: Conexiones adicionales permitidas más allá del pool_size
- `pool_pre_ping=True`: Verifica la validez de conexiones antes de usarlas

---

## Guía de Instalación y Ejecución

### Requisitos Previos

- Python 3.14 o superior
- PostgreSQL 12 o superior
- pip (gestor de paquetes de Python)
- Virtual environment (recomendado)

### Pasos de Instalación

#### 1. Clonar el Repositorio

```bash
git clone <url-del-repositorio>
cd apexstore-api
```

#### 2. Crear un Virtual Environment

```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

#### 3. Instalar Dependencias

```bash
pip install -e .
```

O instalar los paquetes directamente:

```bash
pip install fastapi uvicorn sqlalchemy asyncpg psycopg pydantic-settings python-dotenv
```

#### 4. Configurar Variables de Entorno

Crear un archivo `.env` en la raíz del proyecto:

```env
DATABASE_URL=postgresql+asyncpg://usuario:contraseña@localhost:5432/apexstore
DB_HOST=localhost
DB_PORT=5432
DB_NAME=apexstore
DB_USER=usuario
DB_PASSWORD=contraseña
API_V1_PREFIX=/api/v1
APP_NAME=ApexStore API
ENV=development
```

#### 5. Crear la Base de Datos

```bash
# Conectarse a PostgreSQL
psql -U postgres

# Crear la base de datos
CREATE DATABASE apexstore;

# Salir de psql
\q
```

#### 6. Ejecutar el Script de Prueba de Conexión

```bash
python main.py
```

Resultado esperado:
```
Conexión exitosa. Resultado: (1,)
```

#### 7. Iniciar el Servidor

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Opciones:**
- `--reload`: Recarga automáticamente el servidor cuando hay cambios
- `--host 0.0.0.0`: Escucha en todas las interfaces de red
- `--port 8000`: Puerto en el cual ejecutar la API

#### 8. Acceder a la API

- **API:** http://localhost:8000/api/v1
- **Documentación Swagger:** http://localhost:8000/docs
- **Documentación ReDoc:** http://localhost:8000/redoc
- **Health Check:** http://localhost:8000/

### Estructura de la Base de Datos

La API crea automáticamente las siguientes tablas en PostgreSQL:

#### Tabla: categorias

```sql
CREATE TABLE categorias (
    id_categoria SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(255)
);
```

#### Tabla: productos

```sql
CREATE TABLE productos (
    id_producto SERIAL PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    descripcion VARCHAR(255),
    precio NUMERIC(10, 2) NOT NULL,
    stock INTEGER NOT NULL CHECK (stock >= 0),
    id_categoria INTEGER NOT NULL,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
);
```

#### Tabla: imagenes_producto

```sql
CREATE TABLE imagenes_producto (
    id_imagen SERIAL PRIMARY KEY,
    url_imagen TEXT NOT NULL,
    es_principal BOOLEAN DEFAULT FALSE,
    orden INTEGER DEFAULT 1,
    id_producto INTEGER NOT NULL,
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto) ON DELETE CASCADE
);
```

### Ejemplos de Uso

#### Crear una Categoría

```bash
curl -X POST http://localhost:8000/api/v1/categorias \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Electrónica",
    "descripcion": "Productos electrónicos"
  }'
```

#### Crear un Producto

```bash
curl -X POST http://localhost:8000/api/v1/productos \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Laptop Dell XPS",
    "descripcion": "Laptop de alto rendimiento",
    "precio": 1299.99,
    "stock": 15,
    "id_categoria": 1
  }'
```

#### Obtener Todos los Productos

```bash
curl http://localhost:8000/api/v1/productos
```

#### Actualizar un Producto

```bash
curl -X PUT http://localhost:8000/api/v1/productos/1 \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Laptop Dell XPS 15",
    "descripcion": "Laptop de alto rendimiento actualizada",
    "precio": 1399.99,
    "stock": 20,
    "id_categoria": 1
  }'
```

#### Eliminar un Producto

```bash
curl -X DELETE http://localhost:8000/api/v1/productos/1
```

---

## Características Técnicas

### Características de Seguridad y Rendimiento

1. **Async/Await:** La API utiliza programación asincrónica para mejor rendimiento
2. **Connection Pooling:** Gestión automática de conexiones a la base de datos
3. **Eager Loading:** Las relaciones se cargan automáticamente para evitar N+1 queries
4. **Validación de Datos:** Pydantic valida todos los datos de entrada
5. **Error Handling:** Manejo de excepciones con códigos HTTP apropiados
6. **Documentación Automática:** OpenAPI/Swagger generada automáticamente

### Decisiones de Diseño

1. **Patrón de Capas:** Facilita mantenimiento y testing
2. **Inyección de Dependencias:** FastAPI gestiona inyección de sesiones BD
3. **Repositorio Pattern:** Abstrae la lógica de acceso a datos
4. **Schemas Pydantic:** Validación y serialización de datos
5. **ORM SQLAlchemy:** Mapeo objeto-relacional y queries type-safe

---

## Créditos

**Proyecto:** ApexStore API v1.0.0  
**Desarrollador:** José Guillermo Ortiz Quispe 
**Empresa:** ApexCorp SAC  
**Fecha de Creación:** 2026  
**Última Actualización:** 29 de enero de 2026

Este proyecto fue desarrollado con las mejores prácticas de arquitectura de software, implementando patrones de diseño reconocidos en la industria para garantizar un código mantenible, escalable y de alta calidad.

**Tecnologías Utilizadas:**
- FastAPI 0.128.0
- SQLAlchemy 2.0.46
- PostgreSQL
- AsyncPG
- Pydantic
- Python 3.14+

**Contacto:**
Para más información o consultas técnicas, contactar al equipo de desarrollo de ApexCorp SAC.

---

*Documentación generada automáticamente. Para actualizaciones, consultar el repositorio oficial.*
