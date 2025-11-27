
def add_1(a):
    return a + 1

def multiply2(a):
    return a *2
    
def choose(types):
    if types == 'add_1':
        return add_1
    if types == 'multiply2':
        return multiply2
    
result = choose('multiply2')
print(result(4))

def add_12():
    num = 12
    def add(xs):
        return xs + num
    return add

closure = add_12()
print(closure(5)) 

