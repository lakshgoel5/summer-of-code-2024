from flask import Flask, request, jsonify
import pickle

# Load the pre-trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Create a Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Model API!"

@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)
    
    # Make prediction using the model
    prediction = model.predict(data)
    
    # Return the prediction as JSON
    return jsonify({'prediction': prediction[0]})

# Run the Flask app
if __name__ == '__main__':
    app.run(port=5000, debug=True)
#server: http://127.0.0.1:5000
#Inputs:step,amount,oldbalanceOrg,newbalanceOrig,oldbalanceDest,newbalanceDest,
# isFlaggedFraud,CASH_IN,CASH_OUT,DEBIT,PAYMENT,TRANSFER,C(first letter of NameDest)