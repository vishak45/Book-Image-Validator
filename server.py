from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import numpy as np
from PIL import Image
import io
import base64
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
model = load_model("book_validator_model.keras")

@app.route("/predict", methods=["POST"])
def predict4():
    data = request.get_json()
    if "image" not in data:
        return jsonify({"error": "No image provided"}), 400

    # Decode Base64 to bytes
    img_bytes = base64.b64decode(data["image"])
    img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
    img = img.resize((224, 224))

    # Convert to array and preprocess
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Predict
    prob = model.predict(img_array)[0][0]
    label = "VALID" if prob > 0.7 else "INVALID"
    print(label, prob)
    return jsonify({"label": label, "probability": float(prob)})

if __name__ == "__main__":
    app.run(debug=True)
