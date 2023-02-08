import cv2
import matplotlib.pyplot as plt
import numpy as np
import argparse
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

path_saved_model = 'model_mobilenet.h5'
loaded_model = load_model(path_saved_model);

parser = argparse.ArgumentParser()
parser.add_argument('--d', type=str, required=True)

args = parser.parse_args()

img_path = args.d

img = image.load_img(img_path, target_size=(224, 224));
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)

classes = loaded_model.predict(img_array/255);

for i, class_ in enumerate(classes[0]):
    if class_ == classes[0].max():
        if i == 0:
            print("bakso")
        elif i == 1:
            print("gudeg")
        elif i == 2:
            print("gado")
        elif i == 3:
            print("rendang")
        else:
            print("sate")