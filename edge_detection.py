import cv2
import matplotlib.pyplot as plt

def canny_edge_detection(image_path):
    # Load image and convert to grayscale
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)