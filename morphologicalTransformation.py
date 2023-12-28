import cv2 as cv
import numpy as np

image = cv.imread('picture/letterI.PNG')



cv.imshow('og', image)
kernel = np.ones((5,5), np.uint8)
erosion = cv.erode(image, kernel, iterations= 1)

cv.imshow('erosion', erosion)

#open is erosion followed by dilation, close is reverse
#open filter the noise outside the object, close fill the noise inside the object
opening = cv.morphologyEx(image, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(image, cv.MORPH_CLOSE, kernel)
cv.imshow('close', closing)
cv.imshow('open', opening)

#gradiant is the diff between  
gradient = cv.morphologyEx(image, cv.MORPH_GRADIENT, kernel)
cv.imshow("Gradient", gradient)

#tophat is image vs opening
tophat = cv.morphologyEx(image, cv.MORPH_TOPHAT, kernel)
cv.imshow("tophat", tophat)


#closing vs image
blackhat = cv.morphologyEx(image, cv.MORPH_BLACKHAT, kernel)
cv.imshow("blackhat", blackhat)



cv.waitKey(0)
cv.destroyAllWindows()