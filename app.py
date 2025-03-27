from flask import Flask, request, jsonify
from waitress import serve

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = data['features']
    # Replace this with your model logic
    return jsonify({'prediction': features[0]})  # Example response

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)  # Use Waitress instead of app.run()