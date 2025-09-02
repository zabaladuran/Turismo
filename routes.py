"""
Rutas y controladores del sistema de turismo
Define todas las URLs y la lógica de cada página
"""
from flask import render_template, request, redirect, url_for, flash
from models import db, Hotel, PaqueteTuristico
from forms import HotelForm, PaqueteForm

def init_routes(app):
    """
    Inicializa todas las rutas de la aplicación
    Se llama desde app.py para organizar el código
    """
    
    @app.route('/')
    def index():
        """
        Página principal del sistema
        Muestra estadísticas básicas y enlaces de navegación
        """
        # Obtener estadísticas para mostrar en el dashboard
        total_hoteles = Hotel.query.count()
        total_paquetes = PaqueteTuristico.query.count()
        paquetes_disponibles = PaqueteTuristico.query.filter_by(disponible=True).count()
        
        return render_template('index.html', 
                             total_hoteles=total_hoteles,
                             total_paquetes=total_paquetes,
                             paquetes_disponibles=paquetes_disponibles)
    
    # === RUTAS PARA HOTELES ===
    
    @app.route('/hoteles')
    def listar_hoteles():
        """
        Lista todos los hoteles registrados
        Permite búsqueda por ciudad
        """
        # Obtener parámetro de búsqueda
        busqueda = request.args.get('busqueda', '')
        
        if busqueda:
            # Buscar hoteles por nombre o ciudad
            hoteles = Hotel.query.filter(
                (Hotel.nombre.contains(busqueda)) | 
                (Hotel.ciudad.contains(busqueda))
            ).all()
        else:
            # Mostrar todos los hoteles
            hoteles = Hotel.query.all()
        
        return render_template('hoteles/lista.html', hoteles=hoteles, busqueda=busqueda)
    
    @app.route('/hoteles/crear', methods=['GET', 'POST'])
    def crear_hotel():
        """
        Formulario para crear un nuevo hotel
        Maneja tanto GET (mostrar formulario) como POST (procesar datos)
        """
        form = HotelForm()
        
        if form.validate_on_submit():
            # Crear nuevo hotel con los datos del formulario
            hotel = Hotel(
                nombre=form.nombre.data,
                ciudad=form.ciudad.data,
                pais=form.pais.data,
                direccion=form.direccion.data,
                estrellas=form.estrellas.data,
                descripcion=form.descripcion.data,
                precio_noche=form.precio_noche.data
            )
            
            try:
                # Guardar en la base de datos
                db.session.add(hotel)
                db.session.commit()
                flash('Hotel creado exitosamente!', 'success')
                return redirect(url_for('listar_hoteles'))
            except Exception as e:
                # Manejar errores de base de datos
                db.session.rollback()
                flash(f'Error al crear hotel: {str(e)}', 'error')
        
        return render_template('hoteles/crear.html', form=form)
    
    @app.route('/hoteles/<int:hotel_id>')
    def ver_hotel(hotel_id):
        """
        Muestra detalles de un hotel específico
        Incluye paquetes turísticos asociados
        """
        # Buscar hotel o mostrar error 404
        hotel = Hotel.query.get_or_404(hotel_id)
        
        # Obtener paquetes asociados a este hotel
        paquetes = PaqueteTuristico.query.filter_by(hotel_id=hotel_id).all()
        
        return render_template('hoteles/ver.html', hotel=hotel, paquetes=paquetes)
    
    @app.route('/hoteles/<int:hotel_id>/editar', methods=['GET', 'POST'])
    def editar_hotel(hotel_id):
        """
        Formulario para editar hotel existente
        Pre-llena el formulario con datos actuales
        """
        hotel = Hotel.query.get_or_404(hotel_id)
        form = HotelForm(obj=hotel)  # Pre-llenar formulario
        
        if form.validate_on_submit():
            # Actualizar datos del hotel
            form.populate_obj(hotel)
            
            try:
                db.session.commit()
                flash('Hotel actualizado exitosamente!', 'success')
                return redirect(url_for('ver_hotel', hotel_id=hotel.id))
            except Exception as e:
                db.session.rollback()
                flash(f'Error al actualizar hotel: {str(e)}', 'error')
        
        return render_template('hoteles/crear.html', form=form, hotel=hotel)
    
    # === RUTAS PARA PAQUETES TURÍSTICOS ===
    
    @app.route('/paquetes')
    def listar_paquetes():
        """
        Lista todos los paquetes turísticos
        Permite filtrar por disponibilidad
        """
        # Obtener filtros
        solo_disponibles = request.args.get('disponibles')
        
        if solo_disponibles:
            paquetes = PaqueteTuristico.query.filter_by(disponible=True).all()
        else:
            paquetes = PaqueteTuristico.query.all()
        
        return render_template('paquetes/lista.html', paquetes=paquetes)
    
    @app.route('/paquetes/crear', methods=['GET', 'POST'])
    def crear_paquete():
        """
        Formulario para crear nuevo paquete turístico
        Requiere que exista al menos un hotel
        """
        form = PaqueteForm()
        
        # Poblar lista de hoteles disponibles
        hoteles = Hotel.query.all()
        if not hoteles:
            flash('Debe crear al menos un hotel antes de crear paquetes', 'warning')
            return redirect(url_for('crear_hotel'))
        
        # Llenar opciones del select de hoteles
        form.hotel_id.choices = [(h.id, f'{h.nombre} - {h.ciudad}') for h in hoteles]
        
        if form.validate_on_submit():
            # Crear nuevo paquete
            paquete = PaqueteTuristico(
                nombre=form.nombre.data,
                descripcion=form.descripcion.data,
                duracion_dias=form.duracion_dias.data,
                precio_total=form.precio_total.data,
                actividades=form.actividades.data,
                hotel_id=form.hotel_id.data,
                disponible=form.disponible.data
            )
            
            try:
                db.session.add(paquete)
                db.session.commit()
                flash('Paquete turístico creado exitosamente!', 'success')
                return redirect(url_for('listar_paquetes'))
            except Exception as e:
                db.session.rollback()
                flash(f'Error al crear paquete: {str(e)}', 'error')
        
        return render_template('paquetes/crear.html', form=form)
    
    @app.route('/paquetes/<int:paquete_id>')
    def ver_paquete(paquete_id):
        """
        Muestra detalles completos de un paquete turístico
        Incluye información del hotel asociado
        """
        paquete = PaqueteTuristico.query.get_or_404(paquete_id)
        return render_template('paquetes/ver.html', paquete=paquete)
    
    @app.route('/paquetes/<int:paquete_id>/toggle')
    def toggle_disponibilidad(paquete_id):
        """
        Cambia la disponibilidad de un paquete
        Permite activar/desactivar paquetes rápidamente
        """
        paquete = PaqueteTuristico.query.get_or_404(paquete_id)
        paquete.disponible = not paquete.disponible
        
        try:
            db.session.commit()
            estado = 'disponible' if paquete.disponible else 'no disponible'
            flash(f'Paquete marcado como {estado}', 'info')
        except Exception as e:
            db.session.rollback()
            flash(f'Error al cambiar disponibilidad: {str(e)}', 'error')
        
        return redirect(url_for('listar_paquetes'))