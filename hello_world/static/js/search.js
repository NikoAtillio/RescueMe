document.addEventListener('DOMContentLoaded', function() {
    const searchForm = document.getElementById('search-form');
    const searchInput = document.getElementById('search-input');
    const filters = document.querySelectorAll('select');

    // Function to update results
    function updateResults() {
        const formData = new FormData(searchForm);
        const queryString = new URLSearchParams(formData).toString();

        fetch(`/search-results/?${queryString}`)
            .then(response => response.json())
            .then(data => {
                const resultsDiv = document.getElementById('search-results');
                resultsDiv.innerHTML = data.html;
            });
    }

    // Update on input changes
    searchInput.addEventListener('input', updateResults);
    filters.forEach(filter => {
        filter.addEventListener('change', updateResults);
    });
});