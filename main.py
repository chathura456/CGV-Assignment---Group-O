from load_image import process_images
from custom_preprocessing import apply_preprocessing
from ocr_methods import apply_ocr
import cv2

if __name__ == "__main__":
    # Get the selected image path
    selected_image_path = process_images()

    if selected_image_path:
        # Load the image for preprocessing
        img = cv2.imread(selected_image_path)

        # Apply custom preprocessing based on image-specific configuration
        apply_preprocessing(selected_image_path, img)

        # After preprocessing, apply OCR to the processed image
        ocr_text = apply_ocr(img)

        # Print the extracted OCR text
        print("Extracted Text:")
        print(ocr_text)

