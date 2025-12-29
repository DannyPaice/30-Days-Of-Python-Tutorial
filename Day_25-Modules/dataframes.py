
# DataFrames
import pandas as pd
import numpy as np



# Creating DataFramse from List of Lists
data = [
    ['Asabeneh', 'Finland', 'Helsink'], 
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
df = pd.DataFrame(data, columns=['Names', 'Country', 'City'])
print(df)


# Creating DataFrame Using Dictionary
data = {
    'Name': ['Asabeneh', 'David', 'John'],
    'Country':['Finland', 'UK', 'Sweden'],
    'City': ['Helsiki', 'London', 'Stockholm']
}
df = pd.DataFrame(data)

