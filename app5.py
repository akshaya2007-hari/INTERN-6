import streamlit as st
import pickle
import pandas as pd

# App title
st.title("🚗 Vehicle Maintenance Prediction")

st.write("Predict whether vehicle maintenance is needed based on kilometers driven.")

# Load trained model
with open("model2.pkl", "rb") as f:
    model = pickle.load(f)

# User input
km_driven = st.number_input(
    "Enter Kilometers Driven",
    min_value=0,
    step=100
)

# Predict button
if st.button("Predict Maintenance"):
    input_data = pd.DataFrame([[km_driven]], columns=["km_driven"])
    
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("🔧 Maintenance is REQUIRED")
    else:
        st.success("✅ Maintenance is NOT required")
