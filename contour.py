# import numpy as np
# import cv2 as cv
# im = cv.imread('test.jpg')
# assert im is not None, "file could not be read, check with os.path.exists()"
# imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
# ret, thresh = cv.threshold(imgray, 127, 255, 0)
# contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

import cv2 as cv 
import numpy as np
image = cv.imread('picture/noisy2.PNG')
assert image is not None, "file could not be read, bla bla"
imgray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255,  0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(imgray, contours, -1, (0,0,255), 3)
# cnt = contours[4]
# cv.drawContours(imgray, [cnt], 0, (0,255,0), 3)
cv.imshow('imgray', imgray)


cv.waitKey(0)