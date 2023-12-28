import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('picture/sudoku.PNG', cv.IMREAD_GRAYSCALE)
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

#affine transformation, to find the point adjust and tailor using matplot.pyplot, use cat picture
# pts1 = np.float32([[50,50],[200,50],[50,200]])
# pts2 = np.float32([[10,100],[200,50],[100,250]])
# M = cv.getAffineTransform(pts1,pts2)
# dst = cv.warpAffine(img,M,(cols,rows))

# plt.subplot(121),plt.imshow(img),plt.title('Input'), 
# plt.subplot(122),plt.imshow(dst),plt.title('Output'), plt.imshow([10,100])
# plt.show()

#perspective transformation
#using sudoku.PNG
pts1 = np.float32([[36, 39],[200,32],[20,200],[208,208]])
pts2 = np.float32([[0,0],[255,0],[0,255],[256,257]])
M = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img,M,(300,300))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()