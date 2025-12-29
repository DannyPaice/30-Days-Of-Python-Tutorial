
# Modiying a Dataframe
'''
- We can create a new DataFrame
- We can create a new column and add it to the DataFrame
- We can remove an existing column from a DataFrame
- We can modify an existing column in a DataFrame
- We can change the datatype of column values in the DataFrame
'''
import pandas as pd
import numpy as np

# Creating a DataFrame
data = [
    {"Name": "Asabeneh", "Country":"Finland","City":"Helsinki"},
    {"Name": "David", "Country":"UK","City":"London"},
    {"Name": "John", "Country":"Sweden","City":"Stockholm"}
]
df = pd.DataFrame(data)
print(df)


# Adding a new column, Lets add weights column
weights = [74, 78, 69]
df['Weight'] = weights
print(df)

df['Height'] = [173, 175, 169]
print(df)


# Modifying column Values
df['Height'] = df["Height"] * 0.01
print(df)

def calculate_bmi():
    weights = df['Weight']
    heights = df['Height']
    bmi = []
    for w,h in zip(weights, heights):
        b = w/(h*h)
        bmi.append(b)
    return bmi

bmi = calculate_bmi()

df['BMI'] = bmi
print(df)

birth_year = ['1769', '1985', '1990']
df['Birth Year'] = birth_year



# Formatting DataFrame Columns
df["BMI"] = round(df["BMI"], 1)
print(df.head())


# Checking data types of column values
print(df.Weight.dtype)
print(df['Birth Year'].dtype)

df["Birth Year"] = df["Birth Year"].astype('int')
print(df["Birth Year"].dtype)


# Boolean Indexing
print(df[df['Height'] > 1.7])