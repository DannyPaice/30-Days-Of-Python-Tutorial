
# Generating random numbers
import numpy as np


# Generate a random float number
random_float = np.random.random()
print(random_float)

# Generate a random float number
random_floats = np.random.random(5)
print(random_floats) # array([0.26392192, 0.35842215, 0.87908478, 0.41902195, 0.78926418])

# Generating a random integer between 0 and 10
random_int = np.random.randint(0, 11)
print(random_int)

# Generating random integers between 2 and 11, and creating a one row array
random_ints = np.random.randint(2, 10, size=4)
print(random_ints)

# Generating a random integers between 0 and 10 in a multi-d array
random_ints_2d = np.random.randint(0, 10, size=(3, 3))
print(random_ints_2d)




# Generating Random Numbers

# np.random.normal(mu, sigma, size)
normal_array = np.random.normal(79, 15, 80)
print(normal_array)


