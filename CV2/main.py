import cv2 as cv 
import numpy as np

img = cv.imread('CV2/test_image/1_A000100002001_49.png')
# img = cv.imread('CV2/test_image/13_A000200001003_35.png')
gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#binary threshold
threshold, thresh_img = cv.threshold(gray_image, 128, 255, cv.THRESH_BINARY)
kernel = np.zeros((5,5), np.uint8)
dilate = cv.dilate(thresh_img, kernel, iterations= 1)
#lay net 
canny = cv.Canny(thresh_img, 144, 175)
kernel = np.ones((5,5), np.uint8)
gradient = cv.morphologyEx(canny, cv.MORPH_GRADIENT, kernel)


# Find contours in the binary mask
contours, _ = cv.findContours(gradient, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
gradient = cv.cvtColor(gradient, cv.COLOR_GRAY2BGR)

height, width = gradient.shape[:2]
bounding_rects = [cv.boundingRect(contour) for contour in contours]
print(bounding_rects[3])
# contour1 = contours[13]
# contour2 = contours[3]

# x1, y1, w1, h1 = cv.boundingRect(contour1)
# x2, y2, w2, h2 = cv.boundingRect(contour2)

# # Calculate the new bounding rectangle that surrounds both contours
# new_x = min(x1, x2)
# new_y = min(y1, y2)
# new_w = max(x1 + w1, x2 + w2) - new_x
# new_h = max(y1 + h1, y2 + h2) - new_y

# # Create a new contour based on the new bounding rectangle
# new_contour = np.array([[[new_x, new_y]], [[new_x + new_w, new_y]], [[new_x + new_w, new_y + new_h]],
#                         [[new_x, new_y + new_h]]], dtype=np.int32)

# # Optionally, draw the original contours and the new bounding rectangle on the image
# cv.drawContours(gradient, [contour1, contour2], -1, (0, 255, 0), 2)
# cv.drawContours(gradient, [new_contour], -1, (0, 0, 255), 2)

# # Display the result
# cv.imshow('Concatenated Contours', gradient)

edge_detection = [] # a list of nearby contour need to be merge
mark_for_deletion = []
for i in range(len(bounding_rects)):
    for j in range(i + 1, len(bounding_rects)):
        #logic for nearby contour
        if (
                bounding_rects[i][0]< bounding_rects[j][0] + bounding_rects[j][2] and
                bounding_rects[i][0] + bounding_rects[i][2] +5> bounding_rects[j][0] and
                bounding_rects[i][1]< bounding_rects[j][1] + bounding_rects[j][3] and
                bounding_rects[i][1] + bounding_rects[i][3] +5> bounding_rects[j][1]
            ):     
            x1, y1, w1, h1 = bounding_rects[i][0],  bounding_rects[i][1],  bounding_rects[i][2],  bounding_rects[i][3],
            x2, y2, w2, h2 =  bounding_rects[j][0],  bounding_rects[j][1],  bounding_rects[j][2],  bounding_rects[j][3],

# Calculate the new bounding rectangle that surrounds both contours
            new_x = min(x1, x2)
            new_y = min(y1, y2)
            new_w = max(x1 + w1, x2 + w2) - new_x
            new_h = max(y1 + h1, y2 + h2) - new_y

# Create a new contour based on the new bounding rectangle
            new_rect = (new_x, new_y, new_w, new_h)
            edge_detection.append(new_rect)

                #    x = min(x, x_other)
#                 y = min(y, y_other)
#                 w = max(x + w, x_other + w_other) - x
#                 h = max(y + h, y_other + h_other) - y

new_edge_detection =  list(dict.fromkeys(edge_detection))#remove the duplicate using dict.fromkeys()


# my_tuple = new_edge_detection[0]

for location in  new_edge_detection:

    if location[1] + location[3] != height : #logic to remove the lower edge letter
    # Draw a rectangle around the contour
        cv.rectangle(gradient, (location[0], location[1]), (location[0]+location[2], location[1]+location[3]), (255, 0, 0), 2)  # Blue rectangle
    

# Display the original grayscale image with rectangles
cv.imshow('Contours and Rectangles', gradient)



#logic to remove noise

cv.waitKey(0)
