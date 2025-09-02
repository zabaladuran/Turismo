/**
 * JavaScript personalizado para el Sistema de Gestión Turística
 * Mejora la experiencia del usuario con interacciones dinámicas
 */

// Ejecutar cuando el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', function() {
    console.log('🚀 Sistema de Gestión Turística cargado');
    
    // Inicializar funcionalidades
    initAutoHideAlerts();
    initFormValidation();
    initCardAnimations();
    initTooltips();
});

/**
 * Auto-oculta las alertas después de 5 segundos
 * Mejora UX evitando que las notificaciones persistan demasiado tiempo
 */
function initAutoHideAlerts() {
    const alerts = document.querySelectorAll('.alert:not(.alert-danger)');
    
    alerts.forEach(alert => {
        // Solo auto-ocultar alertas de éxito e info
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000); // 5 segundos
    });
}

/**
 * Validación de formularios en tiempo real
 * Proporciona feedback inmediato al usuario
 */
function initFormValidation() {
    const forms = document.querySelectorAll('form[novalidate]');
    
    forms.forEach(form => {
        const inputs = form.querySelectorAll('input, select, textarea');
        
        inputs.forEach(input => {
            // Validar al perder el foco
            input.addEventListener('blur', function() {
                validateField(this);
            });
            
            // Limpiar errores al escribir
            input.addEventListener('input', function() {
                if (this.classList.contains('is-invalid')) {
                    this.classList.remove('is-invalid');
                    const feedback = this.parentNode.querySelector('.invalid-feedback');
                    if (feedback) {
                        feedback.style.display = 'none';
                    }
                }
            });
        });
    });
}

/**
 * Valida un campo individual del formulario
 * @param {HTMLElement} field - Campo a validar
 */
function validateField(field) {
    const isRequired = field.hasAttribute('required');
    const isEmpty = !field.value.trim();
    
    if (isRequired && isEmpty) {
        field.classList.add('is-invalid');
        showFieldError(field, 'Este campo es obligatorio');
        return false;
    }
    
    // Validaciones específicas por tipo
    if (field.type === 'number' && field.value) {
        const min = field.getAttribute('min');
        const max = field.getAttribute('max');
        const value = parseFloat(field.value);
        
        if (min && value < parseFloat(min)) {
            field.classList.add('is-invalid');
            showFieldError(field, `El valor mínimo es ${min}`);
            return false;
        }
        
        if (max && value > parseFloat(max)) {
            field.classList.add('is-invalid');
            showFieldError(field, `El valor máximo es ${max}`);
            return false;
        }
    }
    
    // Si llegamos aquí, el campo es válido
    field.classList.remove('is-invalid');
    field.classList.add('is-valid');
    return true;
}

/**
 * Muestra mensaje de error para un campo específico
 * @param {HTMLElement} field - Campo con error
 * @param {string} message - Mensaje de error a mostrar
 */
function showFieldError(field, message) {
    let feedback = field.parentNode.querySelector('.invalid-feedback');
    if (!feedback) {
        feedback = document.createElement('div');
        feedback.className = 'invalid-feedback';
        field.parentNode.appendChild(feedback);
    }
    feedback.textContent = message;
    feedback.style.display = 'block';
}

/**
 * Inicializa animaciones suaves para las cards
 * Añade efectos visuales atractivos
 */
function initCardAnimations() {
    const cards = document.querySelectorAll('.card');
    
    // Observador para animar cards cuando entran en viewport
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.animationDelay = Math.random() * 0.3 + 's';
                entry.target.classList.add('fade-in-up');
            }
        });
    });
    
    cards.forEach(card => {
        observer.observe(card);
    });
}

/**
 * Inicializa tooltips de Bootstrap
 * Mejora la accesibilidad y proporciona información adicional
 */
function initTooltips() {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
}

/**
 * Confirma acciones destructivas
 * Previene eliminaciones accidentales
 * @param {string} message - Mensaje de confirmación
 * @returns {boolean} - true si el usuario confirma
 */
function confirmAction(message) {
    return confirm(message || '¿Estás seguro de realizar esta acción?');
}

/**
 * Muestra notificación temporal
 * @param {string} message - Mensaje a mostrar
 * @param {string} type - Tipo de notificación (success, error, info, warning)
 */
function showNotification(message, type = 'info') {
    const alertContainer = document.createElement('div');
    alertContainer.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    alertContainer.style.cssText = 'top: 100px; right: 20px; z-index: 1050; min-width: 300px;';
    
    alertContainer.innerHTML = `
        <i class="fas fa-${getIconForType(type)} me-2"></i>
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    document.body.appendChild(alertContainer);
    
    // Auto-remover después de 4 segundos
    setTimeout(() => {
        if (alertContainer.parentNode) {
            const bsAlert = new bootstrap.Alert(alertContainer);
            bsAlert.close();
        }
    }, 4000);
}

/**
 * Obtiene el icono apropiado para cada tipo de notificación
 * @param {string} type - Tipo de notificación
 * @returns {string} - Nombre del icono de FontAwesome
 */
function getIconForType(type) {
    const icons = {
        'success': 'check-circle',
        'error': 'exclamation-triangle',
        'warning': 'exclamation-triangle',
        'info': 'info-circle',
        'danger': 'exclamation-triangle'
    };
    return icons[type] || 'info-circle';
}

/**
 * Formatea números como moneda
 * @param {number} amount - Cantidad a formatear
 * @returns {string} - Cantidad formateada como USD
 */
function formatCurrency(amount) {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD'
    }).format(amount);
}

/**
 * Anima el scroll suave a un elemento
 * @param {string} elementId - ID del elemento destino
 */
function scrollToElement(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
        element.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
}

/* Clase CSS para animación fade-in-up */
.fade-in-up {
    animation: fadeInUp 0.6s ease forwards;
}

console.log('✅ Funciones JavaScript cargadas correctamente');