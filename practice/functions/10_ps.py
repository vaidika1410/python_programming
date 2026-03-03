# write docstring for a function multiply()

def multiply(a, b):
    '''this function calculates the product of two numbers and returns it
    
    parameters = a, b
    product of parameters = a * b
    '''

    return a*b

def help(doc):
    return doc.__doc__

print(help(multiply))
print(multiply(2,3))