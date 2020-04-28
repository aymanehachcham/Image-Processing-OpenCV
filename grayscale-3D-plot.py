from __future__ import print_function
from __future__ import division
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cv2 as cv
import numpy as np


src = 'head-sculpture.jpg'
input_image = cv.imread(src)
if input_image is None:
    print('Could not open image: ', input_image)
    exit(0)

# Grayscale image:
gray = cv.cvtColor(input_image, cv.COLOR_BGR2GRAY)

# Resize the image:
scale_percent = 80 # Percent of the original image
width = int(gray.shape[0] * scale_percent / 100)
height = int(gray.shape[1] * scale_percent / 100)
dim = (width, height)

resized_img = cv.resize(gray, dim, interpolation=cv.INTER_AREA)

print(resized_img.shape)

cv.imshow('Grayscale', resized_img)
cv.waitKey(0)
cv.destroyAllWindows()

# Generate a meshgrid and plot the pixel values at z axis
xx, yy = np.mgrid[0:resized_img.shape[0], 0:resized_img.shape[1]]
fig = plt.figure(figsize=(15,15))
ax = fig.gca(projection='3d')
ax.plot_surface(xx, yy, resized_img ,rstride=1, cstride=1, cmap=plt.cm.gray,linewidth=2)
ax.view_init(80, 30)

plt.show()
