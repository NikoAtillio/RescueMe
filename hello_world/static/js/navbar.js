document.addEventListener('DOMContentLoaded', () => {
    const navbar = document.querySelector('.navbar');
    if (!navbar) {
        console.error('Navbar element not found');
        return;
    }
    let lastScroll = 0;
    let hoverTimeout;
    
    // Create hover detection area
    const hoverArea = document.createElement('div');
    hoverArea.style.position = 'fixed';
    hoverArea.style.top = '0';
    hoverArea.style.width = '100%';
    hoverArea.style.height = '20px';
    hoverArea.style.zIndex = '999';
    document.body.appendChild(hoverArea);

    // Scroll behavior
    window.addEventListener('scroll', () => {
        const currentScroll = window.scrollY;
        
        // Only hide navbar after scrolling down 100px
        if (currentScroll > lastScroll && currentScroll > 100) {
            navbar.classList.add('hidden');
        } else {
            navbar.classList.remove('hidden');
        }
        
        lastScroll = currentScroll;
    });

   // Hover behavior
   hoverArea.addEventListener('mouseenter', () => {
    console.log('Mouse entered hover area');
    hoverTimeout = setTimeout(() => {
        navbar.classList.remove('hidden');
    }, 1000);
});

hoverArea.addEventListener('mouseleave', () => {
    console.log('Mouse left hover area');
    clearTimeout(hoverTimeout);
});

// Add touch support for mobile
let touchStart = 0;
document.addEventListener('touchstart', (e) => {
    touchStart = e.touches[0].clientY;
});

document.addEventListener('touchmove', (e) => {
    const touchEnd = e.touches[0].clientY;
    if (touchEnd > touchStart) {
        navbar.classList.remove('hidden');
    }
    touchStart = touchEnd;
});
});