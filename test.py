import pickle
import pandas as pd

# Load Model
with open('model_2000.pkl', 'rb') as file:
    model = pickle.load(file)

# Create sample input data
input_data = pd.DataFrame([[170, 70, 25, 120]], columns=['Height_cm', 'Weight_kg', 'Age', 'Blood_Pressure_mmHg'])

# Get predictions
predictions = model.predict(input_data)
print("Model output:", predictions)
