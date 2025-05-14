import cv2
import numpy as np

img = cv2.imread('image.jpg', 0)  # Load grayscale image

# Sobel
sobel = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)

# Prewitt (manual kernel)
kernelx = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
kernely = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
prewitt = cv2.filter2D(img, -1, kernelx) + cv2.filter2D(img, -1, kernely)

# Laplacian
laplacian = cv2.Laplacian(img, cv2.CV_64F)

# Show results
cv2.imshow('Sobel', sobel)
cv2.imshow('Prewitt', prewitt)
cv2.imshow('Laplacian', laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()
