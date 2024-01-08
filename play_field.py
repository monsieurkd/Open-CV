# import numpy as np

# # Create two arrays
# array1 = np.array([[1, 2], [3, 4]])
# array2 = np.array([[5, 6]])

# # Concatenate along axis 0 (rows)
# result = np.concatenate((array1, array2))
# array3 = array1 + array2

# print("Array 1:")
# print(array1)
# print("\nArray 2:")
# print(array2)
# print("\nConcatenated Result along axis 0:")
# print(array3)

my_list = [1, 2, 3, 4, 5]

# Indices of the elements you want to concatenate
index1 = 1
index2 = 3

# Concatenate the selected elements
concatenated_result = my_list[index1] + my_list[index2]

# Replace the original elements with the concatenated result
my_list[index1:index2 + 1] = [concatenated_result]

print(my_list)

