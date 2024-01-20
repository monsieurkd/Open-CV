import cv2
import processing_functions as func
import numpy as np

# Define constants
GREEN = (0, 255, 0)
RED = (0, 0, 255)
FONT = cv2.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 0.5
FONT_THICKNESS = 1

# Create a kernel for erosion
# [ 1,
#   1,
#   1 ]
kernel = np.ones((3, 1), dtype=np.uint8)            

# Get file names of test images
file_names = func.get_file_names("CV2/test_image")

# Process each image
for file_name in file_names:
    # Load the input image
    image = cv2.imread("CV2/test_image/" + file_name)
    print(file_name)

    # Resize the image to a larger size
    height, width = image.shape[:2]
    size = height * width
    # resized = cv2.resize(image, (width * 7, height * 2))

    # Convert the resized image to grayscale
    resized = image
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    # Apply binary thresholding
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Smooth the thresholded image using erosion
    smoothened = cv2.erode(thresh, kernel, iterations=1)

    # Find contours in the smoothened image
    contours, hierarchies = cv2.findContours(smoothened, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on the smoothened image
    cv2.drawContours(smoothened, contours, -1, RED, 1)

    # Prepare a list to store valid rectangles
    rectanglesToDraw = []

    # Process each contour
    for i in range(len(contours)):
        # Calculate the area of the contour
        area = cv2.contourArea(contours[i])

        # Filter out contours based on area
        if area < size and area > (size * 0.005):
            # Obtain the bounding rectangle coordinates
            x, y, w, h = cv2.boundingRect(contours[i])

            # Adjust the coordinates based on image resizing
            # x = int(x / 7)
            # y = int(y / 2)
            # w = int(w / 7)
            # h = int(h / 2)

            # Filter out undesired rectangles
            if w < width and x > 0 and y < (height * 0.9):
                rectanglesToDraw.append([x, y, w, h])

    # Calculate a threshold value
    thresh = size / 32000

    # Filter rectangles based on overlap, closeness, and overlap again
    rectanglesToDraw = func.filterOverlap(rectanglesToDraw)
    rectanglesToDraw = func.filterClose(rectanglesToDraw, thresh)
    rectanglesToDraw = func.filterOverlap(rectanglesToDraw)

    # Draw the filtered rectangles on the original image
    func.drawRectangle(image, rectanglesToDraw)

    # Save the resulting image
    cv2.imwrite("./results" + file_name, image)

    # Display the image and wait for a key press
    cv2.waitKey(0)
    cv2.destroyAllWindows()