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

# setting RGB color list:
color = ('blue', 'green', 'red')

# Iterating throuhg each channel and plotting the corresponding result:
    # cv.calcHist() params:
    # input_image
    # Number of channels to plot: RGB [0, 1, 2] Grayscale [0]
    # Mask: To plut full image => None
    # Count of Bins: Full image [256]
    # Range values: [0, 256]
for i,color in enumerate(color):
    histogram = cv.calcHist([input_image], [i], None, [256], [0, 256])
    cdf = histogram.cumsum()
    cdf_percent = cdf / cdf.max()
    plt.plot(cdf_percent, color=color, label=color+'_cdf')
    plt.xlim([0,256])

plt.title('Histogram Analysis',fontsize=20)
plt.xlabel('Range intensity values',fontsize=14)
plt.ylabel('Count of Pixels',fontsize=14)
plt.legend()
plt.show()