import numpy as np
import cv2 as cv
# Create a black image
img = np.zeros((512,512,3), np.uint8)
# Draw a diagonal blue line with thickness of 5 px
cv.line(img,(0,0),(511,511),(255,0,0),5)
cv.rectangle(img, (0,0), (128,128 ), (0, 255, 0), 3, 1)
cv.circle(img, (256, 256), 68, (255, 0, 0) , 3, 4)
cv.ellipse(img,(256,256),(100,50),0,360,180,255,1)
print(np.array([1,2,2,3,3,3,3,3,3,3]).reshape(-1, 2,5))
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))

cv.imshow("black", img)
cv.waitKey(0)
