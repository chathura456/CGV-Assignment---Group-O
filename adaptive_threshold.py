import cv2
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\viraj\Downloads\CGV Group Assignment'

def preprocess_image(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Transform the image: Resize to standard dimensions for better processing
    scale_percent = 150  # Example scale percentage
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grayscale Image', gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return gray

def preprocess_image(image_path):
    # (Code from the first commit remains the same)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grayscale Image', gray)

    # Apply Adaptive Thresholding
    adaptive_thresh = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2
    )
    cv2.imshow('Adaptive Threshold Image', adaptive_thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return adaptive_thresh

def preprocess_image(image_path):
    # (Code from the first two commits remains the same)

    # Apply Adaptive Thresholding
    adaptive_thresh = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2
    )
    cv2.imshow('Adaptive Threshold Image', adaptive_thresh)

    # Optional: Denoise or blur the image if needed
    blurred = cv2.GaussianBlur(adaptive_thresh, (5, 5), 0)
    cv2.imshow('Blurred Image', blurred)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return blurred

def extract_text(image):
    # OCR the image using Tesseract
    text = pytesseract.image_to_string(image)
    return text


def summarize_receipt(text):
    # Example of basic parsing logic (can be expanded)
    lines = text.split("\n")
    items = []
    subtotal = 0
    for line in lines:
        if line.startswith("#"):  # Item line starts with #
            item_data = line.split("\t")  # Example: item name, quantity, price
            items.append(item_data)
        if "Sub Total" in line:
            subtotal = float(line.split()[-1])

    summary = {
        "items": items,
        "subtotal": subtotal,
    }
    return summary

def main(image_path):
    # Process the image
    processed_image = preprocess_image(image_path)

    # Extract text
    text = extract_text(processed_image)
    print("Extracted Text:\n", text)

    # Summarize the receipt
    summary = summarize_receipt(text)
    print("\nReceipt Summary:")
    print("Subtotal:", summary['subtotal'])

if _name_ == "_main_":
    image_path = 'Recept-I.png'
    main(image_path)