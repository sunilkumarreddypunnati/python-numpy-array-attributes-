'''Problem: NumPy Array Attributes

Task:
Given a static NumPy array, print the following attributes in order:

Shape of the array ,Number of dimensions ,Total number of elements 
Data type of elements ,Memory size in bytes of each element 
Total memory consumed by the array

Array (Static Input):
[[2, 4, 7],
 [3, 9, 6]]

Expected Output:

Shape: (2, 3)
Number of dimensions: 2
Total elements: 6
Data type: int64
Bytes per element: 8
Total memory: 48'''

import numpy as np
arr=np.array([[2,4,7],[3,9,6]])
print("shape:",arr.shape)
print("Number of dimensions:",arr.ndim)
print("Total elements:",arr.size)
print("Data type:",arr.dtype)
print("Bytes per element:",arr.itemsize)
print("Total memory:",arr.nbytes)