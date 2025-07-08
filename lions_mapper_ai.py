import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color
from skimage.measure import regionprops, label

function getColorKMeans(img_src,color_rgb):
  image = cv2.imread(str(img))
  hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
  lower_green = np.array([40, 40, 40]) # Adjust values as needed
  upper_green = np.array(color_rgb)
  green_mask = cv2.inRange(hsv_image, lower_green, upper_green)
  green_detected = cv2.bitwise_and(image, image, mask=green_mask)
  cv2.imshow('Original Image', image)
  cv2.imshow('Green Mask', green_mask)
  cv2.imshow('Green Detected', green_detected)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

function getSpinRoute(img_src,_color_rgb):
  image = io.imread('your_image.jpg')
  image_hsv = color.rgb2hsv(image)
  lower_green = np.array(color_rgb)
  upper_green = np.array(color_rgb)
  green_mask = (image_hsv[:, :, 0] >= lower_green[0]) & (image_hsv[:, :, 0] <=     upper_green[0]) & \ (image_hsv[:, :, 1] >= lower_green[1]) & (image_hsv[:, :, 1] <= upper_green[1]) & \ (image_hsv[:, :, 2] >= lower_green[2]) & (image_hsv[:, :, 2] <= upper_green[2])
  labeled_mask = label(green_mask)
  regions = regionprops(labeled_mask)
  if regions:
    green_region = regions[0]
    min_row, min_col, max_row, max_col = green_region.bbox
    print(f"Initial green point: (x={min_col}, y={min_row})")
    print(f"End green point: (x={max_col}, y={max_row})")
    plt.imshow(image)
    plt.plot([min_col, max_col], [min_row, max_row], color='red', linewidth=2)
    plt.title("RGB Area Detected")
    plt.show()
  else:
    print("No RGB Area detected.")

img_src = sys.argv[1]
color_src = sys.argv[2]
getSpinRoute(img_src,color_rgb)