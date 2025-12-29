
# Pandas in Python


'''
Panda data structures is based on Series and DataFrames

A series is a column and a DataFrame is a multidimensional table made up of
collection of series.
'''

import pandas as pd
import numpy as np

# Creating Panda Series with Default Index
nums = [1,2,3,4,5]
s = pd.Series(nums)
print(s)


# Creatiang Pandas Series with custome Index
nums = [1,2,3,4,5]
s = pd.Series(nums, index=[1,2,3,4,5])
print(s)


# Creating Pandas Series from a Dictionary
dct = {'name': 'Daniel', 'country': 'Australia', 'city': 'Melbourn'}

s = pd.Series(dct)
print(s)

# Creating a COnstant Pandas Series
s = pd.Series(10, index=[1,2,3])
print(s)


# Creating a Pandas Series Using linspace
s = pd.Series(np.linspace(5, 20, 10)) # linspace(<starting>, <end>, <items>)
print(s)