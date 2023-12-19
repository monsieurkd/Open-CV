import cv2 as cv
import numpy as np
import sys

#find flag
flags = [i for i in dir(cv) if i.startswith('COLOR_')]
print(flags)

image_path_1 = r'2.jpg'
image_path_2 = r'3.jpg'

image = cv.imread(image_path_2)

#this is an default in opencv due to their shit but historical choice
gray = cv.cvtColor(image, cv.COLOR_BGR2RGB )

cv.imshow('original ', image)
cv.imshow('change', gray )
cv.waitKey(0)
cv.destroyAllWindows()


