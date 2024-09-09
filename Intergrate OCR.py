import cv2
import pytesseract

image1_path = 'Recept-I.png'
image2_path = 'Recept-II.png'
image3_path = 'Recept-III.png'
image4_path = 'Recept-IV.png'
image5_path = 'Recepts.png'

image1 = cv2.imread(image1_path)
image2 = cv2.imread(image2_path)
image3 = cv2.imread(image3_path)
image4 = cv2.imread(image4_path)
image5 = cv2.imread(image5_path)

gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
gray_image3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)
gray_image4 = cv2.cvtColor(image4, cv2.COLOR_BGR2GRAY)
gray_image5 = cv2.cvtColor(image5, cv2.COLOR_BGR2GRAY)

blurred_image1 = cv2.GaussianBlur(gray_image1, (5, 5), 0)
_, binary_image1 = cv2.threshold(blurred_image1, 150, 255, cv2.THRESH_BINARY)
blurred_image2 = cv2.GaussianBlur(gray_image2, (5, 5), 0)
_, binary_image2 = cv2.threshold(blurred_image2, 150, 255, cv2.THRESH_BINARY)
blurred_image3 = cv2.GaussianBlur(gray_image3, (5, 5), 0)
_, binary_image3 = cv2.threshold(blurred_image3, 150, 255, cv2.THRESH_BINARY)
blurred_image4 = cv2.GaussianBlur(gray_image4, (5, 5), 0)
_, binary_image4 = cv2.threshold(blurred_image4, 150, 255, cv2.THRESH_BINARY)
blurred_image5 = cv2.GaussianBlur(gray_image5, (5, 5), 0)
_, binary_image5 = cv2.threshold(blurred_image5, 150, 255, cv2.THRESH_BINARY)

text1 = pytesseract.image_to_string(binary_image1)
text2 = pytesseract.image_to_string(binary_image2)
text3 = pytesseract.image_to_string(binary_image3)
text4 = pytesseract.image_to_string(binary_image4)
text5 = pytesseract.image_to_string(binary_image5)

print("Extracted Text: \n\n", text1)
print("Extracted Text: \n\n", text2)
print("Extracted Text: \n\n", text3)
print("Extracted Text: \n\n", text4)
print("Extracted Text: \n\n", text5)

cv2.imshow('Processed Image', binary_image1)
cv2.imshow('Processed Image', binary_image2)
cv2.imshow('Processed Image', binary_image3)
cv2.imshow('Processed Image', binary_image4)
cv2.imshow('Processed Image', binary_image5)


cv2.waitKey(0)
cv2.destroyAllWindows()