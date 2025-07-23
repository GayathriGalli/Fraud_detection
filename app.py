#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Save this as app.py

import streamlit as st
import pandas as pd
import pickle

# Load model and scaler
model = pickle.load(open('xgb_fraud_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.title("Fraud Detection App")

uploaded_file = st.file_uploader("C:\\Users\\goecg\\Downloads\\creditcard.csv", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Data preview:", data.head())

    # Preprocess and scale
    data_scaled = scaler.transform(data)

    # Predict
    preds = model.predict(data_scaled)
    proba = model.predict_proba(data_scaled)[:, 1]

    data['Fraud_Prediction'] = preds
    data['Fraud_Probability'] = proba

    st.write(data)


# In[ ]:




