import cv2
import numpy as np

img = cv2.imread('image.jpg', 0)  # Load as grayscale

# Image Negative
negative = 255 - img

# Log Transformation
c = 255 / np.log(1 + np.max(img))
log_transformed = c * np.log(1 + img.astype(np.float32))
log_transformed = np.uint8(log_transformed)

# Show results
cv2.imshow('Original', img)
cv2.imshow('Negative', negative)
cv2.imshow('Log Transform', log_transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()
