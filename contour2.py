import numpy as np
import cv2 as cv
img = cv.imread('picture/contour.png', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
ret,thresh = cv.threshold(img,127,255,0)
contours,hierarchy = cv.findContours(thresh, 1, 2)
cnt = contours[0]

M = cv.moments(cnt)
print( M )

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
print("cx, cy:", cx, cy)
area = cv.contourArea(cnt)
print("contour area: ", area)

perimeter = cv.arcLength(cnt,True)
print("contour perimeter: " ,perimeter)

epsilon = 0.1*cv.arcLength(cnt,True)
approx = cv.approxPolyDP(cnt,0.9,True)
hull = cv.convexHull(cnt)
bgr_img = cv.cvtColor(img, cv.COLOR_GRAY2RGB)
cv.drawContours(bgr_img, hull, -1, (0,255,0), 3)


print(cv.isContourConvex(cnt))

# cv.imshow("original image", img)
# cv.imshow("contour image", bgr_img)

#shape around the contour
lightning = cv.imread('picture/contour2.jpg', cv.IMREAD_GRAYSCALE)
assert lightning is not None, "file could not be read, check with os.path.exists()"
ret,thresh = cv.threshold(lightning,127,255,0)
contours,hierarchy = cv.findContours(thresh, 1, 2)
cnt = contours[0]

bgr_lightning = cv.cvtColor(lightning, cv.COLOR_GRAY2RGB)

moment = cv.moments(cnt)
print( moment )
#draw surroundding rectangle (straight rectangles)
x,y,w,h = cv.boundingRect(cnt)
cv.rectangle(bgr_lightning,(x,y),(x+w,y+h),(0,255,0),2)

#draw a rotated rectangle
rect = cv.minAreaRect(cnt)
box = cv.boxPoints(rect)
box = np.int0(box)
cv.drawContours(bgr_lightning,[box],0,(0,0,255),2)

#draw a circle
(x,y),radius = cv.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
cv.circle(bgr_lightning,center,radius,(0,255,0),2)

#draw a eclipse
ellipse = cv.fitEllipse(cnt)
cv.ellipse(bgr_lightning,ellipse,(0,255,0),2)

#fit a line
rows,cols = bgr_lightning.shape[:2]
[vx,vy,x,y] = cv.fitLine(cnt, cv.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
cv.line(bgr_lightning,(cols-1,righty),(0,lefty),(0,255,0),2)

cv.imshow("original lightning", lightning)
cv.imshow("with rectangle", bgr_lightning)



cv.waitKey(0)
