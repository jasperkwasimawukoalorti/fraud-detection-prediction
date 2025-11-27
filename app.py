import streamlit as st
import joblib
import pandas as pd
import numpy as np
import os

# --- Configuration and Initialization ---
# Load the model, scaler, and feature list
try:
    # Check for the model and scaler files in the current directory
    if not os.path.exists('random_forest_model.pkl') or not os.path.exists('scaler.pkl'):
        st.error("Error: Model or Scaler files not found. Please run the ML Notebook first to save 'random_forest_model.pkl' and 'scaler.pkl'.")
    else:
        model = joblib.load('random_forest_model.pkl')
        scaler = joblib.load('scaler.pkl')
except Exception as e:
    st.error(f"Failed to load model/scaler: {e}")
    st.stop() # Stop the app if crucial files are missing or corrupted

# Define the features that require scaling and the one-hot encoded column names
SCALED_COLS = ['amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest']
TYPE_COLS = ['type_CASH_OUT', 'type_DEBIT', 'type_PAYMENT', 'type_TRANSFER'] # Excludes 'CASH_IN' (the baseline for one-hot encoding)

# --- Streamlit App UI ---
st.set_page_config(page_title="Fraud Detection Prediction App", layout="centered", initial_sidebar_state="auto")
st.title("💸 Fraud Detection Prediction App") # Title
st.markdown("Enter the transaction details below to predict if it is fraudulent or not.") # Instruction text

# Recommended Dark Theme can be set in Streamlit settings (config.toml or user settings)

# Input Sections
with st.form("fraud_prediction_form"):
    st.header("Transaction Details")

    # Transaction Type Dropdown
    transaction_type = st.selectbox(
        "Transaction Type",
        ('CASH_IN', 'CASH_OUT', 'DEBIT', 'PAYMENT', 'TRANSFER')
    )

    # Input Fields
    amount = st.number_input("Transaction Amount", min_value=0.0, format="%.2f")
    oldbalanceOrg = st.number_input("Old Sender Balance", min_value=0.0, format="%.2f")
    newbalanceOrig = st.number_input("New Sender Balance", min_value=0.0, format="%.2f")
    oldbalanceDest = st.number_input("Old Receiver Balance", min_value=0.0, format="%.2f")
    newbalanceDest = st.number_input("New Receiver Balance", min_value=0.0, format="%.2f")

    predict_button = st.form_submit_button("Predict Fraudulence") # Predict button

# --- Prediction Logic ---
if predict_button:
    # 1. Create a DataFrame from user inputs
    input_data = {
        'amount': amount,
        'oldbalanceOrg': oldbalanceOrg,
        'newbalanceOrig': newbalanceOrig,
        'oldbalanceDest': oldbalanceDest,
        'newbalanceDest': newbalanceDest,
        # Initialize one-hot encoded columns to 0
        'type_CASH_OUT': 0, 'type_DEBIT': 0, 'type_PAYMENT': 0, 'type_TRANSFER': 0
    }
    input_df = pd.DataFrame([input_data])

    # 2. Apply One-Hot Encoding based on the selected 'transaction_type'
    # 'CASH_IN' is the baseline (all type_ columns remain 0)
    if transaction_type != 'CASH_IN':
        one_hot_col = f'type_{transaction_type}'
        if one_hot_col in input_df.columns:
            input_df[one_hot_col] = 1

    # 3. Apply the saved StandardScaler to the numerical features
    input_df[SCALED_COLS] = scaler.transform(input_df[SCALED_COLS])

    # 4. Ensure the columns are in the same order as the training data (critical for model)
    # The final columns must match the order in 'model_features' saved in the notebook, but here we assume the order created is:
    # amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest, type_CASH_OUT, type_DEBIT, type_PAYMENT, type_TRANSFER
    final_features = SCALED_COLS + TYPE_COLS
    input_df = input_df[final_features]

    # 5. Make prediction
    prediction = model.predict(input_df)[0]
    prediction_proba = model.predict_proba(input_df)[0] # Get probabilities for a richer output

    # 6. Display Output
    st.subheader("Prediction Result")
    if prediction == 1:
        st.error(f"🚨 **Fraud Alert!** This transaction is predicted as **Fraudulent (1)** with a probability of {prediction_proba[1]*100:.2f}%.")
        st.balloons() # Show alert message
    else:
        st.success(f"✅ **Success!** This transaction is predicted as **Not Fraudulent (0)** with a probability of {prediction_proba[0]*100:.2f}%.")
