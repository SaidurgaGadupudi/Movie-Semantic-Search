import os
import cv2

# Path to the directory containing the input images
img_dir = '/Users/navyaravuri/Documents/MSS/data/'

# Loop over all the files in the directory
for filename in os.listdir(img_dir):
    # Loads the image
    img_path = os.path.join(img_dir, filename)
    img = cv2.imread(img_path)

    # Converts the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Applies Gaussian blur to reduce noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Applies thresholding to segment the image
    ret, thresholded = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    # Finds the contours in the thresholded image
    contours, hierarchy = cv2.findContours(thresholded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Draws the contours on the original image
    cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

    # Display the result
    cv2.imshow('Segmented Image', img)
    key = cv2.waitKey(0)
    if key == 13: # 13 is the ASCII code for "Enter" key
        continue # proceeds to the next image


cv2.destroyAllWindows()
