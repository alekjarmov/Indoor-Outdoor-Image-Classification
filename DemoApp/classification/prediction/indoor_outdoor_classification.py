import os
import cv2
from keras.applications import ResNet50V2
from keras.layers import Dense, Flatten, Dropout
from keras_cv.layers.preprocessing import RandomSaturation
from keras.models import Sequential
import pandas as pd
from keras.utils import image_dataset_from_directory
import tensorflow as tf
import keras
import numpy as np
import os 
import tensorflow_hub as hub

def predict_image(model_number, path, size_x: int = 224, size_y: int = 224):
    print(os. getcwd())
    img = cv2.imread(path[1:])
    print(img)
    img = cv2.resize(img, (size_x, size_y))
    img = np.expand_dims(img, axis=0)
    model = keras.models.load_model(f'classification/prediction/models/model{model_number}.h5')
    return model.predict(img, verbose=False)[0]