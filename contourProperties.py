import numpy as np
import cv2 as cv
img = cv.imread('picture/contour.png', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
ret,thresh = cv.threshold(img,127,255,0)
contours,hierarchy = cv.findContours(thresh, 1, 2)
cnt = contours[0]
x,y,w,h = cv.boundingRect(cnt)
area = cv.contourArea(cnt)
rect_area = w*h
hull = cv.convexHull(cnt)
hull_area = cv.contourArea(hull)

aspect_ratio = float(w)/h
extent = float(area)/rect_area
solidity = float(area)/hull_area
equi_diameter = np.sqrt(4*area/np.pi)
(x,y),(MA,ma),angle = cv.fitEllipse(cnt)

mask = np.zeros(thresh.shape,np.uint8)
cv.drawContours(mask,[cnt],0,255,-1)
pixelpoints = np.transpose(np.nonzero(mask))
print(pixelpoints)
#pixelpoints = cv.findNonZero(mask)

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(thresh,mask = mask)
mean_val = cv.mean(img,mask = mask)