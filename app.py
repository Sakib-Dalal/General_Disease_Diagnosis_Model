from flask import Flask, render_template, request
import pandas as pd
import pickle

# Flask App
app = Flask(__name__)

# Load Model
with open('model_2000.pkl', 'rb') as file:
    model = pickle.load(file)

# Home Page
@app.route('/')
def home():
    return render_template("index.html")

# Prediction Route
@app.route('/predict', methods=['POST'])
def predict():
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    age = float(request.form['age'])
    bloodPressure = float(request.form['bloodPressure'])
    
    input_data = pd.DataFrame([[height, weight, age, bloodPressure]], columns=['Height_cm', 'Weight_kg', 'Age', 'Blood_Pressure_mmHg'])
    
    predictions = model.predict(input_data)
    disease = predictions[0]

    return f"The predicted disease is: {disease}"

if __name__ == "__main__":
    app.run(debug=True, port="80", host="0.0.0.0")
