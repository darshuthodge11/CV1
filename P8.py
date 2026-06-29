import cv2
import numpy as np
# Load the grayscale image
gray_image = cv2.imread("C:/Users/Darshana/OneDrive/Desktop/MSCIT SEM 2/MSC IT SEM 2 COMPUTER VISION/grayimg.jpeg", cv2.IMREAD_GRAYSCALE)
# Convert grayscale image to BGR (3-channel) for colorization
color_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)
# Define a basic colorization lookup table
color_lookup_table = np.zeros((256, 1, 3), dtype=np.uint8)
for i in range(256):
    color_lookup_table[i, 0, 0] = i  # Blue channel
    color_lookup_table[i, 0, 1] = 127  # Green channel
    color_lookup_table[i, 0, 2] = 255 - i  # Red channel
# Apply the colorization lookup table to the grayscale image
colorized_image = cv2.LUT(color_image, color_lookup_table)
# Display the original grayscale image and the colorized image
cv2.imshow('Grayscale Image', gray_image)
cv2.imshow('Colorized Image', colorized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

