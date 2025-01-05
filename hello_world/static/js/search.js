document.addEventListener('DOMContentLoaded', function() {
    const searchForm = document.getElementById('search-form');
    const searchInput = document.getElementById('search-input');
    const filters = document.querySelectorAll('.search-filter');

    if (!searchForm || !searchInput) {
        console.error('Search form elements not found');
        return;
    }

    // Function to update results
    function updateResults() {
        const formData = new FormData(searchForm);
        const queryString = new URLSearchParams(formData).toString();

        fetch(`/rescue/search_results/?${queryString}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                const resultsDiv = document.getElementById('search-results');
                if (resultsDiv) {
                    resultsDiv.innerHTML = data.html;
                }
            })
            .catch(error => {
                console.error('Search error:', error);
            });
    }

    // Debounce function to prevent too many requests
    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

    // Update on input changes
    searchInput.addEventListener('input', debounce(updateResults, 300));
    filters.forEach(filter => {
        filter.addEventListener('change', updateResults);
    });

    // Prevent form submission (we're handling it via AJAX)
    searchForm.addEventListener('submit', function(e) {
        e.preventDefault();
        updateResults();
    });
});