import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


# Load two images
# img1 = cv.imread('picture/gray.jpg')
# img2 = cv.imread('picture/pepsi.png')

# #dynamic threshold
# gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
# adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,9, 8)
# cv.imshow('thresh',adaptive_thresh )

#adaptive threshold
img = cv.imread('picture/sudoku.PNG',0)
img = cv.medianBlur(img,5)
ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
            cv.THRESH_BINARY,11,2)
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv.THRESH_BINARY,11,2)
titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()