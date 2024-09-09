import pytesseract
import cv2

def apply_ocr(img):
    """
    Apply OCR to the preprocessed image and extract text.
    """
    # Convert image to text using pytesseract
    text = pytesseract.image_to_string(img)
    return text

def preprocess_and_ocr(image_path, preprocessing_pipeline):
    """
    Preprocess the image and then apply OCR.
    """
    # Load the image
    img = cv2.imread(image_path)

    # Apply preprocessing steps (from the configuration)
    for operation in preprocessing_pipeline:
        func = operation["function"]
        args = operation.get("args", {})
        img = func(img, **args) if args else func(img)

    # Apply OCR after preprocessing
    ocr_result = apply_ocr(img)
    return ocr_result
