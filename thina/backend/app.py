import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
import joblib
import numpy as np

# ==========================
# Load & Train the Model
# ==========================

# Load dataset
data = pd.read_csv(r"D:\Desktop\health.csv")

# One-Hot Encoding for categorical symptoms
encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')  # ✅ FIXED

X = encoder.fit_transform(data[['symptom1', 'symptom2']])

# Target variable
y = data['condition']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model and encoder
joblib.dump(model, 'model.pkl')
joblib.dump(encoder, 'encoder.pkl')

# ==========================
# Prediction Function
# ==========================

def predict_health_condition(symptoms):
    try:
        if not symptoms or len(symptoms) != 2:  # Ensure two symptoms are provided
            return "Error: Please provide exactly two symptoms.", 0

        # Load model and encoder
        model = joblib.load('model.pkl')
        encoder = joblib.load('encoder.pkl')

        # Convert symptoms to DataFrame with correct column names
        symptoms_df = pd.DataFrame([symptoms], columns=['symptom1', 'symptom2'])
        
        # Encode symptoms
        symptoms_encoded = encoder.transform(symptoms_df)

        # Predict using the trained model
        prediction = model.predict(symptoms_encoded)[0]
        confidence = max(model.predict_proba(symptoms_encoded)[0]) * 100  # Convert to %

        return prediction, confidence

    except Exception as e:
        return f"Prediction Error: {str(e)}", 0

# ==========================
# Run in Command Line
# ==========================

if __name__ == "__main__":
    user_symptoms = input("Enter symptoms separated by commas (e.g., fever,cough): ").split(",")
    prediction, confidence = predict_health_condition(user_symptoms)
    print(f"Prediction: {prediction}, Confidence: {confidence:.2f}%")
