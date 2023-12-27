import cv2 as cv 
import numpy as np

img = cv.imread('CV2/test_image/1_A000100002001_49.png')
gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#binary threshold
threshold, thresh_img = cv.threshold(gray_image, 128, 255, cv.THRESH_BINARY)
cv.imshow("threshold img", thresh_img)

canny = cv.Canny(thresh_img, 144, 175)
cv.imshow('canny', canny)

# Define the lower and upper bounds for black color in grayscale
lower_black = 0
upper_black = 1  # Adjust this threshold as needed

# Create a mask to extract the black pixels
black_mask = cv.inRange(gray_image, lower_black, upper_black)

# Find contours in the binary mask
contours, _ = cv.findContours(black_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# Iterate through the contours and draw rectangles
for contour in contours:
    # Calculate the bounding box of the contour
    x, y, w, h = cv.boundingRect(contour)
    
    # Draw a rectangle around the contour
    cv.rectangle(gray_image, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Blue rectangle

# Display the original grayscale image with rectangles
cv.imshow('Contours and Rectangles', gray_image)
#pixel detection

#draw rectangle

#logic to remove noise

cv.waitKey(0)
