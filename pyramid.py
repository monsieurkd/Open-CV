# cv.pyrUp(), cv.pyrDown()
import cv2 as cv
import numpy as np

# image blending
# Load the two images of apple and orange
# Find the Gaussian Pyramids for apple and orange (in this particular example, number of levels is 6)
# From Gaussian Pyramids, find their Laplacian Pyramids
# Now join the left half of apple and right half of orange in each levels of Laplacian Pyramids
# Finally from this joint image pyramids, reconstruct the original image.

# A = cv.imread('picture/apple.png')
# B = cv.imread('picture/orange.png')
# assert A is not None, "file could not be read, check with os.path.exists()"
# assert B is not None, "file could not be read, check with os.path.exists()"
# # generate Gaussian pyramid for A
# G = A.copy()
# gpA = [G]
# for i in range(6):
#     G = cv.pyrDown(G)
#     gpA.append(G)

# print(gpA)
# # generate Gaussian pyramid for B
# G = B.copy()
# gpB = [G]
# for i in range(6):
#     G = cv.pyrDown(G)
#     gpB.append(G)

# cv.imshow('Glassus for b', gpB)

# # generate Laplacian Pyramid for A
# lpA = [gpA[5]]
# for i in range(5,0,-1):
#     GE = cv.pyrUp(gpA[i])
#     L = cv.subtract(gpA[i-1],GE)
#     lpA.append(L)

# cv.imshow('laplacian for a', lpA)

# # generate Laplacian Pyramid for B
# lpB = [gpB[5]]
# for i in range(5,0,-1):
#     GE = cv.pyrUp(gpB[i])
#     L = cv.subtract(gpB[i-1],GE)
#     lpB.append(L)

# cv.imshow('laplacian for b', lpB)

# # Now add left and right halves of images in each level
# LS = []
# for la,lb in zip(lpA,lpB):
#     rows,cols,dpt = la.shape
#     ls = np.hstack((la[:,0:cols//2], lb[:,cols//2:]))
#     LS.append(ls)

# cv.imshow('halve image', LS)

# # now reconstruct
# ls_ = LS[0]
# for i in range(1,6):
#     ls_ = cv.pyrUp(ls_)
#     ls_ = cv.add(ls_, LS[i])
# # image with direct connecting each half
# real = np.hstack((A[:,:cols//2],B[:,cols//2:]))
# cv.imwrite('Pyramid_blending2.jpg',ls_)
# cv.imwrite('Direct_blending.jpg',real)





cv.waitKey(0)
cv.destroyAllWindows()