from flask import Flask, render_template, request
import pandas as pd
import pickle

# Flask App Here
app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template("index.html")

with open('model_2000.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    age = float(request.form['age'])
    bloodPressure = float(request.form['bloodPressure'])
    
    input_data = pd.DataFrame([[height, weight, age, bloodPressure]], columns=['Height_cm', 'Weight_kg', 'Age', 'Blood_Pressure_mmHg'])
    
    predictions = model.predict(input_data)

    disease = predictions[0][0]
    fineScore = predictions[0][1]

    # Return both results as a string
    return f"The predicted results are: Disease = {disease}, Fine Score = {fineScore}"

if __name__ == "__main__":
    app.run(debug=True, port="80", host="0.0.0.0")