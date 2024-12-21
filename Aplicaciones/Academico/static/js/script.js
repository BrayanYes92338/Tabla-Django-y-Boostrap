window.addEventListener('load', () => {
    const btnEliminacion = document.querySelectorAll('.btn-borrar');

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) => {
            if (!confirm('¿Está seguro de eliminar el registro?')) {
                e.preventDefault();
            }
        });
    });

});

setTimeout(() => {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        alert.classList.remove('show'); // Ocultar gradualmente (si Bootstrap está configurado)
        alert.classList.add('fade'); // Asegurar el efecto de desvanecimiento
    });
}, 5000);