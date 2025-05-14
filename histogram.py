#HISTOGRAM CALCULATION AND EQUALIZATION 
import cv2
import matplotlib.pyplot as plt

# Load image in grayscale
img = cv2.imread('image.jpg', 0)

# Histogram equalization
equalized = cv2.equalizeHist(img)

# Calculate histograms
hist_original = cv2.calcHist([img], [0], None, [256], [0, 256])
hist_equalized = cv2.calcHist([equalized], [0], None, [256], [0, 256])

# Show images
cv2.imshow('Original', img)
cv2.imshow('Equalized', equalized)

# Show histograms
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(hist_original)
plt.title('Original Histogram')

plt.subplot(1, 2, 2)
plt.plot(hist_equalized)
plt.title('Equalized Histogram')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
