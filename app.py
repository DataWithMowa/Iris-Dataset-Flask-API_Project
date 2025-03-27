import pickle
from flask import Flask, request, jsonify
import numpy as np
import os

# Initialize the Flask application
app = Flask(__name__)

# Load the trained model
with open('iris_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define the API endpoint for making predictions
@app.route('/predict', methods=['POST'])
def predict():
 # Get the data from the POST request
    data = request.get_json()

# Ensure data is in the correct format (should be a list of 4 feature values)
    if not data or 'features' not in data or len(data['features']) != 4:
        return jsonify({"error": "Invalid input data"}), 400

# Convert input data into numpy array for prediction
    input_data = np.array([data['features']])

 # Get the prediction from the model
    prediction = model.predict(input_data)

 # Define the species for the predicted class
    species = ['Setosa', 'Versicolor', 'Virginica']

# Return the prediction result in JSON format
    return jsonify({"predicted_species": species[prediction[0]]})

if __name__ == '__main__':
	app.run(debug=True)
