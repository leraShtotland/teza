import os
import scipy
import numpy as np
import scipy.misc
import numpy as np
from time import gmtime, strftime
from six.moves import xrange

import tensorflow as tf
import tensorflow.contrib.slim as slim
from scipy.misc import imresize, imsave

def get_image(image_path, input_height, input_width,
              resize_height=64, resize_width=64,
              crop=True, grayscale=False):
  #print(image_path)
  image = imread(image_path, grayscale)
  #img=scipy.misc.imresize(image, (64,64))

  im=transform(image, input_height, input_width,
                   resize_height, resize_width, crop)
  return im

def transform(image, input_height, input_width,
              resize_height=64, resize_width=64, crop=True):
  if crop:
    cropped_image = center_crop(
      image, input_height, input_width,
      resize_height, resize_width)
  else:
    cropped_image = scipy.misc.imresize(image, [resize_height, resize_width])
  return np.array(cropped_image)/127.5 - 1.


def imread(path, grayscale = False):
  if (grayscale):
    return scipy.misc.imread(path, flatten = True).astype(np.float)
  else:
    return scipy.misc.imread(path).astype(np.float)

list_data=[]

def center_crop(x, crop_h, crop_w,
                resize_h=64, resize_w=64):
  if crop_w is None:
    crop_w = crop_h
  h, w = x.shape[:2]
  j = int(round((h - crop_h)/2.))
  i = int(round((w - crop_w)/2.))
  return scipy.misc.imresize(
      x[j:j+crop_h, i:i+crop_w], [resize_h, resize_w])


for item in range(1, 43585):
    image_path = os.path.join("C:\\Users\\lerasht\\Desktop\\posters_0908", str(item) + ".jpg")
    list_data.append(image_path)

counter=0
for item in list_data:
    image=get_image(item,96,64)
    if (image.shape==(64,64)):
        print(item)
    if (counter%1000==0):
        print(counter)
    counter+=1