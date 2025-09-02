"""
Aplicación principal Flask para gestión turística
Punto de entrada del sistema - configura y ejecuta la aplicación
"""
from flask import Flask
from config import Config
from models import db, Hotel, PaqueteTuristico
from routes import init_routes

def create_app():
    """
    Factory function para crear la aplicación Flask
    Configura base de datos, rutas y extensiones
    """
    # Crear instancia de Flask
    app = Flask(__name__)
    
    # Cargar configuración
    app.config.from_object(Config)
    
    # Inicializar extensiones
    db.init_app(app)
    
    # Registrar rutas
    init_routes(app)
    
    # Crear tablas de base de datos
    with app.app_context():
        db.create_all()
        
        # Crear datos de ejemplo si la base está vacía
        if Hotel.query.count() == 0:
            crear_datos_ejemplo()
    
    return app

def crear_datos_ejemplo():
    """
    Crea datos de ejemplo para demostrar el sistema
    Se ejecuta solo si la base de datos está vacía
    """
    # Hoteles de ejemplo
    hoteles_ejemplo = [
        Hotel(
            nombre='Hotel Vista del Mar',
            ciudad='Cartagena',
            pais='Colombia',
            direccion='Avenida San Martín 123',
            estrellas=4,
            descripcion='Hermoso hotel frente al mar con vistas espectaculares',
            precio_noche=150.00
        ),
        Hotel(
            nombre='Posada Los Andes',
            ciudad='Cusco',
            pais='Perú',
            direccion='Plaza de Armas 456',
            estrellas=3,
            descripcion='Hotel tradicional en el corazón de la ciudad imperial',
            precio_noche=85.00
        ),
        Hotel(
            nombre='Resort Tropical Paradise',
            ciudad='Cancún',
            pais='México',
            direccion='Zona Hotelera Km 12',
            estrellas=5,
            descripcion='Resort todo incluido con playa privada y spa',
            precio_noche=300.00
        )
    ]
    
    # Guardar hoteles
    for hotel in hoteles_ejemplo:
        db.session.add(hotel)
    
    # Confirmar cambios antes de crear paquetes
    db.session.commit()
    
    # Paquetes de ejemplo
    paquetes_ejemplo = [
        PaqueteTuristico(
            nombre='Escapada Romántica Caribeña',
            descripcion='Perfecto para parejas que buscan romance y relajación',
            duracion_dias=3,
            precio_total=500.00,
            actividades='Cena romántica, masajes en pareja, tour en catamarán',
            hotel_id=1,
            disponible=True
        ),
        PaqueteTuristico(
            nombre='Aventura Machu Picchu',
            descripcion='Descubre la maravilla del mundo con guía experto',
            duracion_dias=4,
            precio_total=420.00,
            actividades='Tour Machu Picchu, Valle Sagrado, degustación de comida local',
            hotel_id=2,
            disponible=True
        ),
        PaqueteTuristico(
            nombre='Vacaciones Familiares Todo Incluido',
            descripcion='Diversión garantizada para toda la familia',
            duracion_dias=7,
            precio_total=2100.00,
            actividades='Parque acuático, actividades para niños, espectáculos nocturnos',
            hotel_id=3,
            disponible=True
        )
    ]
    
    # Guardar paquetes
    for paquete in paquetes_ejemplo:
        db.session.add(paquete)
    
    # Confirmar todos los cambios
    db.session.commit()
    print("✅ Datos de ejemplo creados exitosamente")

if __name__ == '__main__':
    """
    Punto de entrada cuando se ejecuta directamente
    Crear y ejecutar la aplicación en modo desarrollo
    """
    app = create_app()
    print("🚀 Iniciando servidor Flask...")
    print("📊 Sistema de Gestión Turística")
    print("🌐 Acceder en: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)