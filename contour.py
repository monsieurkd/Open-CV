

import cv2 as cv 
import numpy as np
image = cv.imread('picture/contour.jpg')
assert image is not None, "file could not be read, bla bla"
imgray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255,  0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

image_contour = cv.cvtColor(imgray, cv.COLOR_GRAY2RGB)

cv.drawContours(image_contour, contours, -1, (0,255,0), 1)
# cnt = contours[4]
# cv.drawContours(imgray, [cnt], 0, (0,255,0), 3)
cv.imshow('image with contour', image_contour)
print(len(contours))
#test.png return error, every value of moment return 0
cnt = contours[0]
M = cv.moments(cnt)


#calculate centroid
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
print(cx ,cy)
#contour area
print(cv.contourArea(cnt))

#contour perimeter
print(cv.arcLength(cnt, False))

#contour approximation
epsilon = 0.000000001*cv.arcLength(cnt,True)
approx = cv.approxPolyDP(cnt,0.001,True)

cv.imshow('i', image)

cv.drawContours(image, approx, -1, (0,255,0), 3)
cv.imshow('img', image)
cv.waitKey(0)