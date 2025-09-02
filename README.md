# 🌍 Sistema de Gestión Turística

Un sistema completo desarrollado en Flask para la gestión de hoteles y paquetes turísticos, con una interfaz moderna y amigable.

## 📋 Características

### 🏨 Gestión de Hoteles
- **CRUD completo**: Crear, leer, actualizar y eliminar hoteles
- **Búsqueda avanzada**: Buscar por nombre o ciudad
- **Información detallada**: Ubicación, estrellas, precios, descripción
- **Validaciones**: Formularios con validación en tiempo real

### 🎒 Gestión de Paquetes Turísticos
- **Paquetes personalizados**: Combinar hoteles con actividades
- **Control de disponibilidad**: Activar/desactivar paquetes
- **Precios dinámicos**: Cálculo de precio total y por día
- **Relaciones**: Asociar paquetes con hoteles específicos

### 🎨 Diseño y UX
- **Bootstrap 5**: Framework CSS moderno y responsive
- **Tema turístico**: Colores océano y natura
- **Animaciones suaves**: Transiciones y micro-interacciones
- **Responsive**: Optimizado para móviles, tablets y desktop
- **Iconos FontAwesome**: Interfaz visual rica

## 🚀 Instalación y Configuración

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de instalación

1. **Instalar dependencias**:
```bash
pip install -r requirements.txt
```

2. **Ejecutar la aplicación**:
```bash
python app.py
```

3. **Acceder al sistema**:
   - Abrir navegador en `http://localhost:5000`
   - El sistema incluye datos de ejemplo para testing

## 📁 Estructura del Proyecto

```
/
├── app.py              # Aplicación principal Flask
├── config.py           # Configuraciones del sistema
├── models.py           # Modelos de base de datos (SQLAlchemy)
├── routes.py           # Rutas y controladores
├── forms.py            # Formularios con validaciones (WTF)
├── requirements.txt    # Dependencias Python
├── templates/          # Plantillas HTML (Jinja2)
│   ├── base.html      # Plantilla base con navegación
│   ├── index.html     # Dashboard principal
│   ├── hoteles/       # Templates de hoteles
│   │   ├── lista.html    # Lista de hoteles
│   │   ├── crear.html    # Formulario crear/editar
│   │   └── ver.html      # Detalles de hotel
│   └── paquetes/      # Templates de paquetes
│       ├── lista.html    # Lista de paquetes
│       ├── crear.html    # Formulario crear paquete
│       └── ver.html      # Detalles de paquete
└── static/            # Archivos estáticos
    ├── css/
    │   └── custom.css    # Estilos personalizados
    └── js/
        └── custom.js     # JavaScript personalizado
```

## 🗄️ Modelo de Base de Datos

### Tabla `Hotel`
- `id`: Identificador único
- `nombre`: Nombre del hotel
- `ciudad`: Ciudad de ubicación
- `pais`: País de ubicación
- `direccion`: Dirección completa (opcional)
- `estrellas`: Calificación 1-5 estrellas
- `descripcion`: Descripción del hotel
- `precio_noche`: Precio por noche en USD
- `fecha_creacion`: Timestamp de registro

### Tabla `PaqueteTuristico`
- `id`: Identificador único
- `nombre`: Nombre del paquete
- `descripcion`: Descripción detallada
- `duracion_dias`: Duración en días
- `precio_total`: Precio total en USD
- `actividades`: Lista de actividades incluidas
- `hotel_id`: Referencia al hotel (clave foránea)
- `disponible`: Estado de disponibilidad
- `fecha_creacion`: Timestamp de registro

## 🔧 Funcionalidades Técnicas

### Backend (Flask)
- **SQLAlchemy**: ORM para manejo de base de datos
- **Flask-WTF**: Formularios seguros con validación
- **SQLite**: Base de datos ligera (fácil para desarrollo)
- **Blueprints**: Organización modular de rutas
- **Error Handling**: Manejo de errores y rollback

### Frontend
- **Bootstrap 5**: Framework CSS responsive
- **FontAwesome**: Librería de iconos
- **JavaScript ES6**: Funciones modernas del navegador
- **CSS3**: Animaciones y transiciones suaves
- **Mobile-First**: Diseño adaptativo

## 📝 Uso del Sistema

### Dashboard Principal
- **Estadísticas**: Resumen de hoteles y paquetes
- **Acciones rápidas**: Enlaces directos a funciones principales
- **Navegación intuitiva**: Menús organizados por categorías

### Gestión de Hoteles
1. **Crear hotel**: Formulario con validaciones
2. **Ver lista**: Grid de hoteles con búsqueda
3. **Ver detalles**: Información completa + paquetes asociados
4. **Editar**: Modificar información existente

### Gestión de Paquetes
1. **Crear paquete**: Seleccionar hotel y definir actividades
2. **Ver lista**: Filtrar por disponibilidad
3. **Ver detalles**: Información completa del paquete
4. **Control disponibilidad**: Activar/desactivar rápidamente

## 🔒 Características de Seguridad

- **CSRF Protection**: Flask-WTF protege contra ataques CSRF
- **Validación server-side**: Todas las entradas son validadas
- **SQL Injection**: SQLAlchemy previene inyecciones SQL
- **Error Handling**: Manejo seguro de errores de BD

## 🚀 Datos de Ejemplo

El sistema incluye datos de ejemplo que se crean automáticamente:

### Hoteles de Ejemplo:
- **Hotel Vista del Mar** (Cartagena, Colombia) - 4 estrellas
- **Posada Los Andes** (Cusco, Perú) - 3 estrellas  
- **Resort Tropical Paradise** (Cancún, México) - 5 estrellas

### Paquetes de Ejemplo:
- **Escapada Romántica Caribeña** - 3 días
- **Aventura Machu Picchu** - 4 días
- **Vacaciones Familiares Todo Incluido** - 7 días

## 🔧 Personalización

### Cambiar Colores del Tema
Editar variables CSS en `static/css/custom.css`:
```css
:root {
    --primary-blue: #0066cc;    /* Color principal */
    --nature-green: #198754;    /* Color secundario */
    --accent-orange: #fd7e14;   /* Color de acento */
}
```

### Agregar Nuevos Campos
1. Modificar modelo en `models.py`
2. Actualizar formulario en `forms.py`
3. Editar templates correspondientes
4. Ejecutar migración de BD (recrear BD para desarrollo)

## 📞 Soporte

Para dudas técnicas sobre el código:
- Revisar comentarios en cada archivo
- Consultar documentación de Flask: https://flask.palletsprojects.com/
- Documentación de Bootstrap: https://getbootstrap.com/

---

**Desarrollado con ❤️ usando Flask + Bootstrap + Python**