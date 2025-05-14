import cv2
import numpy as np

# Read image and reshape
img = cv2.imread('image.jpg')
Z = img.reshape((-1, 3))
Z = np.float32(Z)

# Define criteria and apply k-means
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 3  # Number of segments
_, labels, centers = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Convert back to image
centers = np.uint8(centers)
segmented = centers[labels.flatten()].reshape(img.shape)

cv2.imshow('Segmented Image', segmented)
cv2.waitKey(0)
cv2.destroyAllWindows()
 