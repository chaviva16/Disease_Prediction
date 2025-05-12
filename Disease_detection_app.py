import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load trained models
rf_model = joblib.load("random_forest_model.pkl")
nb_model = joblib.load("naive_bayes_model.pkl")
svm_model = joblib.load("svm_model.pkl")
encoder = joblib.load("label_encoder.pkl")
scaler = joblib.load("scaler.pkl")

# Load symptom index mapping
X = pd.read_csv(r'C:\Users\USER\Downloads\improved_disease_dataset.csv').iloc[:, :-1]
symptom_index = {symptom: idx for idx, symptom in enumerate(X.columns)}

# ------------------------------------------
# Load Model Weights
# ------------------------------------------
rf_accuracy = 0.53  # Replace with actual saved values if needed
nb_accuracy = 0.16
svm_accuracy = 0.54

total_accuracy = rf_accuracy + nb_accuracy + svm_accuracy

# Prevent division by zero errors
if total_accuracy == 0:
    rf_weight, nb_weight, svm_weight = 1/3, 1/3, 1/3
else:
    rf_weight = rf_accuracy / total_accuracy
    nb_weight = nb_accuracy / total_accuracy
    svm_weight = svm_accuracy / total_accuracy

# ------------------------------------------
# Streamlit UI
# ------------------------------------------
st.title("Disease Prediction App 🏥")
st.write("Enter symptoms below to predict the disease.")

# User Input
input_symptoms = st.text_input("Symptoms (comma-separated, e.g., Fever, Headache, Nausea)")

def predict_disease(input_symptoms):
    input_symptoms = input_symptoms.split(",")
    input_data = [0] * len(symptom_index)

    for symptom in input_symptoms:
        symptom = symptom.strip()
        if symptom in symptom_index:
            input_data[symptom_index[symptom]] = 1

    input_data = pd.DataFrame([input_data], columns=list(symptom_index.keys()))
    input_data = pd.DataFrame(scaler.transform(input_data), columns=X.columns)  # Apply scaling

    # Generate predictions
    rf_pred = encoder.classes_[rf_model.predict(input_data)[0]]
    nb_pred = encoder.classes_[nb_model.predict(input_data)[0]]
    svm_pred = encoder.classes_[svm_model.predict(input_data)[0]]

    # Weighted voting using globally defined weights
    weighted_preds = {rf_pred: rf_weight, nb_pred: nb_weight, svm_pred: svm_weight}
    final_pred = max(weighted_preds, key=weighted_preds.get)

    return {
        "Random Forest Prediction": rf_pred,
        "Naive Bayes Prediction": nb_pred,
        "SVM Prediction": svm_pred,
        "Final Prediction": final_pred
    }

# ------------------------------------------
# Run Prediction on User Input
# ------------------------------------------
if st.button("Predict"):
    if input_symptoms:
        result = predict_disease(input_symptoms)
        st.success("Prediction Completed!")
        for model, prediction in result.items():
            st.write(f"**{model}:** {prediction}")
    else:
        st.warning("Please enter symptoms before predicting.")
