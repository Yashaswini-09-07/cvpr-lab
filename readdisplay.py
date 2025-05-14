import cv2
image=cv2.imread("flower.jpg")
cv2.imshow('My image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()