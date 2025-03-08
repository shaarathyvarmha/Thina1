document.getElementById('predictionForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const age = document.getElementById('age').value;
    const gender = document.getElementById('gender').value;
    const symptomsSelect = document.getElementById('symptoms');
    const symptomsArray = Array.from(symptomsSelect.selectedOptions).map(option => option.value);

    // Call the backend API for prediction
    fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ age, gender, symptoms: symptomsArray })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        document.getElementById('result').innerText = `Prediction: ${data.prediction} (Confidence: ${data.confidence}%)`;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'Error: Failed to fetch prediction. Please try again later.';
    });
});