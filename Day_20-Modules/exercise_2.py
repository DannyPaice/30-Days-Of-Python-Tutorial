
'''
Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find:
1. the min, max, mean, median, standard deviation of cats' weight in metric units.
2. the min, max, mean, median, standard deviation of cats' lifespan in years.
3. Create a frequency table of country and breed of cats
'''

import requests
import numpy as np
cats_api = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(cats_api)
cat_list = response.json()

def weight_conv(xs: str) -> int:
    '''
    converts weight 'x - y' into an a single int which is avg(x, y)
    '''
    sliced_str = xs.strip().split()
    nums = [int(sliced_str[0]), int(sliced_str[2])]
    return (nums[0] + nums[1]) / 2

def num_list_conv(cat_list) -> int:
    weight_string = [x['weight']['metric'] for x in cat_list]
    return [weight_conv(x) for x in weight_string]

def weight_stats(xs: list) -> str:
    arr = np.array(xs)
    min_weight = np.min(arr)
    max_weight = np.max(arr)
    mean_weight = np.average(arr)
    median_weight = np.median(arr)
    std_weight = np.std(arr)
    return f'''    min: {min_weight}kg,
    max: {max_weight}kg
    mean: {mean_weight}kg
    median: {median_weight}kg
    std: {std_weight}'''

cat_list_weights = num_list_conv(cat_list)
print(weight_stats(cat_list_weights))
