import tensorflow as tf
from tensorflow import keras
from keras.preprocessing import image
import numpy as np
import json

def load_model():
    with open('Dense_classifier.json', 'r') as json_file:
        model_json = json_file.read()
        model = tf.keras.models.model_from_json(model_json)
    
    model.load_weights('Dense_classifier_weights.h5')
    return model

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
