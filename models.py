"""
Modelos de base de datos para el sistema de turismo
Define las tablas de hoteles, paquetes turísticos y sus relaciones
"""
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Instancia de SQLAlchemy para manejo de base de datos
db = SQLAlchemy()

class Hotel(db.Model):
    """
    Modelo para representar hoteles
    Almacena información básica de cada hotel
    """
    # Identificador único del hotel
    id = db.Column(db.Integer, primary_key=True)
    
    # Nombre del hotel (obligatorio)
    nombre = db.Column(db.String(100), nullable=False)
    
    # Ciudad donde se ubica (obligatorio)
    ciudad = db.Column(db.String(80), nullable=False)
    
    # País del hotel (obligatorio)
    pais = db.Column(db.String(80), nullable=False)
    
    # Dirección completa
    direccion = db.Column(db.Text)
    
    # Número de estrellas (1-5)
    estrellas = db.Column(db.Integer, default=3)
    
    # Descripción del hotel
    descripcion = db.Column(db.Text)
    
    # Precio por noche
    precio_noche = db.Column(db.Float, nullable=False)
    
    # Fecha de creación del registro
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relación con paquetes turísticos
    paquetes = db.relationship('PaqueteTuristico', backref='hotel_incluido', lazy=True)
    
    def __repr__(self):
        """Representación string del hotel"""
        return f'<Hotel {self.nombre} - {self.ciudad}>'

class PaqueteTuristico(db.Model):
    """
    Modelo para paquetes turísticos
    Combina hotel, actividades y precios
    """
    # Identificador único del paquete
    id = db.Column(db.Integer, primary_key=True)
    
    # Nombre del paquete turístico
    nombre = db.Column(db.String(100), nullable=False)
    
    # Descripción detallada del paquete
    descripcion = db.Column(db.Text, nullable=False)
    
    # Duración en días
    duracion_dias = db.Column(db.Integer, nullable=False)
    
    # Precio total del paquete
    precio_total = db.Column(db.Float, nullable=False)
    
    # Actividades incluidas
    actividades = db.Column(db.Text)
    
    # Clave foránea que conecta con el hotel
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.id'), nullable=False)
    
    # Disponibilidad del paquete
    disponible = db.Column(db.Boolean, default=True)
    
    # Fecha de creación
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        """Representación string del paquete"""
        return f'<Paquete {self.nombre} - {self.duracion_dias} días>'