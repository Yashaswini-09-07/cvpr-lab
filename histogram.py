#HISTOGRAM CALCULATION AND EQUALIZATION 
import cv2
# Read the image in grayscale
img = cv2.imread('image.jpg', 0)

# Histogram equalization
equalized = cv2.equalizeHist(img)

# Show original and equalized images
cv2.imshow('Original', img)
cv2.imshow('Equalized', equalized)
cv2.waitKey(0)
cv2.destroyAllWindows()