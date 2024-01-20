import cv2 as cv 
import numpy as np

img = cv.imread('CV2/test_image/1_A000100002001_49.png')
# img = cv.imread('CV2/test_image/5_A000100006001_29.png')
# img = cv.imread('CV2/test_image/4_A000100005001_44.png')
# Load the image
# img = cv.imread('CV2/test_image/4_A000100005001_37.png')

# Convert the image to grayscale
gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Apply thresholding to create a binary image
threshold, thresh_img = cv.threshold(gray_image, 128, 255, cv.THRESH_BINARY)

# Resize the binary image for better visibility
height, width = thresh_img.shape[:2]
# thresh_img = cv.resize(thresh_img, (width * 2, height * 2))
#nếu dùng ảnh đầu tiên, comment code dòng 18 thì sẽ là xử lí ảnh bình thường và không lỗi, còn ba ảnh phía dưới đều sẽ lỗi nếu phóng to và xử lí ảnh 


# Apply dilation to fill gaps in between objects
kernel = np.zeros((5, 5), np.uint8)
dilate = cv.dilate(thresh_img, kernel, iterations=3)

# Display the thresholded and dilated images
cv.imshow('Threshold Image', thresh_img)
cv.imshow('Dilated Image', dilate)

# Apply Canny edge detection
canny = cv.Canny(thresh_img, 144, 175)
cv.imshow('Canny Edge Detection', canny)

# Apply morphological gradient
kernel = np.ones((5, 5), np.uint8)
gradient = cv.morphologyEx(canny, cv.MORPH_GRADIENT, kernel)
cv.imshow('Morphological Gradient', gradient)

# Find contours in the binary mask
contours, _ = cv.findContours(gradient, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# Convert gradient to a 3-channel image for drawing colored rectangles
gradient = cv.cvtColor(gradient, cv.COLOR_GRAY2BGR)

# Get image dimensions
height, width = gradient.shape[:2]

# Calculate bounding rectangles for each contour
bounding_rects = [cv.boundingRect(contour) for contour in contours]

# Function to check if two rectangles overlap
def rectangles_overlap(rect1, rect2):
    return (
        rect1[0] < rect2[0] + rect2[2] and
        rect1[0] + rect1[2] > rect2[0] and
        rect1[1] < rect2[1] + rect2[3] and
        rect1[1] + rect1[3] > rect2[1]
    )

# Function to merge overlapping rectangles
def merge_overlapping_rectangles(rectangles):
    merged_rectangles = []
    mark_for_deletion = []

    for i in range(len(rectangles)):
        for j in range(i + 1, len(rectangles)):
            if rectangles_overlap(rectangles[i], rectangles[j]):
                # Calculate the new bounding rectangle that includes both rectangles
                new_x = min(rectangles[i][0], rectangles[j][0])
                new_y = min(rectangles[i][1], rectangles[j][1])
                new_w = max(rectangles[i][0] + rectangles[i][2], rectangles[j][0] + rectangles[j][2]) - new_x
                new_h = max(rectangles[i][1] + rectangles[i][3], rectangles[j][1] + rectangles[j][3]) - new_y

                # Add the merged rectangle to the list
                merged_rectangles.append((new_x, new_y, new_w, new_h))
                mark_for_deletion.append(rectangles[i])
                mark_for_deletion.append(rectangles[j])

    # Remove rectangles marked for deletion
    rectangles = [rect for rect in rectangles if rect not in mark_for_deletion]

    # Add the newly created rectangles
    rectangles.extend(merged_rectangles)

    # Check if any further merging is needed
    if len(merged_rectangles) > 0:
        return merge_overlapping_rectangles(rectangles)
    else:
        return rectangles

# Call the recursive function to merge overlapping rectangles
final_rectangles = merge_overlapping_rectangles(bounding_rects)

# Draw rectangles on the original image
for location in final_rectangles:
    if location[1] + location[3] != height and location[1] != 0:
        cv.rectangle(img, (location[0], location[1]), (location[0] + location[2], location[1] + location[3]), (255, 0, 0), 2)

# Display the result
cv.imshow('Contours and Merged Rectangles', img)
cv.waitKey(0)
cv.destroyAllWindows()
