# Converting data types for numpy
# .astype('<data_type>') or np.array(<array>, dtype='<data_type>')

import numpy as np

# Int to float
numpy_int_arr = np.array([1,2,3,4], dtype='float')
print(numpy_int_arr)   # array([1., 2., 3., 4.])

# float to int
numpy_int_arr = np.array([1., 2., 3., 4.], dtype='int')
print(numpy_int_arr)    # array([1, 2, 3, 4])

# int to boolean
numpy_inter_array = np.array([1,2,3,4])
print(np.array(numpy_inter_array, dtype='float'))
# or with same syntax as above

# int to str
print(np.array(numpy_inter_array, dtype='str'))
# or
np_float_list = np.array([1,2,3,4], dtype='float')
print(np_float_list.astype('str'))

print(numpy_inter_array.astype('bool'))




