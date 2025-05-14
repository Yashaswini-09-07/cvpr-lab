import cv2
import numpy as np
from sklearn.decomposition import PCA

# Load image in grayscale
img = cv2.imread('image.jpg', 0)

# Apply PCA to reduce to 50 components
pca = PCA(n_components=50)
compressed = pca.fit_transform(img)
restored = pca.inverse_transform(compressed)

# Convert back to uint8
restored = np.uint8(restored)

# Show original and reconstructed images
cv2.imshow('Original', img)
cv2.imshow('PCA Restored', restored)
cv2.waitKey(0)
cv2.destroyAllWindows()
