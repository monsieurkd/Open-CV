import cv2 as cv

# image_path = r'picture/text.jpg'
# image = cv.imread(image_path)
# cv.imshow('original', image)

# average = cv.blur(image, (3,3))
# cv.imshow("Average", average)

# gauss = cv.GaussianBlur(image, (3,3), 0)
# cv.imshow("gauss", gauss)

# median = cv.medianBlur(image, 3)
# cv.imshow("Median", median)

# bilateral = cv.bilateralFilter(image, 5, 35, 25)
# cv.imshow("bilater", bilateral)


#bitwise operation
# Load two images
img1 = cv.imread('picture\starry_night.png')
img2 = cv.imread('picture\gray.jpg', cv.IMREAD_GRAYSCALE)
# assert img1 is not None, "file could not be read, check with os.path.exists()"
# assert img2 is not None, "file could not be read, check with os.path.exists()"
# # I want to put logo on top-left corner, So I create a ROI
# rows,cols = img2.shape
# roi = img1[0:rows, 0:cols]
# cv.imshow('d', roi)
# # Now create a mask of logo and create its inverse mask also
# ret, mask = cv.threshold(img2, 10, 255, cv.THRESH_BINARY)
# mask_inv = cv.bitwise_not(mask)
# # Now black-out the area of logo in ROI
# img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
# cv.imshow('d',img1_bg)
# # Take only region of logo from logo image.
# img2_fg = cv.bitwise_and(img2,img2,mask = mask)
# # Put logo in ROI and modify the main image
# dst = cv.add(img1_bg,img2_fg)
# img1[0:rows, 0:cols ] = dst

#bilateral is gaussian blur but consider the edge with function of pixel difference
blur = cv.bilateralFilter(img2,9,75,75)

cv.imshow('og',img2)

cv.imshow('blur',blur)


cv.waitKey(0)
cv.destroyAllWindows()