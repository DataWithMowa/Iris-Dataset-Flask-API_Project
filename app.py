import pickle
from flask import Flask, request, jsonify
import numpy as np
import threading

# Initialize the Flask application
app = Flask(__name__)

# Load the trained model (make sure 'iris_model.pkl' is in the same directory)
with open('iris_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define the API endpoint for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the POST request
    data = request.get_json()
    
    # Ensure data is in the correct format (should be a list of 4 feature values)
    if not data or len(data['features']) != 4:
        return jsonify({"error": "Invalid input data"}), 400
    
    # Convert input data into numpy array for prediction
    input_data = np.array([data['features']])
    
    # Get the prediction from the model
    prediction = model.predict(input_data)
    
    # Define the species for the predicted class
    species = ['Setosa', 'Versicolor', 'Virginica']
    
    # Return the prediction result in JSON format
    return jsonify({"predicted_species": species[prediction[0]]})

# Run the application in a separate thread
def run_flask():
    app.run(debug=True, use_reloader=False)  # use_reloader=False to prevent double execution in notebook

# Start the Flask app in a separate thread
thread = threading.Thread(target=run_flask)
thread.start()
