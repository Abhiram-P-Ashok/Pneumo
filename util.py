import tensorflow as tf
from tensorflow import keras
from keras.preprocessing import image
import numpy as np
import json

def load_model():
    # Load the model architecture and weights
    with open('Dense_classifier.json', 'r') as json_file:
        model_json = json_file.read()
        model = tf.keras.models.model_from_json(model_json)
    
    model.load_weights('Dense_classifier_weights.h5')
    return model

def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(299, 299))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  # Normalize the image
    return img_array

def classify(image_path):
    # Load the model
    model = load_model()
    
    # Preprocess the image
    img_array = preprocess_image(image_path)
    
    # Make predictions
    predictions = model.predict(img_array)
    return predictions

def set_background(predicted_class):
    # Add logic to set the background color based on the predicted class
    # You can customize this based on your design preferences
    if predicted_class == 'Normal':
        return '#aaffaa'  # Green for normal
    elif predicted_class == 'Viral Pneumonia':
        return '#aaaaff'  # Blue for viral pneumonia
    elif predicted_class == 'Bacterial Pneumonia':
        return '#ffaaaa'  # Red for bacterial pneumonia
    else:
        return '#ffffff'  # Default to white background
