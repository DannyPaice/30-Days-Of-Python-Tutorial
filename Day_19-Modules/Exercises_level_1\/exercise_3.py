
import json

def zoo(xs: list) -> list[dict]:
    """
    Returns a list of dictionaries with each coutry and their population
    """
    return [{'country': dic["name"], 'population': dic['population']} for dic in xs]

def most_populated_countries(num=100, filename='Day_19-Modules/countries_data.json'):
    with open(filename, "r", encoding="utf-8") as f:
        file = json.load(f)
    
    pop_dict = zoo(file)
    sorted_dict_desc = sorted(pop_dict, key=lambda x: x['population'], reverse=True)

    return sorted_dict_desc[:num]

print(most_populated_countries(3))
    





