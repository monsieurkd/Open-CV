import cv2 as cv 
import numpy as np

img = cv.imread('CV2/test_image/1_A000100002001_49.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#binary threshold
threshold, thresh_img = cv.threshold(gray, 128, 255, cv.THRESH_BINARY)
cv.imshow("threshold img", thresh_img)

canny = cv.Canny(thresh_img, 144, 175)
cv.imshow('canny', canny)

cv.waitKey(0)
