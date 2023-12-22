import cv2 as cv
import numpy as np
import sys

#find flag
flags = [i for i in dir(cv) if i.startswith('COLOR_')]
print(flags)

image_path_1 = r'picture/2.jpg'
image_path_2 = r'picture/text.jpg'

image = cv.imread(image_path_1)
image_2 = cv.imread(image_path_2)
#this is an default in opencv due to their shit but historical choice
gray = cv.cvtColor(image_2, cv.COLOR_BGR2GRAY )

cv.imshow('original ', image_2)
cv.imshow('change', gray )
print(gray.shape)
print(image_2.shape)

width, height = image.shape[:2]
print("Width: %d , Height: %d"%( width, height))  # itocv returns a tuple so we can un
cv.waitKey(0)
cv.destroyAllWindows()


