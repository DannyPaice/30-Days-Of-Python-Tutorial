# Reading from URL

'''
~ get(): to open a network and fetch data from url - it returns a response 
  object
~ status_code: After we fetched data, we can check the status of the operation 
  (success, error, etc)
~ headers: To check the header types
~ text: to extract the text from the fetched response object
~ json: to extract json data Let's read a txt file from this website,
  https://www.w3.org/TR/PNG/iso_8859-1.txt.
'''

import requests

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'

response = requests.get(url)    # opening a network and fetching a data
print(response)
print(response.status_code)     # status code, success:200
print(response.headers)         # headers information
print(response.text)            # gives all the text from the page