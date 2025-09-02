"""
Configuración de la aplicación Flask
Este archivo contiene todas las configuraciones necesarias para el proyecto
"""
import os

class Config:
    """Configuración principal de la aplicación"""
    
    # Clave secreta para formularios y sesiones (cambiar en producción)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave-super-secreta-turismo-2025'
    
    # Configuración de la base de datos SQLite
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///turismo.db'
    
    # Desactiva el tracking de modificaciones para mejorar rendimiento
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Configuración para desarrollo
    DEBUG = True