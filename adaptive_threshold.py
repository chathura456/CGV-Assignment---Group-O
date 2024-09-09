from PIL import Image, ImageOps
import numpy as np
import matplotlib.pyplot as plt


# Function to display an image
def display_image(image, title="Image"):
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()


# Function to rotate an image (transformation)
def transform_image(image, angle=30):
    return image.rotate(angle)


# Function to convert image to grayscale
def to_grayscale(image):
    return ImageOps.grayscale(image)


# Function to apply adaptive thresholding
def adaptive_threshold(image, block_size=11, C=2):
    image_array = np.array(image)  # Convert to numpy array
    mean_filtered = np.zeros_like(image_array)

    # Calculate mean value in local neighborhood (block size)
    for i in range(image_array.shape[0]):
        for j in range(image_array.shape[1]):
            i_min = max(i - block_size // 2, 0)
            i_max = min(i + block_size // 2 + 1, image_array.shape[0])
            j_min = max(j - block_size // 2, 0)
            j_max = min(j + block_size // 2 + 1, image_array.shape[1])

            local_region = image_array[i_min:i_max, j_min:j_max]
            mean_filtered[i, j] = np.mean(local_region)

    # Apply adaptive thresholding
    thresholded = (image_array > (mean_filtered - C)) * 255
    return Image.fromarray(thresholded.astype(np.uint8))


# Load images using PIL
image_names = ['Recept-I.jpg', 'Recept-II.jpg', 'Recept-III.jpg', 'Recept-IV.jpg', 'Recepts.jpg']
images = [Image.open(img_name) for img_name in image_names]

# Process each image
for i, img in enumerate(images):
    transformed = transform_image(img)  # Apply rotation
    grayscale = to_grayscale(transformed)  # Convert to grayscale
    thresholded = adaptive_threshold(grayscale)  # Apply adaptive threshold

    # Display original, transformed, and thresholded images
    display_image(grayscale, title=f"Grayscale Image {i + 1}")
    display_image(thresholded, title=f"Adaptive Threshold Image {i + 1}")
