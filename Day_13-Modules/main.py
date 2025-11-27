
x = lambda x, y, z: x + y + z
#print(x(1,2,3))


#print((lambda x,y: x * y)(2, 5))

def power(x):
    return lambda n : x ** n

cube = power(2)(3)
#print(cube)

