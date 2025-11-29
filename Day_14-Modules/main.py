
# higher order function example / closure
def add_1(a):
    return a + 1

def multiply2(a):
    return a *2
    
def choose(types):
    if types == 'add_1':
        return add_1
    if types == 'multiply2':
        return multiply2
    
result = choose('add_1')
print(result(4))

def add_12():
    num = 12
    def add(xs):
        return xs + num
    return add

closure = add_12()
print(closure(5)) 


# Decorator example
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@uppercase_decorator
def greeting():
    return 'Welcome to my world'

output = greeting()
print(output)

# Decorator with multiple arguments
def decorator_with_parameters(func):
    def wrapper(x, y, z):
        func(x, y, z)
        print(f"I am from {z}")
    return wrapper

@decorator_with_parameters
def print_full_name(first_name, last_name, country) -> str:
    print(f"I am {first_name} {last_name}. I love to teach.")

print_full_name('Alice', 'Doe', 'Taiwan')



# Built-in Higher Order Functions
# syntax -> map(function, iterable)

numbers = [1, 2, 3, 4, 5] #iterables
def square(x):
    return x**2
numbers_squared = map(square, numbers)
print(list(numbers_squared))

# lambda application
numbers_squared2 = map(lambda x: x**2, numbers)
print(list(numbers_squared2))

"""
Python Filter Function

The filter() function calls the specified function which returns boolean for
each item of the specified iterable (list). It filters the iterms that satisfy
the filtering criteria

syntax -> fulter(function, iterable)
"""

# Using the same numbers as above, filter for even numbers
def is_even(num) -> bool:
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))



"""
Python Reduce Function
    The reduce() function is defined inthe functools module and we should import
    it from this module. Like map and filter it takes two parameters, a func
    and an iterable. However, it does not return another iterable, instead it
    returns a single value.
"""
from functools import reduce

numbers_str = ['1', '2', '3', '4', '5'] #iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)


