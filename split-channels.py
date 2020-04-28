from __future__ import print_function
from __future__ import division
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
import argparse

src = 'cartoon.jpg'
input_image = cv.imread(src)
if input_image is None:
    print('Could not load image: ', input_image)
    exit(0)

# Splitting image into RGB channels:
blue, green, red = cv.split(input_image)

print(blue.shape)

# We create a dummy 3D array
blue_channel = np.zeros(input_image.shape, input_image.dtype)
green_channel = np.zeros(input_image.shape, input_image.dtype)
red_channel = np.zeros(input_image.shape, input_image.dtype)

# We match each color channel to a 3D dimension:
    # Blue Rendering : [blue; 0; 0]
    # Green Rendering: [0; green; 0]
    # Red Rendering: [0; 0; red]
cv.mixChannels([blue, green, red], [blue_channel], [0,0])
cv.mixChannels([blue, green, red], [green_channel], [1,1])
cv.mixChannels([blue, green, red], [red_channel], [2,2])


cv.imshow('Blue Channel', blue_channel)
cv.imshow('Green Channel', green_channel)
cv.imshow('Red Channel', red_channel)

cv.waitKey(0)
cv.destroyAllWindows()
