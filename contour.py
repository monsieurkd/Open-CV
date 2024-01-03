

import cv2 as cv 
import numpy as np
image = cv.imread('picture/contour.png')
assert image is not None, "file could not be read, bla bla"
imgray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255,  0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(imgray, contours, -1, (0,255,0), 3)
# cnt = contours[4]
# cv.drawContours(imgray, [cnt], 0, (0,255,0), 3)
cv.imshow('imgray', imgray)

#test.png return error, every value of moment return 0


cnt = contours[0]
M = cv.moments(cnt)
print( M )


#calculate centroid
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
print(cx ,cy)
#contour area
print(cv.contourArea(cnt))

#contour perimeter
print(cv.arcLength(cnt, True))

#contour approximation
epsilon = 0.1*cv.arcLength(cnt,True)
approx = cv.approxPolyDP(cnt,epsilon,True)




# cv.imshow('approx', approx)
cv.waitKey(0)