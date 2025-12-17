'''
Scrape the following website and store the data as json file
url = 'https://www.bu.edu/president/boston-university-facts-stats/'
'''

import requests
from bs4 import BeautifulSoup
import json


url = 'https://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
#print(soup.prettify())

#stat-label, stat-figure
output_data = {}
sections = soup.find_all('section', class_='stat-section')

for section in sections:
    group_title = section.find('h4', class_='stat-group-title').get_text(strip=True)
    output_data[group_title] = {}

    stats = section.find_all('li')
    for stat in stats:
        label = stat.find('span', class_='stat-label').get_text(strip=True)
        figure = stat.find('span', class_='stat-figure').get_text(strip=True)

        output_data[group_title][label] = figure

#bu-stat-title, bu-stat-value-field

print(output_data)

with open('Day_22-Modules/campus_stats.json', 'w', encoding='utf-8') as f:
    json.dump(output_data, f, indent=4)
