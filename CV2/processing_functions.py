import os
import numpy as np
import cv2
from sklearn.cluster import DBSCAN

# Define constants
GREEN = (0, 255, 0)
RED = (0, 0, 255)
FONT = cv2.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 0.5
FONT_THICKNESS = 1

def get_file_names(folder_path):
    file_names = []
    for file in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file)):
            file_names.append(file)
    return file_names

def calculate_minimum_rectangle(rectangles):
    min_x = min(rectangle[0] for rectangle in rectangles)
    min_y = min(rectangle[1] for rectangle in rectangles)
    max_x = max(rectangle[0] + rectangle[2] for rectangle in rectangles)
    max_y = max(rectangle[1] + rectangle[3] for rectangle in rectangles)
    width = max_x - min_x
    height = max_y - min_y
    minimum_rectangle = (min_x, min_y, width, height)
    return minimum_rectangle

def drawRectangle(img,rects):
    for idx in range(len(rects)):
        x = rects[idx][0]
        y = rects[idx][1]
        w = rects[idx][2]
        h = rects[idx][3]
        cv2.rectangle(img, (x, y), (x+w, y+h), GREEN, 1)
        cv2.putText(img, str(idx), (x, y), FONT, FONT_SCALE, RED, FONT_THICKNESS)

def drawRectangleRED(img,rects):
    for idx in range(len(rects)):
        x = rects[idx][0]
        y = rects[idx][1]
        w = rects[idx][2]
        h = rects[idx][3]
        cv2.rectangle(img, (x, y), (x+w, y+h), RED, 1)
    print("Draw successfully")

def find_overlapping_rectangles(rectangles):
    overlapping_groups = []

    # Create a list to track the group assignment for each rectangle
    group_assignments = [-1] * len(rectangles)

    # Iterate over each pair of rectangles
    for i in range(len(rectangles)):
        for j in range(i + 1, len(rectangles)):
            rect1 = rectangles[i]
            rect2 = rectangles[j]

            # Check for overlap between rectangles
            if rect1[0] < rect2[0] + rect2[2] and rect1[0] + rect1[2] > rect2[0] and rect1[1] < rect2[1] + rect2[3] and rect1[1] + rect1[3] > rect2[1]:
                # Check the group assignments of rect1 and rect2
                group1 = group_assignments[i]
                group2 = group_assignments[j]

                if group1 == -1 and group2 == -1:
                    # Both rectangles are unassigned, create a new group
                    group_id = len(overlapping_groups)
                    group_assignments[i] = group_id
                    group_assignments[j] = group_id
                    overlapping_groups.append([rect1, rect2])
                elif group1 != -1 and group2 == -1:
                    # Only rect1 is assigned, add rect2 to its group
                    group_assignments[j] = group1
                    overlapping_groups[group1].append(rect2)
                elif group1 == -1 and group2 != -1:
                    # Only rect2 is assigned, add rect1 to its group
                    group_assignments[i] = group2
                    overlapping_groups[group2].append(rect1)
                elif group1 != group2:
                    # Both rectangles are assigned to different groups, merge the groups
                    merged_group = overlapping_groups[group1] + overlapping_groups[group2]
                    for idx in range(len(merged_group)):
                        group_assignments[idx] = group1
                    overlapping_groups[group1] = merged_group

    return overlapping_groups


def find_smallest_covering_rectangle(overlapRect):
    min_x = min(rect[0] for rect in overlapRect)
    min_y = min(rect[1] for rect in overlapRect)
    max_x = max(rect[0] + rect[2] for rect in overlapRect)
    max_y = max(rect[1] + rect[3] for rect in overlapRect)
    width = max_x - min_x
    height = max_y - min_y
    return list((min_x, min_y, width, height))

def delete_subarray(main_array, sub_array):
    try:
        main_array.remove(sub_array)
    except ValueError:
        pass                                    # Subarray not found in main array
    return main_array

def find_close_rectangles2(rectangles, threshold):
    close_groups = []

    # Create a list to track the group assignment for each rectangle
    group_assignments = [-1] * len(rectangles)

    # Iterate over each pair of rectangles
    for i in range(len(rectangles)):
        for j in range(i + 1, len(rectangles)):
            rect1 = rectangles[i]
            rect2 = rectangles[j]

            # Check for closeness between rectangles
            if abs(rect1[0] + rect1[2] - rect2[0]) <= threshold or abs(rect2[0] + rect2[2] - rect1[0]) <= threshold:
                if rect1[1] < rect2[1] + rect2[3] and rect2[1] < rect1[1] + rect1[3]:
                    # Check the group assignments of rect1 and rect2
                    group1 = group_assignments[i]
                    group2 = group_assignments[j]

                    if group1 == -1 and group2 == -1:
                        # Both rectangles are unassigned, create a new group
                        group_id = len(close_groups)
                        group_assignments[i] = group_id
                        group_assignments[j] = group_id
                        close_groups.append([rect1, rect2])
                    elif group1 != -1 and group2 == -1:
                        # Only rect1 is assigned, add rect2 to its group
                        group_assignments[j] = group1
                        close_groups[group1].append(rect2)
                    elif group1 == -1 and group2 != -1:
                        # Only rect2 is assigned, add rect1 to its group
                        group_assignments[i] = group2
                        close_groups[group2].append(rect1)
                    elif group1 != group2:
                        # Both rectangles are assigned to different groups, merge the groups
                        merged_group = close_groups[group1] + close_groups[group2]
                        for idx in range(len(merged_group)):
                            try:
                                group_assignments[idx] = group1
                            except:
                                pass
                        close_groups[group1] = merged_group
    return close_groups



def filterOverlap(rectanglesToDraw):
    # Find overlapping rectangles
    overlapRects = find_overlapping_rectangles(rectanglesToDraw)
    
    # Iterate over each overlapping group
    for overlapRect in overlapRects:
        # Find the smallest covering rectangle for the group
        newRect = find_smallest_covering_rectangle(overlapRect)
        
        # Add the new covering rectangle to rectanglesToDraw
        rectanglesToDraw.append(newRect)
        
        # Remove the individual rectangles from the overlapping group
        for j in overlapRect:
            rectanglesToDraw = delete_subarray(rectanglesToDraw, j)
    
    # Return the updated rectanglesToDraw after removing overlapping rectangles
    return rectanglesToDraw


def filterClose(rectanglesToDraw, thresh):
    closes = find_close_rectangles2(rectanglesToDraw, thresh)
    for i in range(len(closes)):
        closeRects = closes[i] 
        
        newRectToAdd = find_smallest_covering_rectangle(closeRects)
        for closeRect in closeRects:
            rectanglesToDraw = delete_subarray(rectanglesToDraw, closeRect)
        rectanglesToDraw.append(newRectToAdd)
    return rectanglesToDraw

def average_horizontal_distance(rectangles):
    total_distance = 0
    count = 0

    for i in range(len(rectangles)):
        for j in range(i + 1, len(rectangles)):
            rect1 = rectangles[i]
            rect2 = rectangles[j]

            # Calculate the horizontal distance between rectangles
            distance = abs(rect1[0] + rect1[2] - rect2[0])

            total_distance += distance
            count += 1

    if count == 0:
        return 0

    average_distance = total_distance / count
    return average_distance,count
