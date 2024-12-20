let lastScrollY = window.scrollY;
const navbar = document.querySelector('.navbar');
let hoverTimeout;

// Scroll behavior to hide/show navbar
window.addEventListener('scroll', () => {
    const currentScrollY = window.scrollY;

    if (currentScrollY > lastScrollY) {
        // Scrolling down: hide the navbar
        navbar.classList.add('hidden');
    } else {
        // Scrolling up: show the navbar
        navbar.classList.remove('hidden');
    }

    // Update the last scroll position
    lastScrollY = currentScrollY;
});

// Hover behavior to reveal navbar
navbar.addEventListener('mouseenter', () => {
    hoverTimeout = setTimeout(() => {
        navbar.classList.remove('hidden'); // Show navbar after 1 second of hovering
    }, 1000);
});

navbar.addEventListener('mouseleave', () => {
    clearTimeout(hoverTimeout); // Cancel hover reveal if mouse leaves before 1 second
});