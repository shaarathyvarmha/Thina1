from flask import Flask, request, jsonify
import pandas as pd
from model import predict_health_condition

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction, confidence = predict_health_condition(data)
    return jsonify({'prediction': prediction, 'confidence': confidence})

if __name__ == '__main__':
    app.run(debug=True)