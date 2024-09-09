import cv2
import numpy as np

def grayscale_image(img):
    # Convert to grayscale
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def binarize_image(img, threshold=128):
    # Apply binary thresholding
    return cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)[1]

def adaptive_threshold(img, method=cv2.ADAPTIVE_THRESH_MEAN_C, block_size=11, C=2):
    # Adaptive thresholding
    return cv2.adaptiveThreshold(img, 255, method, cv2.THRESH_BINARY, block_size, C)

def histogram_equalization(img):
    # Apply histogram equalization for grayscale or color images
    if len(img.shape) == 2:  # Grayscale
        return cv2.equalizeHist(img)
    else:  # Color (apply to each channel)
        ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
        ycrcb[:, :, 0] = cv2.equalizeHist(ycrcb[:, :, 0])
        return cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)

def remove_noise(img, ksize=(5, 5)):
    # Gaussian blur for noise reduction
    return cv2.GaussianBlur(img, ksize, 0)

def edge_detection(img, low_threshold=100, high_threshold=200):
    # Edge detection with Canny
    return cv2.Canny(img, low_threshold, high_threshold)

def sharpen_image(img):
    # Sharpening with a kernel
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    return cv2.filter2D(img, -1, kernel)

def morphological_operation(img, operation='dilate', ksize=(5, 5), iterations=1):
    # Apply morphological operations (dilate/erode)
    kernel = np.ones(ksize, np.uint8)
    if operation == 'dilate':
        return cv2.dilate(img, kernel, iterations=iterations)
    elif operation == 'erode':
        return cv2.erode(img, kernel, iterations=iterations)
    else:
        raise ValueError("Invalid operation. Choose 'dilate' or 'erode'.")
