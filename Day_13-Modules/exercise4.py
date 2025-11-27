
"""
Flatten outr the following list to a new list
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
"""

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

def rand_func2(stuff):
    return [[xs[0].upper(), xs[0][:3].upper(), xs[1].upper()] for lists in stuff for xs in lists]

print(rand_func2(countries))