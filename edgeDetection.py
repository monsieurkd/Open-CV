import cv2 as cv
import numpy as np
# Load two images
img1 = cv.imread('picture/gray.jpg')
img2 = cv.imread('picture/pepsi.png')
gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)

#laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('lap',lap)

sobelx = cv.Sobel(gray, cv.CV_64F, 1,0)
sobely = cv.Sobel(gray, cv.CV_64F, 0,1)
combine = cv.bitwise_or(sobelx, sobely)
cv.imshow('sobel combine', combine)
cv.imshow('sobelx', sobelx)
cv.imshow('sobely',sobely)


canny = cv.Canny(gray, 144, 175)
cv.imshow('canny', canny)
cv.waitKey(0)
cv.destroyAllWindows()