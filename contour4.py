import cv2 as cv
import numpy as np
#ready for ocr
img1 = cv.imread('picture/handwritten1.jpg', cv.IMREAD_GRAYSCALE)
img2 = cv.imread('picture/number1.jpg', cv.IMREAD_GRAYSCALE)
height, width = img1.shape[:2]
cv.imshow('img1', img1)


img2 = cv.resize(img2, (height//5, width//3))
cv.imshow('img2', img2)

assert img1 is not None, "file could not be read, check with os.path.exists()"
assert img2 is not None, "file could not be read, check with os.path.exists()"
ret, thresh = cv.threshold(img1, 127, 255,0)
ret, thresh2 = cv.threshold(img2, 127, 255,0)
contours1,hierarchy = cv.findContours(thresh,2,1)
cnt = contours1[0]
contours2,hierarchy = cv.findContours(thresh2,2,1)
cnt2 = contours2[0]
ret = cv.matchShapes(cnt,cnt2,1,0.0)
print( ret )



# hull = cv.convexHull(cnt,returnPoints = False)
# #returnPoints = False for the return value to be the point for the convex hull(normally it would be the contour point position in the contour)
# defects = cv.convexityDefects(cnt,hull)
# for i in range(defects.shape[0]):
#     s,e,f,d = defects[i,0]
#     start = tuple(cnt[s][0])
#     end = tuple(cnt[e][0])
#     far = tuple(cnt[f][0])
#     cv.line(img1,start,end,[0,255,0],2)
#     cv.circle(img1,far,5,[0,0,255],-1)
# cv.imshow('img',img1)

# dist = cv.pointPolygonTest(cnt,(50,50),True)
# print('distance to the contour', dist)


cv.waitKey(0)
cv.destroyAllWindows()