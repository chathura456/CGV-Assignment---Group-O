import cv2
import numpy as np

def grayscale_image(img):
    """Convert image to grayscale."""
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def binarize_image(img, threshold=128):
    """Apply binary thresholding."""
    _, binary = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    return binary

def remove_noise(img):
    """Apply Gaussian blur to reduce noise."""
    return cv2.GaussianBlur(img, (5, 5), 0)

def edge_detection(img):
    """Perform edge detection using the Canny algorithm."""
    return cv2.Canny(img, 100, 200)

def sharpen_image(img):
    """Sharpen the image using a kernel."""
    kernel = np.array([[0, -1, 0],
                       [-1, 5,-1],
                       [0, -1, 0]])
    return cv2.filter2D(img, -1, kernel)

def morphological_operation(img):
    """Apply a morphological operation (dilation)."""
    kernel = np.ones((5, 5), np.uint8)
    return cv2.dilate(img, kernel, iterations=1)

