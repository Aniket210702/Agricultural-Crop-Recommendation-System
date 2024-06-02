from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
loaded_model = joblib.load('model.pkl')
app = Flask(__name__)
CORS(app)
labels = {20: 'rice', 11: 'maize', 3: 'chickpea', 9: 'kidneybeans', 18: 'pigeonpeas', 13: 'mothbeans', 14: 'mungbean', 2: 'blackgram', 10: 'lentil', 19: 'pomegranate', 1: 'banana', 12: 'mango', 7: 'grapes', 21: 'watermelon', 15: 'muskmelon', 0: 'apple', 16: 'orange', 17: 'papaya', 4: 'coconut', 6: 'cotton', 8: 'jute', 5: 'coffee'}
@app.route('/', methods=['GET'])
def home():
    return 'Server is running!!'
@app.route('/', methods=['POST'])
def predict():
    try:
        input_data = request.get_json()
        input_df = pd.DataFrame(input_data)
        predictions = loaded_model.predict(input_df)
        response = {'predictions': labels[predictions.tolist()[0]]}
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)})
if __name__ == '__main__':
    app.run()