from __future__ import print_function
from builtins import input
import cv2 as cv
import numpy as np
import argparse

# Get the input image:

class PixelTransforms:

    @ staticmethod
    def get_image(image_path :str):
        """
        Take the path for the input image and output a cv Mat oject to manipulate

        :param image_path: image path in the file system
        :return Mat object: a specific opencv Mat object to manipulate the image
        """
        input_image = cv.imread(image_path)
        if input_image is None:
            print('Could not open image: ', input_image)
            exit(0)
            
        return input_image


    @staticmethod
    def contrast_adjustment(alpha :float, beta :int, input_image :object):
        """
        create image contrast playing with brightness values

        :param alpha: Alpha channel for brightness range of inputs [1.0 - 3.0]
        :param beta: value for image contrast range of inputs [0 - 100]
        """
        # Create a dummy image:
        new_image = np.zeros(input_image.shape, input_image.dtype)

        # Access the pixels inside the image:
        for y in range(input_image.shape[0]):
            for x in range(input_image.shape[1]):
                for c in range(input_image.shape[2]):
                    new_image[y, x, c] = np.clip(alpha * input_image[y, x, c] + beta, 0, 255)

        cv.imshow('Original Image', input_image)
        cv.imshow('New Image', new_image)
        cv.waitKey()

