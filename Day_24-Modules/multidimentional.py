
# Multi-Dimensional Arrays in numpy

import numpy as np

# 2 Dimension Array
two_dimension_arr = np.array([(1,2,3), (4,5,6), (7,8,9)])
print(type(two_dimension_arr)) 
print(two_dimension_arr)
print('Shape: ', two_dimension_arr.shape)
print('Size: ', two_dimension_arr.size)
print('Data type: ', two_dimension_arr.dtype)
'''
<class 'numpy.ndarray'>
[[1 2 3]
 [4 5 6]
 [7 8 9]]
Shape:  (3, 3)
Size:  9
Data type:  int64
'''

# Getting items from a numpy array
two_dimension_arr = np.array([(1,2,3), (4,5,6), (7,8,9)])
first_row = two_dimension_arr[0]
second_row = two_dimension_arr[1]
third_row = two_dimension_arr[2]
print('First row:', first_row)
print('Second row: ', second_row)
print('Third row: ', third_row)
'''
First row: [1 2 3]
Second row:  [4 5 6]
Third row:  [7 8 9]
'''
first_column = two_dimension_arr[:,0]
second_column = two_dimension_arr[:,1]
third_column = two_dimension_arr[:,2]
print('First column:', first_column)
print('Second column: ', second_column)
print('Third column: ', third_column)
'''
First column: [1 4 7]
Second column:  [2 5 8]
Third column:  [3 6 9]
'''



