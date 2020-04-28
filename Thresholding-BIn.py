from __future__ import print_function
from __future__ import division
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cv2 as cv
import numpy as np


src = 'greek.jpg'
input_image = cv.imread(src)
if input_image is None:
    print('Could not open image: ', input_image)
    exit(0)

# Resize the image:
scale_percent = 100 # Percent of the original image
width = int(input_image.shape[0] * scale_percent / 100)
height = int(input_image.shape[1] * scale_percent / 100)
dim = (width, height)

resized_img = cv.resize(input_image, dim, interpolation=cv.INTER_AREA)

# Grayscale image:
gray = cv.cvtColor(input_image, cv.COLOR_BGR2GRAY)

# Thresholding image to render it in black and white:
(thresh, blackAndWhiteImage) = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

# Displaying image:
cv.imshow('Original Image', input_image)
cv.imshow('Grayscale Image', gray)
cv.imshow('Binary Image', blackAndWhiteImage)

cv.waitKey(0)
cv.destroyAllWindows()