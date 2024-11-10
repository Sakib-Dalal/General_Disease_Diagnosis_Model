from flask import Flask, render_template, request
import pandas as pd
import pickle

# Flask App
app = Flask(__name__)

app.secret_key = 'sdakq3wjp29q3jerwo349u1205p4ejfoq8234m0nf380623456245njdkfsgh'

# Home Page
@app.route('/')
def home():
    return render_template("index.html")

def getData():
    age = int(request.form.get("age"))
    weight = int(request.form.get("weight"))
    height = int(request.form.get("height"))
    blood_pressure = int(request.form.get("bloodPressure"))

    input_data = pd.DataFrame([[age, weight, height, blood_pressure]], columns=["Age", "Weight_kg", "Height_cm", "Blood_Pressure_mmHg"])
    return input_data

def modelPredict(input_data):
    # Load Model
    with open('model_2000.pkl', 'rb') as file:
        model = pickle.load(file)
    y_pred = model.predict(input_data)
    return y_pred

# Prediction Route
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    try:
        data = getData()
        output = int(modelPredict(data))
        return f"""<h1>output: {output}</h1>"""
    except:
        return """<h1>Bad Input Data</h1>"""

if __name__ == "__main__":
    app.run(debug=True, port="80", host="0.0.0.0")