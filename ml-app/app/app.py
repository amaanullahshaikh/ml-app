import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)  # Correct usage of __name__

# Load the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)  # Proper indentation

@app.route("/")
def home():
    return "Welcome to the ML App!"  # Proper indentation

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json  # Parse the JSON input
    prediction = model.predict([data["features"]])  # Predict using the model
    return jsonify({"prediction": prediction.tolist()})  # Return as JSON

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Proper indentation