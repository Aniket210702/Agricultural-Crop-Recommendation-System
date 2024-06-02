document.getElementById('dataForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission
    // Get form data
    const formData = new FormData(this);
    // Convert form data to JSON
    const jsonData = {};
    for (const [key, value] of formData.entries()) {
        jsonData[key] =  parseInt(value);
    }
    // Send data to API endpoint
    fetch('http://127.0.0.1:5000', {
        method: 'POST',
        headers: {
            'Content-Type':'application/json'
        },
        body: JSON.stringify([jsonData])
    })
    .then(response => {
        if (response.ok) {
            return response.json(); // Parse response JSON
        } else {
            throw new Error('Failed to send data');
        }
    })
    .then(data => {
        console.log(data);
        if (data.predictions && data.predictions.length > 0) {
            // Display result on the webpage
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = `<p>Suitable Crop for Cultivation: ${data.predictions}</p>`;
        } 
        else {
            throw new Error('Invalid response from API');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Failed to retrieve prediction. Please try again.');
    });
});