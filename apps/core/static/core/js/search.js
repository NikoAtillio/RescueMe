document.addEventListener('DOMContentLoaded', function() {
    const searchForm = document.getElementById('search-form');
    const searchInput = document.getElementById('search-input');
    const filters = document.querySelectorAll('.search-filter');
    const suggestionsContainer = document.getElementById('autocomplete-suggestions');
    let currentFocus = -1;

    if (!searchForm || !searchInput) {
        console.error('Search form elements not found');
        return;
    }

    // Function to update results
    function updateResults() {
        const formData = new FormData(searchForm);
        const queryString = new URLSearchParams(formData).toString();

        fetch(`/marketplace/search_results/?${queryString}`)
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
    searchInput.addEventListener('input', debounce(function() {
        updateResults();
        handleAutocomplete();
    }, 300));
    
    filters.forEach(filter => {
        filter.addEventListener('change', updateResults);
    });

    // Prevent form submission (we're handling it via AJAX)
    searchForm.addEventListener('submit', function(e) {
        e.preventDefault();
        updateResults();
    });

    // Autocomplete functionality
    function handleAutocomplete() {
        const query = searchInput.value.trim();
        
        if (query.length < 2) {
            suggestionsContainer.style.display = 'none';
            return;
        }
        
        fetch(`/marketplace/search/autocomplete/?q=${encodeURIComponent(query)}`)
            .then(response => response.json())
            .then(data => {
                suggestionsContainer.innerHTML = '';
                
                if (data.suggestions && data.suggestions.length > 0) {
                    data.suggestions.forEach(suggestion => {
                        const item = document.createElement('div');
                        item.className = 'autocomplete-suggestion';
                        item.textContent = suggestion;
                        
                        item.addEventListener('click', function() {
                            searchInput.value = suggestion;
                            suggestionsContainer.style.display = 'none';
                            searchInput.focus();
                            updateResults();
                        });
                        
                        suggestionsContainer.appendChild(item);
                    });
                    
                    suggestionsContainer.style.display = 'block';
                } else {
                    suggestionsContainer.style.display = 'none';
                }
            })
            .catch(error => {
                console.error('Error fetching suggestions:', error);
            });
    }

    // Keyboard navigation for autocomplete
    if (searchInput && suggestionsContainer) {
        searchInput.addEventListener('keydown', function(e) {
            const suggestions = suggestionsContainer.getElementsByClassName('autocomplete-suggestion');
            
            if (suggestions.length === 0) return;
            
            // Down arrow
            if (e.keyCode === 40) {
                currentFocus++;
                addActive(suggestions);
                e.preventDefault();
            } 
            // Up arrow
            else if (e.keyCode === 38) {
                currentFocus--;
                addActive(suggestions);
                e.preventDefault();
            } 
            // Enter
            else if (e.keyCode === 13 && currentFocus > -1) {
                if (suggestions[currentFocus]) {
                    suggestions[currentFocus].click();
                    e.preventDefault();
                }
            }
        });

        // Add active class to suggestion
        function addActive(suggestions) {
            if (!suggestions) return false;
            
            removeActive(suggestions);
            
            if (currentFocus >= suggestions.length) currentFocus = 0;
            if (currentFocus < 0) currentFocus = (suggestions.length - 1);
            
            suggestions[currentFocus].classList.add('active');
        }

        // Remove active class from suggestions
        function removeActive(suggestions) {
            for (let i = 0; i < suggestions.length; i++) {
                suggestions[i].classList.remove('active');
            }
        }

        // Hide suggestions when clicking outside
        document.addEventListener('click', function(e) {
            if (!searchInput.contains(e.target) && !suggestionsContainer.contains(e.target)) {
                suggestionsContainer.style.display = 'none';
            }
        });

        // Show suggestions when input is focused if there's content
        searchInput.addEventListener('focus', function() {
            if (this.value.trim().length >= 2) {
                handleAutocomplete();
            }
        });
    }
});