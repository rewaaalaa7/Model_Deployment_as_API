from flask import Flask, request, jsonify
import numpy as np
import pickle
import os

app = Flask(__name__)

# Model paths
model_paths = {
    "Logistic Regression": "models/LogisticRegression_model.pkl",
    "Random Forest": "models/RandomForest_model.pkl",
    "Support Vector Machine": "models/SVC_model.pkl",
    "K-Nearest Neighbors": "models/KNeighbors_model.pkl"
}

# Test accuracies (for optional response info)
model_accuracies = {
    "Logistic Regression": 91.11,
    "Random Forest": 97.78,
    "Support Vector Machine": 97.78,
    "K-Nearest Neighbors": 95.56
}

# Iris class labels
iris_classes = ['Setosa', 'Versicolor', 'Virginica']

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Iris Classifier API!"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # Validate input
    try:
        features = np.array(data["features"]).reshape(1, -1)
        model_name = data["model"]
    except:
        return jsonify({"error": "Invalid input. Expected 'features': [sl, sw, pl, pw] and 'model': model_name"}), 400

    # Load model
    model_path = model_paths.get(model_name)
    if not model_path or not os.path.exists(model_path):
        return jsonify({"error": f"Model '{model_name}' not found."}), 404

    with open(model_path, "rb") as f:
        model = pickle.load(f)

    # Predict
    prediction = model.predict(features)[0]
    label = iris_classes[prediction]
    accuracy = model_accuracies.get(model_name, "Unknown")

    return jsonify({
        "prediction": label,
        "model": model_name,
        "accuracy": accuracy
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

