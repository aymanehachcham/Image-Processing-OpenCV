from __future__ import print_function
from __future__ import division
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

src = 'cartoon.jpg'
input_image = cv.imread(src)
if input_image is None:
    print('Could not load image: ', input_image)
    exit(0)


# Applying Laplacian transformation:
laplacian = cv.Laplacian(input_image, cv.CV_8UC3)


cv.imshow('Original Image', input_image)
cv.imshow('Laplacian Filter', laplacian)
cv.waitKey(0)
cv.destroyAllWindows()