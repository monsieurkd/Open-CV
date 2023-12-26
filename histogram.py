import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('picture/cat.jpg')
cv.imshow("Original Image", img)

blank = np.zeros(img.shape[:2], dtype= 'uint8')


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

circle = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 200, 255, -1)
cv.imshow('circle', circle)


 
mask = cv.bitwise_and(gray, gray, mask=circle)

cv.imshow('mask', mask)

gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])
mask_hist = cv.calcHist([gray], [0], mask, [256], [0,256])


plt.figure()
plt.title("gray histogram")
plt.plot(gray_hist)
plt.plot(mask_hist)
plt.xlim([0,256])
plt.show()

cv.waitKey(0)