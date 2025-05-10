# 🌸 Iris Dataset Flask API Project

<div align="center">
  <img src="Iris Image copy.png"="iris Flower Image" width="auto" height="auto">
</div>

## 📘 Introduction: 
<details>
  <summary>Click to expand</summary>
  <br>

Welcome to the Iris Dataset Flask API project! This application provides a simple, RESTful API built with Flask to predict the species of an Iris flower based on its sepal and petal measurements. Leveraging the classic Iris dataset, a staple in machine learning, this project demonstrates how to deploy a trained model as a web service, making predictions accessible via HTTP requests.

The API accepts feature inputs (sepal length, sepal width, petal length, and petal width) and returns the predicted species: *Setosa*, *Versicolor*, or *Virginica*. Whether you're exploring machine learning deployment, testing API integrations, or just curious about the Iris flowers, this project offers a lightweight and practical starting point.

Key features:
- Built with Flask for simplicity and scalability.
- Trained on the well-known Iris dataset from scikit-learn.
- Easy-to-use endpoint for real-time predictions.

This README will guide you through setup, usage, and contributing to the project. Let’s dive in and classify some flowers!

</details>

## 🎯 Project Objective:
<details>
  <summary>Click to expand</summary>
 <br>

The objective of this project is to create a lightweight Flask-based RESTful API that enables users to predict the species of an Iris flower by providing its sepal and petal measurements. It aims to demonstrate a practical deployment of a machine learning model, offering an accessible and educational tool for real-time classification of the Iris dataset.
 </details>

## 🖥️ How To Create This Flask App Locally:
<details>
  <summary>Click to expand</summary>

## What You’ll Need
- A computer (Windows, Mac, or Linux).
- An internet connection (to download stuff and use Railway).
- About 30 minutes for local setup, or 1 hour minutes if you add Railway.

## Step 1: Install Python (For Local Setup)
Python is the tool that runs this app locally. Let’s get it set up:
1. **Download Python**:
   - Go to [python.org/downloads](https://www.python.org/downloads/).
   - Click the big yellow "Download Python 3.x.x" button (e.g., 3.11.9 as of April 2025). I used 3.9.13 version though.
2. **Install It**:
   - **Windows**: Run the file. Check "Add Python to PATH" at the bottom, then click "Install Now."
   - **Mac**: Open the file and follow the steps.
   - **Linux**: You might already have it—skip to Step 2 if `python3 --version` works in a terminal.
3. **Check It Worked**:
   - Open a terminal:
     - Windows: Press `Win + R`, type `cmd`, press Enter.
     - Mac: Search "Terminal" in Spotlight.
     - Linux: Open your terminal app.
   - Type `python --version` (or `python3 --version` on Mac/Linux) and press Enter. You should see "Python 3.11.9." If not, repeat this step.

## Step 2: Get the App Files
You’ll need these files to run the app locally or online:
1. **Download the Files**:
   - Get these from me (or a link I provide):
     - `app.py`: The main app file (updated with a friendly interface below).
     - `iris_model.pkl`: The brain that makes predictions.
     - `requirements.txt`: A list of tools the app needs.
     - `Procfile`: Tells Railway how to run the app (only needed for online setup).
   - Save them in one folder (e.g., "IrisApp" on your Desktop).
2. **Check They’re There**:
   - Open the folder and confirm you see all four files.

## Step 3: Set Up the Tools (For Local Setup)
The app needs some Python tools (like Flask). Here’s how to install them:
1. **Open Your Terminal**:
   - Use `cmd` (Windows), Terminal (Mac), or your Linux terminal.
2. **Go to Your Folder**:
   - Type this and press Enter (replace "Desktop/IrisApp" with your folder’s path):
     - Windows: `cd Desktop\IrisApp`
     - Mac/Linux: `cd Desktop/IrisApp`
3. **Install the Tools**:
   - Type this and press Enter:
     ```
     pip install -r requirements.txt
     ```
   - Wait a minute—it’s downloading stuff. It’s done when you get a new prompt.
   - If it fails, try `pip3 install -r requirements.txt`.

## Step 4: Run the App Locally
Let’s start the app on your computer with a friendly interface:
1. **Update `app.py`**:
   - Open `app.py` in a text editor (like Notepad on Windows or TextEdit on Mac).
   - Replace its contents with this (it adds a simple webpage):
     ```
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

     # No need to run it here—use the terminal command below
     ```
   - Save the file.
2. **Start the App**:
   - In your terminal (still in the "IrisApp" folder), type:
     ```
     uvicorn app:app --host 0.0.0.0 --port 5000
     ```
   - You’ll see "Uvicorn running on http://0.0.0.0:5000." Keep this terminal open.
3. **Test in a Browser**:
   - Open your web browser (like Chrome or Firefox).
   - Go to `http://localhost:5000`.
   - You’ll see a form. Enter numbers (e.g., 5.1, 3.5, 1.4, 0.2), click "Predict," and see the result (like "setosa")!

## Step 5: Test Locally with a Command (Optional)
If you want to try it like a programmer:
1. **Open a New Terminal**:
   - Keep the app running in the first terminal.
   - Open another one (same way as before).
2. **Run This**:
   - Type:
     ```
     curl -X POST -H "Content-Type: application/json" -d "{\"features\": [5.1, 3.5, 1.4, 0.2]}" http://localhost:5000/predict
     ```
   - You’ll see `{"prediction": "setosa"}`. (Windows users: If "curl" doesn’t work, download it from [curl.se/windows](https://curl.se/windows/), unzip, and use `curl.exe` instead.)

## Step 6: Put It Online with Railway
Want others to use your app online? Railway is a free service that hosts your app so anyone with the link can access it. Here’s why we use Railway and how to set it up:

### Why Railway?
- It’s free (for small apps) and easy—no need to manage a server yourself.
- It puts your app on the internet fast, so friends or family can try it.
- It handles updates automatically when you change the files.

### How to Set Up Railway
1. **Sign Up**:
   - Go to [railway.app](https://railway.app).
   - Click "Login" and sign up with your email or GitHub account (GitHub is easiest if you have it).
2. **Create a New Project**:
   - Click "New Project" on the dashboard.
   - Choose "Deploy from GitHub" (if you know Git) or "Empty Project" (simpler).
3. **Upload Your Files**:
   - **If Using GitHub**:
     - Put your folder (`app.py`, `iris_model.pkl`, `requirements.txt`, `Procfile`) in a GitHub repo. (Ask me if you need help with Git!)
     - Link your GitHub account in Railway and select the repo.
   - **If Manual**:
     - Click your project in Railway, go to "Deploy," and drag your folder (with all four files) into the upload area.
4. **Add the Procfile**:
   - If you don’t have it yet, create a file named `Procfile` (no extension) in your folder.
   - Open it in a text editor and add this line:
     ```
     web: uvicorn app:app --host 0.0.0.0 --port $PORT
     ```
   - Save it and include it with your files.
5. **Deploy It**:
   - Railway will start building your app (you’ll see logs). Wait a minute or two.
   - When it says "Deployed," click the URL (like `https://something.up.railway.app`).
6. **Test It**:
   - In your browser, go to `https://your-url.up.railway.app` (replace with your Railway URL).
   - Use the form to predict an Iris flower!

## Step 7: Test Online with Postman Web
Postman is a free tool to test your online app like a pro. Here’s how to use the web version:
1. **Go to Postman**:
   - Open your browser and go to [web.postman.co](https://web.postman.co).
   - Sign up with your email (or log in if you have an account).
2. **Set Up a Test**:
   - Click "New" > "HTTP Request."
   - In the box at the top, type your Railway URL with `/predict` (e.g., `https://your-url.up.railway.app/predict`).
   - Change "GET" to "POST" in the dropdown.
   - Click the "Body" tab below the URL.
   - Select "raw" and set the type to "JSON" (from the dropdown).
   - Type this in the body:
     ```
     {"features": [5.1, 3.5, 1.4, 0.2]}
     ```
3. **Send It**:
   - Click the blue "Send" button.
   - Look at the bottom—you should see `{"prediction": "setosa"}` (or similar).

## Step 8: Stop the App (Local Only)
- If running locally, go to the terminal with Uvicorn and press `Ctrl + C`.

## What Does It Do?
This app takes four numbers and guesses an Iris flower type using a pre-trained model. You can use it locally in your browser or share it online with Railway!

## Troubleshooting
- **Python Issues?**: Reinstall from Step 1.
- **Files Missing?**: Ensure you have all four files in your folder.
- **Railway Fails?**: Check the logs in Railway for errors (e.g., missing `Procfile`).
- **Errors?**: Copy the error and ask me or a friend.

## My Online Version
I’ve hosted this app at `https://web-production-182ae.up.railway.app`. Try it in your browser or with Postman!

Enjoy your Iris Prediction App!
</details>

## 📂 Data Overview:
<details>
  <summary>Click to expand</summary>
  <br>

This app uses the Iris dataset, a famous collection of flower measurements, to predict Iris flower types. You don’t need to download it—it’s already built into the app’s brain (the `iris_model.pkl` file). Here’s what it’s all about:

### What’s in the Dataset:

- **Sepal Length**: The length of the flower’s sepal (the green part under the petals), measured in centimeters. Think of it as the flower’s "base height."
- **Sepal Width**: The width of the sepal, also in centimeters. This is how wide the base spreads out.
- **Petal Length**: The length of the flower’s petals (the colorful part), in centimeters. It’s like measuring the "showy" part of the flower.
- **Petal Width**: The width of the petals, in centimeters. This tells us how broad the petals are.
- **Species**: The type of Iris flower—either "setosa," "versicolor," or "virginica." This is what the app guesses based on the four measurements above!

The app’s pre-trained model uses these four numbers (sepal length, sepal width, petal length, petal width) to figure out which species the flower is. You just type in the numbers, and it does the rest!

</details>

## ⚙️ Tools and Libraries Used:
<details>
  <summary>Click to expand</summary>
  <br>

Here’s an explanation of the tools and libraries used in your Iris Prediction Flask app:

### Python
- **What It Is**: The main programming language that runs the app. It’s like the kitchen where everything happens.
- **Why We Use It**: Python is easy to work with and great for building apps like this. It’s what makes the app understand the code in `app.py`.

### Flask
- **What It Is**: A tool that helps create web apps. Think of it as the oven that bakes your app so it can run on the internet or your computer.
- **Why We Use It**: Flask lets us make the `/predict` page and the home page with the form. It listens for your requests (like submitting numbers) and sends back answers (like "setosa").

### Uvicorn
- **What It Is**: A helper that runs the Flask app smoothly. It’s like a waiter who serves your app to users.
- **Why We Use It**: Uvicorn makes sure the app starts up and handles requests fast, whether it’s on your computer or online with Railway.

### NumPy
- **What It Is**: A library for handling numbers and math. Imagine it as a calculator for the app.
- **Why We Use It**: The app uses NumPy to turn your four measurements (like 5.1, 3.5, 1.4, 0.2) into a format the model can understand for predictions.

### Joblib
- **What It Is**: A tool that loads the pre-trained model. It’s like a librarian who fetches a book (the model) for us.
- **Why We Use It**: Joblib reads the `iris_model.pkl` file so the app can use the model to guess the flower type without retraining it.

### Scikit-Learn
- **What It Is**: A library for machine learning (smart guessing). Think of it as the brain trainer that made the model.
- **Why We Use It**: The Iris model was built with Scikit-Learn before we saved it. The app needs it to understand how the model works when making predictions.

### Asgiref
- **What It Is**: A small helper that connects Flask and Uvicorn. It’s like a translator between two friends who speak different languages.
- **Why We Use It**: Flask and Uvicorn work in slightly different ways (WSGI vs. ASGI), and Asgiref makes sure they get along so the app runs properly.

### Railway (For Online Hosting)
- **What It Is**: A free service that puts your app on the internet. It’s like a stage where your app performs for the world.
- **Why We Use It**: Railway makes it easy to share your app online without needing your own server. It sets everything up and gives you a link (like `https://your-url.up.railway.app`).

### Postman (For Testing)
- **What It Is**: A free tool to test the app, especially online. Think of it as a practice dummy for trying out requests.
- **Why We Use It**: Postman lets you send numbers to the app and see the prediction, which is handy for checking if it works online.

</details>

## 🚧 Limitations:
<details> <summary>Click to expand</summary> <br>
  
This app is awesome, but it’s not perfect! Here are some things it can’t do:

- **Only Works for Iris Flowers**: It’s trained on the Iris dataset, so it can only predict "setosa," "versicolor," or "virginica." It won’t work for other flowers or anything else.
  
- **Needs Four Numbers**: You have to give it exactly four measurements (sepal length, sepal width, petal length, petal width) in the right order, or it’ll get confused.
  
- **No Fancy Explanations**: It just tells you the flower type—it doesn’t explain why or show you the math behind it.
  
- **Simple Online Version**: If you use it online with Railway, anyone with the link can try it.
  
- **Depends on the Model**: The predictions are only as good as the iris_model.pkl file. If it’s not perfect, the app won’t be either.
  
</details>

## 🔥 Challenges Faced:
<details> <summary>Click to expand</summary> <br>
  
Getting this app up and running wasn’t easy. It took a lot of patience and trial-and-error! Here’s what I ran into and how I got through it:

**Deployment Headaches**: I tried deploying this app on Railway more than 20 times before anything worked. The build process kept failing because of things like wrong Python versions, missing packages, or modules that wouldn’t install. One error even said a package needed Rust (a programming tool) to build, but Railway didn’t have it ready. Figuring out what went wrong each time took many hours of debugging!

**Finally Deployed, Then Crashed**: Around the 30th or 40th try, the app built successfully but then it crashed right after. More attempts followed (maybe 50 in total!), fixing things like Python mismatches, Windows-specific issues, and missing libraries.

**Public URL Trouble**: Even after it deployed successfully, the app wouldn’t work as a public URL. I spent another chunk of time testing and tweaking until the curl command finally worked. It was a long road, but it paid off! Whew!

This taught me that deploying an app can be tricky, especially when tools don’t play nice together. If you hit bumps like these, don’t give up, keep trying, check the error messages, and adjust step-by-step. It’s all worth it when it finally works!
</details>

## 🔎 Summary:
<details> <summary>Click to expand</summary> <br>
  
This Iris Prediction App is a simple way to guess Iris flower types using four measurements! 
  
You can run it on your computer with a friendly webpage or put it online with Railway so others can try it. It uses Python and some tools like Flask and Uvicorn to work, and the pre-trained model does the smart guessing for us. 

Whether you’re testing it locally with a browser or sharing it online with Postman, it’s an easy way to see machine learning in action. Enjoy predicting flowers!

</details>

## 😊 Enjoy Coding!


