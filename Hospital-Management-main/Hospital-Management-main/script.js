function searchMedicine() {
    const searchInput = document.getElementById('searchInput').value.trim();
    
    if (searchInput === '') {
        alert('Please enter a search query.');
        return;
    }
    
    // Construct the URL to query the OpenFDA API for drug details
    const apiUrl = `https://api.fda.gov/drug/label.json?search=${encodeURIComponent(searchInput)}&limit=10`;

    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data.results && data.results.length > 0) {
                displayMedicine(data.results);
            } else {
                displayNoResults();
            }
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
            displayError();
        });
}

function displayMedicine(drugs) {
    const medicineList = document.getElementById('medicineList');
    medicineList.innerHTML = '';

    const ul = document.createElement('ul');
    drugs.forEach(drug => {
        const li = document.createElement('li');
        li.textContent = drug.openfda.generic_name || 'Unknown';
        ul.appendChild(li);
    });

    medicineList.appendChild(ul);
}

function displayNoResults() {
    const medicineList = document.getElementById('medicineList');
    medicineList.innerHTML = 'No medicine found.';
}

function displayError() {
    const medicineList = document.getElementById('medicineList');
    medicineList.innerHTML = 'An error occurred while fetching data. Please try again later.';
}
