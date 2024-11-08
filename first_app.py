import streamlit as st
import pickle
import numpy as np

Load the trained model
with open("rf_model.pkl", "rb") as file:
    rf_model = pickle.load(file)

# Function to predict water potability
def predict_potability(params):
    prediction = rf_model.predict([params])[0]
    return "💧 Safe to Drink!" if prediction == 1 else "🚫 Not Safe to Drink"

# Information about each parameter
def parameter_info():
    st.write("""
    ### 🌊 Water Quality Parameters Explained:

    **pH** - A vital measure! This tells us if the water’s acidic or alkaline. Ideal range? Between 6.5 and 8.5 to keep it safe and refreshing. Too low or too high? It could corrode or scale your pipes - and your stomach isn’t a fan either!

    **Hardness** - Ever noticed soap not lathering easily? High hardness in water is why! While hard water isn’t unsafe, softer water means happier soap and scale-free appliances.

    **Solids (TDS)** - Too many dissolved solids affect taste and clarity. Think of it as the “purity meter” - ideally, we keep it under 500 ppm for safe drinking.

    **Chloramines** - Essential for disinfection but a double-edged sword. It’s safe in controlled amounts, but high levels may pose risks.

    **Sulfate** - Adds bitterness if too high. While safe in small amounts, excessive sulfate could lead to gastrointestinal issues.

    **Conductivity** - Indicates the water’s ability to conduct electricity, directly tied to dissolved salts. The more it conducts, the “saltier” it is!

    **Organic Carbon** - Represents the presence of organic materials. Think of it as a contamination indicator; high organic content isn’t good news.

    **Trihalomethanes (THMs)** - By-products from water disinfection. Safe in low amounts, but prolonged exposure to high levels can be harmful.

    **Turbidity** - Measures cloudiness. Higher values may mean contamination, as clear water is usually safer to drink.
    """)


# # Streamlit App
# st.title("Water Potability Prediction")
# st.write("Enter water quality parameters to check if the water is safe to drink:")

# Streamlit App
st.title("🚰 Water Potability Prediction App 🚰")
st.write("### Is your water safe to drink? Let's find out!")

# Explanation Section
st.markdown("""
    ## Why This Matters 🌍
    Access to clean, safe drinking water is a **human right**. Waterborne illnesses are still a global concern, and ensuring water safety is crucial for health and development. Predicting potability helps monitor water quality, reduce health risks, and support economic growth by cutting healthcare costs.

    **This app** leverages data and machine learning to analyze various water characteristics, helping predict if water is safe for consumption. Each parameter tells us a unique story about water quality, offering valuable insights into water's suitability for drinking.
""")

# st.write("\n---\n")
# parameter_info()

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
# Algorithm Section in Streamlit
st.write("## 🧠 Algorithms: The Powerhouses Behind Water Safety Analysis")

st.markdown("""
In this project, we’ve explored a variety of machine learning algorithms to predict water potability, each bringing unique strengths to the table. Let’s take a closer look at the brains behind the operation:

- **Logistic Regression** 🔄  
   A go-to for binary classification! Logistic regression calculates the probability of water being safe (1) or unsafe (0). It's lightweight—fast and easy to interpret, making it a solid first approach!

- **K-Nearest Neighbors (KNN)** 👥  
   Imagine trying to find similar friends in a crowd! KNN classifies new data by identifying the closest “neighbors” and voting on whether they’re in the safe or unsafe water category. Simple and intuitive, though it can slow down with large datasets.

- **Support Vector Machine (SVM)** ✂️  
   SVM excels at separating data points with a “hyperplane” to classify if water is drinkable or not. It’s especially powerful with complex datasets and excels at finding patterns when water quality data is a bit tricky.

- **Decision Tree** 🌳  
   This model maps decisions in a tree-like structure, branching out at each feature like pH or Chloramines to determine water safety. Easy to interpret, it offers insight into which parameters impact potability the most.

- **Random Forest** 🌲🌲🌲  
   A forest of decision trees! Random Forest builds multiple trees and combines their votes for a robust prediction. This “ensemble” approach reduces errors, making it our most accurate model so far at **70% accuracy**! Think of it as having multiple experts weigh in on water safety.

- **XGBoost** 🚀  
   A high-performance cousin of Random Forest, XGBoost uses “boosting” to refine each decision tree, which increases both speed and accuracy. Perfect for capturing even more patterns in our water data!

---

### 🚀 **Best Model Accuracy So Far: 70% with Random Forest!** 🚀

Our highest accuracy currently sits at 70%, but we’re not stopping here! Here’s what’s next in our quest for cleaner, safer water:

1. **Advanced Model Tuning** 🛠️  
    - We’re experimenting with hyperparameter tuning to refine our models even further. Small tweaks like adjusting the number of trees in Random Forest or the learning rate in XGBoost could make a significant impact on accuracy.

2. **Exploring Ensemble Methods** 👥  
    - Beyond single models, we’re blending algorithms together! Combining predictions from Random Forest and XGBoost could lead to an even higher accuracy rate than using one model alone.

3. **Testing Deep Learning Models** 🤖  
    - For a deeper dive, we’re also considering neural networks to capture complex patterns in water quality data. This could be especially useful in real-time applications with large datasets.

4. **Feature Engineering & Selection** 🔬  
    - By analyzing the importance of each feature, we can refine which parameters contribute most to water safety, optimizing both speed and accuracy.

---

These algorithms work together as our toolkit, bringing us closer to making water safety predictions as accurate and accessible as possible. With every model tweak, we’re one step closer to a safer, cleaner water supply! 🚰💧 

Stay tuned for updates on our journey towards clean water for everyone! 🌍💧
""")

