
# Matrix in Numpy
import numpy as np

four_by_four_matrix = np.matrix(np.ones((4,4), dtype='int'))
print(four_by_four_matrix)

np.asarray(four_by_four_matrix)[2] = 3
print(four_by_four_matrix)