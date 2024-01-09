import numpy as np
import cv2 as cv

# Read image in grayscale mode
img = cv.imread('picture/contour.png', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"

# Convert image to binary using Otsu's method
ret, thresh = cv.threshold(img, 127, 255, 0)

# Find contours in the binary image
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

# Access the first contour
cnt = contours[0]

# Get bounding rectangle for the contour
x, y, w, h = cv.boundingRect(cnt)

# Calculate contour area
area = cv.contourArea(cnt)

# Calculate bounding rectangle area
rect_area = w * h

# Find convex hull for the contour
hull = cv.convexHull(cnt)
cv.drawContours(img, hull, -1, (0,255,0), 2 )
cv.imshow('img', img)

# Calculate hull area
hull_area = cv.contourArea(hull)

# Calculate contour's aspect ratio
aspect_ratio = float(w) / h

# Calculate contour's extent
extent = float(area) / rect_area

# Calculate contour's solidity
solidity = float(area) / hull_area

# Calculate contour's equivalent diameter
equi_diameter = np.sqrt(4 * area / np.pi)

# Fit an ellipse around the contour
(x, y), (MA, ma), angle = cv.fitEllipse(cnt)

# Create a mask for the contour
mask = np.zeros(thresh.shape, np.uint8)
cv.drawContours(mask, [cnt], 0, 255, -1)

# Find all the pixel points inside the contour
pixelpoints = np.transpose(np.nonzero(mask))

# Calculate the minimum and maximum values within the contour, as well as their locations
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(thresh, mask=mask)

# Calculate the mean value of the pixel points within the contour
mean_val = cv.mean(img, mask=mask)


cv.waitKey(0)