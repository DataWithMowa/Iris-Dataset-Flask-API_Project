from flask import Flask, request, jsonify, render_template_string
import numpy as np
import joblib
from asgiref.wsgi import WsgiToAsgi

app = Flask(__name__)
model = joblib.load('iris_model.pkl')
iris_classes = ['setosa', 'versicolor', 'virginica']

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = data['features']
        features_array = np.array(features).reshape(1, -1)
        prediction = model.predict(features_array)[0]
        species = iris_classes[prediction]
        return jsonify({'prediction': species})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        features = [float(request.form['f1']), float(request.form['f2']),
                    float(request.form['f3']), float(request.form['f4'])]
        features_array = np.array(features).reshape(1, -1)
        prediction = model.predict(features_array)[0]
        species = iris_classes[prediction]
        return render_template_string(HTML_FORM, prediction=species)
    return render_template_string(HTML_FORM, prediction=None)

HTML_FORM = '''
    <h1>Iris Prediction</h1>
    <form method="post">
        <label>Sepal Length: <input type="number" step="0.1" name="f1" value="5.1"></label><br>
        <label>Sepal Width: <input type="number" step="0.1" name="f2" value="3.5"></label><br>
        <label>Petal Length: <input type="number" step="0.1" name="f3" value="1.4"></label><br>
        <label>Petal Width: <input type="number" step="0.1" name="f4" value="0.2"></label><br>
        <input type="submit" value="Predict">
    </form>
    {% if prediction %}
        <h2>Prediction: {{ prediction }}</h2>
    {% endif %}
'''

app = WsgiToAsgi(app)