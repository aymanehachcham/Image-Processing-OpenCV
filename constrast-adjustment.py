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

# New dummy image that will contain the adjustments
adjusted_image = np.zeros(input_image.shape, input_image.dtype)

# Defining alpha and beta:
alpha = 3.0   # Contrast Control [1.0-3.0]
beta = 100    # Brightness Control [0-100]

# Scaling and converting the image contrast and brightness
adjusted_image = cv.convertScaleAbs(input_image, alpha=alpha, beta=beta)

cv.imshow('Resulting Image', adjusted_image)

cv.waitKey(0)
cv.destroyAllWindows()