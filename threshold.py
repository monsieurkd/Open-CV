import cv2 as cv
# Load two images
img1 = cv.imread('picture/gray.jpg')
img2 = cv.imread('picture/pepsi.png')

#dynamic threshold
gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,9, 8)
cv.imshow('thresh',adaptive_thresh )



cv.waitKey(0)
cv.destroyAllWindows()