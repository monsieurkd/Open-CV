import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('picture/cat.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
hist = cv.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

plt.imshow(hist,interpolation = 'nearest')
plt.show()

cv.waitKey(0)