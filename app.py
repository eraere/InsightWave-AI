from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load the trained model
model = joblib.load('market_demand_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract data from form
        data = request.form.to_dict()
        features = pd.DataFrame([data])
        prediction = model.predict(features)
        logging.info(f'Prediction made: {prediction[0]}')
        return render_template('index.html', prediction_text=f'Predicted Market Demand: {prediction[0]}')
    except Exception as e:
        logging.error(f'Error during prediction: {str(e)}')
        return render_template('index.html', error_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True) 