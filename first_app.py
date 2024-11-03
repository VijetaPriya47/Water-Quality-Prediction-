import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("rf_model.pkl", "rb") as file:
    rf_model = pickle.load(file)

# Function to predict water potability
def predict_potability(params):
    prediction = rf_model.predict([params])[0]
    return "Safe to Drink" if prediction == 1 else "Not Safe to Drink"

# Information about each parameter
def parameter_info():
    st.write("""
    **Water Quality Parameters:**

    - **pH**: A measure of the acidity or alkalinity of water. The recommended range is 6.5-8.5.
    - **Hardness**: Indicates water’s ability to form lather with soap. High levels can lead to scale formation.
    - **Solids (TDS)**: High Total Dissolved Solids can affect the taste and clarity of water; ideal level is below 500 ppm.
    - **Chloramines**: Used as a disinfectant in water treatment, excessive levels can be harmful.
    - **Sulfate**: Dissolved sulfate salts can impart a bitter taste; ideally under 250 mg/L.
    - **Conductivity**: Indicates the water's ability to conduct electricity, related to the concentration of dissolved salts.
    - **Organic Carbon**: Represents organic material in the water; high levels may indicate contamination.
    - **Trihalomethanes (THMs)**: By-products of chlorine disinfection. High THM levels can be harmful.
    - **Turbidity**: The cloudiness of water. High turbidity can be a sign of contamination.
    """)

# Streamlit App
st.title("Water Potability Prediction")
st.write("Enter water quality parameters to check if the water is safe to drink:")

# Set default values to likely safe ranges
pH = st.number_input("pH (6.5-8.5 is ideal)", min_value=0.0, max_value=14.0, value=7.5, step=0.1)
hardness = st.number_input("Hardness (mg/L)", min_value=0.0, max_value=500.0, value=120.0, step=1.0)
solids = st.number_input("Total Dissolved Solids (ppm)", min_value=0.0, max_value=5000.0, value=250.0, step=1.0)
chloramines = st.number_input("Chloramines (ppm)", min_value=0.0, max_value=10.0, value=2.0, step=0.1)
sulfate = st.number_input("Sulfate (mg/L)", min_value=0.0, max_value=500.0, value=180.0, step=1.0)
conductivity = st.number_input("Conductivity (μS/cm)", min_value=0.0, max_value=1000.0, value=400.0, step=1.0)
organic_carbon = st.number_input("Organic Carbon (ppm)", min_value=0.0, max_value=20.0, value=5.0, step=0.1)
trihalomethanes = st.number_input("Trihalomethanes (μg/L)", min_value=0.0, max_value=200.0, value=40.0, step=1.0)
turbidity = st.number_input("Turbidity (NTU)", min_value=0.0, max_value=10.0, value=2.0, step=0.1)

# Predict potability when user clicks the button
if st.button("Check Potability"):
    params = [pH, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]
    result = predict_potability(params)
    st.subheader(f"Prediction: {result}")

# Display additional information
st.write("\n---\n")
parameter_info()
