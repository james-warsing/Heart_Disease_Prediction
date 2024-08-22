import streamlit as st
import pickle
import gzip
import numpy as np

# Compressed model file
compressed_model_filename = 'c:/Users/James/OneDrive/Documents/Flatiron/Final_project/Heart_Disease_Prediction/final_stacked_model.pkl.gz'

# Load the compressed model
with gzip.open(compressed_model_filename, 'rb') as file:
    model = pickle.load(file)

# Function to make predictions
def predict_heart_disease(model, input_data):
    # Convert input data to a numpy array
    input_array = np.array(input_data).reshape(1, -1)
    
    # Predict using the model
    prediction = model.predict(input_array)
    
    # Return the prediction
    return prediction[0]

# Streamlit app interface
st.markdown("<h1 style='text-align: center;'>❤️ Heart Disease Risk Prediction</h1>", unsafe_allow_html=True)

st.markdown("This app helps you assess the risk of heart disease based on various health indicators and lifestyle factors.")

st.header("🏥 Demographic Information")
age_category = st.selectbox("Age Range:", ["18-24", "25-29", "30-34", "35-39", "40-44", 
                                           "45-49", "50-54", "55-59", "60-64", "65-69", 
                                           "70-74", "75-79", "80 or older"])
sex = st.selectbox("Gender:", ("Male", "Female"))
race = st.selectbox("Race/Ethnicity:", ("White", "Black", "Asian", "American Indian", "Other"))

st.header("💪 Lifestyle Factors")
smoking = st.selectbox("Do You Smoke?", ("Yes", "No"))
alcohol_drinking = st.selectbox("Do You Consume Alcohol?", ("Yes", "No"))
physical_activity = st.selectbox("Do You Engage in Regular Physical Activity?", ("Yes", "No"))
bmi = st.slider("BMI (Body Mass Index):", 10.0, 50.0, 25.0)
sleep_time = st.slider("Hours of Sleep Per Night:", 0, 24, 8)

st.header("🩺 Health History")
stroke = st.selectbox("Have You Ever Had a Stroke?", ("Yes", "No"))
diabetic = st.selectbox("Are You Diabetic?", ("Yes", "No"))
asthma = st.selectbox("Do You Have Asthma?", ("Yes", "No"))
kidney_disease = st.selectbox("Do You Have Kidney Disease?", ("Yes", "No"))
skin_cancer = st.selectbox("Do You Have Skin Cancer?", ("Yes", "No"))

st.header("🧠 Current Health Status")
physical_health = st.slider("Days of Poor Physical Health in the Past Month:", 0, 30, 0)
mental_health = st.slider("Days of Poor Mental Health in the Past Month:", 0, 30, 0)
diff_walking = st.selectbox("Do You Have Difficulty Walking or Climbing Stairs?", ("Yes", "No"))
gen_health = st.selectbox("General Health Status:", ("Poor", "Fair", "Good", "Very Good", "Excellent"))

# Convert categorical variables to numeric values
sex = 1 if sex == "Male" else 0
smoking = 1 if smoking == "Yes" else 0
alcohol_drinking = 1 if alcohol_drinking == "Yes" else 0
stroke = 1 if stroke == "Yes" else 0
diff_walking = 1 if diff_walking == "Yes" else 0
diabetic = 1 if diabetic == "Yes" else 0
physical_activity = 1 if physical_activity == "Yes" else 0
asthma = 1 if asthma == "Yes" else 0
kidney_disease = 1 if kidney_disease == "Yes" else 0
skin_cancer = 1 if skin_cancer == "Yes" else 0
race_mapping = {"White": 0, "Black": 1, "Asian": 2, "American Indian": 3, "Other": 4}
race = race_mapping[race]

age_category_mapping = {
    "18-24": 0, "25-29": 1, "30-34": 2, "35-39": 3, "40-44": 4, 
    "45-49": 5, "50-54": 6, "55-59": 7, "60-64": 8, "65-69": 9, 
    "70-74": 10, "75-79": 11, "80 or older": 12
}
age_category = age_category_mapping[age_category]

gen_health_mapping = {"Poor": 0, "Fair": 1, "Good": 2, "Very Good": 3, "Excellent": 4}
gen_health = gen_health_mapping[gen_health]

# Prepare input data
input_data = [
    bmi, smoking, alcohol_drinking, stroke, physical_health, mental_health, 
    diff_walking, sex, race, diabetic, physical_activity, gen_health, sleep_time, 
    asthma, kidney_disease, skin_cancer, age_category
]

# Make a prediction when the button is clicked
if st.button("Predict"):
    prediction = predict_heart_disease(model, input_data)
    
    if prediction == 1:
        st.error("⚠️ The model predicts a **high risk** of heart disease.")
    else:
        st.success("✅ The model predicts a **low risk** of heart disease.")

st.markdown("""
**Disclaimer**: This tool is a prototype and should not reflect an actual diagnosis. If you feel you are at risk for heart disease then please consult a healthcare professional.
""")