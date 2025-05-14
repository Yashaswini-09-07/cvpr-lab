import cv2
import numpy as np

# 1. Load the image
image = cv2.imread('rabbit.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 2. Apply Canny edge detection
edges = cv2.Canny(gray, 50, 150, apertureSize=3)  # Adjust thresholds as needed

# 3. Perform Hough Transform
lines = cv2.HoughLines(edges, 1, np.pi / 180, threshold=150)  # Adjust threshold as needed

# 4. Draw lines on the image
if lines is not None:
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 2)  # Adjust line color and thickness

# 5. Display the result
cv2.imshow('Original Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()