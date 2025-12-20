
# Day 24 - Statistics

import numpy as np
print('numpy: ', np.__version__)
#print(dir(np))



# Creating int numpy arrays
python_list = [1,2,3,4,5]

# Checking data types
print('Type: ', type(python_list)) # Type: <class 'list'>

print(python_list)

two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]

print(two_dimensional_list)

# Creating Numpy(Numerical Python) array from python list
numpy_array_from_list = np.array(python_list)
print(type(numpy_array_from_list)) # <class 'numpy.ndarray'>
print(numpy_array_from_list)



# Creating float numpy arrays

# Python list
python_list2 = [1,2,3,4,5]
# Using data type parameter
numpy_array_from_list2 = np.array(python_list2, dtype=float)
print(numpy_array_from_list2) # [1. 2. 3. 4. 5.]



# Creating boolean numpy arrays
numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_bool_array) # [False  True  True False False]



# Creating multidimensional array using numpy
two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
numpy_two_dimensional_list = np.array(two_dimensional_list)
print(type(numpy_two_dimensional_list)) # <class 'numpy.ndarray'>
print(numpy_two_dimensional_list)



# Converting numpy array to list
np_to_list = numpy_array_from_list.tolist()
print(type(np_to_list)) # <class 'list'>
print('one dimensional array:', np_to_list)
print('two dimensional array: ', numpy_two_dimensional_list.tolist())




# Converting numpy array fornm tuple
python_tuple = (1,2,3,4,5)
print(type(python_tuple))

numpy_array_from_tuple = np.array(python_tuple)
print('numpy_array_from_tuple ', numpy_array_from_tuple) #numpy_array_from_tuple  [1 2 3 4 5]




# Shape of numpy array
'''
The shape method provides the shape of the array as a tuple. The first is the
row and the second is the column. If the array is just one dimensional it 
returns the size of the array.
'''

nums = np.array([1,2,3,4,5])
print(nums)
print('shape of nums: ', nums.shape)
print(numpy_two_dimensional_list)
print('shape of numpy_two_dimensional_list: ', numpy_two_dimensional_list.shape)
three_by_four_array = np.array([[2,1,2,3],
                                [4,5,6,7],
                                [8,9,10,11]])
print(three_by_four_array)
print('shape of three_by_four_array: ', three_by_four_array.shape)




# Data types of numpy array: str, int, float, complex, bool, list, None
int_lists = [-3, -2, -1, 0, 1, 2,3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)

print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)



# Size of numpy array
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0, 1, 2],
                              [3, 4, 5],
                              [6, 7, 8]])

print('The size:', numpy_array_from_list.size) # 5
print('The size:', two_dimensional_list.size)  # 3




