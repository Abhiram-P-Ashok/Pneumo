import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from keras.models import model_from_json
from keras.preprocessing import image
import numpy as np
import tensorflow as tf

app = Flask(__name__)


def load_model():
    json_file_path = 'Mobile_classifier.json'
    json_file = open(json_file_path, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    loaded_model.load_weights('Mobile_classifier_weights.h5')
    return loaded_model

class_names = ['Bacterial Pneumonia', 'Normal', 'Viral Pneumonia']
model = load_model()

def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(299, 299))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    return img_array

def classify(image_path):
    model = load_model()
    
    img_array = preprocess_image(image_path)
    
    predictions = model.predict(img_array)
    return predictions

def predict_image(img_path):
    img_array = preprocess_image(img_path)
    predictions = model.predict(img_array)
    return predictions[0]

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        try:
            os.makedirs("static/uploads")
        except FileExistsError:
            pass

        file = request.files["file"]

        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join("static/uploads", filename)
            file.save(filepath)

            predictions = predict_image(filepath)

            predicted_class = class_names[np.argmax(predictions)]
            class_probabilities = predictions[np.argmax(predictions)]

            return jsonify({"prediction": predicted_class, "filename": filename, "probability": float(class_probabilities)})

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
