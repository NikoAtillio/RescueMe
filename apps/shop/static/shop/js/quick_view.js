document.addEventListener('DOMContentLoaded', function() {
    const quickViewButtons = document.querySelectorAll('.quick-view');
    const quickViewModal = new bootstrap.Modal(document.getElementById('quickViewModal'));
    const quickViewContent = document.getElementById('quickViewContent');
    
    quickViewButtons.forEach(button => {
        button.addEventListener('click', function() {
            const productId = this.dataset.productId;
            
            // Show loading indicator
            quickViewContent.innerHTML = '<div class="text-center"><div class="spinner-border" role="status"><span class="visually-hidden">Loading...</span></div></div>';
            quickViewModal.show();
            
            // Fetch product details
            fetch(`/shop/product/${productId}/quick-view/`)
                .then(response => response.text())
                .then(html => {
                    quickViewContent.innerHTML = html;
                })
                .catch(error => {
                    quickViewContent.innerHTML = '<div class="alert alert-danger">Error loading product details</div>';
                });
        });
    });
});