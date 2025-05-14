import cv2

img = cv2.imread('image.jpg')  # Load image
blur = cv2.GaussianBlur(img, (5, 5), 0)  # Apply Gaussian blur

cv2.imshow('Original', img)
cv2.imshow('Smoothed', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
#median filter
import cv2

img = cv2.imread('image.jpg')  # Load image
median = cv2.medianBlur(img, 5)  # Apply Median filter

cv2.imshow('Original', img)
cv2.imshow('Median Filtered', median)
cv2.waitKey(0)
cv2.destroyAllWindows()
