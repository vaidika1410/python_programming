# positional arguments

def add(a, b):
    return a + b

print(add(2, 4))


# default arguments
def product(a, b, plus=1):
    return a * b * plus

print(product(3, 5))
print(product(3, 5, 2)) # the value of plus will be overridden


# keyword aguments
print(add(b=10, a=14)) # this is useful if the order of aguments change