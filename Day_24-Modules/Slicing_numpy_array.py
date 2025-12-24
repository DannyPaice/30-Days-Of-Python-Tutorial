
# Slicing Numpy Array
import numpy as np

two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_two_rows_and_columns = two_dimension_array[0:2, 0:2]
print(first_two_rows_and_columns)
'''
[[1 2]
 [4 5]]
'''

# Reversing the rows and the whole array
print(two_dimension_array[::])
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''
print(two_dimension_array[::-1])
'''
[[7 8 9]
 [4 5 6]
 [1 2 3]]
'''
print(two_dimension_array[::-1, ::-1])
'''
[[9 8 7]
 [6 5 4]
 [3 2 1]]
'''


# Represent missing values
two_dimension_array[1,1] = 55
two_dimension_array[1,2] = 44
print(two_dimension_array)
'''
[[ 1  2  3]
 [ 4 55 44]
 [ 7  8  9]]
'''

# Numpy Zeros
# np.zeros(shape, dtype=float, order='C')
numpy_zeros = np.zeros((3,3), dtype='int', order='C')
print(numpy_zeros)

# Numpy ones
numpy_ones = np.ones((3,3), dtype=int, order='C')
print(numpy_ones)
'''
[[1 1 1]
 [1 1 1]
 [1 1 1]]
'''

twos = numpy_ones *2
print(twos)






# Reshaping arrays
# numpy.reshape(), numpy.flatten()
first_shape = np.array([(1,2,3), (4,5,6)])
print(first_shape)
reshaped = first_shape.reshape(3,2)
print(reshaped)
'''
[[1 2 3]
 [4 5 6]]

[[1 2]
 [3 4]
 [5 6]]
'''
flattened = reshaped.flatten()
print(flattened)    # [1 2 3 4 5 6]


# Horizonbtal Stack
np_list_one = np.array([1,2,3])
np_list_two = np.array([4,5,6])

print(np_list_one + np_list_two) # [5 7 9]
print('Horizontal Append: ', np.hstack((np_list_one, np_list_two)))
# [1 2 3 4 5 6]


# Vertical Stack
print('Vertical Append: ', np.vstack((np_list_one, np_list_two)))
'''
Vertical Append:  [[1 2 3]
[4 5 6]]
'''



