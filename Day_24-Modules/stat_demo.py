
# Numpy and Statistics

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

normal_array = np.random.normal(79,15,80)
# print(normal_array)

print(sns.set())
print(plt.hist(normal_array, color='grey', bins=50))

