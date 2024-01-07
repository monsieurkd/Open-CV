import cv2 as cv 
import numpy as np

img = cv.imread('CV2/test_image/1_A000100002001_49.png')
# img = cv.imread('CV2/test_image/13_A000200001003_35.png')
gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#binary threshold
threshold, thresh_img = cv.threshold(gray_image, 128, 255, cv.THRESH_BINARY)

kernel = np.zeros((5,5), np.uint8)
dilate = cv.dilate(thresh_img, kernel, iterations= 1)

cv.imshow('dilate', dilate)

#lay net 
canny = cv.Canny(thresh_img, 144, 175)
cv.imshow('canny', canny)




kernel = np.ones((5,5), np.uint8)

gradient = cv.morphologyEx(canny, cv.MORPH_GRADIENT, kernel)
cv.imshow("Gradient", gradient)


# Find contours in the binary mask
contours, _ = cv.findContours(gradient, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
gradient = cv.cvtColor(gradient, cv.COLOR_GRAY2BGR)

height, width = gradient.shape[:2]
bounding_rects = [cv.boundingRect(contour) for contour in contours]


edge_detection = [] # a list of nearby contour need to be merge
for i in range(len(bounding_rects)):
    for j in range(i + 1, len(bounding_rects)):
        #logic for nearby contour
        if (
                bounding_rects[i][0]< bounding_rects[j][0] + bounding_rects[j][2] and
                bounding_rects[i][0] + bounding_rects[i][2] +5> bounding_rects[j][0] and
                bounding_rects[i][1]< bounding_rects[j][1] + bounding_rects[j][3] and
                bounding_rects[i][1] + bounding_rects[i][3] +5> bounding_rects[j][1]
            ):     
            edge_detection.append(bounding_rects[i])
            edge_detection.append(bounding_rects[j])       
new_edge_detection =  list(dict.fromkeys(edge_detection))#remove the duplicate using dict.fromkeys()


my_tuple = new_edge_detection[0]

distant = [tuple(x - y for x, y in zip(my_tuple, other_tuple)) for other_tuple in new_edge_detection]

print(distant)

for location in  new_edge_detection:

    if location[1] + location[3] != height :
    # Draw a rectangle around the contour
        cv.rectangle(gradient, (location[0], location[1]), (location[0]+location[2], location[1]+location[3]), (255, 0, 0), 1)  # Blue rectangle
    

# Display the original grayscale image with rectangles
cv.imshow('Contours and Rectangles', gradient)



#logic to remove noise

cv.waitKey(0)
