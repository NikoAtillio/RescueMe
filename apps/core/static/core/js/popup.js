// static/core/js/popup.js
document.addEventListener('DOMContentLoaded', function() {
    console.log('Popup script loaded'); // Debug message
    
    // Get popup elements
    const overlay = document.getElementById('newsletterPopupOverlay');
    const closeBtn = document.getElementById('closePopupBtn');
    const form = document.getElementById('popupNewsletterForm');
    const responseDiv = document.getElementById('popup-newsletter-response');
    
    // Check if user has already seen the popup
    const hasSeenPopup = localStorage.getItem('newsletterPopupSeen');
    
    if (!hasSeenPopup && overlay) {
        console.log('Showing popup in 10 seconds'); // Debug message
        
        // Show popup after 10 seconds
        setTimeout(function() {
            console.log('Timeout triggered'); // Debug message
            overlay.classList.add('active');
        }, 10000);
    }
    
    // Close popup when close button is clicked
    if (closeBtn) {
        closeBtn.addEventListener('click', function() {
            overlay.classList.remove('active');
            // Set localStorage to remember user has seen popup
            localStorage.setItem('newsletterPopupSeen', 'true');
        });
    }
    
    // Close popup when clicking outside the popup
    if (overlay) {
        overlay.addEventListener('click', function(e) {
            if (e.target === overlay) {
                overlay.classList.remove('active');
                // Set localStorage to remember user has seen popup
                localStorage.setItem('newsletterPopupSeen', 'true');
            }
        });
    }
    
    // Handle form submission
    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            
            fetch(this.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    responseDiv.className = 'alert alert-success';
                    responseDiv.textContent = data.message;
                    responseDiv.style.display = 'block';
                    
                    // Clear form
                    form.reset();
                    
                    // Set localStorage to remember user has seen popup
                    localStorage.setItem('newsletterPopupSeen', 'true');
                    
                    // Close popup after 3 seconds
                    setTimeout(function() {
                        overlay.classList.remove('active');
                    }, 3000);
                } else {
                    responseDiv.className = 'alert alert-danger';
                    responseDiv.textContent = 'There was an error. Please try again.';
                    responseDiv.style.display = 'block';
                }
            })
            .catch(error => {
                console.error('Error:', error);
                responseDiv.className = 'alert alert-danger';
                responseDiv.textContent = 'There was an error. Please try again.';
                responseDiv.style.display = 'block';
            });
        });
    }
    
    // Add escape key handler to close popup
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && overlay.classList.contains('active')) {
            overlay.classList.remove('active');
            // Set localStorage to remember user has seen popup
            localStorage.setItem('newsletterPopupSeen', 'true');
        }
    });
});