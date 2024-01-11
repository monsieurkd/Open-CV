import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('picture/cat.jpg')

blank = np.zeros(img.shape[:2], dtype= 'uint8')


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#make a mask
circle = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 200, 255, -1)


 
mask = cv.bitwise_and(gray, gray, mask=circle)


gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])
mask_hist = cv.calcHist([gray], [0], mask, [256], [0,256])

color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])


plt.figure()
plt.title("gray histogram")
plt.plot(gray_hist)
plt.plot(mask_hist)
plt.xlim([0,256])
plt.show()

cv.waitKey(0)