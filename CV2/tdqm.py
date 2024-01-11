import concurrent.futures
from tqdm import tqdm
import cv2 as cv
import numpy as np
from main import process_image
# Create a global variable to store the images
images = []

def process_image_for_images(image_path):
    img = cv.imread(image_path)
    # height, width = img.shape[:2]
    # resize_img = cv.resize(img, (width//2, height//2))
    processed_img = process_image(img)
    images.append((f'Original - {image_path}', processed_img))

# List of input image paths
image_paths = [
    "CV2/test_image/1_A000100002001_49.png",
    "CV2/test_image/1_A000100002001_50.png",
    "CV2/test_image/2_A000100003001_9.png",
    "CV2/test_image/2_A000100003001_21.png",
    
    
    "CV2/test_image/5_A000100006001_29.png",
    "CV2/test_image/13_A000200001003_4.png",
    
]  # 6 is the maximum the computer can take

image_paths_produce_error = ["CV2/test_image/4_A000100005001_37.png", "CV2/test_image/4_A000100005001_44.png"]
# Function to process images using ThreadPoolExecutor
def process_images_parallel(image_paths):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Using a list to store futures
        futures = [executor.submit(process_image_for_images, path) for path in image_paths]

        # tqdm is used to display a progress bar for the futures
        for _ in tqdm(concurrent.futures.as_completed(futures), total=len(futures)):
            pass

# Run the image processing in parallel
process_images_parallel(image_paths)

# Create a single window and display all images
for title, img in images:
    cv.imshow(title, img)

# Wait for a key press and close the window
cv.waitKey(0)
cv.destroyAllWindows()
