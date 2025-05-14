import cv2
import numpy as np

img = cv2.imread('image.jpg')  # Load image

# Image Negative
negative = 255 - img

# Gamma Correction
gamma = 2.2  # Change this value as needed
gamma_corrected = np.array(255 * (img / 255) ** (1 / gamma), dtype='uint8')

# Show results
cv2.imshow('Original', img)
cv2.imshow('Negative', negative)
cv2.imshow('Gamma Corrected', gamma_corrected)
cv2.waitKey(0)
cv2.destroyAllWindows()
