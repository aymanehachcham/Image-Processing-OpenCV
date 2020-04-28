from __future__ import print_function
from __future__ import division
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np


src = 'cartoon.jpg'
input_image = cv.imread(src)
if input_image is None:
    print('Could not open image: ', input_image)
    exit(0)

# Grayscale image:
gray = cv.cvtColor(input_image, cv.COLOR_BGR2GRAY)

# Displaying image:
cv.imshow('Original Image', input_image)
cv.imshow('Grayscale Image', gray)

cv.waitKey(0)
cv.destroyAllWindows()