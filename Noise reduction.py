import cv2

# Apply Gaussian blur to remove noise
image = cv2.imread('img/Recept-I.png')

noise_removed_image = cv2.GaussianBlur(image, (5, 5), 0)

cv2.imshow('image.png',image)
cv2.imshow('noise_removed_image.jpg',noise_removed_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
