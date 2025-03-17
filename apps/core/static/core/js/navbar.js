document.addEventListener('DOMContentLoaded', () => {
    try {
        const navbar = document.querySelector('.navbar');
        if (!navbar) throw new Error('Navbar element not found');

        let position = "absolute";
        let navbarTop = 0;
        let lastScrollPosition = 0;
        let touchStart = 0;
        const supportPageOffset = window.pageYOffset !== undefined;

        // Create hover detection area
        const hoverArea = document.createElement('div');
        hoverArea.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:20px;z-index:999;';
        document.body.appendChild(hoverArea);

        function onScroll() {
            const currentScrollPosition = supportPageOffset ? 
                window.pageYOffset : document.documentElement.scrollTop;

            if (currentScrollPosition <= 0) {
                position = "absolute";
                navbarTop = 0;
                lastScrollPosition = 0;
            } else {
                if (currentScrollPosition > lastScrollPosition) {
                    position = "absolute";
                    const { top, height } = navbar.getBoundingClientRect();
                    navbarTop = currentScrollPosition + Math.max(top, -height);
                } else {
                    const { top } = navbar.getBoundingClientRect();
                    if (top >= 0) {
                        navbarTop = 0;
                        position = "fixed";
                    }
                }
                lastScrollPosition = currentScrollPosition;
            }
            
            navbar.style.position = position;
            navbar.style.top = `${navbarTop}px`;
        }

        window.addEventListener("scroll", onScroll, { passive: true });

        // Hover behavior
        let hoverTimeout;
        hoverArea.addEventListener('mouseenter', () => {
            hoverTimeout = setTimeout(() => {
                if (position === "absolute") {
                    position = "fixed";
                    navbarTop = 0;
                    navbar.style.position = position;
                    navbar.style.top = `${navbarTop}px`;
                }
            }, 200);
        });

        hoverArea.addEventListener('mouseleave', () => {
            clearTimeout(hoverTimeout);
        });

        // Touch support
        document.addEventListener('touchstart', (e) => {
            touchStart = e.touches[0].clientY;
        }, { passive: true });

        document.addEventListener('touchmove', (e) => {
            const touchEnd = e.touches[0].clientY;
            if (touchEnd > touchStart && position === "absolute") {
                position = "fixed";
                navbarTop = 0;
                navbar.style.position = position;
                navbar.style.top = `${navbarTop}px`;
            }
            touchStart = touchEnd;
        }, { passive: true });

    } catch (error) {
        console.error('Navbar initialization error:', error);
    }
});