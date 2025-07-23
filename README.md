# 💳 Credit Card Fraud Detection App

A web application built using **Streamlit** to predict credit card fraud using a pre-trained **XGBoost** model.


## 🚀 Features

- Upload your own CSV file with transaction data (same format as `creditcard.csv`)
- Predict fraudulent transactions (fraud vs non-fraud)
- Show fraud probability scores for each transaction
- Filter transactions by fraud status and probability threshold


## 🛠️ Included Files

| File               | Description                       |
|--------------------|---------------------------------|
| `app.py`           | Main Streamlit app script        |
| `xgb_model.pkl`    | Pre-trained XGBoost model file   |
| `requirements.txt` | Python dependencies              |
| `README.md`        | Project overview and instructions|
| `creditcard.csv`   | Sample data file (optional)      |



## 📂 How to Run Locally
```bash
1. Clone the repository:
git clone https://github.com/yourusername/fraud-detection-app.git
cd fraud-detection-app

2. Install required packages:
pip install -r requirements.txt

3. Run the Streamlit app:
streamlit run app.py

4.Upload your CSV file in the app interface to start predicting frauds!
It’s clear, simple, and practical — perfect for your users!
