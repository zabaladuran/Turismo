"""
Formularios para el sistema de turismo
Define los formularios web con validaciones usando Flask-WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, FloatField, SelectField, BooleanField
from wtforms.validators import DataRequired, NumberRange, Length, Optional

class HotelForm(FlaskForm):
    """
    Formulario para crear y editar hoteles
    Incluye todas las validaciones necesarias
    """
    # Campo obligatorio para el nombre del hotel
    nombre = StringField('Nombre del Hotel', 
                        validators=[DataRequired(message='El nombre es obligatorio'),
                                  Length(min=2, max=100, message='El nombre debe tener entre 2 y 100 caracteres')])
    
    # Ciudad donde se ubica el hotel
    ciudad = StringField('Ciudad', 
                        validators=[DataRequired(message='La ciudad es obligatoria'),
                                  Length(min=2, max=80)])
    
    # País del hotel
    pais = StringField('País', 
                      validators=[DataRequired(message='El país es obligatorio'),
                                Length(min=2, max=80)])
    
    # Dirección (opcional)
    direccion = TextAreaField('Dirección', 
                             validators=[Optional(), Length(max=500)])
    
    # Número de estrellas del hotel
    estrellas = SelectField('Estrellas', 
                           choices=[(1, '1 Estrella'), (2, '2 Estrellas'), 
                                   (3, '3 Estrellas'), (4, '4 Estrellas'), 
                                   (5, '5 Estrellas')],
                           coerce=int,
                           validators=[DataRequired()])
    
    # Descripción del hotel
    descripcion = TextAreaField('Descripción', 
                               validators=[Length(max=1000, message='Máximo 1000 caracteres')])
    
    # Precio por noche
    precio_noche = FloatField('Precio por Noche (USD)', 
                             validators=[DataRequired(message='El precio es obligatorio'),
                                       NumberRange(min=1, message='El precio debe ser mayor a 0')])

class PaqueteForm(FlaskForm):
    """
    Formulario para crear y editar paquetes turísticos
    Incluye selección de hotel y validaciones
    """
    # Nombre del paquete
    nombre = StringField('Nombre del Paquete', 
                        validators=[DataRequired(message='El nombre es obligatorio'),
                                  Length(min=2, max=100)])
    
    # Descripción detallada
    descripcion = TextAreaField('Descripción', 
                               validators=[DataRequired(message='La descripción es obligatoria'),
                                         Length(min=10, max=1000)])
    
    # Duración en días
    duracion_dias = IntegerField('Duración (días)', 
                                validators=[DataRequired(message='La duración es obligatoria'),
                                          NumberRange(min=1, max=365, message='Entre 1 y 365 días')])
    
    # Precio total
    precio_total = FloatField('Precio Total (USD)', 
                             validators=[DataRequired(message='El precio es obligatorio'),
                                       NumberRange(min=1, message='El precio debe ser mayor a 0')])
    
    # Actividades incluidas
    actividades = TextAreaField('Actividades Incluidas', 
                               validators=[Length(max=1000, message='Máximo 1000 caracteres')])
    
    # Selección de hotel (se poblará dinámicamente)
    hotel_id = SelectField('Hotel Incluido', 
                          coerce=int,
                          validators=[DataRequired(message='Debe seleccionar un hotel')])
    
    # Disponibilidad
    disponible = BooleanField('Disponible para reserva', default=True)