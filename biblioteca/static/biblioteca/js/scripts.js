// ===========================
const menuToggle = document.getElementById('menuToggle');
const mobileMenu = document.getElementById('mobileMenu');

if (menuToggle) {
    menuToggle.addEventListener('click', () => {
        mobileMenu.classList.toggle('active');

        const menuIcon = menuToggle.querySelector('.menu-icon');
        menuIcon.textContent = mobileMenu.classList.contains('active') ? '✕' : '☰';
    });
}

// Smooth scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));

        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// ===========================
// jQuery dinámico (OBLIGATORIO)
// ===========================
$(document).ready(function () {

    // Datos simulados (podrías cargarlos de JSON en el futuro)
    const modelos = [
        {
            nombre: "Corazón Humano",
            img: "https://via.placeholder.com/300x200",
            nivel: "Intermedio",
            badge: "badge-intermedio"
        },
        {
            nombre: "Engranajes Mecánicos",
            img: "https://via.placeholder.com/300x200",
            nivel: "Avanzado",
            badge: "badge-avanzado"
        },
        {
            nombre: "Molécula ADN",
            img: "https://via.placeholder.com/300x200",
            nivel: "Básico",
            badge: "badge-basico"
        }
    ];

    // Insertamos dinámicamente las tarjetas en el DOM
    modelos.forEach(m => {
        $("#modelGrid").append(`
            <div class="col-md-4">
                <div class="card shadow model-card">
                    <img src="${m.img}" class="card-img-top" alt="${m.nombre}">
                    <div class="card-body">
                        <h5 class="card-title">${m.nombre}</h5>
                        <span class="badge ${m.badge}">Nivel: ${m.nivel}</span>
                    </div>
                </div>
            </div>
        `);
    });

    // Hover con jQuery
    $(".model-card").hover(
        function () { $(this).addClass("shadow-lg"); },
        function () { $(this).removeClass("shadow-lg"); }
    );

});
