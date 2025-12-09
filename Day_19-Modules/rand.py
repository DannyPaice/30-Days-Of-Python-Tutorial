

stuff = [
{
        "name": "Afghanistan",
        "capital": "Kabul",
        "languages": [
            "Pashto",
            "Uzbek",
            "Turkmen"
        ],
        "population": 27657145,
        "flag": "https://restcountries.eu/data/afg.svg",
        "currency": "Afghan afghani"
    },
    {
        "name": "Åland Islands",
        "capital": "Mariehamn",
        "languages": [
            "Swedish"
        ],
        "population": 28875,
        "flag": "https://restcountries.eu/data/ala.svg",
        "currency": "Euro"
    },
    {
        "name": "Åland Islands",
        "capital": "Mariehamn",
        "languages": [
            "English", "English", "English"
        ],
        "population": 28875,
        "flag": "https://restcountries.eu/data/ala.svg",
        "currency": "Euro"
    }
]

country1 = stuff[0]
print(country1)

#for i in country1:
#    print(country1[i])

#print("Pashto" in country1) # False

#print("Pashto" in country1["languages"]) #true


def foo(xs: list) -> dict:
    lan_list = {}
    for dic in xs:
        for language in dic["languages"]:
            if language not in lan_list:
                lan_list[language] = 1
            else:
                lan_list[language] += 1
    return lan_list

#print(foo(stuff))



#for each dictionary, 

# for each language, 

#if the language is not in the dictionary

#add the key and value into the dictionary

#otherwise increase the value by 1




