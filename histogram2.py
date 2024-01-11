import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('picture/cat.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "image is not found"

equ = cv.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
cv.imwrite('res.png',res)

# the numpy way
hist, bins = np.histogram(img.flatten(), 256, [0,256])

cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()

cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m,0).astype('uint8')
img2 = cdf[img]

cv.imshow('img', img)
cv.imshow('img2 after equalization', img2)

plt.plot(cdf, color = 'g')
plt.hist(img2.flatten(),256, [0,256], color = 'r' )
plt.xlim([0,256])
plt.legend(('cdf modified?', 'histogram'), loc = 'upper left')

plt.figure()

plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256, [0,256], color = 'r' )
plt.xlim([0,256])
plt.legend(('cdf real','cdf', 'histogram'), loc = 'upper left')
plt.show()


cv.waitKey(0)

