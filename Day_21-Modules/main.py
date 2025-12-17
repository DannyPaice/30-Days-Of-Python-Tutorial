# Day 21 Classes and Objects

'''
Syntax:
class ClassName:
    code goes here...
'''

class Person:
    pass

print(Person)

'''
Creating an Object:
'''

p = Person()
print(p)

'''
Class Constructor

The init constructor function has a self parameter which is a reference to the
current instance of the class
'''
class Person2:
    def __init__(self, name):
        # self allows to attach parameter to the class
        self.name = name

p = Person2('Daniel')
print(p.name)
print(p)

class Person3:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

p3 = Person3('Daniel', 'Paice', '19', 'Australia', 'Brisbane')
print(p3.country)


# Object Methods
class Person4:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
    
    def person_info(self):
        return f"{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}"

p4 = Person4('Daniel', 'Paice', '19', 'Australia', 'Brisbane')
print(p4.person_info())
    


