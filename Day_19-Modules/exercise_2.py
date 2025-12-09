
# Read the countries_data.json file and create a function that finds the ten
# most spoken languages

import json

def foo(xs: list) -> dict:
    lan_list = {}
    for dic in xs:
        for language in dic["languages"]:
            if language not in lan_list:
                lan_list[language] = 1
            else:
                lan_list[language] += 1
    return lan_list


def most_spoken_languages(num=100, filename='Day_19-Modules/countries_data.json'):
    with open(filename, "r", encoding="utf-8") as f:
        file = json.load(f)
    
    lan_dict = foo(file)
    sorted_items_desc = sorted(lan_dict.items(), key=lambda item: item[1], reverse=True)
    sorted_dict_desc = dict(sorted_items_desc)
    
    sort_list = [(value, key) for key, value in sorted_dict_desc.items()]
    return sort_list[:num]

print(most_spoken_languages(20))
