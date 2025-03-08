def predict_health_condition(data):
    # Simulate prediction logic
    age = data.get('age')
    gender = data.get('gender')
    symptoms = data.get('symptoms')

    # Dummy prediction logic
    prediction = "Healthy" if age < 50 and len(symptoms) < 3 else "Unhealthy"
    confidence = 90 if prediction == "Healthy" else 70

    return prediction, confidence