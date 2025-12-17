
'''
Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find:
1. the min, max, mean, median, standard deviation of cats' weight in metric units.
2. the min, max, mean, median, standard deviation of cats' lifespan in years.
3. Create a frequency table of country and breed of cats
'''

import requests
import numpy as np
import pandas as pd

cats_api = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(cats_api)
cat_list = response.json()

def avg_conv(xs: str) -> float:
    '''
    converts weight 'x - y' into an a single int which is avg(x, y)
    '''
    sliced_str = xs.strip().split()
    nums = [int(sliced_str[0]), int(sliced_str[2])]
    return (nums[0] + nums[1]) / 2

def num_list_conv(cat_list) -> list[float]:
    weight_string = [x['weight']['metric'] for x in cat_list]
    return [avg_conv(x) for x in weight_string]

def weight_stats(xs: list) -> str:
    arr = np.array(xs)
    min_weight = np.min(arr)
    max_weight = np.max(arr)
    mean_weight = np.average(arr)
    median_weight = np.median(arr)
    std_weight = np.std(arr)
    return f'''--- Weight Statistics ---
min: {min_weight:.2f}kg
max: {max_weight:.2f}kg
mean: {mean_weight:.2f}kg
median: {median_weight:.2f}kg
std: {std_weight:.2f}
-------------------------'''

#cat_list_weights = num_list_conv(cat_list)
#print(weight_stats(cat_list_weights))

def lifespan_list_conv(cat_list) -> list[float]:
    lifespan_string = [x['life_span'] for x in cat_list]
    return [avg_conv(x) for x in lifespan_string]

def lifespan_stats(xs: list) -> str:
    arr = np.array(xs)
    min_year = np.min(arr)
    max_year = np.max(arr)
    mean_year = np.average(arr)
    median_year = np.median(arr)
    std = np.std(arr)
    return f'''-- Life-span Statistics --
min: {min_year:.2f} years
max: {max_year:.2f} years
mean: {mean_year:.2f} years
median: {median_year:.2f} years
std: {std:.2f}
--------------------------'''

#cat_list_lifeSpans = num_list_conv(cat_list)
#print(lifespan_stats(cat_list_lifeSpans))

'''
import pandas as pd
data = pd.Series([1, 2, 5, 2, 3, 3, 3, 3, 4, 4, 5])
# Create frequency table
print(data.value_counts())
'''

def data_frame_dict(cat_list) -> dict:
    
    country_list = [x['origin'] for x in cat_list]
    breed_list = [x['name'] for x in cat_list]
    
    return {
        "country": country_list,
        "breed": breed_list
    }

def frequency_table(xs: dict):
    df = pd.DataFrame(xs)
    frequency_table = pd.crosstab(df['country'], df['breed'])
    return frequency_table

print(frequency_table(data_frame_dict(cat_list)))

