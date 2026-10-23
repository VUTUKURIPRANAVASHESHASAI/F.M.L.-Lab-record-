# 1. NumPy: Creation, Operations, Indexing, and Slicing
import numpy as np

print("=== 1. ARRAY CREATION ===")
# Creating 1D and 2D arrays
arr_1d = np.array([10, 20, 30, 40, 50, 60])
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("1D Array:\n", arr_1d)
print("2D Array:\n", arr_2d)
print("Shape of 2D Array:", arr_2d.shape)

print("\n=== 2. ARRAY OPERATIONS ===")
# Element-wise operations and matrix multiplication
arr_ops = np.array([1, 2, 3])
print("Addition (+5):", arr_ops + 5)
print("Multiplication (*2):", arr_ops * 2)
print("Dot Product:", np.dot(arr_ops, arr_ops))

print("\n=== 3. INDEXING & SLICING ===")
# Accessing elements and slicing slices
print("Element at index 2 in 1D array:", arr_1d[2])
print("Slicing 1D array (index 1 to 4):", arr_1d[1:5])
print("Slicing 2D array (first 2 rows, last 2 columns):\n", arr_2d[:2, 1:])
