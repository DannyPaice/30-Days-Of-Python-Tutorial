

# Reading CSV file using pandas

import pandas as pd


df = pd.read_csv('Day_25-Modules/weight-height.csv')
#print(df)

print(df.head(10)) # give five rows, can increase rows by passing argument
print(df.tail(10))

print(df.shape) #(1000, 3)

print(df.columns)

heights = df['Height']
print(heights)


# describe() method provides a descriptive statistical values of a dataset
print(heights.describe())