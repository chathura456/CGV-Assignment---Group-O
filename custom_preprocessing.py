import os
import cv2
import numpy as np
from preprocess_image import grayscale_image, binarize_image, remove_noise, edge_detection, sharpen_image, \
    morphological_operation

# Define the operations to apply based on the image
PREPROCESSING_CONFIG = {
    "Recept-I.png": {
        "operations": [
            {"name": "grayscale", "function": grayscale_image},
            {"name": "binarization", "function": binarize_image, "args": {"threshold": 100}},
        ]
    },
    "Recept-II.png": {
        "operations": [
            {"name": "grayscale", "function": grayscale_image},
            {"name": "edge detection", "function": edge_detection}
        ]
    }
    # Add more image-specific configurations as needed
}


def apply_preprocessing(selected_image_path, img):
    """Apply custom preprocessing based on the selected image's config."""
    # Extract the image name from the full path
    image_name = os.path.basename(selected_image_path)

    # Look for custom preprocessing configuration for the selected image
    config = PREPROCESSING_CONFIG.get(image_name)

    if config is None:
        print(f"No custom preprocessing found for {image_name}")
        return

    # Display the original image
    processed_images = [("Original", img)]

    # Apply each operation defined in the config
    for operation in config["operations"]:
        func = operation["function"]
        args = operation.get("args", {})
        processed_img = func(img, **args) if args else func(img)
        processed_images.append((operation["name"], processed_img))

    # Show the original and processed images side by side
    show_processed_images(processed_images)


def show_processed_images(images):
    """Display the original and processed images in full screen with labels."""
    labeled_images = []

    # Ensure all images have the same number of dimensions and add labels
    for label, img in images:
        if len(img.shape) == 2:  # If the image is grayscale (2D), convert to 3-channel
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

        # Add label to the image
        cv2.putText(img, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

        # Resize the image for uniform display
        labeled_images.append(cv2.resize(img, (400, 400)))

    # Concatenate images horizontally for side-by-side display
    concatenated_image = np.hstack(labeled_images)

    # Create a full-screen window to display the images
    cv2.namedWindow("Processed Images", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Processed Images", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    # Display the concatenated image
    cv2.imshow("Processed Images", concatenated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
