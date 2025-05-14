#morphological operations 
 import cv2   
import numpy as np
img = cv2.imread('image.jpg', 0)  # Load in grayscale
kernel = np.ones((5,5), np.uint8)

dilation = cv2.dilate(img, kernel, iterations=1)
erosion = cv2.erode(img, kernel, iterations=1)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imshow('Original', img)
cv2.imshow('Dilation', dilation)
cv2.imshow('Erosion', erosion)
cv2.imshow('Opening', opening)
cv2.imshow('Closing', closing)
cv2.waitKey(0)
cv2.destroyAllWindows()