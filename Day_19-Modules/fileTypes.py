'''
Docstring for Day_19-Modules.fileTypes

JSON Files ~ looks like a string form of a dictionary
'''




# dictionary
"""
person_dct= {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}
"""

"""
#JSON
person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''
"""

import json

#Changing JSON to Dictionary (loads)
person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''

person_dct = json.loads(person_json)
print(type(person_dct))     #dct
print(person_dct)           #prints dictionary
print(person_dct['name'])




#Changing Disctionary to JSON (dumps)
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# lets convert to JSON
person2_json = json.dumps(person, indent=2) # indent can be 2, 4, 8
print(type(person2_json))
print(person2_json)



# Saving as JSON File
person2 = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
with open("Day_19-Modules/example3.json", "w", encoding='utf-8') as f:
    json.dump(person2, f, ensure_ascii=False, indent=4)














