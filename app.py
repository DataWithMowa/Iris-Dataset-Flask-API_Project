from flask import Flask, request, jsonify
import numpy as np
import joblib
from asgiref.wsgi import WsgiToAsgi  

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('iris_model.pkl') 
iris_classes = ['setosa', 'versicolor', 'virginica']

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = data['features']  # Expecting [5.1, 3.5, 1.4, 0.2]
        features_array = np.array(features).reshape(1, -1)
        prediction = model.predict(features_array)[0]
        species = iris_classes[prediction]
        return jsonify({'prediction': species})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Wrap the Flask WSGI app in an ASGI adapter
app = WsgiToAsgi(app)