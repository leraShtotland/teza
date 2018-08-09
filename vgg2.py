

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16

import os
os.environ["THEANO_FLAGS"] = "mode=FAST_RUN,device=gpu,floatX=float32"
# import necessary modules
import time
import matplotlib.pyplot as plt
import numpy as np
#% matplotlib inline
np.random.seed(2017)
from keras.applications.vgg19 import VGG19
from keras.applications.vgg19 import preprocess_input, decode_predictions
from keras.preprocessing import image
from keras.models import Model
import cv2


poster_path = "C:\\Users\\lerasht\\Desktop\\posters0503_1\\"
total_movies = 500
from keras.applications import VGG16
from keras.applications.vgg16 import preprocess_input
from keras.preprocessing import image as kimage

image = [0]*total_movies
x = [0]*total_movies

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(poster_path) if isfile(join(poster_path, f))]
list=list(onlyfiles)

#base_model = VGG16(include_top=False, weights='imagenet')

base_model = VGG16()
#base_model = VGG19(weights='imagenet')
# pre-process the image
# img = image.load_img('cat.jpg', target_size=(224, 224))
# img = image.img_to_array(img)
# img = np.expand_dims(img, axis=0)
# img = preprocess_input(img)

# define model from base model for feature extraction from fc2 layer
model = Model(input=base_model.input, output=base_model.get_layer('fc2').output)
# obtain the outpur of fc2 layer
dic = {} #dictionary

download_dir = "FeaturesCsv_0603_1.csv" #where you want the file to be downloaded to

csv = open(download_dir, "w")
#"w" indicates that you're writing strings to the file

columnTitleRow = "number, features\n"
csv.write(columnTitleRow)
i=0
#for i in range(total_movies):
for file in list:
    #image[i] = kimage.load_img(poster_path + str(i) + ".jpg", target_size=(224, 224))
    image[i] = kimage.load_img(poster_path+file, target_size=(224, 224))
    x[i] = kimage.img_to_array(image[i])
    x[i] = np.expand_dims(x[i], axis=0)
    x[i] = preprocess_input(x[i])
    fc2_features = model.predict(x[i])
    #print(list(fc2_features))
    #print(len(list(fc2_features)[0]))
    #print ("Feature vector dimensions: ",fc2_features.shape)
    dic[file]=fc2_features
    #dic[i]=fc2_features
    #print ("Feature vector dimensions: ",fc2_features.shape)


for key in dic.keys():
    s = ""
    name = key
    email = dic[key]
    for index in dic[key][0]:
        s=s+","+str(index)
    row = str(name) + s + "\n"
    csv.write(row)



# # load the model
# model = VGG16()
# # load an image from file
# image = load_img('cat.jpg', target_size=(224, 224))
# # convert the image pixels to a numpy array
# image = img_to_array(image)
# # reshape data for the model
# image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
# # prepare the image for the VGG model
# image = preprocess_input(image)
# # predict the probability across all output classes
# yhat = model.predict(image)
# print(len(yhat))
# # convert the probabilities to class labels
# label = decode_predictions(yhat)
# # retrieve the most likely result, e.g. highest probability
# label = label[0][0]
# # print the classification
# print("result")
# print('%s (%.2f%%)' % (label[1], label[2]*100))
