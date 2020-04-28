from __future__ import print_function
from __future__ import division
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import cv2 as cv
import numpy as np

src = 'cartoon.jpg'
input_image = cv.imread(src)
if input_image is None:
    print('Could not load image: ', input_image)
    exit(0)

# Calculate the Cumulative Distribution Function:
blue, green, red = cv.split(input_image)

hist_blue = cv.calcHist([blue], [0], None, [256], [0, 256])
hist_green = cv.calcHist([green], [0], None, [256], [0, 256])
hist_red = cv.calcHist([red], [0], None, [256], [0, 256])

# Calculate the CDF for each histogram channel
cdf_blue = hist_blue.cumsum()
cdf_green = hist_green.cumsum()
cdf_red = hist_red.cumsum()

# Mask null values 
cdf_blue_masked = np.ma.masked_equal(cdf_blue, 0)
cdf_green_masked = np.ma.masked_equal(cdf_green, 0)
cdf_red_masked = np.ma.masked_equal(cdf_red, 0)

# Apply Equalization Formula to all none masked values: (y - ymin)*255 / (ymax - ymin)
cdf_blue_masked = (cdf_blue_masked - cdf_blue_masked.min())*255 / (cdf_blue_masked.max() - cdf_blue_masked.min())
cdf_green_masked = (cdf_green_masked - cdf_green_masked.min())*255 / (cdf_green_masked.max() - cdf_green_masked.min())
cdf_red_masked = (cdf_red_masked - cdf_red_masked.min())*255 / (cdf_red_masked.max() - cdf_red_masked.min())

cdf_final_b = np.ma.filled(cdf_blue_masked, 0).astype('uint8')
cdf_final_g = np.ma.filled(cdf_green_masked, 0).astype('uint8')
cdf_final_r = np.ma.filled(cdf_red_masked, 0).astype('uint8')

# Merge all channels:
blue_img = cdf_final_b[blue]
green_img = cdf_final_g[green]
red_img = cdf_final_r[red]

final_equ_img = cv.merge((blue_img, green_img, red_img))

color = ('blue', 'green', 'red')

# Plot of the Histogram for the Newly Equalized Image
for i,color in enumerate(color):
    histogram = cv.calcHist([final_equ_img], [i], None, [256], [0, 256])
    plt.plot(histogram, color=color, label=color+'_channel')
    plt.xlim([0,256])

plt.title('Histogram for EQ Image',fontsize=20)
plt.xlabel('Range intensity values',fontsize=14)
plt.ylabel('Count of Pixels',fontsize=14)
plt.legend()
plt.show()

# Plot of the CDF Analysis for the Newly Equalized Image
for i,color in enumerate(color):
    histogram = cv.calcHist([final_equ_img], [i], None, [256], [0, 256])
    cdf = histogram.cumsum()
    cdf_percent = cdf / cdf.max()
    plt.plot(histogram, color=color, label=color+'_cdf')
    plt.xlim([0,256])

plt.title('CDF for EQ Image',fontsize=20)
plt.xlabel('Range intensity values',fontsize=14)
plt.ylabel('Percentage of Pixels',fontsize=14)
plt.legend()
plt.show()

# Write/Output new equalized image:
cv.imshow('Original Image', input_image)
cv.imshow('New Equalized Image', final_equ_img)
cv.waitKey(0)
cv.destroyAllWindows()