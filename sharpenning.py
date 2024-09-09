import cv2
import numpy as np

# Create a sharpening kernel
kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])

# Apply the sharpening kernel to the grayscale image
image = cv2.imread('C:\\Users\\Onestore\\PycharmProjects\\pythonProject\\Recept-III.png')
sharpened_image = cv2.filter2D(image, -1, kernel)

# Save the sharpened image
cv2.imwrite('sharpened_image.jpg', sharpened_image)

cv2.imshow('image.png',image)
cv2.imshow('sharpened_image.jpg',sharpened_image)

cv2.waitKey(0)
cv2.destroyAllWindows()