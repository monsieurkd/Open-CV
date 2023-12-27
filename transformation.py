import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('picture/cat.jpg', cv.IMREAD_GRAYSCALE)
cv.imshow('original', img)

# height, weight = image.shape[:2]
# res = cv.resize(image, (2*weight, 2*height), interpolation=cv.INTER_CUBIC)
# cv.imshow('res', res)


rows,cols = img.shape
# M = np.float32([[1,0,100],[0,1,50]])
# dst1 = cv.warpAffine(image,M,(cols,rows))
# cv.imshow('img',dst1)

# M1 = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
#in getRotationMatrix2D: center, angle, size 
# dst = cv.warpAffine(image,M1,(cols,rows))
# cv.imshow('something',dst)

#affine transformation
#how to find this 3 point i have no idea
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv.getAffineTransform(pts1,pts2)
dst = cv.warpAffine(img,M,(cols,rows))

plt.subplot(121),plt.imshow(img),plt.title('Input'), plt.plot(pts1, 'bo')
plt.subplot(122),plt.imshow(dst),plt.title('Output'), plt.plot(pts2, 'bo')
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()