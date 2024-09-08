import os
import cv2


def list_images(directory):
    # List image files in the given directory with supported extensions
    supported_extensions = ['png', 'jpg', 'jpeg', 'bmp']
    images = [f for f in os.listdir(directory) if any(f.endswith(ext) for ext in supported_extensions)]

    if not images:
        print("No images found in the directory.")
        return None
    return images


def select_image(images):
    # Prompt the user to select an image
    while True:
        try:
            choice = int(input("Select an image by entering the number: ")) - 1
            if 0 <= choice < len(images):
                return images[choice]
            else:
                print("Invalid selection. Try again.")
        except ValueError:
            print("Please enter a valid number.")


def show_image(image_path):
    # Load and display the selected image
    img = cv2.imread(image_path)
    if img is None:
        print("Error loading image.")
        return
    cv2.imshow("Selected Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Specify the image directory
    image_directory = "./img"

    # List available images
    images = list_images(image_directory)
    if images is None:
        exit(1)

    # Show the image names in the terminal
    for i, img in enumerate(images):
        print(f"{i + 1}. {img}")

    # Let the user select an image
    selected_image = select_image(images)

    # Show the selected image
    show_image(os.path.join(image_directory, selected_image))
