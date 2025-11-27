
"""
Change the following lists of lists to a list of concatenated strings

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output
['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
"""

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

def foo(rand):
    return [f"{name[0]} {name[1]}" for lists in rand for name in lists]

print(foo(names))