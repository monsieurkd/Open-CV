
# Access pixel values and modify them
# Access image properties
# Set a Region of Interest (ROI)
# Split and merge images

import numpy as np
import cv2 as cv
img = cv.imread('gray.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"

# accessing RED value
print(img.item(10,10,2))

# modifying RED value
img.itemset((10,10,2),100)
# print(img.item(10,10,2))
# print(img.shape, img.size)


#image blending
img1 = cv.imread('landscape.jfif')
img2 = cv.imread('gray.jpg')
print(img1.size, img2.size)
assert img1 is not None, "file could not be read, check with os.path.exists()"
assert img2 is not None, "file could not be read, check with os.path.exists()"
dst = cv.addWeighted(img1,0.5,img2,0.5,0)
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()