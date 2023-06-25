import cv2
import numpy as np

def print_object_info(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Thresholding
    _, thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)

    # Dilation
    kernel = np.ones((2, 2), np.uint8)
    dilation = cv2.dilate(thresh, kernel, iterations=2)

    # Find contours
    contours, _ = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Count objects
    objects = len(contours)
    print("Number of objects:", objects)

    # Calculate total area
    total_area = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        total_area += area

    print("Total Area:", total_area)

# Example usage
image_path = 'c.jpeg'
print_object_info(image_path)
