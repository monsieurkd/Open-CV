import cv2 as cv
import numpy as np
import os



def get_file_names(folder_path):
    file_names = []
    for file in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file)):
            file_names.append(file)
    return file_names

def process_image_for_rectangle(img):
    '''
    process an image and return the same image with letter dectection using contour 
    Input: a Matlike image 
    Output: a MatLike image with rectangle
    '''
    gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

   
    threshold, thresh_img = cv.threshold(gray_image, 128, 255, cv.THRESH_BINARY)
    kernel = np.zeros((5, 5), np.uint8)
    dilate = cv.dilate(thresh_img, kernel, iterations=1)
    canny = cv.Canny(thresh_img, 144, 175)
    kernel = np.ones((5, 5), np.uint8)
    gradient = cv.morphologyEx(dilate, cv.MORPH_GRADIENT, kernel)

    # Find contours in the binary mask
    contours, _ = cv.findContours(gradient, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    gradient = cv.cvtColor(gradient, cv.COLOR_GRAY2BGR)

    height, width = gradient.shape[:2]
    bounding_rects = [cv.boundingRect(contour) for contour in contours]
    bounding_rects = [location for location in bounding_rects if (location[1] + location[3] != height and location[1] != 0 and location[0] != 0) ]
    return bounding_rects

    # A function to check if two rectangles overlap
def rectangles_overlap(rect1, rect2, threshold=0):
    return (
        (rect1[0] < rect2[0] + rect2[2]  and
        rect1[0] + rect1[2] > rect2[0] and
        rect1[1] < rect2[1] + rect2[3]  and
        rect1[1] + rect1[3]  > rect2[1])

    
    )

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

    print('merged_rectangele', merged_rectangles)
    print('mark for deletion', mark_for_deletion)
    
    # Remove rectangles marked for deletion
    rectangles = [rect for rect in rectangles if rect not in mark_for_deletion]

    # Add the newly created rectangles
    rectangles.extend(merged_rectangles)
    print('rectangle', rectangle)
    # Check if any further merging is needed
    # if  len(merged_rectangles) >0:
    #     return merge_overlapping_rectangles(rectangles)
    # else: 
    return rectangles





# Draw rectangles on the image
def draw_rectangle(img, rectangle):   
    height, width = img.shape[:2]
    for location in rectangle:
        
        cv.rectangle(img, (location[0], location[1]), (location[0] + location[2], location[1] + location[3]), (255, 0, 0), 2)
    return img

# Process each image and display the result
# img = cv.imread('CV2/test_image/4_A000100005001_44.png')
# img = cv.imread('CV2/test_image/1_A000100002001_50.png')
# img = cv.imread('CV2/test_image/4_A000100005001_37.png')

# img = cv.imread('CV2/test_image/13_A000200001003_35.png')

# Get file names of test images
file_names = get_file_names("CV2/test_image")

image_paths_produce_error = ["CV2/test_image/4_A000100005001_37.png", "CV2/test_image/4_A000100005001_44.png"]

# Process each image
for file_name in file_names:
    # Load the input image
    img = cv.imread("CV2/test_image/" + file_name)
    print(file_name)


    height, width = img.shape[:2]
    img = cv.resize(img, (width*2, height*2))
    
    rectangle = process_image_for_rectangle(img)
    rectangle = merge_overlapping_rectangles(rectangle)
    rectangle = merge_overlapping_rectangles(rectangle)
    rectangle = merge_overlapping_rectangles(rectangle)




    processed_image = draw_rectangle(img, rectangle)

    cv.imwrite("./results" + file_name, img)
    
    cv.waitKey(0)


    cv.destroyAllWindows()



