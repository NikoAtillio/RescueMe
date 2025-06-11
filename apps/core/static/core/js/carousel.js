// Simple carousel initialization
document.addEventListener('DOMContentLoaded', function() {
    const carousel = document.getElementById('wagCarousel');
    if (carousel) {
        // Let Bootstrap handle everything - just initialize
        new bootstrap.Carousel(carousel, {
            interval: 5000,
            wrap: true,
            touch: true,
            pause: 'hover'
        });
    }
});