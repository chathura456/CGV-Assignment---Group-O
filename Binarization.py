import cv2

image = cv2.imread('img/Recept-I.png')
# Apply binarization using a threshold

grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
binary_image = cv2.threshold(grayscale_image, 128, 255, cv2.THRESH_BINARY)

cv2.imshow('image.png',image)
cv2.imshow('binary_image.jpg',binary_image)

cv2.waitKey(0)
cv2.destroyAllWindows()