from functools import reduce

def cube(x):
    return int(x) ** 3
digits = '123'
cubed_digits = map(cube, digits)
total = reduce(lambda x, y: x + y, cubed_digits)
print(total)