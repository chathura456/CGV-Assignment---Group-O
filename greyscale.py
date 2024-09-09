import cv2

# Load the image
image = cv2.imread('C:\\Users\\Onestore\\PycharmProjects\\pythonProject\\Recept-I.png')

# Convert to grayscale
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Save the grayscale image
cv2.imwrite('grayscale_image.jpg', grayscale_image)

cv2.imshow('image.png',image)
cv2.imshow('grayscale_image.jpg',grayscale_image)

cv2.waitKey(0)
cv2.destroyAllWindows()