import cv2
import numpy as np

img = cv2.imread('image.jpg')  # Read RGB image

# Convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Convert to CMY manually
img_float = img.astype(float) / 255
cmy = 1 - img_float
cmy = (cmy * 255).astype(np.uint8)

cv2.imshow('Original', img)
cv2.imshow('HSV', hsv)
cv2.imshow('CMY', cmy)
cv2.waitKey(0)
cv2.destroyAllWindows()
