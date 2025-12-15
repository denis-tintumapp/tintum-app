// Tintum.app - Aplicación principal

console.log('Tintum.app iniciada');

// Inicialización de la aplicación
document.addEventListener('DOMContentLoaded', () => {
  console.log('DOM cargado');
  
  // Mobile menu toggle
  initMobileMenu();
  
  // Smooth scroll para enlaces de navegación
  initSmoothScroll();
  
  // Formulario de contacto
  initContactForm();
  
  // Animaciones al hacer scroll
  initScrollAnimations();
});

/**
 * Inicializar menú móvil
 */
function initMobileMenu() {
  const menuToggle = document.getElementById('menuToggle');
  const mainNav = document.getElementById('mainNav');
  
  if (menuToggle && mainNav) {
    menuToggle.addEventListener('click', () => {
      mainNav.classList.toggle('active');
      menuToggle.classList.toggle('active');
    });
    
    // Cerrar menú al hacer clic en un enlace
    const navLinks = mainNav.querySelectorAll('a');
    navLinks.forEach(link => {
      link.addEventListener('click', () => {
        mainNav.classList.remove('active');
        menuToggle.classList.remove('active');
      });
    });
  }
}

/**
 * Inicializar smooth scroll
 */
function initSmoothScroll() {
  const links = document.querySelectorAll('a[href^="#"]');
  
  links.forEach(link => {
    link.addEventListener('click', (e) => {
      const href = link.getAttribute('href');
      
      // Ignorar enlaces vacíos
      if (href === '#') {
        e.preventDefault();
        return;
      }
      
      const target = document.querySelector(href);
      
      if (target) {
        e.preventDefault();
        const offsetTop = target.offsetTop - 80; // Ajuste para header sticky
        
        window.scrollTo({
          top: offsetTop,
          behavior: 'smooth'
        });
      }
    });
  });
}

/**
 * Inicializar formulario de contacto
 */
function initContactForm() {
  const contactForm = document.getElementById('contactForm');
  
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      
      const formData = new FormData(contactForm);
      const data = {
        name: formData.get('name'),
        email: formData.get('email'),
        message: formData.get('message')
      };
      
      // Aquí puedes agregar la lógica para enviar el formulario
      // Por ejemplo, a un endpoint de Firebase Functions o un servicio externo
      console.log('Formulario enviado:', data);
      
      // Mostrar mensaje de éxito (temporal)
      alert('¡Gracias por tu mensaje! Te contactaremos pronto.');
      contactForm.reset();
    });
  }
}

/**
 * Inicializar animaciones al hacer scroll
 */
function initScrollAnimations() {
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
      }
    });
  }, observerOptions);
  
  // Observar elementos con animación
  const animatedElements = document.querySelectorAll('.service-card, .about-text');
  animatedElements.forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(el);
  });
}

/**
 * Utilidad: Detectar si el usuario está en mobile
 */
function isMobile() {
  return window.innerWidth <= 768;
}

/**
 * Utilidad: Obtener parámetros de URL
 */
function getURLParams() {
  const params = new URLSearchParams(window.location.search);
  const result = {};
  for (const [key, value] of params) {
    result[key] = value;
  }
  return result;
}

// Exportar funciones útiles para uso futuro
window.TintumApp = {
  isMobile,
  getURLParams
};
