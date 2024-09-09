import os
import cv2


def list_images(directory="./img"):
    """List all image files in the directory ./img."""
    supported_extensions = ['png', 'jpg', 'jpeg', 'bmp']
    images = [f for f in os.listdir(directory) if any(f.endswith(ext) for ext in supported_extensions)]

    if not images:
        print("No images found in the directory.")
        return None
    return images


def select_image(images):
    """Prompt the user to select an image by its number."""
    while True:
        try:
            choice = int(input("Select an image by entering the number: ")) - 1
            if 0 <= choice < len(images):
                return images[choice]
            else:
                print("Invalid selection. Try again.")
        except ValueError:
            print("Please enter a valid number.")


def process_images():
    """Process user input to list, select, and display images."""
    images = list_images()
    if images is None:
        return None

    for i, img in enumerate(images):
        print(f"{i + 1}. {img}")

    selected_image = select_image(images)
    selected_image_path = os.path.join("./img", selected_image)
    return selected_image_path
